# 期权晚报 2026-11-27（快照 16:40 ET）

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

🔍 重点速览
🟡 **近现价集中开仓**: 12-02 134C ΔOI +1,160（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-07 140C ΔOI +467 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 131.20 → 收盘 133.59（+1.8%） ｜ 今日高 134.44 ｜ 低 129.10 ｜ 昨收 127.44 → 收盘 133.59（+4.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.49 | OI比 0.44 | ATM IV 60.1% | Skew 10.0pp | Term 0.99 | ExpMove ±3.4%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 0.99）｜保护溢价显著（Skew 10.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±3.4% ｜ 12-02（5D）±5.4% ｜ 12-04（7D）±7.1% ｜ 12-07（10D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,198,556 | GEX Change vs 上次快照 8,413,958 | Flip: Primary Flip: 128.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 773 / LOW 177 / INVALID 980
结构观察区: Primary Flip 128.07（全链重定价，覆盖 86%）
最近结构参考: Flip 128（现价高于该位 4.3%）
量化视角： 正 Gamma（3920万，无历史分位）｜正 Gamma 增强（+841万）｜现价位于 Flip 上方 4.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 128（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 128（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +12.0k / P +27.2k ｜ Activity HIGH ｜ 3D
12-02  C +7.3k / P +4.0k ｜ Activity HIGH ｜ 5D
12-04  C +8.7k / P +8.0k ｜ Activity HIGH ｜ 7D
12-07  C +1.3k / P +0.8k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 38.1k / P 43.1k，今日变化ΔOI: C +12.0k / P +27.2k，平值价格ATM: C $2.05 / P $2.55 ｜ ATM IV 46.1%，净 delta 敞口 870k shares
仓位参考: Max Pain 125 ｜ Call Wall 140（+4.8%）（OI 6.6k）
量化解读： 存量两侧均衡｜ATM IV 46.1%｜历史 Rank 54%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 870,192 股

📆 12-02 Forward Structure
存量OI: C 17.8k / P 7.6k，今日变化ΔOI: C +7.3k / P +4.0k，平值价格ATM: C $3.38 / P $3.80 ｜ ATM IV 57.5%，净 delta 敞口 404k shares
Top ΔOI: C 134 +1,160 ｜ C 126 +956 ｜ C 135 +764
仓位参考: Max Pain 125 ｜ Call Wall 135（+1.1%，弱）（OI 1.8k） ｜ Put Wall 125（-6.4%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 57.5%｜历史 Rank 54%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 404,405 股

📆 12-04 Forward Structure
存量OI: C 124.3k / P 99.5k，今日变化ΔOI: C +8.7k / P +8.0k，平值价格ATM: C $4.50 / P $5.00 ｜ ATM IV 63.0%，净 delta 敞口 610k shares
Top ΔOI: P 110 +3,636 ｜ P 130 -2,163 ｜ P 119 +1,219
仓位参考: Max Pain 135 ｜ Call Wall 137（+2.6%，弱）（OI 10.5k） ｜ Put Wall 140（+4.8%，弱）（OI 11.7k）
量化解读： 存量 Call 重｜ATM IV 63.0%｜历史 Rank 54%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 610,213 股

📆 12-07 Forward Structure
存量OI: C 3.0k / P 1.6k，今日变化ΔOI: C +1.3k / P +0.8k，平值价格ATM: C $5.05 / P $12.32 ｜ ATM IV 61.3%，净 delta 敞口 57k shares
Top ΔOI: C 140 +467 ｜ C 125 +272
仓位参考: Max Pain 125 ｜ Call Wall 140（+4.8%）（OI 0.7k） ｜ Put Wall 130（-2.7%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 61.3%｜历史 Rank 54%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 57,278 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SPCX_evening.json