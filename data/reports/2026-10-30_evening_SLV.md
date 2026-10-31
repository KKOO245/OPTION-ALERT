# 期权晚报 2026-10-30（快照 21:00 ET）

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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 44.99 → 收盘 44.60（-0.9%） ｜ 今日高 45.06 ｜ 低 44.11 ｜ 昨收 47.28 → 收盘 44.60（-5.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.36 | OI比 0.87 | ATM IV 34.9% | Skew 4.5pp | Term 1.23 | ExpMove ±2.6%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常偏陡（Term 1.23）｜保护溢价中性（Skew 4.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.6% ｜ 11-04（5D）±4.3% ｜ 11-06（7D）±5.3% ｜ 11-09（10D）±6.4%
   ⇒ IV–VIX Spread: +15.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,140,144 | GEX Change vs 上次快照 4,716,795 | Flip: Primary Flip: 46.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 576 / LOW 102 / INVALID 358
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 46.97（全链重定价，覆盖 98%）
最近结构参考: Flip 47（现价低于该位 5.1%）
量化视角： 负 Gamma（2814万，无历史分位）｜负 Gamma 缓解（+472万）｜现价位于 Flip 下方 5.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 48（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 47（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-09  C +0 / P +0 ｜ Activity LOW ｜ 10D

📆 11-02 Forward Structure
存量OI: C 10.1k / P 8.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.63 / P $0.55 ｜ ATM IV 34.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 48 ｜ Call Wall 49（+9.9%，弱）（OI 1.0k） ｜ Put Wall 47.5（+6.5%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 34.9%｜历史 Rank 55%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-04（Activity LOW）仓位参考: Max Pain 48 ｜ Call Wall 48.5（+8.7%，弱）（OI 1.0k） ｜ Put Wall 44（-1.3%）（OI 2.2k）

11-06（Activity LOW）仓位参考: Max Pain 50 ｜ Put Wall 43（-3.6%，弱）（OI 3.5k）

11-09（Activity LOW）仓位参考: Max Pain 47 ｜ Call Wall 47（+5.4%，弱）（OI 0.3k） ｜ Put Wall 43（-3.6%）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SLV_evening.json