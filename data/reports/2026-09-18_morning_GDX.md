# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.85 ｜ QQQ $nan
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 98C ΔOI +10,090（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 98C ΔOI +10,090 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 94.8）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 95.92 → 今开 96.15（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 96.21 ｜ 低 94.41

Options: P/C成交量 0.48 | OI比 1.32 | ATM IV 41.8% | Skew -4.9pp | Term 1.01 | ExpMove ±4.7%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -4.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±4.7% ｜ 10-02（14D）±6.9% ｜ 10-09（21D）±8.3% ｜ 10-16（28D）±9.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -1,933,415 | GEX Change vs 上次快照 -21,988,065 | Flip: Candidates 94.81 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 73%（带内） ｜ IV 有效性: VALID 492 / LOW 145 / INVALID 273
结构观察区: ≈95（全链重定价，覆盖 73%，CONDITIONAL）
Call Wall 100（弱结构｜现价低于该位 5.2%）
最近结构参考: Flip 95（现价低于该位 0.1%）
量化视角： 负 Gamma（193万，无历史分位）｜由正转负（2199万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 91（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 95（全链重定价，覆盖 73%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 98.0C — Vol 8 | 最新价 $1.17 | OI 273→10363 (ΔOI +10090张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10090张（+3696.0% vs前日OI），连续性待观察（方向未知）
09-25 102.0C — Vol 10,174（Yahoo补） | 最新价 $0.63 | OI 735→10794 (ΔOI +10059张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10059张（+1368.6% vs前日OI），连续性待观察（方向未知）
09-25 103.0C — Vol 1 | 最新价 $0.43 | OI 402→10454 (ΔOI +10052张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10052张（+2500.5% vs前日OI），连续性待观察（方向未知）
09-25 99.0C — Vol 10,139（Yahoo补） | 最新价 $1.32 | OI 214→10218 (ΔOI +10004张) | ΔOI/Volume 98.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10004张（+4674.8% vs前日OI），连续性待观察（方向未知）
10-16 75.0P — Vol 4,026（Yahoo补） | 最新价 $0.13 | OI 6918→10378 (ΔOI +3460张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3460张（+50.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 43,665 张（Put 3,460 / Call 40,205），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 314.1k / P 415.8k，今日成交量: C 3.5k / P 1.6k，平值价格ATM: C $0.28 / P $0.60 ｜ ATM IV 41.8%，预期波动 ±0.9%，Max Pain 91
Top ΔOI: C 103 -10,260 ｜ C 99 -7,869 ｜ C 105 -6,308

📆 Forward Expiration Structure

09-25  C +42.0k / P +1.6k ｜ Activity HIGH ｜ 7D
10-02  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
10-09  C +0.4k / P +38 ｜ Activity MEDIUM △ ｜ 21D
10-16  C +1.5k / P +5.7k ｜ Activity MEDIUM △ ｜ 28D

📆 09-25 Forward Structure
存量OI: C 73.7k / P 22.8k，今日变化ΔOI: C +42.0k / P +1.6k，平值价格ATM: C $2.13 / P $2.30 ｜ ATM IV 41.5%，净 delta 敞口 783k shares
Top ΔOI: C 98 +10,090 ｜ C 102 +10,059 ｜ C 103 +10,052
仓位参考: Max Pain 95 ｜ Call Wall 102（+7.7%，弱）（OI 10.8k） ｜ Put Wall 93（-1.8%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 41.5%｜历史 Rank 64%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 正 783,013 股

10-02（MEDIUM △）Top ΔOI: 88P +342 ｜ 90P -149
10-02（MEDIUM △）仓位参考: Max Pain 99 ｜ Call Wall 100（+5.5%，弱）（OI 3.2k） ｜ Put Wall 97（+2.4%）（OI 11.3k）

10-09（MEDIUM △）Top ΔOI: 100C +111 ｜ 65C +47
10-09（MEDIUM △）仓位参考: Max Pain 94 ｜ Call Wall 94（-0.8%，弱）（OI 0.7k） ｜ Put Wall 90（-5.0%，弱）（OI 1.9k）

10-16（MEDIUM △）Top ΔOI: 75P +3,460 ｜ 90P -2,146
10-16（MEDIUM △）仓位参考: Max Pain 92 ｜ Call Wall 100（+5.5%）（OI 10.5k） ｜ Put Wall 90（-5.0%，弱）（OI 9.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/GDX_morning.json