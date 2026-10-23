# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $760.51 ｜ QQQ $703.91
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
🟡 **近现价集中开仓**: 10-26 695P ΔOI +9,999（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-27 735C ΔOI +16,901 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 704.47 → 今开 702.10（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 706.10 ｜ 低 701.16

Options: P/C成交量 0.89 | OI比 1.35 | ATM IV 37.3% | Skew 2.9pp | Term 0.67 | ExpMove ±1.7%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.35×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 6% ｜ P/C OI(近端) 25%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 6%）｜近端持仓结构中性（P/C OI 分位 25%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-26（3D）±1.7% ｜ 10-27（4D）±2.1% ｜ 10-28（5D）±2.6% ｜ 10-29（6D）±3.3%
   ⇒ IV–VIX Spread: +17.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -989,105,722 | GEX Change vs 上次快照 172,098,744 | Flip: Primary Flip: 727.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3267 / LOW 215 / INVALID 1306
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 727.53（全链重定价，覆盖 97%）
Put Wall 690（弱结构｜现价高于该位 2.3%）
最近结构参考: Put Wall 690（现价高于该位 2.3%）
量化视角： 负 Gamma（9.89亿，历史分位偏负区，比 94% 的交易日更负）｜负 Gamma 缓解（+1.72亿）｜现价位于 Flip 下方 3.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 690（Put Wall，弱结构）；上方 714（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 728（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 690.0P — Vol 41,481 | 最新价 $6.88 | OI 56642→87035 (ΔOI +30393张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30393张（+53.7% vs前日OI），连续性待观察（方向未知）
11-20 680.0P — Vol 37,172 | 最新价 $11.20 | OI 42477→65697 (ΔOI +23220张) | ΔOI/Volume 62.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23220张（+54.7% vs前日OI），连续性待观察（方向未知）
11-06 693.0P — Vol 20,108 | 最新价 $11.05 | OI 168→20190 (ΔOI +20022张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20022张（+11917.9% vs前日OI），连续性待观察（方向未知）
10-27 735.0C — Vol 31,934 | 最新价 $0.56 | OI 819→17720 (ΔOI +16901张) | ΔOI/Volume 52.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16901张（+2063.6% vs前日OI），连续性待观察（方向未知）
11-03 680.0P — Vol 16,556 | 最新价 $6.02 | OI 217→16083 (ΔOI +15866张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15866张（+7311.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 106,402 张（Put 89,501 / Call 16,901），跨 5 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $79M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 368.0k / P 497.7k，今日成交量: C 372.8k / P 332.2k，平值价格ATM: C $2.74 / P $2.96 ｜ ATM IV 37.3%，预期波动 ±0.8%，Max Pain 714
Top ΔOI: P 710 -26,524 ｜ P 730 -13,195 ｜ C 710 +10,840

📆 Forward Expiration Structure

10-26  C +22.6k / P +46.4k ｜ Activity HIGH ｜ 3D
10-27  C +35.4k / P +26.4k ｜ Activity HIGH ｜ 4D
10-28  C +9.1k / P +6.7k ｜ Activity HIGH ｜ 5D
10-29  C +5.2k / P +9.3k ｜ Activity HIGH ｜ 6D

📆 10-26 Forward Structure
存量OI: C 69.0k / P 133.5k，今日变化ΔOI: C +22.6k / P +46.4k，平值价格ATM: C $5.90 / P $6.00 ｜ ATM IV 22.2%，净 delta 敞口 304k shares
Top ΔOI: P 695 +9,999 ｜ P 690 +3,803
仓位参考: Max Pain 721 ｜ Call Wall 720（+2.0%，弱）（OI 2.1k） ｜ Put Wall 722（+2.3%，弱）（OI 12.6k）
量化解读： 存量 Put 重｜ATM IV 22.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 304,037 股

📆 10-27 Forward Structure
存量OI: C 74.7k / P 88.6k，今日变化ΔOI: C +35.4k / P +26.4k，平值价格ATM: C $7.36 / P $7.44 ｜ ATM IV 24.1%，净 delta 敞口 189k shares
Top ΔOI: C 735 +16,901 ｜ P 680 +10,738
仓位参考: Max Pain 720
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.32×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 189,078 股

📆 10-28 Forward Structure
存量OI: C 29.8k / P 32.9k，今日变化ΔOI: C +9.1k / P +6.7k，平值价格ATM: C $8.99 / P $9.04 ｜ ATM IV 26.4%，净 delta 敞口 87k shares
Top ΔOI: P 710 +1,052 ｜ P 650 +982 ｜ C 720 +822
仓位参考: Max Pain 720 ｜ Call Wall 720（+2.0%，弱）（OI 1.2k） ｜ Put Wall 720（+2.0%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 26.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.45×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 86,980 股

📆 10-29 Forward Structure
存量OI: C 19.7k / P 45.2k，今日变化ΔOI: C +5.2k / P +9.3k，平值价格ATM: C $10.40 / P $12.91 ｜ ATM IV 28.0%，净 delta 敞口 -2k shares
Top ΔOI: P 660 +1,125 ｜ P 655 +1,079 ｜ P 750 -935
仓位参考: Max Pain 719 ｜ Call Wall 720（+2.0%，弱）（OI 0.5k） ｜ Put Wall 700（-0.8%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 28.0%｜历史 Rank 96%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 负 2,330 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/QQQ_morning.json