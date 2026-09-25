# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $766.83 ｜ QQQ $740.91
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
🟡 **近现价集中开仓**: 10-02 155C ΔOI +2,852（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 180C ΔOI +10,690 占该期限总 OI 13.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 148.03 → 今开 148.38（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 148.74 ｜ 低 146.26

Options: P/C成交量 0.55 | OI比 0.79 | ATM IV 60.9% | Skew -0.8pp | Term 0.73 | ExpMove ±5.2%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±5.2% ｜ 10-09（14D）±7.0% ｜ 10-16（21D）±8.7% ｜ 10-23（28D）±10.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,110,207 | GEX Change vs 上次快照 44,621,659 | Flip: Primary Flip: 147.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 559 / LOW 132 / INVALID 299
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.58（全链重定价，覆盖 97%）
Call Wall 160（弱结构｜现价低于该位 7.7%）
最近结构参考: Flip 148（现价高于该位 0.1%）
量化视角： 正 Gamma（211万，无历史分位）｜由负转正（+4462万）｜现价位于 Flip 上方 0.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 149（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 180.0C — Vol 12,301 | 最新价 $0.26 | OI 1475→12165 (ΔOI +10690张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10690张（+724.8% vs前日OI），连续性待观察（方向未知）
09-25 150.0C — Vol 47,533 | 最新价 $0.79 | OI 10770→16551 (ΔOI +5781张) | ΔOI/Volume 12.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5781张（+53.7% vs前日OI），连续性待观察（方向未知）
09-25 152.5C — Vol 21,982 | 最新价 $0.31 | OI 11179→16267 (ΔOI +5088张) | ΔOI/Volume 23.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5088张（+45.5% vs前日OI），连续性待观察（方向未知）
09-25 148.0C — Vol 27,182 | 最新价 $1.56 | OI 1495→4846 (ΔOI +3351张) | ΔOI/Volume 12.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3351张（+224.2% vs前日OI），连续性待观察（方向未知）
10-02 155.0C — Vol 9,468 | 最新价 $1.71 | OI 7552→10404 (ΔOI +2852张) | ΔOI/Volume 30.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2852张（+37.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,762 张（Put 0 / Call 27,762），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 260.0k / P 206.0k，今日成交量: C 48.3k / P 26.7k，平值价格ATM: C $0.66 / P $1.38 ｜ ATM IV 60.9%，预期波动 ±1.4%，Max Pain 149
Top ΔOI: C 150 +5,781 ｜ P 150 -5,239 ｜ C 152 +5,088

📆 Forward Expiration Structure

10-02  C +17.6k / P +14.6k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +15.2k / P +3.4k ｜ Activity HIGH ｜ 14D
10-16  C +2.2k / P -2.3k ｜ Activity HIGH ｜ 21D
10-23  C +0.7k / P +1.1k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 109.4k / P 111.6k，今日变化ΔOI: C +17.6k / P +14.6k，平值价格ATM: C $3.53 / P $4.15 ｜ ATM IV 46.0%，净 delta 敞口 161k shares
Top ΔOI: C 155 +2,852 ｜ P 140 +2,653 ｜ C 150 +2,631
仓位参考: Max Pain 150 ｜ Call Wall 155（+4.9%，弱）（OI 10.4k） ｜ Put Wall 140（-5.2%，弱）（OI 6.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.0%｜历史 Rank 59%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 160,645 股

📆 10-09 Forward Structure
存量OI: C 43.5k / P 35.4k，今日变化ΔOI: C +15.2k / P +3.4k，平值价格ATM: C $5.05 / P $5.30 ｜ ATM IV 45.4%，净 delta 敞口 141k shares
Top ΔOI: C 180 +10,690 ｜ C 155 +1,797
仓位参考: Max Pain 150 ｜ Call Wall 155（+4.9%，弱）（OI 4.0k） ｜ Put Wall 135（-8.6%）（OI 4.9k）
量化解读： 存量 Call 重｜ATM IV 45.4%｜历史 Rank 59%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 141,404 股

📆 10-16 Forward Structure
存量OI: C 323.4k / P 332.9k，今日变化ΔOI: C +2.2k / P -2.3k，平值价格ATM: C $6.25 / P $6.57 ｜ ATM IV 44.8%，净 delta 敞口 262k shares
Top ΔOI: P 145 -2,912 ｜ P 150 -1,691 ｜ P 140 +970
仓位参考: Max Pain 140 ｜ Call Wall 160（+8.3%，弱）（OI 34.8k） ｜ Put Wall 135（-8.6%，弱）（OI 28.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.8%｜历史 Rank 59%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 262,311 股

📆 10-23 Forward Structure
存量OI: C 21.8k / P 17.7k，今日变化ΔOI: C +0.7k / P +1.1k，平值价格ATM: C $7.45 / P $7.30 ｜ ATM IV 44.6%，净 delta 敞口 7k shares
Top ΔOI: C 150 +220
仓位参考: Max Pain 149 ｜ Call Wall 150（+1.6%，弱）（OI 2.8k） ｜ Put Wall 135（-8.6%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.6%｜历史 Rank 59%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 7,302 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SPCX_morning.json