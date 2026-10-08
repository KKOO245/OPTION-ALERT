# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 52.1% vs 10-12 41.2%（差 +10.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 175C ΔOI +7,529（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 180C ΔOI +1,038 占该期限总 OI 14.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 171.92 → 今开 168.12（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 171.31 ｜ 低 167.33

Options: P/C成交量 1.31 | OI比 1.16 | ATM IV 52.1% | Skew -0.7pp | Term 0.93 | ExpMove ±3.3%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.31×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.3% ｜ 10-12（5D）±3.8% ｜ 10-14（7D）±4.8% ｜ 10-16（9D）±5.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 89,114,371 | GEX Change vs 上次快照 -46,962,748 | Flip: Primary Flip: 160.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 755 / LOW 90 / INVALID 433
结构观察区: Primary Flip 160.09（全链重定价，覆盖 100%）
Call Wall 180（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 160（现价高于该位 5.1%）
量化视角： 正 Gamma（8911万，无历史分位）｜正 Gamma 减弱（4696万）｜现价位于 Flip 上方 5.15%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 175.0C — Vol 81,417 | 最新价 $1.95 | OI 12602→20131 (ΔOI +7529张) | ΔOI/Volume 9.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7529张（+59.7% vs前日OI），连续性待观察（方向未知）
10-09 175.0P — Vol 29,278 | 最新价 $4.90 | OI 670→8132 (ΔOI +7462张) | ΔOI/Volume 25.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7462张（+1113.7% vs前日OI），连续性待观察（方向未知）
10-09 170.0P — Vol 53,556 | 最新价 $2.20 | OI 4030→10644 (ΔOI +6614张) | ΔOI/Volume 12.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6614张（+164.1% vs前日OI），连续性待观察（方向未知）
10-09 172.5P — Vol 29,274 | 最新价 $3.40 | OI 427→4148 (ΔOI +3721张) | ΔOI/Volume 12.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3721张（+871.4% vs前日OI），连续性待观察（方向未知）
10-16 130.0P — Vol 6,102 | 最新价 $0.09 | OI 19052→22593 (ΔOI +3541张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3541张（+18.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 28,867 张（Put 21,338 / Call 7,529），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +22.5k / P +28.5k ｜ Activity HIGH ｜ 2D
10-12  C +13.2k / P +7.1k ｜ Activity HIGH ｜ 5D
10-14  C +4.4k / P +2.7k ｜ Activity MEDIUM △ ｜ 7D
10-16  C +1.2k / P +26.1k ｜ Activity MEDIUM △ ｜ 9D

📆 10-09 Forward Structure
存量OI: C 191.3k / P 221.9k，今日变化ΔOI: C +22.5k / P +28.5k，平值价格ATM: C $3.11 / P $2.40 ｜ ATM IV 52.1%，净 delta 敞口 -1.7M shares
Top ΔOI: C 175 +7,529 ｜ P 175 +7,462 ｜ P 170 +6,614
仓位参考: Max Pain 162 ｜ Call Wall 180（+6.9%，弱）（OI 26.3k） ｜ Put Wall 160（-4.9%，弱）（OI 19.3k）
量化解读： 存量两侧均衡｜ATM IV 52.1%｜历史 Rank 38%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,662,669 股

📆 10-12 Forward Structure
存量OI: C 28.8k / P 15.3k，今日变化ΔOI: C +13.2k / P +7.1k，平值价格ATM: C $3.50 / P $2.95 ｜ ATM IV 41.2%，净 delta 敞口 -134k shares
Top ΔOI: C 182 +2,960 ｜ C 185 +1,492
仓位参考: Max Pain 170 ｜ Call Wall 180（+6.9%，弱）（OI 4.2k） ｜ Put Wall 165（-2.0%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 41.2%｜历史 Rank 38%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 134,377 股

10-14（MEDIUM △）Top ΔOI: 180C +1,038 ｜ 175C +749
10-14（MEDIUM △）仓位参考: Max Pain 172 ｜ Call Wall 180（+6.9%，弱）（OI 1.0k） ｜ Put Wall 170（+1.0%，弱）（OI 0.7k）

10-16（MEDIUM △）Top ΔOI: 150P +3,097 ｜ 160C -2,993
10-16（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（-4.9%，弱）（OI 33.0k） ｜ Put Wall 155（-7.9%，弱）（OI 14.6k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 52.1% vs 10-12 41.2%（差 +10.9pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SPCX_morning.json