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
🟡 **近现价集中开仓**: 10-16 45P ΔOI +562（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 46.14 → 今开 46.74（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 46.74 ｜ 低 45.42

Options: P/C成交量 0.43 | OI比 0.72 | ATM IV 76.7% | Skew -2.5pp | Term 0.83 | ExpMove ±6.1%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.1% ｜ 10-23（14D）±8.3% ｜ 10-30（21D）±11.5% ｜ 11-06（28D）±13.7%
   ⇒ IV–VIX Spread: +61.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,072,144 | GEX Change vs 上次快照 2,929,832 | Flip: Primary Flip: 47.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 233 / LOW 67 / INVALID 152
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.30（全链重定价，覆盖 91%）
Put Wall 45（现价高于该位 1.4%） | Call Wall 50（弱结构｜现价低于该位 8.7%）
最近结构参考: Put Wall 45（现价高于该位 1.4%）
量化视角： 负 Gamma（407万，无历史分位）｜负 Gamma 缓解（+293万）｜现价位于 Flip 下方 3.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall）；上方 47（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 47（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 45.5P — Vol 611 | 最新价 $1.09 | OI 201→763 (ΔOI +562张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增562张（+279.6% vs前日OI），连续性待观察（方向未知）
10-16 40.0P — Vol 383 | 最新价 $0.05 | OI 731→979 (ΔOI +248张) | ΔOI/Volume 64.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增248张（+33.9% vs前日OI），连续性待观察（方向未知）
10-09 45.0P — Vol 277 | 最新价 $0.13 | OI 1268→1447 (ΔOI +179张) | ΔOI/Volume 64.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增179张（+14.1% vs前日OI），连续性待观察（方向未知）
10-09 48.5C — Vol 174 | 最新价 $0.03 | OI 282→439 (ΔOI +157张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增157张（+55.7% vs前日OI），连续性待观察（方向未知）
10-09 47.5C — Vol 207 | 最新价 $0.07 | OI 360→503 (ΔOI +143张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增143张（+39.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,289 张（Put 989 / Call 300），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 11.9k / P 8.5k，今日成交量: C 0.3k / P 0.1k，平值价格ATM: C $0.43 / P $0.34 ｜ ATM IV 76.7%，预期波动 ±1.7%，Max Pain 47
Top ΔOI: P 45 -493 ｜ P 50 -275 ｜ C 50 -258

📆 Forward Expiration Structure

10-16  C +33 / P +0.9k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +0.2k / P +89 ｜ Activity LOW ｜ 14D
10-30  C +82 / P +0.1k ｜ Activity MEDIUM △ ｜ 21D
11-06  C +0.1k / P +48 ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 20.9k / P 18.1k，今日变化ΔOI: C +33 / P +0.9k，平值价格ATM: C $1.44 / P $1.33 ｜ ATM IV 52.0%，净 delta 敞口 -18k shares
Top ΔOI: P 45 +562 ｜ C 49 -78
仓位参考: Max Pain 50 ｜ Call Wall 50（+9.6%）（OI 4.5k） ｜ Put Wall 45（-1.4%，弱）（OI 4.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.0%｜历史 Rank 67%（近端代理）｜IV/RV 1.11×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 18,440 股

10-23（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50（+9.6%，弱）（OI 0.3k） ｜ Put Wall 45（-1.4%，弱）（OI 0.3k）

10-30（MEDIUM △）Top ΔOI: 50C +42
10-30（MEDIUM △）仓位参考: Max Pain 49 ｜ Call Wall 50（+9.6%，弱）（OI 0.4k） ｜ Put Wall 44（-3.6%）（OI 1.6k）

📆 11-06 Forward Structure
存量OI: C 1.2k / P 0.6k，今日变化ΔOI: C +0.1k / P +48，平值价格ATM: C $3.00 / P $3.27 ｜ ATM IV 63.4%，净 delta 敞口 -1k shares
仓位参考: Max Pain 47 ｜ Call Wall 47（+3.0%，弱）（OI 0.1k） ｜ Put Wall 45（-1.4%，弱）（OI 69）
量化解读： 存量 Call 重｜ATM IV 63.4%｜历史 Rank 67%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 负 1,432 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/MP_morning.json