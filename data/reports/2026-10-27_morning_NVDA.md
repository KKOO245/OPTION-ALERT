# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $766.09 ｜ QQQ $715.13
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 222C ΔOI +7,074（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 216.00 → 今开 218.30（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 218.49 ｜ 低 215.53

Options: P/C成交量 0.60 | OI比 0.96 | ATM IV 39.5% | Skew 2.7pp | Term 1.03 | ExpMove ±1.9%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 1.03）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-28（1D）±1.9% ｜ 10-30（3D）±3.0% ｜ 11-02（6D）±3.5% ｜ 11-04（8D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 215,468,477 | GEX Change vs 上次快照 32,918,291 | Flip: Primary Flip: 210.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 740 / LOW 170 / INVALID 550
结构观察区: Primary Flip 210.31（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价高于该位 8.1%） | Call Wall 230（现价低于该位 6.0%）
最近结构参考: Flip 210（现价高于该位 2.8%）
量化视角： 正 Gamma（2.15亿，无历史分位）｜正 Gamma 增强（+3292万）｜现价位于 Flip 上方 2.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 215（MaxPain，仅结算参考）；上方 230（Call Wall）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 227.5C — Vol 25,194 | 最新价 $0.34 | OI 8990→22148 (ΔOI +13158张) | ΔOI/Volume 52.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13158张（+146.4% vs前日OI），连续性待观察（方向未知）
10-30 230.0C — Vol 27,736 | 最新价 $0.19 | OI 24444→36754 (ΔOI +12310张) | ΔOI/Volume 44.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12310张（+50.4% vs前日OI），连续性待观察（方向未知）
10-30 265.0C — Vol 12,662 | 最新价 $0.01 | OI 3097→12735 (ΔOI +9638张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9638张（+311.2% vs前日OI），连续性待观察（方向未知）
10-30 225.0C — Vol 35,927 | 最新价 $0.63 | OI 50890→58558 (ΔOI +7668张) | ΔOI/Volume 21.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7668张（+15.1% vs前日OI），连续性待观察（方向未知）
10-28 222.5C — Vol 20,519 | 最新价 $0.42 | OI 3886→10960 (ΔOI +7074张) | ΔOI/Volume 34.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7074张（+182.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 49,848 张（Put 0 / Call 49,848），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +34.2k / P +27.4k ｜ Activity HIGH ｜ 1D
10-30  C +77.3k / P +16.0k ｜ Activity HIGH ｜ 3D
11-02  C +4.4k / P +6.3k ｜ Activity HIGH ｜ 6D
11-04  C +2.4k / P +1.5k ｜ Activity HIGH ｜ 8D

📆 10-28 Forward Structure
存量OI: C 101.6k / P 97.8k，今日变化ΔOI: C +34.2k / P +27.4k，平值价格ATM: C $2.69 / P $1.42 ｜ ATM IV 39.5%，净 delta 敞口 61k shares
Top ΔOI: C 222 +7,074 ｜ C 225 +6,441 ｜ C 220 +5,910
仓位参考: Max Pain 215 ｜ Call Wall 225（+4.1%，弱）（OI 11.0k） ｜ Put Wall 200（-7.5%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜ATM IV 39.5%｜历史 Rank 38%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,832 股

📆 10-30 Forward Structure
存量OI: C 471.8k / P 298.4k，今日变化ΔOI: C +77.3k / P +16.0k，平值价格ATM: C $3.96 / P $2.60 ｜ ATM IV 39.7%，净 delta 敞口 623k shares
Top ΔOI: C 227 +13,158 ｜ C 230 +12,310
仓位参考: Max Pain 215 ｜ Call Wall 225（+4.1%，弱）（OI 58.6k） ｜ Put Wall 210（-2.8%，弱）（OI 21.4k）
量化解读： 存量 Call 重｜ATM IV 39.7%｜历史 Rank 38%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 623,063 股

📆 11-02 Forward Structure
存量OI: C 14.2k / P 12.4k，今日变化ΔOI: C +4.4k / P +6.3k，平值价格ATM: C $4.47 / P $3.05 ｜ ATM IV 32.8%，净 delta 敞口 20k shares
Top ΔOI: P 210 +1,044
仓位参考: Max Pain 212 ｜ Call Wall 230（+6.4%，弱）（OI 2.7k） ｜ Put Wall 200（-7.5%）（OI 2.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.8%｜历史 Rank 38%（近端代理）｜IV/RV 1.15×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 20,224 股

📆 11-04 Forward Structure
存量OI: C 8.5k / P 6.0k，今日变化ΔOI: C +2.4k / P +1.5k，平值价格ATM: C $5.33 / P $3.92 ｜ ATM IV 35.2%，净 delta 敞口 220 shares
Top ΔOI: C 225 +507 ｜ P 205 +475
仓位参考: Max Pain 215 ｜ Call Wall 225（+4.1%）（OI 3.0k） ｜ Put Wall 205（-5.2%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 38%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 220 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/NVDA_morning.json