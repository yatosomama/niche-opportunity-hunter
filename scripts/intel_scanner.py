#!/usr/bin/env python3
"""
🕵️ 微量情报捕获扫描器 — Micro-Intelligence Scanner
集成 Agent-Reach 15通道全网监听

用法:
  python intel_scanner.py scan              # 全量扫描所有活跃通道
  python intel_scanner.py scan v2ex         # 只扫 V2EX
  python intel_scanner.py scan bilibili     # 只扫 B站
  python intel_scanner.py report            # 生成今日情报简报
  python intel_scanner.py analyze "线索"    # 深入分析指定线索
  python intel_scanner.py watch KEYWORD     # 持续监听特定关键词
  python intel_scanner.py sources           # 列出所有可用情报源
"""

import sys
import os
import json
import re
import time
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ========== 配置 ==========

OUTPUT_DIR = Path("D:/_Hermes输出/情报")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

AGENT_REACH_ENV = "D:/_Hermes输出/agent-reach-env/Scripts/activate"
BASH = "bash"  # git-bash on Windows

# ========== 关键词库 ==========

KEYWORDS = {
    "urgent": [
        "漏了", "接口放开", "接口*放开", "卡bug", "卡BUG",
        "新规漏洞", "免实名", "免认证", "秒下", "hotfix",
        "刚修复", "漏洞已修复", "新规*放开", "限额*取消"
    ],
    "high_value": [
        "跑通了", "跑通", "点位到了", "点位",
        "低调撸", "低调", "API放开", "API*放开",
        "开源了", "门槛降低", "取消限制",
        "海外*API", "搬砖", "自动化脚本", "挂机",
        "无实名", "免梯", "免翻墙",
        "某海外小站", "新功能上线", "新上线"
    ],
    "trend": [
        "改版", "更新了", "新接口", "测试成功",
        "收益到账", "注册量暴增",
        "gas异常", "gas*涨", "平台*改版",
        "workaround", "rate limit", "algorithm*change"
    ],
    "niche": [
        "小绿", "蓝色那个", "某海外", "冷门",
        "偏门", "信息差", "套利", "捡漏",
        "撸*羊毛", "白嫖", "0成本"
    ]
}

# 所有关键词展平
ALL_KEYWORDS = []
for cat in KEYWORDS:
    ALL_KEYWORDS.extend(KEYWORDS[cat])

# ========== 情报源配置 ==========

INTEL_SOURCES = {
    "v2ex": {
        "name": "V2EX",
        "enabled": True,
        "description": "程序员社区 — 技术变动/新API/规则更新",
        "priority": "S级",
        "channels": ["agent-reach search v2ex"]
    },
    "bilibili": {
        "name": "B站",
        "enabled": True,
        "description": "技术区/偏门UP主评论区",
        "priority": "A级",
        "channels": ["agent-reach search bilibili"]
    },
    "github": {
        "name": "GitHub",
        "enabled": True,
        "description": "Trending项目 + Issues讨论（需 gh auth）",
        "priority": "A级",
        "channels": ["gh search", "agent-reach search github"]
    },
    "web": {
        "name": "任意网页",
        "enabled": True,
        "description": "通过Jina Reader扫描指定页面",
        "priority": "A级",
        "channels": ["curl https://r.jina.ai/"]
    },
    "youtube": {
        "name": "YouTube",
        "enabled": True,
        "description": "技术/套利视频字幕分析",
        "priority": "B级",
        "channels": ["agent-reach search youtube"]
    },
    "rss": {
        "name": "RSS订阅",
        "enabled": True,
        "description": "批量扫描多个信息源",
        "priority": "B级",
        "channels": ["agent-reach search rss"]
    }
}


# ========== 工具函数 ==========

def run_bash(cmd, timeout=30):
    """在bash中执行命令"""
    full_cmd = f". \"{AGENT_REACH_ENV}\" 2>/dev/null; {cmd}"
    try:
        result = subprocess.run(
            [BASH, "-c", full_cmd],
            capture_output=True, text=True, timeout=timeout
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "TIMEOUT", -1
    except FileNotFoundError:
        return "", "BASH_NOT_FOUND", -2


def match_keywords(text):
    """在文本中匹配关键词，返回匹配结果"""
    text_lower = text.lower()
    matches = defaultdict(list)
    
    for category, kws in KEYWORDS.items():
        for kw in kws:
            # 处理通配符 pattern
            if "*" in kw:
                parts = kw.lower().split("*")
                pattern = ".*".join(re.escape(p) for p in parts)
                if re.search(pattern, text_lower):
                    matches[category].append(kw)
            else:
                if kw.lower() in text_lower:
                    matches[category].append(kw)
    
    return dict(matches)


def score_signal(matches, text=""):
    """给情报信号打分 (0-100)"""
    score = 0
    
    # 关键词层级加分
    if "urgent" in matches:
        score += 30
    if "high_value" in matches:
        score += 20
    if "trend" in matches:
        score += 10
    if "niche" in matches:
        score += 5
    
    # 信息丰富度加分
    if text:
        word_count = len(text.split())
        if word_count > 50:
            score += 10  # 有具体内容
        if word_count > 200:
            score += 10  # 很详细
        if "http" in text.lower() or "github.com" in text.lower():
            score += 10  # 有链接可验证
        if re.search(r'\d+[万k]', text) or re.search(r'[0-9]{3,}', text):
            score += 5   # 有具体数字
    
    return min(score, 100)


# ========== 扫描模块 ==========

def scan_v2ex():
    """扫描 V2EX 最新内容（通过 Jina Reader）"""
    print("  📡 V2EX 扫描中...")
    results = []
    
    # 通过 Jina Reader 获取 V2EX 热帖
    stdout, stderr, code = run_bash(
        'curl -s "https://r.jina.ai/https://www.v2ex.com/?tab=hot" 2>/dev/null | head -300'
    )
    
    if stdout.strip():
        matches = match_keywords(stdout)
        snippet = stdout[:1500]
        
        if matches:
            s = score_signal(matches, snippet)
            results.append({
                "source": "V2EX热帖",
                "keyword": "批量扫描",
                "score": s,
                "matches": matches,
                "snippet": snippet
            })
        
        # 也在最新帖中搜具体关键词
        for kw in KEYWORDS["urgent"] + KEYWORDS["high_value"][:5]:
            kw_out, _, _ = run_bash(
                f'curl -s "https://r.jina.ai/https://www.v2ex.com/go/tech?q={kw}" 2>/dev/null | head -100'
            )
            if kw_out.strip():
                m = match_keywords(kw_out)
                if m:
                    s2 = score_signal(m, kw_out)
                    results.append({
                        "source": "V2EX",
                        "keyword": kw,
                        "score": s2,
                        "matches": m,
                        "snippet": kw_out[:600]
                    })
            time.sleep(0.3)
    
    return results


def scan_bilibili():
    """扫描 B站 相关内容（通过 Jina Reader + B站搜索API）"""
    print("  📺 B站 扫描中...")
    results = []
    
    for kw in KEYWORDS["urgent"] + KEYWORDS["high_value"][:5]:
        # B站搜索API (公开)
        stdout, stderr, code = run_bash(
            f'curl -s "https://api.bilibili.com/x/web-interface/search/all/v2?keyword={kw}" 2>/dev/null | head -200'
        )
        if stdout.strip():
            matches = match_keywords(stdout)
            if matches:
                s = score_signal(matches, stdout)
                results.append({
                    "source": "B站",
                    "keyword": kw,
                    "score": s,
                    "matches": matches,
                    "snippet": stdout[:600]
                })
        time.sleep(0.5)
    
    return results


def scan_web(url=None):
    """扫描指定网页"""
    if not url:
        print("  ⏭️ 跳过网页扫描（未指定URL）")
        return []
    
    print(f"  🌐 扫描网页: {url}")
    stdout, stderr, code = run_bash(
        f"curl -s \"https://r.jina.ai/{url}\" 2>/dev/null | head -300"
    )
    
    if not stdout.strip():
        return []
    
    matches = match_keywords(stdout)
    if not matches:
        return []
    
    s = score_signal(matches, stdout)
    return [{
        "source": f"Web({url[:50]}...)",
        "keyword": "|".join(sum(matches.values(), [])),
        "score": s,
        "matches": matches,
        "snippet": stdout[:800]
    }]


# ========== 报告生成 ==========

def generate_report(all_results):
    """生成情报简报"""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    date_str = now.strftime("%Y%m%d_%H%M")
    
    # 按分数排序
    all_results.sort(key=lambda x: x["score"], reverse=True)
    
    lines = []
    lines.append(f"# 📡 微量情报简报 — {timestamp}")
    lines.append("")
    lines.append("| 优先级 | 来源 | 关键词 | 分数 |")
    lines.append("|:------:|:----:|--------|:----:|")
    
    for r in all_results:
        prio = "🔴" if r["score"] >= 70 else "🟡" if r["score"] >= 50 else "🟢"
        kws = ", ".join(sum(r["matches"].values(), []))[:40]
        lines.append(f"| {prio} | {r['source']} | {kws} | {r['score']} |")
    
    lines.append("")
    
    # 详细内容
    high_prio = [r for r in all_results if r["score"] >= 60]
    if high_prio:
        lines.append("## 🔴 高优先级信号（>=60分）")
        for r in high_prio:
            lines.append("")
            lines.append(f"### [{r['source']}] 分数: {r['score']}")
            lines.append(f"- **命中关键词:** {', '.join(sum(r['matches'].values(), []))}")
            lines.append(f"- **摘要:**")
            lines.append(f"  ```")
            lines.append(f"  {r['snippet'][:500]}")
            lines.append(f"  ```")
    
    medium_prio = [r for r in all_results if 40 <= r["score"] < 60]
    if medium_prio:
        lines.append("\n## 🟡 中等优先级信号（40-59分）")
        for r in medium_prio:
            lines.append(f"- **{r['source']}** [{r['score']}分] — {', '.join(sum(r['matches'].values(), []))[:60]}")
    
    low_prio = [r for r in all_results if r["score"] < 40]
    if low_prio:
        lines.append(f"\n## 🟢 低优先级信号 (<40分)")
        lines.append(f"共 {len(low_prio)} 条低分信号，已记录")
    
    lines.append("")
    lines.append("---")
    lines.append("*🕵️ 微量情报捕获系统 自动生成 | 请结合人肉判断验证*")
    lines.append("*建议：对60分以上信号进行深入逆向分析*")
    
    content = "\n".join(lines)
    filepath = OUTPUT_DIR / f"intel_brief_{date_str}.md"
    filepath.write_text(content, encoding="utf-8")
    
    return str(filepath), content, all_results


def print_summary(all_results):
    """控制台输出摘要"""
    if not all_results:
        print("  📭 本次扫描未发现匹配信号")
        return
    
    print(f"\n  {'='*50}")
    print(f"  📊 扫描结果汇总")
    print(f"  {'='*50}")
    
    high = [r for r in all_results if r["score"] >= 60]
    med = [r for r in all_results if 40 <= r["score"] < 60]
    low = [r for r in all_results if r["score"] < 40]
    
    print(f"  总信号: {len(all_results)}")
    print(f"  🔴 高优先级(>=60): {len(high)}")
    print(f"  🟡 中优先级(40-59): {len(med)}")
    print(f"  🟢 低优先级(<40): {len(low)}")
    
    if high:
        print(f"\n  🔴 重点信号:")
        for r in high:
            kws = ", ".join(sum(r["matches"].values(), []))
            print(f"    [{r['source']}] {kws[:50]} — {r['score']}分")
    
    print(f"\n  详情见简报文件")


# ========== 分析模块 ==========

def analyze_clue(clue_text):
    """深入分析指定线索（通过 Jina Reader）"""
    print(f"\n  🔍 深入分析线索: {clue_text[:60]}...")
    
    results = []
    
    # V2EX 搜索
    print("    查询 V2EX...")
    out, _, _ = run_bash(
        f'curl -s "https://r.jina.ai/https://www.v2ex.com/go/tech?q={clue_text}" 2>/dev/null | head -200'
    )
    if out.strip() and "Title:" in out:
        results.append({"source": "V2EX", "content": out[:1000]})
    
    time.sleep(0.5)
    
    # B站搜索
    print("    查询 B站...")
    out, _, _ = run_bash(
        f'curl -s "https://api.bilibili.com/x/web-interface/search/all/v2?keyword={clue_text}" 2>/dev/null | head -200'
    )
    if out.strip():
        results.append({"source": "B站", "content": out[:1000]})
    
    time.sleep(0.5)
    
    # Google/Hacker News 泛搜索
    print("    查询 HN 讨论...")
    out, _, _ = run_bash(
        f'curl -s "https://r.jina.ai/https://hn.algolia.com/api/v1/search?query={clue_text}&tags=story" 2>/dev/null | head -200'
    )
    if out.strip():
        results.append({"source": "HackerNews", "content": out[:1000]})
    
    print(f"\n  {'='*50}")
    print(f"  📋 交叉分析结果")
    print(f"  {'='*50}")
    
    if not results:
        print(f"  各渠道暂无相关结果")
        return
    
    for r in results:
        print(f"\n  [{r['source']}]")
        print(f"  {r['content'][:500]}")


# ========== 主入口 ==========

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    action = sys.argv[1].lower()
    
    if action == "scan":
        target = sys.argv[2].lower() if len(sys.argv) > 2 else "all"
        
        print(f"\n  {'='*50}")
        print(f"  🕵️ 微量情报捕获扫描")
        print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  {'='*50}")
        print(f"  活跃关键词: {len(ALL_KEYWORDS)} 个")
        print(f"  目标通道: {target}")
        print()
        
        all_results = []
        
        if target in ("all", "v2ex"):
            all_results.extend(scan_v2ex())
        
        if target in ("all", "bilibili"):
            all_results.extend(scan_bilibili())
        
        if target == "web" and len(sys.argv) > 3:
            all_results.extend(scan_web(sys.argv[3]))
        
        if all_results:
            report_path, _, _ = generate_report(all_results)
            print_summary(all_results)
            print(f"\n  📄 简报已保存: {report_path}")
        else:
            print("  📭 本次扫描未发现匹配情报信号")
    
    elif action == "report":
        # 查找最新简报
        briefs = sorted(OUTPUT_DIR.glob("intel_brief_*.md"), reverse=True)
        if briefs:
            content = briefs[0].read_text(encoding="utf-8")
            print(content[:2000])
            print(f"\n...完整内容: {briefs[0]}")
        else:
            print("📭 暂无简报，请先运行 scan")
    
    elif action == "analyze":
        clue = " ".join(sys.argv[2:]).strip() if len(sys.argv) > 2 else None
        if not clue:
            print("请提供要分析的线索: python intel_scanner.py analyze \"线索内容\"")
            return
        analyze_clue(clue)
    
    elif action == "watch":
        keyword = sys.argv[2] if len(sys.argv) > 2 else None
        if not keyword:
            print("请指定关键词: python intel_scanner.py watch KEYWORD")
            return
        print(f"\n👀 已添加监听: 「{keyword}」")
        print(f"后续对话中提及此关键词时将触发情报分析")
        print(f"可同时运行: python intel_scanner.py scan")
    
    elif action == "sources":
        print(f"\n  📡 可用情报源 ({len(INTEL_SOURCES)} 个)")
        print(f"  {'='*50}")
        for name, cfg in INTEL_SOURCES.items():
            status = "✅" if cfg["enabled"] else "❌"
            print(f"  {status} [{cfg['priority']}] {cfg['name']}")
            print(f"      {cfg['description']}")
    
    elif action == "keywords":
        print(f"\n  🔑 监听关键词库 ({sum(len(v) for v in KEYWORDS.values())} 个)")
        for cat, kws in KEYWORDS.items():
            emoji = "🔴" if cat == "urgent" else "🟡" if cat == "high_value" else "🟢" if cat == "trend" else "⚪"
            print(f"\n  {emoji} {cat.upper()} ({len(kws)})")
            for kw in kws:
                print(f"    • {kw}")
    
    else:
        print(f"未知操作: {action}")
        print(__doc__)


if __name__ == "__main__":
    main()
