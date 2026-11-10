# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.45
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 49C ΔOI +675（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 50C ΔOI +1,788 占该期限总 OI 16.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 48.14 → 今开 46.85（-2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 46.99 ｜ 低 46.44

Options: P/C成交量 0.77 | OI比 0.65 | ATM IV 42.5% | Skew 4.2pp | Term 0.91 | ExpMove ±2.1%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 4.2pp）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（1D）±2.1% ｜ 11-13（3D）±3.3% ｜ 11-16（6D）±3.8% ｜ 11-18（8D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,209,200 | GEX Change vs 上次快照 -13,699,691 | Flip: Primary Flip: 45.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 705 / LOW 150 / INVALID 405
结构观察区: Primary Flip 45.92（全链重定价，覆盖 98%）
最近结构参考: Flip 46（现价高于该位 2.3%）
量化视角： 正 Gamma（3621万，无历史分位）｜正 Gamma 减弱（1370万）｜现价位于 Flip 上方 2.27%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 46（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 50.0C — Vol 39,041 | 最新价 $1.23 | OI 7319→43976 (ΔOI +36657张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36657张（+500.9% vs前日OI），连续性待观察（方向未知）
11-20 48.5C — Vol 3,997 | 最新价 $1.25 | OI 2013→5641 (ΔOI +3628张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3628张（+180.2% vs前日OI），连续性待观察（方向未知）
11-27 40.0P — Vol 3,641 | 最新价 $0.11 | OI 4973→8268 (ΔOI +3295张) | ΔOI/Volume 90.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3295张（+66.3% vs前日OI），连续性待观察（方向未知）
11-11 49.5C — Vol 3,527 | 最新价 $0.20 | OI 520→2869 (ΔOI +2349张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2349张（+451.7% vs前日OI），连续性待观察（方向未知）
11-18 44.5P — Vol 2,161 | 最新价 $0.23 | OI 262→2407 (ΔOI +2145张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2145张（+818.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,074 张（Put 5,440 / Call 42,634），跨 5 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +12.9k / P +6.3k ｜ Activity HIGH ｜ 1D
11-13  C +6.8k / P +2.6k ｜ Activity HIGH ｜ 3D
11-16  C +4.6k / P +1.2k ｜ Activity HIGH ｜ 6D
11-18  C +0.5k / P +2.4k ｜ Activity HIGH ｜ 8D

📆 11-11 Forward Structure
存量OI: C 31.4k / P 20.4k，今日变化ΔOI: C +12.9k / P +6.3k，平值价格ATM: C $0.47 / P $0.53 ｜ ATM IV 42.5%，净 delta 敞口 32k shares
Top ΔOI: C 49 +2,349 ｜ C 50 +1,850
仓位参考: Max Pain 46 ｜ Call Wall 51（+8.6%，弱）（OI 4.4k） ｜ Put Wall 44（-6.3%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 42.5%｜历史 Rank 70%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 31,790 股

📆 11-13 Forward Structure
存量OI: C 69.3k / P 35.5k，今日变化ΔOI: C +6.8k / P +2.6k，平值价格ATM: C $0.77 / P $0.79 ｜ ATM IV 44.1%，净 delta 敞口 51k shares
Top ΔOI: C 50 +1,222 ｜ C 49 +803 ｜ C 49 +675
仓位参考: Max Pain 48 ｜ Call Wall 50（+6.5%）（OI 8.7k） ｜ Put Wall 45（-4.2%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 44.1%｜历史 Rank 70%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 50,752 股

📆 11-16 Forward Structure
存量OI: C 8.1k / P 2.8k，今日变化ΔOI: C +4.6k / P +1.2k，平值价格ATM: C $0.90 / P $0.90 ｜ ATM IV 36.6%，净 delta 敞口 14k shares
Top ΔOI: C 50 +1,788 ｜ C 48 +357
仓位参考: Max Pain 47 ｜ Call Wall 50（+6.5%，弱）（OI 2.0k） ｜ Put Wall 46.5（-1.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 36.6%｜历史 Rank 70%（近端代理）｜IV/RV 0.91×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 14,326 股

📆 11-18 Forward Structure
存量OI: C 2.2k / P 3.4k，今日变化ΔOI: C +0.5k / P +2.4k，平值价格ATM: C $1.05 / P $1.30 ｜ ATM IV 38.7%，净 delta 敞口 -28k shares
Top ΔOI: P 44 +2,145 ｜ C 49 +98 ｜ C 47 +70
仓位参考: Max Pain 45 ｜ Call Wall 50（+6.5%）（OI 0.5k） ｜ Put Wall 44.5（-5.2%）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 38.7%｜历史 Rank 70%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 负 27,573 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SLV_morning.json