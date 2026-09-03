# 期权晨报 2026-09-03（快照 12:15 ET）

📊 市场环境

SPY $773.17 ｜ QQQ $717.23
VIX 14.69 ↓3.4%（5D +1.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-04 475P ΔOI +1,050（距现价 -5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 501.44 → 今开 496.34（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 501.11 ｜ 低 489.21

Options: P/C成交量 0.48 | OI比 0.89 | ATM IV 38.0% | Skew 3.4pp | Term 0.95 | ExpMove ±1.8%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 3.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（1D）±1.8% ｜ 09-11（8D）±3.7% ｜ 09-18（15D）±5.5% ｜ 09-25（22D）±7.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,645,168 | GEX Change vs 上次快照 -4,299,301 | Flip: Primary Flip: 514.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 480 / LOW 356 / INVALID 726
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 514.43（全链重定价，覆盖 92%）
Put Wall 450（弱结构｜现价高于该位 11.1%）
最近结构参考: Flip 514（现价低于该位 2.8%）
量化视角： 负 Gamma（2865万，无历史分位）｜负 Gamma 加深（430万）｜现价位于 Flip 下方 2.83%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 450（Put Wall，弱结构）；上方 510（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 514（全链重定价，覆盖 92%）。
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

09-04  C +0.9k / P +1.9k ｜ Activity HIGH ｜ 1D
09-11  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 8D
09-18  C -0.4k / P +4.5k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.1k / P -0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 29.8k / P 26.4k
今日变化ΔOI: C +0.9k / P +1.9k
平值价格ATM:  C 3.50 / P 5.55
隐含波动率 ATM IV:  38.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 35k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 550 ｜ -1,207 ｜ $0.03 ｜ 名义 $-3.6k* ｜ +10.0%
P 475 ｜ +1,050 ｜ $0.25 ｜ 名义 $26.2k* ｜ -5.0%
P 467 ｜ +853 ｜ $0.25 ｜ 名义 $21.3k* ｜ -6.5%
结构参考：475（-5.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.0%｜历史 Rank 65%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,541 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（MEDIUM △）Top ΔOI: 455P +639 ｜ 490P -312

09-18（MEDIUM △）Top ΔOI: 445P +4,228 ｜ 450P +2,240

09-25（MEDIUM △）Top ΔOI: 490P -136

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 38.0% vs 09-11 31.9%（差 +6.0pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/SOXX_morning.json