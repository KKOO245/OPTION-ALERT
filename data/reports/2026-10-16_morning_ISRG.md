# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $763.10 ｜ QQQ $709.80
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 409.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 427.86 → 今开 428.43（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 434.89 ｜ 低 427.19

Options: P/C成交量 0.04 | OI比 0.90 | ATM IV 56.9% | Skew 13.3pp | Term 0.83 | ExpMove ±3.3%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 13.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.04×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（7D）±3.3% ｜ 10-30（14D）±0.0% ｜ 11-06（21D）±4.7% ｜ 11-13（28D）±3.5%
   ⇒ IV–VIX Spread: +40.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,146,862 | GEX Change vs 上次快照 180,920 | Flip: Candidates 409.12 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 349 / LOW 143 / INVALID 476
结构观察区: ≈409（全链重定价，覆盖 76%，CONDITIONAL）
Call Wall 420（弱结构｜现价高于该位 3.2%）
最近结构参考: Call Wall 420（现价高于该位 3.2%）
量化视角： 正 Gamma（415万，无历史分位）｜正 Gamma 增强（+18万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 409（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 395.0P — Vol 136 | 最新价 $9.71 | OI 81→213 (ΔOI +132张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增132张（+163.0% vs前日OI），连续性待观察（方向未知）
10-16 422.5C — Vol 160 | 最新价 $7.10 | OI 20→94 (ΔOI +74张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增74张（+370.0% vs前日OI），连续性待观察（方向未知）
10-16 437.5C — Vol 73 | 最新价 $0.80 | OI 45→112 (ΔOI +67张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增67张（+148.9% vs前日OI），连续性待观察（方向未知）
10-23 420.0C — Vol 62 | 最新价 $21.45 | OI 58→112 (ΔOI +54张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+93.1% vs前日OI），连续性待观察（方向未知）
11-20 450.0C — Vol 88 | 最新价 $14.51 | OI 418→471 (ΔOI +53张) | ΔOI/Volume 60.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增53张（+12.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 380 张（Put 132 / Call 248），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 12.0k / P 10.8k，今日成交量: C 1.0k / P 30，平值价格ATM: C $3.22 / P $2.25 ｜ ATM IV 56.9%，预期波动 ±1.3%，Max Pain 390
Top ΔOI: C 422 +74 ｜ C 437 +67 ｜ P 410 -50

📆 Forward Expiration Structure

10-23  C +0.2k / P +88 ｜ Activity MEDIUM △ ｜ 7D
10-30  C +76 / P +49 ｜ Activity MEDIUM △ ｜ 14D
11-06  C +66 / P +13 ｜ Activity MEDIUM △ ｜ 21D
11-13  C +38 / P +72 ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 2.7k / P 2.0k，今日变化ΔOI: C +0.2k / P +88，平值价格ATM: C $14.20 / P $0.00 ｜ ATM IV 72.9%，净 delta 敞口 5k shares
Top ΔOI: C 420 +54 ｜ P 425 +20
仓位参考: Max Pain 415 ｜ Call Wall 425（-2.0%，弱）（OI 0.5k） ｜ Put Wall 415（-4.3%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 72.9%｜历史 Rank 94%（近端代理）｜IV/RV 2.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,365 股

10-30（MEDIUM △）Top ΔOI: 420C +25 ｜ 410P +15
10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+6.1%，弱）（OI 96） ｜ Put Wall 400（-7.8%，弱）（OI 48）

11-06（MEDIUM △）Top ΔOI: 420C +29 ｜ 410C +19
11-06（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 455（+4.9%，弱）（OI 52） ｜ Put Wall 400（-7.8%，弱）（OI 28）

11-13（MEDIUM △）Top ΔOI: 410C +24
11-13（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 410（-5.4%，弱）（OI 26）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/ISRG_morning.json