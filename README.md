# 期权日报机器人（v3）

每天自动抓取期权数据、计算专业指标、生成分析，并推送两份报告到你的 Discord：

- **早报（多伦多 9:45，开盘后 15 分钟）**：开盘快照、异动、今日关注
- **晚报（多伦多 16:30，收盘后 30 分钟）**：全天回顾、OI 增仓、IV 变化、明日关注

你不需要每天开电脑，只需要配置一次。

---

## 报告里有什么

对 `config/tickers.txt` 里的每个代码（默认 8 个：SOXX、GDX、SLV、SPCX、VIXY + NVDA、TSLA、AAPL）：

1. **专业指标速览**：近月 P/C 比率（成交量 & 未平仓）、Max Pain（最大痛点）、ATM 隐含波动率（IV）、IV Rank、25Δ 偏度、IV 期限结构、期权市场隐含的预期波动（±%）、全链净 delta 敞口
2. **异动成交 Top**：成交量/OI 异常放大的合约（含成交额、IV、delta）
3. **OI 增仓 Top**：未平仓量较上次快照明显增加的合约（疑似新建仓）
4. **OI 集中带**：现价附近未平仓堆叠最重的行权价（支撑/压力参考）
5. **规则型解读**：每个指标对应的方向性/风险文字（不依赖任何外部服务，永远可用）
6. **AI 深度分析**（可选，推荐开启）：把当天指标交给 AI 模型，生成市场背景、逐标的要点、风险提示、明日关注四节专业中文分析；AI 只解读算好的数字、不自己算数，失败时自动退回规则版
7. **数据附录**：每只标的的核心数字一行列全，方便你核对

> ⚠️ 所有内容基于公开期权数据的量化观察 + AI 辅助解读，**仅供研究参考，不构成投资建议**。

---

## 数据来源与合规

- 主数据源：**CBOE 官方延迟期权接口**（免费、无需 key，含全部希腊字母和 IV，延迟约 15 分钟）
- 兜底数据源：**Yahoo Finance**
- CBOE 数据仅供个人研究；如未来商用或再分发，需先向 Cboe 申请授权
- 希腊字母补算使用开源库 `vollib`（MIT 许可），CBOE 抓取逻辑借鉴 `global-stock-data`（Apache-2.0）

---

## 运行方式：GitHub Actions（推荐）

所有抓取和计算都在 GitHub 的服务器上完成，你的电脑只需要能收 Discord。

### 第一步：把代码推送到你的 GitHub 仓库

用 VS Code 或 GitHub Desktop 打开这个项目文件夹，把全部文件提交并推送到 `KKOO245/OPTION-ALERT`（或你的新仓库）。

### 第二步：Discord Webhook（如果还没配置）

1. 打开 Discord，进入接收报告的频道
2. 频道设置 → 整合(Integrations) → Webhook → 新建 Webhook → 复制 Webhook 网址

### 第三步：在 GitHub 仓库设置两个 Secrets

打开仓库 → Settings → Secrets and variables → Actions → New repository secret：

| Name | Value |
|---|---|
| `DISCORD_WEBHOOK_URL` | 上一步复制的 Webhook 网址 |
| `OPENAI_API_KEY` | 你的 OpenAI API Key（在 platform.openai.com 创建；每天两份 AI 分析成本约几美分） |

可选：在 **Variables** 里加一个 `OPENAI_MODEL`（默认模型已内置，一般不用改）。

### 第四步：手动测试

1. 打开仓库 → Actions → 每日期权报告 → Run workflow
2. 保持"强制发送"勾选，点绿色确认
3. 等 1-2 分钟，Discord 里应收到完整报告（没有 OPENAI_API_KEY 时会自动用规则版分析，不影响发送）

### 第五步：日常维护

只需要编辑 `config/tickers.txt`：每行一个代码，`#` 开头表示注释。

---

## 关于运行时间与可靠性

- 目标时间：多伦多 **9:45 / 16:30**，周一至周五；夏令时/冬令时自动适配，全年不用手动改
- GitHub Actions 的定时任务可能有延迟，系统用"每小时触发一次 + 脚本内判断时间 + 防重复日志 + 并发锁"来兜底，正常延迟不会漏发
- 同一天同一个时段只真正发送一次
- 数据源故障时自动切换备用源；全部失败则跳过本次发送、留给下一次重试

## 关于 IV Rank

IV Rank 需要至少约 20 个交易日的 ATM IV 历史才有意义，**从上线第一天开始自动积累**（每天两次存进 `data/analytics/`），大约一个月后就会显示完整分位。前期显示 N/A 是正常的。

---

## 文件结构

```
OPTION-ALERT/
├── config/
│   └── tickers.txt          ← 你唯一需要经常编辑的文件
├── src/
│   ├── options_report.py    ← 主入口（调度、组装、发送）
│   ├── data_fetcher.py      ← CBOE + yfinance 数据获取
│   ├── metrics.py           ← 指标计算
│   ├── analysis.py          ← 规则解读与报告排版
│   ├── llm_analyst.py       ← AI 深度分析（可选）
│   ├── storage.py           ← 快照与历史指标
│   └── discord_sender.py    ← Discord 发送
├── data/
│   ├── history/             ← 最近快照（对比用）+ 发送记录
│   └── analytics/           ← 每日指标历史（IV Rank 用，自动积累）
├── tests/                   ← 单元测试
├── .github/workflows/       ← 定时任务配置
└── requirements.txt
```

---

## 常见问题

**Q: AI 分析不想要了怎么办？** 在 GitHub 仓库 Variables 里把 `LLM_ENABLED` 设为 `false`，报告自动退回纯规则版。

**Q: 想改个股/加标的？** 编辑 `config/tickers.txt` 即可，下一轮自动生效。

**Q: 异动太多/太少？** 阈值在 `src/options_report.py` 顶部的 `MIN_VOLUME`（当前 500 张）和 `VOL_OI_MIN`（当前 1.0）里，告诉我，我帮你调。

**Q: Actions 没跑/失败？** 看 Actions 标签页的红色日志；最常见是 Secret 名拼错、Webhook 失效或 OpenAI Key 无效。

**Q: 数据准吗？** CBOE 是官方延迟数据、Yahoo 是免费接口，都可能与实时行情有几分钟到十几分钟的差异；对每日参考足够，但不适合做盘内精确决策。
