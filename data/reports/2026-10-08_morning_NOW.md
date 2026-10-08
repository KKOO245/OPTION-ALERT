# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.95
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 144C ΔOI +1,366（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 137.87 → 今开 139.25（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 142.50 ｜ 低 138.35

Options: P/C成交量 0.19 | OI比 0.71 | ATM IV 54.4% | Skew 0.9pp | Term 1.11 | ExpMove ±2.6%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 1.11）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.6% ｜ 10-16（8D）±6.3% ｜ 10-23（15D）±7.8% ｜ 10-30（22D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,580,789 | GEX Change vs 上次快照 4,127,474 | Flip: Primary Flip: 134.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 540 / LOW 47 / INVALID 111
结构观察区: Primary Flip 134.15（全链重定价，覆盖 99%）
Call Wall 150（现价低于该位 7.6%）
最近结构参考: Flip 134（现价高于该位 3.3%）
量化视角： 正 Gamma（1858万，无历史分位）｜正 Gamma 增强（+413万）｜现价位于 Flip 上方 3.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 144.0C — Vol 4,190 | 最新价 $0.47 | OI 866→2232 (ΔOI +1366张) | ΔOI/Volume 32.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1366张（+157.7% vs前日OI），连续性待观察（方向未知）
10-09 140.0C — Vol 3,976 | 最新价 $1.35 | OI 2865→3752 (ΔOI +887张) | ΔOI/Volume 22.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增887张（+31.0% vs前日OI），连续性待观察（方向未知）
10-16 150.0C — Vol 1,404 | 最新价 $0.85 | OI 14185→14910 (ΔOI +725张) | ΔOI/Volume 51.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增725张（+5.1% vs前日OI），连续性待观察（方向未知）
10-16 145.0C — Vol 2,379 | 最新价 $1.74 | OI 5165→5773 (ΔOI +608张) | ΔOI/Volume 25.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增608张（+11.8% vs前日OI），连续性待观察（方向未知）
10-16 129.0P — Vol 816 | 最新价 $1.02 | OI 265→842 (ΔOI +577张) | ΔOI/Volume 70.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增577张（+217.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,163 张（Put 577 / Call 3,586），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.2k / P +0.7k ｜ Activity HIGH ｜ 1D
10-16  C +2.9k / P +1.0k ｜ Activity HIGH ｜ 8D
10-23  C +0.8k / P -52 ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 27.9k / P 19.7k，今日变化ΔOI: C +3.2k / P +0.7k，平值价格ATM: C $1.59 / P $2.02 ｜ ATM IV 54.4%，净 delta 敞口 -4k shares
Top ΔOI: C 144 +1,366 ｜ C 140 +887 ｜ C 147 +522
仓位参考: Max Pain 136 ｜ Call Wall 150（+8.3%，弱）（OI 5.2k） ｜ Put Wall 135（-2.5%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 54.4%｜历史 Rank 34%（近端代理）｜IV/RV 1.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,530 股

📆 10-16 Forward Structure
存量OI: C 83.0k / P 64.4k，今日变化ΔOI: C +2.9k / P +1.0k，平值价格ATM: C $4.65 / P $4.10 ｜ ATM IV 48.8%，净 delta 敞口 55k shares
Top ΔOI: C 150 +725 ｜ C 145 +608 ｜ P 129 +577
仓位参考: Max Pain 130 ｜ Call Wall 150（+8.3%）（OI 14.9k） ｜ Put Wall 125（-9.8%，弱）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 48.8%｜历史 Rank 34%（近端代理）｜IV/RV 1.69×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 55,387 股

10-23（MEDIUM △）Top ΔOI: 150C +240 ｜ 142C +183
10-23（MEDIUM △）仓位参考: Max Pain 134 ｜ Call Wall 140（+1.1%，弱）（OI 1.0k） ｜ Put Wall 125（-9.8%，弱）（OI 2.0k）

10-30（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 150（+8.3%，弱）（OI 0.8k） ｜ Put Wall 130（-6.2%，弱）（OI 0.6k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 54.4% vs 10-16 48.8%（差 +5.5pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NOW_morning.json