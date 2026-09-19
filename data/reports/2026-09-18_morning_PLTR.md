# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.85 ｜ QQQ $nan
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 175C ΔOI +983（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 176.24 → 今开 177.04（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 177.75 ｜ 低 172.00

Options: P/C成交量 0.81 | OI比 0.83 | ATM IV 62.3% | Skew 1.4pp | Term 0.74 | ExpMove ±5.0%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价薄（Skew 1.4pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±5.0% ｜ 10-02（14D）±7.2% ｜ 10-09（21D）±8.9% ｜ 10-16（28D）±10.3%
   ⇒ IV–VIX Spread: +46.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 83,330,799 | GEX Change vs 上次快照 -28,060,114 | Flip: Primary Flip: 166.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 550 / LOW 85 / INVALID 201
结构观察区: Primary Flip 166.67（全链重定价，覆盖 93%）
Call Wall 180（弱结构｜现价低于该位 3.3%）
最近结构参考: Call Wall 180（现价低于该位 3.3%）
量化视角： 正 Gamma（8333万，无历史分位）｜正 Gamma 减弱（2806万）｜现价位于 Flip 上方 4.41%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 100.0P — Vol 8,380（Yahoo补） | 最新价 $0.15 | OI 11056→18015 (ΔOI +6959张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6959张（+62.9% vs前日OI），连续性待观察（方向未知）
09-25 150.0P — Vol 80 | 最新价 $0.28 | OI 2090→5240 (ΔOI +3150张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3150张（+150.7% vs前日OI），连续性待观察（方向未知）
09-18 182.5C — Vol 1,613 | 最新价 $0.03 | OI 10801→13521 (ΔOI +2720张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2720张（+25.2% vs前日OI），连续性待观察（方向未知）
09-18 172.5P — Vol 1,911 | 最新价 $0.90 | OI 4886→7511 (ΔOI +2625张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2625张（+53.7% vs前日OI），连续性待观察（方向未知）
10-09 85.0P — Vol 2,504（Yahoo补） | 最新价 $0.06 | OI 4→2504 (ΔOI +2500张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2500张（+62500.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,954 张（Put 15,234 / Call 2,720），跨 4 个期限｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 353.4k / P 293.8k，今日成交量: C 55.2k / P 44.6k，平值价格ATM: C $0.63 / P $1.86 ｜ ATM IV 62.3%，预期波动 ±1.4%，Max Pain 160
Top ΔOI: C 182 +2,720 ｜ P 172 +2,625 ｜ C 185 +1,744

📆 Forward Expiration Structure

09-25  C +6.5k / P +12.6k ｜ Activity HIGH ｜ 7D
10-02  C +3.9k / P +1.0k ｜ Activity HIGH ｜ 14D
10-09  C +0.5k / P +4.1k ｜ Activity HIGH ｜ 21D
10-16  C +1.8k / P +8.5k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 47.9k / P 59.9k，今日变化ΔOI: C +6.5k / P +12.6k，平值价格ATM: C $3.85 / P $4.85 ｜ ATM IV 45.2%，净 delta 敞口 -83k shares
Top ΔOI: P 150 +3,150 ｜ P 165 +1,812 ｜ P 160 +1,507
仓位参考: Max Pain 172 ｜ Call Wall 190（+9.2%，弱）（OI 6.0k） ｜ Put Wall 170（-2.3%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 45.2%｜历史 Rank 92%（近端代理）｜净 delta 敞口 负 83,406 股

📆 10-02 Forward Structure
存量OI: C 24.5k / P 26.1k，今日变化ΔOI: C +3.9k / P +1.0k，平值价格ATM: C $5.95 / P $6.63 ｜ ATM IV 45.8%，净 delta 敞口 103k shares
Top ΔOI: C 175 +983 ｜ C 187 +672
仓位参考: Max Pain 172 ｜ Call Wall 180（+3.4%，弱）（OI 3.1k） ｜ Put Wall 170（-2.3%）（OI 4.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.8%｜历史 Rank 92%（近端代理）｜净 delta 敞口 正 102,812 股

📆 10-09 Forward Structure
存量OI: C 11.2k / P 20.1k，今日变化ΔOI: C +0.5k / P +4.1k，平值价格ATM: C $7.50 / P $7.95 ｜ ATM IV 45.8%，净 delta 敞口 -33k shares
Top ΔOI: P 170 +329 ｜ P 172 +312
仓位参考: Max Pain 172 ｜ Call Wall 190（+9.2%，弱）（OI 0.8k） ｜ Put Wall 170（-2.3%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 45.8%｜历史 Rank 92%（近端代理）｜净 delta 敞口 负 33,044 股

📆 10-16 Forward Structure
存量OI: C 127.0k / P 151.6k，今日变化ΔOI: C +1.8k / P +8.5k，平值价格ATM: C $8.80 / P $9.10 ｜ ATM IV 46.2%，净 delta 敞口 -30k shares
Top ΔOI: P 100 +6,959 ｜ P 170 +994 ｜ C 200 +709
仓位参考: Max Pain 160 ｜ Call Wall 170（-2.3%）（OI 16.4k） ｜ Put Wall 170（-2.3%，弱）（OI 14.7k）
量化解读： 存量 Put 重｜ATM IV 46.2%｜历史 Rank 92%（近端代理）｜净 delta 敞口 负 29,717 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/PLTR_morning.json