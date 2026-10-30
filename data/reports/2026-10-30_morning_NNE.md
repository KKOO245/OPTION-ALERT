# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $759.94 ｜ QQQ $692.81
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 11P ΔOI -76（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.21 → 今开 11.49（-5.9%） | 较昨收变动（含盘初走势） ｜ 今日高 11.65 ｜ 低 11.36

Options: P/C成交量 0.14 | OI比 0.14 | ATM IV 133.8% | Skew -2.9pp | Term 0.56 | ExpMove ±9.5%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.14）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.14×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±9.5% ｜ 11-13（14D）±13.4% ｜ 11-20（21D）±4.1% ｜ 11-27（28D）±5.6%
   ⇒ IV–VIX Spread: +115.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,326 | GEX Change vs 上次快照 -645,688 | Flip: Primary Flip: 11.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 123 / LOW 91 / INVALID 194
结构观察区: Primary Flip 11.54（全链重定价，覆盖 90%）
Put Wall 12（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 12（现价高于该位 0.2%）
量化视角： 正 Gamma（1万，无历史分位）｜正 Gamma 减弱（65万）｜现价位于 Flip 上方 0.16%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（Put Wall，弱结构） / 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 13.0C — Vol 194 | 最新价 $0.35 | OI 115→268 (ΔOI +153张) | ΔOI/Volume 78.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增153张（+133.0% vs前日OI），连续性待观察（方向未知）
11-06 14.0C — Vol 137 | 最新价 $0.14 | OI 99→236 (ΔOI +137张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增137张（+138.4% vs前日OI），连续性待观察（方向未知）
11-06 13.5C — Vol 87 | 最新价 $0.15 | OI 79→151 (ΔOI +72张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增72张（+91.1% vs前日OI），连续性待观察（方向未知）
11-06 12.5C — Vol 21 | 最新价 $0.64 | OI 25→43 (ΔOI +18张) | ΔOI/Volume 85.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18张（+72.0% vs前日OI），连续性待观察（方向未知）
11-20 15.0C — Vol 26 | 最新价 $0.23 | OI 412→430 (ΔOI +18张) | ΔOI/Volume 69.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增18张（+4.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 398 张（Put 0 / Call 398），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 8.4k / P 1.2k，今日成交量: C 0.4k / P 55，平值价格ATM: C $0.90 / P $0.03 ｜ ATM IV 133.8%，预期波动 ±8.0%，Max Pain 13
Top ΔOI: P 14 -103 ｜ P 15 -28 ｜ C 13 -27

📆 Forward Expiration Structure

11-06  C +0.4k / P -69 ｜ Activity HIGH ｜ 7D
11-13  C +26 / P -3 ｜ Activity MEDIUM △ ｜ 14D
11-20  C +29 / P -2 ｜ Activity MEDIUM △ ｜ 21D
11-27  C +12 / P +0 ｜ Activity MEDIUM △ ｜ 28D

📆 11-06 Forward Structure
存量OI: C 2.3k / P 1.4k，今日变化ΔOI: C +0.4k / P -69，平值价格ATM: C $0.95 / P $0.15 ｜ ATM IV 87.8%，净 delta 敞口 11k shares
Top ΔOI: P 11 -76
仓位参考: Max Pain 14 ｜ Put Wall 11.5（-0.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 87.8%｜历史 Rank 80%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,065 股

11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 12.5（+8.2%，弱）（OI 67）

11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 12（+3.9%，弱）（OI 0.3k）

11-27（MEDIUM △）Top ΔOI: 12C +1
11-27（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 12.5（+8.2%）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/NNE_morning.json