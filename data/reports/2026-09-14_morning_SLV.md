# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.06
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-16 56P ΔOI +3,422（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 58.12 → 今开 56.84（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 57.12 ｜ 低 56.67

Options: P/C成交量 1.21 | OI比 0.57 | ATM IV 41.2% | Skew 0.2pp | Term 1.05 | ExpMove ±3.1%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 1.05）｜保护溢价薄（Skew 0.2pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.57）+ 当日成交偏 Put（P/C量 1.21）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-16（2D）±3.1% ｜ 09-18（4D）±4.3% ｜ 09-21（7D）±4.8% ｜ 09-23（9D）±0.0%
   ⇒ IV–VIX Spread: +23.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,041,830 | GEX Change vs 上次快照 -38,345,661 | Flip: Primary Flip: 56.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 962 / LOW 199 / INVALID 513
结构观察区: Primary Flip 56.27（全链重定价，覆盖 99%）
最近结构参考: Flip 56（现价高于该位 0.8%）
量化视角： 正 Gamma（1204万，无历史分位）｜正 Gamma 减弱（3835万）｜现价位于 Flip 上方 0.79%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 64.0C — Vol 12,371 | 最新价 $1.21 | OI 44281→56350 (ΔOI +12069张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12069张（+27.3% vs前日OI），连续性待观察（方向未知）
09-16 70.0C — Vol 5,149 | 最新价 $0.02 | OI 228→5367 (ΔOI +5139张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5139张（+2253.9% vs前日OI），连续性待观察（方向未知）
09-16 56.0P — Vol 3,898 | 最新价 $0.24 | OI 363→3785 (ΔOI +3422张) | ΔOI/Volume 87.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3422张（+942.7% vs前日OI），连续性待观察（方向未知）
09-16 55.0P — Vol 4,946 | 最新价 $0.12 | OI 269→3563 (ΔOI +3294张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3294张（+1224.5% vs前日OI），连续性待观察（方向未知）
09-18 62.0C — Vol 6,190 | 最新价 $0.24 | OI 15092→18046 (ΔOI +2954张) | ΔOI/Volume 47.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2954张（+19.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,878 张（Put 6,716 / Call 20,162），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 20.1k / P 11.5k，今日成交量: C 5.9k / P 7.1k，平值价格ATM: C $0.41 / P $0.14 ｜ ATM IV 41.2%，预期波动 ±1.0%，Max Pain 59
Top ΔOI: C 60 +2,122 ｜ P 56 +1,068 ｜ C 63 -976

📆 Forward Expiration Structure

09-16  C +7.0k / P +8.7k ｜ Activity HIGH ｜ 2D
09-18  C +3.0k / P +1.6k ｜ Activity HIGH ｜ 4D
09-21  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 7D
09-23  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 9D

📆 09-16 Forward Structure
存量OI: C 14.5k / P 17.6k，今日变化ΔOI: C +7.0k / P +8.7k，平值价格ATM: C $0.98 / P $0.77 ｜ ATM IV 47.6%，净 delta 敞口 -287k shares
Top ΔOI: P 56 +3,422 ｜ P 55 +3,294
仓位参考: Max Pain 59 ｜ Put Wall 58（+2.3%，弱）（OI 5.0k）
量化解读： 存量 Put 重｜ATM IV 47.6%｜历史 Rank 69%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 286,700 股

📆 09-18 Forward Structure
存量OI: C 965.1k / P 462.8k，今日变化ΔOI: C +3.0k / P +1.6k，平值价格ATM: C $1.35 / P $1.08 ｜ ATM IV 49.5%，净 delta 敞口 2k shares
Top ΔOI: C 62 +2,954
仓位参考: Max Pain 60
量化解读： 存量 Call 重｜ATM IV 49.5%｜历史 Rank 69%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,712 股

📆 09-21 Forward Structure
存量OI: C 2.2k / P 1.5k，今日变化ΔOI: C +0.9k / P +0.3k，平值价格ATM: C $1.48 / P $1.24 ｜ ATM IV 42.4%，净 delta 敞口 9k shares
Top ΔOI: C 58 +422 ｜ C 60 +208 ｜ C 61 +129
仓位参考: Max Pain 58 ｜ Call Wall 58（+2.3%，弱）（OI 0.5k） ｜ Put Wall 59（+4.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 42.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 9,429 股

📆 09-23 Forward Structure
存量OI: C 1.4k / P 1.4k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 43.2%，净 delta 敞口 -10k shares
Top ΔOI: P 58 +216 ｜ C 58 +176 ｜ P 55 +68
仓位参考: Max Pain 60 ｜ Put Wall 58（+2.3%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 43.2%｜历史 Rank 69%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 9,823 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SLV_morning.json