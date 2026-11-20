# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $709.44 ｜ QQQ $630.54
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 380C ΔOI +4,390（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 374.41 → 今开 370.22（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 373.88 ｜ 低 363.46

Options: P/C成交量 0.67 | OI比 1.41 | ATM IV 59.3% | Skew -54.1pp | Term 0.90 | ExpMove ±4.1%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -54.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±4.1% ｜ 11-25（5D）±5.7% ｜ 11-27（7D）±6.0% ｜ 12-04（14D）±9.8%
   ⇒ IV–VIX Spread: +31.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -53,711,106 | GEX Change vs 上次快照 -50,335,358 | Flip: Primary Flip: 367.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1112 / LOW 321 / INVALID 156
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 367.18（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 9.0%）
最近结构参考: Flip 367（现价低于该位 0.8%）
量化视角： 负 Gamma（5371万，无历史分位）｜负 Gamma 加深（5034万）｜现价位于 Flip 下方 0.84%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 375（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 367（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 390.0C — Vol 144 | 最新价 $0.84 | OI 6940→12997 (ΔOI +6057张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6057张（+87.3% vs前日OI），连续性待观察（方向未知）
11-27 380.0C — Vol 2 | 最新价 $8.65 | OI 1263→5653 (ΔOI +4390张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4390张（+347.6% vs前日OI），连续性待观察（方向未知）
11-27 390.0C — Vol 10 | 最新价 $4.85 | OI 1494→5798 (ΔOI +4304张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4304张（+288.1% vs前日OI），连续性待观察（方向未知）
11-27 395.0C — Vol 5,799 | 最新价 $3.55 | OI 1727→5965 (ΔOI +4238张) | ΔOI/Volume 73.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4238张（+245.4% vs前日OI），连续性待观察（方向未知）
11-27 382.5C — Vol 5,276 | 最新价 $7.60 | OI 702→4490 (ΔOI +3788张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3788张（+539.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,777 张（Put 0 / Call 22,777），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 378.6k / P 532.5k，今日成交量: C 128.0k / P 85.8k，平值价格ATM: C $7.80 / P $1.31 ｜ ATM IV 59.3%，预期波动 ±2.5%，Max Pain 375
Top ΔOI: C 410 -6,800 ｜ C 397 -6,433 ｜ C 390 +6,057

📆 Forward Expiration Structure

11-23  C +6.1k / P +4.1k ｜ Activity HIGH ｜ 3D
11-25  C +2.9k / P +1.8k ｜ Activity HIGH ｜ 5D
11-27  C +21.7k / P +6.0k ｜ Activity HIGH ｜ 7D
12-04  C +1.5k / P +2.6k ｜ Activity MEDIUM △ ｜ 14D

📆 11-23 Forward Structure
存量OI: C 32.2k / P 17.5k，今日变化ΔOI: C +6.1k / P +4.1k，平值价格ATM: C $10.82 / P $4.05 ｜ ATM IV 49.2%，净 delta 敞口 -86k shares
Top ΔOI: C 400 +891 ｜ P 342 +703
仓位参考: Max Pain 380 ｜ Call Wall 400（+9.9%，弱）（OI 2.2k） ｜ Put Wall 357.5（-1.8%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 49.2%｜历史 Rank 70%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 86,025 股

📆 11-25 Forward Structure
存量OI: C 7.9k / P 9.0k，今日变化ΔOI: C +2.9k / P +1.8k，平值价格ATM: C $14.25 / P $6.52 ｜ ATM IV 53.9%，净 delta 敞口 -18k shares
Top ΔOI: C 400 +530 ｜ P 330 +393
仓位参考: Max Pain 385 ｜ Call Wall 400（+9.9%）（OI 1.1k） ｜ Put Wall 382.5（+5.1%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.9%｜历史 Rank 70%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 负 17,570 股

📆 11-27 Forward Structure
存量OI: C 87.2k / P 66.4k，今日变化ΔOI: C +21.7k / P +6.0k，平值价格ATM: C $14.70 / P $7.25 ｜ ATM IV 52.9%，净 delta 敞口 372k shares
Top ΔOI: C 380 +4,390 ｜ C 390 +4,304 ｜ C 395 +4,238
仓位参考: Max Pain 375 ｜ Call Wall 395（+8.5%，弱）（OI 6.0k） ｜ Put Wall 350（-3.9%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 52.9%｜历史 Rank 70%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 371,627 股

12-04（MEDIUM △）Top ΔOI: 220C +295 ｜ 385P +286
12-04（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 400（+9.9%，弱）（OI 5.1k） ｜ Put Wall 380（+4.4%，弱）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/TSLA_morning.json