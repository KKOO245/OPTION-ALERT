# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $758.10 ｜ QQQ $704.54
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.71 → 今开 15.53（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 15.84 ｜ 低 15.30

Options: P/C成交量 0.35 | OI比 0.54 | ATM IV 81.5% | Skew -2.1pp | Term 0.92 | ExpMove ±6.2%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±6.2% ｜ 09-25（10D）±10.8% ｜ 10-02（17D）±13.7% ｜ 10-09（24D）±14.7%
   ⇒ IV–VIX Spread: +63.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,451,118 | GEX Change vs 上次快照 -2,609,852 | Flip: Primary Flip: 16.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 240 / LOW 84 / INVALID 144
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.26（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 2.3%）
最近结构参考: Put Wall 15（现价高于该位 2.3%）
量化视角： 负 Gamma（645万，无历史分位）｜负 Gamma 加深（261万）｜现价位于 Flip 下方 5.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 17.0C — Vol 1,905 | 最新价 $0.17 | OI 1747→2820 (ΔOI +1073张) | ΔOI/Volume 56.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1073张（+61.4% vs前日OI），连续性待观察（方向未知）
09-25 17.0P — Vol 960 | 最新价 $1.67 | OI 782→1711 (ΔOI +929张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增929张（+118.8% vs前日OI），连续性待观察（方向未知）
10-02 20.0C — Vol 892 | 最新价 $0.15 | OI 283→1011 (ΔOI +728张) | ΔOI/Volume 81.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增728张（+257.2% vs前日OI），连续性待观察（方向未知）
09-18 16.5C — Vol 1,195 | 最新价 $0.27 | OI 505→1176 (ΔOI +671张) | ΔOI/Volume 56.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增671张（+132.9% vs前日OI），连续性待观察（方向未知）
10-02 21.0C — Vol 1,207 | 最新价 $0.10 | OI 100→754 (ΔOI +654张) | ΔOI/Volume 54.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增654张（+654.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,055 张（Put 929 / Call 3,126），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -0.6k / P -0.5k ｜ Activity HIGH ｜ 3D
09-25  C +1.9k / P +1.7k ｜ Activity HIGH ｜ 10D
10-02  C +1.6k / P +43 ｜ Activity HIGH ｜ 17D
10-09  C +0.4k / P +86 ｜ Activity MEDIUM △ ｜ 24D

📆 09-18 Forward Structure
存量OI: C 122.2k / P 66.2k，今日变化ΔOI: C -0.6k / P -0.5k，平值价格ATM: C $0.40 / P $0.56 ｜ ATM IV 81.5%，净 delta 敞口 130k shares
Top ΔOI: P 17 -935
仓位参考: Max Pain 19 ｜ Put Wall 15（-2.3%，弱）（OI 9.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.5%｜历史 Rank 4%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 130,013 股

📆 09-25 Forward Structure
存量OI: C 13.4k / P 6.2k，今日变化ΔOI: C +1.9k / P +1.7k，平值价格ATM: C $0.79 / P $0.87 ｜ ATM IV 78.9%，净 delta 敞口 -63k shares
Top ΔOI: P 17 +929 ｜ P 14 +460
仓位参考: Max Pain 17 ｜ Call Wall 16.5（+7.5%，弱）（OI 1.1k） ｜ Put Wall 15（-2.3%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 78.9%｜历史 Rank 4%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 63,024 股

📆 10-02 Forward Structure
存量OI: C 9.4k / P 3.3k，今日变化ΔOI: C +1.6k / P +43，平值价格ATM: C $1.02 / P $1.08 ｜ ATM IV 76.3%，净 delta 敞口 17k shares
Top ΔOI: P 16 +63
仓位参考: Max Pain 18 ｜ Put Wall 16（+4.2%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 76.3%｜历史 Rank 4%（近端代理）｜净 delta 敞口 正 16,844 股

10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+4.2%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/USAR_morning.json