# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $771.10 ｜ QQQ $744.50
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 200C ΔOI +6,043（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 192.59 → 今开 192.86（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 194.21 ｜ 低 190.61

Options: P/C成交量 0.34 | OI比 0.82 | ATM IV 57.5% | Skew 2.5pp | Term 0.80 | ExpMove ±5.2%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 2.5pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（7D）±5.2% ｜ 10-09（14D）±7.1% ｜ 10-16（21D）±8.8% ｜ 10-23（28D）±10.2%
   ⇒ IV–VIX Spread: +41.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 88,223,689 | GEX Change vs 上次快照 -3,953,612 | Flip: Primary Flip: 173.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 585 / LOW 110 / INVALID 165
结构观察区: Primary Flip 173.89（全链重定价，覆盖 95%）
Call Wall 200（弱结构｜现价低于该位 4.0%）
最近结构参考: Call Wall 200（现价低于该位 4.0%）
量化视角： 正 Gamma（8822万，无历史分位）｜正 Gamma 减弱（395万）｜现价位于 Flip 上方 10.38%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 174（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 200.0C — Vol 12,781 | 最新价 $2.70 | OI 8868→14911 (ΔOI +6043张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6043张（+68.1% vs前日OI），连续性待观察（方向未知）
10-02 207.5C — Vol 5,687 | 最新价 $1.23 | OI 2431→7542 (ΔOI +5111张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5111张（+210.2% vs前日OI），连续性待观察（方向未知）
09-25 190.0P — Vol 27,507 | 最新价 $0.98 | OI 4072→8606 (ΔOI +4534张) | ΔOI/Volume 16.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4534张（+111.3% vs前日OI），连续性待观察（方向未知）
10-02 197.5C — Vol 5,530 | 最新价 $3.55 | OI 1842→6259 (ΔOI +4417张) | ΔOI/Volume 79.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4417张（+239.8% vs前日OI），连续性待观察（方向未知）
10-02 205.0C — Vol 6,079 | 最新价 $1.56 | OI 2083→6152 (ΔOI +4069张) | ΔOI/Volume 66.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4069张（+195.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,174 张（Put 4,534 / Call 19,640），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 144.8k / P 119.0k，今日成交量: C 36.4k / P 12.5k，平值价格ATM: C $0.73 / P $1.75 ｜ ATM IV 57.5%，预期波动 ±1.3%，Max Pain 180
Top ΔOI: P 190 +4,534 ｜ C 190 +1,961 ｜ P 185 -1,942

📆 Forward Expiration Structure

10-02  C +24.3k / P +10.5k ｜ Activity HIGH ｜ 7D
10-09  C +1.6k / P +4.1k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +2.6k / P +2.8k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +1.2k / P +0.8k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 73.3k / P 59.2k，今日变化ΔOI: C +24.3k / P +10.5k，平值价格ATM: C $4.50 / P $5.40 ｜ ATM IV 45.4%，净 delta 敞口 353k shares
Top ΔOI: C 200 +6,043 ｜ C 207 +5,111 ｜ C 197 +4,417
仓位参考: Max Pain 182 ｜ Call Wall 200（+4.2%）（OI 14.9k） ｜ Put Wall 177.5（-7.5%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 45.4%｜历史 Rank 87%（近端代理）｜净 delta 敞口 正 353,263 股

10-09（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 200（+4.2%，弱）（OI 3.2k） ｜ Put Wall 190（-1.0%，弱）（OI 3.4k）

10-16（MEDIUM △）Top ΔOI: 157P +1,340 ｜ 205C +1,006
10-16（MEDIUM △）仓位参考: Max Pain 165 ｜ Call Wall 200（+4.2%，弱）（OI 13.3k） ｜ Put Wall 175（-8.8%，弱）（OI 7.4k）

10-23（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（-6.2%）（OI 4.6k） ｜ Put Wall 175（-8.8%，弱）（OI 1.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/PLTR_morning.json