# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.00 ｜ QQQ $659.51
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
🟡 **事件差分**: 11-20 ATM IV 56.4% vs 11-23 45.7%（差 +10.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-23 41P ΔOI +605（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 42.64 → 今开 41.23（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 41.25 ｜ 低 40.69

Options: P/C成交量 0.73 | OI比 0.44 | ATM IV 61.7% | Skew 4.7pp | Term 0.75 | ExpMove ±3.6%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 4.7pp）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±3.6% ｜ 11-23（5D）±4.5% ｜ 11-25（7D）±5.7% ｜ 11-27（9D）±6.1%
   ⇒ IV–VIX Spread: +37.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -30,408,865 | GEX Change vs 上次快照 -26,407,563 | Flip: Primary Flip: 41.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 623 / LOW 198 / INVALID 425
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 41.72（全链重定价，覆盖 90%）
Put Wall 40（弱结构｜现价高于该位 1.8%）
最近结构参考: Put Wall 40（现价高于该位 1.8%）
量化视角： 负 Gamma（3041万，无历史分位）｜负 Gamma 加深（2641万）｜现价位于 Flip 下方 2.37%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall，弱结构）；上方 43（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 42（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 63.0C — Vol 15,056 | 最新价 $0.05 | OI 18987→33327 (ΔOI +14340张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14340张（+75.5% vs前日OI），连续性待观察（方向未知）
12-18 43.0P — Vol 11,708 | 最新价 $2.24 | OI 3204→13393 (ΔOI +10189张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10189张（+318.0% vs前日OI），连续性待观察（方向未知）
12-18 50.0C — Vol 7,301 | 最新价 $0.32 | OI 17427→22618 (ΔOI +5191张) | ΔOI/Volume 71.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5191张（+29.8% vs前日OI），连续性待观察（方向未知）
12-18 48.0C — Vol 5,962 | 最新价 $0.54 | OI 2568→7743 (ΔOI +5175张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5175张（+201.5% vs前日OI），连续性待观察（方向未知）
11-20 43.5C — Vol 5,502 | 最新价 $0.46 | OI 916→5021 (ΔOI +4105张) | ΔOI/Volume 74.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4105张（+448.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 39,000 张（Put 10,189 / Call 28,811），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 37.7k / P 16.5k，今日成交量: C 9.9k / P 7.2k，平值价格ATM: C $0.43 / P $0.15 ｜ ATM IV 61.7%，预期波动 ±1.4%，Max Pain 43
Top ΔOI: C 43 +2,105 ｜ C 46 +534 ｜ C 44 +403

📆 Forward Expiration Structure

11-20  C +8.0k / P -2.1k ｜ Activity HIGH ｜ 2D
11-23  C +2.8k / P +1.3k ｜ Activity HIGH ｜ 5D
11-25  C +2.5k / P +1.9k ｜ Activity HIGH ｜ 7D
11-27  C +4.5k / P +1.2k ｜ Activity HIGH ｜ 9D

📆 11-20 Forward Structure
存量OI: C 600.7k / P 154.9k，今日变化ΔOI: C +8.0k / P -2.1k，平值价格ATM: C $0.62 / P $0.85 ｜ ATM IV 56.4%，净 delta 敞口 475k shares
Top ΔOI: C 43 +4,105 ｜ P 52 -2,684
仓位参考: Max Pain 48 ｜ Put Wall 40（-1.8%，弱）（OI 15.1k）
量化解读： 存量 Call 重｜ATM IV 56.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 474,966 股

📆 11-23 Forward Structure
存量OI: C 15.9k / P 4.9k，今日变化ΔOI: C +2.8k / P +1.3k，平值价格ATM: C $0.79 / P $1.03 ｜ ATM IV 45.7%，净 delta 敞口 -63k shares
Top ΔOI: C 44 +1,104 ｜ P 41 +605
仓位参考: Max Pain 44 ｜ Call Wall 44（+8.0%，弱）（OI 1.3k） ｜ Put Wall 41.5（+1.9%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 45.7%｜历史 Rank 91%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 62,630 股

📆 11-25 Forward Structure
存量OI: C 5.0k / P 3.3k，今日变化ΔOI: C +2.5k / P +1.9k，平值价格ATM: C $1.30 / P $1.00 ｜ ATM IV 49.2%，净 delta 敞口 -58k shares
Top ΔOI: C 43 +606 ｜ C 44 +531 ｜ P 42 +436
仓位参考: Max Pain 44 ｜ Call Wall 43.5（+6.8%，弱）（OI 0.8k） ｜ Put Wall 42（+3.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 49.2%｜历史 Rank 91%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 58,259 股

📆 11-27 Forward Structure
存量OI: C 69.1k / P 30.6k，今日变化ΔOI: C +4.5k / P +1.2k，平值价格ATM: C $1.20 / P $1.28 ｜ ATM IV 46.6%，净 delta 敞口 -39k shares
Top ΔOI: C 44 +953
仓位参考: Max Pain 45 ｜ Call Wall 44（+8.0%，弱）（OI 2.8k） ｜ Put Wall 40（-1.8%）（OI 8.9k）
量化解读： 存量 Call 重｜ATM IV 46.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 39,234 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 56.4% vs 11-23 45.7%（差 +10.6pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/SLV_morning.json