# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.49
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 16C ΔOI +138（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 16.49 → 今开 15.98（-3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 16.00 ｜ 低 15.38

Options: P/C成交量 0.14 | OI比 0.33 | ATM IV 78.0% | Skew 4.7pp | Term 0.89 | ExpMove ±8.4%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价中性（Skew 4.7pp）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±8.4% ｜ 10-16（9D）±7.3% ｜ 10-23（16D）±11.1% ｜ 10-30（23D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,147,294 | GEX Change vs 上次快照 -470,814 | Flip: Primary Flip: 14.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 191 / LOW 87 / INVALID 150
结构观察区: Primary Flip 14.91（全链重定价，覆盖 96%）
Put Wall 15（弱结构｜现价高于该位 4.3%）
最近结构参考: Put Wall 15（现价高于该位 4.3%）
量化视角： 正 Gamma（115万，无历史分位）｜正 Gamma 减弱（47万）｜现价位于 Flip 上方 4.96%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 21.0C — Vol 1,118 | 最新价 $0.34 | OI 5→1122 (ΔOI +1117张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1117张（+22340.0% vs前日OI），连续性待观察（方向未知）
10-16 17.0C — Vol 2,735 | 最新价 $0.53 | OI 391→1111 (ΔOI +720张) | ΔOI/Volume 26.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增720张（+184.1% vs前日OI），连续性待观察（方向未知）
10-09 17.5C — Vol 738 | 最新价 $0.21 | OI 223→772 (ΔOI +549张) | ΔOI/Volume 74.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增549张（+246.2% vs前日OI），连续性待观察（方向未知）
10-16 18.0C — Vol 344 | 最新价 $0.35 | OI 863→1121 (ΔOI +258张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增258张（+29.9% vs前日OI），连续性待观察（方向未知）
10-09 17.0C — Vol 349 | 最新价 $0.28 | OI 314→499 (ΔOI +185张) | ΔOI/Volume 53.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增185张（+58.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,829 张（Put 0 / Call 2,829），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.3k / P +99 ｜ Activity HIGH ｜ 2D
10-16  C +1.1k / P -0.2k ｜ Activity HIGH ｜ 9D
10-23  C +0.2k / P +3 ｜ Activity MEDIUM △ ｜ 16D
10-30  C +0.1k / P -6 ｜ Activity MEDIUM △ ｜ 23D

📆 10-09 Forward Structure
存量OI: C 7.8k / P 2.6k，今日变化ΔOI: C +1.3k / P +99，平值价格ATM: C $1.20 / P $0.11 ｜ ATM IV 78.0%，净 delta 敞口 30k shares
Top ΔOI: C 17 +185 ｜ C 16 +138
仓位参考: Max Pain 16 ｜ Put Wall 15.5（-0.9%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 78.0%｜历史 Rank 7%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,559 股

📆 10-16 Forward Structure
存量OI: C 21.7k / P 5.5k，今日变化ΔOI: C +1.1k / P -0.2k，平值价格ATM: C $0.80 / P $0.35 ｜ ATM IV 72.3%，净 delta 敞口 54k shares
Top ΔOI: C 17 +720
仓位参考: Max Pain 18 ｜ Call Wall 17（+8.7%，弱）（OI 1.1k） ｜ Put Wall 15（-4.1%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 72.3%｜历史 Rank 7%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,478 股

10-23（MEDIUM △）Top ΔOI: 17C +65
10-23（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 16（+2.3%，弱）（OI 0.2k）

10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15（-4.1%，弱）（OI 89）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 78.0% vs 10-16 72.3%（差 +5.7pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/NNE_morning.json