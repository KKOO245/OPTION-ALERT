# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.40
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-30 360P ΔOI +682（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 377.94 → 今开 384.90（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 386.83 ｜ 低 369.65

Options: P/C成交量 0.51 | OI比 1.03 | ATM IV 64.2% | Skew -4.9pp | Term 0.70 | ExpMove ±2.4%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-28（3D）±2.4% ｜ 09-30（5D）±3.6% ｜ 10-02（7D）±5.2% ｜ 10-05（10D）±5.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 85,266,721 | GEX Change vs 上次快照 -74,122,744 | Flip: Primary Flip: 358.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1205 / LOW 140 / INVALID 527
结构观察区: Primary Flip 358.14（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 7.3%）
最近结构参考: Flip 358（现价高于该位 3.5%）
量化视角： 正 Gamma（8527万，无历史分位）｜正 Gamma 减弱（7412万）｜现价位于 Flip 上方 3.54%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 358（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 375.0P — Vol 82,132 | 最新价 $1.98 | OI 4547→9072 (ΔOI +4525张) | ΔOI/Volume 5.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4525张（+99.5% vs前日OI），连续性待观察（方向未知）
09-25 400.0C — Vol 40,687 | 最新价 $0.09 | OI 21846→26324 (ΔOI +4478张) | ΔOI/Volume 11.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4478张（+20.5% vs前日OI），连续性待观察（方向未知）
09-25 390.0C — Vol 54,283 | 最新价 $0.45 | OI 17943→21461 (ΔOI +3518张) | ΔOI/Volume 6.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3518张（+19.6% vs前日OI），连续性待观察（方向未知）
10-02 140.0P — Vol 3,399 | 最新价 $0.01 | OI 95→3493 (ΔOI +3398张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3398张（+3576.8% vs前日OI），连续性待观察（方向未知）
09-25 380.0C — Vol 127,169 | 最新价 $2.46 | OI 16811→20198 (ΔOI +3387张) | ΔOI/Volume 2.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3387张（+20.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,306 张（Put 7,923 / Call 11,383），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 261.0k / P 268.3k，今日成交量: C 414.8k / P 209.7k，平值价格ATM: C $3.25 / P $1.97 ｜ ATM IV 64.2%，预期波动 ±1.4%，Max Pain 370
Top ΔOI: P 375 +4,525 ｜ C 400 +4,478 ｜ C 390 +3,518

📆 Forward Expiration Structure

09-28  C +10.3k / P +10.5k ｜ Activity HIGH ｜ 3D
09-30  C +5.1k / P +3.3k ｜ Activity HIGH ｜ 5D
10-02  C +11.1k / P +21.5k ｜ Activity HIGH ｜ 7D
10-05  C +2.1k / P +1.3k ｜ Activity HIGH ｜ 10D

📆 09-28 Forward Structure
存量OI: C 38.8k / P 29.4k，今日变化ΔOI: C +10.3k / P +10.5k，平值价格ATM: C $5.00 / P $3.87 ｜ ATM IV 31.9%，净 delta 敞口 -160k shares
仓位参考: Max Pain 378 ｜ Call Wall 400（+7.9%，弱）（OI 4.8k） ｜ Put Wall 365（-1.6%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.9%｜历史 Rank 77%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 159,634 股

📆 09-30 Forward Structure
存量OI: C 21.4k / P 15.2k，今日变化ΔOI: C +5.1k / P +3.3k，平值价格ATM: C $7.21 / P $6.00 ｜ ATM IV 37.3%，净 delta 敞口 -2k shares
Top ΔOI: C 405 +1,200 ｜ C 400 +1,013 ｜ P 360 +682
仓位参考: Max Pain 375 ｜ Call Wall 400（+7.9%）（OI 3.3k） ｜ Put Wall 375（+1.1%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 37.3%｜历史 Rank 77%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,778 股

📆 10-02 Forward Structure
存量OI: C 123.8k / P 125.8k，今日变化ΔOI: C +11.1k / P +21.5k，平值价格ATM: C $10.25 / P $9.02 ｜ ATM IV 45.8%，净 delta 敞口 -138k shares
Top ΔOI: C 397 +3,129
仓位参考: Max Pain 360 ｜ Call Wall 360（-2.9%）（OI 16.7k）
量化解读： 存量两侧均衡｜ATM IV 45.8%｜历史 Rank 77%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 137,607 股

📆 10-05 Forward Structure
存量OI: C 6.6k / P 5.7k，今日变化ΔOI: C +2.1k / P +1.3k，平值价格ATM: C $11.11 / P $9.50 ｜ ATM IV 41.6%，净 delta 敞口 6k shares
Top ΔOI: C 385 +303 ｜ C 405 +240 ｜ C 390 +202
仓位参考: Max Pain 378 ｜ Call Wall 380（+2.5%，弱）（OI 0.8k） ｜ Put Wall 375（+1.1%）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 41.6%｜历史 Rank 77%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 5,708 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/TSLA_morning.json