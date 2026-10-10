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
🟡 **近现价集中开仓**: 10-23 555P ΔOI +714（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 500P ΔOI +1,248 占该期限总 OI 11.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 563.28 → 今开 570.69（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 571.34 ｜ 低 558.31

Options: P/C成交量 0.61 | OI比 1.84 | ATM IV 49.7% | Skew -2.7pp | Term 0.76 | ExpMove ±4.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.84×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±4.3% ｜ 10-23（14D）±6.3% ｜ 10-30（21D）±7.2% ｜ 11-06（28D）±8.3%
   ⇒ IV–VIX Spread: +34.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,441,096 | GEX Change vs 上次快照 -2,470,843 | Flip: Primary Flip: 577.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 532 / LOW 281 / INVALID 733
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 577.79（全链重定价，覆盖 88%）
最近结构参考: Flip 578（现价低于该位 2.9%）
量化视角： 负 Gamma（1444万，无历史分位）｜负 Gamma 加深（247万）｜现价位于 Flip 下方 2.90%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 560（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 578（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 410.0P — Vol 4,002 | 最新价 $0.15 | OI 200→4173 (ΔOI +3973张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3973张（+1986.5% vs前日OI），连续性待观察（方向未知）
10-30 485.0P — Vol 3,505 | 最新价 $2.71 | OI 19→3522 (ΔOI +3503张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3503张（+18436.8% vs前日OI），连续性待观察（方向未知）
10-30 480.0P — Vol 5 | 最新价 $2.20 | OI 133→3106 (ΔOI +2973张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2973张（+2235.3% vs前日OI），连续性待观察（方向未知）
10-09 570.0C — Vol 3,096 | 最新价 $1.90 | OI 151→1790 (ΔOI +1639张) | ΔOI/Volume 52.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1639张（+1085.4% vs前日OI），连续性待观察（方向未知）
10-23 500.0P — Vol 1,255 | 最新价 $2.45 | OI 215→1463 (ΔOI +1248张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1248张（+580.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,336 张（Put 11,697 / Call 1,639），跨 4 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 8.4k / P 15.4k，今日成交量: C 0.5k / P 0.3k，平值价格ATM: C $3.75 / P $2.38 ｜ ATM IV 49.7%，预期波动 ±1.1%，Max Pain 560
Top ΔOI: C 570 +1,639 ｜ P 552 +1,133 ｜ P 555 +1,104

📆 Forward Expiration Structure

10-16  C -0.4k / P +3.9k ｜ Activity HIGH ｜ 7D
10-23  C +0.2k / P +2.5k ｜ Activity HIGH ｜ 14D
10-30  C +5 / P +7.0k ｜ Activity HIGH ｜ 21D
11-06  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 37.5k / P 104.7k，今日变化ΔOI: C -0.4k / P +3.9k，平值价格ATM: C $13.55 / P $10.65 ｜ ATM IV 36.5%，净 delta 敞口 -27k shares
Top ΔOI: P 410 +3,973
仓位参考: Max Pain 535 ｜ Call Wall 550（-2.0%，弱）（OI 2.2k） ｜ Put Wall 530（-5.5%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 36.5%｜历史 Rank 86%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 负 27,155 股

📆 10-23 Forward Structure
存量OI: C 1.6k / P 9.1k，今日变化ΔOI: C +0.2k / P +2.5k，平值价格ATM: C $21.00 / P $14.50 ｜ ATM IV 34.2%，净 delta 敞口 -46k shares
Top ΔOI: P 500 +1,248 ｜ P 555 +714 ｜ P 560 +180
仓位参考: Max Pain 560 ｜ Call Wall 525（-6.4%，弱）（OI 0.1k） ｜ Put Wall 555（-1.1%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 34.2%｜历史 Rank 86%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 45,600 股

📆 10-30 Forward Structure
存量OI: C 6.0k / P 27.5k，今日变化ΔOI: C +5 / P +7.0k，平值价格ATM: C $21.37 / P $19.00 ｜ ATM IV 36.7%，净 delta 敞口 -85k shares
Top ΔOI: P 485 +3,503 ｜ P 480 +2,973 ｜ P 567 +425
仓位参考: Max Pain 568 ｜ Put Wall 550（-2.0%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 36.7%｜历史 Rank 86%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 85,266 股

11-06（MEDIUM △）Top ΔOI: 567C +93 ｜ 600P +30
11-06（MEDIUM △）仓位参考: Max Pain 568 ｜ Call Wall 567.5（+1.1%）（OI 0.2k） ｜ Put Wall 592.5（+5.6%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SOXX_morning.json