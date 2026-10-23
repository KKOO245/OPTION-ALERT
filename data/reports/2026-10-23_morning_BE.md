# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $760.75 ｜ QQQ $704.40
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 190P ΔOI +587（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 217.77 → 今开 203.01（-6.8%） | 较昨收变动（含盘初走势） ｜ 今日高 205.99 ｜ 低 189.00

Options: P/C成交量 0.78 | OI比 0.77 | ATM IV 182.2% | Skew 7.7pp | Term 0.45 | ExpMove ±10.3%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.45，近月 IV 高于远月）｜保护溢价显著（Skew 7.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±10.3% ｜ 11-06（14D）±15.5% ｜ 11-13（21D）±17.1% ｜ 11-20（28D）±18.4%
   ⇒ IV–VIX Spread: +162.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,637,170 | GEX Change vs 上次快照 -4,603,579 | Flip: Primary Flip: 219.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 553 / LOW 145 / INVALID 206
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 219.08（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价低于该位 2.2%）
最近结构参考: Put Wall 200（现价低于该位 2.2%）
量化视角： 负 Gamma（1364万，无历史分位）｜负 Gamma 加深（460万）｜现价位于 Flip 下方 10.73%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 219（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 220.0C — Vol 4,457 | 最新价 $13.46 | OI 381→2980 (ΔOI +2599张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2599张（+682.1% vs前日OI），连续性待观察（方向未知）
10-23 165.0P — Vol 3,052 | 最新价 $0.21 | OI 584→3052 (ΔOI +2468张) | ΔOI/Volume 80.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2468张（+422.6% vs前日OI），连续性待观察（方向未知）
10-30 217.5C — Vol 2,302 | 最新价 $14.62 | OI 82→2096 (ΔOI +2014张) | ΔOI/Volume 87.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2014张（+2456.1% vs前日OI），连续性待观察（方向未知）
10-23 200.0P — Vol 4,522 | 最新价 $3.70 | OI 3460→4763 (ΔOI +1303张) | ΔOI/Volume 28.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1303张（+37.7% vs前日OI），连续性待观察（方向未知）
10-23 180.0P — Vol 3,701 | 最新价 $0.68 | OI 1311→2608 (ΔOI +1297张) | ΔOI/Volume 35.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1297张（+98.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,681 张（Put 5,068 / Call 4,613），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 71.8k / P 55.1k，今日成交量: C 32.6k / P 25.6k，平值价格ATM: C $4.25 / P $3.47 ｜ ATM IV 182.2%，预期波动 ±4.0%，Max Pain 230
Top ΔOI: P 165 +2,468 ｜ P 200 +1,303 ｜ P 180 +1,297

📆 Forward Expiration Structure

10-30  C +13.3k / P +3.8k ｜ Activity HIGH ｜ 7D
11-06  C +2.3k / P +0.6k ｜ Activity HIGH ｜ 14D
11-13  C +0.2k / P -0.3k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +2.2k / P +1.9k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 34.7k / P 31.8k，今日变化ΔOI: C +13.3k / P +3.8k，平值价格ATM: C $10.50 / P $9.60 ｜ ATM IV 93.2%，净 delta 敞口 109k shares
Top ΔOI: C 220 +2,599 ｜ C 217 +2,014 ｜ C 230 +735
仓位参考: Max Pain 230 ｜ Call Wall 210（+7.4%，弱）（OI 0.8k） ｜ Put Wall 190（-2.8%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 93.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 108,549 股

📆 11-06 Forward Structure
存量OI: C 11.0k / P 12.4k，今日变化ΔOI: C +2.3k / P +0.6k，平值价格ATM: C $14.17 / P $16.20 ｜ ATM IV 87.9%，净 delta 敞口 -3k shares
Top ΔOI: C 210 +210
仓位参考: Max Pain 250 ｜ Put Wall 215（+9.9%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 87.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,493 股

11-13（MEDIUM △）Top ΔOI: 230P -432 ｜ 200P -213
11-13（MEDIUM △）仓位参考: Max Pain 250 ｜ Put Wall 200（+2.3%，弱）（OI 0.5k）

📆 11-20 Forward Structure
存量OI: C 50.9k / P 65.2k，今日变化ΔOI: C +2.2k / P +1.9k，平值价格ATM: C $18.55 / P $17.50 ｜ ATM IV 82.2%，净 delta 敞口 -22k shares
Top ΔOI: P 190 +587 ｜ C 240 -447 ｜ C 220 +381
仓位参考: Max Pain 240 ｜ Call Wall 180（-8.0%，弱）（OI 1.2k） ｜ Put Wall 200（+2.3%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 82.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 21,715 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/BE_morning.json