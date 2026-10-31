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


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 761.38 → 收盘 755.72（-0.7%） ｜ 今日高 761.46 ｜ 低 750.36 ｜ 昨收 769.36 → 收盘 755.72（-1.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 1.26 | OI比 1.68 | ATM IV 12.2% | Skew 1.2pp | Term 1.25 | ExpMove ±0.9%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常偏陡（Term 1.25）｜保护溢价薄（Skew 1.2pp）｜当日成交偏 Put（P/C量 1.26）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.68×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 26% ｜ P/C OI(近端) 37%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 26%）｜近端持仓结构中性（P/C OI 分位 37%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-02（3D）±0.9% ｜ 11-03（4D）±1.2% ｜ 11-04（5D）±1.5% ｜ 11-05（6D）±1.7%
   ⇒ IV–VIX Spread: -7.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,395,906,308 | GEX Change vs 上次快照 480,506,283 | Flip: Primary Flip: 775.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2433 / LOW 170 / INVALID 1099
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 775.15（全链重定价，覆盖 99%）
最近结构参考: Flip 775（现价低于该位 2.5%）
量化视角： 负 Gamma（13.96亿，历史分位 26%，中性区）｜负 Gamma 缓解（+4.81亿）｜现价位于 Flip 下方 2.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 772（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-03  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-05  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-02 Forward Structure
存量OI: C 68.4k / P 115.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.89 / P $2.96 ｜ ATM IV 12.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 772 ｜ Call Wall 774（+2.4%，弱）（OI 4.8k） ｜ Put Wall 775（+2.6%）（OI 15.3k）
量化解读： 存量 Put 重｜ATM IV 12.2%｜历史 Rank 45%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-03（Activity LOW）仓位参考: Max Pain 769 ｜ Call Wall 770（+1.9%，弱）（OI 2.7k） ｜ Put Wall 740（-2.1%，弱）（OI 6.2k）

11-04（Activity LOW）仓位参考: Max Pain 769 ｜ Call Wall 776（+2.7%，弱）（OI 4.0k） ｜ Put Wall 767（+1.5%）（OI 37.0k）

11-05（Activity LOW）仓位参考: Max Pain 765 ｜ Put Wall 760（+0.6%，弱）（OI 2.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SPY_evening.json