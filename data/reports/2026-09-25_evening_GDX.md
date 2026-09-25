# 期权晚报 2026-09-25（快照 16:40 ET）

📊 市场环境

SPY $771.35 ｜ QQQ $744.50
VIX 14.87 ↓5.1%（5D +0.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 95C ΔOI +3,407（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 92.44 → 收盘 92.87（+0.5%） ｜ 今日高 93.32 ｜ 低 91.34 ｜ 昨收 92.35 → 收盘 92.87（+0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.61 | OI比 0.57 | ATM IV 30.8% | Skew 13.6pp | Term 1.33 | ExpMove ±4.4%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常偏陡（Term 1.33）｜保护溢价显著（Skew 13.6pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.57）+ 当日成交偏 Put（P/C量 1.61）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.61×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±4.4% ｜ 10-09（14D）±6.4% ｜ 10-16（21D）±7.8% ｜ 10-23（28D）±8.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,552,895 | GEX Change vs 上次快照 1,782,453 | Flip: Primary Flip: 94.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 424 / LOW 110 / INVALID 328
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 94.30（全链重定价，覆盖 80%）
Put Wall 90（弱结构｜现价高于该位 3.2%）
最近结构参考: Flip 94（现价低于该位 1.5%）
量化视角： 负 Gamma（1455万，无历史分位）｜负 Gamma 缓解（+178万）｜现价位于 Flip 下方 1.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 93（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 94（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +5.9k / P +3.8k ｜ Activity HIGH ｜ 7D
10-09  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 14D
10-16  C +2.9k / P +3.4k ｜ Activity HIGH ｜ 21D
10-23  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 39.2k / P 43.2k，今日变化ΔOI: C +5.9k / P +3.8k，平值价格ATM: C $2.08 / P $2.03 ｜ ATM IV 38.8%，净 delta 敞口 173k shares
Top ΔOI: C 95 +3,407 ｜ P 86 +3,106 ｜ C 92 +957
仓位参考: Max Pain 97 ｜ Call Wall 95（+2.3%，弱）（OI 5.0k） ｜ Put Wall 97（+4.4%，弱）（OI 8.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.8%｜历史 Rank 15%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 173,287 股

📆 10-09 Forward Structure
存量OI: C 5.8k / P 9.6k，今日变化ΔOI: C +0.4k / P +0.5k，平值价格ATM: C $2.92 / P $3.01 ｜ ATM IV 40.3%，净 delta 敞口 690 shares
Top ΔOI: P 90 +122 ｜ P 85 +97
仓位参考: Max Pain 94 ｜ Call Wall 94（+1.2%，弱）（OI 0.7k） ｜ Put Wall 90（-3.1%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 40.3%｜历史 Rank 15%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 690 股

📆 10-16 Forward Structure
存量OI: C 94.0k / P 100.4k，今日变化ΔOI: C +2.9k / P +3.4k，平值价格ATM: C $3.75 / P $3.53 ｜ ATM IV 40.2%，净 delta 敞口 61k shares
Top ΔOI: P 80 +2,525 ｜ C 100 +1,572 ｜ C 105 +989
仓位参考: Max Pain 93 ｜ Call Wall 95（+2.3%，弱）（OI 6.0k） ｜ Put Wall 90（-3.1%，弱）（OI 10.0k）
量化解读： 存量两侧均衡｜ATM IV 40.2%｜历史 Rank 15%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 61,024 股

10-23（MEDIUM △）Top ΔOI: 92C +63 ｜ 93C +49
10-23（MEDIUM △）仓位参考: Max Pain 95 ｜ Call Wall 96.5（+3.9%，弱）（OI 0.8k） ｜ Put Wall 93（+0.1%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/GDX_evening.json