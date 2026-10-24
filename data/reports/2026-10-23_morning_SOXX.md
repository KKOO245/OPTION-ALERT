# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $759.97 ｜ QQQ $704.40
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
🟡 **近现价集中开仓**: 10-30 500C ΔOI +2,667（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 475.69 → 今开 474.55（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 481.30 ｜ 低 473.10

Options: P/C成交量 4.52 | OI比 1.51 | ATM IV 68.9% | Skew 25.0pp | Term 0.65 | ExpMove ±5.5%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价显著（Skew 25.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 4.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.52×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.51×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±5.5% ｜ 11-06（14D）±7.5% ｜ 11-13（21D）±9.4% ｜ 11-20（28D）±9.7%
   ⇒ IV–VIX Spread: +49.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -39,838,524 | GEX Change vs 上次快照 -2,491,127 | Flip: Primary Flip: 526.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 611 / LOW 320 / INVALID 653
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 526.27（全链重定价，覆盖 95%）
最近结构参考: Flip 526（现价低于该位 8.7%）
量化视角： 负 Gamma（3984万，无历史分位）｜负 Gamma 加深（249万）｜现价位于 Flip 下方 8.73%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 526（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 470.0P — Vol 5,216 | 最新价 $4.10 | OI 219→5038 (ΔOI +4819张) | ΔOI/Volume 92.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4819张（+2200.5% vs前日OI），连续性待观察（方向未知）
10-30 525.0C — Vol 5,327 | 最新价 $1.90 | OI 2726→6595 (ΔOI +3869张) | ΔOI/Volume 72.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3869张（+141.9% vs前日OI），连续性待观察（方向未知）
10-23 450.0P — Vol 4,954 | 最新价 $0.70 | OI 965→4482 (ΔOI +3517张) | ΔOI/Volume 71.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3517张（+364.5% vs前日OI），连续性待观察（方向未知）
10-30 500.0C — Vol 2,904 | 最新价 $5.70 | OI 230→2897 (ΔOI +2667张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2667张（+1159.6% vs前日OI），连续性待观察（方向未知）
11-27 550.0C — Vol 1,718 | 最新价 $5.45 | OI 149→1789 (ΔOI +1640张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1640张（+1100.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,512 张（Put 8,336 / Call 8,176），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 16.1k / P 24.3k，今日成交量: C 1.8k / P 8.3k，平值价格ATM: C $3.50 / P $3.67 ｜ ATM IV 68.9%，预期波动 ±1.5%，Max Pain 500
Top ΔOI: P 470 +4,819 ｜ P 450 +3,517 ｜ P 550 -1,267

📆 Forward Expiration Structure

10-30  C +8.0k / P +1.6k ｜ Activity HIGH ｜ 7D
11-06  C -0.4k / P +0.7k ｜ Activity MEDIUM △ ｜ 14D
11-13  C +0.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +0.9k / P +3.7k ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 29.0k / P 147.3k，今日变化ΔOI: C +8.0k / P +1.6k，平值价格ATM: C $12.80 / P $13.40 ｜ ATM IV 49.9%，净 delta 敞口 206k shares
Top ΔOI: C 525 +3,869 ｜ C 500 +2,667 ｜ P 470 +1,352
仓位参考: Max Pain 520 ｜ Call Wall 500（+4.1%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 206,181 股

11-06（MEDIUM △）Top ΔOI: 465P +408 ｜ 440P +406
11-06（MEDIUM △）仓位参考: Max Pain 520 ｜ Put Wall 455（-5.3%，弱）（OI 0.8k）

11-13（MEDIUM △）Top ΔOI: 485P +122
11-13（MEDIUM △）仓位参考: Max Pain 520 ｜ Put Wall 460（-4.2%）（OI 3.2k）

11-20（MEDIUM △）Top ΔOI: 440P +1,281 ｜ 430P +881
11-20（MEDIUM △）仓位参考: Max Pain 560 ｜ Put Wall 460（-4.2%，弱）（OI 7.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SOXX_morning.json