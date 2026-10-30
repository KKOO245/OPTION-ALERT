# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $756.16 ｜ QQQ $690.49
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
🟡 **近现价集中开仓**: 11-06 74P ΔOI +1,856（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 81.33 → 今开 78.24（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 78.32 ｜ 低 77.08

Options: P/C成交量 0.02 | OI比 0.24 | ATM IV 60.6% | Skew 8.5pp | Term 0.69 | ExpMove ±2.6%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 8.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.02×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.6% ｜ 11-04（5D）±1.6% ｜ 11-06（7D）±5.1% ｜ 11-09（10D）±2.3%
   ⇒ IV–VIX Spread: +41.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,159,502 | GEX Change vs 上次快照 -63,108,430 | Flip: Primary Flip: 78.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 465 / LOW 150 / INVALID 517
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 78.23（全链重定价，覆盖 86%）
Put Wall 80（弱结构｜现价低于该位 3.3%）
最近结构参考: Flip 78（现价低于该位 1.1%）
量化视角： 负 Gamma（1316万，无历史分位）｜由正转负（6311万）｜现价位于 Flip 下方 1.13%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 80（Put Wall，弱结构） / 81（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 78（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 85.0C — Vol 3,253 | 最新价 $1.98 | OI 2294→4607 (ΔOI +2313张) | ΔOI/Volume 71.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2313张（+100.8% vs前日OI），连续性待观察（方向未知）
11-06 74.0P — Vol 1,998 | 最新价 $0.24 | OI 73→1929 (ΔOI +1856张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1856张（+2542.5% vs前日OI），连续性待观察（方向未知）
11-20 95.0C — Vol 1,458 | 最新价 $0.36 | OI 6307→7396 (ΔOI +1089张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1089张（+17.3% vs前日OI），连续性待观察（方向未知）
11-20 84.0C — Vol 960 | 最新价 $2.20 | OI 10293→11176 (ΔOI +883张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增883张（+8.6% vs前日OI），连续性待观察（方向未知）
10-30 79.0P — Vol 2,346 | 最新价 $0.18 | OI 3654→4516 (ΔOI +862张) | ΔOI/Volume 36.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增862张（+23.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,003 张（Put 2,718 / Call 4,285），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 138.1k / P 32.7k，今日成交量: C 42.8k / P 1.0k，平值价格ATM: C $0.83 / P $0.29 ｜ ATM IV 60.6%，预期波动 ±1.4%，Max Pain 81
Top ΔOI: P 90 -866 ｜ P 79 +862 ｜ C 84 +770

📆 Forward Expiration Structure

11-02  C +0.1k / P +0.1k ｜ Activity HIGH ｜ 3D
11-04  C +48 / P +0.1k ｜ Activity HIGH ｜ 5D
11-06  C +1.1k / P +2.9k ｜ Activity HIGH ｜ 7D
11-09  C -3 / P +80 ｜ Activity MEDIUM △ ｜ 10D

📆 11-02 Forward Structure
存量OI: C 1.8k / P 2.2k，今日变化ΔOI: C +0.1k / P +0.1k，平值价格ATM: C $1.26 / P $0.76 ｜ ATM IV 37.0%，净 delta 敞口 -5k shares
Top ΔOI: P 80 +215 ｜ P 79 +80
仓位参考: Max Pain 83 ｜ Put Wall 76（-1.7%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 37.0%｜历史 Rank 95%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,451 股

📆 11-04 Forward Structure
存量OI: C 0.9k / P 0.3k，今日变化ΔOI: C +48 / P +0.1k，平值价格ATM: C $0.00 / P $1.23 ｜ ATM IV 42.6%，净 delta 敞口 -7k shares
Top ΔOI: P 81 +54 ｜ P 77 +26 ｜ C 85 +26
仓位参考: Max Pain 82 ｜ Call Wall 82（+6.0%，弱）（OI 52） ｜ Put Wall 79（+2.1%，弱）（OI 61）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.6%｜历史 Rank 95%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 7,018 股

📆 11-06 Forward Structure
存量OI: C 13.6k / P 13.4k，今日变化ΔOI: C +1.1k / P +2.9k，平值价格ATM: C $2.18 / P $1.75 ｜ ATM IV 47.5%，净 delta 敞口 -84k shares
Top ΔOI: P 74 +1,856 ｜ P 81 +387
仓位参考: Max Pain 85 ｜ Put Wall 80（+3.4%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 47.5%｜历史 Rank 95%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 84,223 股

11-09（MEDIUM △）Top ΔOI: 73P +25 ｜ 78P +25
11-09（MEDIUM △）仓位参考: Max Pain 82 ｜ Put Wall 78（+0.9%，弱）（OI 29）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/GDX_morning.json