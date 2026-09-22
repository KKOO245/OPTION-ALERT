# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.25 ｜ QQQ $747.46
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 95.5% vs 10-02 84.6%（差 +10.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 250C ΔOI +3,124（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 232.80 → 今开 233.51（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 246.61 ｜ 低 231.76

Options: P/C成交量 0.44 | OI比 0.86 | ATM IV 95.5% | Skew -1.9pp | Term 0.87 | ExpMove ±7.2%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（3D）±7.2% ｜ 10-02（10D）±11.8% ｜ 10-09（17D）±14.1% ｜ 10-16（24D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,159,629 | GEX Change vs 上次快照 7,348,088 | Flip: Primary Flip: 216.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 531 / LOW 40 / INVALID 155
结构观察区: Primary Flip 216.84（全链重定价，覆盖 100%）
最近结构参考: Flip 217（现价高于该位 12.5%）
量化视角： 正 Gamma（1716万，无历史分位）｜正 Gamma 增强（+735万）｜现价位于 Flip 上方 12.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 217（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 310.0C — Vol 4,060 | 最新价 $0.84 | OI 628→3961 (ΔOI +3333张) | ΔOI/Volume 82.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3333张（+530.7% vs前日OI），连续性待观察（方向未知）
09-25 250.0C — Vol 19,147 | 最新价 $3.10 | OI 3520→6644 (ΔOI +3124张) | ΔOI/Volume 16.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3124张（+88.8% vs前日OI），连续性待观察（方向未知）
09-25 260.0C — Vol 7,430 | 最新价 $1.61 | OI 1194→3546 (ΔOI +2352张) | ΔOI/Volume 31.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2352张（+197.0% vs前日OI），连续性待观察（方向未知）
09-25 220.0P — Vol 3,689 | 最新价 $3.50 | OI 3557→5683 (ΔOI +2126张) | ΔOI/Volume 57.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2126张（+59.8% vs前日OI），连续性待观察（方向未知）
10-16 275.0C — Vol 2,211 | 最新价 $7.75 | OI 0→2077 (ΔOI +2077张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2077张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,012 张（Put 2,126 / Call 10,886），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +16.5k / P +8.6k ｜ Activity HIGH ｜ 3D
10-02  C +7.7k / P +1.7k ｜ Activity HIGH ｜ 10D
10-09  C +1.8k / P +1.1k ｜ Activity HIGH ｜ 17D
10-16  C +4.2k / P +2.2k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 60.5k / P 52.0k，今日变化ΔOI: C +16.5k / P +8.6k，平值价格ATM: C $8.00 / P $9.58 ｜ ATM IV 95.5%，净 delta 敞口 341k shares
Top ΔOI: C 250 +3,124 ｜ C 260 +2,352 ｜ P 220 +2,126
仓位参考: Max Pain 220 ｜ Call Wall 250（+2.5%，弱）（OI 6.6k） ｜ Put Wall 220（-9.8%）（OI 5.7k）
量化解读： 存量两侧均衡｜ATM IV 95.5%｜历史 Rank 33%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 340,850 股

📆 10-02 Forward Structure
存量OI: C 21.7k / P 16.7k，今日变化ΔOI: C +7.7k / P +1.7k，平值价格ATM: C $13.65 / P $15.00 ｜ ATM IV 84.6%，净 delta 敞口 152k shares
Top ΔOI: C 310 +3,333 ｜ C 250 +998 ｜ C 315 +612
仓位参考: Max Pain 220 ｜ Call Wall 250（+2.5%，弱）（OI 1.9k） ｜ Put Wall 220（-9.8%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 84.6%｜历史 Rank 33%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 152,447 股

📆 10-09 Forward Structure
存量OI: C 10.5k / P 10.2k，今日变化ΔOI: C +1.8k / P +1.1k，平值价格ATM: C $16.24 / P $18.20 ｜ ATM IV 83.6%，净 delta 敞口 59k shares
Top ΔOI: C 200 +399 ｜ C 320 +306
仓位参考: Max Pain 220 ｜ Call Wall 240（-1.6%）（OI 1.8k） ｜ Put Wall 225（-7.7%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 83.6%｜历史 Rank 33%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 正 58,582 股

📆 10-16 Forward Structure
存量OI: C 53.2k / P 74.4k，今日变化ΔOI: C +4.2k / P +2.2k，平值价格ATM: C $19.23 / P $21.30 ｜ ATM IV 83.8%，净 delta 敞口 70k shares
Top ΔOI: C 275 +2,077 ｜ P 245 +1,001 ｜ C 300 +572
仓位参考: Max Pain 210 ｜ Call Wall 240（-1.6%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 83.8%｜历史 Rank 33%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 正 70,043 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 95.5% vs 10-02 84.6%（差 +10.9pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/NBIS_morning.json