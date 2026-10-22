# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.79
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 175P ΔOI +578（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 177.08 → 今开 170.45（-3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 173.64 ｜ 低 168.55

Options: P/C成交量 0.33 | OI比 0.62 | ATM IV 74.0% | Skew -1.6pp | Term 0.91 | ExpMove ±3.4%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.4% ｜ 10-30（8D）±9.9% ｜ 11-06（15D）±12.0% ｜ 11-13（22D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,060,990 | GEX Change vs 上次快照 -9,860,461 | Flip: Primary Flip: 168.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 425 / LOW 147 / INVALID 274
结构观察区: Primary Flip 168.04（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价高于该位 1.8%）
最近结构参考: Call Wall 170（现价高于该位 1.8%）
量化视角： 正 Gamma（1306万，无历史分位）｜正 Gamma 减弱（986万）｜现价位于 Flip 上方 3.03%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Call Wall，弱结构）；上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 110.0P — Vol 712 | 最新价 $0.20 | OI 1442→2114 (ΔOI +672张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增672张（+46.6% vs前日OI），连续性待观察（方向未知）
10-23 175.0P — Vol 1,912 | 最新价 $2.69 | OI 1402→1980 (ΔOI +578张) | ΔOI/Volume 30.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增578张（+41.2% vs前日OI），连续性待观察（方向未知）
10-30 187.5C — Vol 697 | 最新价 $5.55 | OI 207→659 (ΔOI +452张) | ΔOI/Volume 64.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增452张（+218.4% vs前日OI），连续性待观察（方向未知）
10-23 200.0C — Vol 1,635 | 最新价 $0.12 | OI 2596→3035 (ΔOI +439张) | ΔOI/Volume 26.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增439张（+16.9% vs前日OI），连续性待观察（方向未知）
10-23 165.0P — Vol 1,366 | 最新价 $0.41 | OI 1797→2215 (ΔOI +418张) | ΔOI/Volume 30.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增418张（+23.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,559 张（Put 1,668 / Call 891），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +1.0k / P +1.0k ｜ Activity HIGH ｜ 1D
10-30  C +2.8k / P +1.4k ｜ Activity MEDIUM △ ｜ 8D
11-06  C +0.4k / P +1.1k ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.3k / P +44 ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 67.9k / P 42.4k，今日变化ΔOI: C +1.0k / P +1.0k，平值价格ATM: C $3.22 / P $2.72 ｜ ATM IV 74.0%，净 delta 敞口 -12k shares
Top ΔOI: P 175 +578 ｜ C 172 -551
仓位参考: Max Pain 175 ｜ Call Wall 180（+4.0%，弱）（OI 7.5k） ｜ Put Wall 165（-4.7%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.0%｜历史 Rank 45%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 12,315 股

10-30（MEDIUM △）Top ΔOI: 187C +452 ｜ 180C +395
10-30（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 185（+6.9%，弱）（OI 1.9k） ｜ Put Wall 170（-1.8%，弱）（OI 1.0k）

11-06（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+1.1%，弱）（OI 0.4k）

11-13（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 177.5（+2.5%）（OI 1.1k） ｜ Put Wall 160（-7.6%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/COIN_morning.json