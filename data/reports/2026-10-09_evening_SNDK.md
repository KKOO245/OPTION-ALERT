# 期权晚报 2026-10-09（快照 16:40 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 14.84 ↓3.7%（5D -3.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 1600C ΔOI +142（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 1649.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,633.33 → 收盘 1,581.82（-3.2%） ｜ 今日高 1637.95 ｜ 低 1575.69 ｜ 昨收 1,609.46 → 收盘 1,581.82（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-14，窗口结束前不做对错判定）

Options: P/C成交量 0.65 | OI比 0.78 | ATM IV 63.3% | Skew 4.9pp | Term 1.02 | ExpMove ±5.8%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 1.02）｜保护溢价中性（Skew 4.9pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±5.8% ｜ 10-23（14D）±8.4% ｜ 10-30（21D）±12.5% ｜ 11-06（28D）±14.0%
   ⇒ IV–VIX Spread: +48.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,230,363 | GEX Change vs 上次快照 -2,111,079 | Flip: Candidates 1649.71 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 1522 / LOW 415 / INVALID 1233
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈1650（全链重定价，覆盖 78%，CONDITIONAL）
Put Wall 1,500（弱结构｜现价高于该位 5.5%）
最近结构参考: Flip 1650（现价低于该位 4.1%）
量化视角： 负 Gamma（723万，无历史分位）｜负 Gamma 加深（211万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构）；上方 1,640（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1650（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +2.8k / P +3.0k ｜ Activity HIGH ｜ 7D
10-23  C +1.6k / P +0.8k ｜ Activity HIGH ｜ 14D
10-30  C +1.2k / P +0.9k ｜ Activity HIGH ｜ 21D
11-06  C +0.5k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 52.6k / P 59.0k，今日变化ΔOI: C +2.8k / P +3.0k，平值价格ATM: C $47.76 / P $44.00 ｜ ATM IV 53.0%，净 delta 敞口 44k shares
Top ΔOI: C 1900 +474 ｜ P 1640 +411
仓位参考: Max Pain 1,660 ｜ Call Wall 1700（+7.5%，弱）（OI 1.5k） ｜ Put Wall 1500（-5.2%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜ATM IV 53.0%｜历史 Rank 20%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 44,412 股

📆 10-23 Forward Structure
存量OI: C 12.3k / P 12.3k，今日变化ΔOI: C +1.6k / P +0.8k，平值价格ATM: C $68.67 / P $65.00 ｜ ATM IV 53.5%，净 delta 敞口 10k shares
Top ΔOI: C 2300 +518 ｜ C 1650 +173 ｜ C 1600 +142
仓位参考: Max Pain 1,695 ｜ Call Wall 1700（+7.5%，弱）（OI 0.4k） ｜ Put Wall 1500（-5.2%）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 53.5%｜历史 Rank 20%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 9,623 股

📆 10-30 Forward Structure
存量OI: C 8.3k / P 11.3k，今日变化ΔOI: C +1.2k / P +0.9k，平值价格ATM: C $102.67 / P $95.01 ｜ ATM IV 65.0%，净 delta 敞口 11k shares
Top ΔOI: C 1650 +167 ｜ C 1700 +151
仓位参考: Max Pain 1,700 ｜ Call Wall 1700（+7.5%，弱）（OI 0.6k） ｜ Put Wall 1500（-5.2%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.0%｜历史 Rank 20%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,650 股

📆 11-06 Forward Structure
存量OI: C 3.1k / P 3.8k，今日变化ΔOI: C +0.5k / P +0.9k，平值价格ATM: C $116.00 / P $105.96 ｜ ATM IV 64.8%，净 delta 敞口 -8k shares
Top ΔOI: P 1400 +286 ｜ P 1640 +94 ｜ P 1770 +79
仓位参考: Max Pain 1,675 ｜ Call Wall 1560（-1.4%，弱）（OI 0.1k） ｜ Put Wall 1500（-5.2%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 64.8%｜历史 Rank 20%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 7,957 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SNDK_evening.json