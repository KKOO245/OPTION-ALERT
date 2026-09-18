# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $759.22 ｜ QQQ $717.51
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 375.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 383.54 → 今开 381.84（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 394.53 ｜ 低 379.50

Options: P/C成交量 0.30 | OI比 0.92 | ATM IV 121.5% | Skew 30.7pp | Term 0.28 | ExpMove ±0.7%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.28，近月 IV 高于远月）｜保护溢价显著（Skew 30.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±0.7% ｜ 10-02（14D）±1.9% ｜ 10-09（21D）±9.6% ｜ 10-16（28D）±7.2%
   ⇒ IV–VIX Spread: +106.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,093,962 | GEX Change vs 上次快照 -134,615 | Flip: Candidates 375.71 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 73%（带内） ｜ IV 有效性: VALID 247 / LOW 193 / INVALID 536
结构观察区: ≈376（全链重定价，覆盖 73%，CONDITIONAL）
Call Wall 400（弱结构｜现价低于该位 2.1%）
最近结构参考: Call Wall 400（现价低于该位 2.1%）
量化视角： 正 Gamma（109万，无历史分位）｜正 Gamma 减弱（13万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 372（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 376（全链重定价，覆盖 73%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 360.0P — Vol 158（Yahoo补） | 最新价 $1.20 | OI 152→203 (ΔOI +51张) | ΔOI/Volume 32.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增51张（+33.5% vs前日OI），连续性待观察（方向未知）
10-16 370.0C — Vol 55（Yahoo补） | 最新价 $23.70 | OI 216→266 (ΔOI +50张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50张（+23.1% vs前日OI），连续性待观察（方向未知）
10-16 400.0C — Vol 151（Yahoo补） | 最新价 $7.93 | OI 428→465 (ΔOI +37张) | ΔOI/Volume 24.5% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增37张（+8.6% vs前日OI），值得跟踪（方向未知）
09-25 325.0P — Vol 32（Yahoo补） | 最新价 $0.07 | OI 10→40 (ΔOI +30张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30张（+300.0% vs前日OI），连续性待观察（方向未知）
09-25 400.0C — Vol 36（Yahoo补） | 最新价 $2.25 | OI 140→167 (ΔOI +27张) | ΔOI/Volume 75.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增27张（+19.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 195 张（Put 81 / Call 114），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 16.3k / P 15.0k，今日成交量: C 0 / P 3，平值价格ATM: C $2.75 / P $10.25 ｜ ATM IV 121.5%，预期波动 ±3.3%，Max Pain 372
Top ΔOI: C 375 -81 ｜ P 405 -48 ｜ C 385 -39

📆 Forward Expiration Structure

09-25  C +53 / P +0.1k ｜ Activity MEDIUM △ ｜ 7D
10-02  C +56 / P +2 ｜ Activity MEDIUM △ ｜ 14D
10-09  C +5 / P -2 ｜ Activity LOW ｜ 21D
10-16  C +0.2k / P +54 ｜ Activity LOW ｜ 28D

📆 09-25 Forward Structure
存量OI: C 1.7k / P 0.9k，今日变化ΔOI: C +53 / P +0.1k，平值价格ATM: C $2.90 / P $0.00 ｜ ATM IV 32.1%，净 delta 敞口 669 shares
Top ΔOI: P 360 +51 ｜ C 400 +27
仓位参考: Max Pain 370 ｜ Call Wall 430（+9.9%，弱）（OI 0.3k） ｜ Put Wall 360（-8.0%）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.1%｜历史 Rank 100%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 669 股

10-02（MEDIUM △）Top ΔOI: 407C +24 ｜ 420C +20
10-02（MEDIUM △）仓位参考: Max Pain 365 ｜ Call Wall 405（+3.5%，弱）（OI 79）

10-09（Activity LOW）仓位参考: Max Pain 380 ｜ Call Wall 380（-2.9%）（OI 0.1k） ｜ Put Wall 385（-1.6%）（OI 0.2k）

10-16（Activity LOW）仓位参考: Max Pain 385 ｜ Call Wall 400（+2.2%，弱）（OI 0.5k） ｜ Put Wall 380（-2.9%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/ISRG_morning.json