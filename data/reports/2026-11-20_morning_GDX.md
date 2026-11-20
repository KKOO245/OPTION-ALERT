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

🔍 重点速览
🔵 **期限 OI 集中**: 11-23 72P ΔOI -463 占该期限总 OI 26.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 72.00 → 今开 70.71（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 71.77 ｜ 低 70.20

Options: P/C成交量 4.53 | OI比 0.65 | ATM IV 37.6% | Skew -26.8pp | Term 1.37 | ExpMove ±1.7% | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常偏陡（Term 1.37）｜Put 保护异常便宜（Skew -26.8pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.65）+ 当日成交偏 Put（P/C量 4.53）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 4.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±6.2% ｜ 12-04（14D）±9.8%
   ⇒ IV–VIX Spread: +10.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -88,228,724 | GEX Change vs 上次快照 3,175,802 | Flip: Primary Flip: 73.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 411 / LOW 252 / INVALID 150
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 73.04（全链重定价，覆盖 96%）
Put Wall 67（弱结构｜现价高于该位 5.2%）
最近结构参考: Flip 73（现价低于该位 3.5%）
量化视角： 负 Gamma（8823万，无历史分位）｜负 Gamma 缓解（+318万）｜现价位于 Flip 下方 3.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 67（Put Wall，弱结构）；上方 76（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 73（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 75.0C — Vol 11,587 | 最新价 $1.00 | OI 147→11309 (ΔOI +11162张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11162张（+7593.2% vs前日OI），连续性待观察（方向未知）
11-20 75.0C — Vol 6,364 | 最新价 $0.13 | OI 1832→7216 (ΔOI +5384张) | ΔOI/Volume 84.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5384张（+293.9% vs前日OI），连续性待观察（方向未知）
11-27 78.0C — Vol 5,247 | 最新价 $0.35 | OI 139→5252 (ΔOI +5113张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5113张（+3678.4% vs前日OI），连续性待观察（方向未知）
12-18 80.0C — Vol 6,413 | 最新价 $1.38 | OI 8693→13741 (ΔOI +5048张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5048张（+58.1% vs前日OI），连续性待观察（方向未知）
11-27 79.0C — Vol 5,066 | 最新价 $0.26 | OI 196→5236 (ΔOI +5040张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5040张（+2571.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 31,747 张（Put 0 / Call 31,747），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 166.1k / P 108.6k，今日成交量: C 3.1k / P 13.8k，平值价格ATM: C $0.71 / P $0.47 ｜ ATM IV 37.6%，预期波动 ±1.7%，Max Pain 76
Top ΔOI: P 80 -16,999 ｜ P 70 -8,053 ｜ C 75 +5,384

📆 Forward Expiration Structure

11-23  C -2 / P -0.4k ｜ Activity MEDIUM △ ｜ 3D
11-25  C +21 / P -0.2k ｜ Activity MEDIUM △ ｜ 5D
11-27  C +22.5k / P -38 ｜ Activity HIGH ｜ 7D
12-04  C +0.7k / P +0.5k ｜ Activity HIGH ｜ 14D

📆 11-23 Forward Structure
存量OI: C 1.0k / P 0.8k，今日变化ΔOI: C -2 / P -0.4k，ATM IV 36.3%，净 delta 敞口 44k shares
Top ΔOI: P 72 -463 ｜ P 70 +182
仓位参考: Max Pain 80 ｜ Put Wall 70（-0.7%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 36.3%｜历史 Rank 44%（近端代理）｜IV/RV 0.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 44,027 股

11-25（MEDIUM △）Top ΔOI: 84P -64 ｜ 85P -50
11-25（MEDIUM △）仓位参考: Max Pain 80 ｜ Put Wall 73（+3.5%，弱）（OI 28）

📆 11-27 Forward Structure
存量OI: C 52.3k / P 7.8k，今日变化ΔOI: C +22.5k / P -38，平值价格ATM: C $2.90 / P $1.47 ｜ ATM IV 53.2%，净 delta 敞口 354k shares
Top ΔOI: C 75 +11,162 ｜ C 78 +5,113 ｜ C 79 +5,040
仓位参考: Max Pain 75 ｜ Call Wall 75（+6.4%，弱）（OI 11.3k） ｜ Put Wall 70（-0.7%）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 53.2%｜历史 Rank 44%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 354,171 股

📆 12-04 Forward Structure
存量OI: C 8.0k / P 13.7k，今日变化ΔOI: C +0.7k / P +0.5k，平值价格ATM: C $4.35 / P $2.58 ｜ ATM IV 55.4%，净 delta 敞口 28k shares
Top ΔOI: P 65 +930 ｜ P 88 -176
仓位参考: Max Pain 82 ｜ Put Wall 70（-0.7%）（OI 6.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 55.4%｜历史 Rank 44%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 27,809 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/GDX_morning.json