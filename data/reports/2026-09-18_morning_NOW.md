# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $759.22 ｜ QQQ $717.57
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 138.47 → 今开 139.71（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 139.94 ｜ 低 135.27

Options: P/C成交量 0.43 | OI比 0.99 | ATM IV 64.9% | Skew -2.7pp | Term 0.78 | ExpMove ±5.8%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±5.8% ｜ 10-02（14D）±7.8% ｜ 10-09（21D）±9.0% ｜ 10-16（28D）±11.1%
   ⇒ IV–VIX Spread: +49.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 21,529,306 | GEX Change vs 上次快照 1,197,400 | Flip: Primary Flip: 129.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 547 / LOW 105 / INVALID 168
结构观察区: Primary Flip 129.77（全链重定价，覆盖 92%）
最近结构参考: Flip 130（现价高于该位 5.0%）
量化视角： 正 Gamma（2153万，无历史分位）｜正 Gamma 增强（+120万）｜现价位于 Flip 上方 5.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 123（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 85.0P — Vol 6,010（Yahoo补） | 最新价 $0.08 | OI 2951→8796 (ΔOI +5845张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5845张（+198.1% vs前日OI），连续性待观察（方向未知）
09-25 150.0C — Vol 34 | 最新价 $0.82 | OI 2130→5370 (ΔOI +3240张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3240张（+152.1% vs前日OI），连续性待观察（方向未知）
09-18 150.0C — Vol 519 | 最新价 $0.03 | OI 7197→8422 (ΔOI +1225张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1225张（+17.0% vs前日OI），值得跟踪（方向未知）
09-18 133.0P — Vol 19 | 最新价 $0.14 | OI 520→1579 (ΔOI +1059张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1059张（+203.7% vs前日OI），连续性待观察（方向未知）
09-18 135.0P — Vol 47 | 最新价 $0.45 | OI 2133→3060 (ΔOI +927张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增927张（+43.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,296 张（Put 7,831 / Call 4,465），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 114.8k / P 113.1k，今日成交量: C 7.5k / P 3.2k，平值价格ATM: C $0.98 / P $0.89 ｜ ATM IV 64.9%，预期波动 ±1.4%，Max Pain 123
Top ΔOI: C 150 +1,225 ｜ P 133 +1,059 ｜ P 135 +927

📆 Forward Expiration Structure

09-25  C +5.5k / P +2.2k ｜ Activity HIGH ｜ 7D
10-02  C +0.8k / P +0.8k ｜ Activity MEDIUM △ ｜ 14D
10-09  C +0.2k / P +0.4k ｜ Activity HIGH ｜ 21D
10-16  C +1.4k / P +6.4k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 21.4k / P 13.6k，今日变化ΔOI: C +5.5k / P +2.2k，平值价格ATM: C $3.95 / P $3.94 ｜ ATM IV 50.2%，净 delta 敞口 5k shares
Top ΔOI: C 150 +3,240 ｜ C 145 +642 ｜ P 139 +420
仓位参考: Max Pain 137 ｜ Call Wall 145（+6.4%，弱）（OI 3.0k） ｜ Put Wall 130（-4.6%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 50.2%｜历史 Rank 85%（近端代理）｜净 delta 敞口 正 5,262 股

10-02（MEDIUM △）仓位参考: Max Pain 132 ｜ Call Wall 125（-8.3%，弱）（OI 1.0k） ｜ Put Wall 130（-4.6%，弱）（OI 0.7k）

📆 10-09 Forward Structure
存量OI: C 3.0k / P 4.4k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $6.85 / P $5.40 ｜ ATM IV 51.0%，净 delta 敞口 -9k shares
Top ΔOI: P 144 +216 ｜ C 150 +158 ｜ C 140 +44
仓位参考: Max Pain 140 ｜ Call Wall 145（+6.4%，弱）（OI 0.2k） ｜ Put Wall 140（+2.7%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 51.0%｜历史 Rank 85%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,374 股

📆 10-16 Forward Structure
存量OI: C 64.2k / P 53.2k，今日变化ΔOI: C +1.4k / P +6.4k，平值价格ATM: C $8.35 / P $6.80 ｜ ATM IV 50.9%，净 delta 敞口 12k shares
Top ΔOI: C 155 +502 ｜ C 150 +442
仓位参考: Max Pain 125 ｜ Call Wall 145（+6.4%，弱）（OI 3.4k） ｜ Put Wall 130（-4.6%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.9%｜历史 Rank 85%（近端代理）｜净 delta 敞口 正 12,172 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NOW_morning.json