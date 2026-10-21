# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.43
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
🟡 **近现价集中开仓**: 10-23 175C ΔOI +738（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 170.85 → 今开 175.00（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 176.98 ｜ 低 172.04

Options: P/C成交量 0.40 | OI比 0.62 | ATM IV 72.7% | Skew 0.5pp | Term 0.95 | ExpMove ±4.6%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 0.5pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±4.6% ｜ 10-30（9D）±11.1% ｜ 11-06（16D）±12.0% ｜ 11-13（23D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,026,457 | GEX Change vs 上次快照 6,610,061 | Flip: Primary Flip: 165.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 456 / LOW 131 / INVALID 255
结构观察区: Primary Flip 165.30（全链重定价，覆盖 99%）
Call Wall 170（弱结构｜现价高于该位 1.7%）
最近结构参考: Call Wall 170（现价高于该位 1.7%）
量化视角： 正 Gamma（1403万，无历史分位）｜正 Gamma 增强（+661万）｜现价位于 Flip 上方 4.58%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Call Wall，弱结构）；上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 190.0C — Vol 5,782 | 最新价 $0.31 | OI 4062→7341 (ΔOI +3279张) | ΔOI/Volume 56.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3279张（+80.7% vs前日OI），连续性待观察（方向未知）
10-23 175.0C — Vol 3,508 | 最新价 $2.50 | OI 1546→2284 (ΔOI +738张) | ΔOI/Volume 21.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增738张（+47.7% vs前日OI），连续性待观察（方向未知）
10-23 180.0C — Vol 5,004 | 最新价 $1.25 | OI 7074→7787 (ΔOI +713张) | ΔOI/Volume 14.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增713张（+10.1% vs前日OI），连续性待观察（方向未知）
10-23 185.0C — Vol 2,846 | 最新价 $0.59 | OI 3459→4136 (ΔOI +677张) | ΔOI/Volume 23.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增677张（+19.6% vs前日OI），连续性待观察（方向未知）
10-23 172.5P — Vol 1,043 | 最新价 $5.10 | OI 1444→1976 (ΔOI +532张) | ΔOI/Volume 51.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增532张（+36.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,939 张（Put 532 / Call 5,407），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +6.4k / P +0.6k ｜ Activity HIGH ｜ 2D
10-30  C +0.5k / P +1.2k ｜ Activity HIGH ｜ 9D
11-06  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
11-13  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 66.9k / P 41.4k，今日变化ΔOI: C +6.4k / P +0.6k，平值价格ATM: C $4.30 / P $3.65 ｜ ATM IV 72.7%，净 delta 敞口 142k shares
Top ΔOI: C 190 +3,279 ｜ C 175 +738 ｜ C 180 +713
仓位参考: Max Pain 175 ｜ Call Wall 180（+4.1%，弱）（OI 7.8k）
量化解读： 存量 Call 重｜ATM IV 72.7%｜历史 Rank 40%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 142,326 股

📆 10-30 Forward Structure
存量OI: C 17.8k / P 18.6k，今日变化ΔOI: C +0.5k / P +1.2k，平值价格ATM: C $10.30 / P $8.80 ｜ ATM IV 81.5%，净 delta 敞口 -3k shares
Top ΔOI: P 167 +250 ｜ P 170 +131
仓位参考: Max Pain 180 ｜ Call Wall 185（+7.0%，弱）（OI 1.8k） ｜ Put Wall 170（-1.7%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 81.5%｜历史 Rank 40%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,171 股

11-06（MEDIUM △）Top ΔOI: 175P +96 ｜ 180C +93
11-06（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+1.2%，弱）（OI 0.3k）

11-13（MEDIUM △）Top ΔOI: 160P +311 ｜ 190C +126
11-13（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 177.5（+2.7%）（OI 1.1k） ｜ Put Wall 160（-7.4%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/COIN_morning.json