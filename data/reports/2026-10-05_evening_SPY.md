# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-06 760P ΔOI +4,086（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 787C ΔOI +232,391 占该期限总 OI 20.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 769.69 → 收盘 774.83（+0.7%） ｜ 今日高 776.60 ｜ 低 769.69 ｜ 昨收 769.64 → 收盘 774.83（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.04 | OI比 1.49 | ATM IV 11.5% | Skew 0.8pp | Term 1.12 | ExpMove ±0.4%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 1.12）｜保护溢价薄（Skew 0.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.49×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 75% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 75%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-06（1D）±0.4% ｜ 10-07（2D）±0.6% ｜ 10-08（3D）±0.8% ｜ 10-09（4D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 924,190,998 | GEX Change vs 上次快照 766,033,742 | Flip: Primary Flip: 770.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2519 / LOW 387 / INVALID 2110
结构观察区: Primary Flip 770.92（全链重定价，覆盖 93%）
Call Wall 787（弱结构｜现价低于该位 1.5%）
最近结构参考: Flip 771（现价高于该位 0.5%）
量化视角： 正 Gamma（9.24亿，历史分位 75%，中性区）｜正 Gamma 增强（+7.66亿）｜现价位于 Flip 上方 0.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 768（MaxPain，仅结算参考）；上方 787（Call Wall，弱结构）。
• Gamma 区域：切换参考 771（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 787.0C — Vol 274,560 | 最新价 $0.29 | OI 1714→234105 (ΔOI +232391张) | ΔOI/Volume 84.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增232391张（+13558.4% vs前日OI），连续性待观察（方向未知）
10-09 590.0P — Vol 74 | 最新价 $0.01 | OI 291→68924 (ΔOI +68633张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增68633张（+23585.2% vs前日OI），连续性待观察（方向未知）
10-16 560.0P — Vol 19,377（Yahoo补） | 最新价 $0.03 | OI 318→19595 (ΔOI +19277张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19277张（+6061.9% vs前日OI），连续性待观察（方向未知）
10-16 739.0P — Vol 20,220 | 最新价 $0.51 | OI 3348→20361 (ΔOI +17013张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17013张（+508.1% vs前日OI），连续性待观察（方向未知）
10-16 565.0P — Vol 11 | 最新价 $0.03 | OI 973→17802 (ΔOI +16829张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16829张（+1729.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 354,143 张（Put 121,752 / Call 232,391），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-06  C +15.9k / P +26.8k ｜ Activity HIGH ｜ 1D
10-07  C +14.9k / P +33.0k ｜ Activity HIGH ｜ 2D
10-08  C +22.7k / P +12.9k ｜ Activity HIGH ｜ 3D
10-09  C +281.1k / P +89.8k ｜ Activity HIGH ｜ 4D

📆 10-06 Forward Structure
存量OI: C 155.5k / P 87.7k，今日变化ΔOI: C +15.9k / P +26.8k，平值价格ATM: C $1.52 / P $1.64 ｜ ATM IV 9.7%，净 delta 敞口 407k shares
Top ΔOI: P 760 +4,086 ｜ P 769 +2,439 ｜ P 750 +2,371
仓位参考: Max Pain 768 ｜ Put Wall 760（-1.9%，弱）（OI 7.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 9.7%｜历史 Rank 38%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 406,605 股

📆 10-07 Forward Structure
存量OI: C 123.5k / P 113.5k，今日变化ΔOI: C +14.9k / P +33.0k，平值价格ATM: C $2.31 / P $2.34 ｜ ATM IV 10.1%，净 delta 敞口 170k shares
Top ΔOI: P 725 +5,251 ｜ P 726 +5,182 ｜ P 760 -4,038
仓位参考: Max Pain 768 ｜ Put Wall 760（-1.9%，弱）（OI 5.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 10.1%｜历史 Rank 38%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 169,801 股

📆 10-08 Forward Structure
存量OI: C 46.8k / P 61.5k，今日变化ΔOI: C +22.7k / P +12.9k，平值价格ATM: C $2.94 / P $2.91 ｜ ATM IV 10.4%，净 delta 敞口 26k shares
Top ΔOI: C 795 +6,483 ｜ C 796 +6,197 ｜ C 785 +2,669
仓位参考: Max Pain 766 ｜ Call Wall 795（+2.6%，弱）（OI 6.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 10.4%｜历史 Rank 38%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 25,904 股

📆 10-09 Forward Structure
存量OI: C 655.8k / P 494.3k，今日变化ΔOI: C +281.1k / P +89.8k，平值价格ATM: C $3.68 / P $3.36 ｜ ATM IV 10.7%，净 delta 敞口 1.7M shares
Top ΔOI: C 787 +232,391 ｜ P 590 +68,633 ｜ P 725 -32,472
仓位参考: Max Pain 767 ｜ Call Wall 787（+1.6%）（OI 234.1k） ｜ Put Wall 767（-1.0%，弱）（OI 46.6k）
量化解读： 存量 Call 重｜ATM IV 10.7%｜历史 Rank 38%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 1,712,390 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SPY_evening.json