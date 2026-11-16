# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $664.07
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 35.1（fear）
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
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-17 285C ΔOI +1,434（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 277.54 → 今开 276.10（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 276.54 ｜ 低 274.25

Options: P/C成交量 2.10 | OI比 1.34 | ATM IV 31.0% | Skew 4.1pp | Term 0.65 | ExpMove ±1.2%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜当日成交偏 Put（P/C量 2.10）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.10×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-17（1D）±1.2% ｜ 11-18（2D）±1.6% ｜ 11-19（3D）±1.7% ｜ 11-20（4D）±0.0%
   ⇒ IV–VIX Spread: +9.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,288,417,563 | GEX Change vs 上次快照 -340,358,545 | Flip: Primary Flip: 283.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1284 / LOW 224 / INVALID 1050
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.60（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 1.8%） | Call Wall 300（弱结构｜现价低于该位 8.4%）
最近结构参考: Put Wall 270（现价高于该位 1.8%）
量化视角： 负 Gamma（12.88亿，无历史分位）｜负 Gamma 加深（3.40亿）｜现价位于 Flip 下方 3.06%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 278（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 263.0P — Vol 40,099 | 最新价 $2.50 | OI 10776→40201 (ΔOI +29425张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29425张（+273.1% vs前日OI），连续性待观察（方向未知）
11-20 268.0P — Vol 25,788 | 最新价 $0.60 | OI 71609→93596 (ΔOI +21987张) | ΔOI/Volume 85.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21987张（+30.7% vs前日OI），连续性待观察（方向未知）
12-18 260.0P — Vol 9,063 | 最新价 $2.10 | OI 131399→138442 (ΔOI +7043张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7043张（+5.4% vs前日OI），连续性待观察（方向未知）
12-18 200.0P — Vol 10,012 | 最新价 $0.15 | OI 78047→82676 (ΔOI +4629张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4629张（+5.9% vs前日OI），连续性待观察（方向未知）
11-20 210.0P — Vol 5,003 | 最新价 $0.02 | OI 4538→9153 (ΔOI +4615张) | ΔOI/Volume 92.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4615张（+101.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 67,699 张（Put 67,699 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 33.1k / P 44.3k，今日成交量: C 40.5k / P 84.9k，平值价格ATM: C $0.74 / P $1.10 ｜ ATM IV 31.0%，预期波动 ±0.7%，Max Pain 278
Top ΔOI: P 272 +3,289 ｜ C 280 +2,899 ｜ P 270 +2,200

📆 Forward Expiration Structure

11-17  C +3.5k / P +3.6k ｜ Activity HIGH ｜ 1D
11-18  C +3.4k / P +5.1k ｜ Activity HIGH ｜ 2D
11-19  C +8.7k / P +16.1k ｜ Activity HIGH ｜ 3D
11-20  C +2.6k / P -8.2k ｜ Activity HIGH ｜ 4D

📆 11-17 Forward Structure
存量OI: C 13.1k / P 16.4k，今日变化ΔOI: C +3.5k / P +3.6k，平值价格ATM: C $1.45 / P $1.80 ｜ ATM IV 25.1%，净 delta 敞口 -138k shares
Top ΔOI: C 285 +1,434 ｜ P 274 +1,019 ｜ P 280 +751
仓位参考: Max Pain 280 ｜ Call Wall 285（+3.7%）（OI 2.2k） ｜ Put Wall 274（-0.3%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 25.1%｜历史 Rank 73%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 138,432 股

📆 11-18 Forward Structure
存量OI: C 16.1k / P 18.0k，今日变化ΔOI: C +3.4k / P +5.1k，平值价格ATM: C $1.99 / P $2.30 ｜ ATM IV 24.3%，净 delta 敞口 -131k shares
Top ΔOI: P 275 +2,178 ｜ C 278 +1,872 ｜ P 278 +686
仓位参考: Max Pain 278 ｜ Call Wall 278（+1.1%，弱）（OI 2.0k） ｜ Put Wall 275（+0.0%）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 24.3%｜历史 Rank 73%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 130,717 股

📆 11-19 Forward Structure
存量OI: C 13.8k / P 24.5k，今日变化ΔOI: C +8.7k / P +16.1k，平值价格ATM: C $2.40 / P $2.36 ｜ ATM IV 24.1%，净 delta 敞口 -224k shares
Top ΔOI: P 272 +3,581 ｜ C 287 +3,058 ｜ P 262 +2,996
仓位参考: Max Pain 279 ｜ Call Wall 287（+4.4%）（OI 3.4k） ｜ Put Wall 272（-1.1%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜ATM IV 24.1%｜历史 Rank 73%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 负 224,342 股

📆 11-20 Forward Structure
存量OI: C 562.4k / P 1538.0k，今日变化ΔOI: C +2.6k / P -8.2k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 558k shares
Top ΔOI: P 270 -28,455 ｜ P 268 +21,987 ｜ P 272 -10,688
仓位参考: Max Pain 280 ｜ Call Wall 285（+3.7%，弱）（OI 53.5k） ｜ Put Wall 265（-3.6%，弱）（OI 139.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜净 delta 敞口 正 557,685 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/IWM_morning.json