# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.51 ｜ QQQ $721.50
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 11.09 → 今开 10.97（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 11.13 ｜ 低 10.77

Options: P/C成交量 0.24 | OI比 0.18 | ATM IV 133.3% | Skew 30.3pp | Term 0.63 | ExpMove ±8.8%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 30.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.18×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±8.8% ｜ 10-30（14D）±13.8% ｜ 11-06（21D）±15.3% ｜ 11-13（28D）±20.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,454,264 | GEX Change vs 上次快照 2,927,871 | Flip: Primary Flip: 10.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 190 / LOW 92 / INVALID 130
结构观察区: Primary Flip 10.28（全链重定价，覆盖 93%）
最近结构参考: Flip 10（现价高于该位 7.8%）
量化视角： 正 Gamma（345万，无历史分位）｜正 Gamma 增强（+293万）｜现价位于 Flip 上方 7.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 10.0P — Vol 6,405 | 最新价 $0.69 | OI 1542→7611 (ΔOI +6069张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6069张（+393.6% vs前日OI），连续性待观察（方向未知）
11-20 14.0C — Vol 1,598 | 最新价 $0.40 | OI 960→2177 (ΔOI +1217张) | ΔOI/Volume 76.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1217张（+126.8% vs前日OI），连续性待观察（方向未知）
10-16 12.0C — Vol 1,455 | 最新价 $0.02 | OI 1084→1932 (ΔOI +848张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增848张（+78.2% vs前日OI），连续性待观察（方向未知）
11-20 11.0C — Vol 725 | 最新价 $1.29 | OI 370→1055 (ΔOI +685张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增685张（+185.1% vs前日OI），连续性待观察（方向未知）
10-16 11.5C — Vol 1,770 | 最新价 $0.08 | OI 1152→1733 (ΔOI +581张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增581张（+50.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,400 张（Put 6,069 / Call 3,331），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 61.0k / P 10.7k，今日成交量: C 1.3k / P 0.3k，平值价格ATM: C $0.17 / P $0.14 ｜ ATM IV 133.3%，预期波动 ±2.8%，Max Pain 12
Top ΔOI: C 12 +848 ｜ P 14 -810 ｜ P 15 -745

📆 Forward Expiration Structure

10-23  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 7D
10-30  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
11-06  C +78 / P -77 ｜ Activity MEDIUM △ ｜ 21D
11-13  C +0.5k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 16.4k / P 6.1k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $0.52 / P $0.46 ｜ ATM IV 77.5%，净 delta 敞口 45k shares
Top ΔOI: P 17 -196 ｜ C 11 +118
仓位参考: Max Pain 12 ｜ Put Wall 12（+8.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 77.5%｜历史 Rank 71%（近端代理）｜IV/RV 1.39×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 45,177 股

10-30（MEDIUM △）Top ΔOI: 12C +114
10-30（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 12（+8.4%，弱）（OI 0.3k） ｜ Put Wall 12（+8.4%，弱）（OI 0.9k）

11-06（MEDIUM △）Top ΔOI: 11C +27
11-06（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 10（-9.7%，弱）（OI 0.8k）

11-13（MEDIUM △）Top ΔOI: 11C +64
11-13（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 12（+8.4%，弱）（OI 0.3k） ｜ Put Wall 11（-0.7%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/USAR_morning.json