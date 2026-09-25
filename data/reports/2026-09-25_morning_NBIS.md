# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $771.10 ｜ QQQ $744.50
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 243.48 → 今开 246.90（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 246.90 ｜ 低 235.79

Options: P/C成交量 0.52 | OI比 0.91 | ATM IV 109.2% | Skew -0.9pp | Term 0.72 | ExpMove ±8.5%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（7D）±8.5% ｜ 10-09（14D）±11.8% ｜ 10-16（21D）±14.4% ｜ 10-23（28D）±17.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,493,309 | GEX Change vs 上次快照 -7,210,289 | Flip: Primary Flip: 224.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 532 / LOW 70 / INVALID 152
结构观察区: Primary Flip 224.79（全链重定价，覆盖 97%）
最近结构参考: Flip 225（现价高于该位 6.3%）
量化视角： 正 Gamma（1749万，无历史分位）｜正 Gamma 减弱（721万）｜现价位于 Flip 上方 6.31%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 300.0C — Vol 6,873 | 最新价 $4.80 | OI 7601→11392 (ΔOI +3791张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3791张（+49.9% vs前日OI），连续性待观察（方向未知）
09-25 265.0C — Vol 5,534 | 最新价 $0.33 | OI 1037→2695 (ΔOI +1658张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1658张（+159.9% vs前日OI），连续性待观察（方向未知）
09-25 240.0P — Vol 9,013 | 最新价 $3.02 | OI 1106→2506 (ΔOI +1400张) | ΔOI/Volume 15.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1400张（+126.6% vs前日OI），连续性待观察（方向未知）
09-25 255.0C — Vol 6,573 | 最新价 $1.20 | OI 1050→2212 (ΔOI +1162张) | ΔOI/Volume 17.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1162张（+110.7% vs前日OI），连续性待观察（方向未知）
10-30 290.0C — Vol 1,368 | 最新价 $10.75 | OI 128→1238 (ΔOI +1110张) | ΔOI/Volume 81.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1110张（+867.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,121 张（Put 1,400 / Call 7,721），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 66.5k / P 60.8k，今日成交量: C 17.5k / P 9.0k，平值价格ATM: C $1.98 / P $3.85 ｜ ATM IV 109.2%，预期波动 ±2.4%，Max Pain 230
Top ΔOI: C 265 +1,658 ｜ C 250 -1,600 ｜ P 220 -1,450

📆 Forward Expiration Structure

10-02  C +6.0k / P +3.5k ｜ Activity HIGH ｜ 7D
10-09  C +2.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +7.0k / P +0.9k ｜ Activity HIGH ｜ 21D
10-23  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 40.1k / P 26.5k，今日变化ΔOI: C +6.0k / P +3.5k，平值价格ATM: C $9.30 / P $11.05 ｜ ATM IV 74.0%，净 delta 敞口 -100k shares
Top ΔOI: C 270 +762 ｜ C 210 -638
仓位参考: Max Pain 225 ｜ Call Wall 235（-1.7%，弱）（OI 5.0k） ｜ Put Wall 220（-7.9%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 74.0%｜历史 Rank 56%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 100,440 股

10-09（MEDIUM △）Top ΔOI: 212C +830
10-09（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 240（+0.4%，弱）（OI 2.0k） ｜ Put Wall 225（-5.8%，弱）（OI 0.7k）

📆 10-16 Forward Structure
存量OI: C 62.7k / P 79.5k，今日变化ΔOI: C +7.0k / P +0.9k，平值价格ATM: C $17.00 / P $17.50 ｜ ATM IV 77.0%，净 delta 敞口 47k shares
Top ΔOI: C 300 +3,791 ｜ C 270 +855 ｜ C 275 +802
仓位参考: Max Pain 220 ｜ Call Wall 240（+0.4%，弱）（OI 4.3k） ｜ Put Wall 220（-7.9%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.0%｜历史 Rank 56%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 47,322 股

10-23（MEDIUM △）Top ΔOI: 235P +141
10-23（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 225（-5.8%，弱）（OI 0.4k） ｜ Put Wall 235（-1.7%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NBIS_morning.json