# 期权晨报 2026-09-04（快照 10:20 ET）

📊 市场环境

SPY $772.01 ｜ QQQ $719.74
VIX 14.05 ↓1.9%（5D -2.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 43.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 102C ΔOI +5,300（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 101.49 → 今开 98.75（-2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 99.76 ｜ 低 98.02

Options: P/C成交量 1.59 | OI比 0.98 | ATM IV 54.9% | Skew 7.7pp | Term 0.80 | ExpMove ±4.8%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 7.7pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.59×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±4.8% ｜ 09-18（14D）±6.7% ｜ 09-25（21D）±8.9% ｜ 10-02（28D）±9.6%
   ⇒ IV–VIX Spread: +40.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 11,377,285 | GEX Change vs 上次快照 -54,067,849 | Flip: Primary Flip: 98.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 478 / LOW 204 / INVALID 296
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 98.35（全链重定价，覆盖 93%）
Call Wall 100（弱结构｜现价低于该位 1.2%）
最近结构参考: Flip 98（现价高于该位 0.5%）
量化视角： 正 Gamma（1138万，无历史分位）｜正 Gamma 减弱（5407万）｜现价位于 Flip 上方 0.47%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 98（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 102.0C — Vol 359 | 最新价 $1.14 | OI 213→5513 (ΔOI +5300张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5300张（+2488.3% vs前日OI），连续性待观察（方向未知）
09-11 106.0C — Vol 454 | 最新价 $0.44 | OI 146→5226 (ΔOI +5080张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5080张（+3479.4% vs前日OI），连续性待观察（方向未知）
09-18 80.0P — Vol 6,550（Yahoo补） | 最新价 $0.08 | OI 66246→71131 (ΔOI +4885张) | ΔOI/Volume 74.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4885张（+7.4% vs前日OI），连续性待观察（方向未知）
09-04 98.0P — Vol 1,545 | 最新价 $0.31 | OI 3276→7510 (ΔOI +4234张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4234张（+129.2% vs前日OI），连续性待观察（方向未知）
09-18 95.0P — Vol 65 | 最新价 $1.75 | OI 11067→14922 (ΔOI +3855张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3855张（+34.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,354 张（Put 12,974 / Call 10,380），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +14.1k / P +0.5k ｜ Activity HIGH ｜ 7D
09-18  C +3.4k / P +11.5k ｜ Activity MEDIUM △ ｜ 14D
09-25  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 21D
10-02  C +0.1k / P +0.6k ｜ Activity MEDIUM △ ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 49.0k / P 36.0k
今日变化ΔOI: C +14.1k / P +0.5k
平值价格ATM:  C 2.27 / P 2.46
隐含波动率 ATM IV:  42.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 239k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 102 ｜ +5,300 ｜ $1.14 ｜ 名义 $604.2k* ｜ +3.2%
C 106 ｜ +5,080 ｜ $0.44 ｜ 名义 $223.5k* ｜ +7.3%
C 107 ｜ +3,036 ｜ $0.75 ｜ 名义 $227.7k* ｜ +8.3%
结构参考：102（+3.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 42.4%｜历史 Rank 89%（近端代理）｜净 delta 敞口 正 239,329 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 95P +3,855 ｜ 110C +3,173

09-25（MEDIUM △）Top ΔOI: 102C +125 ｜ 95P +112

10-02（MEDIUM △）Top ΔOI: 90P +97 ｜ 99P +94

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/GDX_morning.json