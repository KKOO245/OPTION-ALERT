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
🟡 **近现价集中开仓**: 11-04 210P ΔOI +1,452（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 187P ΔOI +14,746 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 208.88 → 收盘 204.64（-2.0%） ｜ 今日高 209.05 ｜ 低 200.92 ｜ 昨收 213.66 → 收盘 204.64（-4.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.88 | OI比 0.63 | ATM IV 41.3% | Skew -0.2pp | Term 1.09 | ExpMove ±2.3%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构正常（Term 1.09）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.3% ｜ 11-04（5D）±3.8% ｜ 11-06（7D）±4.5% ｜ 11-09（10D）±5.1%
   ⇒ IV–VIX Spread: +21.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -61,514,383 | GEX Change vs 上次快照 -64,628,890 | Flip: Primary Flip: 208.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 632 / LOW 190 / INVALID 586
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 208.15（全链重定价，覆盖 87%）
Put Wall 190（弱结构｜现价高于该位 7.7%）
最近结构参考: Flip 208（现价低于该位 1.7%）
量化视角： 负 Gamma（6151万，无历史分位）｜由正转负（6463万）｜现价位于 Flip 下方 1.69%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构）；上方 212（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 208（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +11.0k / P +36.6k ｜ Activity HIGH ｜ 3D
11-04  C +5.2k / P +5.5k ｜ Activity HIGH ｜ 5D
11-06  C +49.6k / P +4.8k ｜ Activity HIGH ｜ 7D
11-09  C +0.9k / P +0.6k ｜ Activity HIGH ｜ 10D

📆 11-02 Forward Structure
存量OI: C 38.5k / P 68.4k，今日变化ΔOI: C +11.0k / P +36.6k，平值价格ATM: C $2.21 / P $2.46 ｜ ATM IV 30.9%，净 delta 敞口 -105k shares
Top ΔOI: P 187 +14,746 ｜ P 190 +7,107 ｜ P 185 +7,105
仓位参考: Max Pain 212 ｜ Call Wall 220（+7.5%，弱）（OI 6.6k） ｜ Put Wall 187.5（-8.4%，弱）（OI 14.9k）
量化解读： 存量 Put 重｜ATM IV 30.9%｜历史 Rank 46%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 105,111 股

📆 11-04 Forward Structure
存量OI: C 20.1k / P 17.6k，今日变化ΔOI: C +5.2k / P +5.5k，平值价格ATM: C $3.85 / P $3.90 ｜ ATM IV 40.1%，净 delta 敞口 -225k shares
Top ΔOI: P 210 +1,452 ｜ C 220 +1,280 ｜ C 217 +1,263
仓位参考: Max Pain 215 ｜ Call Wall 225（+9.9%）（OI 4.0k） ｜ Put Wall 212.5（+3.8%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.1%｜历史 Rank 46%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 224,996 股

📆 11-06 Forward Structure
存量OI: C 165.6k / P 164.7k，今日变化ΔOI: C +49.6k / P +4.8k，平值价格ATM: C $4.65 / P $4.60 ｜ ATM IV 41.0%，净 delta 敞口 1.1M shares
Top ΔOI: C 225 +16,296 ｜ C 217 +13,166 ｜ C 215 +7,439
仓位参考: Max Pain 215 ｜ Call Wall 225（+9.9%）（OI 26.8k） ｜ Put Wall 200（-2.3%）（OI 13.7k）
量化解读： 存量两侧均衡｜ATM IV 41.0%｜历史 Rank 46%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,079,848 股

📆 11-09 Forward Structure
存量OI: C 3.3k / P 2.3k，今日变化ΔOI: C +0.9k / P +0.6k，平值价格ATM: C $5.15 / P $5.25 ｜ ATM IV 37.8%，净 delta 敞口 -13k shares
Top ΔOI: C 225 +326 ｜ C 215 +234 ｜ P 195 +100
仓位参考: Max Pain 215 ｜ Call Wall 225（+9.9%，弱）（OI 0.8k） ｜ Put Wall 215（+5.1%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 37.8%｜历史 Rank 46%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 负 13,239 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/NVDA_evening.json