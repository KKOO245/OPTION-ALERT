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
🔴 **事件差分**: 10-21（1D）ATM IV 154.6% vs 10-23 109.0%（差 +45.6pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-21 140P ΔOI -1,892（距现价 -3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 85P ΔOI +1,500 占该期限总 OI 13.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 147.96 → 今开 146.13（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 147.54 ｜ 低 143.27

Options: P/C成交量 0.89 | OI比 0.80 | ATM IV 154.6% | Skew 4.0pp | Term 0.38 | ExpMove ±7.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.38，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-21（1D）±7.2% ｜ 10-23（3D）±8.3% ｜ 10-26（6D）±8.6% ｜ 10-28（8D）±8.8%
   ⇒ IV–VIX Spread: +136.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,791,703 | GEX Change vs 上次快照 -2,312,480 | Flip: Primary Flip: 147.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 866 / LOW 56 / INVALID 588
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.09（全链重定价，覆盖 100%）
Put Wall 140（弱结构｜现价高于该位 3.7%）
最近结构参考: Flip 147（现价低于该位 1.3%）
量化视角： 负 Gamma（1079万，无历史分位）｜负 Gamma 加深（231万）｜现价位于 Flip 下方 1.30%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 149（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 170.0C — Vol 21,939 | 最新价 $0.65 | OI 5848→21371 (ΔOI +15523张) | ΔOI/Volume 70.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15523张（+265.4% vs前日OI），连续性待观察（方向未知）
10-23 167.5C — Vol 16,742 | 最新价 $0.80 | OI 3504→16859 (ΔOI +13355张) | ΔOI/Volume 79.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13355张（+381.1% vs前日OI），连续性待观察（方向未知）
10-21 155.0C — Vol 19,249 | 最新价 $2.52 | OI 4230→10280 (ΔOI +6050张) | ΔOI/Volume 31.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6050张（+143.0% vs前日OI），连续性待观察（方向未知）
10-23 80.0P — Vol 5,491 | 最新价 $0.02 | OI 6594→11558 (ΔOI +4964张) | ΔOI/Volume 90.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4964张（+75.3% vs前日OI），连续性待观察（方向未知）
11-20 100.0P — Vol 5,793 | 最新价 $0.40 | OI 20505→25430 (ΔOI +4925张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4925张（+24.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 44,817 张（Put 9,889 / Call 34,928），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-21  C +19.8k / P +9.8k ｜ Activity HIGH ｜ 1D
10-23  C +46.2k / P +22.7k ｜ Activity HIGH ｜ 3D
10-26  C +3.2k / P +2.1k ｜ Activity HIGH ｜ 6D
10-28  C +0.5k / P +2.1k ｜ Activity HIGH ｜ 8D

📆 10-21 Forward Structure
存量OI: C 50.7k / P 40.6k，今日变化ΔOI: C +19.8k / P +9.8k，平值价格ATM: C $5.40 / P $5.10 ｜ ATM IV 154.6%，净 delta 敞口 306k shares
Top ΔOI: C 155 +6,050 ｜ P 140 -1,892
仓位参考: Max Pain 149 ｜ Call Wall 155（+6.8%）（OI 10.3k） ｜ Put Wall 135（-7.0%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 154.6%｜历史 Rank 100%（近端代理）｜IV/RV 3.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 305,742 股

📆 10-23 Forward Structure
存量OI: C 153.4k / P 152.5k，今日变化ΔOI: C +46.2k / P +22.7k，平值价格ATM: C $6.15 / P $5.95 ｜ ATM IV 109.0%，净 delta 敞口 282k shares
Top ΔOI: C 170 +15,523 ｜ C 167 +13,355
仓位参考: Max Pain 150 ｜ Call Wall 155（+6.8%，弱）（OI 9.9k） ｜ Put Wall 140（-3.6%，弱）（OI 14.5k）
量化解读： 存量两侧均衡｜ATM IV 109.0%｜历史 Rank 100%（近端代理）｜IV/RV 2.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 281,892 股

📆 10-26 Forward Structure
存量OI: C 9.2k / P 5.7k，今日变化ΔOI: C +3.2k / P +2.1k，平值价格ATM: C $6.30 / P $6.12 ｜ ATM IV 83.0%，净 delta 敞口 13k shares
Top ΔOI: C 150 +850 ｜ P 140 +609
仓位参考: Max Pain 149 ｜ Call Wall 150（+3.3%，弱）（OI 1.4k） ｜ Put Wall 144（-0.8%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 83.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,353 股

📆 10-28 Forward Structure
存量OI: C 2.8k / P 8.4k，今日变化ΔOI: C +0.5k / P +2.1k，平值价格ATM: C $6.70 / P $6.15 ｜ ATM IV 78.2%，净 delta 敞口 -19k shares
Top ΔOI: P 150 +304 ｜ C 155 +99
仓位参考: Max Pain 150 ｜ Call Wall 150（+3.3%，弱）（OI 0.3k） ｜ Put Wall 148（+1.9%）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 78.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.58×（近似）｜净 delta 敞口 负 18,518 股

📅 事件差分（观察，非因果）: 10-21（1D）ATM IV 154.6% vs 10-23 109.0%（差 +45.6pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=59 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=59）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SPCX_morning.json