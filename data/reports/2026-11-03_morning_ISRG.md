# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.37 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 48.7% vs 11-13 38.3%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 445C ΔOI +442（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 445C ΔOI +442 占该期限总 OI 10.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 436.87 → 今开 436.01（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 439.86 ｜ 低 434.05

Options: P/C成交量 0.91 | OI比 0.64 | ATM IV 48.7% | Skew 4.1pp | Term 0.69 | ExpMove ±4.4%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.91×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±4.4% ｜ 11-13（10D）±0.0% ｜ 11-20（17D）±5.8% ｜ 11-27（24D）±6.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,209,494 | GEX Change vs 上次快照 748,439 | Flip: Primary Flip: 416.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 279 / LOW 115 / INVALID 518
结构观察区: Primary Flip 416.88（全链重定价，覆盖 98%）
Call Wall 420（弱结构｜现价高于该位 4.2%）
最近结构参考: Call Wall 420（现价高于该位 4.2%）
量化视角： 正 Gamma（221万，无历史分位）｜正 Gamma 增强（+75万）｜现价位于 Flip 上方 5.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 430（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 417（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 445.0C — Vol 557 | 最新价 $4.80 | OI 42→484 (ΔOI +442张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增442张（+1052.4% vs前日OI），连续性待观察（方向未知）
11-06 460.0C — Vol 99 | 最新价 $1.43 | OI 26→108 (ΔOI +82张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增82张（+315.4% vs前日OI），连续性待观察（方向未知）
11-20 450.0C — Vol 254 | 最新价 $9.60 | OI 505→579 (ΔOI +74张) | ΔOI/Volume 29.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增74张（+14.7% vs前日OI），连续性待观察（方向未知）
11-06 465.0C — Vol 61 | 最新价 $1.06 | OI 41→99 (ΔOI +58张) | ΔOI/Volume 95.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增58张（+141.5% vs前日OI），连续性待观察（方向未知）
11-13 477.5C — Vol 125 | 最新价 $1.70 | OI 0→58 (ΔOI +58张) | ΔOI/Volume 46.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增58张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 714 张（Put 0 / Call 714），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.7k / P +87 ｜ Activity HIGH ｜ 3D
11-13  C +0.3k / P +4 ｜ Activity MEDIUM △ ｜ 10D
11-20  C +0.1k / P +69 ｜ Activity LOW ｜ 17D
11-27  C +20 / P +4 ｜ Activity LOW ｜ 24D

📆 11-06 Forward Structure
存量OI: C 2.5k / P 1.6k，今日变化ΔOI: C +0.7k / P +87，平值价格ATM: C $11.55 / P $7.80 ｜ ATM IV 48.7%，净 delta 敞口 18k shares
Top ΔOI: C 445 +442 ｜ C 460 +82 ｜ C 465 +58
仓位参考: Max Pain 430 ｜ Call Wall 445（+1.7%）（OI 0.5k） ｜ Put Wall 420（-4.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 48.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,919 股

11-13（MEDIUM △）Top ΔOI: 477C +58 ｜ 472C +54
11-13（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 440（+0.5%，弱）（OI 0.1k） ｜ Put Wall 420（-4.1%，弱）（OI 82）

11-20（Activity LOW）仓位参考: Max Pain 405 ｜ Call Wall 420（-4.1%，弱）（OI 0.8k） ｜ Put Wall 410（-6.3%，弱）（OI 0.5k）

11-27（Activity LOW）仓位参考: Max Pain 425 ｜ Call Wall 430（-1.8%，弱）（OI 64） ｜ Put Wall 395（-9.8%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 48.7% vs 11-13 38.3%（差 +10.4pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/ISRG_morning.json