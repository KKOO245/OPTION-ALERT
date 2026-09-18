# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 760P ΔOI -56,090（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 754.05 → 今开 763.15（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 763.41 ｜ 低 759.96

Options: P/C成交量 1.02 | OI比 1.74 | ATM IV 13.5% | Skew 2.2pp | Term 0.94 | ExpMove ±0.7%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 2.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 41%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端持仓结构中性（P/C OI 分位 41%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-18（1D）±0.7% ｜ 09-21（4D）±0.9% ｜ 09-22（5D）±1.1% ｜ 09-23（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -916,438,754 | GEX Change vs 上次快照 1,337,607,051 | Flip: Primary Flip: 764.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 3162 / LOW 446 / INVALID 1712
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 764.69（全链重定价，覆盖 93%）
Call Wall 800（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 765（现价低于该位 0.5%）
量化视角： 负 Gamma（9.16亿，历史分位 35%，中性区）｜负 Gamma 缓解（+13.38亿）｜现价位于 Flip 下方 0.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 755（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 765（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 730.0P — Vol 94,968 | 最新价 $1.83 | OI 35915→129515 (ΔOI +93600张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增93600张（+260.6% vs前日OI），连续性待观察（方向未知）
09-25 745.0P — Vol 93,256 | 最新价 $4.37 | OI 58544→149776 (ΔOI +91232张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增91232张（+155.8% vs前日OI），连续性待观察（方向未知）
09-25 780.0C — Vol 31,271 | 最新价 $0.16 | OI 6455→30707 (ΔOI +24252张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24252张（+375.7% vs前日OI），连续性待观察（方向未知）
09-30 780.0C — Vol 19,145 | 最新价 $0.37 | OI 16972→31205 (ΔOI +14233张) | ΔOI/Volume 74.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14233张（+83.9% vs前日OI），连续性待观察（方向未知）
09-18 666.0P — Vol 16,543 | 最新价 $0.04 | OI 1256→15269 (ΔOI +14013张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14013张（+1115.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 237,330 张（Put 198,845 / Call 38,485），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $57M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 160.6k / P 278.8k，今日成交量: C 1475.5k / P 1507.3k，平值价格ATM: C $0.97 / P $1.06 ｜ ATM IV 13.5%，预期波动 ±0.3%，Max Pain 755
Top ΔOI: P 730 +13,306 ｜ P 715 +12,465 ｜ C 760 +12,236

📆 Forward Expiration Structure

09-18  C +64.0k / P -82.8k ｜ Activity HIGH ｜ 1D
09-21  C +19.9k / P +22.7k ｜ Activity HIGH ｜ 4D
09-22  C +17.8k / P +15.7k ｜ Activity HIGH ｜ 5D
09-23  C +23.8k / P +11.6k ｜ Activity HIGH ｜ 6D

📆 09-18 Forward Structure
存量OI: C 1320.6k / P 3938.7k，今日变化ΔOI: C +64.0k / P -82.8k，平值价格ATM: C $1.73 / P $3.42 ｜ ATM IV 13.1%，净 delta 敞口 6.5M shares
Top ΔOI: P 760 -56,090 ｜ P 750 -39,471 ｜ P 745 -22,088
仓位参考: Max Pain 755 ｜ Call Wall 790（+3.8%，弱）（OI 58.5k） ｜ Put Wall 740（-2.7%，弱）（OI 97.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.1%｜历史 Rank 55%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,463,809 股

📆 09-21 Forward Structure
存量OI: C 79.6k / P 89.0k，今日变化ΔOI: C +19.9k / P +22.7k，平值价格ATM: C $2.60 / P $4.23 ｜ ATM IV 10.3%，净 delta 敞口 409k shares
仓位参考: Max Pain 756 ｜ Call Wall 789（+3.7%，弱）（OI 6.9k） ｜ Put Wall 755（-0.8%）（OI 11.5k）
量化解读： 存量两侧均衡｜ATM IV 10.3%｜历史 Rank 55%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 409,124 股

📆 09-22 Forward Structure
存量OI: C 38.7k / P 38.6k，今日变化ΔOI: C +17.8k / P +15.7k，平值价格ATM: C $3.20 / P $4.80 ｜ ATM IV 10.8%，净 delta 敞口 66k shares
Top ΔOI: P 733 +5,605 ｜ P 750 +4,775 ｜ C 804 +3,062
仓位参考: Max Pain 759 ｜ Call Wall 804（+5.7%，弱）（OI 3.1k） ｜ Put Wall 733（-3.7%，弱）（OI 6.0k）
量化解读： 存量两侧均衡｜ATM IV 10.8%｜历史 Rank 55%（近端代理）｜净 delta 敞口 正 66,238 股

📆 09-23 Forward Structure
存量OI: C 40.8k / P 31.1k，今日变化ΔOI: C +23.8k / P +11.6k，平值价格ATM: C $3.79 / P $5.19 ｜ ATM IV 11.2%，净 delta 敞口 254k shares
Top ΔOI: C 808 +5,368 ｜ C 807 +5,344 ｜ P 685 +1,501
仓位参考: Max Pain 757 ｜ Call Wall 807（+6.1%，弱）（OI 5.4k） ｜ Put Wall 725（-4.7%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 11.2%｜历史 Rank 55%（近端代理）｜净 delta 敞口 正 254,052 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SPY_morning.json