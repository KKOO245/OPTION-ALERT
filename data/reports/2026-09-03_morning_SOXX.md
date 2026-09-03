# 期权晨报 2026-09-03（快照 10:16 ET）

📊 市场环境

SPY $769.39 ｜ QQQ $712.30
VIX 15.00 ↓1.3%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-04 475P ΔOI +1,050（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 501.44 → 今开 496.34（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 497.00 ｜ 低 489.21

Options: P/C成交量 7.22 | OI比 0.89 | ATM IV 40.0% | Skew -5.2pp | Term 0.92 | ExpMove ±2.6%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -5.2pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 7.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 7.22×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（1D）±2.6% ｜ 09-11（8D）±4.3% ｜ 09-18（15D）±5.9% ｜ 09-25（22D）±9.4%
   ⇒ IV–VIX Spread: +25.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -34,583,553 | GEX Change vs 上次快照 -10,237,686 | Flip: Primary Flip: 512.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 452 / LOW 364 / INVALID 746
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 512.84（全链重定价，覆盖 88%）
Put Wall 450（弱结构｜现价高于该位 9.7%）
最近结构参考: Flip 513（现价低于该位 3.7%）
量化视角： 负 Gamma（3458万，无历史分位）｜负 Gamma 加深（1024万）｜现价位于 Flip 下方 3.70%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 450（Put Wall，弱结构）；上方 510（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 513（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 445.0P — Vol 6（Yahoo补） | 最新价 $1.90 | OI 1421→5649 (ΔOI +4228张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4228张（+297.5% vs前日OI），连续性待观察（方向未知）
09-18 450.0P — Vol 15（Yahoo补） | 最新价 $2.24 | OI 10573→12813 (ΔOI +2240张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2240张（+21.2% vs前日OI），连续性待观察（方向未知）
09-04 475.0P — Vol 2 | 最新价 $0.75 | OI 2393→3443 (ΔOI +1050张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1050张（+43.9% vs前日OI），连续性待观察（方向未知）
09-04 467.5P — Vol 5（Yahoo补） | 最新价 $0.27 | OI 23→876 (ΔOI +853张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增853张（+3708.7% vs前日OI），连续性待观察（方向未知）
09-04 527.5C — Vol 791（Yahoo补） | 最新价 $0.25 | OI 30→800 (ΔOI +770张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增770张（+2566.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,141 张（Put 8,371 / Call 770），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.9k / P +1.9k ｜ Activity MEDIUM △ ｜ 1D
09-11  C +0.4k / P +0.3k ｜ Activity LOW ｜ 8D
09-18  C -0.4k / P +4.5k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.1k / P -0.2k ｜ Activity LOW ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 29.8k / P 26.4k
今日变化ΔOI: C +0.9k / P +1.9k
平值价格ATM:  C 9.60 / P 3.50
隐含波动率 ATM IV:  40.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 475 ｜ +1,050 ｜ $0.75 ｜ 名义 $78.8k* ｜ -3.8%
P 467 ｜ +853 ｜ $0.27 ｜ 名义 $23.0k* ｜ -5.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：475（-3.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.0%｜历史 Rank 70%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,941 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 445P +4,228 ｜ 450P +2,240

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 40.0% vs 09-11 34.2%（差 +5.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=10 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=10）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/SOXX_morning.json