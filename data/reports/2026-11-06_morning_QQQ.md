# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $740.12 ｜ QQQ $660.07
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-09 660C ΔOI +6,094（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 647.05 → 今开 658.35（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 664.52 ｜ 低 655.17

Options: P/C成交量 0.72 | OI比 0.89 | ATM IV 56.7% | Skew 8.1pp | Term 0.51 | ExpMove ±2.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.51，近月 IV 高于远月）｜保护溢价显著（Skew 8.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 25% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 25%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-09（3D）±2.3% ｜ 11-10（4D）±2.9% ｜ 11-11（5D）±3.4% ｜ 11-12（6D）±3.6%
   ⇒ IV–VIX Spread: +31.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -387,287,837 | GEX Change vs 上次快照 191,795,433 | Flip: Primary Flip: 684.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2945 / LOW 230 / INVALID 2217
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 684.02（全链重定价，覆盖 93%）
Put Wall 650（弱结构｜现价高于该位 1.7%）
最近结构参考: Put Wall 650（现价高于该位 1.7%）
量化视角： 负 Gamma（3.87亿，历史分位 25%，中性区）｜负 Gamma 缓解（+1.92亿）｜现价位于 Flip 下方 3.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 650（Put Wall，弱结构）；上方 680（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 684（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 650.0P — Vol 73,423 | 最新价 $17.59 | OI 32092→61638 (ΔOI +29546张) | ΔOI/Volume 40.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29546张（+92.1% vs前日OI），连续性待观察（方向未知）
11-20 680.0C — Vol 32,499 | 最新价 $6.42 | OI 657→23996 (ΔOI +23339张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23339张（+3552.4% vs前日OI），连续性待观察（方向未知）
11-06 670.0C — Vol 66,899 | 最新价 $1.02 | OI 170→19836 (ΔOI +19666张) | ΔOI/Volume 29.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19666张（+11568.2% vs前日OI），连续性待观察（方向未知）
11-20 670.0C — Vol 29,852 | 最新价 $9.77 | OI 797→17992 (ΔOI +17195张) | ΔOI/Volume 57.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17195张（+2157.5% vs前日OI），连续性待观察（方向未知）
11-06 650.0P — Vol 90,432 | 最新价 $9.30 | OI 10845→24814 (ΔOI +13969张) | ΔOI/Volume 15.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13969张（+128.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 103,715 张（Put 43,515 / Call 60,200），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $65M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 625.9k / P 555.0k，今日成交量: C 527.8k / P 381.1k，平值价格ATM: C $3.84 / P $4.22 ｜ ATM IV 56.7%，预期波动 ±1.2%，Max Pain 680
Top ΔOI: P 713 -34,798 ｜ C 670 +19,666 ｜ P 700 -15,872

📆 Forward Expiration Structure

11-09  C +57.3k / P +14.8k ｜ Activity HIGH ｜ 3D
11-10  C +18.9k / P +7.8k ｜ Activity HIGH ｜ 4D
11-11  C +11.5k / P +12.4k ｜ Activity HIGH ｜ 5D
11-12  C +18.4k / P +12.9k ｜ Activity HIGH ｜ 6D

📆 11-09 Forward Structure
存量OI: C 98.6k / P 102.2k，今日变化ΔOI: C +57.3k / P +14.8k，平值价格ATM: C $7.54 / P $7.76 ｜ ATM IV 30.5%，净 delta 敞口 2.1M shares
Top ΔOI: C 660 +6,094 ｜ C 680 +5,293 ｜ C 670 +4,105
仓位参考: Max Pain 663 ｜ Call Wall 660（-0.2%，弱）（OI 6.1k） ｜ Put Wall 650（-1.7%，弱）（OI 4.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 30.5%｜历史 Rank 100%（近端代理）｜IV/RV 0.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,116,855 股

📆 11-10 Forward Structure
存量OI: C 59.1k / P 28.1k，今日变化ΔOI: C +18.9k / P +7.8k，平值价格ATM: C $9.70 / P $9.49 ｜ ATM IV 33.8%，净 delta 敞口 523k shares
Top ΔOI: C 672 +3,599 ｜ C 660 +2,026 ｜ C 670 +1,434
仓位参考: Max Pain 670 ｜ Call Wall 672（+1.6%，弱）（OI 3.6k） ｜ Put Wall 650（-1.7%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 33.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 523,275 股

📆 11-11 Forward Structure
存量OI: C 33.5k / P 29.9k，今日变化ΔOI: C +11.5k / P +12.4k，平值价格ATM: C $11.45 / P $10.97 ｜ ATM IV 34.6%，净 delta 敞口 177k shares
Top ΔOI: C 690 +1,454 ｜ P 605 +1,338 ｜ P 635 +1,177
仓位参考: Max Pain 676 ｜ Call Wall 670（+1.3%，弱）（OI 0.9k） ｜ Put Wall 645（-2.5%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 177,200 股

📆 11-12 Forward Structure
存量OI: C 37.7k / P 26.1k，今日变化ΔOI: C +18.4k / P +12.9k，平值价格ATM: C $12.10 / P $12.04 ｜ ATM IV 35.1%，净 delta 敞口 272k shares
Top ΔOI: C 685 +2,543 ｜ C 695 +2,434 ｜ C 656 +1,709
仓位参考: Max Pain 667 ｜ Call Wall 656（-0.8%，弱）（OI 1.7k） ｜ Put Wall 656（-0.8%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 35.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 272,417 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/QQQ_morning.json