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
🟡 **近现价集中开仓**: 10-07 56C ΔOI +647（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 54.74 → 今开 55.60（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 55.61 ｜ 低 55.06

Options: P/C成交量 0.91 | OI比 0.60 | ATM IV 35.0% | Skew 3.0pp | Term 0.97 | ExpMove ±2.1%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 3.0pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.91×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-07（2D）±2.1% ｜ 10-09（4D）±2.9% ｜ 10-12（7D）±3.2% ｜ 10-14（9D）±4.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 41,709,513 | GEX Change vs 上次快照 27,149,931 | Flip: Primary Flip: 54.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 701 / LOW 130 / INVALID 411
结构观察区: Primary Flip 54.12（全链重定价，覆盖 98%）
Put Wall 60（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 54（现价高于该位 2.2%）
量化视角： 正 Gamma（4171万，无历史分位）｜正 Gamma 增强（+2715万）｜现价位于 Flip 上方 2.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（MaxPain，仅结算参考）；上方 60（Put Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-05 56.5C — Vol 5,043 | 最新价 $0.04 | OI 457→4892 (ΔOI +4435张) | ΔOI/Volume 87.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4435张（+970.5% vs前日OI），连续性待观察（方向未知）
11-06 60.0C — Vol 5,300 | 最新价 $0.69 | OI 2434→5844 (ΔOI +3410张) | ΔOI/Volume 64.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3410张（+140.1% vs前日OI），连续性待观察（方向未知）
10-07 51.5P — Vol 2,799 | 最新价 $0.06 | OI 301→2824 (ΔOI +2523张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2523张（+838.2% vs前日OI），连续性待观察（方向未知）
10-16 60.0C — Vol 3,756 | 最新价 $0.14 | OI 53242→55713 (ΔOI +2471张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2471张（+4.6% vs前日OI），连续性待观察（方向未知）
10-05 52.0P — Vol 2,130 | 最新价 $0.01 | OI 1262→3167 (ΔOI +1905张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1905张（+150.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,744 张（Put 4,428 / Call 10,316），跨 4 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 19.9k / P 11.8k，今日成交量: C 18.5k / P 16.7k，平值价格ATM: C $0.11 / P $0.36 ｜ ATM IV 35.0%，预期波动 ±0.8%，Max Pain 55
Top ΔOI: C 56 +4,435 ｜ P 52 +1,905 ｜ C 56 +1,380

📆 Forward Expiration Structure

10-07  C +3.7k / P +4.3k ｜ Activity HIGH ｜ 2D
10-09  C +9.2k / P +4.9k ｜ Activity HIGH ｜ 4D
10-12  C +0.5k / P +0.3k ｜ Activity HIGH ｜ 7D
10-14  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 9D

📆 10-07 Forward Structure
存量OI: C 22.3k / P 11.5k，今日变化ΔOI: C +3.7k / P +4.3k，平值价格ATM: C $0.46 / P $0.68 ｜ ATM IV 32.5%，净 delta 敞口 97k shares
Top ΔOI: P 51 +2,523 ｜ C 56 +647
仓位参考: Max Pain 55 ｜ Call Wall 58（+4.9%，弱）（OI 3.1k） ｜ Put Wall 51.5（-6.8%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.5%｜历史 Rank 56%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 96,921 股

📆 10-09 Forward Structure
存量OI: C 82.7k / P 23.3k，今日变化ΔOI: C +9.2k / P +4.9k，平值价格ATM: C $0.71 / P $0.88 ｜ ATM IV 32.6%，净 delta 敞口 79k shares
Top ΔOI: C 58 +1,831 ｜ P 54 +1,073
仓位参考: Max Pain 56 ｜ Call Wall 60（+8.5%，弱）（OI 5.0k） ｜ Put Wall 55（-0.5%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 32.6%｜历史 Rank 56%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 79,046 股

📆 10-12 Forward Structure
存量OI: C 2.2k / P 4.2k，今日变化ΔOI: C +0.5k / P +0.3k，平值价格ATM: C $0.81 / P $0.97 ｜ ATM IV 28.5%，净 delta 敞口 12k shares
Top ΔOI: P 50 +104 ｜ C 57 +97 ｜ C 56 +68
仓位参考: Max Pain 55 ｜ Call Wall 58（+4.9%，弱）（OI 0.4k） ｜ Put Wall 54（-2.3%）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.5%｜历史 Rank 56%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,995 股

10-14（MEDIUM △）Top ΔOI: 56C +99 ｜ 57C +98
10-14（MEDIUM △）仓位参考: Max Pain 55 ｜ Call Wall 58（+4.9%，弱）（OI 0.4k） ｜ Put Wall 55（-0.5%）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SLV_morning.json