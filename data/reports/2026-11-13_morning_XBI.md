# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.49
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 145C ΔOI +1,000（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 151.20 → 今开 151.24（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 151.29 ｜ 低 148.26

Options: P/C成交量 1.94 | OI比 0.80 | ATM IV 88.5% | Skew 7.4pp | Term 0.37 | ExpMove ±3.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.37，近月 IV 高于远月）｜保护溢价显著（Skew 7.4pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.80）+ 当日成交偏 Put（P/C量 1.94）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.94×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±3.1% ｜ 11-27（14D）±2.7% ｜ 12-04（21D）±0.0% ｜ 12-11（28D）±2.7%
   ⇒ IV–VIX Spread: +68.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,708,582 | GEX Change vs 上次快照 -6,070,160 | Flip: Primary Flip: 152.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 433 / LOW 169 / INVALID 320
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.53（全链重定价，覆盖 93%）
最近结构参考: Flip 153（现价低于该位 2.6%）
量化视角： 负 Gamma（1671万，无历史分位）｜负 Gamma 加深（607万）｜现价位于 Flip 下方 2.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 157.0C — Vol 2,366 | 最新价 $0.05 | OI 153→2365 (ΔOI +2212张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2212张（+1445.8% vs前日OI），连续性待观察（方向未知）
11-13 156.0C — Vol 1,501 | 最新价 $0.08 | OI 241→1375 (ΔOI +1134张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1134张（+470.5% vs前日OI），连续性待观察（方向未知）
11-20 145.0C — Vol 1,000 | 最新价 $7.30 | OI 206→1206 (ΔOI +1000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1000张（+485.4% vs前日OI），连续性待观察（方向未知）
11-13 158.0C — Vol 1,730 | 最新价 $0.02 | OI 377→1069 (ΔOI +692张) | ΔOI/Volume 40.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增692张（+183.6% vs前日OI），连续性待观察（方向未知）
11-13 153.0C — Vol 1,096 | 最新价 $0.71 | OI 52→736 (ΔOI +684张) | ΔOI/Volume 62.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增684张（+1315.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,722 张（Put 0 / Call 5,722），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 11.5k / P 9.2k，今日成交量: C 1.4k / P 0.6k，平值价格ATM: C $1.98 / P $0.93 ｜ ATM IV 88.5%，预期波动 ±2.0%，Max Pain 150
Top ΔOI: C 157 +2,212 ｜ C 156 +1,134 ｜ C 158 +692

📆 Forward Expiration Structure

11-20  C +1.4k / P +0.8k ｜ Activity MEDIUM △ ｜ 7D
11-27  C +51 / P +1.0k ｜ Activity HIGH ｜ 14D
12-04  C +21 / P +15 ｜ Activity MEDIUM △ ｜ 21D
12-11  C +18 / P +8 ｜ Activity LOW ｜ 28D

📆 11-20 Forward Structure
存量OI: C 26.1k / P 57.3k，今日变化ΔOI: C +1.4k / P +0.8k，平值价格ATM: C $3.19 / P $1.36 ｜ ATM IV 33.5%，净 delta 敞口 66k shares
Top ΔOI: C 145 +1,000 ｜ P 145 +364 ｜ C 155 -300
仓位参考: Max Pain 153 ｜ Call Wall 155（+4.3%，弱）（OI 1.5k） ｜ Put Wall 140（-5.8%）（OI 9.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.5%｜历史 Rank 100%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 65,565 股

📆 11-27 Forward Structure
存量OI: C 1.2k / P 2.9k，今日变化ΔOI: C +51 / P +1.0k，平值价格ATM: C $0.00 / P $4.00 ｜ ATM IV 33.8%，净 delta 敞口 -26k shares
Top ΔOI: P 147 +303 ｜ P 137 +300 ｜ P 145 +202
仓位参考: Max Pain 158 ｜ Call Wall 152.5（+2.6%，弱）（OI 0.1k） ｜ Put Wall 147（-1.1%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 33.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 25,600 股

12-04（MEDIUM △）Top ΔOI: 152C +20 ｜ 141P +5
12-04（MEDIUM △）仓位参考: Max Pain 161 ｜ Call Wall 152.5（+2.6%，弱）（OI 21） ｜ Put Wall 145（-2.4%，弱）（OI 59）

12-11（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 154（+3.6%，弱）（OI 84） ｜ Put Wall 143（-3.8%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/XBI_morning.json