# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.01 ｜ QQQ $716.42
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
🟡 **近现价集中开仓**: 10-23 190C ΔOI +4,350（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 183.81 → 今开 181.11（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 183.40 ｜ 低 178.77

Options: P/C成交量 1.28 | OI比 0.81 | ATM IV 88.2% | Skew -0.2pp | Term 0.82 | ExpMove ±6.6%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.81）+ 当日成交偏 Put（P/C量 1.28）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.28×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（7D）±6.6% ｜ 10-30（14D）±12.2% ｜ 11-06（21D）±13.9% ｜ 11-13（28D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,106,277 | GEX Change vs 上次快照 -9,045,749 | Flip: Primary Flip: 171.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 436 / LOW 121 / INVALID 265
结构观察区: Primary Flip 171.84（全链重定价，覆盖 96%）
最近结构参考: Flip 172（现价高于该位 5.5%）
量化视角： 正 Gamma（2911万，无历史分位）｜正 Gamma 减弱（905万）｜现价位于 Flip 上方 5.50%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 172（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 197.5C — Vol 6,035 | 最新价 $2.42 | OI 823→5819 (ΔOI +4996张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4996张（+607.0% vs前日OI），连续性待观察（方向未知）
10-23 190.0C — Vol 6,200 | 最新价 $4.50 | OI 1751→6101 (ΔOI +4350张) | ΔOI/Volume 70.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4350张（+248.4% vs前日OI），连续性待观察（方向未知）
10-23 100.0P — Vol 2,399 | 最新价 $0.06 | OI 6294→8499 (ΔOI +2205张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2205张（+35.0% vs前日OI），连续性待观察（方向未知）
10-23 172.5C — Vol 1,203 | 最新价 $14.81 | OI 140→1099 (ΔOI +959张) | ΔOI/Volume 79.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增959张（+685.0% vs前日OI），连续性待观察（方向未知）
10-23 195.0C — Vol 1,350 | 最新价 $2.93 | OI 733→1617 (ΔOI +884张) | ΔOI/Volume 65.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增884张（+120.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,394 张（Put 2,205 / Call 11,189），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 129.7k / P 105.7k，今日成交量: C 7.6k / P 9.8k，平值价格ATM: C $1.48 / P $2.02 ｜ ATM IV 88.2%，预期波动 ±1.9%，Max Pain 178
Top ΔOI: C 185 -5,308 ｜ C 192 -2,727 ｜ P 165 -1,756

📆 Forward Expiration Structure

10-23  C +15.3k / P +5.0k ｜ Activity HIGH ｜ 7D
10-30  C +1.1k / P +1.8k ｜ Activity MEDIUM △ ｜ 14D
11-06  C +0.5k / P +9 ｜ Activity MEDIUM △ ｜ 21D
11-13  C +0.1k / P +0.6k ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 30.7k / P 25.9k，今日变化ΔOI: C +15.3k / P +5.0k，平值价格ATM: C $5.72 / P $6.21 ｜ ATM IV 58.8%，净 delta 敞口 373k shares
Top ΔOI: C 197 +4,996 ｜ C 190 +4,350
仓位参考: Max Pain 180 ｜ Call Wall 190（+4.8%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 58.8%｜历史 Rank 78%（近端代理）｜IV/RV 1.34×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 372,915 股

10-30（MEDIUM △）Top ΔOI: 180C +215 ｜ 185C +188
10-30（MEDIUM △）仓位参考: Max Pain 182 ｜ Call Wall 185（+2.0%，弱）（OI 1.6k） ｜ Put Wall 180（-0.7%，弱）（OI 0.9k）

11-06（MEDIUM △）Top ΔOI: 125C +94 ｜ 180P -51
11-06（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（-3.5%，弱）（OI 0.2k）

11-13（MEDIUM △）Top ΔOI: 155P +157 ｜ 167P +127
11-13（MEDIUM △）仓位参考: Max Pain 182 ｜ Call Wall 185（+2.0%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/COIN_morning.json