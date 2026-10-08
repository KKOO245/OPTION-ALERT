# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.91
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 55C ΔOI +1,383（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 53.82 → 今开 53.34（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 53.58 ｜ 低 53.30

Options: P/C成交量 0.56 | OI比 0.31 | ATM IV 33.9% | Skew 0.4pp | Term 0.99 | ExpMove ±1.6%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.6% ｜ 10-12（4D）±2.2% ｜ 10-14（6D）±3.3% ｜ 10-16（8D）±3.8%
   ⇒ IV–VIX Spread: +18.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,518,230 | GEX Change vs 上次快照 5,382,873 | Flip: Primary Flip: 53.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 699 / LOW 124 / INVALID 403
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 53.63（全链重定价，覆盖 97%）
Put Wall 50（弱结构｜现价高于该位 6.8%）
最近结构参考: Flip 54（现价低于该位 0.4%）
量化视角： 负 Gamma（652万，无历史分位）｜负 Gamma 缓解（+538万）｜现价位于 Flip 下方 0.42%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 59.5C — Vol 2,888 | 最新价 $0.38 | OI 1331→4138 (ΔOI +2807张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2807张（+210.9% vs前日OI），连续性待观察（方向未知）
11-06 63.0P — Vol 1,562 | 最新价 $9.43 | OI 21→1583 (ΔOI +1562张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1562张（+7438.1% vs前日OI），连续性待观察（方向未知）
10-09 55.5C — Vol 4,239 | 最新价 $0.12 | OI 2198→3581 (ΔOI +1383张) | ΔOI/Volume 32.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1383张（+62.9% vs前日OI），连续性待观察（方向未知）
10-09 55.0C — Vol 4,841 | 最新价 $0.20 | OI 3788→5145 (ΔOI +1357张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1357张（+35.8% vs前日OI），连续性待观察（方向未知）
10-09 54.5C — Vol 2,866 | 最新价 $0.32 | OI 507→1819 (ΔOI +1312张) | ΔOI/Volume 45.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1312张（+258.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,421 张（Put 1,562 / Call 6,859），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +6.7k / P +3.1k ｜ Activity HIGH ｜ 1D
10-12  C +1.0k / P +1.5k ｜ Activity HIGH ｜ 4D
10-14  C +0.7k / P +1.8k ｜ Activity HIGH ｜ 6D
10-16  C -3.2k / P -9.9k ｜ Activity HIGH ｜ 8D

📆 10-09 Forward Structure
存量OI: C 99.4k / P 30.4k，今日变化ΔOI: C +6.7k / P +3.1k，平值价格ATM: C $0.40 / P $0.47 ｜ ATM IV 33.9%，净 delta 敞口 204k shares
Top ΔOI: C 55 +1,383 ｜ C 55 +1,357 ｜ C 54 +1,312
仓位参考: Max Pain 55 ｜ Call Wall 55（+3.0%，弱）（OI 5.1k） ｜ Put Wall 55（+3.0%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 33.9%｜历史 Rank 54%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 204,478 股

📆 10-12 Forward Structure
存量OI: C 5.8k / P 9.1k，今日变化ΔOI: C +1.0k / P +1.5k，平值价格ATM: C $0.55 / P $0.64 ｜ ATM IV 25.9%，净 delta 敞口 -76k shares
Top ΔOI: P 57 +681 ｜ C 57 +353 ｜ C 54 +285
仓位参考: Max Pain 56 ｜ Call Wall 57.5（+7.7%，弱）（OI 0.7k） ｜ Put Wall 54（+1.1%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 25.9%｜历史 Rank 54%（近端代理）｜IV/RV 0.78×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 75,912 股

📆 10-14 Forward Structure
存量OI: C 6.9k / P 5.7k，今日变化ΔOI: C +0.7k / P +1.8k，平值价格ATM: C $0.87 / P $0.87 ｜ ATM IV 30.1%，净 delta 敞口 -66k shares
Top ΔOI: P 55 +321 ｜ P 52 +237 ｜ P 49 +226
仓位参考: Max Pain 56 ｜ Call Wall 58.5（+9.5%，弱）（OI 0.5k） ｜ Put Wall 53.5（+0.2%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.1%｜历史 Rank 54%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 负 65,606 股

📆 10-16 Forward Structure
存量OI: C 482.4k / P 197.7k，今日变化ΔOI: C -3.2k / P -9.9k，平值价格ATM: C $0.98 / P $1.03 ｜ ATM IV 31.3%，净 delta 敞口 697k shares
Top ΔOI: P 53 -9,827
仓位参考: Max Pain 56 ｜ Call Wall 50（-6.4%，弱）（OI 27.0k） ｜ Put Wall 50（-6.4%，弱）（OI 23.1k）
量化解读： 存量 Call 重｜ATM IV 31.3%｜历史 Rank 54%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 697,017 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 33.9% vs 10-12 25.9%（差 +8.1pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SLV_morning.json