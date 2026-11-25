# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $610.21
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 123P ΔOI +1,401（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-11 120P ΔOI +4,958 占该期限总 OI 25.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 128.62 → 今开 121.21（-5.8%） | 较昨收变动（含盘初走势） ｜ 今日高 122.74 ｜ 低 118.66

Options: P/C成交量 1.21 | OI比 0.44 | ATM IV 91.7% | Skew 8.9pp | Term 0.81 | ExpMove ±6.7%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.44）+ 当日成交偏 Put（P/C量 1.21）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±6.7% ｜ 12-04（9D）±14.3% ｜ 12-11（16D）±8.4% ｜ 12-18（23D）±18.6%
   ⇒ IV–VIX Spread: +60.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -30,789,076 | GEX Change vs 上次快照 -5,384,182 | Flip: Primary Flip: 135.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 633 / LOW 320 / INVALID 571
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 135.68（全链重定价，覆盖 99%）
Put Wall 125（弱结构｜现价低于该位 2.7%）
最近结构参考: Put Wall 125（现价低于该位 2.7%）
量化视角： 负 Gamma（3079万，无历史分位）｜负 Gamma 加深（538万）｜现价位于 Flip 下方 10.39%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 125（Put Wall，弱结构） / 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 136（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 140.0C — Vol 20,025 | 最新价 $4.65 | OI 2582→9233 (ΔOI +6651张) | ΔOI/Volume 33.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6651张（+257.6% vs前日OI），连续性待观察（方向未知）
12-11 120.0P — Vol 6,738 | 最新价 $4.96 | OI 532→5490 (ΔOI +4958张) | ΔOI/Volume 73.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4958张（+932.0% vs前日OI），连续性待观察（方向未知）
12-24 120.0P — Vol 3,749 | 最新价 $6.60 | OI 573→4003 (ΔOI +3430张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3430张（+598.6% vs前日OI），连续性待观察（方向未知）
12-18 135.0C — Vol 3,530 | 最新价 $6.40 | OI 393→3563 (ΔOI +3170张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3170张（+806.6% vs前日OI），连续性待观察（方向未知）
12-18 123.33P — Vol 3,030 | 最新价 $6.95 | OI 574→3538 (ΔOI +2964张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2964张（+516.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,173 张（Put 11,352 / Call 9,821），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +1.7k / P -4.2k ｜ Activity HIGH ｜ 2D
12-04  C +2.7k / P +3.7k ｜ Activity HIGH ｜ 9D
12-11  C +1.7k / P +7.5k ｜ Activity HIGH ｜ 16D
12-18  C +16.4k / P +5.7k ｜ Activity HIGH ｜ 23D

📆 11-27 Forward Structure
存量OI: C 75.9k / P 33.2k，今日变化ΔOI: C +1.7k / P -4.2k，平值价格ATM: C $3.49 / P $4.70 ｜ ATM IV 91.7%，净 delta 敞口 574k shares
Top ΔOI: P 163 -2,591 ｜ P 150 -1,371
仓位参考: Max Pain 140 ｜ Put Wall 120（-1.3%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 91.7%｜历史 Rank 99%（近端代理）｜IV/RV 0.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 573,893 股

📆 12-04 Forward Structure
存量OI: C 16.7k / P 57.8k，今日变化ΔOI: C +2.7k / P +3.7k，平值价格ATM: C $10.50 / P $6.87 ｜ ATM IV 83.8%，净 delta 敞口 -57k shares
Top ΔOI: P 110 +1,450 ｜ P 123 +1,401 ｜ C 149 +800
仓位参考: Max Pain 149 ｜ Put Wall 122（+0.3%，弱）（OI 5.1k）
量化解读： 存量 Put 重｜ATM IV 83.8%｜历史 Rank 99%（近端代理）｜IV/RV 0.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 56,752 股

📆 12-11 Forward Structure
存量OI: C 6.9k / P 12.3k，今日变化ΔOI: C +1.7k / P +7.5k，平值价格ATM: C $8.00 / P $2.18 ｜ ATM IV 81.7%，净 delta 敞口 -275k shares
Top ΔOI: P 120 +4,958 ｜ C 135 +1,002 ｜ P 115 +987
仓位参考: Max Pain 140 ｜ Put Wall 120（-1.3%）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 81.7%｜历史 Rank 99%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 274,808 股

📆 12-18 Forward Structure
存量OI: C 275.9k / P 210.4k，今日变化ΔOI: C +16.4k / P +5.7k，平值价格ATM: C $12.40 / P $10.23 ｜ ATM IV 80.0%，净 delta 敞口 203k shares
Top ΔOI: C 140 +6,651 ｜ C 135 +3,170 ｜ P 123 +2,964
仓位参考: Max Pain 155 ｜ Put Wall 125（+2.8%）（OI 34.2k）
量化解读： 存量 Call 重｜ATM IV 80.0%｜历史 Rank 99%（近端代理）｜IV/RV 0.18×（近似）｜净 delta 敞口 正 203,029 股

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 91.7% vs 12-04 83.8%（差 +7.9pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SOXX_morning.json