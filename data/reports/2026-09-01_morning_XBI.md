# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $762.30 ｜ QQQ $708.36
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.2（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-04 155P ΔOI +268（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-11 155P ΔOI +1,659 占该期限总 OI 16.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 162.50 → 今开 161.75（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 163.24 ｜ 低 161.16

Options: P/C成交量 1.59 | OI比 1.92 | ATM IV 39.4% | Skew -7.4pp | Term 0.80 | ExpMove ±2.7%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.4pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.59×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.92×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±2.7% ｜ 09-11（10D）±3.8% ｜ 09-18（17D）±5.6% ｜ 09-25（24D）±10.8%
   ⇒ IV–VIX Spread: +23.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,058,373 | GEX Change vs 上次快照 -6,553,116 | Flip: Primary Flip: 166.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 406 / LOW 116 / INVALID 350
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.18（全链重定价，覆盖 98%）
Put Wall 155（弱结构｜现价高于该位 4.1%） | Call Wall 155（弱结构｜现价高于该位 4.1%）
最近结构参考: Flip 166（现价低于该位 2.9%）
量化视角： 负 Gamma（1606万，无历史分位）｜负 Gamma 加深（655万）｜现价位于 Flip 下方 2.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（Put Wall，弱结构）；上方 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 155.0P — Vol 10（Yahoo补） | 最新价 $1.03 | OI 49→1708 (ΔOI +1659张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1659张（+3385.7% vs前日OI），连续性待观察（方向未知）
09-18 159.0P — Vol 1,257（Yahoo补） | 最新价 $2.68 | OI 84→1324 (ΔOI +1240张) | ΔOI/Volume 98.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1240张（+1476.2% vs前日OI），连续性待观察（方向未知）
09-18 154.0P — Vol 337（Yahoo补） | 最新价 $1.80 | OI 217→510 (ΔOI +293张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增293张（+135.0% vs前日OI），连续性待观察（方向未知）
09-04 155.0P — Vol 321（Yahoo补） | 最新价 $0.38 | OI 309→577 (ΔOI +268张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增268张（+86.7% vs前日OI），连续性待观察（方向未知）
09-04 170.0C — Vol 262（Yahoo补） | 最新价 $0.32 | OI 136→365 (ΔOI +229张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增229张（+168.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,689 张（Put 3,460 / Call 229），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.6k / P +0.4k ｜ Activity MEDIUM △ ｜ 3D
09-11  C +0.2k / P +1.8k ｜ Activity HIGH ｜ 10D
09-18  C -0.8k / P +0.2k ｜ Activity MEDIUM △ ｜ 17D
09-25  C +33 / P +58 ｜ Activity MEDIUM △ ｜ 24D

   Top ΔOI: 155P +268 ｜ 170C +229

📆 09-11 Forward Structure
存量OI:      C 1.5k / P 8.3k
今日变化ΔOI: C +0.2k / P +1.8k
平值价格ATM:  C 3.18 / P 2.99
隐含波动率 ATM IV:  30.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -30k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 155 ｜ +1,659 ｜ $1.03 ｜ 名义 $170.9k* ｜ -3.9%
C 165 ｜ +94 ｜ $1.99 ｜ 名义 $18.7k* ｜ +2.3%
C 169 ｜ +81 ｜ $0.98 ｜ 名义 $7.9k* ｜ +4.8%
结构参考：165（+2.3%） / 155（-3.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 30.5%｜历史 Rank 82%（近端代理）｜净 delta 敞口 负 30,378 股（方向不可观测）——方向不可观测，观察点，非方向信号

   Top ΔOI: 159P +1,240 ｜ 155P -859

   Top ΔOI: 160P +31 ｜ 172C +13

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 39.4% vs 09-11 30.5%（差 +8.9pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/XBI_morning.json