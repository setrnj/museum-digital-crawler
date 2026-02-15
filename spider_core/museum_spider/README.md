# 中国国家博物馆网上展览数据采集项目

## 项目简介

本项目是一个**轻量级 Python 数据采集与清洗系统**，用于抓取  
**中国国家博物馆官网「网上展览」栏目**中的当前展览信息。

- 数据来源：https://www.chnmuseum.cn/zl/wszl/
- 采集方式：requests + BeautifulSoup（无浏览器、无 JS）
- 输出结果：结构化 JSON 数据
- 数据规模：12 条真实展览（截至 2026 年 2 月）

该项目适合用于 **数字人文 / 文博信息化 / 数据分析 / 复试展示**。

---

## 项目背景

许多博物馆官网采用**非标准 HTML 结构**：

- 展厅、展期、标题混杂在同一段文本中
- 无标准列表 API
- 不适合直接 Scrapy / XPath

本项目通过：

- 精准 DOM 定位
- 正则表达式清洗
- 字段语义拆分

实现了从**污染文本 → 干净结构化数据**的完整流程。

---

## 数据字段说明

每条展览包含以下字段：

| 字段名 | 说明 |
|------|----|
| museum | 博物馆名称 |
| title | 纯展览标题 |
| hall | 展厅位置（如 南3、南4展厅） |
| publish_time | 展览时间 |
| detail_url | 展览详情页 |
| column_id | 数据来源栏目 |

---

## 示例数据（节选）

```json
{
  "museum": "中国国家博物馆",
  "title": "涅瓦河畔的遐思——列宾艺术特展",
  "hall": "南3、南4展厅",
  "publish_time": "2025/7/23—2026/1/11",
  "detail_url": "https://www.chnmuseum.cn/zl/lszl/gjjlxl/202507/t20250709_272123.shtml",
  "column_id": "网上展览"
}
```

---

## 技术栈

- Python 3.6+
- requests
- beautifulsoup4
- re（正则清洗）

**无 Selenium / Chromium / Scrapy 依赖**  
完全适配老服务器、低内存环境。

---

## 项目结构

```
namuseum_crawler/
├── core/
│   └── namuseum_online_exhibitions_crawler.py
├── data/
│   └── namuseum_online_exhibitions.json
└── README.md
```

---

## 运行方式

### 1. 安装依赖

```bash
pip install requests beautifulsoup4
```

### 2. 运行爬虫

```bash
python core/namuseum_online_exhibitions_crawler.py
```

### 3. 查看结果

```bash
cat data/namuseum_online_exhibitions.json
```

---

## 项目亮点（面试 / 复试可讲）

- 识别真实文博网站的非标准结构
- 正则清洗混合字段文本
- 无浏览器、低资源消耗
- 数据真实、可复现、可分析

---

## 可扩展方向

- 抓取详情页（展览介绍、图片）
- 扩展至其他博物馆（故宫、上博等）
- 数据库存储（SQLite / MongoDB）
- Pandas / Streamlit 可视化分析

---

## 声明

- 本项目仅用于学习与学术研究
- 数据来源于中国国家博物馆官网公开页面
- 请合理控制访问频率，遵守 robots.txt

作者：lzrp  
更新时间：2026 年 2 月
