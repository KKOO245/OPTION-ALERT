# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $718.15 ｜ QQQ $638.10
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 167C ΔOI +620（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 159.36 → 今开 157.80（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 162.97 ｜ 低 157.80

Options: P/C成交量 0.43 | OI比 0.53 | ATM IV 64.5% | Skew 8.4pp | Term 0.89 | ExpMove ±4.8%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 8.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±4.8% ｜ 12-04（10D）±8.5% ｜ 12-11（17D）±10.8% ｜ 12-18（24D）±12.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 30,295,490 | GEX Change vs 上次快照 9,938,191 | Flip: Primary Flip: 151.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 499 / LOW 166 / INVALID 243
结构观察区: Primary Flip 151.41（全链重定价，覆盖 100%）
Call Wall 165（弱结构｜现价低于该位 1.8%）
最近结构参考: Call Wall 165（现价低于该位 1.8%）
量化视角： 正 Gamma（3030万，无历史分位）｜正 Gamma 增强（+994万）｜现价位于 Flip 上方 7.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 175.0C — Vol 12,549 | 最新价 $0.33 | OI 1422→10695 (ΔOI +9273张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9273张（+652.1% vs前日OI），连续性待观察（方向未知）
11-27 177.5C — Vol 9,771 | 最新价 $0.11 | OI 1157→8092 (ΔOI +6935张) | ΔOI/Volume 71.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6935张（+599.4% vs前日OI），连续性待观察（方向未知）
12-04 180.0C — Vol 6,166 | 最新价 $0.87 | OI 1043→5998 (ΔOI +4955张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4955张（+475.1% vs前日OI），连续性待观察（方向未知）
11-27 172.5C — Vol 4,564 | 最新价 $0.57 | OI 1532→3308 (ΔOI +1776张) | ΔOI/Volume 38.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1776张（+115.9% vs前日OI），连续性待观察（方向未知）
12-18 115.0P — Vol 2,695 | 最新价 $0.65 | OI 2792→4411 (ΔOI +1619张) | ΔOI/Volume 60.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1619张（+58.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,558 张（Put 1,619 / Call 22,939），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +18.9k / P +6.2k ｜ Activity HIGH ｜ 3D
12-04  C +8.8k / P +3.5k ｜ Activity HIGH ｜ 10D
12-11  C +1.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 17D
12-18  C +1.4k / P +3.9k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 104.8k / P 56.0k，今日变化ΔOI: C +18.9k / P +6.2k，平值价格ATM: C $3.54 / P $4.32 ｜ ATM IV 64.5%，净 delta 敞口 -23k shares
Top ΔOI: C 175 +9,273 ｜ C 177 +6,935 ｜ C 172 +1,776
仓位参考: Max Pain 152 ｜ Call Wall 175（+8.0%，弱）（OI 10.7k） ｜ Put Wall 150（-7.5%，弱）（OI 5.1k）
量化解读： 存量 Call 重｜ATM IV 64.5%｜历史 Rank 75%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,213 股

📆 12-04 Forward Structure
存量OI: C 32.7k / P 24.6k，今日变化ΔOI: C +8.8k / P +3.5k，平值价格ATM: C $6.65 / P $7.20 ｜ ATM IV 61.2%，净 delta 敞口 109k shares
Top ΔOI: C 180 +4,955 ｜ P 147 +1,050 ｜ C 167 +620
仓位参考: Max Pain 160 ｜ Call Wall 175（+8.0%，弱）（OI 1.6k） ｜ Put Wall 155（-4.4%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 61.2%｜历史 Rank 75%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 109,178 股

12-11（MEDIUM △）Top ΔOI: 175C +325 ｜ 162C +260
12-11（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 175（+8.0%，弱）（OI 1.2k） ｜ Put Wall 150（-7.5%，弱）（OI 2.0k）

📆 12-18 Forward Structure
存量OI: C 265.7k / P 262.1k，今日变化ΔOI: C +1.4k / P +3.9k，平值价格ATM: C $9.65 / P $10.05 ｜ ATM IV 58.5%，净 delta 敞口 49k shares
Top ΔOI: P 115 +1,619
仓位参考: Max Pain 140 ｜ Call Wall 165（+1.8%，弱）（OI 14.2k） ｜ Put Wall 160（-1.3%，弱）（OI 18.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.5%｜历史 Rank 75%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 49,188 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/PLTR_morning.json