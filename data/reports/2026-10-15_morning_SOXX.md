# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $767.19 ｜ QQQ $720.62
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 60.2% vs 10-23 46.9%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 505P ΔOI +1,017（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 450P ΔOI +6,514 占该期限总 OI 11.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 519.42 → 今开 500.41（-3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 507.19 ｜ 低 495.79

Options: P/C成交量 2.77 | OI比 2.32 | ATM IV 60.2% | Skew 9.4pp | Term 0.70 | ExpMove ±2.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 9.4pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.77×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.9% ｜ 10-23（8D）±5.2% ｜ 10-30（15D）±7.0% ｜ 11-06（22D）±14.2%
   ⇒ IV–VIX Spread: +42.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -60,001,467 | GEX Change vs 上次快照 -18,689,852 | Flip: Primary Flip: 561.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 611 / LOW 350 / INVALID 691
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 561.44（全链重定价，覆盖 93%）
Put Wall 500（弱结构｜现价低于该位 0.1%）
最近结构参考: Put Wall 500（现价低于该位 0.1%）
量化视角： 负 Gamma（6000万，无历史分位）｜负 Gamma 加深（1869万）｜现价位于 Flip 下方 11.01%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 500（Put Wall，弱结构） / 538（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 561（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 450.0P — Vol 6,564 | 最新价 $2.10 | OI 64→6578 (ΔOI +6514张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6514张（+10178.1% vs前日OI），连续性待观察（方向未知）
10-30 500.0P — Vol 8,045 | 最新价 $10.20 | OI 10749→17087 (ΔOI +6338张) | ΔOI/Volume 78.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6338张（+59.0% vs前日OI），连续性待观察（方向未知）
10-16 505.0P — Vol 621 | 最新价 $2.70 | OI 2377→3394 (ΔOI +1017张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1017张（+42.8% vs前日OI），连续性待观察（方向未知）
10-16 495.0P — Vol 1,066 | 最新价 $1.50 | OI 791→1738 (ΔOI +947张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增947张（+119.7% vs前日OI），连续性待观察（方向未知）
10-16 600.0C — Vol 3,267 | 最新价 $0.05 | OI 8111→8963 (ΔOI +852张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增852张（+10.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,668 张（Put 14,816 / Call 852），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.6k / P +1.7k ｜ Activity HIGH ｜ 1D
10-23  C +0.6k / P +1.1k ｜ Activity MEDIUM △ ｜ 8D
10-30  C +1.1k / P +13.9k ｜ Activity HIGH ｜ 15D
11-06  C +0.2k / P +88 ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 46.0k / P 106.7k，今日变化ΔOI: C +0.6k / P +1.7k，平值价格ATM: C $5.80 / P $8.70 ｜ ATM IV 60.2%，净 delta 敞口 -58k shares
Top ΔOI: P 505 +1,017 ｜ P 495 +947 ｜ P 530 -864
仓位参考: Max Pain 538 ｜ Call Wall 510（+2.1%，弱）（OI 2.1k） ｜ Put Wall 480（-3.9%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜ATM IV 60.2%｜历史 Rank 93%（近端代理）｜IV/RV 2.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 57,572 股

10-23（MEDIUM △）Top ΔOI: 490P +480 ｜ 525C +140
10-23（MEDIUM △）仓位参考: Max Pain 555 ｜ Call Wall 525（+5.1%，弱）（OI 0.3k） ｜ Put Wall 510（+2.1%，弱）（OI 3.0k）

📆 10-30 Forward Structure
存量OI: C 7.6k / P 48.5k，今日变化ΔOI: C +1.1k / P +13.9k，平值价格ATM: C $17.60 / P $17.60 ｜ ATM IV 43.0%，净 delta 敞口 -425k shares
Top ΔOI: P 450 +6,514 ｜ P 500 +6,338 ｜ P 490 +664
仓位参考: Max Pain 560 ｜ Put Wall 500（+0.1%）（OI 17.1k）
量化解读： 存量 Put 重｜ATM IV 43.0%｜历史 Rank 93%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 424,947 股

11-06（MEDIUM △）Top ΔOI: 550C +184 ｜ 570P -87
11-06（MEDIUM △）仓位参考: Max Pain 568 ｜ Put Wall 500（+0.1%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 60.2% vs 10-23 46.9%（差 +13.4pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SOXX_morning.json