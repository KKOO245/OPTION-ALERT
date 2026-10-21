# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.40
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 147C ΔOI -2,605（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 142.72 → 今开 146.20（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 147.45 ｜ 低 143.93

Options: P/C成交量 0.68 | OI比 0.78 | ATM IV 78.9% | Skew -0.1pp | Term 0.88 | ExpMove ±5.0%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±5.0% ｜ 10-30（9D）±9.5% ｜ 11-06（16D）±12.1% ｜ 11-13（23D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 66,827,629 | GEX Change vs 上次快照 6,238,670 | Flip: Primary Flip: 134.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 616 / LOW 97 / INVALID 191
结构观察区: Primary Flip 134.48（全链重定价，覆盖 98%）
Call Wall 135（弱结构｜现价高于该位 7.4%）
最近结构参考: Call Wall 135（现价高于该位 7.4%）
量化视角： 正 Gamma（6683万，无历史分位）｜正 Gamma 增强（+624万）｜现价位于 Flip 上方 7.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 155.0C — Vol 8,583 | 最新价 $0.61 | OI 26372→29241 (ΔOI +2869张) | ΔOI/Volume 33.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2869张（+10.9% vs前日OI），连续性待观察（方向未知）
10-30 120.0P — Vol 3,213 | 最新价 $0.89 | OI 6663→8580 (ΔOI +1917张) | ΔOI/Volume 59.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1917张（+28.8% vs前日OI），连续性待观察（方向未知）
10-23 105.0P — Vol 2,415 | 最新价 $0.06 | OI 2676→4293 (ΔOI +1617张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1617张（+60.4% vs前日OI），连续性待观察（方向未知）
10-23 135.0P — Vol 10,400 | 最新价 $1.14 | OI 2031→3376 (ΔOI +1345张) | ΔOI/Volume 12.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1345张（+66.2% vs前日OI），连续性待观察（方向未知）
10-23 150.0C — Vol 13,229 | 最新价 $1.39 | OI 13708→14996 (ΔOI +1288张) | ΔOI/Volume 9.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1288张（+9.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,036 张（Put 4,879 / Call 4,157），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C -1.5k / P +4.6k ｜ Activity HIGH ｜ 2D
10-30  C +3.4k / P +9.1k ｜ Activity MEDIUM △ ｜ 9D
11-06  C +0.9k / P +3.9k ｜ Activity MEDIUM △ ｜ 16D
11-13  C +1.0k / P +4.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 228.8k / P 179.0k，今日变化ΔOI: C -1.5k / P +4.6k，平值价格ATM: C $3.70 / P $3.50 ｜ ATM IV 78.9%，净 delta 敞口 -262k shares
Top ΔOI: C 157 -2,946 ｜ C 155 +2,869 ｜ C 147 -2,605
仓位参考: Max Pain 141 ｜ Call Wall 155（+6.9%，弱）（OI 29.2k） ｜ Put Wall 140（-3.5%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.9%｜历史 Rank 48%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 262,375 股

10-30（MEDIUM △）Top ΔOI: 120P +1,917 ｜ 150C +936
10-30（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 155（+6.9%，弱）（OI 2.5k） ｜ Put Wall 155（+6.9%，弱）（OI 3.9k）

11-06（MEDIUM △）Top ΔOI: 110P +650
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 155（+6.9%，弱）（OI 0.8k） ｜ Put Wall 155（+6.9%，弱）（OI 3.3k）

11-13（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 144（-0.7%，弱）（OI 0.8k） ｜ Put Wall 155（+6.9%，弱）（OI 1.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/MSTR_morning.json