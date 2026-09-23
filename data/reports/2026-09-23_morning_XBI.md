# 期权晨报 2026-09-23（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $742.16
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 36.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　⏰ 今日
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 161.87 → 今开 161.94（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 162.68 ｜ 低 159.44

Options: P/C成交量 2.27 | OI比 3.66 | ATM IV 33.1% | Skew 1.8pp | Term 0.92 | ExpMove ±3.5%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 1.8pp）｜当日成交偏 Put（P/C量 2.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.66×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±3.5% ｜ 10-02（9D）±4.5% ｜ 10-09（16D）±1.5% ｜ 10-16（23D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,283,984 | GEX Change vs 上次快照 0 | Flip: Primary Flip: 163.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 370 / LOW 66 / INVALID 332
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.24（全链重定价，覆盖 94%）
最近结构参考: Flip 163（现价低于该位 0.8%）
量化视角： 负 Gamma（528万，无历史分位）｜负 Gamma 加深（0万）｜现价位于 Flip 下方 0.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-25 Forward Structure
存量OI: C 11.8k / P 43.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.77 / P $4.82 ｜ ATM IV 33.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 157 ｜ Call Wall 160（-1.2%，弱）（OI 2.7k） ｜ Put Wall 156（-3.6%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 33.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 165（+1.9%）（OI 1.0k） ｜ Put Wall 157（-3.0%，弱）（OI 0.2k）

10-09（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 172（+6.3%，弱）（OI 38）

10-16（Activity LOW）仓位参考: Max Pain 165 ｜ Call Wall 170（+5.0%，弱）（OI 5.0k） ｜ Put Wall 153（-5.5%，弱）（OI 6.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/XBI_morning.json