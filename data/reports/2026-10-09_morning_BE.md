# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.69 ｜ QQQ $751.27
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 275C ΔOI +827（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 272.82 → 今开 275.85（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 277.79 ｜ 低 271.03

Options: P/C成交量 0.49 | OI比 1.03 | ATM IV 95.5% | Skew 0.1pp | Term 0.85 | ExpMove ±7.5%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 0.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（7D）±7.5% ｜ 10-23（14D）±10.3% ｜ 10-30（21D）±15.0% ｜ 11-06（28D）±18.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 264,564 | GEX Change vs 上次快照 7,464,408 | Flip: Primary Flip: 274.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 552 / LOW 115 / INVALID 203
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 274.01（全链重定价，覆盖 98%）
Call Wall 300（弱结构｜现价低于该位 8.6%）
最近结构参考: Flip 274（现价高于该位 0.1%）
量化视角： 正 Gamma（26万，无历史分位）｜由负转正（+746万）｜现价位于 Flip 上方 0.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 280（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 274（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 300.0C — Vol 6,157 | 最新价 $0.13 | OI 3055→5547 (ΔOI +2492张) | ΔOI/Volume 40.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2492张（+81.6% vs前日OI），连续性待观察（方向未知）
10-09 285.0C — Vol 4,718 | 最新价 $1.03 | OI 789→2093 (ΔOI +1304张) | ΔOI/Volume 27.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1304张（+165.3% vs前日OI），连续性待观察（方向未知）
10-09 295.0C — Vol 3,238 | 最新价 $0.27 | OI 1505→2560 (ΔOI +1055张) | ΔOI/Volume 32.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1055张（+70.1% vs前日OI），连续性待观察（方向未知）
10-09 280.0C — Vol 6,215 | 最新价 $2.07 | OI 953→1922 (ΔOI +969张) | ΔOI/Volume 15.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增969张（+101.7% vs前日OI），连续性待观察（方向未知）
10-16 275.0C — Vol 1,852 | 最新价 $10.30 | OI 1290→2117 (ΔOI +827张) | ΔOI/Volume 44.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增827张（+64.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,647 张（Put 0 / Call 6,647），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 43.8k / P 44.9k，今日成交量: C 8.3k / P 4.1k，平值价格ATM: C $2.65 / P $3.02 ｜ ATM IV 95.5%，预期波动 ±2.1%，Max Pain 280
Top ΔOI: C 300 +2,492 ｜ C 285 +1,304 ｜ C 295 +1,055

📆 Forward Expiration Structure

10-16  C +5.4k / P +3.5k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +0.7k / P +1.4k ｜ Activity MEDIUM △ ｜ 14D
10-30  C +0.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
11-06  C +1.0k / P +1.3k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 86.7k / P 96.8k，今日变化ΔOI: C +5.4k / P +3.5k，平值价格ATM: C $10.23 / P $10.32 ｜ ATM IV 64.7%，净 delta 敞口 281k shares
Top ΔOI: P 360 -1,205 ｜ C 275 +827 ｜ C 285 +689
仓位参考: Max Pain 270 ｜ Call Wall 270（-1.5%，弱）（OI 7.0k） ｜ Put Wall 260（-5.2%，弱）（OI 4.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.7%｜历史 Rank 58%（近端代理）｜IV/RV 0.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 281,219 股

10-23（MEDIUM △）Top ΔOI: 250P +490 ｜ 235P +227
10-23（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 300（+9.4%，弱）（OI 1.2k） ｜ Put Wall 250（-8.8%，弱）（OI 1.3k）

10-30（MEDIUM △）Top ΔOI: 320C +463 ｜ 210P -341
10-30（MEDIUM △）仓位参考: Max Pain 280 ｜ Call Wall 300（+9.4%，弱）（OI 1.5k） ｜ Put Wall 285（+3.9%，弱）（OI 1.8k）

📆 11-06 Forward Structure
存量OI: C 4.0k / P 10.2k，今日变化ΔOI: C +1.0k / P +1.3k，平值价格ATM: C $23.20 / P $28.11 ｜ ATM IV 81.1%，净 delta 敞口 2k shares
Top ΔOI: C 355 +332 ｜ P 215 +186 ｜ P 220 +174
仓位参考: Max Pain 275 ｜ Call Wall 300（+9.4%，弱）（OI 0.2k） ｜ Put Wall 250（-8.8%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 81.1%｜历史 Rank 58%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 2,434 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/BE_morning.json