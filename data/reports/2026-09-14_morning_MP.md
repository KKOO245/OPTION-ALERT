# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.11
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 49P ΔOI +286（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 50.51 → 今开 49.77（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 50.62 ｜ 低 49.53

Options: P/C成交量 0.70 | OI比 0.83 | ATM IV 57.9% | Skew -8.0pp | Term 1.05 | ExpMove ±6.5%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -8.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±6.5% ｜ 09-25（11D）±10.0% ｜ 10-02（18D）±12.9% ｜ 10-09（25D）±13.2%
   ⇒ IV–VIX Spread: +40.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,940,763 | GEX Change vs 上次快照 -2,352,008 | Flip: Primary Flip: 54.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 259 / LOW 41 / INVALID 118
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.36（全链重定价，覆盖 98%）
Put Wall 55（弱结构｜现价低于该位 9.0%）
最近结构参考: Flip 54（现价低于该位 7.9%）
量化视角： 负 Gamma（594万，无历史分位）｜负 Gamma 加深（235万）｜现价位于 Flip 下方 7.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（Put Wall，弱结构） / 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 53.0P — Vol 375 | 最新价 $3.13 | OI 296→665 (ΔOI +369张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增369张（+124.7% vs前日OI），连续性待观察（方向未知）
09-18 49.0P — Vol 354 | 最新价 $0.90 | OI 280→566 (ΔOI +286张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增286张（+102.1% vs前日OI），连续性待观察（方向未知）
09-18 54.0P — Vol 261 | 最新价 $3.85 | OI 281→524 (ΔOI +243张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增243张（+86.5% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 1,053 | 最新价 $0.42 | OI 4579→4803 (ΔOI +224张) | ΔOI/Volume 21.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增224张（+4.9% vs前日OI），值得跟踪（方向未知）
09-18 52.0C — Vol 229 | 最新价 $1.06 | OI 128→268 (ΔOI +140张) | ΔOI/Volume 61.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+109.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,262 张（Put 898 / Call 364），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -0.2k / P +1.0k ｜ Activity HIGH ｜ 4D
09-25  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 11D
10-02  C +0.1k / P +40 ｜ Activity HIGH ｜ 18D
10-09  C +0.2k / P +61 ｜ Activity HIGH ｜ 25D

📆 09-18 Forward Structure
存量OI: C 52.6k / P 43.9k，今日变化ΔOI: C -0.2k / P +1.0k，平值价格ATM: C $1.90 / P $1.35 ｜ ATM IV 57.9%，净 delta 敞口 -35k shares
Top ΔOI: C 54 -769 ｜ P 53 +369 ｜ P 49 +286
仓位参考: Max Pain 55 ｜ Put Wall 55（+9.8%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.9%｜历史 Rank 33%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 34,652 股

09-25（MEDIUM △）Top ΔOI: 50C +54 ｜ 49P +39
09-25（MEDIUM △）仓位参考: Max Pain 54

📆 10-02 Forward Structure
存量OI: C 2.6k / P 3.1k，今日变化ΔOI: C +0.1k / P +40，平值价格ATM: C $3.84 / P $2.61 ｜ ATM IV 63.8%，净 delta 敞口 2k shares
Top ΔOI: C 55 +27 ｜ C 54 +14
仓位参考: Max Pain 58 ｜ Put Wall 50（-0.1%）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.8%｜历史 Rank 33%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,555 股

📆 10-09 Forward Structure
存量OI: C 2.4k / P 1.6k，今日变化ΔOI: C +0.2k / P +61，平值价格ATM: C $3.63 / P $3.00 ｜ ATM IV 61.1%，净 delta 敞口 5k shares
Top ΔOI: C 50 +100 ｜ C 51 +22
仓位参考: Max Pain 52 ｜ Call Wall 55（+9.8%）（OI 1.0k） ｜ Put Wall 47（-6.1%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 61.1%｜历史 Rank 33%（近端代理）｜净 delta 敞口 正 4,573 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/MP_morning.json