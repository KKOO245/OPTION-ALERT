# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.82
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 155C ΔOI -12,286（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 150.88 → 今开 153.76（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 156.87 ｜ 低 152.63

Options: P/C成交量 0.47 | OI比 0.85 | ATM IV 61.0% | Skew 1.7pp | Term 0.82 | ExpMove ±2.8%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.8% ｜ 09-25（8D）±6.3% ｜ 10-02（15D）±8.3% ｜ 10-09（22D）±10.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 178,980,730 | GEX Change vs 上次快照 29,246,753 | Flip: Primary Flip: 147.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 634 / LOW 119 / INVALID 303
结构观察区: Primary Flip 147.38（全链重定价，覆盖 98%）
Call Wall 160（弱结构｜现价低于该位 3.7%）
最近结构参考: Call Wall 160（现价低于该位 3.7%）
量化视角： 正 Gamma（1.79亿，无历史分位）｜正 Gamma 增强（+2925万）｜现价位于 Flip 上方 4.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 146（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 167.5C — Vol 20,799 | 最新价 $0.10 | OI 1938→17923 (ΔOI +15985张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15985张（+824.8% vs前日OI），连续性待观察（方向未知）
09-18 144.0P — Vol 28,216 | 最新价 $0.78 | OI 5686→19362 (ΔOI +13676张) | ΔOI/Volume 48.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13676张（+240.5% vs前日OI），连续性待观察（方向未知）
10-16 200.0C — Vol 20,791 | 最新价 $0.48 | OI 38355→46328 (ΔOI +7973张) | ΔOI/Volume 38.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7973张（+20.8% vs前日OI），连续性待观察（方向未知）
09-25 140.0P — Vol 13,760 | 最新价 $1.56 | OI 7508→15193 (ΔOI +7685张) | ΔOI/Volume 55.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7685张（+102.4% vs前日OI），连续性待观察（方向未知）
09-18 152.5C — Vol 48,379 | 最新价 $2.21 | OI 18976→25423 (ΔOI +6447张) | ΔOI/Volume 13.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6447张（+34.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 51,766 张（Put 21,361 / Call 30,405），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.7k / P +33.4k ｜ Activity HIGH ｜ 1D
09-25  C +8.3k / P +23.9k ｜ Activity HIGH ｜ 8D
10-02  C +2.9k / P +2.9k ｜ Activity HIGH ｜ 15D
10-09  C +2.3k / P +1.3k ｜ Activity HIGH ｜ 22D

📆 09-18 Forward Structure
存量OI: C 724.9k / P 615.9k，今日变化ΔOI: C +2.7k / P +33.4k，平值价格ATM: C $1.94 / P $2.43 ｜ ATM IV 61.0%，净 delta 敞口 -1.4M shares
Top ΔOI: C 167 +15,985 ｜ P 144 +13,676 ｜ C 155 -12,286
仓位参考: Max Pain 146 ｜ Call Wall 160（+3.8%，弱）（OI 62.2k） ｜ Put Wall 150（-2.7%）（OI 49.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.0%｜历史 Rank 50%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,365,076 股

📆 09-25 Forward Structure
存量OI: C 89.4k / P 119.1k，今日变化ΔOI: C +8.3k / P +23.9k，平值价格ATM: C $4.68 / P $5.06 ｜ ATM IV 52.7%，净 delta 敞口 -269k shares
Top ΔOI: P 140 +7,685 ｜ P 138 +2,961
仓位参考: Max Pain 147 ｜ Call Wall 160（+3.8%，弱）（OI 8.3k） ｜ Put Wall 140（-9.2%，弱）（OI 15.2k）
量化解读： 存量 Put 重｜ATM IV 52.7%｜历史 Rank 50%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 269,165 股

📆 10-02 Forward Structure
存量OI: C 35.1k / P 46.8k，今日变化ΔOI: C +2.9k / P +2.9k，平值价格ATM: C $6.26 / P $6.60 ｜ ATM IV 51.1%，净 delta 敞口 -51k shares
Top ΔOI: C 165 +1,340 ｜ P 148 +701 ｜ P 150 +515
仓位参考: Max Pain 147 ｜ Call Wall 165（+7.1%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 51.1%｜历史 Rank 50%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 50,572 股

📆 10-09 Forward Structure
存量OI: C 16.7k / P 17.7k，今日变化ΔOI: C +2.3k / P +1.3k，平值价格ATM: C $7.60 / P $8.12 ｜ ATM IV 50.4%，净 delta 敞口 50k shares
Top ΔOI: C 170 +718 ｜ C 149 +520 ｜ P 148 +509
仓位参考: Max Pain 148 ｜ Call Wall 165（+7.1%，弱）（OI 1.8k） ｜ Put Wall 140（-9.2%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.4%｜历史 Rank 50%（近端代理）｜净 delta 敞口 正 50,317 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 61.0% vs 09-25 52.7%（差 +8.3pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SPCX_morning.json