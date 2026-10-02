# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 55C ΔOI +625（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-12 54P ΔOI +2,083 占该期限总 OI 37.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 55.02 → 今开 55.46（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 55.67 ｜ 低 55.23

Options: P/C成交量 0.77 | OI比 0.44 | ATM IV 48.0% | Skew 1.8pp | Term 0.69 | ExpMove ±1.7%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-05（3D）±1.7% ｜ 10-07（5D）±2.6% ｜ 10-09（7D）±3.4% ｜ 10-12（10D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 52,337,997 | GEX Change vs 上次快照 33,291,313 | Flip: Primary Flip: 54.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 748 / LOW 136 / INVALID 326
结构观察区: Primary Flip 54.31（全链重定价，覆盖 93%）
Call Wall 60（弱结构｜现价低于该位 7.4%）
最近结构参考: Flip 54（现价高于该位 2.3%）
量化视角： 正 Gamma（5234万，无历史分位）｜正 Gamma 增强（+3329万）｜现价位于 Flip 上方 2.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（MaxPain，仅结算参考）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 56.0C — Vol 3,628 | 最新价 $1.07 | OI 6274→8981 (ΔOI +2707张) | ΔOI/Volume 74.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2707张（+43.1% vs前日OI），连续性待观察（方向未知）
10-02 53.0P — Vol 3,884 | 最新价 $0.04 | OI 1340→4041 (ΔOI +2701张) | ΔOI/Volume 69.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2701张（+201.6% vs前日OI），连续性待观察（方向未知）
10-02 57.0C — Vol 5,218 | 最新价 $0.04 | OI 4757→7247 (ΔOI +2490张) | ΔOI/Volume 47.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2490张（+52.3% vs前日OI），连续性待观察（方向未知）
10-16 52.0P — Vol 4,386 | 最新价 $0.40 | OI 3653→5811 (ΔOI +2158张) | ΔOI/Volume 49.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2158张（+59.1% vs前日OI），连续性待观察（方向未知）
10-12 54.0P — Vol 2,126 | 最新价 $0.69 | OI 53→2136 (ΔOI +2083张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2083张（+3930.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,139 张（Put 6,942 / Call 5,197），跨 3 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 112.1k / P 49.5k，今日成交量: C 26.4k / P 20.5k，平值价格ATM: C $0.35 / P $0.23 ｜ ATM IV 48.0%，预期波动 ±1.1%，Max Pain 55
Top ΔOI: P 53 +2,701 ｜ C 57 +2,490 ｜ P 59 -2,026

📆 Forward Expiration Structure

10-05  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 3D
10-07  C +1.8k / P +2.3k ｜ Activity HIGH ｜ 5D
10-09  C +5.3k / P +0.7k ｜ Activity MEDIUM △ ｜ 7D
10-12  C +0.2k / P +3.3k ｜ Activity HIGH ｜ 10D

📆 10-05 Forward Structure
存量OI: C 9.9k / P 7.2k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $0.49 / P $0.44 ｜ ATM IV 23.8%，净 delta 敞口 74k shares
Top ΔOI: C 57 +438 ｜ P 59 -405 ｜ C 55 +394
仓位参考: Max Pain 56 ｜ Call Wall 60（+8.0%，弱）（OI 1.2k） ｜ Put Wall 52（-6.4%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 23.8%｜历史 Rank 80%（近端代理）｜IV/RV 0.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 73,954 股

📆 10-07 Forward Structure
存量OI: C 18.5k / P 7.3k，今日变化ΔOI: C +1.8k / P +2.3k，平值价格ATM: C $0.74 / P $0.71 ｜ ATM IV 28.4%，净 delta 敞口 55k shares
Top ΔOI: P 52 +1,475 ｜ C 55 +625 ｜ C 57 +357
仓位参考: Max Pain 56 ｜ Call Wall 58（+4.4%，弱）（OI 3.0k） ｜ Put Wall 52（-6.4%）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 28.4%｜历史 Rank 80%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 正 55,162 股

10-09（MEDIUM △）Top ΔOI: 55C +1,230 ｜ 58C +621
10-09（MEDIUM △）仓位参考: Max Pain 56 ｜ Call Wall 60（+8.0%，弱）（OI 4.6k） ｜ Put Wall 55（-1.0%，弱）（OI 2.7k）

📆 10-12 Forward Structure
存量OI: C 1.7k / P 3.9k，今日变化ΔOI: C +0.2k / P +3.3k，平值价格ATM: C $1.01 / P $1.01 ｜ ATM IV 28.6%，净 delta 敞口 -74k shares
Top ΔOI: P 54 +2,083 ｜ P 52 +868 ｜ P 55 +241
仓位参考: Max Pain 55 ｜ Call Wall 58（+4.4%，弱）（OI 0.4k） ｜ Put Wall 54（-2.8%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 28.6%｜历史 Rank 80%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 负 74,034 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SLV_morning.json