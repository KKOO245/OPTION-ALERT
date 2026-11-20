# 期权晚报 2026-11-20（快照 16:40 ET）

📊 市场环境

SPY $689.81 ｜ QQQ $608.45
VIX 35.89 ↑26.2%（5D +86.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-23 260P ΔOI +6,801（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 261P ΔOI +7,101 占该期限总 OI 13.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 263.32 → 收盘 256.61（-2.5%） ｜ 今日高 265.85 ｜ 低 256.32 ｜ 昨收 264.22 → 收盘 256.61（-2.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 1.95 | OI比 1.88 | ATM IV 81.7% | Skew 2.2pp | Term 0.39 | ExpMove ±2.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.39，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜当日成交偏 Put（P/C量 1.95）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.95×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.88×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±2.2% ｜ 11-24（4D）±3.0% ｜ 11-25（5D）±3.5% ｜ 11-27（7D）±3.8%
   ⇒ IV–VIX Spread: +45.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,004,256,515 | GEX Change vs 上次快照 1,444,933,577 | Flip: Primary Flip: 292.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 993 / LOW 288 / INVALID 1391
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 292.05（全链重定价，覆盖 88%）
Put Wall 270（弱结构｜现价低于该位 5.0%）
最近结构参考: Put Wall 270（现价低于该位 5.0%）
量化视角： 负 Gamma（10.04亿，无历史分位）｜负 Gamma 缓解（+14.45亿）｜现价位于 Flip 下方 12.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 270（Put Wall，弱结构） / 272（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 292（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 380.0P — Vol 0 | 最新价 $84.89 | OI 0→4 (ΔOI +4张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增4张（量数据缺失），以日内换手为主
11-27 292.5P — Vol 0 | 最新价 $17.50 | OI 0→1 (ΔOI +1张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增1张（量数据缺失），以日内换手为主
12-18 365.0P — Vol 0 | 最新价 $70.15 | OI 0→1 (ΔOI +1张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增1张（量数据缺失），以日内换手为主
12-18 375.0P — Vol 0 | 最新价 $80.26 | OI 0→1 (ΔOI +1张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增1张（量数据缺失），以日内换手为主
量化视角： 4 个事件合计 ΔOI ≈ 7 张（Put 7 / Call 0），跨 2 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-23  C +7.6k / P +16.4k ｜ Activity HIGH ｜ 3D（新行权价 C 0.6k / P 41）
11-24  C +1.4k / P -0.6k ｜ Activity HIGH ｜ 4D（新行权价 C 1.1k / P 1.9k）
11-25  C +2.4k / P +20.3k ｜ Activity HIGH ｜ 5D（新行权价 C 3.3k / P 0.9k）
11-27  C +6.8k / P +6.6k ｜ Activity HIGH ｜ 7D（新行权价 C 12）

📆 11-23 Forward Structure
存量OI: C 31.6k / P 44.5k，今日变化ΔOI: C +7.6k / P +16.4k（新行权价 C 0.6k / P 41），平值价格ATM: C $2.82 / P $2.96 ｜ ATM IV 30.9%，净 delta 敞口 -905k shares
Top ΔOI: P 260 +6,801 ｜ C 272 +5,439 ｜ P 255 +4,404
仓位参考: Max Pain 270 ｜ Call Wall 272（+6.0%）（OI 5.9k） ｜ Put Wall 270（+5.2%）（OI 12.2k）
量化解读： 存量 Put 重｜ATM IV 30.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 904,856 股

📆 11-24 Forward Structure
存量OI: C 10.9k / P 13.7k，今日变化ΔOI: C +1.4k / P -0.6k（新行权价 C 1.1k / P 1.9k），平值价格ATM: C $3.82 / P $4.00 ｜ ATM IV 35.4%，净 delta 敞口 78k shares
Top ΔOI: C 270 +383 ｜ P 277 -328 ｜ P 278 -249
仓位参考: Max Pain 271 ｜ Call Wall 275（+7.2%，弱）（OI 1.2k） ｜ Put Wall 270（+5.2%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 77,931 股

📆 11-25 Forward Structure
存量OI: C 17.2k / P 35.9k，今日变化ΔOI: C +2.4k / P +20.3k（新行权价 C 3.3k / P 0.9k），平值价格ATM: C $4.38 / P $4.51 ｜ ATM IV 36.7%，净 delta 敞口 -893k shares
Top ΔOI: P 261 +7,101 ｜ P 240 +5,953 ｜ P 260 +2,535
仓位参考: Max Pain 270 ｜ Call Wall 277（+7.9%，弱）（OI 4.3k） ｜ Put Wall 261（+1.7%，弱）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 36.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 893,446 股

📆 11-27 Forward Structure
存量OI: C 79.0k / P 203.6k，今日变化ΔOI: C +6.8k / P +6.6k（新行权价 C 12），平值价格ATM: C $5.16 / P $4.65 ｜ ATM IV 34.7%，净 delta 敞口 -220k shares
Top ΔOI: P 254 +1,841 ｜ P 245 -1,780 ｜ P 258 +1,640
仓位参考: Max Pain 275 ｜ Call Wall 275（+7.2%，弱）（OI 6.5k） ｜ Put Wall 270（+5.2%，弱）（OI 35.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 负 219,569 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/IWM_evening.json