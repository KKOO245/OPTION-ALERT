# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 52C ΔOI +1,802（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 51.70 → 收盘 52.12（+0.8%） ｜ 今日高 52.89 ｜ 低 51.55 ｜ 昨收 51.54 → 收盘 52.12（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.35 | OI比 0.54 | ATM IV 34.3% | Skew 2.8pp | Term 0.97 | ExpMove ±1.5%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 2.8pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-21（1D）±1.5% ｜ 10-23（3D）±2.4% ｜ 10-26（6D）±3.0% ｜ 10-28（8D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,195,167 | GEX Change vs 上次快照 5,575,265 | Flip: Primary Flip: 50.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 710 / LOW 126 / INVALID 420
结构观察区: Primary Flip 50.80（全链重定价，覆盖 98%）
Put Wall 50（弱结构｜现价高于该位 4.2%）
最近结构参考: Flip 51（现价高于该位 2.6%）
量化视角： 正 Gamma（5120万，无历史分位）｜正 Gamma 增强（+558万）｜现价位于 Flip 上方 2.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 51（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-21  C +5.4k / P +2.1k ｜ Activity HIGH ｜ 1D
10-23  C +3.0k / P -3.8k ｜ Activity HIGH ｜ 3D
10-26  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 6D
10-28  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 8D

📆 10-21 Forward Structure
存量OI: C 29.7k / P 16.0k，今日变化ΔOI: C +5.4k / P +2.1k，平值价格ATM: C $0.46 / P $0.31 ｜ ATM IV 34.3%，净 delta 敞口 277k shares
Top ΔOI: C 52 +1,802 ｜ P 51 +758 ｜ C 52 +716
仓位参考: Max Pain 51 ｜ Call Wall 54（+3.6%）（OI 5.3k） ｜ Put Wall 48（-7.9%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 34.3%｜历史 Rank 54%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 276,933 股

📆 10-23 Forward Structure
存量OI: C 67.7k / P 46.5k，今日变化ΔOI: C +3.0k / P -3.8k，平值价格ATM: C $0.71 / P $0.56 ｜ ATM IV 33.2%，净 delta 敞口 515k shares
Top ΔOI: P 58 -2,186 ｜ P 57 -1,650
仓位参考: Max Pain 53 ｜ Call Wall 57（+9.4%，弱）（OI 7.0k） ｜ Put Wall 50（-4.1%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 33.2%｜历史 Rank 54%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 515,360 股

📆 10-26 Forward Structure
存量OI: C 4.2k / P 3.4k，今日变化ΔOI: C +0.9k / P +0.3k，平值价格ATM: C $0.85 / P $0.69 ｜ ATM IV 28.1%，净 delta 敞口 17k shares
Top ΔOI: C 53 +339 ｜ C 52 +128 ｜ C 54 +79
仓位参考: Max Pain 50 ｜ Call Wall 50.5（-3.1%）（OI 1.5k） ｜ Put Wall 48（-7.9%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 28.1%｜历史 Rank 54%（近端代理）｜IV/RV 0.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 17,022 股

📆 10-28 Forward Structure
存量OI: C 2.1k / P 2.1k，今日变化ΔOI: C +0.4k / P +0.5k，平值价格ATM: C $1.09 / P $0.88 ｜ ATM IV 32.1%，净 delta 敞口 -3k shares
Top ΔOI: P 51 +135 ｜ C 52 +77 ｜ P 51 +74
仓位参考: Max Pain 52 ｜ Call Wall 55（+5.5%，弱）（OI 0.3k） ｜ Put Wall 48（-7.9%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 32.1%｜历史 Rank 54%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 负 3,076 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SLV_evening.json