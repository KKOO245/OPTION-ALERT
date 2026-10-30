# 期权晚报 2026-10-30（快照 16:40 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 125P ΔOI +3,709（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 131.52 → 收盘 130.51（-0.8%） ｜ 今日高 134.51 ｜ 低 124.10 ｜ 昨收 141.62 → 收盘 130.51（-7.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 0.63 | ATM IV 87.9% | Skew 4.1pp | Term 0.86 | ExpMove ±9.5%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±9.5% ｜ 11-13（14D）±12.8% ｜ 11-20（21D）±15.0% ｜ 11-27（28D）±16.8%
   ⇒ IV–VIX Spread: +68.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,474,219 | GEX Change vs 上次快照 -4,445,737 | Flip: Primary Flip: 133.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 527 / LOW 91 / INVALID 320
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 133.97（全链重定价，覆盖 80%）
Call Wall 135（弱结构｜现价低于该位 3.3%）
最近结构参考: Flip 134（现价低于该位 2.6%）
量化视角： 负 Gamma（447万，无历史分位）｜负 Gamma 加深（445万）｜现价位于 Flip 下方 2.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 141（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +13.9k / P +14.3k ｜ Activity HIGH ｜ 7D
11-13  C +0.9k / P +4.5k ｜ Activity HIGH ｜ 14D
11-20  C +0.5k / P +2.8k ｜ Activity MEDIUM △ ｜ 21D
11-27  C +0.3k / P +2.4k ｜ Activity HIGH ｜ 28D

📆 11-06 Forward Structure
存量OI: C 43.0k / P 80.3k，今日变化ΔOI: C +13.9k / P +14.3k，平值价格ATM: C $5.90 / P $6.46 ｜ ATM IV 84.3%，净 delta 敞口 -296k shares
Top ΔOI: P 125 +3,709 ｜ P 118 +3,241 ｜ C 152 +2,664
仓位参考: Max Pain 150 ｜ Put Wall 125（-4.2%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 84.3%｜历史 Rank 64%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 296,023 股

📆 11-13 Forward Structure
存量OI: C 21.6k / P 51.3k，今日变化ΔOI: C +0.9k / P +4.5k，平值价格ATM: C $8.15 / P $8.55 ｜ ATM IV 80.6%，净 delta 敞口 -83k shares
Top ΔOI: P 105 +534 ｜ P 110 +531 ｜ P 100 +520
仓位参考: Max Pain 160 ｜ Put Wall 140（+7.3%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 80.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 82,593 股

11-20（MEDIUM △）Top ΔOI: 100P +556 ｜ 105P +533
11-20（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 135（+3.4%）（OI 42.4k） ｜ Put Wall 120（-8.1%，弱）（OI 6.2k）

📆 11-27 Forward Structure
存量OI: C 9.0k / P 17.2k，今日变化ΔOI: C +0.3k / P +2.4k，平值价格ATM: C $11.50 / P $10.45 ｜ ATM IV 75.3%，净 delta 敞口 -80k shares
Top ΔOI: P 95 +395 ｜ P 100 +349
仓位参考: Max Pain 155 ｜ Call Wall 140（+7.3%，弱）（OI 0.3k） ｜ Put Wall 140（+7.3%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 75.3%｜历史 Rank 64%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 80,010 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/MSTR_evening.json