# 期权晚报 2026-11-27（快照 21:00 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 725.86 → 收盘 728.32（+0.3%） ｜ 今日高 729.15 ｜ 低 719.62 ｜ 昨收 716.70 → 收盘 728.32（+1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.99 | OI比 1.73 | ATM IV 16.0% | Skew 3.7pp | Term 1.21 | ExpMove ±1.2%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构正常偏陡（Term 1.21）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.73×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 48% ｜ P/C OI(近端) 41%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 48%）｜近端持仓结构中性（P/C OI 分位 41%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-30（3D）±1.2% ｜ 12-01（4D）±1.6% ｜ 12-02（5D）±1.9% ｜ 12-03（6D）±2.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -339,193,035 | GEX Change vs 上次快照 129,638,319 | Flip: Primary Flip: 734.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2929 / LOW 417 / INVALID 1828
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 734.88（全链重定价，覆盖 97%）
最近结构参考: Flip 735（现价低于该位 0.9%）
量化视角： 负 Gamma（3.39亿，历史分位 48%，中性区）｜负 Gamma 缓解（+1.30亿）｜现价位于 Flip 下方 0.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 727（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 735（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
12-01  C +0 / P +0 ｜ Activity LOW ｜ 4D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-03  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-30 Forward Structure
存量OI: C 420.2k / P 728.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.39 / P $4.21 ｜ ATM IV 16.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 727 ｜ Call Wall 750（+3.0%，弱）（OI 13.2k） ｜ Put Wall 727（-0.2%，弱）（OI 16.2k）
量化解读： 存量 Put 重｜ATM IV 16.0%｜历史 Rank 67%（近端代理）｜IV/RV 0.51×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

12-01（Activity LOW）仓位参考: Max Pain 718 ｜ Call Wall 724（-0.6%，弱）（OI 4.6k） ｜ Put Wall 720（-1.1%，弱）（OI 2.2k）

12-02（Activity LOW）仓位参考: Max Pain 710 ｜ Call Wall 715（-1.8%）（OI 9.0k）

12-03（Activity LOW）仓位参考: Max Pain 715 ｜ Call Wall 725（-0.5%，弱）（OI 1.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SPY_evening.json