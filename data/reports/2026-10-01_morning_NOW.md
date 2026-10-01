# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.36 ｜ QQQ $737.40
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 62.0% vs 10-09 50.6%（差 +11.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 145C ΔOI +911（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 150C ΔOI -2,612 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 134.01 → 今开 139.05（+3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 140.80 ｜ 低 137.73

Options: P/C成交量 0.33 | OI比 0.75 | ATM IV 61.9% | Skew 1.2pp | Term 0.95 | ExpMove ±2.9%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.9% ｜ 10-09（8D）±6.0% ｜ 10-16（15D）±8.4% ｜ 10-23（22D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,662,160 | GEX Change vs 上次快照 16,081,780 | Flip: Primary Flip: 132.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 562 / LOW 40 / INVALID 102
结构观察区: Primary Flip 132.10（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 7.1%）
最近结构参考: Flip 132（现价高于该位 5.5%）
量化视角： 正 Gamma（2366万，无历史分位）｜正 Gamma 增强（+1608万）｜现价位于 Flip 上方 5.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 132（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 134.0C — Vol 971 | 最新价 $7.05 | OI 88→1011 (ΔOI +923张) | ΔOI/Volume 95.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增923张（+1048.9% vs前日OI），连续性待观察（方向未知）
10-02 145.0C — Vol 1,553 | 最新价 $0.13 | OI 2063→2974 (ΔOI +911张) | ΔOI/Volume 58.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增911张（+44.2% vs前日OI），连续性待观察（方向未知）
10-02 130.0C — Vol 1,946 | 最新价 $5.10 | OI 1129→1642 (ΔOI +513张) | ΔOI/Volume 26.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增513张（+45.4% vs前日OI），连续性待观察（方向未知）
10-02 128.0P — Vol 1,235 | 最新价 $0.35 | OI 739→1189 (ΔOI +450张) | ΔOI/Volume 36.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增450张（+60.9% vs前日OI），连续性待观察（方向未知）
10-02 138.0C — Vol 1,069 | 最新价 $0.88 | OI 944→1378 (ΔOI +434张) | ΔOI/Volume 40.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增434张（+46.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,231 张（Put 450 / Call 2,781），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +3.0k / P +0.3k ｜ Activity HIGH ｜ 1D
10-09  C -1.9k / P +0.3k ｜ Activity HIGH ｜ 8D
10-16  C -0.1k / P -0.5k ｜ Activity HIGH ｜ 15D
10-23  C +1.4k / P -10 ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 34.4k / P 25.7k，今日变化ΔOI: C +3.0k / P +0.3k，平值价格ATM: C $1.89 / P $2.08 ｜ ATM IV 62.0%，净 delta 敞口 126k shares
Top ΔOI: C 145 +911 ｜ C 130 +513 ｜ C 132 -464
仓位参考: Max Pain 132 ｜ Call Wall 150（+7.7%，弱）（OI 3.2k） ｜ Put Wall 130（-6.7%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 62.0%｜历史 Rank 74%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 126,104 股

📆 10-09 Forward Structure
存量OI: C 13.4k / P 11.9k，今日变化ΔOI: C -1.9k / P +0.3k，平值价格ATM: C $4.25 / P $4.05 ｜ ATM IV 50.6%，净 delta 敞口 -29k shares
Top ΔOI: C 150 -2,612 ｜ C 135 +156
仓位参考: Max Pain 134 ｜ Call Wall 150（+7.7%）（OI 4.5k） ｜ Put Wall 131（-6.0%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.6%｜历史 Rank 74%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 负 29,077 股

📆 10-16 Forward Structure
存量OI: C 75.9k / P 62.3k，今日变化ΔOI: C -0.1k / P -0.5k，平值价格ATM: C $5.90 / P $5.85 ｜ ATM IV 49.8%，净 delta 敞口 958 shares
Top ΔOI: P 125 -635 ｜ C 145 -198 ｜ C 130 -71
仓位参考: Max Pain 130 ｜ Call Wall 150（+7.7%）（OI 13.9k） ｜ Put Wall 130（-6.7%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 49.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 958 股

10-23（MEDIUM △）Top ΔOI: 134C +923 ｜ 150C +74
10-23（MEDIUM △）仓位参考: Max Pain 133 ｜ Call Wall 134（-3.8%，弱）（OI 1.0k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 62.0% vs 10-09 50.6%（差 +11.4pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/NOW_morning.json