# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.78 ｜ QQQ $756.20
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-06 760P ΔOI +4,086（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 787C ΔOI +232,391 占该期限总 OI 20.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 769.64 → 今开 769.69（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 772.82 ｜ 低 769.69

Options: P/C成交量 0.84 | OI比 1.49 | ATM IV 14.0% | Skew 1.9pp | Term 0.94 | ExpMove ±0.5%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.49×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 59% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 59%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-06（1D）±0.5% ｜ 10-07（2D）±0.7% ｜ 10-08（3D）±0.9% ｜ 10-09（4D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 158,157,256 | GEX Change vs 上次快照 208,184,300 | Flip: Primary Flip: 770.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2438 / LOW 339 / INVALID 2239
结构观察区: Primary Flip 770.48（全链重定价，覆盖 96%）
Call Wall 787（弱结构｜现价低于该位 2.0%）
最近结构参考: Flip 770（现价高于该位 0.1%）
量化视角： 正 Gamma（1.58亿，历史分位 59%，中性区）｜由负转正（+2.08亿）｜现价位于 Flip 上方 0.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 768（MaxPain，仅结算参考）；上方 787（Call Wall，弱结构）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 787.0C — Vol 246,654 | 最新价 $0.21 | OI 1714→234105 (ΔOI +232391张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增232391张（+13558.4% vs前日OI），连续性待观察（方向未知）
10-09 590.0P — Vol 77,324 | 最新价 $0.02 | OI 291→68924 (ΔOI +68633张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增68633张（+23585.2% vs前日OI），连续性待观察（方向未知）
10-16 560.0P — Vol 19,377 | 最新价 $0.03 | OI 318→19595 (ΔOI +19277张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19277张（+6061.9% vs前日OI），连续性待观察（方向未知）
10-16 739.0P — Vol 18,539 | 最新价 $0.89 | OI 3348→20361 (ΔOI +17013张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17013张（+508.1% vs前日OI），连续性待观察（方向未知）
10-16 565.0P — Vol 17,553 | 最新价 $0.03 | OI 973→17802 (ΔOI +16829张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16829张（+1729.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 354,143 张（Put 121,752 / Call 232,391），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 176.9k / P 264.2k，今日成交量: C 516.0k / P 435.4k，平值价格ATM: C $1.23 / P $1.10 ｜ ATM IV 14.0%，预期波动 ±0.3%，Max Pain 768
Top ΔOI: P 726 +14,578 ｜ C 772 +12,328 ｜ P 760 +8,338

📆 Forward Expiration Structure

10-06  C +15.9k / P +26.8k ｜ Activity HIGH ｜ 1D
10-07  C +14.9k / P +33.0k ｜ Activity HIGH ｜ 2D
10-08  C +22.7k / P +12.9k ｜ Activity HIGH ｜ 3D
10-09  C +281.1k / P +89.8k ｜ Activity HIGH ｜ 4D

📆 10-06 Forward Structure
存量OI: C 155.5k / P 87.7k，今日变化ΔOI: C +15.9k / P +26.8k，平值价格ATM: C $2.18 / P $1.99 ｜ ATM IV 11.5%，净 delta 敞口 -115k shares
Top ΔOI: P 760 +4,086 ｜ P 769 +2,439 ｜ P 750 +2,371
仓位参考: Max Pain 768 ｜ Put Wall 760（-1.4%，弱）（OI 7.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 11.5%｜历史 Rank 59%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 负 115,393 股

📆 10-07 Forward Structure
存量OI: C 123.5k / P 113.5k，今日变化ΔOI: C +14.9k / P +33.0k，平值价格ATM: C $2.90 / P $2.67 ｜ ATM IV 11.4%，净 delta 敞口 -87k shares
Top ΔOI: P 725 +5,251 ｜ P 726 +5,182 ｜ P 760 -4,038
仓位参考: Max Pain 768 ｜ Put Wall 760（-1.4%，弱）（OI 5.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 11.4%｜历史 Rank 59%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 86,911 股

📆 10-08 Forward Structure
存量OI: C 46.8k / P 61.5k，今日变化ΔOI: C +22.7k / P +12.9k，平值价格ATM: C $3.48 / P $3.17 ｜ ATM IV 11.4%，净 delta 敞口 -69k shares
Top ΔOI: C 795 +6,483 ｜ C 796 +6,197 ｜ C 785 +2,669
仓位参考: Max Pain 766 ｜ Call Wall 785（+1.8%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.4%｜历史 Rank 59%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 68,764 股

📆 10-09 Forward Structure
存量OI: C 655.8k / P 494.3k，今日变化ΔOI: C +281.1k / P +89.8k，平值价格ATM: C $4.21 / P $3.57 ｜ ATM IV 11.6%，净 delta 敞口 263k shares
Top ΔOI: C 787 +232,391 ｜ P 590 +68,633 ｜ P 725 -32,472
仓位参考: Max Pain 767 ｜ Call Wall 787（+2.1%）（OI 234.1k） ｜ Put Wall 767（-0.5%，弱）（OI 46.6k）
量化解读： 存量 Call 重｜ATM IV 11.6%｜历史 Rank 59%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 262,763 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SPY_morning.json