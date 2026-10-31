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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,330.05 → 今开 1,215.09（-8.6%） | 较昨收变动（含盘初走势） ｜ 今日高 1239.00 ｜ 低 1196.29

Options: P/C成交量 0.63 | OI比 0.78 | ATM IV 134.4% | Skew -1.3pp | Term 0.52 | ExpMove ±8.8%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±8.8% ｜ 11-13（14D）±11.8% ｜ 11-20（21D）±14.5% ｜ 11-27（28D）±15.6%
   ⇒ IV–VIX Spread: +115.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,972,556 | GEX Change vs 上次快照 -5,457,862 | Flip: Primary Flip: 1281.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1628 / LOW 614 / INVALID 1166
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1281.38（全链重定价，覆盖 98%）
最近结构参考: Flip 1281（现价低于该位 4.9%）
量化视角： 负 Gamma（597万，无历史分位）｜负 Gamma 加深（546万）｜现价位于 Flip 下方 4.92%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,350（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1281（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 1100.0P — Vol 3,574 | 最新价 $1.10 | OI 1305→2658 (ΔOI +1353张) | ΔOI/Volume 37.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1353张（+103.7% vs前日OI），连续性待观察（方向未知）
10-30 1400.0C — Vol 3,268 | 最新价 $22.72 | OI 1741→2996 (ΔOI +1255张) | ΔOI/Volume 38.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1255张（+72.1% vs前日OI），连续性待观察（方向未知）
11-27 1150.0P — Vol 1,004 | 最新价 $34.00 | OI 45→1043 (ΔOI +998张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增998张（+2217.8% vs前日OI），连续性待观察（方向未知）
10-30 1000.0P — Vol 1,932 | 最新价 $0.35 | OI 1265→2228 (ΔOI +963张) | ΔOI/Volume 49.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增963张（+76.1% vs前日OI），连续性待观察（方向未知）
10-30 1410.0C — Vol 1,074 | 最新价 $20.20 | OI 143→1097 (ΔOI +954张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增954张（+667.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,523 张（Put 3,314 / Call 2,209），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 63.2k / P 49.5k，今日成交量: C 22.0k / P 13.9k，平值价格ATM: C $19.45 / P $16.00 ｜ ATM IV 134.4%，预期波动 ±2.9%，Max Pain 1,350
Top ΔOI: P 1100 +1,353 ｜ C 1400 +1,255 ｜ P 1000 +963

📆 Forward Expiration Structure

11-06  C +3.1k / P +2.3k ｜ Activity HIGH ｜ 7D
11-13  C +0.4k / P +1.3k ｜ Activity HIGH ｜ 14D
11-20  C +1.1k / P +0.5k ｜ Activity HIGH ｜ 21D
11-27  C +0.5k / P +1.4k ｜ Activity HIGH ｜ 28D

📆 11-06 Forward Structure
存量OI: C 21.4k / P 15.9k，今日变化ΔOI: C +3.1k / P +2.3k，平值价格ATM: C $55.06 / P $51.80 ｜ ATM IV 77.8%，净 delta 敞口 -16k shares
Top ΔOI: C 1350 +423
仓位参考: Max Pain 1,380 ｜ Call Wall 1300（+6.7%，弱）（OI 0.5k） ｜ Put Wall 1200（-1.5%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 77.8%｜历史 Rank 87%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,207 股

📆 11-13 Forward Structure
存量OI: C 6.5k / P 7.9k，今日变化ΔOI: C +0.4k / P +1.3k，平值价格ATM: C $75.59 / P $68.13 ｜ ATM IV 73.7%，净 delta 敞口 -9k shares
仓位参考: Max Pain 1,480 ｜ Call Wall 1300（+6.7%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜ATM IV 73.7%｜历史 Rank 87%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,373 股

📆 11-20 Forward Structure
存量OI: C 45.7k / P 51.8k，今日变化ΔOI: C +1.1k / P +0.5k，平值价格ATM: C $89.56 / P $86.70 ｜ ATM IV 73.0%，净 delta 敞口 36k shares
Top ΔOI: P 1200 -298 ｜ C 1800 +285 ｜ P 1000 +256
仓位参考: Max Pain 1,480 ｜ Call Wall 1300（+6.7%，弱）（OI 0.5k） ｜ Put Wall 1200（-1.5%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,851 股

📆 11-27 Forward Structure
存量OI: C 4.7k / P 6.8k，今日变化ΔOI: C +0.5k / P +1.4k，平值价格ATM: C $97.90 / P $91.94 ｜ ATM IV 69.5%，净 delta 敞口 -36k shares
Top ΔOI: P 1150 +998 ｜ C 1800 +177 ｜ C 1365 +64
仓位参考: Max Pain 1,390 ｜ Call Wall 1150（-5.6%，弱）（OI 0.2k） ｜ Put Wall 1150（-5.6%）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 69.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 36,097 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SNDK_morning.json