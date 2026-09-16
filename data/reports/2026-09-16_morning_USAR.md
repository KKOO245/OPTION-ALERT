# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.93
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 16C ΔOI +386（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.40 → 今开 15.60（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 15.69 ｜ 低 15.18

Options: P/C成交量 0.23 | OI比 0.53 | ATM IV 87.1% | Skew -2.0pp | Term 0.86 | ExpMove ±6.0%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±6.0% ｜ 09-25（9D）±9.7% ｜ 10-02（16D）±12.8% ｜ 10-09（23D）±15.4%
   ⇒ IV–VIX Spread: +70.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,066,673 | GEX Change vs 上次快照 -1,470,099 | Flip: Primary Flip: 16.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 239 / LOW 87 / INVALID 142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.11（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 1.9%）
最近结构参考: Put Wall 15（现价高于该位 1.9%）
量化视角： 负 Gamma（707万，无历史分位）｜负 Gamma 加深（147万）｜现价位于 Flip 下方 5.11%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 16.5P — Vol 935 | 最新价 $1.44 | OI 298→1133 (ΔOI +835张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增835张（+280.2% vs前日OI），连续性待观察（方向未知）
09-25 18.0C — Vol 874 | 最新价 $0.13 | OI 820→1608 (ΔOI +788张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增788张（+96.1% vs前日OI），连续性待观察（方向未知）
09-25 17.0C — Vol 736 | 最新价 $0.27 | OI 618→1297 (ΔOI +679张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增679张（+109.9% vs前日OI），连续性待观察（方向未知）
09-25 18.5C — Vol 879 | 最新价 $0.11 | OI 224→888 (ΔOI +664张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增664张（+296.4% vs前日OI），连续性待观察（方向未知）
09-18 16.0C — Vol 1,581 | 最新价 $0.24 | OI 1536→1922 (ΔOI +386张) | ΔOI/Volume 24.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增386张（+25.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,352 张（Put 835 / Call 2,517），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -60 / P -1.9k ｜ Activity MEDIUM △ ｜ 2D
09-25  C +2.3k / P +1.2k ｜ Activity MEDIUM △ ｜ 9D
10-02  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
10-09  C +21 / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 09-18 Forward Structure
存量OI: C 122.1k / P 64.3k，今日变化ΔOI: C -60 / P -1.9k，平值价格ATM: C $0.32 / P $0.59 ｜ ATM IV 87.1%，净 delta 敞口 189k shares
Top ΔOI: P 16 -927 ｜ P 17 -430 ｜ C 16 +386
仓位参考: Max Pain 19 ｜ Put Wall 15（-1.9%，弱）（OI 9.5k）
量化解读： 存量 Call 重｜ATM IV 87.1%｜历史 Rank 8%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 189,488 股

09-25（MEDIUM △）Top ΔOI: 16P +835
09-25（MEDIUM △）仓位参考: Max Pain 17 ｜ Call Wall 16.5（+7.9%，弱）（OI 1.1k） ｜ Put Wall 16.5（+7.9%，弱）（OI 1.1k）

10-02（MEDIUM △）Top ΔOI: 16P +66 ｜ 16C +60
10-02（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+4.6%，弱）（OI 0.6k）

10-09（MEDIUM △）Top ΔOI: 14P +55 ｜ 15P +34
10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+4.6%）（OI 1.2k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 87.1% vs 09-25 77.3%（差 +9.8pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/USAR_morning.json