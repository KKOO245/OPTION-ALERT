# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $764.28 ｜ QQQ $704.47
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 150P ΔOI +3,993（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 153.48 → 今开 145.08（-5.5%） | 较昨收变动（含盘初走势） ｜ 今日高 148.75 ｜ 低 144.08

Options: P/C成交量 1.20 | OI比 0.83 | ATM IV 83.8% | Skew -1.4pp | Term 0.83 | ExpMove ±3.9%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.83）+ 当日成交偏 Put（P/C量 1.20）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.20×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.9% ｜ 10-30（8D）±9.0% ｜ 11-06（15D）±12.2% ｜ 11-13（22D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 79,279,253 | GEX Change vs 上次快照 -12,796,143 | Flip: Primary Flip: 137.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 592 / LOW 77 / INVALID 235
结构观察区: Primary Flip 137.02（全链重定价，覆盖 99%）
Call Wall 135（弱结构｜现价高于该位 9.8%）
最近结构参考: Flip 137（现价高于该位 8.2%）
量化视角： 正 Gamma（7928万，无历史分位）｜正 Gamma 减弱（1280万）｜现价位于 Flip 上方 8.22%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 120.0P — Vol 7,450 | 最新价 $0.05 | OI 7653→13940 (ΔOI +6287张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6287张（+82.2% vs前日OI），连续性待观察（方向未知）
10-23 150.0P — Vol 21,130 | 最新价 $2.00 | OI 3503→7496 (ΔOI +3993张) | ΔOI/Volume 18.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3993张（+114.0% vs前日OI），连续性待观察（方向未知）
10-30 90.0P — Vol 3,992 | 最新价 $0.09 | OI 1617→3883 (ΔOI +2266张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2266张（+140.1% vs前日OI），连续性待观察（方向未知）
10-23 170.0C — Vol 12,051 | 最新价 $0.24 | OI 3554→5396 (ΔOI +1842张) | ΔOI/Volume 15.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1842张（+51.8% vs前日OI），连续性待观察（方向未知）
10-23 149.0P — Vol 4,675 | 最新价 $1.58 | OI 1403→3219 (ΔOI +1816张) | ΔOI/Volume 38.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1816张（+129.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,204 张（Put 14,362 / Call 1,842），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +4.9k / P +15.5k ｜ Activity HIGH ｜ 1D
10-30  C +4.7k / P +8.9k ｜ Activity HIGH ｜ 8D
11-06  C +2.1k / P +4.6k ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.9k / P +3.9k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 233.8k / P 194.5k，今日变化ΔOI: C +4.9k / P +15.5k，平值价格ATM: C $2.99 / P $2.85 ｜ ATM IV 83.8%，净 delta 敞口 -750k shares
Top ΔOI: P 150 +3,993 ｜ C 148 -2,675
仓位参考: Max Pain 142 ｜ Call Wall 155（+4.5%，弱）（OI 29.0k） ｜ Put Wall 150（+1.2%，弱）（OI 7.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 83.8%｜历史 Rank 57%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 750,500 股

📆 10-30 Forward Structure
存量OI: C 55.2k / P 96.0k，今日变化ΔOI: C +4.7k / P +8.9k，平值价格ATM: C $6.75 / P $6.57 ｜ ATM IV 74.3%，净 delta 敞口 -30k shares
Top ΔOI: P 125 +1,347 ｜ C 170 +867
仓位参考: Max Pain 152 ｜ Call Wall 160（+7.9%，弱）（OI 3.9k） ｜ Put Wall 155（+4.5%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 74.3%｜历史 Rank 57%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 29,932 股

11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+7.9%）（OI 2.0k） ｜ Put Wall 160（+7.9%，弱）（OI 3.6k）

11-13（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 144（-2.9%，弱）（OI 0.8k） ｜ Put Wall 160（+7.9%，弱）（OI 2.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/MSTR_morning.json