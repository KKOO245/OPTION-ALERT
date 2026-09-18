# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 72.3% vs 09-25 61.5%（差 +10.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 160P ΔOI -3,486（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 164.51 → 今开 169.87（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 171.38 ｜ 低 165.73

Options: P/C成交量 0.51 | OI比 0.53 | ATM IV 72.3% | Skew -3.3pp | Term 0.86 | ExpMove ±3.3%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.3% ｜ 09-25（8D）±7.5% ｜ 10-02（15D）±9.9% ｜ 10-09（22D）±12.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,855,379 | GEX Change vs 上次快照 18,418,042 | Flip: Primary Flip: 167.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 480 / LOW 174 / INVALID 320
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 167.54（全链重定价，覆盖 96%）
Put Wall 160（弱结构｜现价高于该位 5.2%）
最近结构参考: Flip 168（现价高于该位 0.5%）
量化视角： 正 Gamma（286万，无历史分位）｜由负转正（+1842万）｜现价位于 Flip 上方 0.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（Put Wall，弱结构）；上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 185.0C — Vol 1,634 | 最新价 $1.30 | OI 1380→2372 (ΔOI +992张) | ΔOI/Volume 60.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增992张（+71.9% vs前日OI），连续性待观察（方向未知）
09-18 172.5C — Vol 2,285 | 最新价 $1.12 | OI 467→1095 (ΔOI +628张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增628张（+134.5% vs前日OI），连续性待观察（方向未知）
09-18 170.0C — Vol 5,699 | 最新价 $1.66 | OI 8488→9079 (ΔOI +591张) | ΔOI/Volume 10.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+7.0% vs前日OI），连续性待观察（方向未知）
09-18 165.0C — Vol 2,747 | 最新价 $3.45 | OI 1431→2022 (ΔOI +591张) | ΔOI/Volume 21.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+41.3% vs前日OI），连续性待观察（方向未知）
09-18 165.0P — Vol 9,898 | 最新价 $3.75 | OI 4715→5303 (ΔOI +588张) | ΔOI/Volume 5.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增588张（+12.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,390 张（Put 588 / Call 2,802），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +1.4k / P -7.3k ｜ Activity HIGH ｜ 1D
09-25  C +3.5k / P +2.7k ｜ Activity HIGH ｜ 8D
10-02  C +0.8k / P +0.4k ｜ Activity HIGH ｜ 15D
10-09  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 22D

📆 09-18 Forward Structure
存量OI: C 227.6k / P 120.4k，今日变化ΔOI: C +1.4k / P -7.3k，平值价格ATM: C $2.80 / P $2.70 ｜ ATM IV 72.3%，净 delta 敞口 673k shares
Top ΔOI: P 160 -3,486 ｜ P 220 -1,693 ｜ P 210 -1,546
仓位参考: Max Pain 175 ｜ Call Wall 182.5（+8.4%，弱）（OI 10.4k） ｜ Put Wall 160（-4.9%，弱）（OI 13.7k）
量化解读： 存量 Call 重｜ATM IV 72.3%｜历史 Rank 37%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 673,011 股

📆 09-25 Forward Structure
存量OI: C 23.3k / P 18.4k，今日变化ΔOI: C +3.5k / P +2.7k，平值价格ATM: C $6.53 / P $6.04 ｜ ATM IV 61.5%，净 delta 敞口 29k shares
Top ΔOI: C 185 +992 ｜ P 165 +421 ｜ P 157 +382
仓位参考: Max Pain 170 ｜ Call Wall 185（+9.9%，弱）（OI 2.4k） ｜ Put Wall 155（-7.9%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 61.5%｜历史 Rank 37%（近端代理）｜净 delta 敞口 正 29,392 股

📆 10-02 Forward Structure
存量OI: C 12.3k / P 17.1k，今日变化ΔOI: C +0.8k / P +0.4k，平值价格ATM: C $8.80 / P $7.85 ｜ ATM IV 62.5%，净 delta 敞口 25k shares
Top ΔOI: C 180 +188
仓位参考: Max Pain 185 ｜ Call Wall 180（+7.0%，弱）（OI 0.8k） ｜ Put Wall 172.5（+2.5%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.5%｜历史 Rank 37%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,100 股

📆 10-09 Forward Structure
存量OI: C 2.8k / P 4.1k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $10.50 / P $9.80 ｜ ATM IV 62.2%，净 delta 敞口 -23k shares
Top ΔOI: P 187 +391 ｜ P 160 +49
仓位参考: Max Pain 188 ｜ Call Wall 185（+9.9%，弱）（OI 0.2k） ｜ Put Wall 160（-4.9%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 62.2%｜历史 Rank 37%（近端代理）｜净 delta 敞口 负 23,061 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 72.3% vs 09-25 61.5%（差 +10.8pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/COIN_morning.json