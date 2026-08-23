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

## 月度归档（当前只归档、不删除）

`monthly-archive.yml` 每月 1 日凌晨运行：把上个月 `analytics/daily/` 打包成 `data-YYYY-MM.zip` 上传到 Releases（单文件 <2GB、总量不限、不计仓库配额）。多伦多时间对应上个月最后一个晚上，因此每月第一个工作日的"下载归档"提醒时，归档已经存在。**当前阶段不删除仓库里的旧快照**——按每天几 MB 的量，仓库几年内都不会接近 1GB 建议线；等真要清理时再启用删除逻辑，且必须确认 Release 附件存在、本地/云盘已拉取。
