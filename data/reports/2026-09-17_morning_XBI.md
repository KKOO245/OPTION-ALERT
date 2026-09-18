# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 09-18（1D）ATM IV 48.9% vs 09-25 32.5%（差 +16.4pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-18 155P ΔOI -2,829（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 150P ΔOI +8,398 占该期限总 OI 20.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 154.18 → 今开 157.31（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 160.33 ｜ 低 156.94

Options: P/C成交量 1.73 | OI比 1.31 | ATM IV 48.9% | Skew 5.5pp | Term 0.64 | ExpMove ±2.8%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价中性（Skew 5.5pp）｜当日成交偏 Put（P/C量 1.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.73×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.31×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.8% ｜ 09-25（8D）±4.9% ｜ 10-02（15D）±4.7% ｜ 10-09（22D）±2.7%
   ⇒ IV–VIX Spread: +33.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -27,672,154 | GEX Change vs 上次快照 32,270,274 | Flip: Primary Flip: 162.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 311 / LOW 166 / INVALID 367
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.73（全链重定价，覆盖 88%）
Put Wall 150（现价高于该位 6.2%） | Call Wall 170（弱结构｜现价低于该位 6.3%）
最近结构参考: Flip 163（现价低于该位 2.2%）
量化视角： 负 Gamma（2767万，无历史分位）｜负 Gamma 缓解（+3227万）｜现价位于 Flip 下方 2.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 156（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 150.0P — Vol 9,655 | 最新价 $1.97 | OI 3100→11498 (ΔOI +8398张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8398张（+270.9% vs前日OI），连续性待观察（方向未知）
09-18 157.0C — Vol 2,846 | 最新价 $0.56 | OI 975→2762 (ΔOI +1787张) | ΔOI/Volume 62.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1787张（+183.3% vs前日OI），连续性待观察（方向未知）
09-18 150.0P — Vol 3,619 | 最新价 $0.45 | OI 10359→11833 (ΔOI +1474张) | ΔOI/Volume 40.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1474张（+14.2% vs前日OI），连续性待观察（方向未知）
09-18 161.0C — Vol 1,033 | 最新价 $0.21 | OI 361→1356 (ΔOI +995张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增995张（+275.6% vs前日OI），连续性待观察（方向未知）
09-18 160.0C — Vol 1,782 | 最新价 $0.15 | OI 3591→4479 (ΔOI +888张) | ΔOI/Volume 49.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增888张（+24.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,542 张（Put 9,872 / Call 3,670），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.8k / P -1.8k ｜ Activity HIGH ｜ 1D
09-25  C -2.7k / P +8.5k ｜ Activity HIGH ｜ 8D
10-02  C +0.2k / P -4 ｜ Activity HIGH ｜ 15D
10-09  C +12 / P +4 ｜ Activity MEDIUM △ ｜ 22D

📆 09-18 Forward Structure
存量OI: C 79.5k / P 104.4k，今日变化ΔOI: C +2.8k / P -1.8k，平值价格ATM: C $0.30 / P $4.13 ｜ ATM IV 48.9%，净 delta 敞口 240k shares
Top ΔOI: P 155 -2,829 ｜ C 157 +1,787 ｜ P 150 +1,474
仓位参考: Max Pain 156 ｜ Call Wall 170（+6.8%，弱）（OI 10.1k） ｜ Put Wall 150（-5.8%，弱）（OI 11.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.9%｜历史 Rank 96%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 239,918 股

📆 09-25 Forward Structure
存量OI: C 6.8k / P 33.3k，今日变化ΔOI: C -2.7k / P +8.5k，平值价格ATM: C $1.09 / P $6.72 ｜ ATM IV 32.5%，净 delta 敞口 -235k shares
Top ΔOI: P 150 +8,398 ｜ C 170 -3,000 ｜ C 153 +245
仓位参考: Max Pain 157 ｜ Call Wall 160（+0.5%，弱）（OI 2.3k） ｜ Put Wall 145（-8.9%，弱）（OI 15.2k）
量化解读： 存量 Put 重｜ATM IV 32.5%｜历史 Rank 96%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 234,777 股

📆 10-02 Forward Structure
存量OI: C 1.6k / P 1.4k，今日变化ΔOI: C +0.2k / P -4，平值价格ATM: C $2.19 / P $5.35 ｜ ATM IV 30.1%，净 delta 敞口 5k shares
Top ΔOI: C 163 +280 ｜ C 165 -134 ｜ C 162 +46
仓位参考: Max Pain 160 ｜ Call Wall 165（+3.6%）（OI 0.7k） ｜ Put Wall 157（-1.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 30.1%｜历史 Rank 96%（近端代理）｜净 delta 敞口 正 5,251 股

10-09（MEDIUM △）Top ΔOI: 162C +10 ｜ 150P +5
10-09（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 175（+9.9%）（OI 77） ｜ Put Wall 150（-5.8%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 48.9% vs 09-25 32.5%（差 +16.4pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/XBI_morning.json