# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $776.00 ｜ QQQ $749.70
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 42.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-12 775C ΔOI +3,850（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-15 690P ΔOI +9,810 占该期限总 OI 15.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 747.58 → 今开 752.55（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 752.86 ｜ 低 748.36

Options: P/C成交量 0.98 | OI比 2.05 | ATM IV 20.3% | Skew 3.0pp | Term 0.91 | ExpMove ±0.8%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 3.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.05×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 41% ｜ P/C OI(近端) 79%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 41%）｜近端持仓结构中性（P/C OI 分位 79%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-12（3D）±0.8% ｜ 10-13（4D）±1.1% ｜ 10-14（5D）±1.4% ｜ 10-15（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -149,594,479 | GEX Change vs 上次快照 111,704,028 | Flip: Primary Flip: 750.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3112 / LOW 274 / INVALID 1536
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 750.41（全链重定价，覆盖 97%）
Call Wall 760（弱结构｜现价低于该位 1.5%）
最近结构参考: Flip 750（现价低于该位 0.2%）
量化视角： 负 Gamma（1.50亿，历史分位 41%，中性区）｜负 Gamma 缓解（+1.12亿）｜现价位于 Flip 下方 0.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 748（MaxPain，仅结算参考）；上方 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 750（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 717.0P — Vol 18,288 | 最新价 $1.06 | OI 4166→21007 (ΔOI +16841张) | ΔOI/Volume 92.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16841张（+404.2% vs前日OI），连续性待观察（方向未知）
10-09 575.0P — Vol 16,688 | 最新价 $0.01 | OI 1530→18035 (ΔOI +16505张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16505张（+1078.8% vs前日OI），连续性待观察（方向未知）
10-09 600.0P — Vol 17,327 | 最新价 $0.01 | OI 2437→18857 (ΔOI +16420张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16420张（+673.8% vs前日OI），连续性待观察（方向未知）
10-16 734.0P — Vol 21,508 | 最新价 $2.87 | OI 7122→23159 (ΔOI +16037张) | ΔOI/Volume 74.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16037张（+225.2% vs前日OI），连续性待观察（方向未知）
10-09 735.0P — Vol 28,526 | 最新价 $0.27 | OI 7912→20613 (ΔOI +12701张) | ΔOI/Volume 44.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12701张（+160.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 78,504 张（Put 78,504 / Call 0），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 260.6k / P 533.7k，今日成交量: C 444.4k / P 454.2k，平值价格ATM: C $1.65 / P $1.65 ｜ ATM IV 20.3%，预期波动 ±0.4%，Max Pain 748
Top ΔOI: P 575 +16,505 ｜ P 600 +16,420 ｜ P 735 +12,701

📆 Forward Expiration Structure

10-12  C +39.3k / P +30.3k ｜ Activity HIGH ｜ 3D
10-13  C +9.1k / P +15.1k ｜ Activity HIGH ｜ 4D
10-14  C +5.4k / P +11.2k ｜ Activity HIGH ｜ 5D
10-15  C +6.7k / P +26.5k ｜ Activity HIGH ｜ 6D

📆 10-12 Forward Structure
存量OI: C 70.1k / P 157.0k，今日变化ΔOI: C +39.3k / P +30.3k，平值价格ATM: C $3.15 / P $3.16 ｜ ATM IV 11.1%，净 delta 敞口 541k shares
Top ΔOI: C 775 +3,850 ｜ C 755 +3,682 ｜ P 735 +2,885
仓位参考: Max Pain 750 ｜ Call Wall 755（+0.8%，弱）（OI 5.2k） ｜ Put Wall 738（-1.5%，弱）（OI 13.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.1%｜历史 Rank 62%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 540,584 股

📆 10-13 Forward Structure
存量OI: C 26.5k / P 92.3k，今日变化ΔOI: C +9.1k / P +15.1k，平值价格ATM: C $4.00 / P $4.02 ｜ ATM IV 12.4%，净 delta 敞口 34k shares
Top ΔOI: P 731 +3,207 ｜ P 723 +3,110 ｜ P 692 -2,006
仓位参考: Max Pain 751 ｜ Call Wall 770（+2.8%，弱）（OI 1.8k） ｜ Put Wall 740（-1.2%，弱）（OI 11.2k）
量化解读： 存量 Put 重｜ATM IV 12.4%｜历史 Rank 62%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 33,632 股

📆 10-14 Forward Structure
存量OI: C 20.1k / P 47.2k，今日变化ΔOI: C +5.4k / P +11.2k，平值价格ATM: C $5.27 / P $4.96 ｜ ATM IV 14.4%，净 delta 敞口 -95k shares
Top ΔOI: P 710 +1,690 ｜ C 770 +1,642
仓位参考: Max Pain 752 ｜ Call Wall 770（+2.8%，弱）（OI 2.3k） ｜ Put Wall 730（-2.5%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 14.4%｜历史 Rank 62%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 负 94,561 股

📆 10-15 Forward Structure
存量OI: C 16.6k / P 45.1k，今日变化ΔOI: C +6.7k / P +26.5k，平值价格ATM: C $6.29 / P $5.59 ｜ ATM IV 15.1%，净 delta 敞口 -16k shares
Top ΔOI: P 690 +9,810 ｜ P 734 +1,470
仓位参考: Max Pain 750 ｜ Call Wall 763（+1.9%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 15.1%｜历史 Rank 62%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 16,196 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/QQQ_morning.json