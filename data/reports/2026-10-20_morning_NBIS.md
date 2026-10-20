# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.58 ｜ QQQ $717.63
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 10-23 ATM IV 108.2% vs 10-30 94.6%（差 +13.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 170.24 → 今开 163.96（-3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 170.49 ｜ 低 160.28

Options: P/C成交量 0.97 | OI比 0.65 | ATM IV 108.2% | Skew 5.1pp | Term 0.88 | ExpMove ±8.2%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±8.2% ｜ 10-30（10D）±12.6% ｜ 11-06（17D）±16.4% ｜ 11-13（24D）±20.1%
   ⇒ IV–VIX Spread: +90.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,910,309 | GEX Change vs 上次快照 -3,123,664 | Flip: Primary Flip: 179.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 558 / LOW 59 / INVALID 193
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 179.49（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 10.5%）
最近结构参考: Flip 179（现价低于该位 7.6%）
量化视角： 负 Gamma（1091万，无历史分位）｜负 Gamma 加深（312万）｜现价位于 Flip 下方 7.63%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 179（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 220.0P — Vol 2,800 | 最新价 $48.40 | OI 1077→3767 (ΔOI +2690张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2690张（+249.8% vs前日OI），连续性待观察（方向未知）
10-30 225.0P — Vol 2,358 | 最新价 $55.52 | OI 420→2657 (ΔOI +2237张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2237张（+532.6% vs前日OI），连续性待观察（方向未知）
10-23 155.0P — Vol 8,343 | 最新价 $1.95 | OI 1910→3824 (ΔOI +1914张) | ΔOI/Volume 22.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1914张（+100.2% vs前日OI），连续性待观察（方向未知）
10-30 230.0P — Vol 1,967 | 最新价 $57.42 | OI 391→2142 (ΔOI +1751张) | ΔOI/Volume 89.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1751张（+447.8% vs前日OI），连续性待观察（方向未知）
10-23 195.0C — Vol 4,434 | 最新价 $0.96 | OI 1546→3134 (ΔOI +1588张) | ΔOI/Volume 35.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1588张（+102.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,180 张（Put 8,592 / Call 1,588），跨 2 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +9.7k / P +0.7k ｜ Activity HIGH ｜ 3D
10-30  C +3.8k / P +8.2k ｜ Activity HIGH ｜ 10D
11-06  C +1.4k / P +0.5k ｜ Activity HIGH ｜ 17D
11-13  C +1.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 95.3k / P 62.2k，今日变化ΔOI: C +9.7k / P +0.7k，平值价格ATM: C $7.61 / P $6.00 ｜ ATM IV 108.2%，净 delta 敞口 502k shares
Top ΔOI: P 220 -2,202 ｜ P 155 +1,914 ｜ C 195 +1,588
仓位参考: Max Pain 185 ｜ Call Wall 180（+8.6%，弱）（OI 4.3k） ｜ Put Wall 165（-0.5%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 108.2%｜历史 Rank 59%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 502,288 股

📆 10-30 Forward Structure
存量OI: C 43.4k / P 36.0k，今日变化ΔOI: C +3.8k / P +8.2k，平值价格ATM: C $11.20 / P $9.67 ｜ ATM IV 94.6%，净 delta 敞口 -629k shares
Top ΔOI: P 220 +2,690 ｜ P 225 +2,237 ｜ P 230 +1,751
仓位参考: Max Pain 215 ｜ Put Wall 165（-0.5%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 94.6%｜历史 Rank 59%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 628,697 股

📆 11-06 Forward Structure
存量OI: C 29.5k / P 16.6k，今日变化ΔOI: C +1.4k / P +0.5k，平值价格ATM: C $14.20 / P $12.95 ｜ ATM IV 93.3%，净 delta 敞口 19k shares
Top ΔOI: C 230 +802
仓位参考: Max Pain 210 ｜ Put Wall 170（+2.5%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 93.3%｜历史 Rank 59%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 18,827 股

11-13（MEDIUM △）Top ΔOI: 190C +215 ｜ 200C +143
11-13（MEDIUM △）仓位参考: Max Pain 205 ｜ Call Wall 180（+8.6%，弱）（OI 0.4k） ｜ Put Wall 165（-0.5%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 108.2% vs 10-30 94.6%（差 +13.7pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=59 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=59）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/NBIS_morning.json