# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.40 ｜ QQQ $714.88
VIX 15.78 ↓11.6%（5D +8.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.2　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 3.4 ｜ 前值 3.4　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 2.4 ｜ 前值 2.5　✅ 今日已公布
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 47.8 ｜ 前值 51.7　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-14 730C ΔOI +5,291（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 708.69 → 今开 715.44（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 717.04 ｜ 低 713.93

Options: P/C成交量 1.23 | OI比 1.44 | ATM IV 19.8% | Skew 3.7pp | Term 0.91 | ExpMove ±0.9%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 3.7pp）｜当日成交偏 Put（P/C量 1.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.44×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 49% ｜ P/C OI(近端) 32%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 49%）｜近端持仓结构中性（P/C OI 分位 32%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-14（3D）±0.9% ｜ 09-15（4D）±1.1% ｜ 09-16（5D）±1.5% ｜ 09-17（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -31,428,996 | GEX Change vs 上次快照 658,841,772 | Flip: Primary Flip: 716.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2973 / LOW 464 / INVALID 2367
结构观察区: Primary Flip 716.82（全链重定价，覆盖 95%）
Put Wall 700（弱结构｜现价高于该位 2.3%） | Call Wall 750（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 717（现价低于该位 0.1%）
量化视角： 负 Gamma（3143万，历史分位 49%，中性区）｜负 Gamma 缓解（+6.59亿）｜现价位于 Flip 下方 0.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 712（MaxPain，仅结算参考）；上方 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 717（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 675.0P — Vol 30,519 | 最新价 $1.77 | OI 21099→43643 (ΔOI +22544张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22544张（+106.8% vs前日OI），连续性待观察（方向未知）
09-18 700.0P — Vol 50,952 | 最新价 $5.56 | OI 102500→118265 (ΔOI +15765张) | ΔOI/Volume 30.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15765张（+15.4% vs前日OI），连续性待观察（方向未知）
09-30 720.0C — Vol 10,857 | 最新价 $7.80 | OI 21240→31305 (ΔOI +10065张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10065张（+47.4% vs前日OI），连续性待观察（方向未知）
09-30 735.0C — Vol 10,769 | 最新价 $2.83 | OI 2310→12322 (ΔOI +10012张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10012张（+433.4% vs前日OI），连续性待观察（方向未知）
09-30 650.0P — Vol 11,799 | 最新价 $2.10 | OI 8664→17620 (ΔOI +8956张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8956张（+103.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 67,342 张（Put 47,265 / Call 20,077），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $15M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +23.6k / P +31.7k ｜ Activity HIGH ｜ 3D
09-15  C +11.4k / P +28.5k ｜ Activity HIGH ｜ 4D
09-16  C +9.1k / P +9.3k ｜ Activity HIGH ｜ 5D
09-17  C +6.8k / P +10.6k ｜ Activity HIGH ｜ 6D

📆 09-14 Forward Structure
存量OI: C 42.5k / P 87.5k，今日变化ΔOI: C +23.6k / P +31.7k，平值价格ATM: C $3.36 / P $2.97 ｜ ATM IV 11.6%，净 delta 敞口 649k shares
Top ΔOI: C 730 +5,291 ｜ C 722 +2,446 ｜ P 684 +2,353
仓位参考: Max Pain 711 ｜ Call Wall 730（+1.9%）（OI 8.3k） ｜ Put Wall 655（-8.6%）（OI 11.9k）
量化解读： 存量 Put 重｜ATM IV 11.6%｜历史 Rank 58%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 649,297 股

📆 09-15 Forward Structure
存量OI: C 24.9k / P 78.0k，今日变化ΔOI: C +11.4k / P +28.5k，平值价格ATM: C $4.29 / P $3.92 ｜ ATM IV 13.2%，净 delta 敞口 137k shares
Top ΔOI: P 650 +7,307 ｜ P 645 +5,022 ｜ P 696 +3,056
仓位参考: Max Pain 715 ｜ Call Wall 730（+1.9%，弱）（OI 5.2k） ｜ Put Wall 650（-9.3%）（OI 15.7k）
量化解读： 存量 Put 重｜ATM IV 13.2%｜历史 Rank 58%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 136,952 股

📆 09-16 Forward Structure
存量OI: C 17.3k / P 27.8k，今日变化ΔOI: C +9.1k / P +9.3k，平值价格ATM: C $5.76 / P $5.14 ｜ ATM IV 15.9%，净 delta 敞口 228k shares
Top ΔOI: P 677 +3,377 ｜ C 740 +1,035 ｜ C 735 +713
仓位参考: Max Pain 710 ｜ Call Wall 740（+3.3%，弱）（OI 2.0k） ｜ Put Wall 677（-5.5%）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 15.9%｜历史 Rank 58%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 227,689 股

📆 09-17 Forward Structure
存量OI: C 11.9k / P 21.4k，今日变化ΔOI: C +6.8k / P +10.6k，平值价格ATM: C $6.80 / P $5.98 ｜ ATM IV 16.9%，净 delta 敞口 171k shares
Top ΔOI: C 725 +1,045 ｜ P 690 +808 ｜ C 726 +700
仓位参考: Max Pain 710 ｜ Call Wall 725（+1.2%）（OI 1.7k） ｜ Put Wall 690（-3.7%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 16.9%｜历史 Rank 58%（近端代理）｜净 delta 敞口 正 171,281 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/QQQ_morning.json