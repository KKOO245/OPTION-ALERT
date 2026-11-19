# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $735.61 ｜ QQQ $nan
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 149.8% vs 11-27 110.2%（差 +39.6pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 780C ΔOI +1,106（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 797.24 → 今开 805.87（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 813.18 ｜ 低 753.86

Options: P/C成交量 0.82 | OI比 0.61 | ATM IV 149.8% | Skew 10.3pp | Term 0.69 | ExpMove ±9.5%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 10.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±9.5% ｜ 11-27（9D）±13.8% ｜ 12-04（16D）±18.2% ｜ 12-11（23D）±21.4%
   ⇒ IV–VIX Spread: +125.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,503,169 | GEX Change vs 上次快照 1,404,227 | Flip: Primary Flip: 830.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1686 / LOW 714 / INVALID 1096
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 830.16（全链重定价，覆盖 100%）
最近结构参考: Flip 830（现价低于该位 6.1%）
量化视角： 负 Gamma（350万，无历史分位）｜负 Gamma 缓解（+140万）｜现价位于 Flip 下方 6.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 920（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 830（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 1000.0C — Vol 3,961 | 最新价 $2.64 | OI 4197→5516 (ΔOI +1319张) | ΔOI/Volume 33.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1319张（+31.4% vs前日OI），连续性待观察（方向未知）
11-20 780.0C — Vol 2,266 | 最新价 $54.13 | OI 92→1198 (ΔOI +1106张) | ΔOI/Volume 48.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1106张（+1202.2% vs前日OI），连续性待观察（方向未知）
12-18 680.0P — Vol 714 | 最新价 $45.99 | OI 259→812 (ΔOI +553张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增553张（+213.5% vs前日OI），连续性待观察（方向未知）
11-20 950.0C — Vol 2,091 | 最新价 $5.54 | OI 1274→1747 (ΔOI +473张) | ΔOI/Volume 22.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增473张（+37.1% vs前日OI），连续性待观察（方向未知）
12-18 890.0C — Vol 564 | 最新价 $59.50 | OI 102→569 (ΔOI +467张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增467张（+457.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,918 张（Put 553 / Call 3,365），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +5.9k / P +0.9k ｜ Activity HIGH ｜ 2D
11-27  C +1.5k / P +0.4k ｜ Activity HIGH ｜ 9D
12-04  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 16D
12-11  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 100.2k / P 60.9k，今日变化ΔOI: C +5.9k / P +0.9k，平值价格ATM: C $35.70 / P $38.40 ｜ ATM IV 149.8%，净 delta 敞口 306k shares
Top ΔOI: C 1000 +1,319 ｜ C 780 +1,106
仓位参考: Max Pain 920 ｜ Call Wall 800（+2.6%，弱）（OI 1.8k） ｜ Put Wall 800（+2.6%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 149.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 306,370 股

📆 11-27 Forward Structure
存量OI: C 23.6k / P 13.3k，今日变化ΔOI: C +1.5k / P +0.4k，平值价格ATM: C $53.40 / P $54.50 ｜ ATM IV 110.2%，净 delta 敞口 61k shares
Top ΔOI: C 900 +153 ｜ C 800 +127
仓位参考: Max Pain 930 ｜ Call Wall 850（+9.0%，弱）（OI 0.5k） ｜ Put Wall 800（+2.6%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 110.2%｜历史 Rank 92%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 61,463 股

📆 12-04 Forward Structure
存量OI: C 11.6k / P 6.9k，今日变化ΔOI: C +0.6k / P +0.2k，平值价格ATM: C $70.85 / P $70.75 ｜ ATM IV 106.8%，净 delta 敞口 9k shares
仓位参考: Max Pain 945 ｜ Put Wall 820（+5.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 106.8%｜历史 Rank 92%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,767 股

12-11（MEDIUM △）Top ΔOI: 630P +31 ｜ 1550P -22
12-11（MEDIUM △）仓位参考: Max Pain 900 ｜ Call Wall 840（+7.7%，弱）（OI 63） ｜ Put Wall 830（+6.4%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 149.8% vs 11-27 110.2%（差 +39.6pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/SNDK_morning.json