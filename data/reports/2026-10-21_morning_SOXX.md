# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $773.28 ｜ QQQ $725.20
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 515C ΔOI +1,163（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 520C ΔOI +6,396 占该期限总 OI 33.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 500.01 → 今开 509.74（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 511.90 ｜ 低 503.40

Options: P/C成交量 5.01 | OI比 1.52 | ATM IV 50.3% | Skew 7.9pp | Term 0.80 | ExpMove ±3.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 7.9pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 5.01）——观察点，非方向信号
   ⇒ Put/Call Volume: 5.01×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.52×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±3.3% ｜ 10-30（9D）±7.6% ｜ 11-06（16D）±3.8% ｜ 11-13（23D）±4.5%
   ⇒ IV–VIX Spread: +33.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -23,699,893 | GEX Change vs 上次快照 12,307,081 | Flip: Primary Flip: 542.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 623 / LOW 270 / INVALID 653
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 542.07（全链重定价，覆盖 99%）
Call Wall 520（弱结构｜现价低于该位 2.4%）
最近结构参考: Call Wall 520（现价低于该位 2.4%）
量化视角： 负 Gamma（2370万，无历史分位）｜负 Gamma 缓解（+1231万）｜现价位于 Flip 下方 6.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 515（MaxPain，仅结算参考） / 520（Call Wall，弱结构）。
• Gamma 区域：切换参考 542（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 520.0C — Vol 6,409 | 最新价 $14.24 | OI 28→6424 (ΔOI +6396张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6396张（+22842.9% vs前日OI），连续性待观察（方向未知）
11-13 570.0C — Vol 6,413 | 最新价 $2.90 | OI 112→6434 (ΔOI +6322张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6322张（+5644.6% vs前日OI），连续性待观察（方向未知）
10-30 440.0P — Vol 5,008 | 最新价 $1.70 | OI 52→5056 (ΔOI +5004张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5004张（+9623.1% vs前日OI），连续性待观察（方向未知）
11-13 460.0P — Vol 3,201 | 最新价 $7.10 | OI 22→3221 (ΔOI +3199张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3199张（+14540.9% vs前日OI），连续性待观察（方向未知）
10-30 450.0P — Vol 5,607 | 最新价 $2.22 | OI 9983→13016 (ΔOI +3033张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3033张（+30.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,954 张（Put 11,236 / Call 12,718），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.0k / P +0.4k ｜ Activity MEDIUM △ ｜ 2D
10-30  C +1.8k / P +4.5k ｜ Activity HIGH ｜ 9D
11-06  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 16D
11-13  C +12.8k / P +3.3k ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 13.3k / P 20.1k，今日变化ΔOI: C +2.0k / P +0.4k，平值价格ATM: C $8.00 / P $8.66 ｜ ATM IV 50.3%，净 delta 敞口 74k shares
Top ΔOI: C 515 +1,163 ｜ P 495 +292
仓位参考: Max Pain 515 ｜ Call Wall 515（+1.5%）（OI 2.2k） ｜ Put Wall 510（+0.5%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.3%｜历史 Rank 86%（近端代理）｜IV/RV 1.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 73,996 股

📆 10-30 Forward Structure
存量OI: C 21.6k / P 147.8k，今日变化ΔOI: C +1.8k / P +4.5k，平值价格ATM: C $14.90 / P $23.87 ｜ ATM IV 43.9%，净 delta 敞口 125k shares
Top ΔOI: P 440 +5,004 ｜ P 480 -4,851 ｜ P 450 +3,033
仓位参考: Max Pain 530 ｜ Call Wall 525（+3.5%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 43.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 125,123 股

11-06（MEDIUM △）Top ΔOI: 495P +323 ｜ 537C -149
11-06（MEDIUM △）仓位参考: Max Pain 538 ｜ Call Wall 537.5（+5.9%，弱）（OI 0.8k） ｜ Put Wall 495（-2.4%，弱）（OI 1.0k）

📆 11-13 Forward Structure
存量OI: C 14.0k / P 5.1k，今日变化ΔOI: C +12.8k / P +3.3k，平值价格ATM: C $22.95 / P $0.00 ｜ ATM IV 40.9%，净 delta 敞口 316k shares
Top ΔOI: C 520 +6,396 ｜ C 570 +6,322 ｜ P 460 +3,199
仓位参考: Max Pain 520 ｜ Call Wall 520（+2.5%，弱）（OI 6.4k）
量化解读： 存量 Call 重｜ATM IV 40.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 316,285 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/SOXX_morning.json