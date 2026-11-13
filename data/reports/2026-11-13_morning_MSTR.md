# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.69
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 110P ΔOI +978（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 114.41 → 今开 112.00（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 112.63 ｜ 低 109.71

Options: P/C成交量 1.51 | OI比 0.75 | ATM IV 117.1% | Skew 8.1pp | Term 0.66 | ExpMove ±9.3%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 8.1pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.75）+ 当日成交偏 Put（P/C量 1.51）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.51×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±9.3% ｜ 11-27（14D）±12.2% ｜ 12-04（21D）±15.1% ｜ 12-11（28D）±17.8%
   ⇒ IV–VIX Spread: +97.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,146,048 | GEX Change vs 上次快照 20,265,138 | Flip: Primary Flip: 112.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 444 / LOW 218 / INVALID 370
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 112.10（全链重定价，覆盖 97%）
最近结构参考: Flip 112（现价低于该位 1.7%）
量化视角： 负 Gamma（1015万，无历史分位）｜负 Gamma 缓解（+2027万）｜现价位于 Flip 下方 1.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 120（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 112（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 126.0C — Vol 18,210 | 最新价 $1.64 | OI 303→18191 (ΔOI +17888张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17888张（+5903.6% vs前日OI），连续性待观察（方向未知）
11-20 120.0C — Vol 19,916 | 最新价 $3.20 | OI 2116→19394 (ΔOI +17278张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17278张（+816.5% vs前日OI），连续性待观察（方向未知）
11-20 127.0C — Vol 14,435 | 最新价 $1.50 | OI 299→14230 (ΔOI +13931张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13931张（+4659.2% vs前日OI），连续性待观察（方向未知）
11-20 121.0C — Vol 13,719 | 最新价 $2.89 | OI 431→13855 (ΔOI +13424张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13424张（+3114.6% vs前日OI），连续性待观察（方向未知）
11-20 122.0C — Vol 10,256 | 最新价 $2.61 | OI 336→10323 (ΔOI +9987张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9987张（+2972.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 72,508 张（Put 0 / Call 72,508），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 172.4k / P 128.9k，今日成交量: C 20.4k / P 30.9k，平值价格ATM: C $1.61 / P $1.21 ｜ ATM IV 117.1%，预期波动 ±2.6%，Max Pain 120
Top ΔOI: C 133 -22,477 ｜ C 139 -20,589 ｜ C 132 -6,620

📆 Forward Expiration Structure

11-20  C +84.8k / P -4.7k ｜ Activity HIGH ｜ 7D
11-27  C +2.1k / P +4.8k ｜ Activity MEDIUM △ ｜ 14D
12-04  C -3.6k / P +4.6k ｜ Activity HIGH ｜ 21D
12-11  C +0.5k / P +4.3k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 257.2k / P 155.8k，今日变化ΔOI: C +84.8k / P -4.7k，平值价格ATM: C $5.25 / P $5.05 ｜ ATM IV 82.6%，净 delta 敞口 2.8M shares
Top ΔOI: C 126 +17,888 ｜ C 120 +17,278 ｜ C 127 +13,931
仓位参考: Max Pain 121 ｜ Call Wall 120（+8.9%，弱）（OI 19.4k） ｜ Put Wall 110（-0.2%，弱）（OI 15.2k）
量化解读： 存量 Call 重｜ATM IV 82.6%｜历史 Rank 90%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,822,747 股

11-27（MEDIUM △）Top ΔOI: 165P -1,175 ｜ 110P +978
11-27（MEDIUM △）仓位参考: Max Pain 145 ｜ Put Wall 100（-9.2%，弱）（OI 4.5k）

📆 12-04 Forward Structure
存量OI: C 13.7k / P 37.5k，今日变化ΔOI: C -3.6k / P +4.6k，平值价格ATM: C $8.75 / P $7.93 ｜ ATM IV 77.0%，净 delta 敞口 -47k shares
Top ΔOI: P 80 +718
仓位参考: Max Pain 150 ｜ Put Wall 100（-9.2%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 77.0%｜历史 Rank 90%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 47,067 股

📆 12-11 Forward Structure
存量OI: C 6.2k / P 23.1k，今日变化ΔOI: C +0.5k / P +4.3k，平值价格ATM: C $10.40 / P $9.20 ｜ ATM IV 77.1%，净 delta 敞口 -97k shares
Top ΔOI: P 75 +546 ｜ P 80 +512
仓位参考: Max Pain 155 ｜ Call Wall 120（+8.9%，弱）（OI 0.5k） ｜ Put Wall 100（-9.2%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 77.1%｜历史 Rank 90%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 97,004 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 82.6% vs 11-27 77.3%（差 +5.3pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/MSTR_morning.json