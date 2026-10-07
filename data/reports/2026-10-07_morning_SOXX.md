# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.04 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 580P ΔOI +984（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 589.45 → 今开 576.72（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 579.77 ｜ 低 574.13

Options: P/C成交量 2.43 | OI比 1.97 | ATM IV 32.2% | Skew 6.1pp | Term 1.10 | ExpMove ±2.1%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常（Term 1.10）｜保护溢价显著（Skew 6.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.43×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.97×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.1% ｜ 10-16（9D）±4.1% ｜ 10-23（16D）±5.4% ｜ 10-30（23D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -1,348,700 | GEX Change vs 上次快照 -10,340,756 | Flip: Primary Flip: 578.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 509 / LOW 271 / INVALID 742
结构观察区: Primary Flip 578.90（全链重定价，覆盖 87%）
Call Wall 600（现价低于该位 3.8%）
最近结构参考: Flip 579（现价低于该位 0.3%）
量化视角： 负 Gamma（135万，无历史分位）｜由正转负（1034万）｜现价位于 Flip 下方 0.32%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 570（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 579（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 640.0C — Vol 1,445 | 最新价 $5.80 | OI 81→1364 (ΔOI +1283张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1283张（+1584.0% vs前日OI），连续性待观察（方向未知）
10-16 520.0P — Vol 1,004 | 最新价 $0.65 | OI 6290→7293 (ΔOI +1003张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1003张（+15.9% vs前日OI），连续性待观察（方向未知）
10-16 450.0P — Vol 1,021 | 最新价 $0.10 | OI 7615→8608 (ΔOI +993张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增993张（+13.0% vs前日OI），连续性待观察（方向未知）
10-09 580.0P — Vol 1,069 | 最新价 $3.10 | OI 172→1156 (ΔOI +984张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增984张（+572.1% vs前日OI），连续性待观察（方向未知）
10-16 605.0C — Vol 752 | 最新价 $6.40 | OI 105→839 (ΔOI +734张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增734张（+699.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,997 张（Put 2,980 / Call 2,017），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +71 / P +2.4k ｜ Activity HIGH ｜ 2D
10-16  C +0.6k / P +2.8k ｜ Activity HIGH ｜ 9D
10-23  C +17 / P +0.3k ｜ Activity MEDIUM △ ｜ 16D
10-30  C +1.3k / P +45 ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 5.7k / P 11.1k，今日变化ΔOI: C +71 / P +2.4k，平值价格ATM: C $5.90 / P $6.00 ｜ ATM IV 32.2%，净 delta 敞口 -114k shares
Top ΔOI: P 580 +984 ｜ P 577 +683
仓位参考: Max Pain 570 ｜ Put Wall 555（-3.8%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 32.2%｜历史 Rank 44%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 113,748 股

📆 10-16 Forward Structure
存量OI: C 40.1k / P 99.3k，今日变化ΔOI: C +0.6k / P +2.8k，平值价格ATM: C $12.00 / P $11.50 ｜ ATM IV 32.2%，净 delta 敞口 -37k shares
Top ΔOI: P 520 +1,003 ｜ C 605 +734
仓位参考: Max Pain 530 ｜ Call Wall 600（+4.0%）（OI 8.7k）
量化解读： 存量 Put 重｜ATM IV 32.2%｜历史 Rank 44%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 36,589 股

10-23（MEDIUM △）Top ΔOI: 560P +247
10-23（MEDIUM △）仓位参考: Max Pain 555 ｜ Call Wall 555（-3.8%，弱）（OI 92）

📆 10-30 Forward Structure
存量OI: C 5.7k / P 19.8k，今日变化ΔOI: C +1.3k / P +45，平值价格ATM: C $24.82 / P $0.00 ｜ ATM IV 34.7%，净 delta 敞口 12k shares
Top ΔOI: C 640 +1,283 ｜ P 590 +80
仓位参考: Max Pain 560 ｜ Put Wall 550（-4.7%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.7%｜历史 Rank 44%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 11,872 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SOXX_morning.json