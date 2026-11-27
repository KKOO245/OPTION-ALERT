# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $730.70 ｜ QQQ $650.99
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 170C ΔOI +7,866（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 95P ΔOI +12,070 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 163.59 → 今开 169.76（+3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 171.04 ｜ 低 164.80

Options: P/C成交量 0.37 | OI比 0.61 | ATM IV 94.0% | Skew 7.6pp | Term 0.60 | ExpMove ±7.0%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价显著（Skew 7.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±7.0% ｜ 12-11（14D）±9.6% ｜ 12-18（21D）±11.2% ｜ 12-24（27D）±11.9%
   ⇒ IV–VIX Spread: +66.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 46,209,974 | GEX Change vs 上次快照 5,949,980 | Flip: Primary Flip: 155.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 413 / LOW 177 / INVALID 368
结构观察区: Primary Flip 155.01（全链重定价，覆盖 92%）
Call Wall 175（弱结构｜现价低于该位 4.3%）
最近结构参考: Call Wall 175（现价低于该位 4.3%）
量化视角： 正 Gamma（4621万，无历史分位）｜正 Gamma 增强（+595万）｜现价位于 Flip 上方 8.09%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 175（Call Wall，弱结构）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 95.0P — Vol 12,194 | 最新价 $0.05 | OI 210→12280 (ΔOI +12070张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12070张（+5747.6% vs前日OI），连续性待观察（方向未知）
12-04 170.0C — Vol 9,105 | 最新价 $3.80 | OI 1433→9299 (ΔOI +7866张) | ΔOI/Volume 86.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7866张（+548.9% vs前日OI），连续性待观察（方向未知）
12-04 175.0C — Vol 9,772 | 最新价 $2.26 | OI 1894→9441 (ΔOI +7547张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7547张（+398.5% vs前日OI），连续性待观察（方向未知）
12-04 85.0P — Vol 4,663 | 最新价 $0.04 | OI 419→4705 (ΔOI +4286张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4286张（+1022.9% vs前日OI），连续性待观察（方向未知）
12-04 80.0P — Vol 1,934 | 最新价 $0.02 | OI 67→1726 (ΔOI +1659张) | ΔOI/Volume 85.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1659张（+2476.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 33,428 张（Put 18,015 / Call 15,413），跨 1 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 105.3k / P 63.9k，今日成交量: C 24.6k / P 9.0k，平值价格ATM: C $1.33 / P $1.15 ｜ ATM IV 94.0%，预期波动 ±1.5%，Max Pain 152
Top ΔOI: C 155 -2,323 ｜ C 180 +1,440 ｜ P 155 +1,335

📆 Forward Expiration Structure

12-04  C +18.9k / P +21.7k ｜ Activity HIGH ｜ 7D
12-11  C +0.5k / P +1.2k ｜ Activity HIGH ｜ 14D
12-18  C +0.6k / P -0.4k ｜ Activity HIGH ｜ 21D
12-24  C +0.3k / P +20 ｜ Activity LOW ｜ 27D

📆 12-04 Forward Structure
存量OI: C 54.3k / P 48.0k，今日变化ΔOI: C +18.9k / P +21.7k，平值价格ATM: C $6.00 / P $5.73 ｜ ATM IV 62.7%，净 delta 敞口 713k shares
Top ΔOI: C 170 +7,866 ｜ C 175 +7,547
仓位参考: Max Pain 160 ｜ Call Wall 175（+4.4%，弱）（OI 9.4k） ｜ Put Wall 155（-7.5%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.7%｜历史 Rank 93%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 712,599 股

📆 12-11 Forward Structure
存量OI: C 13.9k / P 16.3k，今日变化ΔOI: C +0.5k / P +1.2k，平值价格ATM: C $8.25 / P $7.80 ｜ ATM IV 60.5%，净 delta 敞口 10k shares
Top ΔOI: P 145 +352 ｜ C 180 -317
仓位参考: Max Pain 160 ｜ Call Wall 175（+4.4%，弱）（OI 1.3k） ｜ Put Wall 160（-4.5%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 60.5%｜历史 Rank 93%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,252 股

📆 12-18 Forward Structure
存量OI: C 267.5k / P 262.8k，今日变化ΔOI: C +0.6k / P -0.4k，平值价格ATM: C $9.61 / P $9.18 ｜ ATM IV 59.1%，净 delta 敞口 28k shares
Top ΔOI: C 190 +938 ｜ P 130 -569
仓位参考: Max Pain 140 ｜ Call Wall 165（-1.5%，弱）（OI 14.3k） ｜ Put Wall 160（-4.5%，弱）（OI 18.5k）
量化解读： 存量两侧均衡｜ATM IV 59.1%｜历史 Rank 93%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,165 股

12-24（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 180（+7.4%，弱）（OI 0.7k） ｜ Put Wall 155（-7.5%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/PLTR_morning.json