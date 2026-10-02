# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 197C ΔOI +5,042（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 190.04 → 今开 193.24（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 194.78 ｜ 低 190.60

Options: P/C成交量 0.44 | OI比 0.70 | ATM IV 59.9% | Skew 0.9pp | Term 0.73 | ExpMove ±4.5%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±4.5% ｜ 10-16（14D）±6.5% ｜ 10-23（21D）±8.2% ｜ 10-30（28D）±10.1%
   ⇒ IV–VIX Spread: +44.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 85,356,330 | GEX Change vs 上次快照 25,684,924 | Flip: Primary Flip: 183.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 528 / LOW 107 / INVALID 201
结构观察区: Primary Flip 183.25（全链重定价，覆盖 94%）
Call Wall 200（现价低于该位 3.9%）
最近结构参考: Call Wall 200（现价低于该位 3.9%）
量化视角： 正 Gamma（8536万，无历史分位）｜正 Gamma 增强（+2568万）｜现价位于 Flip 上方 4.91%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 183（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 197.5C — Vol 5,783 | 最新价 $2.03 | OI 1310→6352 (ΔOI +5042张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5042张（+384.9% vs前日OI），连续性待观察（方向未知）
10-09 205.0C — Vol 6,996 | 最新价 $0.70 | OI 2041→6785 (ΔOI +4744张) | ΔOI/Volume 67.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4744张（+232.4% vs前日OI），连续性待观察（方向未知）
10-09 195.0C — Vol 6,597 | 最新价 $2.73 | OI 2096→6225 (ΔOI +4129张) | ΔOI/Volume 62.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4129张（+197.0% vs前日OI），连续性待观察（方向未知）
10-09 202.5C — Vol 4,824 | 最新价 $1.06 | OI 1231→5003 (ΔOI +3772张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3772张（+306.4% vs前日OI），连续性待观察（方向未知）
10-02 195.0C — Vol 21,049 | 最新价 $0.39 | OI 11000→13251 (ΔOI +2251张) | ΔOI/Volume 10.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2251张（+20.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,938 张（Put 0 / Call 19,938），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 125.5k / P 88.1k，今日成交量: C 33.0k / P 14.6k，平值价格ATM: C $1.06 / P $1.44 ｜ ATM IV 59.9%，预期波动 ±1.3%，Max Pain 185
Top ΔOI: C 197 -3,973 ｜ C 205 -3,442 ｜ C 195 +2,251

📆 Forward Expiration Structure

10-09  C +23.7k / P +6.9k ｜ Activity HIGH ｜ 7D
10-16  C +2.0k / P -0.4k ｜ Activity HIGH ｜ 14D
10-23  C +0.3k / P +1.0k ｜ Activity MEDIUM △ ｜ 21D
10-30  C +1.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 60.3k / P 51.8k，今日变化ΔOI: C +23.7k / P +6.9k，平值价格ATM: C $4.32 / P $4.40 ｜ ATM IV 40.8%，净 delta 敞口 508k shares
Top ΔOI: C 197 +5,042 ｜ C 205 +4,744 ｜ C 195 +4,129
仓位参考: Max Pain 188 ｜ Call Wall 200（+4.0%，弱）（OI 6.8k） ｜ Put Wall 190（-1.2%，弱）（OI 5.8k）
量化解读： 存量两侧均衡｜ATM IV 40.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 507,784 股

📆 10-16 Forward Structure
存量OI: C 156.0k / P 169.3k，今日变化ΔOI: C +2.0k / P -0.4k，平值价格ATM: C $6.30 / P $6.20 ｜ ATM IV 41.4%，净 delta 敞口 41k shares
Top ΔOI: C 212 +865 ｜ C 215 +861 ｜ C 205 -620
仓位参考: Max Pain 168 ｜ Call Wall 200（+4.0%，弱）（OI 15.4k） ｜ Put Wall 175（-9.0%，弱）（OI 8.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.4%｜历史 Rank 92%（近端代理）｜IV/RV 1.69×（近似）｜净 delta 敞口 正 41,451 股

10-23（MEDIUM △）Top ΔOI: 175P +193
10-23（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 180（-6.4%）（OI 4.6k） ｜ Put Wall 175（-9.0%，弱）（OI 1.7k）

10-30（MEDIUM △）Top ΔOI: 220C +286 ｜ 185P +199
10-30（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 200（+4.0%，弱）（OI 2.2k） ｜ Put Wall 180（-6.4%，弱）（OI 1.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/PLTR_morning.json