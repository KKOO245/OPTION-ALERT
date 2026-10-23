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
🟡 **近现价集中开仓**: 11-06 10C ΔOI +104（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 9P ΔOI +2,966 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 9.63 → 今开 9.54（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 9.58 ｜ 低 9.26

Options: P/C成交量 0.48 | OI比 0.18 | ATM IV 121.3% | Skew 21.4pp | Term 0.72 | ExpMove ±9.1%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 21.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.18×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±9.1% ｜ 11-06（14D）±13.4% ｜ 11-13（21D）±18.1% ｜ 11-20（28D）±19.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 544,105 | GEX Change vs 上次快照 1,591,258 | Flip: Primary Flip: 9.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 204 / LOW 76 / INVALID 160
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.45（全链重定价，覆盖 90%）
Put Wall 10（现价低于该位 4.5%）
最近结构参考: Flip 9（现价高于该位 1.1%）
量化视角： 正 Gamma（54万，无历史分位）｜由负转正（+159万）｜现价位于 Flip 上方 1.09%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 9.0P — Vol 3,367 | 最新价 $0.20 | OI 674→3640 (ΔOI +2966张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2966张（+440.1% vs前日OI），连续性待观察（方向未知）
10-23 10.5C — Vol 1,404 | 最新价 $0.03 | OI 2510→3053 (ΔOI +543张) | ΔOI/Volume 38.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增543张（+21.6% vs前日OI），连续性待观察（方向未知）
11-20 10.5P — Vol 581 | 最新价 $1.53 | OI 1288→1739 (ΔOI +451张) | ΔOI/Volume 77.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增451张（+35.0% vs前日OI），连续性待观察（方向未知）
11-20 16.0C — Vol 445 | 最新价 $0.06 | OI 1499→1916 (ΔOI +417张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增417张（+27.8% vs前日OI），连续性待观察（方向未知）
10-23 10.0C — Vol 2,584 | 最新价 $0.07 | OI 2472→2879 (ΔOI +407张) | ΔOI/Volume 15.8% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增407张（+16.5% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,784 张（Put 3,417 / Call 1,367），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 27.2k / P 4.8k，今日成交量: C 0.5k / P 0.2k，平值价格ATM: C $0.14 / P $0.11 ｜ ATM IV 121.3%，预期波动 ±2.6%，Max Pain 10
Top ΔOI: P 12 -604 ｜ C 10 +543 ｜ C 10 +407

📆 Forward Expiration Structure

10-30  C +0.5k / P -0.2k ｜ Activity MEDIUM △ ｜ 7D
11-06  C +0.3k / P -99 ｜ Activity HIGH ｜ 14D
11-13  C +0.2k / P -0.8k ｜ Activity HIGH ｜ 21D
11-20  C +0.6k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 19.4k / P 8.8k，今日变化ΔOI: C +0.5k / P -0.2k，平值价格ATM: C $0.45 / P $0.42 ｜ ATM IV 80.7%，净 delta 敞口 260k shares
Top ΔOI: P 9 +2,966 ｜ P 14 -2,090 ｜ P 13 -523
仓位参考: Max Pain 11 ｜ Call Wall 10（+4.7%，弱）（OI 0.9k） ｜ Put Wall 9（-5.8%）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 80.7%｜历史 Rank 58%（近端代理）｜IV/RV 1.41×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 260,410 股

📆 11-06 Forward Structure
存量OI: C 5.2k / P 4.3k，今日变化ΔOI: C +0.3k / P -99，平值价格ATM: C $0.65 / P $0.63 ｜ ATM IV 87.2%，净 delta 敞口 26k shares
Top ΔOI: C 10 +104 ｜ P 15 -98 ｜ C 9 +52
仓位参考: Max Pain 12 ｜ Put Wall 9（-5.8%）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 87.2%｜历史 Rank 58%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 正 26,039 股

📆 11-13 Forward Structure
存量OI: C 2.7k / P 2.6k，今日变化ΔOI: C +0.2k / P -0.8k，平值价格ATM: C $0.87 / P $0.86 ｜ ATM IV 87.6%，净 delta 敞口 86k shares
Top ΔOI: P 16 -505 ｜ P 17 -296 ｜ C 10 +102
仓位参考: Max Pain 12 ｜ Call Wall 10.5（+9.9%，弱）（OI 0.4k） ｜ Put Wall 10.5（+9.9%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 87.6%｜历史 Rank 58%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 正 86,371 股

📆 11-20 Forward Structure
存量OI: C 24.0k / P 26.4k，今日变化ΔOI: C +0.6k / P +0.9k，平值价格ATM: C $0.93 / P $0.93 ｜ ATM IV 87.8%，净 delta 敞口 -8k shares
Top ΔOI: P 10 +451
仓位参考: Max Pain 14 ｜ Put Wall 10（+4.7%，弱）（OI 8.2k）
量化解读： 存量两侧均衡｜ATM IV 87.8%｜历史 Rank 58%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 负 8,025 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/USAR_morning.json