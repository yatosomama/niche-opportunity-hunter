# 📡 全网情报源大全 — 1000+ Sources Reference

> 本文件收录 1000+ 个可监控的情报源，涵盖 30+ 大类。
> 每个源标注：名称 / 类型 / 访问方式 / 价值说明
> 实时更新，可配合 intel_scanner.py 使用。

---

## 目录

```
一、爬虫引擎 (15)
二、中文论坛 (26)
三、中文新闻媒体 (50)
四、国际/封锁新闻 (45)
五、电视/广播直播流 (20)
六、视频平台频道 (40)
七、短视频平台 (12)
八、代码仓库 (10)
九、国际社区/论坛 (35)
十、社交网络 (15)
十一、即时通讯/群组 (20)
十二、学术/研究 (40)
十三、专利/知识产权 (10)
十四、RSS订阅源 (80)
十五、RSSHub 路由 (120)
十六、博客/个人站 (50)
十七、Newsletter/邮件 (30)
十八、播客 (30)
十九、维基/百科 (8)
二十、政府/监管 (25)
二十一、金融/市场 (25)
二十二、招聘/就业 (12)
二十三、问答/知识 (15)
二十四、电商/商品 (15)
二十五、APP/应用商店 (12)
二十六、设计/创意 (10)
二十七、安全/漏洞 (15)
二十八、数据库/数据集 (15)
二十九、API/开发者工具 (18)
三十、网盘/资源 (10)
三十一、暗网/深网 (8)
三十二、邮件列表/Group (12)
三十三、期刊/杂志 (25)
三十四、会议/活动 (12)
三十五、导航/聚合站 (15)
三十六、其他冷门源 (50)
```

---

## 一、⚙️ 爬虫工具引擎 (15)

| # | 工具 | 用途 | 状态 | 价值 |
|:-:|------|------|:----:|------|
| 1 | Jina Reader (r.jina.ai) | 任意网页读取，突破反爬/封锁 | ✅ | 核心引擎 |
| 2 | Playwright | 浏览器自动化，渲染JS页面 | 🔧 | 复杂页面 |
| 3 | Scrapy | Python爬虫框架，批量采集入库 | 🔧 | 规模化 |
| 4 | BeautifulSoup4 | HTML/XML解析，灵活提取 | 🔧 | 精细解析 |
| 5 | newspaper3k | 文章自动提取(标题/作者/日期/正文) | 🔧 | 新闻专用 |
| 6 | trafilatura | 高精度网页正文提取 | 🔧 | 正文提取 |
| 7 | Readability | Mozilla阅读模式算法 | 🔧 | 正文提取 |
| 8 | Common Crawl | 全球网页存档(数十亿页) | 🔧 | 历史数据 |
| 9 | Archive.org (Wayback) | 查看已删除/变更的历史页面 | 🔧 | 信息溯源 |
| 10 | Google Cache | 读取谷歌缓存的网页快照 | 🔧 | 封锁绕过 |
| 11 | RSS/Atom Parser | 订阅更新，批量监控 | ✅ | 自动化 |
| 12 | Telegram Bot API | TG频道/群组消息实时采集 | 🔧 | 实时情报 |
| 13 | Webhook | 实时回调通知 | 🔧 | 即时推送 |
| 14 | curl + Platform API | 各平台公开API直接调用 | ✅ | 基础能力 |
| 15 | Selenium | 复杂交互页面爬取 | 🔧 | 深度爬取 |

---

## 二、🏛️ 中文论坛社区 (26)

| # | 名称 | 核心价值 | 类型 | 优先级 |
|:-:|------|---------|:----:|:-----:|
| 1 | V2EX (v2ex.com) | 程序员/创业/技术红利信号 | 综合技术 | 🔴 S |
| 2 | 吾爱破解 (52pojie.cn) | 逆向工程/偏门技巧/技术交流 | 安全技术 | 🔴 S |
| 3 | Hostloc (hostloc.com) | 主机/VPS/跨境/网赚圈核心 | 站长 | 🔴 S |
| 4 | Nodeseek (nodeseek.com) | 云服务/节点/代理技术 | 技术 | 🔴 S |
| 5 | A5站长论坛 (bbs.admin5.com) | 站长圈/流量/变现/SEO | 站长 | 🟡 A |
| 6 | 落伍者 (im286.com) | 最老牌站长/网赚社区 | 站长 | 🟡 A |
| 7 | 开源中国 (oschina.net) | 开源项目/技术讨论 | 技术 | 🟡 A |
| 8 | 掘金 (juejin.cn) | 前沿技术/偏门技术栈 | 技术 | 🟡 A |
| 9 | SegmentFault (segmentfault.com) | 技术问答/疑难线索 | 技术 | 🟡 A |
| 10 | 博客园 (cnblogs.com) | 深度技术博客/实战分享 | 技术 | 🟡 A |
| 11 | CSDN (csdn.net) | 国内最大技术社区 | 技术 | 🟡 A |
| 12 | IT之家 (ithome.com) | 科技资讯/数码/软硬件 | 科技 | 🟡 A |
| 13 | 酷安 (coolapk.com) | 数码/APP/搞机/玩机 | 数码 | 🟡 A |
| 14 | 少数派 (sspai.com) | 效率工具/方法论 | 效率 | 🟡 A |
| 15 | 知乎 (zhihu.com) | 深度问答/行业/技术/职业 | 知识 | 🟢 B |
| 16 | 豆瓣 (douban.com) | 兴趣小组/冷门圈层 | 兴趣 | 🟢 B |
| 17 | 天涯 (tianya.cn) | 综合/卧虎藏龙 | 综合 | 🟢 B |
| 18 | 凯迪社区 (kdnet.net) | 时政/深度讨论 | 时政 | 🟢 B |
| 19 | 龙空论坛 (lkong.com) | 网络文学/版权/网文变现 | 文学 | 🟢 B |
| 20 | 贴吧 (tieba.baidu.com) | 垂直细分吧(网赚/淘客/AI) | 兴趣 | 🔴 S |
| 21 | 水木社区 (newsmth.net) | 清华系/创业讨论 | 高校 | 🟢 B |
| 22 | Hi-PDA (hi-pda.com) | 数码极客圈 | 数码 | 🟢 B |
| 23 | 国学论坛 (guoxue.com) | 传统文化/冷门知识 | 文化 | 🟢 B |
| 24 | LowEndTalk (lowendtalk.com) | 低配VPS/廉价服务器 | 国际 | 🟡 A |
| 25 | DigitalPoint (digitalpoint.com) | 国际站长/SEO/变现 | 国际 | 🟡 A |
| 26 | WebmasterWorld (webmasterworld.com) | 搜索引擎/算法变动 | 国际 | 🟢 B |

---

## 三、📰 中文新闻媒体 (50)

### 综合科技 (12)
| # | 媒体 | 价值 | 特有内容 |
|:-:|------|------|---------|
| 1 | 虎嗅 (huxiu.com) | 商业/科技深度 | 独家行业内幕 |
| 2 | 36氪 (36kr.com) | 创业/投融资 | 新项目首发报道 |
| 3 | 品玩 (pingwest.com) | 科技商业新锐 | 硅谷视角 |
| 4 | 差评 (chaping.cn) | 科技热评 | 大众化解读 |
| 5 | 钛媒体 (tmtpost.com) | 科技财经 | 深度产业分析 |
| 6 | 爱范儿 (ifanr.com) | 数字生活/科技产品 | 产品测评 |
| 7 | 极客公园 (geekpark.net) | 极客文化/创新 | 创新产品报道 |
| 8 | 动点科技 (technode.com) | 中英文科技 | 国际视角中文科技 |
| 9 | 机器之心 (jiqizhixin.com) | AI/机器学习 | 技术前沿 |
| 10 | 量子位 (qbitai.com) | AI/人工智能 | 行业动态 |
| 11 | 新智元 (aiera.com.cn) | AI/智能 | 行业观察 |
| 12 | 雷锋网 (leiphone.com) | 科技/智能硬件 | 硬件前沿 |

### 门户科技 (10)
| 13 | 新浪科技 (tech.sina.com.cn) | 综合科技资讯 |
| 14 | 网易科技 (tech.163.com) | 综合科技资讯 |
| 15 | 腾讯科技 (tech.qq.com) | 综合科技资讯 |
| 16 | 搜狐科技 (it.sohu.com) | 综合科技资讯 |
| 17 | 凤凰网科技 (tech.ifeng.com) | 综合科技资讯 |
| 18 | 人民网科技 (scitech.people.com.cn) | 官方科技资讯 |
| 19 | 新华网科技 (xinhuanet.com/tech) | 官方科技 |
| 20 | 央视网科技 (tech.cctv.com) | 官方科技 |
| 21 | 环球网科技 (tech.huanqiu.com) | 国际科技视角 |
| 22 | 观察者网科技 (guancha.cn) | 深度评论 |

### 财经商业 (12)
| 23 | 第一财经 (yicai.com) | 财经商业深度 |
| 24 | 财新网 (caixin.com) | 财经深度调查 |
| 25 | 界面新闻 (jiemian.com) | 财经/商业 |
| 26 | 每日经济新闻 (nbd.com.cn) | 财经资讯 |
| 27 | 财经网 (caijing.com.cn) | 财经/产经 |
| 28 | 经济观察报 (eeo.com.cn) | 产经/宏观 |
| 29 | 21世纪经济报道 (21jingji.com) | 财经深度 |
| 30 | 中国经营报 (cb.com.cn) | 商业/产业 |
| 31 | 华尔街见闻 (wallstreetcn.com) | 金融资讯 |
| 32 | 金十数据 (jin10.com) | 实时金融数据 |
| 33 | 东方财富网 (eastmoney.com) | 股票/财经 |
| 34 | 同花顺 (10jqka.com.cn) | 金融/股票 |

### 综合新闻 (16)
| 35 | 澎湃新闻 (thepaper.cn) | 深度调查/时政 |
| 36 | 新京报 (bjnews.com.cn) | 社会/深度 |
| 37 | 南方周末 (infzm.com) | 深度报道 |
| 38 | 南方都市报 (oeeee.com) | 社会/民生 |
| 39 | 中国新闻网 (chinanews.com) | 综合新闻 |
| 40 | 观察者网 (guancha.cn) | 深度评论 |
| 41 | 环球网 (huanqiu.com) | 国际新闻 |
| 42 | 参考消息 (cankaoxiaoxi.com) | 外媒编译 |
| 43 | 中国青年报 (cyol.com) | 青年/教育 |
| 44 | 光明网 (gmw.cn) | 文化/思想 |
| 45 | 央广网 (cnr.cn) | 综合新闻 |
| 46 | 国际在线 (cri.cn) | 国际新闻 |
| 47 | 新浪新闻 (news.sina.com.cn) | 综合 |
| 48 | 网易新闻 (news.163.com) | 综合 |
| 49 | 腾讯新闻 (news.qq.com) | 综合 |
| 50 | 百度新闻 (news.baidu.com) | 聚合 |

---

## 四、🌍 国际/封锁新闻 (45)

### 中文国际媒体 (18)
| # | 媒体 | 国家/地区 | 核心价值 |
|:-:|------|:--------:|---------|
| 1 | 联合早报 (zaobao.com) | 🇸🇬 新加坡 | 中文视角东南亚 |
| 2 | BBC中文 (bbc.com/zhongwen) | 🇬🇧 英国 | 国际视野双语 |
| 3 | 德国之声中文 (dw.com/zh) | 🇩🇪 德国 | 欧洲视角 |
| 4 | RFI法广中文 (rfi.fr/cn) | 🇫🇷 法国 | 国际时政 |
| 5 | 自由亚洲电台 (rfa.org) | 🇺🇸 美国 | 亚洲地缘 |
| 6 | 华尔街日报中文 (cn.wsj.com) | 🇺🇸 美国 | 全球财经深度 |
| 7 | FT中文网 (ftchinese.com) | 🇬🇧 英国 | 商界视野 |
| 8 | 路透中文 (cn.reuters.com) | 🇬🇧 英国 | 最快财经资讯 |
| 9 | 日经中文网 (cn.nikkei.com) | 🇯🇵 日本 | 亚洲经济 |
| 10 | 纽约时报中文 (cn.nytimes.com) | 🇺🇸 美国 | 美国主流视角 |
| 11 | 端传媒 (theinitium.com) | 🇭🇰 香港 | 香港深度媒体 |
| 12 | 关键评论网 (thenewslens.com) | 🇹🇼 台湾 | 独立评论 |
| 13 | 报导者 (twreporter.org) | 🇹🇼 台湾 | 深度调查 |
| 14 | 朝鲜日报中文 (chinese.chosun.com) | 🇰🇷 韩国 | 韩国视角 |
| 15 | 中央日报中文 (chinese.joins.com) | 🇰🇷 韩国 | 韩国视角 |
| 16 | 大纪元 (epochtimes.com) | 🌍 全球 | 法轮功视角 |
| 17 | 博讯 (boxun.com) | 🌍 全球 | 独立新闻 |
| 18 | 多维新闻网 (dwnews.com) | 🌍 全球 | 华人视角 |

### 英文国际媒体 (27)
| # | 媒体 | 国家 | 核心价值 |
|:-:|------|:---:|---------|
| 19 | Reuters (reuters.com) | 🌍 全球 | 最快新闻 |
| 20 | Associated Press (apnews.com) | 🇺🇸 美国 | 新闻基准 |
| 21 | Bloomberg (bloomberg.com) | 🇺🇸 美国 | 财经/金融 |
| 22 | The Guardian (theguardian.com) | 🇬🇧 英国 | 独立媒体 |
| 23 | The New York Times (nytimes.com) | 🇺🇸 美国 | 深度报道 |
| 24 | The Wall Street Journal (wsj.com) | 🇺🇸 美国 | 财经权威 |
| 25 | Financial Times (ft.com) | 🇬🇧 英国 | 全球商业 |
| 26 | Washington Post (washingtonpost.com) | 🇺🇸 美国 | 时政深度 |
| 27 | Nikkei Asia (asia.nikkei.com) | 🇯🇵 日本 | 亚洲经济 |
| 28 | SCMP (scmp.com) | 🇭🇰 香港 | 亚洲视角英文 |
| 29 | Al Jazeera (aljazeera.com) | 🇶🇦 卡塔尔 | 中东/全球 |
| 30 | The Economist (economist.com) | 🇬🇧 英国 | 深度分析 |
| 31 | Politico (politico.com) | 🇺🇸 美国 | 政治/政策 |
| 32 | Axios (axios.com) | 🇺🇸 美国 | 简洁新闻 |
| 33 | The Intercept (theintercept.com) | 🇺🇸 美国 | 调查报道 |
| 34 | TechCrunch (techcrunch.com) | 🇺🇸 美国 | 科技创业 |
| 35 | The Verge (theverge.com) | 🇺🇸 美国 | 科技文化 |
| 36 | Wired (wired.com) | 🇺🇸 美国 | 科技深度 |
| 37 | Ars Technica (arstechnica.com) | 🇺🇸 美国 | 技术深度 |
| 38 | MIT Technology Review (technologyreview.com) | 🇺🇸 美国 | 前沿技术 |
| 39 | ZDNet (zdnet.com) | 🌍 全球 | IT资讯 |
| 40 | The Register (theregister.com) | 🇬🇧 英国 | IT/安全 |
| 41 | InfoQ (infoq.com) | 🌍 全球 | 软件工程 |
| 42 | The Next Web (thenextweb.com) | 🇳🇱 荷兰 | 科技文化 |
| 43 | VentureBeat (venturebeat.com) | 🇺🇸 美国 | 科技投资 |
| 44 | Business Insider (businessinsider.com) | 🇺🇸 美国 | 商业/科技 |
| 45 | Quartz (qz.com) | 🇺🇸 美国 | 经济/商业 |

---

## 五、📺 电视/广播直播流 (20)

| # | 名称 | 类型 | 核心价值 |
|:-:|------|:----:|---------|
| 1 | CNN (cnn.com) | 新闻电视 | 美国时政 |
| 2 | BBC News (bbc.com/news) | 新闻电视 | 国际时政 |
| 3 | Bloomberg TV (bloomberg.com/tv) | 财经电视 | 实时财经 |
| 4 | CNBC (cnbc.com) | 财经电视 | 金融市场 |
| 5 | CCTV 新闻 (cctv.com) | 官方新闻 | 中国政策 |
| 6 | 凤凰卫视 (ifeng.com) | 华语新闻 | 两岸视角 |
| 7 | France 24 (france24.com) | 国际新闻 | 法国视角 |
| 8 | Al Jazeera English (aljazeera.com) | 国际新闻 | 中东视角 |
| 9 | RT (rt.com) | 国际新闻 | 俄罗斯视角 |
| 10 | NHK World (nhk.or.jp) | 日本新闻 | 亚洲视角 |
| 11 | CGTN (cgtn.com) | 中国国际 | 中国视角 |
| 12 | EuroNews (euronews.com) | 欧洲新闻 | 欧洲视角 |
| 13 | DW News (dw.com) | 德国新闻 | 德国视角 |
| 14 | Sky News (news.sky.com) | 英国新闻 | 英国视角 |
| 15 | PBS News (pbs.org/newshour) | 美国新闻 | 公共广播 |
| 16 | ABC News (abcnews.go.com) | 美国新闻 | 综合 |
| 17 | CBS News (cbsnews.com) | 美国新闻 | 综合 |
| 18 | NBC News (nbcnews.com) | 美国新闻 | 综合 |
| 19 | Fox News (foxnews.com) | 美国新闻 | 保守派视角 |
| 20 | C-SPAN (c-span.org) | 政府直播 | 美国政府 |

---

## 六、📹 视频平台频道 (40)

### YouTube 频道 (20)
| # | 频道 | 领域 | 核心价值 |
|:-:|------|:----:|---------|
| 1 | Y Combinator | 创业 | 硅谷投资风向 |
| 2 | Stanford CS | 学术 | 前沿计算机 |
| 3 | MIT OpenCourseWare | 学术 | 名校课程 |
| 4 | Two Minute Papers | AI | AI论文解读 |
| 5 | Yannic Kilcher | AI | LLM深度分析 |
| 6 | Andrej Karpathy | AI | 神经网络 |
| 7 | Lex Fridman | 访谈 | 思想对话 |
| 8 | Fireship | 开发 | 代码速览 |
| 9 | Theo - t3.gg | 开发 | Web技术 |
| 10 | NetworkChuck | 网络 | 网络技术 |
| 11 | Linus Tech Tips | 硬件 | 硬件评测 |
| 12 | Marques Brownlee | 科技 | 产品评测 |
| 13 | Computerphile | 计算机 | 计算机科学 |
| 14 | Tom Scott | 科技 | 科技趣闻 |
| 15 | Siraj Raval | AI | AI教程 |
| 16 | sentdex | Python | Python/AI |
| 17 | TechLinked | 科技 | 科技快报 |
| 18 | JayzTwoCents | 硬件 | 硬件DIY |
| 19 | Gamers Nexus | 硬件 | 深度测评 |
| 20 | Mrwhosetheboss | 数码 | 数码产品 |

### Bilibili UP主 (20)
| # | UP主 | 领域 | 核心价值 |
|:-:|------|:----:|---------|
| 21 | 老师好我叫何同学 | 科技测评 | 深度科技 |
| 22 | 影视飓风 | 影视技术 | 视频制作 |
| 23 | 极客湾Geekerwan | 数码 | 硬件深度 |
| 24 | 程序员鱼皮 | 编程 | 编程教程 |
| 25 | CodeSheep | 编程 | 程序人生 |
| 26 | 黑马程序员 | 编程 | Java/全栈 |
| 27 | 尚硅谷 | 编程 | 技术教程 |
| 28 | 奇乐编程 | 编程 | 前端/全栈 |
| 29 | 码农高天 | 编程 | C++/系统 |
| 30 | 技术胖 | 编程 | Vue/前端 |
| 31 | 智能路障 | 社会评论 | 深度思考 |
| 32 | 所长林超 | 经济 | 宏观经济 |
| 33 | 半佛仙人 | 商业 | 商业拆解 |
| 34 | 赚钱研究所 | 网赚 | 副业/赚钱 |
| 35 | 老华带你飞 | 创业 | 商业实战 |
| 36 | 麦克MAX | 数码 | 产品体验 |
| 37 | 钟文泽 | 数码 | 苹果产品 |
| 38 | TESTV | 数码 | 测评 |
| 39 | 花生说 | 数码 | 手机 |
| 40 | 科技九州 | 科技 | 综合科技 |

---

## 七、📱 短视频平台 (12)

| # | 平台 | 核心价值 | 监控方向 |
|:-:|------|---------|---------|
| 1 | 抖音 (douyin.com) | 带货/流量趋势/规则变动 | 商品/话题/榜单 |
| 2 | TikTok (tiktok.com) | 全球短视频趋势/内容风向 | 话题/地区/品类 |
| 3 | 快手 (kuaishou.com) | 下沉市场/区域经济信号 | 电商/直播 |
| 4 | 小红书 (xiaohongshu.com) | 消费/生活方式/信息密度 | 笔记/商品/话题 |
| 5 | 西瓜视频 (ixigua.com) | 中视频/深度内容 | 自媒体/知识 |
| 6 | 视频号 (weixin.qq.com) | 微信生态/私域流量 | 公众号/直播 |
| 7 | 微博视频 (weibo.com) | 社交热点/短内容 | 热搜/话题 |
| 8 | 知乎视频 (zhihu.com) | 知识类内容 | 知识/教程 |
| 9 | AcFun (acfun.cn) | 二次元/文化圈层 | ACG/文化 |
| 10 | 美拍 (meipai.com) | 女性/生活 | 美妆/生活 |
| 11 | 微视 (weishi.qq.com) | 腾讯短视频 | 社交短视频 |
| 12 | 全民小视频 | 泛娱乐 | 下沉内容 |

---

## 八、💻 代码仓库/开发者平台 (10)

| # | 平台 | 核心价值 | 监控方式 |
|:-:|------|---------|---------|
| 1 | GitHub (github.com) | 全球最大/新项目首发 | API/Trending |
| 2 | GitLab (gitlab.com) | 企业/私有项目/CI | RSS/API |
| 3 | Gitee (gitee.com) | 国内开源/国产化替代 | API/热门 |
| 4 | SourceForge (sourceforge.net) | 老牌开源/经典项目 | RSS/热门 |
| 5 | GitCode (gitcode.net) | CSDN旗下开发者社区 | API/趋势 |
| 6 | Bitbucket (bitbucket.org) | 小团队/企业项目 | RSS |
| 7 | Coding.net | 腾讯云旗下/DevOps | API |
| 8 | HuggingFace (huggingface.co) | AI模型/数据集首发地 | API/热门 |
| 9 | Docker Hub (hub.docker.com) | 容器镜像/新项目 | API/趋势 |
| 10 | npm (npmjs.com) | JavaScript包/工具 | API/下载量 |

---

## 九、🌐 国际社区/论坛 (35)

| # | 社区 | 核心价值 | 优先级 |
|:-:|------|---------|:-----:|
| 1 | Hacker News (news.ycombinator.com) | 硅谷风向标/冷门首发 | 🔴 S |
| 2 | Reddit (reddit.com) | 边缘sub宝藏多 | 🔴 S |
|   | - r/sidehustle | 副业/偏门赚钱 | |
|   | - r/SaaS | SaaS创业 | |
|   | - r/EntrepreneurRideAlong | 创业实录 | |
|   | - r/beermoney | 小额赚钱 | |
|   | - r/workonline | 在线工作 | |
|   | - r/flipping | 转卖套利 | |
|   | - r/sweatystartup | 实体创业 | |
|   | - r/digitalnomad | 数字游民 | |
|   | - r/juststart | 开始行动 | |
|   | - r/passiveincome | 被动收入 | |
|   | - r/Affiliatemarketing | 联盟营销 | |
|   | - r/dropship | 代发 | |
|   | - r/selfhosted | 自托管 | |
| 3 | Lobsters (lobste.rs) | 技术社区HN替代 | 🟡 A |
| 4 | Product Hunt (producthunt.com) | 新产品首发平台 | 🔴 S |
| 5 | AlternativeTo (alternativeto.net) | 替代品发现/市场空白 | 🟡 A |
| 6 | Twitter/X (x.com) | 实时关键词/极小号信号 | 🔴 S |
| 7 | Facebook Groups (facebook.com) | 私密群组/跨境电商 | 🟡 A |
| 8 | Telegram (t.me) | 频道/群组偏门信息 | 🔴 S |
| 9 | Discord (discord.com) | 小众频道/Alpha/Trading | 🟡 A |
| 10 | LinkedIn (linkedin.com) | 行业动态/人脉 | 🟢 B |
| 11 | Medium (medium.com) | 深度技术/商业文章 | 🟡 A |
| 12 | Dev.to (dev.to) | 开发者社区 | 🟢 B |
| 13 | Indie Hackers (indiehackers.com) | 独立开发者/创业 | 🟡 A |
| 14 | Stack Overflow (stackoverflow.com) | 技术问答 | 🟢 B |
| 15 | Quora (quora.com) | 知识问答 | 🟢 B |
| 16 | Stack Exchange (stackexchange.com) | 专业问答网络 | 🟢 B |
| 17 | HackerOne (hackerone.com) | 漏洞赏金/安全 | 🟡 A |
| 18 | Bugcrowd (bugcrowd.com) | 漏洞赏金平台 | 🟡 A |
| 19 | Betalist (betalist.com) | 初创产品测试 | 🟡 A |
| 20 | UneeQ (uneeq.com) | 数字人/AI | 🟢 B |
| 21 | Slashdot (slashdot.org) | 老牌科技社区 | 🟢 B |
| 22 | Digg (digg.com) | 新闻聚合 | 🟢 B |
| 23 | Fark (fark.com) | 有趣新闻 | 🟢 B |
| 24 | MetaFilter (metafilter.com) | 社区博客 | 🟢 B |
| 25 | Something Awful (forums.somethingawful.com) | 综合论坛 | 🟢 B |
| 26 | 4chan (4chan.org) | 匿名论坛/边缘文化 | 🟡 A |
| 27 | 8kun (8kun.net) | 匿名论坛 | 🟡 A |
| 28 | SaidIt (saidit.net) | Reddit替代 | 🟢 B |
| 29 | Tildes (tildes.net) | 社区论坛 | 🟢 B |
| 30 | Gwern (gwern.net) | AI/自我量化 | 🟡 A |
| 31 | LessWrong (lesswrong.com) | 理性/AI安全 | 🟡 A |
| 32 | Astral Codex Ten (astralcodexten.com) | 理性/科学 | 🟡 A |
| 33 | Marginal Revolution (marginalrevolution.com) | 经济学/文化 | 🟡 A |
| 34 | 80,000 Hours (80000hours.org) | 职业/影响力 | 🟢 B |
| 35 | Slate Star Codex 存档 | 理性社区历史 | 🟢 B |

---

## 十、🌍 社交网络 (15)

| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | 微博 (weibo.com) | 国内热搜/实时话题 |
| 2 | Twitter/X (x.com) | 实时关键词/极小号信号 |
| 3 | 小红书 (xiaohongshu.com) | 消费/生活方式 |
| 4 | 知乎 (zhihu.com) | 深度问答/趋势 |
| 5 | 豆瓣 (douban.com) | 兴趣小组/书影音 |
| 6 | 即刻 (jike.com) | 兴趣圈子 |
| 7 | 探探/陌陌 | 社交 |
| 8 | Telegram 频道 (t.me) | 公共频道/群组 |
| 9 | Discord (discord.com) | 主题服务器 |
| 10 | Mastodon (mastodon.social) | 去中心化社交 |
| 11 | Bluesky (bsky.app) | 分布式社交 |
| 12 | Threads (threads.net) | Meta社交 |
| 13 | Truth Social | 保守派社交 |
| 14 | Parler | 言论自由社交 |
| 15 | Gab | 另类社交 |

---

## 十一、💬 即时通讯/群组 (20)

| # | 平台 | 核心价值 | 监控方式 |
|:-:|------|---------|---------|
| 1 | Telegram 公开频道 | 各类信息流 | Bot API |
| 2 | Telegram 群组 | 社群讨论 | Bot API |
| 3 | Discord 公开服务器 | 主题社区 | Bot |
| 4 | Discord 私密服务器 | Alpha/Trading | Bot |
| 5 | Slack 公开社区 | 行业讨论 | API |
| 6 | 微信群 (需授权) | 私密群组 | 爬虫 |
| 7 | QQ群 (需授权) | 各类社群 | 爬虫 |
| 8 | Signal 群组 | 加密通讯 | 有限 |
| 9 | WhatsApp 群组 | 海外社群 | 有限 |
| 10 | Matrix (matrix.org) | 去中心化通讯 | API |
| 11 | IRC 频道 | 老牌聊天 | 直接 |
| 12 | Zulip 社区 | 开源团队 | API |
| 13 | Rocket.Chat | 开源聊天 | API |
| 14 | Mattermost | 企业聊天 | API |
| 15 | Keybase | 加密社群 | API |
| 16 | Line 群组 | 日韩社群 | 有限 |
| 17 | KakaoTalk 群组 | 韩国社群 | 有限 |
| 18 | VK Groups | 俄语社群 | API |
| 19 | WeChat Work | 企业微信 | 有限 |
| 20 | Element | Matrix客户端 | API |

---

## 十二、🎓 学术/研究 (40)

### 论文预印本 (8)
| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | arXiv (arxiv.org) | AI/ML/CS论文首发 |
| 2 | Papers With Code (paperswithcode.com) | 论文+代码 |
| 3 | Semantic Scholar (semanticscholar.org) | AI论文搜索 |
| 4 | Google Scholar (scholar.google.com) | 全球学术 |
| 5 | SSRN (ssrn.com) | 社会科学预印本 |
| 6 | ResearchGate (researchgate.net) | 学术社交 |
| 7 | Academia (academia.edu) | 学术论文 |
| 8 | bioRxiv (biorxiv.org) | 生物学预印本 |

### 中文学术 (6)
| 9 | 知网 (cnki.net) | 中文学术 |
| 10 | 万方 (wanfangdata.com) | 中文学术 |
| 11 | 维普 (cqvip.com) | 中文学术 |
| 12 | 国家哲学社会科学文献中心 (ncpssd.cn) | 社科 |
| 13 | 中国科学院科技论文预印本 (chinaxiv.org) | 中文预印本 |
| 14 | 百度学术 (xueshu.baidu.com) | 学术搜索 |

### 会议 (10)
| 15 | NeurIPS (neurips.cc) | AI顶级会议 |
| 16 | ICML (icml.cc) | ML顶级 |
| 17 | ICLR (iclr.cc) | 表征学习 |
| 18 | CVPR (cvpr.com) | 计算机视觉 |
| 19 | ACL (aclweb.org) | NLP顶级 |
| 20 | EMNLP (emnlp.org) | NLP |
| 21 | AAAI (aaai.org) | AI综合 |
| 22 | IJCAI (ijcai.org) | AI综合 |
| 23 | ACM SIGCOMM | 网络 |
| 24 | IEEE (ieee.org) | 工程 |

### 研究机构 (10)
| 25 | OpenAI (openai.com) | AI前沿 |
| 26 | DeepMind (deepmind.com) | AI研究 |
| 27 | Google Research (research.google) | 综合 |
| 28 | Meta AI (ai.meta.com) | AI研究 |
| 29 | Microsoft Research (microsoft.com/research) | 综合 |
| 30 | Anthropic (anthropic.com) | AI安全 |
| 31 | Allen AI (allenai.org) | AI研究 |
| 32 | MIT CSAIL (csail.mit.edu) | CS/AI |
| 33 | Stanford AI (ai.stanford.edu) | 学术 |
| 34 | Berkeley AI (bair.berkeley.edu) | 学术 |

### 论文周报 (6)
| 35 | arXiv.org AI周报 | AI周报 |
| 36 | Papers With Code 每周热门 | 论文排行 |
| 37 | Connected Papers (connectedpapers.com) | 论文关联 |
| 38 | Elicit (elicit.com) | AI辅助研究 |
| 39 | Perplexity (perplexity.ai) | AI搜索 |
| 40 | Consensus (consensus.app) | 学术搜索 |

---

## 十三、📜 专利/知识产权 (10)

| # | 数据库 | 核心价值 |
|:-:|--------|---------|
| 1 | Google Patents (patents.google.com) | 全球专利搜索 |
| 2 | WIPO Patents (wipo.int) | 国际专利 |
| 3 | USPTO (uspto.gov) | 美国专利 |
| 4 | EPO (epo.org) | 欧洲专利 |
| 5 | CNIPA (cnipa.gov.cn) | 中国专利 |
| 6 | JPO (jpo.go.jp) | 日本专利 |
| 7 | KIPO (kipo.go.kr) | 韩国专利 |
| 8 | Patentscope (patentscope.wipo.int) | PCT专利 |
| 9 | FreePatentsOnline (freepatentsonline.com) | 免费专利 |
| 10 | Lens (lens.org) | 开放专利 |

---

## 十四、📡 RSS 订阅源 (80)

### 技术RSS (20)
| # | 名称 | 订阅URL |
|:-:|------|---------|
| 1 | Hacker News | news.ycombinator.com/rss |
| 2 | HN Show HN | hn.algolia.com/rss |
| 3 | Hacker News 新帖 | news.ycombinator.com/newest |
| 4 | GitHub Trending | github.com/trending.rss |
| 5 | GitHub Releases | github.com/releases.rss |
| 6 | Product Hunt | producthunt.com/feed |
| 7 | Lobsters | lobste.rs/rss |
| 8 | Ars Technica | arstechnica.com/feed |
| 9 | The Verge | theverge.com/rss |
| 10 | TechCrunch | techcrunch.com/feed |
| 11 | Wired | wired.com/feed |
| 12 | MIT Tech Review | technologyreview.com/feed |
| 13 | InfoQ | infoq.com/feed |
| 14 | Dev.to | dev.to/feed |
| 15 | CSS-Tricks | css-tricks.com/feed |
| 16 | Smashing Magazine | smashingmagazine.com/feed |
| 17 | A List Apart | alistapart.com/main/feed |
| 18 | SitePoint | sitepoint.com/feed |
| 19 | Tuts+ | tutsplus.com/feed |
| 20 | CodeProject | codeproject.com/webservices |

### 新闻RSS (20)
| 21 | BBC News | bbc.com/news/rss |
| 22 | Reuters Top News | reuters.com/rss |
| 23 | AP News | apnews.com/rss |
| 24 | The Guardian | theguardian.com/rss |
| 25 | NYT Home | nytimes.com/rss |
| 26 | WSJ | wsj.com/rss |
| 27 | Bloomberg | bloomberg.com/feed |
| 28 | CNN | cnn.com/rss |
| 29 | NPR | npr.org/rss |
| 30 | BBC中文 | bbc.com/zhongwen/rss |
| 31 | 华尔街见闻 | wallstreetcn.com/rss |
| 32 | 虎嗅 | huxiu.com/rss |
| 33 | 36氪 | 36kr.com/feed |
| 34 | 钛媒体 | tmtpost.com/rss |
| 35 | 极客公园 | geekpark.net/rss |
| 36 | 品玩 | pingwest.com/feed |
| 37 | Solidot | solidot.org/feed |
| 38 | 喷嚏网 | dapenti.com/feed |
| 39 | 喷嚏图卦 | dapenti.com/blog/rss |
| 40 | SOTH | soth.media/feed |

### 财经RSS (10)
| 41 | Yahoo Finance | finance.yahoo.com/rss |
| 42 | MarketWatch | marketwatch.com/rss |
| 43 | Seeking Alpha | seekingalpha.com/feed |
| 44 | Investopedia | investopedia.com/feed |
| 45 | 东方财富 | eastmoney.com/rss |
| 46 | 第一财经 | yicai.com/feed |
| 47 | 财新网 | caixin.com/rss |
| 48 | 金十数据 | jin10.com/rss |
| 49 | 金十雷达 | jin10.com/rss/radar |
| 50 | CoinDesk | coindesk.com/rss |

### 安全RSS (10)
| 51 | KrebsOnSecurity | krebsonsecurity.com/feed |
| 52 | Schneier on Security | schneier.com/feed |
| 53 | The Hacker News | thehackernews.com/rss |
| 54 | Bleeping Computer | bleepingcomputer.com/feed |
| 55 | Threatpost | threatpost.com/feed |
| 56 | SecurityWeek | securityweek.com/rss |
| 57 | Dark Reading | darkreading.com/rss |
| 58 | Naked Security | nakedsecurity.sophos.com/feed |
| 59 | Troy Hunt | troyhunt.com/rss |
| 60 | PortSwigger Research | portswigger.net/research/rss |

### AI/ML RSS (10)
| 61 | Google AI Blog | ai.googleblog.com/rss |
| 62 | Meta AI | ai.meta.com/blog/rss |
| 63 | OpenAI Blog | openai.com/blog/rss |
| 64 | DeepMind | deepmind.com/blog/rss |
| 65 | Anthropic | anthropic.com/blog/rss |
| 66 | HuggingFace Blog | huggingface.co/blog/feed |
| 67 | arXiv ML | arxiv.org/rss/cs.LG |
| 68 | arXiv AI | arxiv.org/rss/cs.AI |
| 69 | arXiv CL | arxiv.org/rss/cs.CL |
| 70 | PapersWithCode | paperswithcode.com/rss |

### 冷门博客RSS (10)
| 71 | 阮一峰 | ruanyifeng.com/feed |
| 72 | 小众软件 | appinn.com/feed |
| 73 | 思有邪 | siyouxie.com/feed |
| 74 | 槽边往事 | caobiange.com/feed |
| 75 | MacTalk | mac-talk.net/feed |
| 76 | 搞笑诺贝尔 | improbable.com/feed |
| 77 | Gwern | gwern.net/index.xml |
| 78 | Marginal Revolution | marginalrevolution.com/feed |
| 79 | Astral Codex Ten | astralcodexten.com/feed |
| 80 | LessWrong | lesswrong.com/feed |

---

## 十五、🔗 RSSHub 路由 (120)

RSSHub 是一个万能 RSS 生成器，可将 300+ 网站内容转为 RSS。
以下为常用路由，安装 RSSHub 后可直接使用：

### 社交媒体路由 (20)
| # | 路由 | 说明 |
|:-:|------|------|
| 1 | /twitter/user/:id | 用户推文 |
| 2 | /twitter/keyword/:keyword | 关键词搜索 |
| 3 | /twitter/trends | 趋势 |
| 4 | /twitter/list/:id/:slug | 列表 |
| 5 | /instagram/user/:id | Instagram用户 |
| 6 | /instagram/tag/:tag | 标签 |
| 7 | /pixiv/user/:id | Pixiv用户 |
| 8 | /pixiv/ranking/:mode | 排行 |
| 9 | /telegram/channel/:username | TG频道 |
| 10 | /telegram/stickerpack/:name | 贴纸包 |
| 11 | /discord/channel/:id | Discord频道 |
| 12 | /mastodon/user/:id | Mastodon |
| 13 | /bluesky/user/:id | Bluesky |
| 14 | /tumblr/blog/:name | Tumblr |
| 15 | /reddit/:subreddit | Reddit板块 |
| 16 | /reddit/search/:q | Reddit搜索 |
| 17 | /zhihu/collection/:id | 知乎收藏 |
| 18 | /zhihu/people/activities/:id | 知乎动态 |
| 19 | /zhihu/topic/:topicId | 知乎话题 |
| 20 | /zhihu/hotlist | 知乎热榜 |

### 新闻路由 (15)
| 21 | /bbc/:site | BBC新闻 |
| 22 | /reuters/:id | 路透 |
| 23 | /bloomberg/authors/:id | Bloomberg作者 |
| 24 | /bloomberg/topics/:slug | Bloomberg话题 |
| 25 | /theguardian/:type | 卫报 |
| 26 | /cnn/:path | CNN |
| 27 | /wsj/:id | WSJ |
| 28 | /ntimes/:path | NYT |
| 29 | /nikkei/:id | 日经 |
| 30 | /zaobao/:type | 联合早报 |
| 31 | /rfa/:language | 自由亚洲 |
| 32 | /dw/:path | 德国之声 |
| 33 | /voa/:path | 美国之音 |
| 34 | /rfi/:language | 法广 |
| 35 | /epochtimes/:path | 大纪元 |

### 技术路由 (20)
| 36 | /github/trending/:since | 趋势 |
| 37 | /github/repos/:user | 用户仓库 |
| 38 | /github/search/:query | 搜索 |
| 39 | /github/issues/:user/:repo | Issues |
| 40 | /github/pull/:user/:repo | PR |
| 41 | /github/release/:user/:repo | 发布 |
| 42 | /github/stars/:user/:repo | Stars |
| 43 | /github/topics/:name | Topics |
| 44 | /hackernews/:section | HN板块 |
| 45 | /producthunt/today | PH今日 |
| 46 | /programmingpush/:topic | 编程推送 |
| 47 | /stackoverflow/questions/:type | StackOverflow |
| 48 | /v2ex/topics/:type | V2EX |
| 49 | /v2ex/post/:id | V2EX帖子 |
| 50 | /v2ex/tab/:tab | V2EX标签 |
| 51 | /v2ex/member/:name | V2EX用户 |
| 52 | /solidot/:type | Solidot |
| 53 | /36kr/:type | 36氪 |
| 54 | /huxiu/:type | 虎嗅 |
| 55 | /juejin/category/:category | 掘金分类 |

### 视频路由 (10)
| 56 | /bilibili/user/video/:uid | B站UP主 |
| 57 | /bilibili/user/fav/:uid | 收藏 |
| 58 | /bilibili/partion/:tid | 分区热门 |
| 59 | /bilibili/live/room/:id | 直播 |
| 60 | /bilibili/topic/:topic | 话题 |
| 61 | /youtube/user/:username | YouTube频道 |
| 62 | /youtube/channel/:id | 频道 |
| 63 | /youtube/playlist/:id | 播放列表 |
| 64 | /youtube/trending | 趋势 |
| 65 | /douyin/user/:id | 抖音用户 |

### 论坛路由 (15)
| 66 | /hostloc/:type | Hostloc |
| 67 | /nodeseek/:type | Nodeseek |
| 68 | /52pojie/:category | 吾爱破解 |
| 69 | /coolapk/:type | 酷安 |
| 70 | /sspai/:type | 少数派 |
| 71 | /ithome/:type | IT之家 |
| 72 | /csdn/:user | CSDN用户 |
| 73 | /cnblogs/:type | 博客园 |
| 74 | /segmentfault/:type | SegmentFault |
| 75 | /oschina/:type | 开源中国 |
| 76 | /tieba/forum/:name | 贴吧 |
| 77 | /tieba/forum/recommend | 吧推荐 |
| 78 | /douban/group/:id | 豆瓣小组 |
| 79 | /douban/topic/:type | 豆瓣话题 |
| 80 | /zhihu/daily | 知乎日报 |

### 博客/文章路由 (10)
| 81 | /medium/:user | Medium |
| 82 | /blogs/:site | 博客 |
| 83 | /wordpress/:url | WordPress |
| 84 | /substack/:id | Substack |
| 85 | /hello-github/:volume | HelloGitHub |
| 86 | /readhub/:category | Readhub |
| 87 | /geektime/:tid | 极客时间 |
| 88 | /infoq/:topic | InfoQ |
| 89 | /ruanyifeng/:type | 阮一峰 |
| 90 | /appinn/:category | 小众软件 |

### 学术路由 (10)
| 91 | /arxiv/:query | arXiv搜索 |
| 92 | /arxiv/:category | 分类 |
| 93 | /dblp/:name | DBLP作者 |
| 94 | /paperswithcode/:type | PapersWithCode |
| 95 | /semanticscholar/:id | SemanticScholar |
| 96 | /scholar/:query | 学术搜索 |
| 97 | /cnki/:keyword | 知网搜索 |
| 98 | /wandb/:entity/:project | WeightsBiases |
| 99 | /huggingface/blog | HF博客 |
| 100 | /huggingface/daily-papers | 每日论文 |

### 生活/杂项路由 (20)
| 101 | /weather/:city | 天气 |
| 102 | /currency/:from/:to | 汇率 |
| 103 | /cryptocurrency/:id | 加密货币 |
| 104 | /stock/:code | 股票 |
| 105 | /juejin/trending/:category | 掘金趋势 |
| 106 | /jobs/:source | 招聘 |
| 107 | /zxhh/:type | 杂项 |
| 108 | /xueqiu/:type | 雪球 |
| 109 | /tophub/:id | 今日热榜 |
| 110 | /baidu/top/:category | 百度热搜 |
| 111 | /weibo/hot | 微博热搜 |
| 112 | /douyin/hot | 抖音热搜 |
| 113 | /bilibili/hot | B站热搜 |
| 114 | /zhihu/hot | 知乎热搜 |
| 115 | /sina/top/:type | 新浪热搜 |
| 116 | /netease/top/:type | 网易热搜 |
| 117 | /toutiao/top | 头条热搜 |
| 118 | /kuaishou/hot | 快手热搜 |
| 119 | /weibo/search/:q | 微博搜索 |
| 120 | /google/trends/:keyword | Google趋势 |

---

## 十六、📝 博客/个人站 (50)

| # | 博客 | 领域 | 价值 |
|:-:|------|:----:|------|
| 1 | 阮一峰的网络日志 | 综合 | 技术周刊 |
| 2 | 小众软件 | 软件 | 冷门软件发现 |
| 3 | 异次元软件 (iplaysoft.com) | 软件 | 效率工具 |
| 4 | 善用佳软 (xbeta.info) | 软件 | 效率提升 |
| 5 | 海量软件 (hiliSoft) | 软件 | 免费工具 |
| 6 | 大虾软件 (daxiaSoft) | 软件 | 实用工具 |
| 7 | 思有邪 (siyouxie.com) | 社会 | 时评 |
| 8 | 槽边往事 (caobiange.com) | 生活 | 和菜头 |
| 9 | MacTalk (mac-talk.net) | 科技 | 池建强 |
| 10 | 小道消息 (weibo.com) | 互联网 | Fenng |
| 11 | 可能吧 (kenengba.com) | 互联网 | 综合 |
| 12 | 月光博客 (williamlong.info) | 互联网 | 站长 |
| 13 | 卢松松博客 (lusongsong.com) | 站长 | 站长圈 |
| 14 | 张戈博客 (zhangge.net) | 技术 | 运维 |
| 15 | 运维派 (yunweipai.com) | 运维 | 运维技术 |
| 16 | 酷壳 (coolshell.cn) | 技术 | 左耳朵耗子 |
| 17 | 陈皓的博客 (coolshell.org) | 技术 | 架构 |
| 18 | 美团技术团队 (tech.meituan.com) | 技术 | 大厂实战 |
| 19 | 腾讯AlloyTeam (alloyteam.com) | 前端 | 大厂前端 |
| 20 | 淘宝FED (fed.taobao.org) | 前端 | 大厂 |
| 21 | 百度ECharts (echarts.baidu.com) | 可视化 | 百度 |
| 22 | 京东JDC (jdc.jd.com) | 前端 | 京东 |
| 23 | 有赞技术 (tech.youzan.com) | 技术 | SaaS |
| 24 | 字节跳动技术 (tech.bytedance.com) | 技术 | 大厂 |
| 25 | 阿里巴巴技术 (102.alibaba.com) | 技术 | 大厂 |
| 26 | 微软DevBlogs (devblogs.microsoft.com) | 技术 | 微软 |
| 27 | Google Developers (developers.googleblog.com) | 技术 | Google |
| 28 | Cloudflare Blog (blog.cloudflare.com) | 技术 | 网络 |
| 29 | AWS Blog (aws.amazon.com/blogs) | 云 | AWS |
| 30 | Netflix TechBlog (netflixtechblog.com) | 技术 | 流媒体 |
| 31 | Uber Engineering (eng.uber.com) | 技术 | 出行 |
| 32 | Airbnb Engineering (airbnb.io) | 技术 | 民宿 |
| 33 | Stripe Blog (stripe.com/blog) | 支付 | 金融 |
| 34 | Discord Blog (discord.com/blog) | 技术 | 聊天 |
| 35 | Figma Blog (figma.com/blog) | 设计 | 设计工具 |
| 36 | Notion Blog (notion.so/blog) | 效率 | 笔记 |
| 37 | Wordpress Blog (wordpress.com/blog) | 博客 | 开源 |
| 38 | Signal Blog (signal.org/blog) | 安全 | 加密 |
| 39 | Tor Blog (blog.torproject.org) | 隐私 | 匿名 |
| 40 | EFF Blog (eff.org) | 隐私 | 数字权利 |
| 41 | ACLU Blog (aclu.org) | 权利 | 民权 |
| 42 | O'Reilly Radar (radar.oreilly.com) | 技术 | 出版业 |
| 43 | Stratechery (stratechery.com) | 科技战略 | 深度分析 |
| 44 | Benedict Evans (benn.substack.com) | 科技 | 趋势分析 |
| 45 | A16Z (a16z.com) | VC | 风投观点 |
| 46 | Sequoia (sequoiacap.com) | VC | 风投 |
| 47 | Accel (accel.com) | VC | 风投 |
| 48 | YC Blog (blog.ycombinator.com) | 创业 | 孵化器 |
| 49 | Paul Graham (paulgraham.com) | 创业 | 创始人 |
| 50 | Sam Altman (blog.samaltman.com) | AI | CEO观点 |

---

## 十七、📧 Newsletter/邮件 (30)

| # | 名称 | 内容 | 频次 |
|:-:|------|:----:|:----:|
| 1 | Stratechery (stratechery.com) | 科技战略深度 | 每日 |
| 2 | Ben Evans (benn.substack.com) | 科技趋势 | 每周 |
| 3 | The Diff (thediff.co) | 金融/科技 | 每日 |
| 4 | Matt Levine's Money Stuff (bloomberg.com) | 金融 | 每日 |
| 5 | TLDR (tldr.tech) | 科技简报 | 每日 |
| 6 | HackerNews Digest (hndigest.com) | HN精选 | 每日 |
| 7 | The Neuron (theneurondaily.com) | AI日报 | 每日 |
| 8 | Last Week in AI (lastweekin.ai) | AI周报 | 每周 |
| 9 | Import AI (jack@jack-clark.com) | AI周报 | 每周 |
| 10 | The Batch (deeplearning.ai) | AI简报 | 每周 |
| 11 | AI Breakfast (aibreakfast.beehiiv.com) | AI早餐 | 每日 |
| 12 | Ben's Bites (bensbites.beehiiv.com) | AI | 每日 |
| 13 | Superhuman (superhuman.ai) | AI | 每日 |
| 14 | TheSequence (thesequence.substack.com) | ML | 每周 |
| 15 | Nate Silver's Silver Bulletin | 数据 | 不定期 |
| 16 | Noahpinion (noahpinion.substack.com) | 经济学 | 每周 |
| 17 | Asia Sentinel (asiasentinel.com) | 亚洲 | 每日 |
| 18 | ChinaTalk (chinatalk.substack.com) | 中国科技 | 每周 |
| 19 | Sinocism (sinocism.com) | 中国 | 每日 |
| 20 | SupChina (supchina.com) | 中国 | 每日 |
| 21 | The Garbage Day (garbageday.email) | 网络文化 | 每日 |
| 22 | Dense Discovery (densediscovery.com) | 设计/科技 | 每周 |
| 23 | Product Hunt Daily (producthunt.com) | 产品 | 每日 |
| 24 | Indie Hackers Newsletter | 创业 | 每周 |
| 25 | Maker Mag (makermag.com) | 创造者 | 每周 |
| 26 | SaaS Weekly (saasweekly.com) | SaaS | 每周 |
| 27 | GrowthHackers (growthhackers.com) | 增长 | 每日 |
| 28 | Marketing Examples (marketingexamples.com) | 营销 | 每周 |
| 29 | Copyblogger (copyblogger.com) | 写作 | 每周 |
| 30 | Seth Godin (seths.blog) | 营销 | 每日 |

---

## 十八、🎙️ 播客 (30)

| # | 名称 | 领域 | 价值 |
|:-:|------|:----:|------|
| 1 | Lex Fridman Podcast | AI/访谈 | 深入对话 |
| 2 | Acquired | 商业 | 公司深度 |
| 3 | How I Built This | 创业 | 创始人故事 |
| 4 | StartUp Podcast | 创业 | 创业实录 |
| 5 | The Tim Ferriss Show | 效率 | 访谈 |
| 6 | Software Engineering Daily | 工程 | 技术 |
| 7 | Changelog | 开源 | 开发者 |
| 8 | Syntax FM | Web开发 | 前端 |
| 9 | Full Stack Radio | 全栈 | 技术 |
| 10 | ShopTalk Show | 前端 | 设计 |
| 11 | JS Party | JS | JavaScript |
| 12 | Kubernetes Podcast | K8s | 云原生 |
| 13 | Data Skeptic | 数据 | AI/数据 |
| 14 | Machine Learning Street Talk | ML | 深度ML |
| 15 | Practical AI | AI | 实践 |
| 16 | AI Podcast | AI | 综合 |
| 17 | TWIML (This Week in ML) | ML | 周报 |
| 18 | Talk Python To Me | Python | 技术 |
| 19 | Python Bytes | Python | 周报 |
| 20 | Real Python Podcast | Python | 教程 |
| 21 | Software Engineering Radio | 工程 | 综合 |
| 22 | 科技乱炖 | 中文科技 | 大狗熊 |
| 23 | 津津乐道 | 中文科技 | 综合 |
| 24 | Teahour.fm | 中文技术 | 开发者 |
| 25 | Swift by Sundell | Swift | 苹果 |
| 26 | Under the Radar | 苹果 | 独立开发 |
| 27 | ATP (Accidental Tech Podcast) | 苹果 | 综合 |
| 28 | Mac Power Users | 效率 | 苹果用户 |
| 29 | Cortex | 效率 | 创作者 |
| 30 | Reconcilable Differences | 文化 | 科技生活 |

---

## 十九、📖 维基/百科 (8)

| # | 名称 | 核心价值 |
|:-:|------|---------|
| 1 | Wikipedia (wikipedia.org) | 全球知识库 |
| 2 | Wikipedia最新条目 | 新概念/新事件 |
| 3 | 维基百科中文 (zh.wikipedia.org) | 中文知识 |
| 4 | 百度百科 (baike.baidu.com) | 中文百科 |
| 5 | Wikidata (wikidata.org) | 结构化数据 |
| 6 | WikiHow (wikihow.com) | 教程 |
| 7 | Fandom (fandom.com) | 粉丝维基 |
| 8 | 萌娘百科 (moegirl.org.cn) | ACG百科 |

---

## 二十、🏛️ 政府/监管 (25)

| # | 机构 | 国家 | 核心价值 |
|:-:|------|:----:|---------|
| 1 | 中国政府网 (gov.cn) | 🇨🇳 中国 | 政策发布 |
| 2 | 工信部 (miit.gov.cn) | 🇨🇳 中国 | 产业政策 |
| 3 | 网信办 (cac.gov.cn) | 🇨🇳 中国 | 互联网监管 |
| 4 | 科技部 (most.gov.cn) | 🇨🇳 中国 | 科技政策 |
| 5 | 商务部 (mofcom.gov.cn) | 🇨🇳 中国 | 贸易政策 |
| 6 | 发改委 (ndrc.gov.cn) | 🇨🇳 中国 | 宏观政策 |
| 7 | 央行 (pbc.gov.cn) | 🇨🇳 中国 | 货币政策 |
| 8 | 证监会 (csrc.gov.cn) | 🇨🇳 中国 | 证券监管 |
| 9 | 国家知识产权局 (cnipa.gov.cn) | 🇨🇳 中国 | 知识产权 |
| 10 | 国家统计局 (stats.gov.cn) | 🇨🇳 中国 | 经济数据 |
| 11 | SEC (sec.gov) | 🇺🇸 美国 | 证券监管 |
| 12 | FTC (ftc.gov) | 🇺🇸 美国 | 消费者保护 |
| 13 | FCC (fcc.gov) | 🇺🇸 美国 | 通信监管 |
| 14 | FDA (fda.gov) | 🇺🇸 美国 | 药品/食品 |
| 15 | NIH (nih.gov) | 🇺🇸 美国 | 医疗研究 |
| 16 | NSF (nsf.gov) | 🇺🇸 美国 | 科学基金 |
| 17 | DARPA (darpa.mil) | 🇺🇸 美国 | 前沿技术 |
| 18 | FBI (fbi.gov) | 🇺🇸 美国 | 执法动态 |
| 19 | CIA (cia.gov) | 🇺🇸 美国 | 情报 |
| 20 | EU Commission (ec.europa.eu) | 🇪🇺 欧盟 | 欧盟政策 |
| 21 | EU DG Connect | 🇪🇺 欧盟 | 数字政策 |
| 22 | UK Gov (gov.uk) | 🇬🇧 英国 | 英国政策 |
| 23 | 日本经济产业省 (meti.go.jp) | 🇯🇵 日本 | 产业政策 |
| 24 | 韩国科学技术部 (msit.go.kr) | 🇰🇷 韩国 | 科技政策 |
| 25 | 新加坡政府 (gov.sg) | 🇸🇬 新加坡 | 东南亚政策 |

---

## 二十一、💰 金融/市场 (25)

| # | 源 | 类型 | 核心价值 |
|:-:|----|:----:|---------|
| 1 | Yahoo Finance (finance.yahoo.com) | 股票 | 综合金融 |
| 2 | TradingView (tradingview.com) | 图表 | 技术分析 |
| 3 | Investing.com | 金融 | 全球市场 |
| 4 | MarketWatch (marketwatch.com) | 金融 | 市场新闻 |
| 5 | Bloomberg Terminal | 专业 | 金融数据 |
| 6 | Reuters Markets | 金融 | 实时行情 |
| 7 | CoinMarketCap (coinmarketcap.com) | 加密货币 | 币市行情 |
| 8 | CoinGecko (coingecko.com) | 加密货币 | 币市行情 |
| 9 | DeFi Pulse (defipulse.com) | DeFi | 去中心化金融 |
| 10 | Dune Analytics (dune.com) | 链上数据 | 区块链分析 |
| 11 | Glassnode (glassnode.com) | 链上数据 | 比特币分析 |
| 12 | Messari (messari.io) | 加密研究 | 项目分析 |
| 13 | The Block (theblock.co) | 加密新闻 | 行业新闻 |
| 14 | Tokenterminal | 加密 | 项目指标 |
| 15 | Nansen (nansen.ai) | 链上 | 钱包分析 |
| 16 | 雪球 (xueqiu.com) | 股票社区 | A股讨论 |
| 17 | 同花顺 (10jqka.com.cn) | 股票 | 行情数据 |
| 18 | 东方财富 (eastmoney.com) | 股票 | 综合金融 |
| 19 | 新浪财经 (finance.sina.com.cn) | 财经 | 综合 |
| 20 | 网易财经 (money.163.com) | 财经 | 综合 |
| 21 | 腾讯财经 (finance.qq.com) | 财经 | 综合 |
| 22 | 凤凰财经 (finance.ifeng.com) | 财经 | 综合 |
| 23 | 格隆汇 (gelonghui.com) | 港股 | 港股分析 |
| 24 | 36氪二级市场 | 财经 | 上市公司 |
| 25 | SEC EDGAR (sec.gov/edgar) | 财报 | 上市公司文件 |

---

## 二十二、💼 招聘/就业 (12)

| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | LinkedIn Jobs (linkedin.com) | 全球招聘趋势 |
| 2 | Indeed (indeed.com) | 招聘市场 |
| 3 | Glassdoor (glassdoor.com) | 公司评价/薪资 |
| 4 | BOSS直聘 (zhipin.com) | 国内招聘 |
| 5 | 拉勾 (lagou.com) | 互联网招聘 |
| 6 | 猎聘 (liepin.com) | 高端招聘 |
| 7 | 智联招聘 (zhaopin.com) | 综合招聘 |
| 8 | 前程无忧 (51job.com) | 综合招聘 |
| 9 | Upwork (upwork.com) | 自由职业 |
| 10 | Fiverr (fiverr.com) | 自由职业市场 |
| 11 | Freelancer (freelancer.com) | 全球自由职业 |
| 12 | Toptal (toptal.com) | 高端自由职业 |

---

## 二十三、❓ 问答/知识社区 (15)

| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | Stack Overflow (stackoverflow.com) | 技术问答/疑难 |
| 2 | Quora (quora.com) | 综合问答/话题 |
| 3 | 知乎 (zhihu.com) | 中文深度问答 |
| 4 | 百度知道 (zhidao.baidu.com) | 中文问答 |
| 5 | 悟空问答 (wukong.com) | 综合问答 |
| 6 | Product Hunt Discussion | 产品讨论 |
| 7 | Hacker News Ask | 提问 |
| 8 | Reddit AMA | 问我任何事 |
| 9 | Stack Exchange Network (stackexchange.com) | 专业问答网络 |
| 10 | Server Fault (serverfault.com) | 系统管理 |
| 11 | Super User (superuser.com) | 电脑使用 |
| 12 | Ask Ubuntu (askubuntu.com) | Ubuntu |
| 13 | Unix & Linux (unix.stackexchange.com) | Unix |
| 14 | Database Administrators (dba.stackexchange.com) | 数据库 |
| 15 | Security StackExchange (security.stackexchange.com) | 安全 |

---

## 二十四、🛒 电商/商品 (15)

| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | Amazon (amazon.com) | 全球电商趋势 |
| 2 | 淘宝 (taobao.com) | 国内电商 |
| 3 | 京东 (jd.com) | 综合电商 |
| 4 | 拼多多 (pinduoduo.com) | 下沉电商 |
| 5 | 1688 (1688.com) | 批发货源 |
| 6 | eBay (ebay.com) | 国际二手 |
| 7 | AliExpress (aliexpress.com) | 跨境出口 |
| 8 | Shopee (shopee.com) | 东南亚电商 |
| 9 | Lazada (lazada.com) | 东南亚电商 |
| 10 | Etsy (etsy.com) | 手工/创意 |
| 11 | Walmart (walmart.com) | 美国零售 |
| 12 | Best Buy (bestbuy.com) | 电子产品 |
| 13 | Newegg (newegg.com) | 电脑硬件 |
| 14 | 闲鱼 (2.taobao.com) | 二手交易 |
| 15 | 转转 (zhuanzhuan.com) | 二手交易 |

---

## 二十五、📱 APP/应用商店 (12)

| # | 商店 | 核心价值 |
|:-:|------|---------|
| 1 | App Store (apps.apple.com) | iOS应用排名 |
| 2 | Google Play (play.google.com) | Android应用 |
| 3 | Steam (store.steampowered.com) | PC游戏 |
| 4 | Epic Games Store (epicgames.com) | 游戏 |
| 5 | App Annie (data.ai) | 移动数据 |
| 6 | Sensor Tower (sensortower.com) | App市场数据 |
| 7 | Similarweb (similarweb.com) | 网站流量 |
| 8 | Appfigures (appfigures.com) | App分析 |
| 9 | 七麦数据 (qimai.cn) | iOS国内排名 |
| 10 | 酷传 (kuchuan.com) | 应用市场监控 |
| 11 | 小米应用商店 | Android |
| 12 | 华为应用市场 | Android |

---

## 二十六、🎨 设计/创意 (10)

| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | Behance (behance.net) | 设计作品/趋势 |
| 2 | Dribbble (dribbble.com) | UI设计 |
| 3 | Unsplash (unsplash.com) | 免费图片 |
| 4 | Figma Community (figma.com) | 设计资源 |
| 5 | DeviantArt (deviantart.com) | 艺术社区 |
| 6 | ArtStation (artstation.com) | 概念艺术 |
| 7 | Awwwards (awwwards.com) | 网页设计 |
| 8 | CSS Design Awards | CSS设计 |
| 9 | Design Milk (design-milk.com) | 设计新闻 |
| 10 | Dezeen (dezeen.com) | 建筑/设计 |

---

## 二十七、🔒 安全/漏洞 (15)

| # | 源 | 核心价值 |
|:-:|-----|---------|
| 1 | CVE Database (cve.mitre.org) | 漏洞公告 |
| 2 | NVD (nvd.nist.gov) | 国家漏洞库 |
| 3 | Exploit-DB (exploit-db.com) | 漏洞利用 |
| 4 | HackerOne Hacker Activity | H1活动 |
| 5 | Bugcrowd Research | 安全研究 |
| 6 | 乌云-镜像 (wooyun.org) | 国内漏洞 |
| 7 | 知道创宇 (scanv.com) | 国内安全 |
| 8 | 360漏洞 (loudong.360.cn) | 360 |
| 9 | 腾讯安全 (s.tencent.com) | 腾讯 |
| 10 | 阿里安全 (alibabagroup.com) | 阿里 |
| 11 | SANS Internet Storm (isc.sans.edu) | 威胁情报 |
| 12 | AlienVault OTX (otx.alienvault.com) | 威胁情报 |
| 13 | Talos Intelligence (talosintelligence.com) | Cisco |
| 14 | Fortinet Threat (fortinet.com) | 威胁 |
| 15 | McAfee Labs (mcafee.com) | 安全研究 |

---

## 二十八、🗃️ 数据库/数据集 (15)

| # | 源 | 核心价值 |
|:-:|----|---------|
| 1 | Kaggle (kaggle.com) | 数据集/竞赛 |
| 2 | HuggingFace Datasets (huggingface.co/datasets) | AI数据集 |
| 3 | Google Dataset Search | 数据集搜索 |
| 4 | Data.gov (data.gov) | 美国政府数据 |
| 5 | Our World in Data (ourworldindata.org) | 全球数据 |
| 6 | Gapminder (gapminder.org) | 全球统计 |
| 7 | Statista (statista.com) | 统计数据 |
| 8 | World Bank Data (data.worldbank.org) | 世界银行 |
| 9 | IMF Data (imf.org) | 国际货币基金 |
| 10 | UN Data (data.un.org) | 联合国数据 |
| 11 | OECD Data (oecd.org) | 经合组织 |
| 12 | WTO Data (wto.org) | 贸易数据 |
| 13 | Eurostat (ec.europa.eu/eurostat) | 欧洲数据 |
| 14 | 国家统计局 (stats.gov.cn) | 中国数据 |
| 15 | 中国海关总署 (customs.gov.cn) | 贸易数据 |

---

## 二十九、🔧 API/开发者工具 (18)

| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | API List (apilist.fun) | 公共API目录 |
| 2 | ProgrammableWeb (programmableweb.com) | API目录 |
| 3 | RapidAPI (rapidapi.com) | API市场 |
| 4 | APINEWS (apinews.com) | API新闻 |
| 5 | Postman Blog (blog.postman.com) | API工具 |
| 6 | Swagger/Tools | API规范 |
| 7 | Web.Dev (web.dev) | Web技术 |
| 8 | MDN Web Docs (developer.mozilla.org) | Web标准 |
| 9 | CanIUse (caniuse.com) | 浏览器兼容 |
| 10 | NPM Trends (npmtrends.com) | JS包趋势 |
| 11 | PyPI Stats (pypistats.org) | Python包趋势 |
| 12 | Docker Trends | 容器趋势 |
| 13 | CNCF Landscape (landscape.cncf.io) | 云原生全景 |
| 14 | ThoughtWorks Tech Radar (thoughtworks.com) | 技术雷达 |
| 15 | StackShare (stackshare.io) | 技术栈分享 |
| 16 | LibHunt (libhunt.com) | 库推荐 |
| 17 | Openbase (openbase.com) | 开源包 |
| 18 | Snyk Advisor (snyk.io/advisor) | 包安全 |

---

## 三十、📦 网盘/资源 (10)

| # | 平台 | 核心价值 |
|:-:|------|---------|
| 1 | 百度网盘 (pan.baidu.com) | 国内分享 |
| 2 | 阿里云盘 (aliyundrive.com) | 国内存储 |
| 3 | 天翼云盘 (cloud.189.cn) | 国内 |
| 4 | 夸克网盘 (pan.quark.cn) | 国内 |
| 5 | 蓝奏云 (lanzou.com) | 国内 |
| 6 | 腾讯微云 (weiyun.com) | 国内 |
| 7 | Google Drive (drive.google.com) | 国际 |
| 8 | Dropbox (dropbox.com) | 国际 |
| 9 | Mega (mega.nz) | 加密存储 |
| 10 | MediaFire (mediafire.com) | 文件分享 |

---

## 三十一、🌑 暗网/深网/边缘 (8)

| # | 源 | 说明 | 风险 |
|:-:|----|------|:----:|
| 1 | Tor 隐藏服务 (.onion) | 匿名网站 | 高 |
| 2 | I2P 网络 (i2p.net) | 匿名网络 | 中 |
| 3 | Freenet (freenet.org) | 去中心化 | 中 |
| 4 | ZeroNet (zeronet.io) | 去中心化网站 | 低 |
| 5 | IPFS (ipfs.io) | 星际文件系统 | 低 |
| 6 | 区块链交易分析 | 链上资金流向 | 低 |
| 7 | Darknet Market监测 | 暗网市场 | 高 |
| 8 | 加密论坛 | 加密讨论 | 中 |

---

## 三十二、📧 邮件列表/Group (12)

| # | 列表 | 内容 |
|:-:|------|------|
| 1 | LLVM Developers (lists.llvm.org) | 编译器开发 |
| 2 | Linux Kernel (vger.kernel.org) | 内核开发 |
| 3 | Python Dev (mail.python.org) | Python语言 |
| 4 | IETF (ietf.org) | 互联网标准 |
| 5 | W3C (w3.org) | Web标准 |
| 6 | Apache Foundation (apache.org) | 开源 |
| 7 | GNOME Foundation (gnome.org) | 桌面 |
| 8 | Debian Mailing Lists (lists.debian.org) | Linux发行版 |
| 9 | Fedora (lists.fedoraproject.org) | 发行版 |
| 10 | FreeBSD (lists.freebsd.org) | BSD |
| 11 | Mozilla (lists.mozilla.org) | 浏览器 |
| 12 | Google Groups (groups.google.com) | 综合讨论组 |

---

## 三十三、📔 期刊/杂志 (25)

| # | 期刊 | 领域 |
|:-:|------|:----:|
| 1 | Nature (nature.com) | 科学综合 |
| 2 | Science (science.org) | 科学综合 |
| 3 | Cell (cell.com) | 生命科学 |
| 4 | The Lancet (thelancet.com) | 医学 |
| 5 | IEEE Spectrum (spectrum.ieee.org) | 工程 |
| 6 | ACM Communications (cacm.acm.org) | 计算机 |
| 7 | JMLR (jmlr.org) | ML研究 |
| 8 | JMLT (jmlt.org) | ML |
| 9 | TMLR (jmlr.org/tmlr) | ML |
| 10 | Nature Machine Intelligence | AI |
| 11 | Nature Digital Medicine | 数字医疗 |
| 12 | Science Robotics | 机器人 |
| 13 | Harvard Business Review (hbr.org) | 商业 |
| 14 | MIT Sloan Management Review | 管理 |
| 15 | Stanford Social Innovation Review | 社会创新 |
| 16 | Foreign Affairs (foreignaffairs.com) | 国际关系 |
| 17 | Foreign Policy (foreignpolicy.com) | 外交 |
| 18 | The Atlantic (theatlantic.com) | 文化 |
| 19 | The New Yorker (newyorker.com) | 文化深度 |
| 20 | The Economist (economist.com) | 经济 |
| 21 | Wired Magazine (wired.com) | 科技文化 |
| 22 | Fast Company (fastcompany.com) | 商业创新 |
| 23 | Inc. (inc.com) | 创业 |
| 24 | Forbes (forbes.com) | 商业 |
| 25 | Fortune (fortune.com) | 商业 |

---

## 三十四、📅 会议/活动 (12)

| # | 会议 | 领域 | 频次 |
|:-:|------|:----:|:----:|
| 1 | CES (ces.tech) | 消费电子 | 年度 |
| 2 | MWC (mwc.com) | 移动通信 | 年度 |
| 3 | Google I/O (io.google) | 开发 | 年度 |
| 4 | Apple WWDC (developer.apple.com) | 苹果 | 年度 |
| 5 | Microsoft Build (build.microsoft.com) | 微软 | 年度 |
| 6 | AWS re:Invent (reinvent.awsevents.com) | 云 | 年度 |
| 7 | OpenAI DevDay (openai.com) | AI | 年度 |
| 8 | PyCon (pycon.org) | Python | 年度 |
| 9 | KubeCon (cncf.io) | 云原生 | 半年度 |
| 10 | DEF CON (defcon.org) | 安全 | 年度 |
| 11 | Black Hat (blackhat.com) | 安全 | 年度 |
| 12 | SXSW (sxsw.com) | 科技文化 | 年度 |

---

## 三十五、🧭 导航/聚合站 (15)

| # | 站 | 核心价值 |
|:-:|---|---------|
| 1 | 今日热榜 (tophub.today) | 全网热门聚合 |
| 2 | AnyKnew (anyknew.com) | 综合热榜 |
| 3 | Readhub (readhub.cn) | 科技动态 |
| 4 | 抽屉新热榜 (chouti.com) | 热门 |
| 5 | 煎蛋 (jandan.net) | 有趣/科技 |
| 6 | 果壳 (guokr.com) | 科普 |
| 7 | 虎扑步行街 (hupu.com) | 综合 |
| 8 | 最右 (izuiyou.com) | 搞笑/热帖 |
| 9 | 酷安头条 (coolapk.com) | 数码热帖 |
| 10 | 海淘网 (haitao.com) | 海淘 |
| 11 | 什么值得买 (smzdm.com) | 折扣好价 |
| 12 | 慢慢买 (manmanbuy.com) | 历史价格 |
| 13 | 比价网 (bijiak.com) | 比价 |
| 14 | Awesome Lists (github.com/sindresorhus/awesome) | 资源聚合 |
| 15 | Hacker News Front (hn.premii.com) | HN精选 |

---

## 三十六、🌀 其他冷门源 (50)

| # | 源 | 类型 | 价值说明 |
|:-:|----|:----:|---------|
| 1 | 草榴 (t66y.com) | 论坛 | 技术讨论区 |
| 2 | 1024 | 论坛 | 资源分享 |
| 3 | 91porn 技术区 | 技术 | 视频技术 |
| 4 | 品葱 (pincong.net) | 论坛 | 时政讨论 |
| 5 | 膜乎 (mohu.org) | 论坛 | 政治幽默 |
| 6 | 连岳 (ilianyue.com) | 博客 | 时评 |
| 7 | 王陶陶 | 微博 | 地缘政治 |
| 8 | 明镜 (mingjing.org) | 媒体 | 独立 |
| 9 | 大参考 (dacankao.com) | 媒体 | 国际 |
| 10 | 安替 (anti.org) | 博客 | 国际关系 |
| 11 | 立刚老师 | 微博 | 科技评论 |
| 12 | 项立刚 | 微博 | 通信 |
| 13 | 老军医 | 论坛 | 医疗 |
| 14 | 抽屉 (chouti.com) | 聚合 | 热帖 |
| 15 | 开源派 (oschina.net) | 社区 | 开源 |
| 16 | V2EX 二手交易 | 二手 | 物品流通 |
| 17 | 考研帮 (kaoyan.com) | 教育 | 考研 |
| 18 | 小木虫 (emuch.net) | 学术 | 科研 |
| 19 | 丁香园 (dxy.cn) | 医疗 | 医生 |
| 20 | 医学微视 (mvyxws.com) | 医疗 | 视频 |
| 21 | 法律快车 (lawtime.cn) | 法律 | 法规 |
| 22 | 华律 (66law.cn) | 法律 | 咨询 |
| 23 | 应届生 (yingjiesheng.com) | 招聘 | 应届 |
| 24 | 海投网 (haitou.cc) | 招聘 | 校园 |
| 25 | 赛迪网 (ccidnet.com) | 产业 | IT研究 |
| 26 | IDC (idc.com) | 研究 | 市场数据 |
| 27 | Gartner (gartner.com) | 研究 | 技术分析 |
| 28 | Forrester (forrester.com) | 研究 | 市场 |
| 29 | 艾瑞咨询 (iresearch.com) | 研究 | 互联网 |
| 30 | 易观 (analysys.cn) | 研究 | 移动 |
| 31 | 199IT (199it.com) | 数据 | 互联网数据 |
| 32 | 36氪研究院 | 研究 | 行业报告 |
| 33 | 亿欧网 (iyiou.com) | 研究 | 产业 |
| 34 | 甲子光年 (jajiguangnian.com) | 研究 | 科技 |
| 35 | 深度学习i (deeplearningi.com) | 技术 | 中文AI |
| 36 | AI科技评论 (aitechreview.com) | 技术 | AI中文 |
| 37 | InfoQ中文 (infoq.cn) | 技术 | 开发者 |
| 38 | DoNews (donews.com) | 科技 | IT |
| 39 | 站长之家 (chinaz.com) | 站长 | 互联网 |
| 40 | A5站长网 (admin5.com) | 站长 | 运营 |
| 41 | 卢松松 (lusongsong.com) | 站长 | 博客 |
| 42 | 月光博客 (williamlong.info) | 站长 | 综合 |
| 43 | 牟长青 (mouchangqing.com) | 站长 | 推广 |
| 44 | 王通 (wangtong.com) | 站长 | 营销 |
| 45 | 江礼坤 (jianglikun.com) | 站长 | 网络营销 |
| 46 | 懂懂 (dongdong.com) | 博客 | 商业 |
| 47 | 和菜头 (hecaitou.net) | 博客 | 随笔 |
| 48 | 连岳 (ilianyue.com) | 博客 | 时评 |
| 49 | 六神磊磊 | 公众号 | 金庸/时评 |
| 50 | 兽爷 | 公众号 | 深度调查 |

---

## 📊 数据统计

```
爬虫工具引擎:    15种
中文论坛社区:    26个
中文新闻媒体:    50个
国际/封锁新闻:   45个
电视广播直播:    20个
视频频道:        40个
短视频平台:      12个
代码仓库:        10个
国际社区/论坛:   35个
社交网络:        15个
即时通讯群组:    20个
学术/研究:       40个
专利/知识产权:   10个
RSS订阅源:       80个
RSSHub路由:     120个
博客/个人站:     50个
Newsletter:     30个
播客:            30个
维基/百科:        8个
政府/监管:       25个
金融/市场:       25个
招聘/就业:       12个
问答/知识:       15个
电商/商品:       15个
APP商店:         12个
设计/创意:       10个
安全/漏洞:       15个
数据库/数据集:    15个
API/开发者:       18个
网盘/资源:        10个
暗网/深网:        8个
邮件列表:        12个
期刊/杂志:       25个
会议/活动:       12个
导航/聚合:       15个
其他冷门源:      50个
────────────────────
总计:         1,059个情报源
```

---

> **版本 3.0.0** | 配合 SKILL.md 和 intel_scanner.py 使用
> 实际可监控源数量随 RSSHub/Telegram/自定义爬虫 加入持续扩展，无上限。
