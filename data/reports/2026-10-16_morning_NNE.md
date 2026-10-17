# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 13C ΔOI +95（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 15C ΔOI +196 占该期限总 OI 24.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 13.59 → 今开 13.43（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 13.72 ｜ 低 13.28

Options: P/C成交量 1.04 | OI比 0.16 | ATM IV 90.4% | Skew 14.3pp | Term 0.82 | ExpMove ±9.8%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 14.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.16）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.16×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±9.8% ｜ 10-30（14D）±10.3% ｜ 11-06（21D）±22.7% ｜ 11-13（28D）±17.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 720,976 | GEX Change vs 上次快照 288,477 | Flip: Primary Flip: 12.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 165 / LOW 104 / INVALID 147
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 12.49（全链重定价，覆盖 90%）
Put Wall 14（弱结构｜现价低于该位 2.5%）
最近结构参考: Put Wall 14（现价低于该位 2.5%）
量化视角： 正 Gamma（72万，无历史分位）｜正 Gamma 增强（+29万）｜现价位于 Flip 上方 9.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall，弱结构） / 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 15.5C — Vol 197 | 最新价 $0.35 | OI 4→200 (ΔOI +196张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增196张（+4900.0% vs前日OI），连续性待观察（方向未知）
10-23 15.0C — Vol 110 | 最新价 $0.17 | OI 40→143 (ΔOI +103张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增103张（+257.5% vs前日OI），连续性待观察（方向未知）
10-23 13.5C — Vol 143 | 最新价 $0.67 | OI 73→168 (ΔOI +95张) | ΔOI/Volume 66.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增95张（+130.1% vs前日OI），连续性待观察（方向未知）
10-23 14.0C — Vol 76 | 最新价 $0.42 | OI 33→97 (ΔOI +64张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64张（+193.9% vs前日OI），连续性待观察（方向未知）
10-30 12.0P — Vol 61 | 最新价 $0.33 | OI 13→71 (ΔOI +58张) | ΔOI/Volume 95.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增58张（+446.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 516 张（Put 58 / Call 458），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 23.2k / P 3.7k，今日成交量: C 0.4k / P 0.4k，平值价格ATM: C $0.30 / P $0.23 ｜ ATM IV 90.4%，预期波动 ±3.8%，Max Pain 15
Top ΔOI: P 20 -55 ｜ C 12 +53 ｜ C 13 +43

📆 Forward Expiration Structure

10-23  C +0.3k / P +20 ｜ Activity HIGH ｜ 7D
10-30  C +74 / P +86 ｜ Activity HIGH ｜ 14D
11-06  C +46 / P +16 ｜ Activity MEDIUM △ ｜ 21D
11-13  C +0.3k / P +69 ｜ Activity HIGH ｜ 28D

📆 10-23 Forward Structure
存量OI: C 5.7k / P 1.8k，今日变化ΔOI: C +0.3k / P +20，平值价格ATM: C $0.67 / P $0.66 ｜ ATM IV 73.2%，净 delta 敞口 10k shares
Top ΔOI: C 15 +103 ｜ C 13 +95 ｜ C 14 +64
仓位参考: Max Pain 16 ｜ Put Wall 14（+2.6%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 73.2%｜历史 Rank 23%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 9,575 股

📆 10-30 Forward Structure
存量OI: C 6.4k / P 1.0k，今日变化ΔOI: C +74 / P +86，平值价格ATM: C $0.60 / P $0.80 ｜ ATM IV 70.7%，净 delta 敞口 3k shares
Top ΔOI: C 13 +41 ｜ C 14 +33
仓位参考: Max Pain 15 ｜ Put Wall 14（+2.6%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.7%｜历史 Rank 23%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 2,776 股

11-06（MEDIUM △）Top ΔOI: 15C +8
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（-4.7%，弱）（OI 76）

📆 11-13 Forward Structure
存量OI: C 0.6k / P 0.2k，今日变化ΔOI: C +0.3k / P +69，平值价格ATM: C $1.00 / P $1.35 ｜ ATM IV 74.1%，净 delta 敞口 9k shares
Top ΔOI: C 13 +47
仓位参考: Max Pain 14 ｜ Call Wall 14.5（+6.3%，弱）（OI 0.1k） ｜ Put Wall 13（-4.7%，弱）（OI 21）
量化解读： 存量 Call 重｜ATM IV 74.1%｜历史 Rank 23%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 9,087 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/NNE_morning.json