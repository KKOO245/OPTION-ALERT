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
🟡 **近现价集中开仓**: 10-16 157C ΔOI +7,561（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 151.47 → 今开 154.37（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 157.60 ｜ 低 150.50

Options: P/C成交量 0.37 | OI比 0.94 | ATM IV 81.0% | Skew -6.5pp | Term 0.82 | ExpMove ±6.7%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.7% ｜ 10-23（14D）±9.3% ｜ 10-30（21D）±11.8% ｜ 11-06（28D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,050,154 | GEX Change vs 上次快照 17,292,789 | Flip: Primary Flip: 148.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 539 / LOW 117 / INVALID 286
结构观察区: Primary Flip 148.52（全链重定价，覆盖 92%）
Call Wall 160（弱结构｜现价低于该位 4.8%）
最近结构参考: Flip 149（现价高于该位 2.6%）
量化视角： 正 Gamma（2305万，无历史分位）｜正 Gamma 增强（+1729万）｜现价位于 Flip 上方 2.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 152（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 157.5C — Vol 9,723 | 最新价 $3.38 | OI 1280→8841 (ΔOI +7561张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7561张（+590.7% vs前日OI），连续性待观察（方向未知）
10-16 165.0C — Vol 10,200 | 最新价 $1.66 | OI 4149→10350 (ΔOI +6201张) | ΔOI/Volume 60.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6201张（+149.5% vs前日OI），连续性待观察（方向未知）
10-16 155.0C — Vol 11,027 | 最新价 $4.05 | OI 11350→17067 (ΔOI +5717张) | ΔOI/Volume 51.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5717张（+50.4% vs前日OI），连续性待观察（方向未知）
10-16 152.5C — Vol 6,653 | 最新价 $5.05 | OI 557→5465 (ΔOI +4908张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4908张（+881.1% vs前日OI），连续性待观察（方向未知）
10-16 162.5C — Vol 8,291 | 最新价 $2.15 | OI 2143→6948 (ΔOI +4805张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4805张（+224.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,192 张（Put 0 / Call 29,192），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 178.0k / P 167.8k，今日成交量: C 36.0k / P 13.4k，平值价格ATM: C $1.52 / P $1.18 ｜ ATM IV 81.0%，预期波动 ±1.8%，Max Pain 152
Top ΔOI: C 172 -12,425 ｜ C 165 -11,093 ｜ C 170 -8,012

📆 Forward Expiration Structure

10-16  C +19.5k / P +13.6k ｜ Activity HIGH ｜ 7D
10-23  C +4.4k / P +5.6k ｜ Activity MEDIUM △ ｜ 14D
10-30  C +2.5k / P +3.9k ｜ Activity HIGH ｜ 21D
11-06  C +0.4k / P +2.2k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 221.6k / P 201.8k，今日变化ΔOI: C +19.5k / P +13.6k，平值价格ATM: C $5.20 / P $5.00 ｜ ATM IV 58.5%，净 delta 敞口 -123k shares
Top ΔOI: C 95 -12,394 ｜ C 157 +7,561 ｜ C 165 +6,201
仓位参考: Max Pain 140 ｜ Call Wall 155（+1.7%，弱）（OI 17.1k） ｜ Put Wall 142（-6.8%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜ATM IV 58.5%｜历史 Rank 52%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 123,028 股

10-23（MEDIUM △）Top ΔOI: 150C +1,250 ｜ 149C +1,039
10-23（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 165（+8.3%，弱）（OI 2.4k） ｜ Put Wall 160（+5.0%）（OI 6.1k）

📆 10-30 Forward Structure
存量OI: C 29.3k / P 38.9k，今日变化ΔOI: C +2.5k / P +3.9k，平值价格ATM: C $8.85 / P $9.05 ｜ ATM IV 62.0%，净 delta 敞口 -30k shares
Top ΔOI: C 200 +1,252 ｜ C 195 +661 ｜ C 165 -571
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+6.7%，弱）（OI 2.6k） ｜ Put Wall 160（+5.0%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜ATM IV 62.0%｜历史 Rank 52%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 29,549 股

📆 11-06 Forward Structure
存量OI: C 8.5k / P 15.3k，今日变化ΔOI: C +0.4k / P +2.2k，平值价格ATM: C $11.05 / P $11.70 ｜ ATM IV 66.3%，净 delta 敞口 -66k shares
Top ΔOI: P 165 +535 ｜ P 120 +512
仓位参考: Max Pain 160 ｜ Call Wall 160（+5.0%）（OI 1.2k） ｜ Put Wall 160（+5.0%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 66.3%｜历史 Rank 52%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 66,444 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/MSTR_morning.json