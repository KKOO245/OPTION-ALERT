# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.05 ｜ QQQ $706.68
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 150C ΔOI +8,484（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 145.80 → 今开 144.38（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 149.71 ｜ 低 144.21

Options: P/C成交量 0.53 | OI比 0.83 | ATM IV 111.5% | Skew 2.5pp | Term 0.65 | ExpMove ±9.0%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价中性（Skew 2.5pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（7D）±9.0% ｜ 11-06（14D）±11.8% ｜ 11-13（21D）±14.2% ｜ 11-20（28D）±16.3%
   ⇒ IV–VIX Spread: +91.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 70,166,700 | GEX Change vs 上次快照 2,284,229 | Flip: Primary Flip: 137.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 546 / LOW 117 / INVALID 281
结构观察区: Primary Flip 137.92（全链重定价，覆盖 94%）
Call Wall 155（弱结构｜现价低于该位 3.6%）
最近结构参考: Call Wall 155（现价低于该位 3.6%）
量化视角： 正 Gamma（7017万，无历史分位）｜正 Gamma 增强（+228万）｜现价位于 Flip 上方 8.32%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）；上方 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 150.0C — Vol 9,688 | 最新价 $4.90 | OI 2352→10836 (ΔOI +8484张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8484张（+360.7% vs前日OI），连续性待观察（方向未知）
10-23 155.0C — Vol 20,679 | 最新价 $0.32 | OI 28994→34358 (ΔOI +5364张) | ΔOI/Volume 25.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5364张（+18.5% vs前日OI），连续性待观察（方向未知）
10-30 152.5C — Vol 6,029 | 最新价 $4.23 | OI 835→5848 (ΔOI +5013张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5013张（+600.4% vs前日OI），连续性待观察（方向未知）
10-30 157.5C — Vol 6,266 | 最新价 $2.70 | OI 1089→5754 (ΔOI +4665张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4665张（+428.4% vs前日OI），连续性待观察（方向未知）
10-23 140.0P — Vol 25,516 | 最新价 $0.72 | OI 6398→10058 (ΔOI +3660张) | ΔOI/Volume 14.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3660张（+57.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,186 张（Put 3,660 / Call 23,526），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 233.7k / P 193.8k，今日成交量: C 42.0k / P 22.2k，平值价格ATM: C $1.92 / P $1.67 ｜ ATM IV 111.5%，预期波动 ±2.4%，Max Pain 141
Top ΔOI: C 155 +5,364 ｜ P 140 +3,660 ｜ C 142 -3,212

📆 Forward Expiration Structure

10-30  C +26.0k / P +10.0k ｜ Activity HIGH ｜ 7D
11-06  C +1.3k / P +3.8k ｜ Activity MEDIUM △ ｜ 14D
11-13  C +0.5k / P +3.7k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +1.6k / P +4.1k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 81.2k / P 106.0k，今日变化ΔOI: C +26.0k / P +10.0k，平值价格ATM: C $6.75 / P $6.75 ｜ ATM IV 77.6%，净 delta 敞口 900k shares
Top ΔOI: C 150 +8,484 ｜ C 152 +5,013 ｜ C 157 +4,665
仓位参考: Max Pain 150 ｜ Call Wall 150（+0.4%）（OI 10.8k） ｜ Put Wall 155（+3.7%，弱）（OI 4.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.6%｜历史 Rank 88%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 899,847 股

11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+7.1%）（OI 2.2k） ｜ Put Wall 160（+7.1%，弱）（OI 3.7k）

11-13（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 144（-3.6%，弱）（OI 0.8k） ｜ Put Wall 160（+7.1%，弱）（OI 2.2k）

📆 11-20 Forward Structure
存量OI: C 142.5k / P 103.0k，今日变化ΔOI: C +1.6k / P +4.1k，平值价格ATM: C $12.60 / P $11.70 ｜ ATM IV 72.2%，净 delta 敞口 -34k shares
仓位参考: Max Pain 135 ｜ Call Wall 135（-9.6%）（OI 42.3k） ｜ Put Wall 160（+7.1%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.2%｜历史 Rank 88%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 34,213 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/MSTR_morning.json