# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 56.57 → 收盘 54.53（-3.6%） ｜ 今日高 58.52 ｜ 低 54.19 ｜ 昨收 53.78 → 收盘 54.53（+1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-11，窗口结束前不做对错判定）

Options: P/C成交量 0.29 | OI比 0.74 | ATM IV 93.5% | Skew 4.2pp | Term 0.69 | ExpMove ±6.6%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 4.2pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±6.6% ｜ 09-18（14D）±9.7% ｜ 09-25（21D）±12.5% ｜ 10-02（28D）±14.4%
   ⇒ IV–VIX Spread: +79.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 595,425 | GEX Change vs 上次快照 624,354 | Flip: Primary Flip: 54.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 273 / LOW 69 / INVALID 152
结构观察区: Primary Flip 54.08（全链重定价，覆盖 90%）
Put Wall 55（弱结构｜现价低于该位 0.9%）
最近结构参考: Flip 54（现价高于该位 0.8%）
量化视角： 正 Gamma（60万，无历史分位）｜由负转正（+62万）｜现价位于 Flip 上方 0.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 54（MaxPain，仅结算参考）；上方 55（Put Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 65.0C — Vol 1,391 | 最新价 $0.10 | OI 452→1483 (ΔOI +1031张) | ΔOI/Volume 74.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1031张（+228.1% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 271 | 最新价 $2.38 | OI 3214→3455 (ΔOI +241张) | ΔOI/Volume 88.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增241张（+7.5% vs前日OI），连续性待观察（方向未知）
09-04 55.0C — Vol 2,002 | 最新价 $0.02 | OI 1038→1276 (ΔOI +238张) | ΔOI/Volume 11.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增238张（+22.9% vs前日OI），连续性待观察（方向未知）
09-18 60.0C — Vol 491 | 最新价 $0.93 | OI 6140→6366 (ΔOI +226张) | ΔOI/Volume 46.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增226张（+3.7% vs前日OI），值得跟踪（方向未知）
09-04 54.0C — Vol 404 | 最新价 $0.48 | OI 290→497 (ΔOI +207张) | ΔOI/Volume 51.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增207张（+71.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,943 张（Put 0 / Call 1,943），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 6.2k / P 4.5k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 1.55 / P 2.03
隐含波动率 ATM IV:  58.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 54（结算参考）
量化解读： 存量 Call 重｜ATM IV 58.6%｜历史 Rank 88%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 55（结算参考） ｜ Put Wall 55（+0.9%，弱）（OI 9.2k）

09-25（Activity LOW）仓位参考: Max Pain 52（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 60（结算参考） ｜ Put Wall 50（-8.3%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/MP_evening.json