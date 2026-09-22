# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $774.05 ｜ QQQ $745.53
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
🟡 **近现价集中开仓**: 09-25 380P ΔOI +263（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 401.65 → 今开 403.00（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 403.97 ｜ 低 397.72

Options: P/C成交量 0.75 | OI比 0.60 | ATM IV 39.2% | Skew -0.0pp | Term 1.11 | ExpMove ±3.2%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常（Term 1.11）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±3.2% ｜ 10-02（10D）±4.5% ｜ 10-09（17D）±5.8% ｜ 10-16（24D）±7.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,974,902 | GEX Change vs 上次快照 231,851 | Flip: Primary Flip: 384.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 309 / LOW 149 / INVALID 432
结构观察区: Primary Flip 384.53（全链重定价，覆盖 95%）
Call Wall 400（现价低于该位 0.3%）
最近结构参考: Call Wall 400（现价低于该位 0.3%）
量化视角： 正 Gamma（197万，无历史分位）｜正 Gamma 增强（+23万）｜现价位于 Flip 上方 3.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 380（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 385（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 400.0C — Vol 605 | 最新价 $16.55 | OI 477→998 (ΔOI +521张) | ΔOI/Volume 86.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增521张（+109.2% vs前日OI），连续性待观察（方向未知）
09-25 380.0P — Vol 292 | 最新价 $0.62 | OI 45→308 (ΔOI +263张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增263张（+584.4% vs前日OI），连续性待观察（方向未知）
09-25 420.0C — Vol 167 | 最新价 $1.20 | OI 36→189 (ΔOI +153张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增153张（+425.0% vs前日OI），连续性待观察（方向未知）
09-25 415.0C — Vol 207 | 最新价 $1.70 | OI 79→228 (ΔOI +149张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增149张（+188.6% vs前日OI），连续性待观察（方向未知）
10-16 450.0C — Vol 138 | 最新价 $2.28 | OI 401→517 (ΔOI +116张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增116张（+28.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,202 张（Put 263 / Call 939），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 3D
10-02  C +77 / P +0.1k ｜ Activity HIGH ｜ 10D
10-09  C +72 / P +9 ｜ Activity HIGH ｜ 17D
10-16  C +0.9k / P -8 ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 2.4k / P 1.4k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $7.60 / P $5.10 ｜ ATM IV 39.2%，净 delta 敞口 4k shares
Top ΔOI: P 380 +263 ｜ C 420 +153 ｜ C 415 +149
仓位参考: Max Pain 380 ｜ Call Wall 430（+7.8%，弱）（OI 0.3k） ｜ Put Wall 380（-4.8%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 39.2%｜历史 Rank 45%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,929 股

📆 10-02 Forward Structure
存量OI: C 1.1k / P 3.0k，今日变化ΔOI: C +77 / P +0.1k，平值价格ATM: C $10.61 / P $7.40 ｜ ATM IV 36.0%，净 delta 敞口 280 shares
Top ΔOI: C 410 +28 ｜ P 395 +27
仓位参考: Max Pain 370 ｜ Call Wall 410（+2.8%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 36.0%｜历史 Rank 45%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 280 股

📆 10-09 Forward Structure
存量OI: C 0.5k / P 0.4k，今日变化ΔOI: C +72 / P +9，平值价格ATM: C $12.80 / P $10.20 ｜ ATM IV 32.6%，净 delta 敞口 1k shares
Top ΔOI: C 430 +43 ｜ C 410 +19 ｜ C 390 -12
仓位参考: Max Pain 380 ｜ Call Wall 380（-4.8%）（OI 0.1k） ｜ Put Wall 385（-3.5%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 32.6%｜历史 Rank 45%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,234 股

📆 10-16 Forward Structure
存量OI: C 10.1k / P 8.9k，今日变化ΔOI: C +0.9k / P -8，平值价格ATM: C $16.55 / P $13.10 ｜ ATM IV 34.4%，净 delta 敞口 37k shares
Top ΔOI: C 400 +521 ｜ C 405 +65
仓位参考: Max Pain 385 ｜ Call Wall 400（+0.3%）（OI 1.0k） ｜ Put Wall 380（-4.8%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 34.4%｜历史 Rank 45%（近端代理）｜净 delta 敞口 正 37,374 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/ISRG_morning.json