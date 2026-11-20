# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $693.35 ｜ QQQ $608.45
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 108.87 → 今开 107.01（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 111.09 ｜ 低 106.86

Options: P/C成交量 4.09 | OI比 0.35 | ATM IV 56.1% | Skew -23.6pp | Term 1.31 | ExpMove ±8.8%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常偏陡（Term 1.31）｜Put 保护异常便宜（Skew -23.6pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.35）+ 当日成交偏 Put（P/C量 4.09）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 4.09×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±8.8% ｜ 12-04（14D）±10.9% ｜ 12-11（21D）±15.1% ｜ 12-18（28D）±16.4%
   ⇒ IV–VIX Spread: +28.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,399,747 | GEX Change vs 上次快照 9,448,191 | Flip: Primary Flip: 109.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 334 / LOW 256 / INVALID 137
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 109.80（全链重定价，覆盖 99%）
Put Wall 110（现价低于该位 1.6%）
最近结构参考: Flip 110（现价低于该位 1.4%）
量化视角： 负 Gamma（440万，无历史分位）｜负 Gamma 缓解（+945万）｜现价位于 Flip 下方 1.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 110（Put Wall） / 125（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 110（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 121.0C — Vol 2,200 | 最新价 $1.25 | OI 219→2218 (ΔOI +1999张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1999张（+912.8% vs前日OI），连续性待观察（方向未知）
11-27 120.0C — Vol 1,654 | 最新价 $1.14 | OI 2388→3389 (ΔOI +1001张) | ΔOI/Volume 60.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1001张（+41.9% vs前日OI），连续性待观察（方向未知）
11-20 115.0C — Vol 1,853 | 最新价 $0.40 | OI 822→1259 (ΔOI +437张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增437张（+53.2% vs前日OI），连续性待观察（方向未知）
11-20 100.0P — Vol 1,535 | 最新价 $0.23 | OI 2982→3303 (ΔOI +321张) | ΔOI/Volume 20.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增321张（+10.8% vs前日OI），连续性待观察（方向未知）
11-27 115.0C — Vol 705 | 最新价 $2.35 | OI 263→577 (ΔOI +314张) | ΔOI/Volume 44.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增314张（+119.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,072 张（Put 321 / Call 3,751），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 133.6k / P 46.3k，今日成交量: C 4.7k / P 19.1k，平值价格ATM: C $1.79 / P $1.33 ｜ ATM IV 56.1%，预期波动 ±2.9%，Max Pain 125
Top ΔOI: P 130 -3,701 ｜ P 125 -2,047 ｜ P 122 -1,240

📆 Forward Expiration Structure

11-27  C +4.0k / P +0.1k ｜ Activity HIGH ｜ 7D
12-04  C +0.3k / P -0.8k ｜ Activity MEDIUM △ ｜ 14D
12-11  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 21D
12-18  C +0.2k / P -3.7k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 18.7k / P 10.9k，今日变化ΔOI: C +4.0k / P +0.1k，平值价格ATM: C $5.00 / P $4.55 ｜ ATM IV 67.4%，净 delta 敞口 103k shares
Top ΔOI: C 121 +1,999 ｜ C 120 +1,001 ｜ C 115 +314
仓位参考: Max Pain 120 ｜ Put Wall 100（-7.7%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 67.4%｜历史 Rank 5%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 103,090 股

12-04（MEDIUM △）Top ΔOI: 160P -422 ｜ 150P -323
12-04（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 100（-7.7%，弱）（OI 1.8k）

12-11（MEDIUM △）Top ΔOI: 100P +134
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 110（+1.6%，弱）（OI 0.1k） ｜ Put Wall 100（-7.7%，弱）（OI 0.7k）

12-18（MEDIUM △）Top ΔOI: 170P -2,779 ｜ 165P -590
12-18（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 110（+1.6%）（OI 8.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/COIN_morning.json