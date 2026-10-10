# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,609.46 → 今开 1,633.33（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 1637.95 ｜ 低 1606.00

Options: P/C成交量 0.62 | OI比 0.78 | ATM IV 75.3% | Skew 0.3pp | Term 0.86 | ExpMove ±6.2%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.3pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.2% ｜ 10-23（14D）±9.0% ｜ 10-30（21D）±12.6% ｜ 11-06（28D）±15.0%
   ⇒ IV–VIX Spread: +60.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,119,284 | GEX Change vs 上次快照 7,818,340 | Flip: Primary Flip: 1635.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1543 / LOW 524 / INVALID 1103
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1635.97（全链重定价，覆盖 96%）
Put Wall 1,500（弱结构｜现价高于该位 7.8%）
最近结构参考: Flip 1636（现价低于该位 1.2%）
量化视角： 负 Gamma（512万，无历史分位）｜负 Gamma 缓解（+782万）｜现价位于 Flip 下方 1.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构）；上方 1,640（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1636（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 1700.0C — Vol 13,032 | 最新价 $2.00 | OI 1019→2654 (ΔOI +1635张) | ΔOI/Volume 12.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1635张（+160.4% vs前日OI），连续性待观察（方向未知）
10-09 1730.0C — Vol 4,102 | 最新价 $0.95 | OI 778→1691 (ΔOI +913张) | ΔOI/Volume 22.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增913张（+117.3% vs前日OI），连续性待观察（方向未知）
10-09 1650.0C — Vol 6,889 | 最新价 $7.90 | OI 243→962 (ΔOI +719张) | ΔOI/Volume 10.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增719张（+295.9% vs前日OI），连续性待观察（方向未知）
10-09 1600.0C — Vol 4,548 | 最新价 $27.21 | OI 365→907 (ΔOI +542张) | ΔOI/Volume 11.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增542张（+148.5% vs前日OI），连续性待观察（方向未知）
10-23 2300.0C — Vol 646 | 最新价 $1.70 | OI 456→974 (ΔOI +518张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增518张（+113.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,327 张（Put 0 / Call 4,327），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 55.8k / P 43.3k，今日成交量: C 15.0k / P 9.3k，平值价格ATM: C $14.95 / P $11.50 ｜ ATM IV 75.3%，预期波动 ±1.6%，Max Pain 1,640
Top ΔOI: C 1700 +1,635 ｜ C 1730 +913 ｜ P 1800 -886

📆 Forward Expiration Structure

10-16  C +2.8k / P +3.0k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +1.6k / P +0.8k ｜ Activity MEDIUM △ ｜ 14D
10-30  C +1.2k / P +0.9k ｜ Activity MEDIUM △ ｜ 21D
11-06  C +0.5k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 52.6k / P 59.0k，今日变化ΔOI: C +2.8k / P +3.0k，平值价格ATM: C $50.89 / P $49.94 ｜ ATM IV 55.2%，净 delta 敞口 85k shares
Top ΔOI: C 2000 -558 ｜ C 1900 +474 ｜ P 1640 +411
仓位参考: Max Pain 1,660 ｜ Call Wall 1700（+5.2%，弱）（OI 1.5k） ｜ Put Wall 1500（-7.2%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜ATM IV 55.2%｜历史 Rank 32%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 84,699 股

10-23（MEDIUM △）Top ΔOI: 2300C +518 ｜ 1650C +173
10-23（MEDIUM △）仓位参考: Max Pain 1,695 ｜ Call Wall 1700（+5.2%，弱）（OI 0.4k） ｜ Put Wall 1500（-7.2%）（OI 0.8k）

10-30（MEDIUM △）Top ΔOI: 1650C +167 ｜ 1700C +151
10-30（MEDIUM △）仓位参考: Max Pain 1,700 ｜ Call Wall 1700（+5.2%，弱）（OI 0.6k） ｜ Put Wall 1500（-7.2%，弱）（OI 0.5k）

📆 11-06 Forward Structure
存量OI: C 3.1k / P 3.8k，今日变化ΔOI: C +0.5k / P +0.9k，平值价格ATM: C $124.00 / P $119.20 ｜ ATM IV 64.9%，净 delta 敞口 -3k shares
Top ΔOI: P 1400 +286 ｜ P 1640 +94 ｜ P 1770 +79
仓位参考: Max Pain 1,675 ｜ Call Wall 1750（+8.3%，弱）（OI 0.1k） ｜ Put Wall 1500（-7.2%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 64.9%｜历史 Rank 32%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 2,798 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SNDK_morning.json