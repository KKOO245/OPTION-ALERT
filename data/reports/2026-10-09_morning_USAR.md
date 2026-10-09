# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $776.00 ｜ QQQ $749.78
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 42.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 12.63 → 今开 12.67（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 12.75 ｜ 低 12.42

Options: P/C成交量 4.38 | OI比 0.19 | ATM IV 85.3% | Skew 6.0pp | Term 0.83 | ExpMove ±7.3%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 6.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.19）+ 当日成交偏 Put（P/C量 4.38）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 4.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.19×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±7.3% ｜ 10-23（14D）±11.0% ｜ 10-30（21D）±13.3% ｜ 11-06（28D）±15.6%
   ⇒ IV–VIX Spread: +70.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,000,992 | GEX Change vs 上次快照 4,391,287 | Flip: Primary Flip: 10.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 143 / LOW 74 / INVALID 179
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 10.96（全链重定价，覆盖 83%）
最近结构参考: Flip 11（现价高于该位 13.5%）
量化视角： 正 Gamma（200万，无历史分位）｜由负转正（+439万）｜现价位于 Flip 上方 13.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 13.0C — Vol 1,492 | 最新价 $0.07 | OI 188→934 (ΔOI +746张) | ΔOI/Volume 50.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增746张（+396.8% vs前日OI），连续性待观察（方向未知）
10-16 13.0C — Vol 879 | 最新价 $0.34 | OI 323→665 (ΔOI +342张) | ΔOI/Volume 38.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增342张（+105.9% vs前日OI），连续性待观察（方向未知）
10-30 15.5P — Vol 439 | 最新价 $3.05 | OI 253→571 (ΔOI +318张) | ΔOI/Volume 72.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增318张（+125.7% vs前日OI），连续性待观察（方向未知）
10-16 12.5P — Vol 511 | 最新价 $0.41 | OI 401→690 (ΔOI +289张) | ΔOI/Volume 56.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增289张（+72.1% vs前日OI），连续性待观察（方向未知）
10-16 14.0C — Vol 703 | 最新价 $0.12 | OI 1150→1405 (ΔOI +255张) | ΔOI/Volume 36.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增255张（+22.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,950 张（Put 607 / Call 1,343），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 20.3k / P 3.8k，今日成交量: C 0.4k / P 1.5k，平值价格ATM: C $0.11 / P $0.12 ｜ ATM IV 85.3%，预期波动 ±1.9%，Max Pain 14
Top ΔOI: C 13 +746 ｜ P 15 -564 ｜ P 14 -499

📆 Forward Expiration Structure

10-16  C +1.0k / P -0.5k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +0.3k / P -0.6k ｜ Activity MEDIUM △ ｜ 14D
10-30  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
11-06  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 51.1k / P 16.3k，今日变化ΔOI: C +1.0k / P -0.5k，平值价格ATM: C $0.43 / P $0.48 ｜ ATM IV 63.2%，净 delta 敞口 119k shares
Top ΔOI: C 13 +342 ｜ P 18 -329 ｜ P 16 -309
仓位参考: Max Pain 15 ｜ Put Wall 13（+4.5%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 63.2%｜历史 Rank 14%（近端代理）｜IV/RV 1.19×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 119,200 股

10-23（MEDIUM △）Top ΔOI: 15P -434 ｜ 13C +251
10-23（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 13.5（+8.5%，弱）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 15P +318 ｜ 19P -262
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 13.5（+8.5%，弱）（OI 0.2k） ｜ Put Wall 12.5（+0.4%，弱）（OI 1.2k）

11-06（MEDIUM △）Top ΔOI: 16P +187 ｜ 13C +103
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 13.5（+8.5%，弱）（OI 0.2k） ｜ Put Wall 13（+4.5%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/USAR_morning.json