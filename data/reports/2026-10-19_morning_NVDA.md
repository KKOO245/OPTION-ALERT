# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.16
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 220C ΔOI +4,659（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 230C ΔOI +1,650 占该期限总 OI 11.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 214.13 → 今开 218.01（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 218.03 ｜ 低 214.70

Options: P/C成交量 0.65 | OI比 0.67 | ATM IV 45.0% | Skew 3.3pp | Term 0.88 | ExpMove ±2.5%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-21（2D）±2.5% ｜ 10-23（4D）±3.3% ｜ 10-26（7D）±3.8% ｜ 10-28（9D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 96,843,684 | GEX Change vs 上次快照 80,007,199 | Flip: Primary Flip: 212.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 742 / LOW 197 / INVALID 569
结构观察区: Primary Flip 212.12（全链重定价，覆盖 97%）
Call Wall 230（弱结构｜现价低于该位 6.4%）
最近结构参考: Flip 212（现价高于该位 1.5%）
量化视角： 正 Gamma（9684万，无历史分位）｜正 Gamma 增强（+8001万）｜现价位于 Flip 上方 1.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 218（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 212（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 220.0C — Vol 64,056 | 最新价 $1.95 | OI 12338→45215 (ΔOI +32877张) | ΔOI/Volume 51.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32877张（+266.5% vs前日OI），连续性待观察（方向未知）
10-23 222.5C — Vol 45,650 | 最新价 $1.31 | OI 3184→35808 (ΔOI +32624张) | ΔOI/Volume 71.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32624张（+1024.6% vs前日OI），连续性待观察（方向未知）
10-23 230.0C — Vol 55,043 | 最新价 $0.32 | OI 17632→47405 (ΔOI +29773张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29773张（+168.9% vs前日OI），连续性待观察（方向未知）
10-23 227.5C — Vol 47,310 | 最新价 $0.51 | OI 13531→41548 (ΔOI +28017张) | ΔOI/Volume 59.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28017张（+207.1% vs前日OI），连续性待观察（方向未知）
10-23 105.0P — Vol 26,309 | 最新价 $0.01 | OI 908→19135 (ΔOI +18227张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18227张（+2007.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 141,518 张（Put 18,227 / Call 123,291），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 108.0k / P 72.7k，今日成交量: C 134.4k / P 87.4k，平值价格ATM: C $1.19 / P $0.91 ｜ ATM IV 45.0%，预期波动 ±1.0%，Max Pain 218
Top ΔOI: P 197 +5,719 ｜ C 220 +5,012 ｜ C 222 +4,090

📆 Forward Expiration Structure

10-21  C +22.8k / P +15.5k ｜ Activity HIGH ｜ 2D
10-23  C +144.8k / P +127.7k ｜ Activity HIGH ｜ 4D
10-26  C +5.1k / P +6.1k ｜ Activity HIGH ｜ 7D
10-28  C +2.7k / P +5.0k ｜ Activity HIGH ｜ 9D

📆 10-21 Forward Structure
存量OI: C 62.0k / P 41.6k，今日变化ΔOI: C +22.8k / P +15.5k，平值价格ATM: C $2.87 / P $2.48 ｜ ATM IV 39.9%，净 delta 敞口 -70k shares
Top ΔOI: C 220 +4,659 ｜ P 217 +3,411 ｜ C 222 +2,740
仓位参考: Max Pain 220 ｜ Call Wall 230（+6.9%，弱）（OI 7.7k） ｜ Put Wall 200（-7.1%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜ATM IV 39.9%｜历史 Rank 58%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 69,666 股

📆 10-23 Forward Structure
存量OI: C 381.9k / P 315.0k，今日变化ΔOI: C +144.8k / P +127.7k，平值价格ATM: C $3.80 / P $3.39 ｜ ATM IV 38.8%，净 delta 敞口 1.9M shares
Top ΔOI: C 220 +32,877 ｜ C 222 +32,624 ｜ C 230 +29,773
仓位参考: Max Pain 220 ｜ Call Wall 230（+6.9%，弱）（OI 47.4k） ｜ Put Wall 220（+2.2%，弱）（OI 14.9k）
量化解读： 存量 Call 重｜ATM IV 38.8%｜历史 Rank 58%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,898,897 股

📆 10-26 Forward Structure
存量OI: C 22.5k / P 12.0k，今日变化ΔOI: C +5.1k / P +6.1k，平值价格ATM: C $4.28 / P $3.90 ｜ ATM IV 33.8%，净 delta 敞口 46k shares
Top ΔOI: P 210 +1,154 ｜ P 212 +1,051 ｜ P 202 +1,035
仓位参考: Max Pain 215 ｜ Call Wall 225（+4.5%，弱）（OI 2.2k） ｜ Put Wall 200（-7.1%）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.8%｜历史 Rank 58%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 46,382 股

📆 10-28 Forward Structure
存量OI: C 7.8k / P 7.2k，今日变化ΔOI: C +2.7k / P +5.0k，平值价格ATM: C $5.10 / P $4.54 ｜ ATM IV 35.3%，净 delta 敞口 -71k shares
Top ΔOI: C 230 +1,650 ｜ P 215 +1,548
仓位参考: Max Pain 220 ｜ Call Wall 230（+6.9%）（OI 4.7k） ｜ Put Wall 215（-0.1%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.3%｜历史 Rank 58%（近端代理）｜IV/RV 1.49×（近似）｜净 delta 敞口 负 71,056 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/NVDA_morning.json