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
🟡 **近现价集中开仓**: 11-23 600P ΔOI +8,551（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 638.81 → 收盘 608.45（-4.8%） ｜ 今日高 643.28 ｜ 低 606.23 ｜ 昨收 645.04 → 收盘 608.45（-5.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 1.12 | OI比 0.72 | ATM IV 102.9% | Skew 7.4pp | Term 0.40 | ExpMove ±3.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.40，近月 IV 高于远月）｜保护溢价显著（Skew 7.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 19% ｜ P/C OI(近端) 1%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 19%）｜近端持仓极端 Call 重（P/C OI 分位 1%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-23（3D）±3.4% ｜ 11-24（4D）±4.8% ｜ 11-25（5D）±5.4% ｜ 11-27（7D）±5.6%
   ⇒ IV–VIX Spread: +67.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -522,521,717 | GEX Change vs 上次快照 78,925,020 | Flip: Primary Flip: 663.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 2788 / LOW 645 / INVALID 1989
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 663.07（全链重定价，覆盖 85%）
Put Wall 600（弱结构｜现价高于该位 1.4%）
最近结构参考: Put Wall 600（现价高于该位 1.4%）
量化视角： 负 Gamma（5.23亿，历史分位偏负区，比 81% 的交易日更负）｜负 Gamma 缓解（+7893万）｜现价位于 Flip 下方 8.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 600（Put Wall，弱结构）；上方 670（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 663（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 224.78C — Vol 1 | 最新价 $405.01 | OI 5→6 (ΔOI +1张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1张（+20.0% vs前日OI），连续性待观察（方向未知）
量化视角： 1 个事件合计 ΔOI ≈ 1 张（Put 0 / Call 1），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-23  C +24.2k / P +49.3k ｜ Activity HIGH ｜ 3D（新行权价 C 1.4k）
11-24  C +7.1k / P +30.8k ｜ Activity HIGH ｜ 4D（新行权价 C 1.0k / P 9.0k）
11-25  C +12.8k / P +11.2k ｜ Activity HIGH ｜ 5D（新行权价 C 2.2k / P 0.7k）
11-27  C +21.2k / P +16.0k ｜ Activity HIGH ｜ 7D（新行权价 C 3.8k）

📆 11-23 Forward Structure
存量OI: C 78.0k / P 91.9k，今日变化ΔOI: C +24.2k / P +49.3k（新行权价 C 1.4k），平值价格ATM: C $13.00 / P $7.95 ｜ ATM IV 46.4%，净 delta 敞口 -1.7M shares
Top ΔOI: P 600 +8,551 ｜ P 510 +5,793 ｜ C 660 +4,401
仓位参考: Max Pain 660 ｜ Put Wall 600（-1.4%，弱）（OI 9.7k）
量化解读： 存量两侧均衡｜ATM IV 46.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.34×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,742,985 股

📆 11-24 Forward Structure
存量OI: C 40.6k / P 76.9k，今日变化ΔOI: C +7.1k / P +30.8k（新行权价 C 1.0k / P 9.0k），平值价格ATM: C $17.34 / P $11.60 ｜ ATM IV 53.0%，净 delta 敞口 -539k shares
Top ΔOI: P 560 +11,313 ｜ P 540 +7,832 ｜ P 565 +6,035
仓位参考: Max Pain 663 ｜ Put Wall 600（-1.4%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 53.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 539,478 股

📆 11-25 Forward Structure
存量OI: C 55.6k / P 35.1k，今日变化ΔOI: C +12.8k / P +11.2k（新行权价 C 2.2k / P 0.7k），平值价格ATM: C $19.05 / P $13.88 ｜ ATM IV 53.6%，净 delta 敞口 -476k shares
Top ΔOI: P 565 +4,059 ｜ C 680 +3,499
仓位参考: Max Pain 661 ｜ Put Wall 625（+2.7%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 53.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 475,941 股

📆 11-27 Forward Structure
存量OI: C 195.2k / P 141.5k，今日变化ΔOI: C +21.2k / P +16.0k（新行权价 C 3.8k），平值价格ATM: C $19.18 / P $14.95 ｜ ATM IV 49.6%，净 delta 敞口 -678k shares
Top ΔOI: C 660 +4,644 ｜ P 654 +3,979 ｜ C 670 +2,138
仓位参考: Max Pain 670 ｜ Put Wall 595（-2.2%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜ATM IV 49.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 负 677,735 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/QQQ_evening.json