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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-30 40C ΔOI +1,498（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 38C ΔOI +3,504 占该期限总 OI 14.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 37.10 → 今开 39.56（+6.6%） | 较昨收变动（含盘初走势） ｜ 今日高 39.65 ｜ 低 39.10

Options: P/C成交量 0.92 | OI比 0.30 | ATM IV 77.2% | Skew 3.9pp | Term 0.72 | ExpMove ±3.4%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±3.4% ｜ 12-02（5D）±5.1% ｜ 12-04（7D）±6.3% ｜ 12-07（10D）±7.4%
   ⇒ IV–VIX Spread: +49.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,465,132 | GEX Change vs 上次快照 65,369,607 | Flip: Primary Flip: 35.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 784 / LOW 254 / INVALID 718
结构观察区: Primary Flip 35.80（全链重定价，覆盖 93%）
Put Wall 40（弱结构｜现价低于该位 1.8%）
最近结构参考: Put Wall 40（现价低于该位 1.8%）
量化视角： 正 Gamma（5447万，无历史分位）｜由负转正（+6537万）｜现价位于 Flip 上方 9.73%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 38（MaxPain，仅结算参考）；上方 40（Put Wall，弱结构）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-11 40.0C — Vol 5,548 | 最新价 $0.82 | OI 775→5546 (ΔOI +4771张) | ΔOI/Volume 86.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4771张（+615.6% vs前日OI），连续性待观察（方向未知）
12-11 42.0C — Vol 5,169 | 最新价 $0.43 | OI 2244→6442 (ΔOI +4198张) | ΔOI/Volume 81.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4198张（+187.1% vs前日OI），连续性待观察（方向未知）
12-02 38.5C — Vol 4,112 | 最新价 $0.66 | OI 325→3829 (ΔOI +3504张) | ΔOI/Volume 85.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3504张（+1078.2% vs前日OI），连续性待观察（方向未知）
12-18 30.0P — Vol 4,619 | 最新价 $0.36 | OI 10956→14098 (ΔOI +3142张) | ΔOI/Volume 68.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3142张（+28.7% vs前日OI），连续性待观察（方向未知）
12-11 34.5P — Vol 2,867 | 最新价 $0.95 | OI 5→2787 (ΔOI +2782张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2782张（+55640.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,397 张（Put 5,924 / Call 12,473），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 139.4k / P 41.5k，今日成交量: C 18.2k / P 16.7k，平值价格ATM: C $0.14 / P $0.37 ｜ ATM IV 77.2%，预期波动 ±1.3%，Max Pain 38
Top ΔOI: C 37 +2,488 ｜ C 38 +2,453 ｜ C 39 +2,103

📆 Forward Expiration Structure

11-30  C +7.6k / P +0.9k ｜ Activity HIGH ｜ 3D
12-02  C +8.3k / P +1.7k ｜ Activity HIGH ｜ 5D
12-04  C +6.0k / P +0.9k ｜ Activity HIGH ｜ 7D
12-07  C +3.3k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 37.1k / P 14.4k，今日变化ΔOI: C +7.6k / P +0.9k，平值价格ATM: C $0.59 / P $0.75 ｜ ATM IV 45.1%，净 delta 敞口 492k shares
Top ΔOI: C 40 +1,498 ｜ C 38 +1,213 ｜ C 36 +1,078
仓位参考: Max Pain 38 ｜ Call Wall 40（+1.8%，弱）（OI 3.8k） ｜ Put Wall 39（-0.7%）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 45.1%｜历史 Rank 96%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 492,014 股

📆 12-02 Forward Structure
存量OI: C 18.3k / P 6.2k，今日变化ΔOI: C +8.3k / P +1.7k，平值价格ATM: C $0.96 / P $1.05 ｜ ATM IV 54.9%，净 delta 敞口 478k shares
Top ΔOI: C 38 +3,504 ｜ C 40 +1,353 ｜ C 38 +778
仓位参考: Max Pain 38 ｜ Call Wall 42（+6.9%，弱）（OI 5.1k） ｜ Put Wall 39（-0.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 54.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 477,741 股

📆 12-04 Forward Structure
存量OI: C 121.5k / P 22.4k，今日变化ΔOI: C +6.0k / P +0.9k，平值价格ATM: C $1.21 / P $1.27 ｜ ATM IV 58.9%，净 delta 敞口 299k shares
Top ΔOI: C 42 +1,417 ｜ C 42 +1,109 ｜ C 36 +583
仓位参考: Max Pain 40 ｜ Put Wall 40（+1.8%）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 58.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 298,750 股

📆 12-07 Forward Structure
存量OI: C 4.3k / P 1.7k，今日变化ΔOI: C +3.3k / P +0.4k，平值价格ATM: C $1.33 / P $1.56 ｜ ATM IV 54.5%，净 delta 敞口 273k shares
Top ΔOI: C 34 +2,521 ｜ C 34 +168 ｜ C 40 +117
仓位参考: Max Pain 34 ｜ Call Wall 38（-3.3%，弱）（OI 0.6k） ｜ Put Wall 36（-8.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 54.5%｜历史 Rank 96%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 272,705 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SLV_morning.json