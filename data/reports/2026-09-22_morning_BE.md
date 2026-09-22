# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $774.05 ｜ QQQ $745.51
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 92.8% vs 10-02 80.0%（差 +12.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 272.89 → 今开 274.16（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 280.79 ｜ 低 269.00

Options: P/C成交量 0.53 | OI比 1.22 | ATM IV 92.8% | Skew 3.5pp | Term 0.84 | ExpMove ±6.9%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价中性（Skew 3.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±6.9% ｜ 10-02（10D）±10.7% ｜ 10-09（17D）±6.5% ｜ 10-16（24D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,336,697 | GEX Change vs 上次快照 2,257,761 | Flip: Primary Flip: 258.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 577 / LOW 102 / INVALID 249
结构观察区: Primary Flip 258.20（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价高于该位 2.8%）
最近结构参考: Call Wall 270（现价高于该位 2.8%）
量化视角： 正 Gamma（1034万，无历史分位）｜正 Gamma 增强（+226万）｜现价位于 Flip 上方 7.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 262（MaxPain，仅结算参考） / 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 258（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 300.0C — Vol 6,015 | 最新价 $2.32 | OI 2834→4217 (ΔOI +1383张) | ΔOI/Volume 23.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1383张（+48.8% vs前日OI），连续性待观察（方向未知）
09-25 240.0P — Vol 1,866 | 最新价 $0.87 | OI 1926→2923 (ΔOI +997张) | ΔOI/Volume 53.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增997张（+51.8% vs前日OI），连续性待观察（方向未知）
09-25 250.0P — Vol 2,251 | 最新价 $2.00 | OI 3423→4279 (ΔOI +856张) | ΔOI/Volume 38.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增856张（+25.0% vs前日OI），连续性待观察（方向未知）
09-25 312.5C — Vol 863 | 最新价 $0.95 | OI 124→859 (ΔOI +735张) | ΔOI/Volume 85.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增735张（+592.7% vs前日OI），连续性待观察（方向未知）
09-25 302.5C — Vol 988 | 最新价 $2.08 | OI 125→841 (ΔOI +716张) | ΔOI/Volume 72.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增716张（+572.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,687 张（Put 1,853 / Call 2,834），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +8.4k / P +6.7k ｜ Activity HIGH ｜ 3D
10-02  C +1.6k / P +2.1k ｜ Activity MEDIUM △ ｜ 10D
10-09  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 17D
10-16  C +3.3k / P +4.0k ｜ Activity MEDIUM △ ｜ 24D

📆 09-25 Forward Structure
存量OI: C 37.2k / P 45.5k，今日变化ΔOI: C +8.4k / P +6.7k，平值价格ATM: C $10.25 / P $8.80 ｜ ATM IV 92.8%，净 delta 敞口 75k shares
Top ΔOI: C 300 +1,383 ｜ P 240 +997 ｜ P 250 +856
仓位参考: Max Pain 262 ｜ Call Wall 300（+8.1%，弱）（OI 4.2k） ｜ Put Wall 250（-9.9%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 92.8%｜历史 Rank 54%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 74,910 股

10-02（MEDIUM △）Top ΔOI: 245P +231 ｜ 290C +228
10-02（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 270（-2.7%）（OI 5.5k） ｜ Put Wall 250（-9.9%，弱）（OI 0.6k）

10-09（MEDIUM △）Top ΔOI: 260P +67
10-09（MEDIUM △）仓位参考: Max Pain 255 ｜ Call Wall 295（+6.3%）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 280C -799 ｜ 257P +628
10-16（MEDIUM △）仓位参考: Max Pain 252 ｜ Call Wall 280（+0.9%，弱）（OI 8.2k） ｜ Put Wall 260（-6.3%，弱）（OI 3.5k）

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 92.8% vs 10-02 80.0%（差 +12.8pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/BE_morning.json