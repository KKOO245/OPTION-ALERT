# 期权晚报 2026-11-16（快照 16:40 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
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
🟡 **近现价集中开仓**: 11-17 285C ΔOI +1,434（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 276.10 → 收盘 272.94（-1.1%） ｜ 今日高 276.54 ｜ 低 271.97 ｜ 昨收 277.54 → 收盘 272.94（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 1.83 | OI比 1.34 | ATM IV 21.9% | Skew 5.3pp | Term 0.97 | ExpMove ±1.1%（近端） | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 5.3pp）｜当日成交偏 Put（P/C量 1.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.83×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-17（1D）±1.1% ｜ 11-18（2D）±1.5% ｜ 11-19（3D）±1.8% ｜ 11-20（4D）±2.1%
   ⇒ IV–VIX Spread: -1.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,497,648,267 | GEX Change vs 上次快照 -209,230,704 | Flip: Primary Flip: 285.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1208 / LOW 258 / INVALID 1092
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 285.62（全链重定价，覆盖 96%）
Put Wall 270（弱结构｜现价高于该位 1.1%） | Call Wall 300（弱结构｜现价低于该位 9.0%）
最近结构参考: Put Wall 270（现价高于该位 1.1%）
量化视角： 负 Gamma（14.98亿，无历史分位）｜负 Gamma 加深（2.09亿）｜现价位于 Flip 下方 4.44%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 278（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 286（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 263.0P — Vol 32,389 | 最新价 $3.76 | OI 10776→40201 (ΔOI +29425张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29425张（+273.1% vs前日OI），连续性待观察（方向未知）
11-20 268.0P — Vol 33,035 | 最新价 $1.26 | OI 71609→93596 (ΔOI +21987张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21987张（+30.7% vs前日OI），连续性待观察（方向未知）
12-18 260.0P — Vol 38,182 | 最新价 $3.11 | OI 131399→138442 (ΔOI +7043张) | ΔOI/Volume 18.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7043张（+5.4% vs前日OI），连续性待观察（方向未知）
12-18 200.0P — Vol 18 | 最新价 $0.20 | OI 78047→82676 (ΔOI +4629张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增4629张（+5.9% vs前日OI），值得跟踪（方向未知）
11-20 210.0P — Vol 2 | 最新价 $0.01 | OI 4538→9153 (ΔOI +4615张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4615张（+101.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 67,699 张（Put 67,699 / Call 0），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $16M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-17  C +3.5k / P +3.6k ｜ Activity HIGH ｜ 1D
11-18  C +3.4k / P +5.1k ｜ Activity HIGH ｜ 2D
11-19  C +8.7k / P +16.1k ｜ Activity HIGH ｜ 3D
11-20  C +2.6k / P -8.2k ｜ Activity MEDIUM △ ｜ 4D

📆 11-17 Forward Structure
存量OI: C 13.1k / P 16.4k，今日变化ΔOI: C +3.5k / P +3.6k，平值价格ATM: C $1.42 / P $1.55 ｜ ATM IV 25.9%，净 delta 敞口 -190k shares
Top ΔOI: C 285 +1,434 ｜ P 274 +1,019 ｜ P 280 +751
仓位参考: Max Pain 280 ｜ Call Wall 285（+4.4%）（OI 2.2k） ｜ Put Wall 274（+0.4%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 25.9%｜历史 Rank 41%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 190,195 股

📆 11-18 Forward Structure
存量OI: C 16.1k / P 18.0k，今日变化ΔOI: C +3.4k / P +5.1k，平值价格ATM: C $2.01 / P $2.03 ｜ ATM IV 25.2%，净 delta 敞口 -229k shares
Top ΔOI: P 275 +2,178 ｜ C 278 +1,872 ｜ P 278 +686
仓位参考: Max Pain 278 ｜ Call Wall 278（+1.9%，弱）（OI 2.0k） ｜ Put Wall 275（+0.8%）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 25.2%｜历史 Rank 41%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 228,804 股

📆 11-19 Forward Structure
存量OI: C 13.8k / P 24.5k，今日变化ΔOI: C +8.7k / P +16.1k，平值价格ATM: C $2.53 / P $2.46 ｜ ATM IV 25.4%，净 delta 敞口 -361k shares
Top ΔOI: P 272 +3,581 ｜ C 287 +3,058 ｜ P 262 +2,996
仓位参考: Max Pain 279 ｜ Call Wall 287（+5.2%）（OI 3.4k） ｜ Put Wall 272（-0.3%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜ATM IV 25.4%｜历史 Rank 41%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 361,295 股

11-20（MEDIUM △）Top ΔOI: 270P -28,455 ｜ 268P +21,987
11-20（MEDIUM △）仓位参考: Max Pain 280 ｜ Call Wall 285（+4.4%，弱）（OI 53.5k） ｜ Put Wall 265（-2.9%，弱）（OI 139.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/IWM_evening.json