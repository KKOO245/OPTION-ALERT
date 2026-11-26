# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
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
🟡 **近现价集中开仓**: 12-18 75P ΔOI +1,713（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 77.55 → 今开 74.24（-4.3%） | 较昨收变动（含盘初走势） ｜ 今日高 74.95 ｜ 低 70.37

Options: P/C成交量 1.38 | OI比 0.56 | ATM IV 122.9% | Skew 11.7pp | Term 0.90 | ExpMove ±7.5%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价显著（Skew 11.7pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.56）+ 当日成交偏 Put（P/C量 1.38）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±7.5% ｜ 12-04（9D）±15.4% ｜ 12-11（16D）±19.6% ｜ 12-18（23D）±22.7%
   ⇒ IV–VIX Spread: +91.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,179,997 | GEX Change vs 上次快照 -2,481,551 | Flip: Primary Flip: 78.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 571 / LOW 216 / INVALID 245
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 78.44（全链重定价，覆盖 100%）
Put Wall 80（弱结构｜现价低于该位 8.0%）
最近结构参考: Flip 78（现价低于该位 6.1%）
量化视角： 负 Gamma（2018万，无历史分位）｜负 Gamma 加深（248万）｜现价位于 Flip 下方 6.11%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 80（Put Wall，弱结构） / 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 78（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 80.0C — Vol 8,532 | 最新价 $4.60 | OI 97→7153 (ΔOI +7056张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7056张（+7274.2% vs前日OI），连续性待观察（方向未知）
12-04 80.0P — Vol 8,006 | 最新价 $6.90 | OI 4829→8766 (ΔOI +3937张) | ΔOI/Volume 49.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3937张（+81.5% vs前日OI），连续性待观察（方向未知）
12-18 65.0P — Vol 4,693 | 最新价 $3.50 | OI 2990→6102 (ΔOI +3112张) | ΔOI/Volume 66.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3112张（+104.1% vs前日OI），连续性待观察（方向未知）
11-27 87.0C — Vol 4,019 | 最新价 $0.44 | OI 1174→3860 (ΔOI +2686张) | ΔOI/Volume 66.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2686张（+228.8% vs前日OI），连续性待观察（方向未知）
11-27 79.0C — Vol 4,168 | 最新价 $2.38 | OI 132→2525 (ΔOI +2393张) | ΔOI/Volume 57.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2393张（+1812.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,184 张（Put 7,049 / Call 12,135），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C -7.5k / P -15.9k ｜ Activity HIGH ｜ 2D
12-04  C +16.5k / P +7.1k ｜ Activity HIGH ｜ 9D
12-11  C +1.5k / P +2.5k ｜ Activity HIGH ｜ 16D
12-18  C +2.1k / P -1.3k ｜ Activity HIGH ｜ 23D

📆 11-27 Forward Structure
存量OI: C 262.3k / P 145.7k，今日变化ΔOI: C -7.5k / P -15.9k，平值价格ATM: C $2.70 / P $2.86 ｜ ATM IV 122.9%，净 delta 敞口 2.0M shares
Top ΔOI: P 100 -5,700
仓位参考: Max Pain 85 ｜ Put Wall 80（+8.6%，弱）（OI 7.9k）
量化解读： 存量 Call 重｜ATM IV 122.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,974,937 股

📆 12-04 Forward Structure
存量OI: C 60.4k / P 78.8k，今日变化ΔOI: C +16.5k / P +7.1k，平值价格ATM: C $5.60 / P $5.77 ｜ ATM IV 121.8%，净 delta 敞口 132k shares
Top ΔOI: C 80 +7,056 ｜ P 80 +3,937 ｜ C 101 +1,730
仓位参考: Max Pain 86 ｜ Call Wall 80（+8.6%，弱）（OI 7.2k） ｜ Put Wall 80（+8.6%，弱）（OI 8.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 121.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 132,067 股

📆 12-11 Forward Structure
存量OI: C 13.4k / P 39.6k，今日变化ΔOI: C +1.5k / P +2.5k，平值价格ATM: C $6.95 / P $7.45 ｜ ATM IV 116.9%，净 delta 敞口 66k shares
Top ΔOI: P 60 +1,082 ｜ P 55 +777
仓位参考: Max Pain 100 ｜ Put Wall 80（+8.6%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜ATM IV 116.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 65,744 股

📆 12-18 Forward Structure
存量OI: C 247.1k / P 170.8k，今日变化ΔOI: C +2.1k / P -1.3k，平值价格ATM: C $8.17 / P $8.56 ｜ ATM IV 112.9%，净 delta 敞口 834k shares
Top ΔOI: P 160 -7,884 ｜ P 65 +3,112 ｜ P 75 +1,713
仓位参考: Max Pain 115 ｜ Put Wall 80（+8.6%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 112.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 正 834,236 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/MSTR_morning.json