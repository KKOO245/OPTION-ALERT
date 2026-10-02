# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $753.96
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 235C ΔOI +641（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 232.28 → 今开 235.76（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 246.30 ｜ 低 235.34

Options: P/C成交量 0.37 | OI比 0.63 | ATM IV 104.9% | Skew -1.8pp | Term 0.74 | ExpMove ±8.2%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±8.2% ｜ 10-16（14D）±11.8% ｜ 10-23（21D）±14.5% ｜ 10-30（28D）±19.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,995,489 | GEX Change vs 上次快照 15,046,873 | Flip: Primary Flip: 225.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 526 / LOW 47 / INVALID 125
结构观察区: Primary Flip 225.28（全链重定价，覆盖 100%）
最近结构参考: Flip 225（现价高于该位 8.5%）
量化视角： 正 Gamma（2400万，无历史分位）｜正 Gamma 增强（+1505万）｜现价位于 Flip 上方 8.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 220.0P — Vol 2,464 | 最新价 $7.99 | OI 3262→4524 (ΔOI +1262张) | ΔOI/Volume 51.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1262张（+38.7% vs前日OI），连续性待观察（方向未知）
10-16 210.0P — Vol 1,426 | 最新价 $4.68 | OI 3669→4504 (ΔOI +835张) | ΔOI/Volume 58.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增835张（+22.8% vs前日OI），连续性待观察（方向未知）
10-09 210.0P — Vol 1,253 | 最新价 $2.10 | OI 2716→3524 (ΔOI +808张) | ΔOI/Volume 64.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增808张（+29.8% vs前日OI），连续性待观察（方向未知）
10-02 285.0C — Vol 862 | 最新价 $0.02 | OI 824→1600 (ΔOI +776张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增776张（+94.2% vs前日OI），连续性待观察（方向未知）
10-16 230.0C — Vol 1,232 | 最新价 $15.15 | OI 3285→4004 (ΔOI +719张) | ΔOI/Volume 58.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增719张（+21.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,400 张（Put 2,905 / Call 1,495），跨 3 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 66.3k / P 41.7k，今日成交量: C 18.1k / P 6.7k，平值价格ATM: C $2.42 / P $3.15 ｜ ATM IV 104.9%，预期波动 ±2.3%，Max Pain 230
Top ΔOI: C 285 +776 ｜ C 240 +583 ｜ C 265 -392

📆 Forward Expiration Structure

10-09  C +1.9k / P +4.0k ｜ Activity HIGH ｜ 7D
10-16  C +2.8k / P +2.9k ｜ Activity HIGH ｜ 14D
10-23  C +0.9k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
10-30  C +0.3k / P +1.2k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 32.6k / P 25.0k，今日变化ΔOI: C +1.9k / P +4.0k，平值价格ATM: C $10.00 / P $10.00 ｜ ATM IV 72.0%，净 delta 敞口 45k shares
Top ΔOI: P 210 +808 ｜ C 212 -739 ｜ C 235 +641
仓位参考: Max Pain 222 ｜ Call Wall 242.5（-0.8%）（OI 6.7k） ｜ Put Wall 225（-8.0%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.0%｜历史 Rank 53%（近端代理）｜IV/RV 1.40×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 44,853 股

📆 10-16 Forward Structure
存量OI: C 71.4k / P 87.2k，今日变化ΔOI: C +2.8k / P +2.9k，平值价格ATM: C $14.20 / P $14.57 ｜ ATM IV 73.6%，净 delta 敞口 90k shares
Top ΔOI: P 220 +1,262 ｜ P 210 +835 ｜ C 230 +719
仓位参考: Max Pain 220 ｜ Call Wall 250（+2.3%，弱）（OI 6.0k）
量化解读： 存量 Put 重｜ATM IV 73.6%｜历史 Rank 53%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 89,573 股

10-23（MEDIUM △）Top ΔOI: 220C +672 ｜ 220P +196
10-23（MEDIUM △）仓位参考: Max Pain 225 ｜ Call Wall 230（-5.9%，弱）（OI 0.5k） ｜ Put Wall 230（-5.9%，弱）（OI 0.3k）

10-30（MEDIUM △）Top ΔOI: 180P +543 ｜ 275C -383
10-30（MEDIUM △）仓位参考: Max Pain 225 ｜ Call Wall 260（+6.4%，弱）（OI 0.5k） ｜ Put Wall 240（-1.8%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NBIS_morning.json