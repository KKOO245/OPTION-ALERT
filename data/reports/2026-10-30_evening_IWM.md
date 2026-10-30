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
🟡 **近现价集中开仓**: 11-02 291C ΔOI +26,268（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 291C ΔOI +26,268 占该期限总 OI 40.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 281.97 → 收盘 279.33（-0.9%） ｜ 今日高 282.71 ｜ 低 276.91 ｜ 昨收 284.01 → 收盘 279.33（-1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.43 | OI比 2.08 | ATM IV 24.7% | Skew 9.0pp | Term 0.81 | ExpMove ±1.1%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 9.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.43×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.08×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±1.1% ｜ 11-03（4D）±1.5% ｜ 11-04（5D）±1.9% ｜ 11-05（6D）±2.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -518,373,824 | GEX Change vs 上次快照 -85,732,183 | Flip: Primary Flip: 287.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 1206 / LOW 162 / INVALID 914
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 287.25（全链重定价，覆盖 88%）
Put Wall 270（弱结构｜现价高于该位 3.5%） | Call Wall 285（弱结构｜现价低于该位 2.0%）
最近结构参考: Call Wall 285（现价低于该位 2.0%）
量化视角： 负 Gamma（5.18亿，无历史分位）｜负 Gamma 加深（8573万）｜现价位于 Flip 下方 2.76%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 280（MaxPain，仅结算参考） / 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 287（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +33.4k / P +4.7k ｜ Activity HIGH ｜ 3D
11-03  C +2.6k / P +1.3k ｜ Activity HIGH ｜ 4D
11-04  C +4.2k / P +4.5k ｜ Activity HIGH ｜ 5D
11-05  C +1.0k / P +4.1k ｜ Activity HIGH ｜ 6D

📆 11-02 Forward Structure
存量OI: C 46.5k / P 18.1k，今日变化ΔOI: C +33.4k / P +4.7k，平值价格ATM: C $1.96 / P $1.21 ｜ ATM IV 15.3%，净 delta 敞口 -221k shares
Top ΔOI: C 291 +26,268 ｜ C 288 +2,712 ｜ P 284 +1,283
仓位参考: Max Pain 280 ｜ Call Wall 291（+4.2%）（OI 26.3k） ｜ Put Wall 275（-1.6%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 15.3%｜历史 Rank 62%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 221,057 股

📆 11-03 Forward Structure
存量OI: C 12.2k / P 17.2k，今日变化ΔOI: C +2.6k / P +1.3k，平值价格ATM: C $2.39 / P $1.71 ｜ ATM IV 17.6%，净 delta 敞口 -64k shares
Top ΔOI: C 289 +1,046 ｜ P 270 -800 ｜ C 288 +556
仓位参考: Max Pain 279 ｜ Call Wall 282（+1.0%，弱）（OI 1.6k） ｜ Put Wall 270（-3.3%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.6%｜历史 Rank 62%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 64,339 股

📆 11-04 Forward Structure
存量OI: C 8.8k / P 15.2k，今日变化ΔOI: C +4.2k / P +4.5k，平值价格ATM: C $3.08 / P $2.33 ｜ ATM IV 20.4%，净 delta 敞口 -113k shares
Top ΔOI: C 291 +1,521 ｜ P 273 +1,376 ｜ P 272 +656
仓位参考: Max Pain 280 ｜ Call Wall 291（+4.2%）（OI 1.9k） ｜ Put Wall 280（+0.2%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 20.4%｜历史 Rank 62%（近端代理）｜净 delta 敞口 负 113,311 股

📆 11-05 Forward Structure
存量OI: C 6.0k / P 14.7k，今日变化ΔOI: C +1.0k / P +4.1k，平值价格ATM: C $3.37 / P $2.59 ｜ ATM IV 20.8%，净 delta 敞口 -153k shares
Top ΔOI: P 280 +701 ｜ P 281 +614 ｜ C 290 +480
仓位参考: Max Pain 280 ｜ Call Wall 280（+0.2%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 20.8%｜历史 Rank 62%（近端代理）｜净 delta 敞口 负 153,380 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/IWM_evening.json