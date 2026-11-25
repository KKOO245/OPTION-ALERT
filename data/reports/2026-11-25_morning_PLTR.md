# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $611.06
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 162C ΔOI -1,010（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 161.18 → 今开 154.22（-4.3%） | 较昨收变动（含盘初走势） ｜ 今日高 157.39 ｜ 低 151.51

Options: P/C成交量 0.73 | OI比 0.56 | ATM IV 68.8% | Skew 8.5pp | Term 0.88 | ExpMove ±4.2%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 8.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±4.2% ｜ 12-04（9D）±9.3% ｜ 12-11（16D）±12.3% ｜ 12-18（23D）±12.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,506,025 | GEX Change vs 上次快照 -10,698,614 | Flip: Primary Flip: 151.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 498 / LOW 176 / INVALID 240
结构观察区: Primary Flip 151.56（全链重定价，覆盖 99%）
Call Wall 165（弱结构｜现价低于该位 4.8%）
最近结构参考: Flip 152（现价高于该位 3.6%）
量化视角： 正 Gamma（1951万，无历史分位）｜正 Gamma 减弱（1070万）｜现价位于 Flip 上方 3.59%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 152（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 175.0C — Vol 3,267 | 最新价 $0.19 | OI 10695→11675 (ΔOI +980张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增980张（+9.2% vs前日OI），连续性待观察（方向未知）
12-04 180.0C — Vol 4,564 | 最新价 $0.84 | OI 5998→6961 (ΔOI +963张) | ΔOI/Volume 21.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增963张（+16.1% vs前日OI），连续性待观察（方向未知）
11-27 167.5C — Vol 4,340 | 最新价 $1.19 | OI 3967→4845 (ΔOI +878张) | ΔOI/Volume 20.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增878张（+22.1% vs前日OI），连续性待观察（方向未知）
12-18 120.0P — Vol 1,119 | 最新价 $0.85 | OI 11531→12387 (ΔOI +856张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增856张（+7.4% vs前日OI），连续性待观察（方向未知）
11-27 165.0P — Vol 1,747 | 最新价 $5.75 | OI 947→1663 (ΔOI +716张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增716张（+75.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,393 张（Put 1,572 / Call 2,821），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +2.4k / P +4.2k ｜ Activity HIGH ｜ 2D
12-04  C +2.6k / P +1.8k ｜ Activity MEDIUM △ ｜ 9D
12-11  C +1.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 16D
12-18  C +1.2k / P +1.2k ｜ Activity HIGH ｜ 23D

📆 11-27 Forward Structure
存量OI: C 107.2k / P 60.2k，今日变化ΔOI: C +2.4k / P +4.2k，平值价格ATM: C $2.90 / P $3.71 ｜ ATM IV 68.8%，净 delta 敞口 -156k shares
Top ΔOI: C 162 -1,010 ｜ C 167 +878
仓位参考: Max Pain 152 ｜ Call Wall 165（+5.1%，弱）（OI 8.8k） ｜ Put Wall 150（-4.5%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 68.8%｜历史 Rank 78%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 156,131 股

12-04（MEDIUM △）Top ΔOI: 150P +294
12-04（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+1.9%，弱）（OI 1.7k） ｜ Put Wall 155（-1.3%，弱）（OI 3.1k）

12-11（MEDIUM △）Top ΔOI: 180C +450 ｜ 148C +298
12-11（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 170（+8.3%，弱）（OI 1.1k） ｜ Put Wall 150（-4.5%，弱）（OI 2.0k）

📆 12-18 Forward Structure
存量OI: C 266.9k / P 263.3k，今日变化ΔOI: C +1.2k / P +1.2k，平值价格ATM: C $9.30 / P $10.50 ｜ ATM IV 62.2%，净 delta 敞口 11k shares
Top ΔOI: P 120 +856 ｜ P 125 -745 ｜ C 162 +673
仓位参考: Max Pain 140 ｜ Call Wall 165（+5.1%，弱）（OI 14.3k） ｜ Put Wall 160（+1.9%，弱）（OI 18.9k）
量化解读： 存量两侧均衡｜ATM IV 62.2%｜历史 Rank 78%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 11,327 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/PLTR_morning.json