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
🔵 **Flip 状态**: CONDITIONAL（Candidates: 15.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 15.41 → 收盘 15.18（-1.5%） ｜ 今日高 15.54 ｜ 低 15.02 ｜ 昨收 15.38 → 收盘 15.18（-1.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-30，窗口结束前不做对错判定）

Options: P/C成交量 2.25 | OI比 0.52 | ATM IV 165.1% | Skew -11.7pp | Term 0.40 | ExpMove ±6.5%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.40，近月 IV 高于远月）｜Put 保护异常便宜（Skew -11.7pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.52）+ 当日成交偏 Put（P/C量 2.25）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±6.5% ｜ 10-09（14D）±9.7% ｜ 10-16（21D）±12.5% ｜ 10-23（28D）±15.5%
   ⇒ IV–VIX Spread: +150.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,594,502 | GEX Change vs 上次快照 1,507,064 | Flip: Candidates 15.67 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 74%（带内） ｜ IV 有效性: VALID 192 / LOW 66 / INVALID 184
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈16（全链重定价，覆盖 74%，CONDITIONAL）
Put Wall 15（现价高于该位 1.2%）
最近结构参考: Put Wall 15（现价高于该位 1.2%）
量化视角： 负 Gamma（159万，无历史分位）｜负 Gamma 缓解（+151万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 74%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.9k / P +1.6k ｜ Activity HIGH ｜ 7D
10-09  C +28 / P +0.5k ｜ Activity HIGH ｜ 14D
10-16  C +1.1k / P +0.4k ｜ Activity HIGH ｜ 21D
10-23  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 20.1k / P 10.7k，今日变化ΔOI: C +0.9k / P +1.6k，平值价格ATM: C $0.59 / P $0.39 ｜ ATM IV 60.6%，净 delta 敞口 -80k shares
Top ΔOI: P 16 +1,045 ｜ C 16 +397 ｜ C 16 +320
仓位参考: Max Pain 17 ｜ Put Wall 16（+5.4%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.6%｜历史 Rank 88%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 79,925 股

📆 10-09 Forward Structure
存量OI: C 6.4k / P 3.8k，今日变化ΔOI: C +28 / P +0.5k，平值价格ATM: C $0.87 / P $0.60 ｜ ATM IV 64.1%，净 delta 敞口 -28k shares
Top ΔOI: P 17 +293 ｜ P 16 +131
仓位参考: Max Pain 16 ｜ Put Wall 16（+5.4%）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 负 27,801 股

📆 10-16 Forward Structure
存量OI: C 38.5k / P 13.6k，今日变化ΔOI: C +1.1k / P +0.4k，平值价格ATM: C $1.09 / P $0.81 ｜ ATM IV 65.9%，净 delta 敞口 14k shares
Top ΔOI: P 15 +253
仓位参考: Max Pain 17 ｜ Put Wall 15（-1.2%）（OI 5.6k）
量化解读： 存量 Call 重｜ATM IV 65.9%｜历史 Rank 88%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 13,632 股

10-23（MEDIUM △）Top ΔOI: 14P +129
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（-1.2%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/USAR_evening.json