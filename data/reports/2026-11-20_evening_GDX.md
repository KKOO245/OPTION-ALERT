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
🟡 **近现价集中开仓**: 11-23 70P ΔOI +182（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 75C ΔOI +11,162 占该期限总 OI 18.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 70.71 → 收盘 68.40（-3.3%） ｜ 今日高 71.77 ｜ 低 68.03 ｜ 昨收 72.00 → 收盘 68.40（-5.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 1.25 | OI比 0.66 | ATM IV 242.0% | Skew 50.6pp | Term 0.23 | ExpMove ±4.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.23，近月 IV 高于远月）｜保护溢价显著（Skew 50.6pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.66）+ 当日成交偏 Put（P/C量 1.25）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±4.2% ｜ 11-25（5D）±6.7% ｜ 11-27（7D）±6.6% ｜ 11-30（10D）±3.1%
   ⇒ IV–VIX Spread: +206.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -48,542,042 | GEX Change vs 上次快照 39,686,681 | Flip: Primary Flip: 76.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 438 / LOW 252 / INVALID 614
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 76.97（全链重定价，覆盖 87%）
Put Wall 67（弱结构｜现价高于该位 2.1%）
最近结构参考: Put Wall 67（现价高于该位 2.1%）
量化视角： 负 Gamma（4854万，无历史分位）｜负 Gamma 缓解（+3969万）｜现价位于 Flip 下方 11.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 67（Put Wall，弱结构）；上方 76（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 77（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 130.0P — Vol 1 | 最新价 $35.53 | OI 0→48 (ΔOI +48张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增48张（量数据缺失），以日内换手为主
11-27 100.0P — Vol 0 | 最新价 $12.25 | OI 0→21 (ΔOI +21张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增21张（量数据缺失），以日内换手为主
12-18 29.0C — Vol 434 | 最新价 $63.15 | OI 306→321 (ΔOI +15张) | ΔOI/Volume 3.5% | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增仓仅占量3.5%，以日内换手为主
12-18 23.0C — Vol 5 | 最新价 $25.90 | OI 1→5 (ΔOI +4张) | ΔOI/Volume 80.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4张（+400.0% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 88 张（Put 69 / Call 19），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-23  C -2 / P -0.4k ｜ Activity HIGH ｜ 3D（新行权价 C 2.9k / P 1.7k）
11-25  C +21 / P -0.2k ｜ Activity HIGH ｜ 5D（新行权价 C 1.0k / P 0.8k）
11-27  C +22.5k / P -59 ｜ Activity HIGH ｜ 7D（新行权价 C 0.8k / P 0.3k）
11-30  C N/A / P N/A ｜ Activity LOW ｜ 10D（新上架）

📆 11-23 Forward Structure
存量OI: C 3.8k / P 2.5k，今日变化ΔOI: C -2 / P -0.4k（新行权价 C 2.9k / P 1.7k），平值价格ATM: C $1.63 / P $1.26 ｜ ATM IV 54.8%，净 delta 敞口 41k shares
Top ΔOI: P 72 -463 ｜ P 70 +182
仓位参考: Max Pain 75 ｜ Put Wall 65（-5.0%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 54.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,213 股

📆 11-25 Forward Structure
存量OI: C 1.7k / P 1.1k，今日变化ΔOI: C +21 / P -0.2k（新行权价 C 1.0k / P 0.8k），平值价格ATM: C $2.79 / P $1.81 ｜ ATM IV 65.6%，净 delta 敞口 18k shares
Top ΔOI: P 86 -68 ｜ P 84 -64 ｜ P 85 -50
仓位参考: Max Pain 75 ｜ Call Wall 72（+5.3%，弱）（OI 0.2k） ｜ Put Wall 72（+5.3%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 65.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,069 股

📆 11-27 Forward Structure
存量OI: C 53.1k / P 8.1k，今日变化ΔOI: C +22.5k / P -59（新行权价 C 0.8k / P 0.3k），平值价格ATM: C $2.58 / P $1.94 ｜ ATM IV 60.3%，净 delta 敞口 195k shares
Top ΔOI: C 75 +11,162
仓位参考: Max Pain 75 ｜ Put Wall 70（+2.3%）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 60.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 195,044 股

11-30（Activity LOW）仓位参考: Max Pain 78 ｜ Put Wall 70（+2.3%）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/GDX_evening.json