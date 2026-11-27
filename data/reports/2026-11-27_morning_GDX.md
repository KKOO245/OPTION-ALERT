# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $641.80
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-30 78C ΔOI +700（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 67P ΔOI +720 占该期限总 OI 28.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 73.89 → 今开 77.12（+4.4%） | 较昨收变动（含盘初走势） ｜ 今日高 77.76 ｜ 低 76.52

Options: P/C成交量 0.63 | OI比 0.24 | ATM IV 62.1% | Skew -1.9pp | Term 0.82 | ExpMove ±2.9%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±2.9% ｜ 12-02（5D）±4.5% ｜ 12-04（7D）±5.5% ｜ 12-07（10D）±7.2%
   ⇒ IV–VIX Spread: +34.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,429,694 | GEX Change vs 上次快照 16,384,297 | Flip: Primary Flip: 73.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 567 / LOW 207 / INVALID 520
结构观察区: Primary Flip 73.47（全链重定价，覆盖 98%）
Put Wall 75（弱结构｜现价高于该位 2.5%）
最近结构参考: Put Wall 75（现价高于该位 2.5%）
量化视角： 正 Gamma（2943万，无历史分位）｜正 Gamma 增强（+1638万）｜现价位于 Flip 上方 4.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构） / 71（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 73（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 76.0C — Vol 17,663 | 最新价 $1.78 | OI 2991→20555 (ΔOI +17564张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17564张（+587.2% vs前日OI），连续性待观察（方向未知）
12-04 79.0C — Vol 17,547 | 最新价 $0.80 | OI 232→17681 (ΔOI +17449张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17449张（+7521.1% vs前日OI），连续性待观察（方向未知）
12-04 67.0P — Vol 3,152 | 最新价 $0.60 | OI 202→3293 (ΔOI +3091张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3091张（+1530.2% vs前日OI），连续性待观察（方向未知）
12-18 70.0C — Vol 4,501 | 最新价 $6.54 | OI 2679→5250 (ΔOI +2571张) | ΔOI/Volume 57.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2571张（+96.0% vs前日OI），连续性待观察（方向未知）
12-18 75.0C — Vol 4,315 | 最新价 $3.65 | OI 9463→11998 (ΔOI +2535张) | ΔOI/Volume 58.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2535张（+26.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 43,210 张（Put 3,091 / Call 40,119），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 71.4k / P 16.9k，今日成交量: C 2.2k / P 1.4k，平值价格ATM: C $0.28 / P $0.49 ｜ ATM IV 62.1%，预期波动 ±1.0%，Max Pain 71
Top ΔOI: C 75 -9,183 ｜ C 78 -4,250 ｜ C 79 -3,422

📆 Forward Expiration Structure

11-30  C +1.2k / P +0.6k ｜ Activity HIGH ｜ 3D
12-02  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 5D
12-04  C +35.6k / P +3.4k ｜ Activity HIGH ｜ 7D
12-07  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 4.5k / P 2.8k，今日变化ΔOI: C +1.2k / P +0.6k，平值价格ATM: C $1.01 / P $1.18 ｜ ATM IV 39.7%，净 delta 敞口 61k shares
Top ΔOI: P 71 +705 ｜ C 78 +700
仓位参考: Max Pain 71 ｜ Call Wall 80（+4.0%）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 39.7%｜历史 Rank 94%（近端代理）｜IV/RV 0.64×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 61,477 股

📆 12-02 Forward Structure
存量OI: C 1.2k / P 1.4k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $1.73 / P $1.71 ｜ ATM IV 47.8%，净 delta 敞口 8k shares
Top ΔOI: P 73 +50 ｜ C 79 +40
仓位参考: Max Pain 73 ｜ Call Wall 75（-2.5%）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 47.8%｜历史 Rank 94%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 正 7,824 股

📆 12-04 Forward Structure
存量OI: C 48.5k / P 20.9k，今日变化ΔOI: C +35.6k / P +3.4k，平值价格ATM: C $2.13 / P $2.12 ｜ ATM IV 52.3%，净 delta 敞口 1.7M shares
Top ΔOI: C 76 +17,564 ｜ C 79 +17,449 ｜ P 67 +3,091
仓位参考: Max Pain 76 ｜ Call Wall 76（-1.2%，弱）（OI 20.6k） ｜ Put Wall 72（-6.4%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 52.3%｜历史 Rank 94%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,655,561 股

📆 12-07 Forward Structure
存量OI: C 1.0k / P 0.6k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $2.93 / P $2.59 ｜ ATM IV 49.4%，净 delta 敞口 34k shares
Top ΔOI: C 77 +610 ｜ C 80 +71
仓位参考: Max Pain 72 ｜ Call Wall 77（+0.1%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 49.4%｜历史 Rank 94%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 34,234 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/GDX_morning.json