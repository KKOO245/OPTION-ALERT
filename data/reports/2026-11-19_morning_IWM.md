# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $735.18 ｜ QQQ $663.71
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 263P ΔOI +15,988（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 270.12 → 今开 271.08（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 271.80 ｜ 低 268.78

Options: P/C成交量 1.24 | OI比 1.86 | ATM IV 36.4% | Skew 3.8pp | Term 0.60 | ExpMove ±1.4%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜当日成交偏 Put（P/C量 1.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.86×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±1.4% ｜ 11-23（4D）±1.8% ｜ 11-24（5D）±2.2% ｜ 11-25（6D）±2.7%
   ⇒ IV–VIX Spread: +13.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,132,280,087 | GEX Change vs 上次快照 -119,088,753 | Flip: Primary Flip: 280.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1144 / LOW 250 / INVALID 1222
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 280.10（全链重定价，覆盖 96%）
Put Wall 265（弱结构｜现价高于该位 1.6%）
最近结构参考: Put Wall 265（现价高于该位 1.6%）
量化视角： 负 Gamma（21.32亿，无历史分位）｜负 Gamma 加深（1.19亿）｜现价位于 Flip 下方 3.83%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 265（Put Wall，弱结构）；上方 272（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 280（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 257.0P — Vol 30,424 | 最新价 $3.09 | OI 16909→44761 (ΔOI +27852张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27852张（+164.7% vs前日OI），连续性待观察（方向未知）
11-20 263.0P — Vol 26,072 | 最新价 $0.44 | OI 89241→105229 (ΔOI +15988张) | ΔOI/Volume 61.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15988张（+17.9% vs前日OI），连续性待观察（方向未知）
12-18 258.0P — Vol 36,388 | 最新价 $3.30 | OI 8353→21727 (ΔOI +13374张) | ΔOI/Volume 36.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13374张（+160.1% vs前日OI），连续性待观察（方向未知）
11-20 277.0C — Vol 16,555 | 最新价 $0.19 | OI 5980→16726 (ΔOI +10746张) | ΔOI/Volume 64.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10746张（+179.7% vs前日OI），连续性待观察（方向未知）
12-04 252.0P — Vol 9,185 | 最新价 $1.03 | OI 266→9045 (ΔOI +8779张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8779张（+3300.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 76,739 张（Put 65,993 / Call 10,746），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $14M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 30.9k / P 57.4k，今日成交量: C 86.6k / P 107.0k，平值价格ATM: C $1.61 / P $0.65 ｜ ATM IV 36.4%，预期波动 ±0.8%，Max Pain 272
Top ΔOI: P 267 +5,650 ｜ P 257 +3,122 ｜ C 273 +2,056

📆 Forward Expiration Structure

11-20  C +20.3k / P -33.6k ｜ Activity HIGH ｜ 1D
11-23  C +7.0k / P +2.2k ｜ Activity HIGH ｜ 4D
11-24  C +2.5k / P +2.4k ｜ Activity HIGH ｜ 5D
11-25  C +3.6k / P +9.2k ｜ Activity HIGH ｜ 6D

📆 11-20 Forward Structure
存量OI: C 605.8k / P 1402.9k，今日变化ΔOI: C +20.3k / P -33.6k，平值价格ATM: C $2.25 / P $1.42 ｜ ATM IV 28.8%，净 delta 敞口 2.2M shares
Top ΔOI: P 263 +15,988 ｜ C 277 +10,746 ｜ P 270 -10,029
仓位参考: Max Pain 276 ｜ Call Wall 285（+5.8%，弱）（OI 50.6k） ｜ Put Wall 265（-1.6%，弱）（OI 127.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.8%｜历史 Rank 80%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,160,130 股

📆 11-23 Forward Structure
存量OI: C 23.5k / P 28.1k，今日变化ΔOI: C +7.0k / P +2.2k，平值价格ATM: C $2.65 / P $2.20 ｜ ATM IV 21.2%，净 delta 敞口 128k shares
Top ΔOI: C 281 +2,550 ｜ C 270 +2,095 ｜ P 265 +1,212
仓位参考: Max Pain 271 ｜ Call Wall 281（+4.3%，弱）（OI 3.5k） ｜ Put Wall 270（+0.2%）（OI 12.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.2%｜历史 Rank 80%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 127,679 股

📆 11-24 Forward Structure
存量OI: C 8.9k / P 14.0k，今日变化ΔOI: C +2.5k / P +2.4k，平值价格ATM: C $3.35 / P $2.72 ｜ ATM IV 22.2%，净 delta 敞口 30k shares
Top ΔOI: P 255 +1,258 ｜ P 265 +718 ｜ C 274 +582
仓位参考: Max Pain 274 ｜ Call Wall 275（+2.1%，弱）（OI 1.3k） ｜ Put Wall 270（+0.2%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.2%｜历史 Rank 80%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 29,508 股

📆 11-25 Forward Structure
存量OI: C 12.4k / P 15.1k，今日变化ΔOI: C +3.6k / P +9.2k，平值价格ATM: C $4.27 / P $2.91 ｜ ATM IV 22.9%，净 delta 敞口 -109k shares
Top ΔOI: P 255 +2,162 ｜ P 265 +1,920 ｜ C 272 +1,080
仓位参考: Max Pain 272 ｜ Call Wall 277（+2.8%，弱）（OI 4.2k） ｜ Put Wall 255（-5.3%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 22.9%｜历史 Rank 80%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 108,777 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/IWM_morning.json