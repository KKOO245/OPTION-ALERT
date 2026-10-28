# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.82
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 40.87 → 今开 40.92（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 41.36 ｜ 低 39.69

Options: P/C成交量 0.30 | OI比 0.62 | ATM IV 77.5% | Skew -4.9pp | Term 0.84 | ExpMove ±4.6%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±4.6% ｜ 11-06（9D）±9.8% ｜ 11-13（16D）±12.6% ｜ 11-20（23D）±12.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,250,445 | GEX Change vs 上次快照 927,389 | Flip: Primary Flip: 38.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 306 / LOW 64 / INVALID 156
结构观察区: Primary Flip 38.41（全链重定价，覆盖 95%）
最近结构参考: Flip 38（现价高于该位 3.8%）
量化视角： 正 Gamma（225万，无历史分位）｜正 Gamma 增强（+93万）｜现价位于 Flip 上方 3.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 41（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 38（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 36.5P — Vol 649 | 最新价 $1.12 | OI 95→743 (ΔOI +648张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增648张（+682.1% vs前日OI），连续性待观察（方向未知）
11-06 45.0C — Vol 693 | 最新价 $0.73 | OI 997→1619 (ΔOI +622张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增622张（+62.4% vs前日OI），连续性待观察（方向未知）
10-30 43.0C — Vol 711 | 最新价 $0.39 | OI 482→1004 (ΔOI +522张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增522张（+108.3% vs前日OI），连续性待观察（方向未知）
11-20 45.0C — Vol 601 | 最新价 $1.43 | OI 1479→1913 (ΔOI +434张) | ΔOI/Volume 72.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增434张（+29.3% vs前日OI），连续性待观察（方向未知）
11-27 48.0C — Vol 411 | 最新价 $1.00 | OI 603→1001 (ΔOI +398张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增398张（+66.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,624 张（Put 648 / Call 1,976），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +1.0k / P +0.5k ｜ Activity MEDIUM △ ｜ 2D
11-06  C +1.2k / P +41 ｜ Activity MEDIUM △ ｜ 9D
11-13  C +0.2k / P +6 ｜ Activity MEDIUM △ ｜ 16D
11-20  C +0.9k / P +0.8k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 13.1k / P 8.1k，今日变化ΔOI: C +1.0k / P +0.5k，平值价格ATM: C $0.83 / P $1.00 ｜ ATM IV 77.5%，净 delta 敞口 15k shares
Top ΔOI: C 43 +522 ｜ C 41 +359 ｜ C 41 +218
仓位参考: Max Pain 41 ｜ Call Wall 40（+0.3%，弱）（OI 1.1k） ｜ Put Wall 38（-4.7%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 77.5%｜历史 Rank 69%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,010 股

11-06（MEDIUM △）Top ΔOI: 42C +141
11-06（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 43（+7.9%，弱）（OI 0.9k） ｜ Put Wall 38（-4.7%）（OI 0.9k）

11-13（MEDIUM △）Top ΔOI: 43C +57 ｜ 42C +34
11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 39（-2.2%）（OI 0.8k）

11-20（MEDIUM △）Top ΔOI: 36P +648
11-20（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 40（+0.3%，弱）（OI 0.9k） ｜ Put Wall 40（+0.3%，弱）（OI 1.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/MP_morning.json