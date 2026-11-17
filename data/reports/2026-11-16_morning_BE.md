# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（4D）ATM IV 126.5% vs 11-27 102.2%（差 +24.4pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 191.99 → 今开 176.60（-8.0%） | 较昨收变动（含盘初走势） ｜ 今日高 183.20 ｜ 低 175.12

Options: P/C成交量 0.69 | OI比 1.01 | ATM IV 126.5% | Skew 8.4pp | Term 0.76 | ExpMove ±11.4%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 8.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（4D）±11.4% ｜ 11-27（11D）±14.3% ｜ 12-04（18D）±17.4% ｜ 12-11（25D）±20.1%
   ⇒ IV–VIX Spread: +105.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,210,401 | GEX Change vs 上次快照 -1,749,593 | Flip: Primary Flip: 202.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 531 / LOW 90 / INVALID 177
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 202.13（全链重定价，覆盖 100%）
最近结构参考: Flip 202（现价低于该位 11.6%）
量化视角： 负 Gamma（921万，无历史分位）｜负 Gamma 加深（175万）｜现价位于 Flip 下方 11.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 205（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 202（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 210.0C — Vol 3,279 | 最新价 $14.62 | OI 1997→4426 (ΔOI +2429张) | ΔOI/Volume 74.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2429张（+121.6% vs前日OI），连续性待观察（方向未知）
11-20 155.0C — Vol 1,300 | 最新价 $37.86 | OI 496→1796 (ΔOI +1300张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1300张（+262.1% vs前日OI），连续性待观察（方向未知）
11-20 250.0C — Vol 1,851 | 最新价 $0.37 | OI 4428→5670 (ΔOI +1242张) | ΔOI/Volume 67.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1242张（+28.1% vs前日OI），连续性待观察（方向未知）
11-20 200.0C — Vol 2,419 | 最新价 $7.20 | OI 3142→4287 (ΔOI +1145张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1145张（+36.4% vs前日OI），连续性待观察（方向未知）
12-18 200.0C — Vol 1,469 | 最新价 $18.30 | OI 2962→3937 (ΔOI +975张) | ΔOI/Volume 66.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增975张（+32.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,091 张（Put 0 / Call 7,091），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +8.0k / P +3.4k ｜ Activity HIGH ｜ 4D
11-27  C +1.6k / P +0.3k ｜ Activity HIGH ｜ 11D
12-04  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 18D
12-11  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 91.8k / P 92.4k，今日变化ΔOI: C +8.0k / P +3.4k，平值价格ATM: C $11.05 / P $9.40 ｜ ATM IV 126.5%，净 delta 敞口 234k shares
Top ΔOI: C 155 +1,300 ｜ C 200 +1,145
仓位参考: Max Pain 205 ｜ Call Wall 190（+6.3%，弱）（OI 3.1k） ｜ Put Wall 170（-4.9%，弱）（OI 4.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 126.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 234,258 股

📆 11-27 Forward Structure
存量OI: C 12.4k / P 11.7k，今日变化ΔOI: C +1.6k / P +0.3k，平值价格ATM: C $13.80 / P $11.70 ｜ ATM IV 102.2%，净 delta 敞口 37k shares
Top ΔOI: C 200 +567 ｜ P 200 -255
仓位参考: Max Pain 210 ｜ Put Wall 190（+6.3%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 102.2%｜历史 Rank 81%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,124 股

📆 12-04 Forward Structure
存量OI: C 7.4k / P 7.7k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $16.88 / P $14.30 ｜ ATM IV 99.0%，净 delta 敞口 3k shares
Top ΔOI: C 185 +91 ｜ C 190 +62
仓位参考: Max Pain 200 ｜ Call Wall 195（+9.1%，弱）（OI 0.2k） ｜ Put Wall 185（+3.5%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 99.0%｜历史 Rank 81%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,913 股

12-11（MEDIUM △）Top ΔOI: 165P +30 ｜ 195P +30
12-11（MEDIUM △）仓位参考: Max Pain 210 ｜ Call Wall 195（+9.1%，弱）（OI 0.2k） ｜ Put Wall 175（-2.1%）（OI 2.0k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 126.5% vs 11-27 102.2%（差 +24.4pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/BE_morning.json