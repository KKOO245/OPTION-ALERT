# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $766.83 ｜ QQQ $741.09
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-02 285C ΔOI +726（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 266.65 → 今开 269.91（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 286.93 ｜ 低 264.01

Options: P/C成交量 0.48 | OI比 1.21 | ATM IV 141.8% | Skew 0.5pp | Term 0.55 | ExpMove ±9.1%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±9.1% ｜ 10-09（14D）±5.8% ｜ 10-16（21D）±15.1% ｜ 10-23（28D）±17.7%
   ⇒ IV–VIX Spread: +125.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,777,195 | GEX Change vs 上次快照 14,762,575 | Flip: Primary Flip: 264.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 615 / LOW 132 / INVALID 187
结构观察区: Primary Flip 264.31（全链重定价，覆盖 98%）
Call Wall 300（弱结构｜现价低于该位 4.5%）
最近结构参考: Call Wall 300（现价低于该位 4.5%）
量化视角： 正 Gamma（1478万，无历史分位）｜正 Gamma 增强（+1476万）｜现价位于 Flip 上方 8.42%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 265（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 264（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 260.0P — Vol 1,420 | 最新价 $8.99 | OI 438→1666 (ΔOI +1228张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1228张（+280.4% vs前日OI），连续性待观察（方向未知）
10-02 285.0C — Vol 1,140 | 最新价 $5.75 | OI 665→1391 (ΔOI +726张) | ΔOI/Volume 63.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增726张（+109.2% vs前日OI），连续性待观察（方向未知）
10-02 250.0P — Vol 1,145 | 最新价 $5.10 | OI 1432→2001 (ΔOI +569张) | ΔOI/Volume 49.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增569张（+39.7% vs前日OI），连续性待观察（方向未知）
10-23 175.0P — Vol 802 | 最新价 $0.71 | OI 73→618 (ΔOI +545张) | ΔOI/Volume 68.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增545张（+746.6% vs前日OI），连续性待观察（方向未知）
10-02 290.0C — Vol 1,264 | 最新价 $4.60 | OI 700→1231 (ΔOI +531张) | ΔOI/Volume 42.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增531张（+75.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,599 张（Put 2,342 / Call 1,257），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 42.2k / P 51.0k，今日成交量: C 18.7k / P 8.9k，平值价格ATM: C $3.05 / P $5.85 ｜ ATM IV 141.8%，预期波动 ±3.1%，Max Pain 265
Top ΔOI: C 250 +444 ｜ P 250 -423 ｜ P 222 +391

📆 Forward Expiration Structure

10-02  C +3.6k / P +6.1k ｜ Activity HIGH ｜ 7D
10-09  C +0.7k / P +1.4k ｜ Activity HIGH ｜ 14D
10-16  C -83 / P +1.4k ｜ Activity HIGH ｜ 21D
10-23  C +1.0k / P +1.7k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 25.3k / P 27.4k，今日变化ΔOI: C +3.6k / P +6.1k，平值价格ATM: C $12.00 / P $14.04 ｜ ATM IV 82.5%，净 delta 敞口 93k shares
Top ΔOI: P 260 +1,228 ｜ C 285 +726 ｜ P 250 +569
仓位参考: Max Pain 260 ｜ Call Wall 300（+4.7%，弱）（OI 3.9k） ｜ Put Wall 260（-9.3%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 82.5%｜历史 Rank 88%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 93,438 股

📆 10-09 Forward Structure
存量OI: C 5.6k / P 10.5k，今日变化ΔOI: C +0.7k / P +1.4k，平值价格ATM: C $16.75 / P $0.00 ｜ ATM IV 78.2%，净 delta 敞口 23k shares
仓位参考: Max Pain 260 ｜ Call Wall 295（+2.9%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 78.2%｜历史 Rank 88%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 23,183 股

📆 10-16 Forward Structure
存量OI: C 67.8k / P 72.9k，今日变化ΔOI: C -83 / P +1.4k，平值价格ATM: C $21.45 / P $21.90 ｜ ATM IV 79.0%，净 delta 敞口 2k shares
Top ΔOI: C 320 -344 ｜ C 350 -291 ｜ P 235 +285
仓位参考: Max Pain 255 ｜ Call Wall 280（-2.3%，弱）（OI 8.5k） ｜ Put Wall 260（-9.3%，弱）（OI 3.7k）
量化解读： 存量两侧均衡｜ATM IV 79.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,766 股

📆 10-23 Forward Structure
存量OI: C 6.8k / P 12.7k，今日变化ΔOI: C +1.0k / P +1.7k，平值价格ATM: C $26.00 / P $24.65 ｜ ATM IV 78.0%，净 delta 敞口 32k shares
Top ΔOI: C 300 +451 ｜ P 220 +187
仓位参考: Max Pain 250 ｜ Call Wall 300（+4.7%）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 78.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 32,224 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/BE_morning.json