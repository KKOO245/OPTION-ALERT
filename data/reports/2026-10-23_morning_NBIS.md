# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.05 ｜ QQQ $706.85
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.1（extreme fear）
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


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 159.17 → 今开 158.76（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 162.78 ｜ 低 155.86

Options: P/C成交量 0.36 | OI比 0.49 | ATM IV 136.6% | Skew 0.8pp | Term 0.73 | ExpMove ±11.0%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±11.0% ｜ 11-06（14D）±15.1% ｜ 11-13（21D）±20.4% ｜ 11-20（28D）±23.9%
   ⇒ IV–VIX Spread: +116.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,421,064 | GEX Change vs 上次快照 12,603,939 | Flip: Primary Flip: 165.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 559 / LOW 89 / INVALID 234
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.12（全链重定价，覆盖 99%）
Put Wall 150（弱结构｜现价高于该位 7.6%）
最近结构参考: Flip 165（现价低于该位 2.3%）
量化视角： 负 Gamma（542万，无历史分位）｜负 Gamma 缓解（+1260万）｜现价位于 Flip 下方 2.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 168（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 225.0C — Vol 3,389 | 最新价 $0.22 | OI 4376→7659 (ΔOI +3283张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3283张（+75.0% vs前日OI），连续性待观察（方向未知）
10-23 167.5C — Vol 9,976 | 最新价 $1.19 | OI 864→2747 (ΔOI +1883张) | ΔOI/Volume 18.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1883张（+217.9% vs前日OI），连续性待观察（方向未知）
10-23 162.5C — Vol 6,721 | 最新价 $2.54 | OI 494→2348 (ΔOI +1854张) | ΔOI/Volume 27.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1854张（+375.3% vs前日OI），连续性待观察（方向未知）
10-30 220.0C — Vol 2,592 | 最新价 $0.33 | OI 1648→3423 (ΔOI +1775张) | ΔOI/Volume 68.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1775张（+107.7% vs前日OI），连续性待观察（方向未知）
10-23 150.0P — Vol 10,002 | 最新价 $0.92 | OI 3392→5153 (ΔOI +1761张) | ΔOI/Volume 17.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1761张（+51.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,556 张（Put 1,761 / Call 8,795），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 116.1k / P 56.8k，今日成交量: C 18.8k / P 6.7k，平值价格ATM: C $2.04 / P $2.79 ｜ ATM IV 136.6%，预期波动 ±3.0%，Max Pain 168
Top ΔOI: P 200 -2,301 ｜ C 167 +1,883 ｜ C 162 +1,854

📆 Forward Expiration Structure

10-30  C +11.9k / P +1.8k ｜ Activity HIGH ｜ 7D
11-06  C +1.7k / P -85 ｜ Activity MEDIUM △ ｜ 14D
11-13  C +2.0k / P -26 ｜ Activity MEDIUM △ ｜ 21D
11-20  C +1.7k / P -2.8k ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 66.6k / P 44.0k，今日变化ΔOI: C +11.9k / P +1.8k，平值价格ATM: C $8.50 / P $9.31 ｜ ATM IV 96.1%，净 delta 敞口 236k shares
Top ΔOI: C 225 +3,283 ｜ C 200 +1,247
仓位参考: Max Pain 198 ｜ Call Wall 175（+8.5%，弱）（OI 2.1k） ｜ Put Wall 150（-7.0%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 96.1%｜历史 Rank 85%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 236,253 股

11-06（MEDIUM △）Top ΔOI: 150C +317 ｜ 170C +236
11-06（MEDIUM △）仓位参考: Max Pain 200 ｜ Put Wall 170（+5.4%，弱）（OI 1.6k）

11-13（MEDIUM △）Top ΔOI: 175C +700 ｜ 200C +661
11-13（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 175（+8.5%，弱）（OI 1.0k） ｜ Put Wall 165（+2.3%，弱）（OI 1.4k）

11-20（MEDIUM △）Top ΔOI: 145P -1,766 ｜ 140P -841
11-20（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 170（+5.4%，弱）（OI 2.8k） ｜ Put Wall 150（-7.0%，弱）（OI 8.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/NBIS_morning.json