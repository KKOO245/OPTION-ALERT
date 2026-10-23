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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-26 215C ΔOI +4,281（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 212.21 → 今开 210.94（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 213.32 ｜ 低 210.18

Options: P/C成交量 0.48 | OI比 0.78 | ATM IV 55.4% | Skew 1.5pp | Term 0.78 | ExpMove ±2.4%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.4% ｜ 10-28（5D）±3.6% ｜ 10-30（7D）±4.4% ｜ 11-02（10D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 114,740,129 | GEX Change vs 上次快照 172,332,383 | Flip: Primary Flip: 210.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 716 / LOW 218 / INVALID 528
结构观察区: Primary Flip 210.07（全链重定价，覆盖 94%）
Put Wall 200（弱结构｜现价高于该位 6.5%） | Call Wall 230（弱结构｜现价低于该位 7.4%）
最近结构参考: Flip 210（现价高于该位 1.4%）
量化视角： 正 Gamma（1.15亿，无历史分位）｜由负转正（+1.72亿）｜现价位于 Flip 上方 1.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 215（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 217.5C — Vol 141,666 | 最新价 $0.38 | OI 7687→30850 (ΔOI +23163张) | ΔOI/Volume 16.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23163张（+301.3% vs前日OI），连续性待观察（方向未知）
10-30 225.0C — Vol 43,608 | 最新价 $0.94 | OI 11266→32301 (ΔOI +21035张) | ΔOI/Volume 48.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21035张（+186.7% vs前日OI），连续性待观察（方向未知）
10-30 217.5C — Vol 29,707 | 最新价 $2.76 | OI 2137→23035 (ΔOI +20898张) | ΔOI/Volume 70.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20898张（+977.9% vs前日OI），连续性待观察（方向未知）
10-23 215.0C — Vol 117,613 | 最新价 $0.94 | OI 9041→17514 (ΔOI +8473张) | ΔOI/Volume 7.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8473张（+93.7% vs前日OI），连续性待观察（方向未知）
10-23 205.0P — Vol 31,594 | 最新价 $0.24 | OI 11982→19946 (ΔOI +7964张) | ΔOI/Volume 25.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7964张（+66.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 81,533 张（Put 7,964 / Call 73,569），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 486.5k / P 381.8k，今日成交量: C 211.1k / P 100.7k，平值价格ATM: C $1.48 / P $1.10 ｜ ATM IV 55.4%，预期波动 ±1.2%，Max Pain 215
Top ΔOI: C 217 +23,163 ｜ C 227 -11,467 ｜ C 222 -9,761

📆 Forward Expiration Structure

10-26  C +19.1k / P +8.3k ｜ Activity HIGH ｜ 3D
10-28  C +15.4k / P +5.0k ｜ Activity HIGH ｜ 5D
10-30  C +63.1k / P +17.8k ｜ Activity HIGH ｜ 7D
11-02  C +2.8k / P +1.3k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 61.5k / P 45.6k，今日变化ΔOI: C +19.1k / P +8.3k，平值价格ATM: C $2.77 / P $2.33 ｜ ATM IV 31.5%，净 delta 敞口 514k shares
Top ΔOI: C 215 +4,281 ｜ C 217 +4,057 ｜ C 220 +2,744
仓位参考: Max Pain 215 ｜ Call Wall 225（+5.7%，弱）（OI 7.0k） ｜ Put Wall 200（-6.1%）（OI 10.1k）
量化解读： 存量 Call 重｜ATM IV 31.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.10×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 514,428 股

📆 10-28 Forward Structure
存量OI: C 34.3k / P 22.0k，今日变化ΔOI: C +15.4k / P +5.0k，平值价格ATM: C $4.20 / P $3.54 ｜ ATM IV 37.4%，净 delta 敞口 345k shares
Top ΔOI: C 217 +3,377 ｜ C 215 +2,650 ｜ C 220 +2,370
仓位参考: Max Pain 215 ｜ Call Wall 230（+8.0%，弱）（OI 5.9k） ｜ Put Wall 215（+1.0%）（OI 3.5k）
量化解读： 存量 Call 重｜ATM IV 37.4%｜历史 Rank 81%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 345,347 股

📆 10-30 Forward Structure
存量OI: C 272.4k / P 211.3k，今日变化ΔOI: C +63.1k / P +17.8k，平值价格ATM: C $4.95 / P $4.40 ｜ ATM IV 38.8%，净 delta 敞口 1.8M shares
Top ΔOI: C 225 +21,035 ｜ C 217 +20,898 ｜ C 220 +4,957
仓位参考: Max Pain 218 ｜ Call Wall 225（+5.7%，弱）（OI 32.3k） ｜ Put Wall 210（-1.4%，弱）（OI 19.1k）
量化解读： 存量 Call 重｜ATM IV 38.8%｜历史 Rank 81%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,750,751 股

📆 11-02 Forward Structure
存量OI: C 7.3k / P 2.7k，今日变化ΔOI: C +2.8k / P +1.3k，平值价格ATM: C $5.40 / P $5.05 ｜ ATM IV 35.9%，净 delta 敞口 67k shares
Top ΔOI: C 220 +862 ｜ C 215 +352 ｜ C 225 +325
仓位参考: Max Pain 212 ｜ Call Wall 230（+8.0%，弱）（OI 2.0k） ｜ Put Wall 200（-6.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 35.9%｜历史 Rank 81%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 67,088 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/NVDA_morning.json