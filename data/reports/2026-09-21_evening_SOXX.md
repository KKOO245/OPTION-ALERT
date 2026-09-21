# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 545.20 → 收盘 559.34（+2.6%） ｜ 今日高 562.20 ｜ 低 541.47 ｜ 昨收 533.07 → 收盘 559.34（+4.9%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-09-24，窗口结束前不做对错判定）

Options: P/C成交量 0.94 | OI比 1.45 | ATM IV 36.2% | Skew 2.9pp | Term 1.06 | ExpMove ±3.0%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.45×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±3.0% ｜ 10-02（11D）±4.9% ｜ 10-09（18D）±6.5% ｜ 10-16（25D）±8.2%
   ⇒ IV–VIX Spread: +21.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,587,959 | GEX Change vs 上次快照 3,690,197 | Flip: Primary Flip: 543.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 523 / LOW 236 / INVALID 747
结构观察区: Primary Flip 543.53（全链重定价，覆盖 99%）
最近结构参考: Flip 544（现价高于该位 2.9%）
量化视角： 正 Gamma（759万，无历史分位）｜正 Gamma 增强（+369万）｜现价位于 Flip 上方 2.91%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 520（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 544（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 525.0P — Vol 353 | 最新价 $8.90 | OI 568→1294 (ΔOI +726张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增726张（+127.8% vs前日OI），连续性待观察（方向未知）
10-16 500.0P — Vol 156 | 最新价 $4.20 | OI 4577→5293 (ΔOI +716张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增716张（+15.6% vs前日OI），值得跟踪（方向未知）
10-16 435.0P — Vol 19 | 最新价 $1.01 | OI 189→894 (ΔOI +705张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增705张（+373.0% vs前日OI），连续性待观察（方向未知）
09-25 520.0P — Vol 262 | 最新价 $0.62 | OI 191→481 (ΔOI +290张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增290张（+151.8% vs前日OI），值得跟踪（方向未知）
09-25 490.0P — Vol 280 | 最新价 $0.20 | OI 1430→1683 (ΔOI +253张) | ΔOI/Volume 90.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增253张（+17.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,690 张（Put 2,690 / Call 0），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.7k / P +0.9k ｜ Activity HIGH ｜ 4D
10-02  C +0.3k / P +0.6k ｜ Activity HIGH ｜ 11D
10-09  C +0.2k / P +83 ｜ Activity HIGH ｜ 18D
10-16  C -0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 11.1k / P 16.0k，今日变化ΔOI: C +0.7k / P +0.9k，平值价格ATM: C $8.89 / P $7.86 ｜ ATM IV 36.2%，净 delta 敞口 66k shares
Top ΔOI: P 520 +290
仓位参考: Max Pain 520 ｜ Call Wall 580（+3.7%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 36.2%｜历史 Rank 59%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 65,549 股

📆 10-02 Forward Structure
存量OI: C 11.6k / P 11.1k，今日变化ΔOI: C +0.3k / P +0.6k，平值价格ATM: C $14.23 / P $13.22 ｜ ATM IV 36.7%，净 delta 敞口 26k shares
Top ΔOI: C 550 +134
仓位参考: Max Pain 515 ｜ Call Wall 542.5（-3.0%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.7%｜历史 Rank 59%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 25,958 股

📆 10-09 Forward Structure
存量OI: C 3.5k / P 1.9k，今日变化ΔOI: C +0.2k / P +83，平值价格ATM: C $17.80 / P $18.29 ｜ ATM IV 36.3%，净 delta 敞口 9k shares
Top ΔOI: C 530 +99 ｜ P 525 +38 ｜ C 550 +28
仓位参考: Max Pain 515 ｜ Call Wall 525（-6.1%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 36.3%｜历史 Rank 59%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 9,013 股

10-16（MEDIUM △）Top ΔOI: 480P -1,227 ｜ 525P +726
10-16（MEDIUM △）仓位参考: Max Pain 520 ｜ Call Wall 550（-1.7%，弱）（OI 3.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SOXX_evening.json