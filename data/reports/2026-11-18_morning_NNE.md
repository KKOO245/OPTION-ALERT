# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.13 ｜ QQQ $659.51
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 119.5% vs 11-27 89.3%（差 +30.2pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 11C ΔOI +127（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 10.49 → 今开 10.62（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 11.25 ｜ 低 10.35

Options: P/C成交量 1.03 | OI比 0.30 | ATM IV 119.5% | Skew 14.2pp | Term 0.79 | ExpMove ±9.2%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 14.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±9.2% ｜ 11-27（9D）±11.9% ｜ 12-04（16D）±15.5% ｜ 12-11（23D）±17.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,510,736 | GEX Change vs 上次快照 767,595 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 71%（带内） ｜ IV 有效性: VALID 166 / LOW 71 / INVALID 129
结构观察区: NO_CROSS
Put Wall 11（弱结构｜现价高于该位 0.4%）
最近结构参考: Put Wall 11（现价高于该位 0.4%）
量化视角： 正 Gamma（151万，无历史分位）｜正 Gamma 增强（+77万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall，弱结构）；上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 11.0C — Vol 158 | 最新价 $0.15 | OI 157→284 (ΔOI +127张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+80.9% vs前日OI），连续性待观察（方向未知）
11-20 11.5C — Vol 85 | 最新价 $0.07 | OI 365→437 (ΔOI +72张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增72张（+19.7% vs前日OI），连续性待观察（方向未知）
12-04 11.0C — Vol 65 | 最新价 $0.56 | OI 1→65 (ΔOI +64张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64张（+6400.0% vs前日OI），连续性待观察（方向未知）
12-18 12.0C — Vol 27 | 最新价 $0.40 | OI 133→157 (ΔOI +24张) | ΔOI/Volume 88.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增24张（+18.1% vs前日OI），值得跟踪（方向未知）
11-20 16.5P — Vol 67 | 最新价 $6.15 | OI 11→28 (ΔOI +17张) | ΔOI/Volume 25.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17张（+154.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 304 张（Put 17 / Call 287），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +0.2k / P -13 ｜ Activity MEDIUM △ ｜ 2D
11-27  C +9 / P +1 ｜ Activity MEDIUM △ ｜ 9D
12-04  C +67 / P +3 ｜ Activity HIGH ｜ 16D
12-11  C +18 / P +1 ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 7.0k / P 2.1k，今日变化ΔOI: C +0.2k / P -13，平值价格ATM: C $0.15 / P $0.87 ｜ ATM IV 119.5%，净 delta 敞口 7k shares
Top ΔOI: C 11 +127 ｜ C 11 +72 ｜ P 11 -32
仓位参考: Max Pain 12 ｜ Call Wall 12（+8.6%，弱）（OI 0.9k） ｜ Put Wall 12（+8.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 119.5%｜历史 Rank 68%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,120 股

11-27（MEDIUM △）Top ΔOI: 10C +7 ｜ 11P +7
11-27（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 10（-9.5%，弱）（OI 0.1k）

📆 12-04 Forward Structure
存量OI: C 0.6k / P 0.4k，今日变化ΔOI: C +67 / P +3，平值价格ATM: C $0.56 / P $1.15 ｜ ATM IV 96.4%，净 delta 敞口 3k shares
Top ΔOI: C 11 +64 ｜ C 11 +2 ｜ P 10 +1
仓位参考: Max Pain 12 ｜ Call Wall 11（-0.4%，弱）（OI 65）
量化解读： 存量 Call 重｜ATM IV 96.4%｜历史 Rank 68%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,684 股

12-11（MEDIUM △）Top ΔOI: 12C +4
12-11（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 11（-0.4%，弱）（OI 41） ｜ Put Wall 12（+8.6%）（OI 23）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 119.5% vs 11-27 89.3%（差 +30.2pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/NNE_morning.json