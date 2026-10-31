# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-04 210P ΔOI +1,452（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 187P ΔOI +14,746 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 213.66 → 今开 208.88（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 209.05 ｜ 低 205.71

Options: P/C成交量 0.47 | OI比 0.63 | ATM IV 51.0% | Skew 3.5pp | Term 0.83 | ExpMove ±2.1%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 3.5pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.1% ｜ 11-04（5D）±3.4% ｜ 11-06（7D）±4.1% ｜ 11-09（10D）±4.9%
   ⇒ IV–VIX Spread: +32.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 3,114,507 | GEX Change vs 上次快照 -123,324,869 | Flip: Primary Flip: 207.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 614 / LOW 234 / INVALID 560
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 207.52（全链重定价，覆盖 94%）
Put Wall 190（弱结构｜现价高于该位 9.3%）
最近结构参考: Flip 208（现价高于该位 0.0%）
量化视角： 正 Gamma（311万，无历史分位）｜正 Gamma 减弱（1.23亿）｜现价位于 Flip 上方 0.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构）；上方 212（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 208（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 225.0C — Vol 21,774 | 最新价 $0.72 | OI 10524→26820 (ΔOI +16296张) | ΔOI/Volume 74.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16296张（+154.8% vs前日OI），连续性待观察（方向未知）
11-02 187.5P — Vol 27,270 | 最新价 $0.04 | OI 119→14865 (ΔOI +14746张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14746张（+12391.6% vs前日OI），连续性待观察（方向未知）
11-06 217.5C — Vol 19,578 | 最新价 $2.58 | OI 4565→17731 (ΔOI +13166张) | ΔOI/Volume 67.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13166张（+288.4% vs前日OI），连续性待观察（方向未知）
10-30 215.0C — Vol 128,127 | 最新价 $0.97 | OI 37476→49952 (ΔOI +12476张) | ΔOI/Volume 9.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12476张（+33.3% vs前日OI），连续性待观察（方向未知）
10-30 220.0C — Vol 72,025 | 最新价 $0.10 | OI 53910→64166 (ΔOI +10256张) | ΔOI/Volume 14.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10256张（+19.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 66,940 张（Put 14,746 / Call 52,194），跨 3 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 532.7k / P 332.9k，今日成交量: C 213.8k / P 101.1k，平值价格ATM: C $1.32 / P $0.98 ｜ ATM IV 51.0%，预期波动 ±1.1%，Max Pain 212
Top ΔOI: C 225 -13,348 ｜ C 215 +12,476 ｜ C 220 +10,256

📆 Forward Expiration Structure

11-02  C +11.0k / P +36.6k ｜ Activity HIGH ｜ 3D
11-04  C +5.2k / P +5.5k ｜ Activity HIGH ｜ 5D
11-06  C +49.6k / P +4.8k ｜ Activity HIGH ｜ 7D
11-09  C +0.9k / P +0.6k ｜ Activity HIGH ｜ 10D

📆 11-02 Forward Structure
存量OI: C 38.5k / P 68.4k，今日变化ΔOI: C +11.0k / P +36.6k，平值价格ATM: C $2.36 / P $2.09 ｜ ATM IV 27.9%，净 delta 敞口 93k shares
Top ΔOI: P 187 +14,746 ｜ P 190 +7,107
仓位参考: Max Pain 212 ｜ Call Wall 220（+6.0%，弱）（OI 6.6k） ｜ Put Wall 187.5（-9.7%，弱）（OI 14.9k）
量化解读： 存量 Put 重｜ATM IV 27.9%｜历史 Rank 75%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 93,079 股

📆 11-04 Forward Structure
存量OI: C 20.1k / P 17.6k，今日变化ΔOI: C +5.2k / P +5.5k，平值价格ATM: C $3.68 / P $3.27 ｜ ATM IV 34.8%，净 delta 敞口 -159k shares
Top ΔOI: P 210 +1,452 ｜ C 220 +1,280 ｜ C 217 +1,263
仓位参考: Max Pain 215 ｜ Call Wall 225（+8.4%）（OI 4.0k） ｜ Put Wall 212.5（+2.4%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.8%｜历史 Rank 75%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 158,955 股

📆 11-06 Forward Structure
存量OI: C 165.6k / P 164.7k，今日变化ΔOI: C +49.6k / P +4.8k，平值价格ATM: C $4.54 / P $4.05 ｜ ATM IV 37.1%，净 delta 敞口 1.4M shares
Top ΔOI: C 225 +16,296 ｜ C 217 +13,166 ｜ C 215 +7,439
仓位参考: Max Pain 215 ｜ Call Wall 225（+8.4%）（OI 26.8k） ｜ Put Wall 200（-3.7%）（OI 13.7k）
量化解读： 存量两侧均衡｜ATM IV 37.1%｜历史 Rank 75%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,361,997 股

📆 11-09 Forward Structure
存量OI: C 3.3k / P 2.3k，今日变化ΔOI: C +0.9k / P +0.6k，平值价格ATM: C $5.00 / P $5.14 ｜ ATM IV 34.4%，净 delta 敞口 -6k shares
Top ΔOI: C 225 +326 ｜ C 215 +234 ｜ P 195 +100
仓位参考: Max Pain 215 ｜ Call Wall 225（+8.4%，弱）（OI 0.8k） ｜ Put Wall 215（+3.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 34.4%｜历史 Rank 75%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 5,954 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/NVDA_morning.json