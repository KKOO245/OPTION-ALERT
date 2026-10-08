# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.87
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
🟡 **近现价集中开仓**: 10-12 785C ΔOI +2,202（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 777.22 → 今开 774.86（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 776.08 ｜ 低 774.45

Options: P/C成交量 0.86 | OI比 1.82 | ATM IV 13.8% | Skew 1.0pp | Term 0.93 | ExpMove ±0.6%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 0.93）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.82×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 56% ｜ P/C OI(近端) 49%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 56%）｜近端持仓结构中性（P/C OI 分位 49%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-09（1D）±0.6% ｜ 10-12（4D）±0.8% ｜ 10-13（5D）±0.9% ｜ 10-14（6D）±1.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -197,949 | GEX Change vs 上次快照 -466,785,611 | Flip: Primary Flip: 775.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2569 / LOW 412 / INVALID 1881
结构观察区: Primary Flip 775.30（全链重定价，覆盖 95%）
Call Wall 785（弱结构｜现价低于该位 1.2%）
最近结构参考: Flip 775（现价低于该位 0.0%）
量化视角： 负 Gamma（20万，历史分位 56%，中性区）｜由正转负（4.67亿）｜现价位于 Flip 下方 0.00%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 776（MaxPain，仅结算参考） / 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-08 738.0P — Vol 42,140 | 最新价 $0.01 | OI 980→37129 (ΔOI +36149张) | ΔOI/Volume 85.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36149张（+3688.7% vs前日OI），连续性待观察（方向未知）
10-08 739.0P — Vol 36,086 | 最新价 $0.01 | OI 744→34147 (ΔOI +33403张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33403张（+4489.6% vs前日OI），连续性待观察（方向未知）
10-30 765.0P — Vol 26,984 | 最新价 $4.68 | OI 4391→29703 (ΔOI +25312张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25312张（+576.5% vs前日OI），连续性待观察（方向未知）
10-30 740.0P — Vol 25,964 | 最新价 $1.59 | OI 81801→106842 (ΔOI +25041张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25041张（+30.6% vs前日OI），连续性待观察（方向未知）
10-09 710.0P — Vol 19,551 | 最新价 $0.02 | OI 2330→20337 (ΔOI +18007张) | ΔOI/Volume 92.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18007张（+772.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 137,912 张（Put 137,912 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $16M，买/卖方向不可观测）｜彩票/名义 3 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 185.1k / P 337.6k，今日成交量: C 507.6k / P 515.6k，平值价格ATM: C $1.42 / P $0.93 ｜ ATM IV 13.8%，预期波动 ±0.3%，Max Pain 776
Top ΔOI: P 738 +36,149 ｜ P 739 +33,403 ｜ C 778 +14,882

📆 Forward Expiration Structure

10-09  C +37.9k / P +78.9k ｜ Activity HIGH ｜ 1D
10-12  C +17.3k / P +10.2k ｜ Activity HIGH ｜ 4D
10-13  C +17.8k / P +22.3k ｜ Activity HIGH ｜ 5D
10-14  C +18.7k / P +20.2k ｜ Activity HIGH ｜ 6D

📆 10-09 Forward Structure
存量OI: C 558.2k / P 707.9k，今日变化ΔOI: C +37.9k / P +78.9k，平值价格ATM: C $2.58 / P $1.76 ｜ ATM IV 11.7%，净 delta 敞口 136k shares
Top ΔOI: P 710 +18,007 ｜ P 715 +17,223 ｜ P 725 -7,542
仓位参考: Max Pain 773 ｜ Call Wall 785（+1.3%）（OI 124.7k） ｜ Put Wall 767（-1.1%，弱）（OI 70.3k）
量化解读： 存量 Put 重｜ATM IV 11.7%｜历史 Rank 58%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 135,975 股

📆 10-12 Forward Structure
存量OI: C 65.1k / P 109.4k，今日变化ΔOI: C +17.3k / P +10.2k，平值价格ATM: C $3.34 / P $2.55 ｜ ATM IV 8.7%，净 delta 敞口 21k shares
Top ΔOI: C 785 +2,202
仓位参考: Max Pain 775 ｜ Call Wall 785（+1.3%，弱）（OI 5.3k） ｜ Put Wall 770（-0.7%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 8.7%｜历史 Rank 58%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,208 股

📆 10-13 Forward Structure
存量OI: C 45.7k / P 74.5k，今日变化ΔOI: C +17.8k / P +22.3k，平值价格ATM: C $3.90 / P $3.00 ｜ ATM IV 9.2%，净 delta 敞口 -98k shares
Top ΔOI: P 705 +4,039 ｜ C 790 +2,912 ｜ P 774 +2,808
仓位参考: Max Pain 776 ｜ Call Wall 790（+1.9%，弱）（OI 4.1k） ｜ Put Wall 774（-0.2%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 9.2%｜历史 Rank 58%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 97,700 股

📆 10-14 Forward Structure
存量OI: C 106.6k / P 70.3k，今日变化ΔOI: C +18.7k / P +20.2k，平值价格ATM: C $4.55 / P $3.78 ｜ ATM IV 10.2%，净 delta 敞口 88k shares
Top ΔOI: P 700 +9,669 ｜ C 790 +8,628 ｜ P 778 +2,504
仓位参考: Max Pain 775 ｜ Call Wall 790（+1.9%）（OI 79.8k） ｜ Put Wall 755（-2.6%，弱）（OI 5.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 10.2%｜历史 Rank 58%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 88,234 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SPY_morning.json