# 期权晨报 2026-09-18（快照 10:20 ET）

📊 市场环境

SPY $758.97 ｜ QQQ $716.80
VIX 15.53 ↑0.6%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 260P ΔOI +1,322（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 280.76 → 今开 284.32（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 285.10 ｜ 低 266.72

Options: P/C成交量 0.58 | OI比 0.90 | ATM IV 139.1% | Skew 2.9pp | Term 0.55 | ExpMove ±8.7%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±8.7% ｜ 10-02（14D）±12.1% ｜ 10-09（21D）±14.9% ｜ 10-16（28D）±16.6%
   ⇒ IV–VIX Spread: +123.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,465,002 | GEX Change vs 上次快照 -19,629,471 | Flip: Primary Flip: 260.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 554 / LOW 111 / INVALID 345
结构观察区: Primary Flip 260.38（全链重定价，覆盖 88%）
Call Wall 250（弱结构｜现价高于该位 8.3%）
最近结构参考: Flip 260（现价高于该位 4.0%）
量化视角： 正 Gamma（1647万，无历史分位）｜正 Gamma 减弱（1963万）｜现价位于 Flip 上方 3.99%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 260（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 307.5C — Vol 1 | 最新价 $0.03 | OI 107→4496 (ΔOI +4389张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4389张（+4101.9% vs前日OI），连续性待观察（方向未知）
09-18 265.0P — Vol 144 | 最新价 $0.73 | OI 648→4994 (ΔOI +4346张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4346张（+670.7% vs前日OI），连续性待观察（方向未知）
09-18 252.5P — Vol 9 | 最新价 $0.10 | OI 717→2636 (ΔOI +1919张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1919张（+267.6% vs前日OI），连续性待观察（方向未知）
09-25 260.0P — Vol 395 | 最新价 $4.86 | OI 631→1953 (ΔOI +1322张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1322张（+209.5% vs前日OI），连续性待观察（方向未知）
10-16 185.0P — Vol 1,031（Yahoo补） | 最新价 $0.93 | OI 630→1552 (ΔOI +922张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增922张（+146.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,898 张（Put 8,509 / Call 4,389），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 172.6k / P 155.5k，今日成交量: C 9.8k / P 5.7k，平值价格ATM: C $4.58 / P $3.67 ｜ ATM IV 139.1%，预期波动 ±3.0%，Max Pain 250
Top ΔOI: C 307 +4,389 ｜ P 265 +4,346 ｜ P 252 +1,919

📆 Forward Expiration Structure

09-25  C +2.5k / P +4.9k ｜ Activity HIGH ｜ 7D
10-02  C +0.3k / P +1.3k ｜ Activity MEDIUM △ ｜ 14D
10-09  C +0.2k / P +97 ｜ Activity MEDIUM △ ｜ 21D
10-16  C -68 / P +2.8k ｜ Activity MEDIUM △ ｜ 28D

📆 09-25 Forward Structure
存量OI: C 22.0k / P 30.4k，今日变化ΔOI: C +2.5k / P +4.9k，平值价格ATM: C $12.35 / P $11.21 ｜ ATM IV 77.4%，净 delta 敞口 -101k shares
Top ΔOI: P 260 +1,322 ｜ P 280 +831 ｜ C 280 +624
仓位参考: Max Pain 255 ｜ Call Wall 280（+3.4%，弱）（OI 2.5k） ｜ Put Wall 260（-4.0%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 77.4%｜历史 Rank 87%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 101,491 股

10-02（MEDIUM △）Top ΔOI: 250P +174 ｜ 255P +118
10-02（MEDIUM △）仓位参考: Max Pain 245 ｜ Call Wall 270（-0.3%）（OI 5.4k） ｜ Put Wall 245（-9.5%，弱）（OI 1.1k）

10-09（MEDIUM △）Top ΔOI: 285C +39
10-09（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 295（+9.0%）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 280C -1,026 ｜ 185P +922
10-16（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 280（+3.4%，弱）（OI 8.9k） ｜ Put Wall 260（-4.0%，弱）（OI 3.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/BE_morning.json