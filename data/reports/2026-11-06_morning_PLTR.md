# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.1（extreme fear）
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
🟡 **近现价集中开仓**: 11-13 165C ΔOI +7,714（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 154.99 → 今开 158.75（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 163.97 ｜ 低 157.24

Options: P/C成交量 0.43 | OI比 0.82 | ATM IV 99.8% | Skew 4.2pp | Term 0.54 | ExpMove ±6.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价中性（Skew 4.2pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（7D）±6.8% ｜ 11-20（14D）±9.4% ｜ 11-27（21D）±11.1% ｜ 12-04（28D）±12.5%
   ⇒ IV–VIX Spread: +74.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,851,531 | GEX Change vs 上次快照 43,511,014 | Flip: Primary Flip: 160.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 460 / LOW 177 / INVALID 303
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 160.67（全链重定价，覆盖 96%）
最近结构参考: Flip 161（现价高于该位 0.5%）
量化视角： 正 Gamma（285万，无历史分位）｜由负转正（+4351万）｜现价位于 Flip 上方 0.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 165.0C — Vol 12,913 | 最新价 $2.79 | OI 277→7991 (ΔOI +7714张) | ΔOI/Volume 59.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7714张（+2784.8% vs前日OI），连续性待观察（方向未知）
11-13 160.0C — Vol 8,801 | 最新价 $4.60 | OI 257→7181 (ΔOI +6924张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6924张（+2694.2% vs前日OI），连续性待观察（方向未知）
11-06 160.0C — Vol 12,933 | 最新价 $1.20 | OI 639→4567 (ΔOI +3928张) | ΔOI/Volume 30.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3928张（+614.7% vs前日OI），连续性待观察（方向未知）
11-06 165.0C — Vol 15,530 | 最新价 $0.36 | OI 410→2898 (ΔOI +2488张) | ΔOI/Volume 16.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2488张（+606.8% vs前日OI），连续性待观察（方向未知）
11-06 157.5C — Vol 11,681 | 最新价 $2.07 | OI 77→2555 (ΔOI +2478张) | ΔOI/Volume 21.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2478张（+3218.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,532 张（Put 0 / Call 23,532），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 204.5k / P 168.6k，今日成交量: C 47.3k / P 20.4k，平值价格ATM: C $1.15 / P $2.50 ｜ ATM IV 99.8%，预期波动 ±2.3%，Max Pain 165
Top ΔOI: P 172 -4,393 ｜ C 160 +3,928 ｜ P 170 -3,786

📆 Forward Expiration Structure

11-13  C +27.3k / P +6.0k ｜ Activity HIGH ｜ 7D
11-20  C +1.4k / P -0.6k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +0.9k / P +2.4k ｜ Activity HIGH ｜ 21D
12-04  C +0.7k / P +0.5k ｜ Activity MEDIUM △ ｜ 28D

📆 11-13 Forward Structure
存量OI: C 70.2k / P 43.2k，今日变化ΔOI: C +27.3k / P +6.0k，平值价格ATM: C $5.05 / P $6.00 ｜ ATM IV 60.8%，净 delta 敞口 1.2M shares
Top ΔOI: C 165 +7,714 ｜ C 160 +6,924 ｜ C 187 +2,295
仓位参考: Max Pain 162 ｜ Call Wall 165（+2.2%，弱）（OI 8.0k） ｜ Put Wall 155（-4.0%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 60.8%｜历史 Rank 94%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,193,565 股

11-20（MEDIUM △）Top ΔOI: 175C +2,203 ｜ 150P -1,725
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 165（+2.2%，弱）（OI 12.3k） ｜ Put Wall 170（+5.3%，弱）（OI 8.1k）

📆 11-27 Forward Structure
存量OI: C 15.8k / P 17.3k，今日变化ΔOI: C +0.9k / P +2.4k，平值价格ATM: C $10.27 / P $7.61 ｜ ATM IV 55.3%，净 delta 敞口 29k shares
Top ΔOI: P 115 +1,209 ｜ P 150 +867
仓位参考: Max Pain 180 ｜ Call Wall 160（-0.9%，弱）（OI 0.6k） ｜ Put Wall 150（-7.1%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 55.3%｜历史 Rank 94%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,004 股

12-04（MEDIUM △）Top ΔOI: 180C +208 ｜ 175C +148
12-04（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+8.4%，弱）（OI 0.8k） ｜ Put Wall 150（-7.1%，弱）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/PLTR_morning.json