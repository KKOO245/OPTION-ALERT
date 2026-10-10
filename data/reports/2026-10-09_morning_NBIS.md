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

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 225P ΔOI +775（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 219.71 → 今开 222.49（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 225.11 ｜ 低 218.50

Options: P/C成交量 0.58 | OI比 0.69 | ATM IV 95.7% | Skew 1.9pp | Term 0.74 | ExpMove ±7.5%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±7.5% ｜ 10-23（14D）±10.5% ｜ 10-30（21D）±13.3% ｜ 11-06（28D）±15.6%
   ⇒ IV–VIX Spread: +80.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,770,542 | GEX Change vs 上次快照 15,378,478 | Flip: Primary Flip: 222.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 497 / LOW 58 / INVALID 137
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 222.21（全链重定价，覆盖 94%）
Put Wall 220（弱结构｜现价高于该位 0.2%）
最近结构参考: Put Wall 220（现价高于该位 0.2%）
量化视角： 负 Gamma（377万，无历史分位）｜负 Gamma 缓解（+1538万）｜现价位于 Flip 下方 0.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 222（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 260.0C — Vol 8,837 | 最新价 $0.96 | OI 4236→8727 (ΔOI +4491张) | ΔOI/Volume 50.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4491张（+106.0% vs前日OI），连续性待观察（方向未知）
10-09 230.0C — Vol 15,321 | 最新价 $0.79 | OI 1619→5407 (ΔOI +3788张) | ΔOI/Volume 24.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3788张（+234.0% vs前日OI），连续性待观察（方向未知）
10-09 227.5C — Vol 7,268 | 最新价 $1.25 | OI 145→2666 (ΔOI +2521张) | ΔOI/Volume 34.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2521张（+1738.6% vs前日OI），连续性待观察（方向未知）
10-23 212.5C — Vol 1,837 | 最新价 $16.24 | OI 0→1831 (ΔOI +1831张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1831张（前日OI缺失），连续性待观察（方向未知）
10-16 240.0C — Vol 5,784 | 最新价 $3.00 | OI 5974→7726 (ΔOI +1752张) | ΔOI/Volume 30.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1752张（+29.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,383 张（Put 0 / Call 14,383），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 67.8k / P 46.9k，今日成交量: C 14.9k / P 8.7k，平值价格ATM: C $2.73 / P $1.83 ｜ ATM IV 95.7%，预期波动 ±2.1%，Max Pain 230
Top ΔOI: C 230 +3,788 ｜ C 227 +2,521 ｜ C 235 +1,475

📆 Forward Expiration Structure

10-16  C +10.0k / P +5.5k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +3.6k / P +1.5k ｜ Activity HIGH ｜ 14D
10-30  C +1.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 21D
11-06  C +1.2k / P +2.1k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 105.8k / P 111.2k，今日变化ΔOI: C +10.0k / P +5.5k，平值价格ATM: C $8.60 / P $7.91 ｜ ATM IV 66.9%，净 delta 敞口 112k shares
Top ΔOI: C 260 +4,491 ｜ C 240 +1,752 ｜ C 270 -1,291
仓位参考: Max Pain 225 ｜ Call Wall 240（+8.9%，弱）（OI 7.7k） ｜ Put Wall 220（-0.2%，弱）（OI 8.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.9%｜历史 Rank 38%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 112,037 股

📆 10-23 Forward Structure
存量OI: C 18.8k / P 13.3k，今日变化ΔOI: C +3.6k / P +1.5k，平值价格ATM: C $12.15 / P $10.90 ｜ ATM IV 66.8%，净 delta 敞口 117k shares
Top ΔOI: C 212 +1,831 ｜ P 225 +775 ｜ C 235 +434
仓位参考: Max Pain 220 ｜ Call Wall 212.5（-3.6%）（OI 1.8k） ｜ Put Wall 200（-9.3%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 66.8%｜历史 Rank 38%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 117,047 股

10-30（MEDIUM △）Top ΔOI: 300C +388 ｜ 225C +355
10-30（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 235（+6.6%，弱）（OI 0.7k） ｜ Put Wall 200（-9.3%，弱）（OI 2.0k）

📆 11-06 Forward Structure
存量OI: C 6.9k / P 10.1k，今日变化ΔOI: C +1.2k / P +2.1k，平值价格ATM: C $17.50 / P $16.90 ｜ ATM IV 70.9%，净 delta 敞口 -10k shares
Top ΔOI: C 260 +879 ｜ P 200 +850 ｜ P 190 +386
仓位参考: Max Pain 235 ｜ Call Wall 240（+8.9%，弱）（OI 1.1k） ｜ Put Wall 200（-9.3%）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 70.9%｜历史 Rank 38%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 10,124 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/NBIS_morning.json