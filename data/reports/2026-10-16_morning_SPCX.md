# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.01 ｜ QQQ $716.65
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 150C ΔOI +1,796（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 150C ΔOI +699 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 148.62 → 今开 147.82（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 147.92 ｜ 低 144.04

Options: P/C成交量 0.61 | OI比 0.86 | ATM IV 80.4% | Skew -5.7pp | Term 0.74 | ExpMove ±3.2%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-19（3D）±3.2% ｜ 10-21（5D）±8.9% ｜ 10-23（7D）±8.9% ｜ 10-26（10D）±9.6%
   ⇒ IV–VIX Spread: +64.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,446,821 | GEX Change vs 上次快照 36,409,135 | Flip: Primary Flip: 146.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 808 / LOW 110 / INVALID 498
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 146.93（全链重定价，覆盖 94%）
最近结构参考: Flip 147（现价低于该位 0.4%）
量化视角： 负 Gamma（745万，无历史分位）｜负 Gamma 缓解（+3641万）｜现价位于 Flip 下方 0.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 147（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 120.0P — Vol 9,534 | 最新价 $0.01 | OI 12916→17753 (ΔOI +4837张) | ΔOI/Volume 50.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4837张（+37.5% vs前日OI），连续性待观察（方向未知）
10-23 136.0P — Vol 4,178 | 最新价 $0.82 | OI 273→4217 (ΔOI +3944张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3944张（+1444.7% vs前日OI），连续性待观察（方向未知）
10-16 152.5C — Vol 20,366 | 最新价 $0.65 | OI 4867→8724 (ΔOI +3857张) | ΔOI/Volume 18.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3857张（+79.2% vs前日OI），连续性待观察（方向未知）
10-16 150.0C — Vol 49,922 | 最新价 $1.37 | OI 17566→21347 (ΔOI +3781张) | ΔOI/Volume 7.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3781张（+21.5% vs前日OI），连续性待观察（方向未知）
10-23 165.0C — Vol 5,993 | 最新价 $0.58 | OI 7591→11015 (ΔOI +3424张) | ΔOI/Volume 57.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3424张（+45.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,843 张（Put 8,781 / Call 11,062），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 448.1k / P 384.1k，今日成交量: C 76.9k / P 47.1k，平值价格ATM: C $1.31 / P $1.21 ｜ ATM IV 80.4%，预期波动 ±1.7%，Max Pain 147
Top ΔOI: P 165 -7,144 ｜ P 162 -6,750 ｜ P 120 +4,837

📆 Forward Expiration Structure

10-19  C +8.6k / P +12.1k ｜ Activity HIGH ｜ 3D
10-21  C +7.4k / P +3.9k ｜ Activity HIGH ｜ 5D
10-23  C +13.3k / P +19.8k ｜ Activity HIGH ｜ 7D
10-26  C +1.9k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 10-19 Forward Structure
存量OI: C 45.2k / P 34.8k，今日变化ΔOI: C +8.6k / P +12.1k，平值价格ATM: C $2.38 / P $2.27 ｜ ATM IV 41.8%，净 delta 敞口 179k shares
Top ΔOI: C 155 +2,232 ｜ P 135 +2,029
仓位参考: Max Pain 155 ｜ Call Wall 157.5（+7.7%，弱）（OI 4.6k） ｜ Put Wall 148（+1.2%）（OI 8.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.8%｜历史 Rank 99%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 179,413 股

📆 10-21 Forward Structure
存量OI: C 20.7k / P 11.0k，今日变化ΔOI: C +7.4k / P +3.9k，平值价格ATM: C $6.30 / P $6.70 ｜ ATM IV 86.8%，净 delta 敞口 147k shares
Top ΔOI: C 150 +1,796 ｜ C 146 +1,080 ｜ C 155 +618
仓位参考: Max Pain 150 ｜ Call Wall 150（+2.6%，弱）（OI 2.0k） ｜ Put Wall 147（+0.5%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 86.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 147,000 股

📆 10-23 Forward Structure
存量OI: C 80.2k / P 91.0k，今日变化ΔOI: C +13.3k / P +19.8k，平值价格ATM: C $6.65 / P $6.40 ｜ ATM IV 79.8%，净 delta 敞口 -92k shares
Top ΔOI: P 136 +3,944 ｜ C 165 +3,424 ｜ P 145 +3,095
仓位参考: Max Pain 155 ｜ Call Wall 155（+6.0%，弱）（OI 7.8k） ｜ Put Wall 140（-4.3%，弱）（OI 7.8k）
量化解读： 存量两侧均衡｜ATM IV 79.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 92,452 股

📆 10-26 Forward Structure
存量OI: C 4.1k / P 2.7k，今日变化ΔOI: C +1.9k / P +0.4k，平值价格ATM: C $6.60 / P $7.50 ｜ ATM IV 70.1%，净 delta 敞口 54k shares
Top ΔOI: C 150 +699 ｜ C 155 +417 ｜ P 144 -167
仓位参考: Max Pain 150 ｜ Call Wall 155（+6.0%，弱）（OI 0.8k） ｜ Put Wall 144（-1.6%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 70.1%｜历史 Rank 99%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 53,709 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SPCX_morning.json