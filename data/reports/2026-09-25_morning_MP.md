# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $766.83 ｜ QQQ $741.00
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
🟡 **近现价集中开仓**: 10-16 48P ΔOI +504（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 49.30 → 今开 49.30（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 49.76 ｜ 低 48.16

Options: P/C成交量 0.45 | OI比 0.67 | ATM IV 75.5% | Skew -10.6pp | Term 0.75 | ExpMove ±6.4%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±6.4% ｜ 10-09（14D）±11.4% ｜ 10-16（21D）±10.8% ｜ 10-23（28D）±12.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 879,658 | GEX Change vs 上次快照 1,209,602 | Flip: Primary Flip: 48.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 267 / LOW 70 / INVALID 147
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.00（全链重定价，覆盖 89%）
Put Wall 50（弱结构｜现价低于该位 3.4%）
最近结构参考: Flip 48（现价高于该位 0.6%）
量化视角： 正 Gamma（88万，无历史分位）｜由负转正（+121万）｜现价位于 Flip 上方 0.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 49（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 49.0C — Vol 2,269 | 最新价 $0.87 | OI 549→2050 (ΔOI +1501张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1501张（+273.4% vs前日OI），连续性待观察（方向未知）
09-25 50.0C — Vol 1,285 | 最新价 $0.42 | OI 1286→2011 (ΔOI +725张) | ΔOI/Volume 56.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增725张（+56.4% vs前日OI），连续性待观察（方向未知）
10-02 51.0C — Vol 651 | 最新价 $0.90 | OI 179→713 (ΔOI +534张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增534张（+298.3% vs前日OI），连续性待观察（方向未知）
10-16 48.5P — Vol 504 | 最新价 $2.26 | OI 37→541 (ΔOI +504张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增504张（+1362.2% vs前日OI），连续性待观察（方向未知）
10-02 54.0C — Vol 723 | 最新价 $0.34 | OI 214→603 (ΔOI +389张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增389张（+181.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,653 张（Put 504 / Call 3,149），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 17.5k / P 11.7k，今日成交量: C 0.5k / P 0.2k，平值价格ATM: C $0.39 / P $0.41 ｜ ATM IV 75.5%，预期波动 ±1.6%，Max Pain 49
Top ΔOI: C 49 +1,501 ｜ C 50 +725 ｜ P 55 -422

📆 Forward Expiration Structure

10-02  C +1.5k / P +0.5k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +0.2k / P +39 ｜ Activity MEDIUM △ ｜ 14D
10-16  C +0.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +68 / P +30 ｜ Activity LOW ｜ 28D

📆 10-02 Forward Structure
存量OI: C 9.5k / P 5.7k，今日变化ΔOI: C +1.5k / P +0.5k，平值价格ATM: C $1.97 / P $1.10 ｜ ATM IV 54.8%，净 delta 敞口 20k shares
Top ΔOI: C 51 +534 ｜ C 50 +332
仓位参考: Max Pain 50 ｜ Call Wall 49（+1.4%，弱）（OI 1.2k） ｜ Put Wall 50（+3.5%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 54.8%｜历史 Rank 64%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 20,457 股

10-09（MEDIUM △）Top ΔOI: 50C -16
10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 47（-2.7%）（OI 1.1k）

10-16（MEDIUM △）Top ΔOI: 48P +504 ｜ 45C +196
10-16（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 50（+3.5%，弱）（OI 3.0k） ｜ Put Wall 50（+3.5%，弱）（OI 3.3k）

10-23（Activity LOW）仓位参考: Max Pain 52 ｜ Put Wall 50（+3.5%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/MP_morning.json