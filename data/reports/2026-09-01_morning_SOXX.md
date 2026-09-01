# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $762.01 ｜ QQQ $707.64
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
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
🟡 **单日价格波动**: -2.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 475P ΔOI +2,270（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 511.04 → 今开 501.30（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 501.64 ｜ 低 495.11

Options: P/C成交量 0.79 | OI比 0.90 | ATM IV 41.4% | Skew 3.9pp | Term 0.88 | ExpMove ±4.7%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（3D）±4.7% ｜ 09-11（10D）±9.8% ｜ 09-18（17D）±7.4% ｜ 09-25（24D）±9.4%
   ⇒ IV–VIX Spread: +25.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -31,617,152 | GEX Change vs 上次快照 -16,076,553 | Flip: Primary Flip: 520.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 518 / LOW 303 / INVALID 711
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 520.45（全链重定价，覆盖 96%）
Put Wall 500（弱结构｜现价低于该位 0.7%）
最近结构参考: Put Wall 500（现价低于该位 0.7%）
量化视角： 负 Gamma（3162万，无历史分位）｜负 Gamma 加深（1608万）｜现价位于 Flip 下方 4.63%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 520（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 450.0P — Vol 1 | 最新价 $2.20 | OI 7157→10579 (ΔOI +3422张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3422张（+47.8% vs前日OI），连续性待观察（方向未知）
09-11 530.0C — Vol 7（Yahoo补） | 最新价 $4.40 | OI 280→3258 (ΔOI +2978张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2978张（+1063.6% vs前日OI），连续性待观察（方向未知）
10-02 470.0P — Vol 47（Yahoo补） | 最新价 $7.22 | OI 737→3121 (ΔOI +2384张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2384张（+323.5% vs前日OI），连续性待观察（方向未知）
10-02 570.0C — Vol 2,508（Yahoo补） | 最新价 $3.70 | OI 163→2489 (ΔOI +2326张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2326张（+1427.0% vs前日OI），连续性待观察（方向未知）
09-04 475.0P — Vol 1 | 最新价 $0.60 | OI 87→2357 (ΔOI +2270张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2270张（+2609.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,380 张（Put 8,076 / Call 5,304），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.7k / P +4.1k ｜ Activity MEDIUM △ ｜ 3D
09-11  C +7.2k / P +1.8k ｜ Activity HIGH ｜ 10D
09-18  C +5 / P +2.5k ｜ Activity MEDIUM △ ｜ 17D
09-25  C +0.9k / P +1.2k ｜ Activity HIGH ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 27.5k / P 24.6k
今日变化ΔOI: C +0.7k / P +4.1k
平值价格ATM:  C 17.25 / P 6.15
隐含波动率 ATM IV:  41.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -25k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 475 ｜ +2,270 ｜ $0.60 ｜ 名义 $136.2k* ｜ -4.3%
P 480 ｜ +893 ｜ $1.35 ｜ 名义 $120.6k* ｜ -3.3%
P 485 ｜ +687 ｜ $2.53 ｜ 名义 $173.8k* ｜ -2.3%
结构参考：475（-4.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.3%｜历史 Rank 74%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 24,999 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 10.6k / P 14.7k
今日变化ΔOI: C +7.2k / P +1.8k
平值价格ATM:  C 40.81 / P 7.58
隐含波动率 ATM IV:  35.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 36k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 530 ｜ +2,978 ｜ $4.40 ｜ 名义 $1.31M* ｜ +6.8%
C 545 ｜ +1,802 ｜ $1.80 ｜ 名义 $324.4k* ｜ +9.8%
C 535 ｜ +1,384 ｜ $3.26 ｜ 名义 $451.2k* ｜ +7.8%
结构参考：530（+6.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.0%｜历史 Rank 74%（近端代理）｜净 delta 敞口 正 36,114 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 450P +3,422 ｜ 475P -885

📆 09-25 Forward Structure
存量OI:      C 7.5k / P 5.6k
今日变化ΔOI: C +0.9k / P +1.2k
平值价格ATM:  C 35.30 / P 11.39
隐含波动率 ATM IV:  36.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -39k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 490 ｜ +1,015 ｜ $13.29 ｜ 名义 $1.35M* ｜ -1.3%
C 600 ｜ +779 ｜ $0.81 ｜ 名义 $63.1k* ｜ +20.9%
P 470 ｜ +99 ｜ $5.45 ｜ 名义 $54.0k* ｜ -5.3%
结构参考：600（+20.9%） / 490（-1.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.1%｜历史 Rank 74%（近端代理）｜净 delta 敞口 负 38,859 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 41.3% vs 09-11 35.0%（差 +6.4pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/SOXX_morning.json