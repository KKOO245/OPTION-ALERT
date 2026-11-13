# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.80 ｜ QQQ $679.89
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 154.99 → 今开 153.26（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 154.37 ｜ 低 145.82

Options: P/C成交量 3.38 | OI比 2.14 | ATM IV 167.8% | Skew 19.9pp | Term 0.32 | ExpMove ±7.5%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.32，近月 IV 高于远月）｜保护溢价显著（Skew 19.9pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 3.38）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.14×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±7.5% ｜ 11-27（14D）±10.7% ｜ 12-04（21D）±11.4% ｜ 12-11（28D）±4.4%
   ⇒ IV–VIX Spread: +148.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -30,642,469 | GEX Change vs 上次快照 -29,359,642 | Flip: Primary Flip: 152.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 535 / LOW 457 / INVALID 812
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.27（全链重定价，覆盖 89%）
Call Wall 155（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 152（现价低于该位 3.0%）
量化视角： 负 Gamma（3064万，无历史分位）｜负 Gamma 加深（2936万）｜现价位于 Flip 下方 2.98%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考） / 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 152（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 140.0P — Vol 8,764 | 最新价 $4.16 | OI 3177→7875 (ΔOI +4698张) | ΔOI/Volume 53.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4698张（+147.9% vs前日OI），连续性待观察（方向未知）
11-20 143.33P — Vol 221 | 最新价 $1.75 | OI 13066→16165 (ΔOI +3099张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3099张（+23.7% vs前日OI），连续性待观察（方向未知）
11-13 150.0P — Vol 4,906 | 最新价 $0.66 | OI 2783→5783 (ΔOI +3000张) | ΔOI/Volume 61.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3000张（+107.8% vs前日OI），连续性待观察（方向未知）
11-20 130.0P — Vol 398 | 最新价 $0.41 | OI 8943→11747 (ΔOI +2804张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2804张（+31.4% vs前日OI），连续性待观察（方向未知）
11-13 145.0P — Vol 2,941 | 最新价 $0.20 | OI 1125→3320 (ΔOI +2195张) | ΔOI/Volume 74.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2195张（+195.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,796 张（Put 15,796 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 117.5k / P 252.0k，今日成交量: C 0.6k / P 2.1k，平值价格ATM: C $4.00 / P $1.38 ｜ ATM IV 167.8%，预期波动 ±3.6%，Max Pain 153
Top ΔOI: P 150 +3,000 ｜ P 145 +2,195 ｜ P 148 +1,703

📆 Forward Expiration Structure

11-20  C -8.0k / P -3.7k ｜ Activity MEDIUM △ ｜ 7D
11-27  C +2.1k / P +0.6k ｜ Activity MEDIUM △ ｜ 14D
12-04  C +0.9k / P +0.7k ｜ Activity MEDIUM △ ｜ 21D
12-11  C +76 / P -98 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 199.2k / P 248.1k，今日变化ΔOI: C -8.0k / P -3.7k，平值价格ATM: C $5.60 / P $5.40 ｜ ATM IV 65.5%，净 delta 敞口 35k shares
Top ΔOI: C 166 -8,887 ｜ P 140 -3,641 ｜ P 125 -3,482
仓位参考: Max Pain 158 ｜ Call Wall 155（+4.9%，弱）（OI 17.9k） ｜ Put Wall 153.33（+3.8%，弱）（OI 17.3k）
量化解读： 存量 Put 重｜ATM IV 65.5%｜历史 Rank 100%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,569 股

11-27（MEDIUM △）Top ΔOI: 167C +1,004 ｜ 175C +934
11-27（MEDIUM △）仓位参考: Max Pain 162 ｜ Put Wall 150（+1.5%，弱）（OI 3.6k）

12-04（MEDIUM △）Top ΔOI: 175C +503 ｜ 135P +464
12-04（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 153.33（+3.8%，弱）（OI 0.4k） ｜ Put Wall 150（+1.5%，弱）（OI 1.3k）

12-11（MEDIUM △）Top ΔOI: 147C -367 ｜ 170C +305
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 155（+4.9%，弱）（OI 0.2k） ｜ Put Wall 140（-5.2%）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 65.5% vs 11-27 58.7%（差 +6.8pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SOXX_morning.json