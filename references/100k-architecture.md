# 🏗️ 10万源精准快扫架构 — 软硬件一体方案

> 用开源工具搭建专业情报管道：
> 10万源 → 自动过滤 → AI分析 → 每日3分钟精准简报

---

## 一、核心架构

```
         RSSHub (45K⭐)               Crawlee (24K⭐)
         「万物皆可RSS」              「深度爬取」
              │                            │
              ▼                            ▼
         ┌─────────────────────────────────────┐
         │         FreshRSS (15K⭐)             │
         │   聚合所有RSS Feed → 统一管理        │
         └─────────────────────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────────┐
         │       Huginn (49K⭐)                 │
         │   Agent监控 → 关键词过滤 → 去重      │
         │   ┌──────────────────────────────┐   │
         │   │Agent 1: RSS监控员             │   │
         │   │Agent 2: 关键词过滤器          │   │
         │   │Agent 3: 变动通知员            │   │
         │   │Agent 4: 跨源交叉验证         │   │
         │   └──────────────────────────────┘   │
         └─────────────────────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────────┐
         │   Changedetection.io (32K⭐)         │
         │   1000+页面关键词实时监控             │
         └─────────────────────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────────┐
         │        SearXNG (32K⭐)               │
         │  同时搜索70+引擎                     │
         │  → 主动发现新情报                    │
         └─────────────────────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────────┐
         │     n8n (194K⭐) + Dify (147K⭐)      │
         │  AI工作流 → LLM分析 → 可信度评分     │
         │  → 知识库(RAG) → 每日简报生成        │
         └─────────────────────────────────────┘
                      │
                      ▼
         ┌─────────────────────────────────────┐
         │         📋 精准简报                  │
         │   每天10条精华信号                    │
         │   每条含：来源/价值/可信度/操作建议   │
         └─────────────────────────────────────┘
```

---

## 二、推荐的10个GitHub工具

| # | 工具 | ⭐Stars | 做什么 | 为什么必装 |
|:-:|------|:-------:|--------|-----------|
| 1 | **Huginn** | 49K | Agent自动化平台 | **🔥 核心大脑** — 创建Agent自动监控/过滤/聚合/通知。10万源管理中枢 |
| 2 | **n8n** | 194K | AI工作流引擎 | **🔥 AI分析层** — 接入LLM，自动分析情报、评分、生成简报 |
| 3 | **RSSHub** | 45K | 万物皆可RSS | **🔥 源倍增器** — 300+网站转RSS，一个路由配N个参数=N个源 |
| 4 | **Changedetection.io** | 32K | 网页变动监控 | **🔥 精准监控** — 监控1000+页面，关键词变动立即通知 |
| 5 | **SearXNG** | 32K | 自建元搜索引擎 | **🔥 主动发现** — 同时搜70+搜索引擎，发现新情报源 |
| 6 | **Dify** | 147K | AI知识库平台 | 情报存入知识库，RAG方式快速检索 |
| 7 | **FreshRSS** | 15K | RSS聚合器 | 统一管理海量RSS订阅 |
| 8 | **Crawlee** | 24K | 爬虫框架 | 深度爬取反爬严格的站点 |
| 9 | **FastGPT** | 28K | 知识库+RAG | 用AI分析情报并生成报告 |
| 10 | **ArchiveBox** | 27K | 网页存档 | 自动存档发现的每条情报 |

---

## 三、如何做到10万源

```
不用手写10万个URL，而是跑RSSHub路由展开：

1个路由模板 × N个参数值 = N个情报源

示例：
  /twitter/user/:id       × 500个人       = 500个
  /telegram/channel/:user × 500个频道     = 500个
  /reddit/:subreddit      × 2000个板块    = 2,000个
  /bilibili/user/video/:uid × 1000个UP主  = 1,000个
  /youtube/channel/:id    × 1000个频道    = 1,000个
  /medium/:user           × 500个作者     = 500个
  /substack/:id           × 1000个newsletter = 1,000个
  /weibo/user/:id         × 500个大V      = 500个
  /zhihu/topic/:topicId   × 300个话题     = 300个
  FreshRSS批量导入OPML    × 8000个RSS    = 8,000个
  RSSHub自动发现          × 自己发现      = 8,000个
  全球新闻站模板          × 2000个        = 2,000个
  Twitter关键词搜索       × 500个关键词   = 500个
  SearXNG搜索引擎查询      × 700个查询     = 700个
  Changedetection监控      × 2000个页面    = 2,000个
  Huginn Agent自动发现     × 不限          = 不断增长
  ──────────────────────────────────────────────
  总计：轻松达到100,000+
```

---

## 四、精准过滤流水线（这才是关键）

> 10万源 = 海量数据，必须用AI流水线过滤才有用。

```
┌─────────────────────────────────────────────────┐
│  Step 1: 关键词初筛                              │
│  Huginn Agent自动匹配200个核心关键词              │
│  过滤率：95% → 10万条原始变5千条候选              │
├─────────────────────────────────────────────────┤
│  Step 2: 可信度粗评                              │
│  n8n + LLM 快速评分（0-100）                     │
│  过滤率：80% → 5千条变1千条高价值                 │
├─────────────────────────────────────────────────┤
│  Step 3: 交叉验证                                │
│  Huginn Agent跨源比对 → 多源一致才保留            │
│  过滤率：70% → 1千条变300条可信                   │
├─────────────────────────────────────────────────┤
│  Step 4: AI深度分析                              │
│  Dify + LLM RAG分析 → 价值分类+操作建议           │
│  过滤率：90% → 300条变30条精华                    │
├─────────────────────────────────────────────────┤
│  Step 5: 人工精选                                │
│  最后30条 → 你花3分钟看一遍 → 选Top10             │
│  输出：每日精准简报10条                          │
└─────────────────────────────────────────────────┘

📊 效率数据
───────────────
10万条原始 → 5万条有内容 → 5千条匹配关键词
→ 1千条高价值 → 300条可信 → 30条精华 → 10条简报
───────────────
从10万到10条，过滤精度99.99%
```

---

## 五、推荐安装方案

### 方案A：轻量版（今天就能装）

```bash
# 1. Huginn — 核心Agent引擎（Docker一键）
docker run -d --name huginn \
  -p 3000:3000 \
  -v huginn-data:/var/lib/mysql \
  huginn/huginn

# 2. Changedetection.io — 关键词监控
docker run -d --name changedetection \
  -p 5000:5000 \
  -v changedetection-data:/datastore \
  dgtlmoon/changedetection.io

# 3. SearXNG — 元搜索
docker run -d --name searxng \
  -p 4000:8080 \
  -v searxng-data:/etc/searxng \
  searxng/searxng
```

### 方案B：完整版（推荐）

```bash
# RSSHub — 源倍增器
docker run -d --name rsshub -p 1200:1200 diygod/rsshub

# FreshRSS — RSS聚合
docker run -d --name freshrss -p 8080:80 freshrss/freshrss

# Huginn — 智能Agent
docker run -d --name huginn -p 3000:3000 huginn/huginn

# Changedetection — 变动监控
docker run -d --name changedetection -p 5000:5000 dgtlmoon/changedetection.io

# SearXNG — 元搜索
docker run -d --name searxng -p 4000:8080 searxng/searxng

# n8n — AI工作流
docker run -d --name n8n -p 5678:5678 n8nio/n8n

# Dify — 知识库+AI分析
docker run -d --name dify -p 3001:3001 langgenius/dify
```

---

## 六、与现有Hermes Skill联动

```
现有micro-intel-capture + precision-quick-scan
            ↓
     Huginn / Changedetection / SearXNG
            ↓
     n8n + Dify AI 分析
            ↓
     每日精准简报 → 喂回Agent
            ↓
     "快扫一下今天有什么"
     直接输出10条精华
```

---

> **方案版本 1.0** | 建议先装方案A（Huginn + Changedetection + SearXNG）
> 三件套Docker 5分钟装好，10万源架构直接落地
