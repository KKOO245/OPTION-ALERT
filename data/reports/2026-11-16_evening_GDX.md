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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 80.46 → 收盘 78.95（-1.9%） ｜ 今日高 81.80 ｜ 低 78.83 ｜ 昨收 81.64 → 收盘 78.95（-3.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 0.88 | OI比 0.83 | ATM IV 95.2% | Skew 30.4pp | Term 0.48 | ExpMove ±3.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价显著（Skew 30.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.0% ｜ 11-20（4D）±4.4% ｜ 11-23（7D）±7.7% ｜ 11-25（9D）±2.8%
   ⇒ IV–VIX Spread: +72.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -49,083,211 | GEX Change vs 上次快照 -27,476,451 | Flip: Primary Flip: 81.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 512 / LOW 216 / INVALID 556
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 81.86（全链重定价，覆盖 94%）
Put Wall 75（弱结构｜现价高于该位 5.3%）
最近结构参考: Flip 82（现价低于该位 3.6%）
量化视角： 负 Gamma（4908万，无历史分位）｜负 Gamma 加深（2748万）｜现价位于 Flip 下方 3.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构）；上方 83（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 82（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 83.0C — Vol 326 | 最新价 $0.43 | OI 1583→11867 (ΔOI +10284张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10284张（+649.6% vs前日OI），连续性待观察（方向未知）
11-20 55.0P — Vol 10,000（Yahoo补） | 最新价 $0.03 | OI 179→10172 (ΔOI +9993张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9993张（+5582.7% vs前日OI），连续性待观察（方向未知）
11-20 86.0C — Vol 1,152 | 最新价 $0.11 | OI 2813→11641 (ΔOI +8828张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8828张（+313.8% vs前日OI），连续性待观察（方向未知）
11-20 87.0C — Vol 93 | 最新价 $0.06 | OI 12414→19991 (ΔOI +7577张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7577张（+61.0% vs前日OI），连续性待观察（方向未知）
11-20 84.0C — Vol 520 | 最新价 $0.26 | OI 17690→22258 (ΔOI +4568张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4568张（+25.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 41,250 张（Put 9,993 / Call 31,257），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-18  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 2D
11-20  C +32.7k / P +13.2k ｜ Activity HIGH ｜ 4D
11-23  C +74 / P +46 ｜ Activity HIGH ｜ 7D
11-25  C +98 / P +65 ｜ Activity HIGH ｜ 9D

📆 11-18 Forward Structure
存量OI: C 1.6k / P 1.4k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $1.15 / P $1.21 ｜ ATM IV 53.1%，净 delta 敞口 -12k shares
Top ΔOI: C 86 +300 ｜ C 85 +127
仓位参考: Max Pain 84 ｜ Put Wall 84（+6.4%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 53.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,767 股

📆 11-20 Forward Structure
存量OI: C 167.8k / P 183.6k，今日变化ΔOI: C +32.7k / P +13.2k，平值价格ATM: C $1.85 / P $1.65 ｜ ATM IV 51.5%，净 delta 敞口 355k shares
Top ΔOI: C 83 +10,284 ｜ C 86 +8,828
仓位参考: Max Pain 84 ｜ Call Wall 84（+6.4%，弱）（OI 22.3k） ｜ Put Wall 80（+1.3%，弱）（OI 24.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.5%｜历史 Rank 100%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 355,192 股

📆 11-23 Forward Structure
存量OI: C 0.4k / P 0.3k，今日变化ΔOI: C +74 / P +46，平值价格ATM: C $4.60 / P $1.50 ｜ ATM IV 43.6%，净 delta 敞口 -2k shares
Top ΔOI: P 81 +38 ｜ C 86 +31
仓位参考: Max Pain 86 ｜ Call Wall 83（+5.1%，弱）（OI 24） ｜ Put Wall 81（+2.6%，弱）（OI 40）
量化解读： 存量 Call 重｜ATM IV 43.6%｜历史 Rank 100%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,155 股

📆 11-25 Forward Structure
存量OI: C 0.3k / P 0.4k，今日变化ΔOI: C +98 / P +65，平值价格ATM: C $0.00 / P $2.19 ｜ ATM IV 47.2%，净 delta 敞口 -1k shares
Top ΔOI: P 80 +41 ｜ C 86 +30
仓位参考: Max Pain 84 ｜ Call Wall 83（+5.1%）（OI 0.2k） ｜ Put Wall 80（+1.3%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.2%｜历史 Rank 100%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 1,205 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/GDX_evening.json