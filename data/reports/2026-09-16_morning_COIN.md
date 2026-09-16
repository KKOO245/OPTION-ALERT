# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.91
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 09-18 ATM IV 78.8% vs 09-25 66.9%（差 +11.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 160P ΔOI +3,405（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 172.11 → 今开 172.55（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 173.97 ｜ 低 166.29

Options: P/C成交量 1.60 | OI比 0.56 | ATM IV 78.8% | Skew -1.8pp | Term 0.81 | ExpMove ±5.0%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.56）+ 当日成交偏 Put（P/C量 1.60）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.60×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±5.0% ｜ 09-25（9D）±8.1% ｜ 10-02（16D）±11.1% ｜ 10-09（23D）±13.0%
   ⇒ IV–VIX Spread: +62.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,522,023 | GEX Change vs 上次快照 -11,189,747 | Flip: Primary Flip: 168.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 545 / LOW 166 / INVALID 263
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 168.65（全链重定价，覆盖 100%）
Put Wall 160（弱结构｜现价高于该位 4.7%）
最近结构参考: Flip 169（现价低于该位 0.6%）
量化视角： 负 Gamma（252万，无历史分位）｜由正转负（1119万）｜现价位于 Flip 下方 0.63%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（Put Wall，弱结构）；上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 169（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 160.0P — Vol 33,520 | 最新价 $0.98 | OI 13793→17198 (ΔOI +3405张) | ΔOI/Volume 10.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3405张（+24.7% vs前日OI），连续性待观察（方向未知）
09-18 150.0P — Vol 10,930 | 最新价 $0.27 | OI 5876→8460 (ΔOI +2584张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2584张（+44.0% vs前日OI），连续性待观察（方向未知）
09-18 190.0C — Vol 10,865 | 最新价 $0.70 | OI 7973→9897 (ΔOI +1924张) | ΔOI/Volume 17.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1924张（+24.1% vs前日OI），连续性待观察（方向未知）
09-18 165.0P — Vol 11,483 | 最新价 $2.00 | OI 2935→4715 (ΔOI +1780张) | ΔOI/Volume 15.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1780张（+60.6% vs前日OI），连续性待观察（方向未知）
09-18 175.0P — Vol 9,107 | 最新价 $6.56 | OI 4237→5908 (ΔOI +1671张) | ΔOI/Volume 18.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1671张（+39.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,364 张（Put 9,440 / Call 1,924），跨 1 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +5.4k / P +10.5k ｜ Activity HIGH ｜ 2D
09-25  C +3.4k / P +1.8k ｜ Activity HIGH ｜ 9D
10-02  C +0.7k / P +0.8k ｜ Activity HIGH ｜ 16D
10-09  C +69 / P +0.5k ｜ Activity MEDIUM △ ｜ 23D

📆 09-18 Forward Structure
存量OI: C 226.2k / P 127.7k，今日变化ΔOI: C +5.4k / P +10.5k，平值价格ATM: C $4.10 / P $4.25 ｜ ATM IV 78.8%，净 delta 敞口 114k shares
Top ΔOI: P 160 +3,405 ｜ P 150 +2,584
仓位参考: Max Pain 175 ｜ Call Wall 182.5（+8.9%，弱）（OI 10.1k） ｜ Put Wall 160（-4.5%）（OI 17.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.8%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 114,082 股

📆 09-25 Forward Structure
存量OI: C 19.8k / P 15.7k，今日变化ΔOI: C +3.4k / P +1.8k，平值价格ATM: C $7.00 / P $6.60 ｜ ATM IV 66.9%，净 delta 敞口 28k shares
Top ΔOI: P 150 +925 ｜ C 190 +519 ｜ C 180 +487
仓位参考: Max Pain 175 ｜ Call Wall 180（+7.4%，弱）（OI 1.2k） ｜ Put Wall 160（-4.5%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 66.9%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,247 股

📆 10-02 Forward Structure
存量OI: C 11.5k / P 16.7k，今日变化ΔOI: C +0.7k / P +0.8k，平值价格ATM: C $9.70 / P $8.85 ｜ ATM IV 64.6%，净 delta 敞口 7k shares
Top ΔOI: P 150 +201
仓位参考: Max Pain 188 ｜ Call Wall 180（+7.4%，弱）（OI 0.6k） ｜ Put Wall 172.5（+2.9%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 64.6%｜历史 Rank 57%（近端代理）｜净 delta 敞口 正 6,978 股

10-09（MEDIUM △）Top ΔOI: 160P +83 ｜ 155P +70
10-09（MEDIUM △）仓位参考: Max Pain 182 ｜ Call Wall 172.5（+2.9%，弱）（OI 69） ｜ Put Wall 160（-4.5%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 78.8% vs 09-25 66.9%（差 +11.9pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/COIN_morning.json