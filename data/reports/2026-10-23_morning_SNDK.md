# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $760.51 ｜ QQQ $703.64
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 20.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 1300C ΔOI +539（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,260.93 → 今开 1,269.00（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 1294.33 ｜ 低 1258.03

Options: P/C成交量 0.82 | OI比 0.70 | ATM IV 118.3% | Skew 9.3pp | Term 0.66 | ExpMove ±11.6%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 9.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±11.6% ｜ 11-06（14D）±14.4% ｜ 11-13（21D）±15.8% ｜ 11-20（28D）±17.4%
   ⇒ IV–VIX Spread: +98.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,926,810 | GEX Change vs 上次快照 7,692,505 | Flip: Primary Flip: 1300.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 1833 / LOW 624 / INVALID 1101
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1300.83（全链重定价，覆盖 95%）
Put Wall 1,200（弱结构｜现价高于该位 7.1%）
最近结构参考: Flip 1301（现价低于该位 1.2%）
量化视角： 负 Gamma（193万，无历史分位）｜负 Gamma 缓解（+769万）｜现价位于 Flip 下方 1.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,200（Put Wall，弱结构）；上方 1,325（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1301（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 1500.0C — Vol 2,940 | 最新价 $39.00 | OI 2269→4409 (ΔOI +2140张) | ΔOI/Volume 72.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2140张（+94.3% vs前日OI），连续性待观察（方向未知）
10-23 1200.0P — Vol 7,082 | 最新价 $7.56 | OI 1220→3062 (ΔOI +1842张) | ΔOI/Volume 26.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1842张（+151.0% vs前日OI），连续性待观察（方向未知）
10-23 1300.0C — Vol 5,951 | 最新价 $12.20 | OI 459→1588 (ΔOI +1129张) | ΔOI/Volume 19.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1129张（+246.0% vs前日OI），连续性待观察（方向未知）
10-23 1400.0C — Vol 7,624 | 最新价 $0.90 | OI 1107→2188 (ΔOI +1081张) | ΔOI/Volume 14.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1081张（+97.7% vs前日OI），连续性待观察（方向未知）
10-30 750.0P — Vol 1,017 | 最新价 $0.57 | OI 0→1010 (ΔOI +1010张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1010张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,202 张（Put 2,852 / Call 4,350），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 59.0k / P 41.6k，今日成交量: C 14.5k / P 12.0k，平值价格ATM: C $17.50 / P $15.40 ｜ ATM IV 118.3%，预期波动 ±2.6%，Max Pain 1,325
Top ΔOI: P 1200 +1,842 ｜ C 1300 +1,129 ｜ C 1400 +1,081

📆 Forward Expiration Structure

10-30  C +3.1k / P +2.6k ｜ Activity MEDIUM △ ｜ 7D
11-06  C +1.1k / P +0.7k ｜ Activity MEDIUM △ ｜ 14D
11-13  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +4.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 31.3k / P 21.2k，今日变化ΔOI: C +3.1k / P +2.6k，平值价格ATM: C $76.10 / P $73.22 ｜ ATM IV 102.3%，净 delta 敞口 99k shares
Top ΔOI: P 750 +1,010 ｜ C 1300 +539
仓位参考: Max Pain 1,425 ｜ Call Wall 1300（+1.1%，弱）（OI 1.0k） ｜ Put Wall 1350（+5.0%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 102.3%｜历史 Rank 77%（近端代理）｜IV/RV 1.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 98,600 股

11-06（MEDIUM △）Top ΔOI: 1240P +197 ｜ 1700C +142
11-06（MEDIUM △）仓位参考: Max Pain 1,465 ｜ Call Wall 1400（+8.9%，弱）（OI 0.7k） ｜ Put Wall 1200（-6.6%）（OI 0.7k）

11-13（MEDIUM △）Top ΔOI: 900P +117 ｜ 1500P +94
11-13（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Call Wall 1320（+2.7%，弱）（OI 86） ｜ Put Wall 1300（+1.1%，弱）（OI 0.1k）

11-20（MEDIUM △）Top ΔOI: 1500C +2,140 ｜ 1000P +465
11-20（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Put Wall 1200（-6.6%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SNDK_morning.json