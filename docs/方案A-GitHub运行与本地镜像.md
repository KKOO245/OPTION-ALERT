# 方案 A：GitHub 运行报告 + 本地每周镜像

## 架构

```
GitHub Actions（每天 10:15 / 16:30 后自动跑，无需你电脑开机）
  ├─ 抓数据（CBOE/yfinance）
  ├─ 生成报告 → 推 Discord
  ├─ 生成 snapshot_v1 → 机械检测 → 事件入库（thesis/）
  ├─ 结果回填 / Episode 聚类
  └─ 把数据 commit 回仓库（data/analytics、analytics/daily、state、thesis、episodes）
        │
        ├─ 每月 1 日（凌晨）：月度归档 workflow 打包上个月快照 → GitHub Releases（无限量）
        └─ 每天 17:30-18:30：看门狗检查两份报告是否已发，漏发发 Discord 告警

本地电脑（每周五晚报提醒你手动拉一次，或开机后随时补拉）
  └─ D:\git\Option Alert-数据储存：git pull 拉到本地，用于回测/研究
```

## 本地镜像（一次性初始化 + 每周一次）

首次（目录为空时）：

```bat
git clone https://github.com/KKOO245/OPTION-ALERT.git "D:\git\Option Alert-数据储存"
```

每周五收到晚报提醒后（或任何时间）：

```bat
cd /d "D:\git\Option Alert-数据储存"
git pull
```

说明：
- 报告由 GitHub 自动发送，本地只做数据镜像；关机几天也不影响报告，开机后 `git pull` 一次补齐全部缺失提交。
- 本地镜像会同步仓库的删除操作。将来仓库开始"月度清理旧快照"后，被清掉的旧数据要从 Releases 归档下载（每月第一个工作日晚报会提醒）。
- 月度归档下载：网页打开仓库 Releases 页，或命令行 `gh release download data-YYYY-MM`（需要先 `gh auth login`）。

## 发送时间（单向窗口）

改造后报告**绝不提前发送**：早报在 10:15 之后、晚报在 16:30 之后，实际由每小时整点触发决定，通常早报约 11:00、晚报约 17:00 发出。这样抓到的数据更新鲜（15 分钟延时数据对应更晚的时点），也不会出现 9 点就发晨报的情况。

## 看门狗

每天多伦多时间 17:30-18:30 检查 `data/history/_sent_log.json`，若当天早报/晚报缺发送记录，会通过 Discord webhook 发告警。

## 月度归档（v1.1：归档 + 清理，保留最近 3 个月）

`monthly-archive.yml` 每月 1 日凌晨运行：把上个月 `analytics/daily/` 打包成 `data-YYYY-MM.zip` 上传到 Releases（单文件 <2GB、总量不限、不计仓库配额）；**上传成功后才**清理 `analytics/daily/` 中早于截止月（约保留最近 4 个自然月，含当月）的旧目录。`thesis/ episodes/ state/` 永不裁剪；本地镜像会随 `git pull` 同步删除旧目录，因此每月"下载 Releases 归档"的提醒不可跳过。

**清理不影响分析**：验证层（Base Rate/Lift/CI/Episode）使用 `thesis/` 与 `episodes/`，趋势层（IV Rank/动量/期限结构）使用 `data/analytics/*.csv`——这两类数据**永不清理**，全量累计。被清理的只有"超过 3 个月的每日原始快照 JSON"，它们已按月归档到 Releases，回测任何历史月份时下载解压即可。即：**先归档、后清理，统计分析与全量历史回测不受影响。**

**监控上限**：ticker 数量上限 20（`config/tickers.txt` 超限会打印警告）。按 20 个标的、每天 2 份快照估算，仓库 git 历史主要增长来自 `data/history` 全链覆盖提交；若接近 1GB 建议线，再启用"data/history 只保留最近 N 天 + 更早进 Releases"。
