# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.54
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-11 11C ΔOI -1（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 11.09 → 今开 11.10（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 11.25 ｜ 低 10.77

Options: P/C成交量 0.93 | OI比 0.35 | ATM IV 121.9% | Skew 31.3pp | Term 0.69 | ExpMove ±15.5%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 31.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±15.5% ｜ 11-27（14D）±12.0% ｜ 12-04（21D）±5.1% ｜ 12-11（28D）±16.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,048,896 | GEX Change vs 上次快照 -314,441 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 123 / LOW 81 / INVALID 182
结构观察区: NO_CROSS
Put Wall 11（现价低于该位 1.5%）
最近结构参考: Put Wall 11（现价低于该位 1.5%）
量化视角： 正 Gamma（105万，无历史分位）｜正 Gamma 减弱（31万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 11（Put Wall） / 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 10.0P — Vol 75 | 最新价 $0.25 | OI 19→94 (ΔOI +75张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增75张（+394.7% vs前日OI），连续性待观察（方向未知）
11-20 13.0C — Vol 47 | 最新价 $0.10 | OI 144→174 (ΔOI +30张) | ΔOI/Volume 63.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30张（+20.8% vs前日OI），连续性待观察（方向未知）
11-20 12.0C — Vol 32 | 最新价 $0.27 | OI 688→711 (ΔOI +23张) | ΔOI/Volume 71.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增23张（+3.3% vs前日OI），值得跟踪（方向未知）
12-04 12.0P — Vol 21 | 最新价 $1.27 | OI 3→23 (ΔOI +20张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20张（+666.7% vs前日OI），连续性待观察（方向未知）
12-18 10.0C — Vol 15 | 最新价 $1.85 | OI 28→43 (ΔOI +15张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15张（+53.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 163 张（Put 95 / Call 68），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 3.0k / P 1.1k，今日成交量: C 0.1k / P 0.1k，平值价格ATM: C $0.33 / P $0.25 ｜ ATM IV 121.9%，预期波动 ±5.3%，Max Pain 12
Top ΔOI: P 13 -76 ｜ P 12 -67 ｜ C 13 -31

📆 Forward Expiration Structure

11-20  C +62 / P -35 ｜ Activity MEDIUM △ ｜ 7D
11-27  C +8 / P +78 ｜ Activity HIGH ｜ 14D
12-04  C -1 / P +24 ｜ Activity MEDIUM △ ｜ 21D
12-11  C -12 / P +2 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 6.3k / P 2.0k，今日变化ΔOI: C +62 / P -35，平值价格ATM: C $1.23 / P $0.45 ｜ ATM IV 86.1%，净 delta 敞口 5k shares
仓位参考: Max Pain 12 ｜ Call Wall 10（-7.7%，弱）（OI 0.2k） ｜ Put Wall 11（+1.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 86.1%｜历史 Rank 70%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,399 股

📆 11-27 Forward Structure
存量OI: C 4.8k / P 0.7k，今日变化ΔOI: C +8 / P +78，平值价格ATM: C $0.90 / P $0.40 ｜ ATM IV 80.0%，净 delta 敞口 -2k shares
Top ΔOI: P 10 +75 ｜ P 11 +2
仓位参考: Max Pain 12 ｜ Put Wall 10（-7.7%，弱）（OI 94）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 80.0%｜历史 Rank 70%（近端代理）｜IV/RV 0.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,764 股

12-04（MEDIUM △）Top ΔOI: 11P +2
12-04（MEDIUM △）仓位参考: Max Pain 13

12-11（MEDIUM △）Top ΔOI: 11C -1
12-11（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 10（-7.7%，弱）（OI 33） ｜ Put Wall 11（+1.5%，弱）（OI 13）

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 86.1% vs 11-27 80.0%（差 +6.0pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/NNE_morning.json