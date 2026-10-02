# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔵 **期限 OI 集中**: 10-30 20C ΔOI +4,917 占该期限总 OI 77.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.73 → 今开 16.37（+4.1%） | 较昨收变动（含盘初走势） ｜ 今日高 16.40 ｜ 低 15.61

Options: P/C成交量 0.07 | OI比 0.32 | ATM IV 114.7% | Skew 35.4pp | Term 0.63 | ExpMove ±8.5%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 35.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.07×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±8.5% ｜ 10-16（14D）±11.2% ｜ 10-23（21D）±16.2% ｜ 10-30（28D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,480,022 | GEX Change vs 上次快照 1,188,387 | Flip: Primary Flip: 14.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 162 / LOW 99 / INVALID 175
结构观察区: Primary Flip 14.40（全链重定价，覆盖 84%）
Put Wall 15（弱结构｜现价高于该位 5.1%）
最近结构参考: Put Wall 15（现价高于该位 5.1%）
量化视角： 正 Gamma（148万，无历史分位）｜正 Gamma 增强（+119万）｜现价位于 Flip 上方 9.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 20.5C — Vol 5,629 | 最新价 $0.20 | OI 97→5014 (ΔOI +4917张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4917张（+5069.1% vs前日OI），连续性待观察（方向未知）
10-23 14.0P — Vol 300 | 最新价 $0.38 | OI 26→326 (ΔOI +300张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增300张（+1153.8% vs前日OI），连续性待观察（方向未知）
10-09 14.5P — Vol 172 | 最新价 $0.15 | OI 35→205 (ΔOI +170张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增170张（+485.7% vs前日OI），连续性待观察（方向未知）
10-09 16.0C — Vol 250 | 最新价 $0.65 | OI 9→109 (ΔOI +100张) | ΔOI/Volume 40.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增100张（+1111.1% vs前日OI），连续性待观察（方向未知）
10-09 16.5P — Vol 100 | 最新价 $1.02 | OI 40→140 (ΔOI +100张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增100张（+250.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,587 张（Put 570 / Call 5,017），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 5.9k / P 1.9k，今日成交量: C 0.2k / P 12，平值价格ATM: C $0.08 / P $0.35 ｜ ATM IV 114.7%，预期波动 ±2.7%，Max Pain 16
Top ΔOI: P 17 -110 ｜ C 16 +100 ｜ P 18 -86

📆 Forward Expiration Structure

10-09  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
10-16  C +39 / P -0.2k ｜ Activity LOW ｜ 14D
10-23  C +30 / P +0.3k ｜ Activity MEDIUM △ ｜ 21D
10-30  C +4.9k / P +10 ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 5.4k / P 1.8k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $0.65 / P $0.69 ｜ ATM IV 66.4%，净 delta 敞口 -5k shares
Top ΔOI: P 15 -174 ｜ P 14 +170 ｜ C 16 +100
仓位参考: Max Pain 18 ｜ Put Wall 16（+1.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.4%｜历史 Rank 60%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,793 股

10-16（Activity LOW）仓位参考: Max Pain 19 ｜ Put Wall 15（-4.8%，弱）（OI 0.9k）

10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+1.5%，弱）（OI 0.2k）

📆 10-30 Forward Structure
存量OI: C 5.7k / P 0.6k，今日变化ΔOI: C +4.9k / P +10，平值价格ATM: C $1.05 / P $1.27 ｜ ATM IV 72.0%，净 delta 敞口 73k shares
Top ΔOI: C 20 +4,917
仓位参考: Max Pain 16 ｜ Put Wall 15（-4.8%，弱）（OI 89）
量化解读： 存量 Call 重｜ATM IV 72.0%｜历史 Rank 60%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 73,253 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NNE_morning.json