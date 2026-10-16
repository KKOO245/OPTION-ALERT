# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.01 ｜ QQQ $716.55
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 230C ΔOI +1,344（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 240P ΔOI -1,265 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 236.30 → 今开 231.28（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 233.59 ｜ 低 226.30

Options: P/C成交量 0.51 | OI比 0.79 | ATM IV 129.8% | Skew -3.9pp | Term 0.68 | ExpMove ±12.3%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±12.3% ｜ 10-30（14D）±14.9% ｜ 11-06（21D）±17.6% ｜ 11-13（28D）±18.9%
   ⇒ IV–VIX Spread: +113.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,932,134 | GEX Change vs 上次快照 11,304,090 | Flip: Primary Flip: 235.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 587 / LOW 99 / INVALID 208
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 235.78（全链重定价，覆盖 93%）
Put Wall 240（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 236（现价低于该位 3.0%）
量化视角： 负 Gamma（593万，无历史分位）｜负 Gamma 缓解（+1130万）｜现价位于 Flip 下方 2.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（Put Wall，弱结构） / 245（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 236（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 240.0C — Vol 13,471 | 最新价 $3.45 | OI 1571→3823 (ΔOI +2252张) | ΔOI/Volume 16.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2252张（+143.3% vs前日OI），连续性待观察（方向未知）
10-16 245.0C — Vol 10,274 | 最新价 $1.90 | OI 875→2788 (ΔOI +1913张) | ΔOI/Volume 18.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1913张（+218.6% vs前日OI），连续性待观察（方向未知）
10-23 255.0C — Vol 1,844 | 最新价 $8.25 | OI 335→1802 (ΔOI +1467张) | ΔOI/Volume 79.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1467张（+437.9% vs前日OI），连续性待观察（方向未知）
11-20 300.0C — Vol 2,418 | 最新价 $7.80 | OI 2720→4155 (ΔOI +1435张) | ΔOI/Volume 59.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1435张（+52.8% vs前日OI），连续性待观察（方向未知）
10-23 230.0C — Vol 1,777 | 最新价 $18.28 | OI 59→1403 (ΔOI +1344张) | ΔOI/Volume 75.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1344张（+2278.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,411 张（Put 0 / Call 8,411），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 112.3k / P 89.1k，今日成交量: C 9.5k / P 4.9k，平值价格ATM: C $2.84 / P $3.58 ｜ ATM IV 129.8%，预期波动 ±2.8%，Max Pain 245
Top ΔOI: P 275 -3,579 ｜ C 240 +2,252 ｜ P 270 -2,060

📆 Forward Expiration Structure

10-23  C +5.7k / P +2.8k ｜ Activity HIGH ｜ 7D
10-30  C +1.9k / P +2.8k ｜ Activity MEDIUM △ ｜ 14D
11-06  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 21D
11-13  C +0.3k / P -0.6k ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 33.1k / P 30.1k，今日变化ΔOI: C +5.7k / P +2.8k，平值价格ATM: C $14.05 / P $14.05 ｜ ATM IV 106.7%，净 delta 敞口 98k shares
Top ΔOI: C 255 +1,467 ｜ C 230 +1,344 ｜ C 245 +883
仓位参考: Max Pain 255 ｜ Call Wall 230（+0.5%，弱）（OI 1.4k） ｜ Put Wall 230（+0.5%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 106.7%｜历史 Rank 83%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 97,696 股

10-30（MEDIUM △）Top ΔOI: 230C +491
10-30（MEDIUM △）仓位参考: Max Pain 260 ｜ Call Wall 240（+4.9%，弱）（OI 1.3k） ｜ Put Wall 230（+0.5%）（OI 3.5k）

11-06（MEDIUM △）Top ΔOI: 240P -291 ｜ 235P +278
11-06（MEDIUM △）仓位参考: Max Pain 260 ｜ Call Wall 240（+4.9%，弱）（OI 0.3k） ｜ Put Wall 235（+2.7%）（OI 2.7k）

11-13（MEDIUM △）Top ΔOI: 240P -1,265 ｜ 230P +278
11-13（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 240（+4.9%，弱）（OI 0.3k） ｜ Put Wall 230（+0.5%）（OI 2.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/BE_morning.json