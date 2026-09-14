# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.01
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -3.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-16 220C ΔOI +2,760（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 218.29 → 今开 211.08（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 211.70 ｜ 低 208.93

Options: P/C成交量 1.01 | OI比 0.69 | ATM IV 49.3% | Skew 2.6pp | Term 0.69 | ExpMove ±2.6%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-16（2D）±2.6% ｜ 09-18（4D）±3.4% ｜ 09-21（7D）±3.7% ｜ 09-23（9D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 10,712,763 | GEX Change vs 上次快照 -243,844,675 | Flip: Primary Flip: 210.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 681 / LOW 208 / INVALID 649
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 210.33（全链重定价，覆盖 98%）
Put Wall 200（弱结构｜现价高于该位 5.4%）
最近结构参考: Flip 210（现价高于该位 0.2%）
量化视角： 正 Gamma（1071万，无历史分位）｜正 Gamma 减弱（2.44亿）｜现价位于 Flip 上方 0.18%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 232.5C — Vol 30,535 | 最新价 $0.27 | OI 10792→32348 (ΔOI +21556张) | ΔOI/Volume 70.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21556张（+199.7% vs前日OI），连续性待观察（方向未知）
09-18 225.0C — Vol 91,251 | 最新价 $1.22 | OI 56693→77122 (ΔOI +20429张) | ΔOI/Volume 22.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20429张（+36.0% vs前日OI），连续性待观察（方向未知）
09-14 225.0C — Vol 51,741 | 最新价 $0.12 | OI 8953→24892 (ΔOI +15939张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15939张（+178.0% vs前日OI），连续性待观察（方向未知）
09-14 222.5C — Vol 51,851 | 最新价 $0.30 | OI 2416→9667 (ΔOI +7251张) | ΔOI/Volume 14.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7251张（+300.1% vs前日OI），连续性待观察（方向未知）
09-18 235.0C — Vol 19,851 | 最新价 $0.16 | OI 48172→55384 (ΔOI +7212张) | ΔOI/Volume 36.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7212张（+15.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 72,387 张（Put 0 / Call 72,387），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 107.3k / P 74.5k，今日成交量: C 165.0k / P 166.0k，平值价格ATM: C $1.50 / P $0.81 ｜ ATM IV 49.3%，预期波动 ±1.1%，Max Pain 220
Top ΔOI: C 225 +15,939 ｜ C 222 +7,251 ｜ C 220 +4,663

📆 Forward Expiration Structure

09-16  C +15.3k / P +17.6k ｜ Activity HIGH ｜ 2D
09-18  C +65.0k / P +37.1k ｜ Activity HIGH ｜ 4D
09-21  C +2.5k / P +1.7k ｜ Activity HIGH ｜ 7D
09-23  C +1.3k / P +0.4k ｜ Activity HIGH ｜ 9D

📆 09-16 Forward Structure
存量OI: C 56.7k / P 38.6k，今日变化ΔOI: C +15.3k / P +17.6k，平值价格ATM: C $3.11 / P $2.31 ｜ ATM IV 40.4%，净 delta 敞口 -668k shares
Top ΔOI: C 220 +2,760 ｜ C 230 +2,585
仓位参考: Max Pain 220
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 667,881 股

📆 09-18 Forward Structure
存量OI: C 1272.2k / P 1064.8k，今日变化ΔOI: C +65.0k / P +37.1k，平值价格ATM: C $4.00 / P $3.10 ｜ ATM IV 38.9%，净 delta 敞口 -997k shares
Top ΔOI: C 232 +21,556 ｜ C 225 +20,429
仓位参考: Max Pain 205 ｜ Call Wall 230（+9.2%，弱）（OI 94.9k）
量化解读： 存量 Call 重｜ATM IV 38.9%｜历史 Rank 69%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 997,229 股

📆 09-21 Forward Structure
存量OI: C 16.3k / P 17.7k，今日变化ΔOI: C +2.5k / P +1.7k，平值价格ATM: C $4.40 / P $3.45 ｜ ATM IV 33.2%，净 delta 敞口 -61k shares
Top ΔOI: C 225 +829 ｜ P 212 +484 ｜ C 227 +381
仓位参考: Max Pain 218
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.2%｜历史 Rank 69%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 负 60,961 股

📆 09-23 Forward Structure
存量OI: C 11.1k / P 3.1k，今日变化ΔOI: C +1.3k / P +0.4k，平值价格ATM: C $4.97 / P $4.15 ｜ ATM IV 34.1%，净 delta 敞口 2k shares
Top ΔOI: C 230 +554 ｜ C 225 +157 ｜ C 227 +113
仓位参考: Max Pain 225 ｜ Call Wall 230（+9.2%）（OI 4.4k） ｜ Put Wall 225（+6.8%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 34.1%｜历史 Rank 69%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 1,731 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/NVDA_morning.json