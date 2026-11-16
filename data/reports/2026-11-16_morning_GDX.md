# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $663.91
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
🟡 **近现价集中开仓**: 11-20 83C ΔOI +10,284（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 81.64 → 今开 80.46（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 81.79 ｜ 低 80.07

Options: P/C成交量 1.12 | OI比 0.83 | ATM IV 61.3% | Skew 4.3pp | Term 0.70 | ExpMove ±3.3%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价中性（Skew 4.3pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.3% ｜ 11-20（4D）±0.0% ｜ 11-23（7D）±5.5% ｜ 11-25（9D）±0.0%
   ⇒ IV–VIX Spread: +39.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,606,760 | GEX Change vs 上次快照 10,932,000 | Flip: Primary Flip: 82.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 553 / LOW 201 / INVALID 530
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 82.45（全链重定价，覆盖 96%）
最近结构参考: Flip 82（现价低于该位 1.4%）
量化视角： 负 Gamma（2161万，无历史分位）｜负 Gamma 缓解（+1093万）｜现价位于 Flip 下方 1.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 83（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 82（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 83.0C — Vol 10,724 | 最新价 $1.30 | OI 1583→11867 (ΔOI +10284张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10284张（+649.6% vs前日OI），连续性待观察（方向未知）
11-20 55.0P — Vol 10,000 | 最新价 $0.03 | OI 179→10172 (ΔOI +9993张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9993张（+5582.7% vs前日OI），连续性待观察（方向未知）
11-20 86.0C — Vol 10,128 | 最新价 $0.46 | OI 2813→11641 (ΔOI +8828张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8828张（+313.8% vs前日OI），连续性待观察（方向未知）
11-20 87.0C — Vol 7,869 | 最新价 $0.32 | OI 12414→19991 (ΔOI +7577张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7577张（+61.0% vs前日OI），连续性待观察（方向未知）
11-20 84.0C — Vol 7,727 | 最新价 $0.91 | OI 17690→22258 (ΔOI +4568张) | ΔOI/Volume 59.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4568张（+25.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 41,250 张（Put 9,993 / Call 31,257），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 4.2k / P 3.5k，今日成交量: C 2.9k / P 3.2k，平值价格ATM: C $0.62 / P $0.46 ｜ ATM IV 61.3%，预期波动 ±1.3%，Max Pain 83
Top ΔOI: P 79 +426 ｜ C 82 +245 ｜ C 81 +156

📆 Forward Expiration Structure

11-18  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 2D
11-20  C +32.7k / P +13.2k ｜ Activity HIGH ｜ 4D
11-23  C +74 / P +46 ｜ Activity MEDIUM △ ｜ 7D
11-25  C +98 / P +65 ｜ Activity MEDIUM △ ｜ 9D

📆 11-18 Forward Structure
存量OI: C 1.6k / P 1.4k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $1.50 / P $1.18 ｜ ATM IV 52.7%，净 delta 敞口 -3k shares
Top ΔOI: C 86 +300 ｜ C 85 +127
仓位参考: Max Pain 84 ｜ Call Wall 86（+5.8%）（OI 0.4k） ｜ Put Wall 84（+3.4%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 52.7%｜历史 Rank 94%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,011 股

📆 11-20 Forward Structure
存量OI: C 167.8k / P 183.6k，今日变化ΔOI: C +32.7k / P +13.2k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 48.9%，净 delta 敞口 825k shares
Top ΔOI: C 83 +10,284 ｜ C 86 +8,828
仓位参考: Max Pain 84 ｜ Call Wall 84（+3.4%，弱）（OI 22.3k） ｜ Put Wall 80（-1.5%，弱）（OI 24.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.9%｜历史 Rank 94%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 825,155 股

11-23（MEDIUM △）Top ΔOI: 81P +38 ｜ 86C +31
11-23（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 86（+5.8%，弱）（OI 40） ｜ Put Wall 81（-0.3%，弱）（OI 40）

11-25（MEDIUM △）Top ΔOI: 80P +41 ｜ 88C +39
11-25（MEDIUM △）仓位参考: Max Pain 84 ｜ Call Wall 83（+2.1%）（OI 0.2k） ｜ Put Wall 80（-1.5%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/GDX_morning.json