# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-12 54C ΔOI +1,657（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 53.45 → 今开 54.90（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 55.24 ｜ 低 54.79

Options: P/C成交量 0.38 | OI比 0.27 | ATM IV 37.9% | Skew -0.7pp | Term 0.86 | ExpMove ±1.8%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.27×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-12（3D）±1.8% ｜ 10-14（5D）±3.0% ｜ 10-16（7D）±3.5% ｜ 10-19（10D）±3.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,295,551 | GEX Change vs 上次快照 79,046,998 | Flip: Primary Flip: 52.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 722 / LOW 170 / INVALID 334
结构观察区: Primary Flip 52.99（全链重定价，覆盖 95%）
Put Wall 50（弱结构｜现价高于该位 10.0%） | Call Wall 60（现价低于该位 8.3%）
最近结构参考: Flip 53（现价高于该位 3.8%）
量化视角： 正 Gamma（7430万，无历史分位）｜由负转正（+7905万）｜现价位于 Flip 上方 3.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 54（MaxPain，仅结算参考）；上方 60（Call Wall）。
• Gamma 区域：切换参考 53（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 53.5C — Vol 9,389 | 最新价 $0.44 | OI 792→3892 (ΔOI +3100张) | ΔOI/Volume 33.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3100张（+391.4% vs前日OI），连续性待观察（方向未知）
10-09 54.0C — Vol 6,952 | 最新价 $0.26 | OI 1796→3973 (ΔOI +2177张) | ΔOI/Volume 31.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2177张（+121.2% vs前日OI），连续性待观察（方向未知）
10-12 54.0C — Vol 2,029 | 最新价 $0.42 | OI 124→1781 (ΔOI +1657张) | ΔOI/Volume 81.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1657张（+1336.3% vs前日OI），连续性待观察（方向未知）
10-16 55.0C — Vol 5,594 | 最新价 $0.51 | OI 20077→21690 (ΔOI +1613张) | ΔOI/Volume 28.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1613张（+8.0% vs前日OI），连续性待观察（方向未知）
10-09 54.5C — Vol 3,935 | 最新价 $0.13 | OI 1819→3226 (ΔOI +1407张) | ΔOI/Volume 35.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1407张（+77.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,954 张（Put 0 / Call 9,954），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 107.4k / P 28.9k，今日成交量: C 16.1k / P 6.1k，平值价格ATM: C $0.23 / P $0.23 ｜ ATM IV 37.9%，预期波动 ±0.8%，Max Pain 54
Top ΔOI: C 53 +3,100 ｜ C 54 +2,177 ｜ C 54 +1,407

📆 Forward Expiration Structure

10-12  C +7.0k / P +1.2k ｜ Activity HIGH ｜ 3D
10-14  C +1.1k / P +1.6k ｜ Activity HIGH ｜ 5D
10-16  C -4.0k / P -4.0k ｜ Activity HIGH ｜ 7D
10-19  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 10D

📆 10-12 Forward Structure
存量OI: C 12.8k / P 10.3k，今日变化ΔOI: C +7.0k / P +1.2k，平值价格ATM: C $0.49 / P $0.49 ｜ ATM IV 23.5%，净 delta 敞口 346k shares
Top ΔOI: C 54 +1,657 ｜ C 55 +999 ｜ C 54 +883
仓位参考: Max Pain 54 ｜ Call Wall 54（-1.8%，弱）（OI 1.8k） ｜ Put Wall 54（-1.8%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 23.5%｜历史 Rank 62%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 346,496 股

📆 10-14 Forward Structure
存量OI: C 8.0k / P 7.3k，今日变化ΔOI: C +1.1k / P +1.6k，平值价格ATM: C $0.85 / P $0.78 ｜ ATM IV 30.0%，净 delta 敞口 46k shares
Top ΔOI: C 53 +322 ｜ P 50 +267
仓位参考: Max Pain 55 ｜ Call Wall 60（+9.1%，弱）（OI 0.9k） ｜ Put Wall 53.5（-2.7%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.0%｜历史 Rank 62%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,488 股

📆 10-16 Forward Structure
存量OI: C 478.4k / P 193.7k，今日变化ΔOI: C -4.0k / P -4.0k，平值价格ATM: C $0.97 / P $0.94 ｜ ATM IV 31.1%，净 delta 敞口 646k shares
Top ΔOI: P 63 -2,295 ｜ C 55 +1,613
仓位参考: Max Pain 56 ｜ Call Wall 60（+9.1%，弱）（OI 56.5k） ｜ Put Wall 60（+9.1%，弱）（OI 31.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.1%｜历史 Rank 62%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 645,819 股

📆 10-19 Forward Structure
存量OI: C 1.9k / P 0.9k，今日变化ΔOI: C +0.6k / P +0.2k，平值价格ATM: C $1.11 / P $1.03 ｜ ATM IV 28.4%，净 delta 敞口 32k shares
Top ΔOI: C 54 +180 ｜ C 56 +151 ｜ C 55 +93
仓位参考: Max Pain 54 ｜ Call Wall 54（-1.8%，弱）（OI 0.3k） ｜ Put Wall 55.5（+0.9%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 28.4%｜历史 Rank 62%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 32,402 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SLV_morning.json