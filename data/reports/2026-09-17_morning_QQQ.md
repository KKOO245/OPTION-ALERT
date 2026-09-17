# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.88
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-18 700P ΔOI -24,151（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 704.72 → 今开 716.05（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 716.80 ｜ 低 713.32

Options: P/C成交量 1.21 | OI比 1.86 | ATM IV 17.9% | Skew 2.6pp | Term 0.97 | ExpMove ±0.8%（近端） | Rank 47%
量化视角： IV 中性（Rank 47%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 2.6pp）｜当日成交偏 Put（P/C量 1.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.86×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 72% ｜ P/C OI(近端) 67%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 72%）｜近端持仓结构中性（P/C OI 分位 67%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-18（1D）±0.8% ｜ 09-21（4D）±1.1% ｜ 09-22（5D）±1.4% ｜ 09-23（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 207,854,338 | GEX Change vs 上次快照 1,078,515,228 | Flip: Primary Flip: 713.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3115 / LOW 435 / INVALID 1792
结构观察区: Primary Flip 713.55（全链重定价，覆盖 94%）
Put Wall 690（弱结构｜现价高于该位 3.7%） | Call Wall 720（弱结构｜现价低于该位 0.6%）
最近结构参考: Flip 714（现价高于该位 0.3%）
量化视角： 正 Gamma（2.08亿，历史分位 72%，中性区）｜由负转正（+10.79亿）｜现价位于 Flip 上方 0.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 690（Put Wall，弱结构） / 708（MaxPain，仅结算参考）；上方 720（Call Wall，弱结构）。
• Gamma 区域：切换参考 714（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 721.0C — Vol 25,200 | 最新价 $3.42 | OI 275→25271 (ΔOI +24996张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24996张（+9089.5% vs前日OI），连续性待观察（方向未知）
09-25 690.0P — Vol 18,907 | 最新价 $3.96 | OI 78691→89603 (ΔOI +10912张) | ΔOI/Volume 57.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10912张（+13.9% vs前日OI），连续性待观察（方向未知）
09-25 700.0P — Vol 16,322 | 最新价 $6.60 | OI 8097→17678 (ΔOI +9581张) | ΔOI/Volume 58.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9581张（+118.3% vs前日OI），连续性待观察（方向未知）
09-30 726.0C — Vol 10,123 | 最新价 $2.17 | OI 1005→10254 (ΔOI +9249张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9249张（+920.3% vs前日OI），连续性待观察（方向未知）
09-30 710.0C — Vol 12,750 | 最新价 $7.83 | OI 2156→11045 (ΔOI +8889张) | ΔOI/Volume 69.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8889张（+412.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 63,627 张（Put 20,493 / Call 43,134），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 132.7k / P 247.1k，今日成交量: C 883.6k / P 1068.9k，平值价格ATM: C $1.27 / P $1.23 ｜ ATM IV 17.9%，预期波动 ±0.3%，Max Pain 708
Top ΔOI: P 700 +7,146 ｜ P 710 +6,331 ｜ C 715 +6,076

📆 Forward Expiration Structure

09-18  C +32.5k / P -28.9k ｜ Activity MEDIUM △ ｜ 1D
09-21  C +7.1k / P +52.4k ｜ Activity HIGH ｜ 4D
09-22  C +13.8k / P +8.5k ｜ Activity HIGH ｜ 5D
09-23  C +6.5k / P +12.6k ｜ Activity HIGH ｜ 6D

📆 09-18 Forward Structure
存量OI: C 1158.6k / P 1530.6k，今日变化ΔOI: C +32.5k / P -28.9k，平值价格ATM: C $3.01 / P $2.77 ｜ ATM IV 17.5%，净 delta 敞口 1.8M shares
Top ΔOI: P 700 -24,151 ｜ P 685 -19,902 ｜ P 665 +6,718
仓位参考: Max Pain 700 ｜ Call Wall 750（+4.8%，弱）（OI 50.6k） ｜ Put Wall 700（-2.1%，弱）（OI 90.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.5%｜历史 Rank 47%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,817,293 股

📆 09-21 Forward Structure
存量OI: C 31.8k / P 97.9k，今日变化ΔOI: C +7.1k / P +52.4k，平值价格ATM: C $4.05 / P $4.19 ｜ ATM IV 13.2%，净 delta 敞口 -5k shares
仓位参考: Max Pain 715 ｜ Call Wall 720（+0.6%，弱）（OI 2.3k） ｜ Put Wall 715（-0.1%，弱）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 13.2%｜历史 Rank 47%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,767 股

📆 09-22 Forward Structure
存量OI: C 26.3k / P 30.6k，今日变化ΔOI: C +13.8k / P +8.5k，平值价格ATM: C $4.81 / P $4.85 ｜ ATM IV 14.1%，净 delta 敞口 97k shares
Top ΔOI: C 758 +3,433 ｜ C 757 +3,276 ｜ C 756 +1,141
仓位参考: Max Pain 710 ｜ Call Wall 758（+6.0%，弱）（OI 3.4k） ｜ Put Wall 685（-4.2%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.1%｜历史 Rank 47%（近端代理）｜净 delta 敞口 正 97,435 股

📆 09-23 Forward Structure
存量OI: C 17.7k / P 24.4k，今日变化ΔOI: C +6.5k / P +12.6k，平值价格ATM: C $5.45 / P $5.51 ｜ ATM IV 14.8%，净 delta 敞口 101k shares
Top ΔOI: P 680 +1,714 ｜ C 720 +1,206 ｜ P 674 +948
仓位参考: Max Pain 710 ｜ Call Wall 735（+2.7%，弱）（OI 1.9k） ｜ Put Wall 680（-4.9%）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 14.8%｜历史 Rank 47%（近端代理）｜净 delta 敞口 正 100,710 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/QQQ_morning.json