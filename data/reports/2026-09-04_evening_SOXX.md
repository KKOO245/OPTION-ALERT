# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 509.40 → 收盘 519.86（+2.1%） ｜ 今日高 520.55 ｜ 低 507.25 ｜ 昨收 502.20 → 收盘 519.86（+3.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.79 | ATM IV 41.1% | Skew -4.1pp | Term 0.90 | ExpMove ±3.5%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±3.5% ｜ 09-18（14D）±5.5% ｜ 09-25（21D）±6.9% ｜ 10-02（28D）±8.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,431,017 | GEX Change vs 上次快照 175,721 | Flip: Primary Flip: 518.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 497 / LOW 304 / INVALID 761
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 518.64（全链重定价，覆盖 92%）
最近结构参考: Flip 519（现价高于该位 0.2%）
量化视角： 正 Gamma（143万，无历史分位）｜正 Gamma 增强（+18万）｜现价位于 Flip 上方 0.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 519（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 550.0C — Vol 306 | 最新价 $3.91 | OI 366→1661 (ΔOI +1295张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1295张（+353.8% vs前日OI），连续性待观察（方向未知）
09-04 520.0C — Vol 2,394 | 最新价 $0.09 | OI 570→1068 (ΔOI +498张) | ΔOI/Volume 20.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增498张（+87.4% vs前日OI），连续性待观察（方向未知）
09-04 500.0C — Vol 131 | 最新价 $16.51 | OI 286→664 (ΔOI +378张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增378张（+132.2% vs前日OI），值得跟踪（方向未知）
09-04 515.0C — Vol 822 | 最新价 $1.40 | OI 860→1186 (ΔOI +326张) | ΔOI/Volume 39.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增326张（+37.9% vs前日OI），连续性待观察（方向未知）
09-18 500.0C — Vol 179 | 最新价 $24.90 | OI 895→1137 (ΔOI +242张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增242张（+27.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,739 张（Put 0 / Call 2,739），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 12.4k / P 14.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 7.65 / P 10.50
隐含波动率 ATM IV:  31.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 500（结算参考） ｜ Call Wall 530（+2.0%）（OI 3.2k） ｜ Put Wall 500（-3.8%）（OI 3.5k）
量化解读： 存量两侧均衡｜ATM IV 31.4%｜历史 Rank 74%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 530（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 545（结算参考） ｜ Put Wall 490（-5.7%，弱）（OI 1.0k）

10-02（Activity LOW）仓位参考: Max Pain 525（结算参考） ｜ Call Wall 570（+9.6%）（OI 2.5k） ｜ Put Wall 470（-9.6%）（OI 2.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/SOXX_evening.json