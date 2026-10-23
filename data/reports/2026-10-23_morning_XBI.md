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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 151.64 → 今开 150.46（-0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 150.70 ｜ 低 147.63

Options: P/C成交量 1.09 | OI比 1.38 | ATM IV 69.9% | Skew 25.1pp | Term 0.48 | ExpMove ±4.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价显著（Skew 25.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.09×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±4.2% ｜ 11-06（14D）±4.5% ｜ 11-13（21D）±3.9% ｜ 11-20（28D）±8.0%
   ⇒ IV–VIX Spread: +50.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,025,177 | GEX Change vs 上次快照 -11,286,847 | Flip: Primary Flip: 159.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 366 / LOW 104 / INVALID 312
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.04（全链重定价，覆盖 90%）
Put Wall 140（弱结构｜现价高于该位 6.3%）
最近结构参考: Put Wall 140（现价高于该位 6.3%）
量化视角： 负 Gamma（2803万，无历史分位）｜负 Gamma 加深（1129万）｜现价位于 Flip 下方 6.43%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构） / 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 165.0C — Vol 2,588 | 最新价 $1.41 | OI 5386→7350 (ΔOI +1964张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1964张（+36.5% vs前日OI），连续性待观察（方向未知）
10-23 140.0P — Vol 1,052 | 最新价 $0.02 | OI 1914→2598 (ΔOI +684张) | ΔOI/Volume 65.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增684张（+35.7% vs前日OI），连续性待观察（方向未知）
10-23 148.0P — Vol 738 | 最新价 $0.48 | OI 1545→2027 (ΔOI +482张) | ΔOI/Volume 65.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增482张（+31.2% vs前日OI），连续性待观察（方向未知）
11-20 175.0C — Vol 400 | 最新价 $0.34 | OI 279→679 (ΔOI +400张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增400张（+143.4% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 221 | 最新价 $1.96 | OI 1276→1456 (ΔOI +180张) | ΔOI/Volume 81.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增180张（+14.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,710 张（Put 1,346 / Call 2,364），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 17.8k / P 24.5k，今日成交量: C 0.5k / P 1.3k，平值价格ATM: C $1.09 / P $1.21 ｜ ATM IV 69.9%，预期波动 ±1.5%，Max Pain 148
Top ΔOI: P 140 +684 ｜ P 148 +482 ｜ P 151 -166

📆 Forward Expiration Structure

10-30  C +0.2k / P +2 ｜ Activity LOW ｜ 7D
11-06  C +0.1k / P +94 ｜ Activity MEDIUM △ ｜ 14D
11-13  C +0.2k / P +0 ｜ Activity MEDIUM △ ｜ 21D
11-20  C +2.3k / P +81 ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 7.4k / P 54.2k，今日变化ΔOI: C +0.2k / P +2，平值价格ATM: C $3.02 / P $3.20 ｜ ATM IV 36.9%，净 delta 敞口 4k shares
Top ΔOI: P 150 -119 ｜ P 152 +110 ｜ C 160 +98
仓位参考: Max Pain 152 ｜ Call Wall 155（+4.2%）（OI 1.8k） ｜ Put Wall 140（-5.9%，弱）（OI 16.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,090 股

11-06（MEDIUM △）Top ΔOI: 136P +81 ｜ 160C +39
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 154（+3.5%，弱）（OI 0.1k） ｜ Put Wall 151（+1.5%）（OI 0.6k）

11-13（MEDIUM △）Top ΔOI: 158C +74 ｜ 157C +53
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 150（+0.8%）（OI 0.2k） ｜ Put Wall 153（+2.8%，弱）（OI 0.4k）

11-20（MEDIUM △）Top ΔOI: 165C +1,964
11-20（MEDIUM △）仓位参考: Max Pain 154 ｜ Put Wall 145（-2.6%，弱）（OI 7.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/XBI_morning.json