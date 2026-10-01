# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $764.48 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
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
🔴 **事件差分**: 10-02（1D）ATM IV 94.8% vs 10-09 75.6%（差 +19.2pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 235C ΔOI -3,593（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 242C ΔOI +6,208 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 235.88 → 今开 236.07（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 239.00 ｜ 低 228.47

Options: P/C成交量 0.32 | OI比 0.66 | ATM IV 94.8% | Skew -4.2pp | Term 0.81 | ExpMove ±4.5%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±4.5% ｜ 10-09（8D）±9.2% ｜ 10-16（15D）±12.3% ｜ 10-23（22D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,061,338 | GEX Change vs 上次快照 -5,326,324 | Flip: Primary Flip: 225.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 532 / LOW 34 / INVALID 132
结构观察区: Primary Flip 225.14（全链重定价，覆盖 100%）
Put Wall 210（弱结构｜现价高于该位 9.9%）
最近结构参考: Flip 225（现价高于该位 2.5%）
量化视角： 正 Gamma（706万，无历史分位）｜正 Gamma 减弱（533万）｜现价位于 Flip 上方 2.46%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 210（Put Wall，弱结构） / 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 242.5C — Vol 6,553 | 最新价 $9.00 | OI 153→6361 (ΔOI +6208张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6208张（+4057.5% vs前日OI），连续性待观察（方向未知）
10-09 220.0P — Vol 2,604 | 最新价 $4.70 | OI 656→2737 (ΔOI +2081张) | ΔOI/Volume 79.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2081张（+317.2% vs前日OI），连续性待观察（方向未知）
10-09 207.5C — Vol 1,824 | 最新价 $30.90 | OI 0→1824 (ΔOI +1824张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1824张（前日OI缺失），连续性待观察（方向未知）
10-09 210.0P — Vol 1,844 | 最新价 $2.23 | OI 991→2716 (ΔOI +1725张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1725张（+174.1% vs前日OI），连续性待观察（方向未知）
10-16 250.0C — Vol 3,813 | 最新价 $10.30 | OI 4361→5555 (ΔOI +1194张) | ΔOI/Volume 31.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1194张（+27.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,032 张（Put 3,806 / Call 9,226），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C -0.1k / P -1.9k ｜ Activity HIGH ｜ 1D
10-09  C +10.1k / P +4.7k ｜ Activity HIGH ｜ 8D
10-16  C +2.6k / P +0.6k ｜ Activity HIGH ｜ 15D
10-23  C +38 / P +16 ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 64.8k / P 42.5k，今日变化ΔOI: C -0.1k / P -1.9k，平值价格ATM: C $5.34 / P $5.11 ｜ ATM IV 94.8%，净 delta 敞口 -114k shares
Top ΔOI: C 235 -3,593 ｜ P 220 -1,778 ｜ P 210 -1,445
仓位参考: Max Pain 230 ｜ Call Wall 250（+8.4%，弱）（OI 6.3k） ｜ Put Wall 210（-9.0%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 94.8%｜历史 Rank 33%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 113,646 股

📆 10-09 Forward Structure
存量OI: C 30.7k / P 21.0k，今日变化ΔOI: C +10.1k / P +4.7k，平值价格ATM: C $10.85 / P $10.50 ｜ ATM IV 75.6%，净 delta 敞口 271k shares
Top ΔOI: C 242 +6,208 ｜ P 220 +2,081 ｜ C 207 +1,824
仓位参考: Max Pain 220 ｜ Call Wall 242.5（+5.1%）（OI 6.4k） ｜ Put Wall 220（-4.6%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 75.6%｜历史 Rank 33%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 270,831 股

📆 10-16 Forward Structure
存量OI: C 68.6k / P 84.3k，今日变化ΔOI: C +2.6k / P +0.6k，平值价格ATM: C $15.01 / P $13.30 ｜ ATM IV 76.1%，净 delta 敞口 49k shares
Top ΔOI: C 250 +1,194 ｜ C 300 +488 ｜ C 245 +285
仓位参考: Max Pain 220 ｜ Call Wall 250（+8.4%，弱）（OI 5.6k） ｜ Put Wall 210（-9.0%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.1%｜历史 Rank 33%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 49,236 股

10-23（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 240（+4.0%，弱）（OI 0.5k） ｜ Put Wall 210（-9.0%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 94.8% vs 10-09 75.6%（差 +19.2pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/NBIS_morning.json