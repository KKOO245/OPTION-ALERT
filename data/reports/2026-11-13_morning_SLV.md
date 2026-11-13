# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.80 ｜ QQQ $679.89
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-18 46C ΔOI +680（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 49C ΔOI +2,891 占该期限总 OI 14.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 45.12 → 今开 44.78（-0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 45.17 ｜ 低 44.44

Options: P/C成交量 0.53 | OI比 0.49 | ATM IV 42.4% | Skew -0.9pp | Term 0.92 | ExpMove ±2.3%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±2.3% ｜ 11-18（5D）±3.5% ｜ 11-20（7D）±4.5% ｜ 11-23（10D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,632,120 | GEX Change vs 上次快照 18,649,023 | Flip: Primary Flip: 44.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 621 / LOW 197 / INVALID 386
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 44.85（全链重定价，覆盖 94%）
最近结构参考: Flip 45（现价高于该位 0.1%）
量化视角： 正 Gamma（163万，无历史分位）｜由负转正（+1865万）｜现价位于 Flip 上方 0.09%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 46（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 45（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 46.0C — Vol 14,111 | 最新价 $1.89 | OI 1926→14719 (ΔOI +12793张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12793张（+664.2% vs前日OI），连续性待观察（方向未知）
12-18 52.0C — Vol 12,591 | 最新价 $0.44 | OI 26113→38220 (ΔOI +12107张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12107张（+46.4% vs前日OI），连续性待观察（方向未知）
11-13 44.0P — Vol 5,435 | 最新价 $0.12 | OI 1715→4821 (ΔOI +3106张) | ΔOI/Volume 57.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3106张（+181.1% vs前日OI），连续性待观察（方向未知）
11-18 49.0C — Vol 2,931 | 最新价 $0.07 | OI 1973→4864 (ΔOI +2891张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2891张（+146.5% vs前日OI），连续性待观察（方向未知）
12-18 47.0C — Vol 2,828 | 最新价 $1.50 | OI 7141→9150 (ΔOI +2009张) | ΔOI/Volume 71.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2009张（+28.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,906 张（Put 3,106 / Call 29,800），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 90.6k / P 44.4k，今日成交量: C 6.5k / P 3.4k，平值价格ATM: C $0.15 / P $0.28 ｜ ATM IV 42.4%，预期波动 ±0.9%，Max Pain 46
Top ΔOI: P 44 +3,106 ｜ C 46 +1,966 ｜ C 45 +1,343

📆 Forward Expiration Structure

11-16  C +3.4k / P +2.1k ｜ Activity HIGH ｜ 3D
11-18  C +6.2k / P +1.4k ｜ Activity HIGH ｜ 5D
11-20  C -8.2k / P -4.8k ｜ Activity MEDIUM △ ｜ 7D
11-23  C +2.0k / P +0.2k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 14.7k / P 6.6k，今日变化ΔOI: C +3.4k / P +2.1k，平值价格ATM: C $0.45 / P $0.57 ｜ ATM IV 30.3%，净 delta 敞口 48k shares
Top ΔOI: C 48 +1,070 ｜ C 48 +726
仓位参考: Max Pain 46 ｜ Call Wall 48（+6.9%，弱）（OI 2.2k） ｜ Put Wall 45（+0.3%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 30.3%｜历史 Rank 69%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 47,731 股

📆 11-18 Forward Structure
存量OI: C 11.2k / P 8.7k，今日变化ΔOI: C +6.2k / P +1.4k，平值价格ATM: C $0.82 / P $0.75 ｜ ATM IV 37.3%，净 delta 敞口 51k shares
Top ΔOI: C 49 +2,891 ｜ C 46 +680
仓位参考: Max Pain 46 ｜ Call Wall 49（+9.2%）（OI 4.9k） ｜ Put Wall 44.5（-0.9%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 37.3%｜历史 Rank 69%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 51,434 股

11-20（MEDIUM △）Top ΔOI: 55P -2,339 ｜ 54P -1,706
11-20（MEDIUM △）仓位参考: Max Pain 50 ｜ Put Wall 41（-8.7%，弱）（OI 11.5k）

📆 11-23 Forward Structure
存量OI: C 6.4k / P 0.9k，今日变化ΔOI: C +2.0k / P +0.2k，平值价格ATM: C $1.22 / P $1.10 ｜ ATM IV 36.4%，净 delta 敞口 53k shares
Top ΔOI: C 46 +1,857 ｜ C 49 +74 ｜ C 45 +44
仓位参考: Max Pain 45 ｜ Call Wall 47.5（+5.8%）（OI 3.0k） ｜ Put Wall 48（+6.9%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 36.4%｜历史 Rank 69%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 53,275 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SLV_morning.json