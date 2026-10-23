# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.05 ｜ QQQ $706.88
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-26 385C ΔOI +2,560（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 455C ΔOI +7,079 占该期限总 OI 36.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 374.58 → 今开 373.14（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 375.93 ｜ 低 365.27

Options: P/C成交量 1.17 | OI比 1.02 | ATM IV 62.8% | Skew 2.0pp | Term 0.64 | ExpMove ±2.6%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价薄（Skew 2.0pp）｜当日成交偏 Put（P/C量 1.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.17×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.6% ｜ 10-28（5D）±3.9% ｜ 10-30（7D）±4.7% ｜ 11-02（10D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,762,317 | GEX Change vs 上次快照 -45,346,378 | Flip: Primary Flip: 365.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1165 / LOW 204 / INVALID 813
结构观察区: Primary Flip 365.08（全链重定价，覆盖 97%）
Call Wall 400（现价低于该位 8.1%）
最近结构参考: Flip 365（现价高于该位 0.6%）
量化视角： 正 Gamma（1576万，无历史分位）｜正 Gamma 减弱（4535万）｜现价位于 Flip 上方 0.65%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 370（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-02 455.0C — Vol 7,093 | 最新价 $0.19 | OI 309→7388 (ΔOI +7079张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7079张（+2290.9% vs前日OI），连续性待观察（方向未知）
10-23 390.0C — Vol 78,929 | 最新价 $0.50 | OI 9393→15260 (ΔOI +5867张) | ΔOI/Volume 7.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5867张（+62.5% vs前日OI），连续性待观察（方向未知）
10-30 420.0C — Vol 21,238 | 最新价 $0.54 | OI 4075→9079 (ΔOI +5004张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5004张（+122.8% vs前日OI），连续性待观察（方向未知）
10-30 300.0P — Vol 6,706 | 最新价 $0.10 | OI 2564→7510 (ΔOI +4946张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4946张（+192.9% vs前日OI），连续性待观察（方向未知）
10-23 400.0C — Vol 73,616 | 最新价 $0.14 | OI 19583→24401 (ΔOI +4818张) | ΔOI/Volume 6.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4818张（+24.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,714 张（Put 4,946 / Call 22,768），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 277.2k / P 282.7k，今日成交量: C 192.0k / P 225.3k，平值价格ATM: C $3.27 / P $1.85 ｜ ATM IV 62.8%，预期波动 ±1.4%，Max Pain 370
Top ΔOI: C 390 +5,867 ｜ C 420 -5,043 ｜ C 400 +4,818

📆 Forward Expiration Structure

10-26  C +18.9k / P +6.9k ｜ Activity HIGH ｜ 3D
10-28  C +5.4k / P +5.6k ｜ Activity HIGH ｜ 5D
10-30  C +24.8k / P +17.5k ｜ Activity HIGH ｜ 7D
11-02  C +10.0k / P +1.6k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 68.9k / P 36.5k，今日变化ΔOI: C +18.9k / P +6.9k，平值价格ATM: C $5.56 / P $4.00 ｜ ATM IV 34.4%，净 delta 敞口 -201k shares
Top ΔOI: C 385 +2,560
仓位参考: Max Pain 375 ｜ Put Wall 365（-0.7%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 34.4%｜历史 Rank 75%（近端代理）｜IV/RV 1.06×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 201,442 股

📆 10-28 Forward Structure
存量OI: C 14.8k / P 16.2k，今日变化ΔOI: C +5.4k / P +5.6k，平值价格ATM: C $7.98 / P $6.40 ｜ ATM IV 39.9%，净 delta 敞口 -185k shares
Top ΔOI: P 385 +1,160 ｜ C 387 +906 ｜ P 382 +611
仓位参考: Max Pain 380 ｜ Call Wall 400（+8.9%，弱）（OI 1.4k） ｜ Put Wall 350（-4.7%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 39.9%｜历史 Rank 75%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 184,841 股

📆 10-30 Forward Structure
存量OI: C 107.5k / P 113.1k，今日变化ΔOI: C +24.8k / P +17.5k，平值价格ATM: C $9.55 / P $7.88 ｜ ATM IV 41.5%，净 delta 敞口 8k shares
Top ΔOI: C 420 +5,004 ｜ C 395 +3,491
仓位参考: Max Pain 372 ｜ Call Wall 400（+8.9%，弱）（OI 10.4k） ｜ Put Wall 340（-7.5%，弱）（OI 4.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.5%｜历史 Rank 75%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,560 股

📆 11-02 Forward Structure
存量OI: C 13.2k / P 6.1k，今日变化ΔOI: C +10.0k / P +1.6k，平值价格ATM: C $10.35 / P $9.45 ｜ ATM IV 38.4%，净 delta 敞口 -42k shares
Top ΔOI: C 455 +7,079 ｜ P 380 +493
仓位参考: Max Pain 380 ｜ Put Wall 380（+3.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 38.4%｜历史 Rank 75%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 41,684 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/TSLA_morning.json