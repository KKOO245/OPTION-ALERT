# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.05 ｜ QQQ $706.73
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 175C ΔOI +3,824（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 169.09 → 今开 168.00（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 169.84 ｜ 低 164.15

Options: P/C成交量 0.17 | OI比 0.64 | ATM IV 90.2% | Skew -6.6pp | Term 0.78 | ExpMove ±9.7%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±9.7% ｜ 11-06（14D）±12.7% ｜ 11-13（21D）±14.3% ｜ 11-20（28D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,566,735 | GEX Change vs 上次快照 9,991,194 | Flip: Primary Flip: 160.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 440 / LOW 134 / INVALID 308
结构观察区: Primary Flip 160.40（全链重定价，覆盖 94%）
Call Wall 170（弱结构｜现价低于该位 0.9%）
最近结构参考: Call Wall 170（现价低于该位 0.9%）
量化视角： 正 Gamma（1357万，无历史分位）｜正 Gamma 增强（+999万）｜现价位于 Flip 上方 4.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 175（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 175.0C — Vol 4,123 | 最新价 $6.03 | OI 524→4348 (ΔOI +3824张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3824张（+729.8% vs前日OI），连续性待观察（方向未知）
10-30 182.5C — Vol 3,873 | 最新价 $3.77 | OI 740→4292 (ΔOI +3552张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3552张（+480.0% vs前日OI），连续性待观察（方向未知）
10-30 177.5C — Vol 1,805 | 最新价 $5.30 | OI 358→1997 (ΔOI +1639张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1639张（+457.8% vs前日OI），连续性待观察（方向未知）
10-30 185.0C — Vol 1,813 | 最新价 $3.19 | OI 1934→3512 (ΔOI +1578张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1578张（+81.6% vs前日OI），连续性待观察（方向未知）
10-30 172.5C — Vol 1,756 | 最新价 $7.15 | OI 400→1830 (ΔOI +1430张) | ΔOI/Volume 81.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1430张（+357.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,023 张（Put 0 / Call 12,023），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 64.6k / P 41.1k，今日成交量: C 14.4k / P 2.5k，平值价格ATM: C $2.31 / P $1.10 ｜ ATM IV 90.2%，预期波动 ±2.0%，Max Pain 175
Top ΔOI: C 192 -2,720 ｜ C 190 -1,517 ｜ C 182 +1,416

📆 Forward Expiration Structure

10-30  C +14.2k / P +3.0k ｜ Activity HIGH ｜ 7D
11-06  C +0.3k / P +0.3k ｜ Activity LOW ｜ 14D
11-13  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +0.5k / P +0.9k ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 34.8k / P 23.0k，今日变化ΔOI: C +14.2k / P +3.0k，平值价格ATM: C $8.98 / P $7.30 ｜ ATM IV 86.7%，净 delta 敞口 407k shares
Top ΔOI: C 175 +3,824 ｜ C 182 +3,552 ｜ C 177 +1,639
仓位参考: Max Pain 175 ｜ Call Wall 175（+3.9%，弱）（OI 4.3k） ｜ Put Wall 170（+0.9%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 86.7%｜历史 Rank 81%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 407,341 股

11-06（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 175（+3.9%，弱）（OI 0.4k）

11-13（MEDIUM △）Top ΔOI: 180C +139 ｜ 175P +136
11-13（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 177.5（+5.4%）（OI 1.1k） ｜ Put Wall 160（-5.0%，弱）（OI 0.5k）

11-20（MEDIUM △）Top ΔOI: 167P +551 ｜ 220C +403
11-20（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 170（+0.9%）（OI 13.4k） ｜ Put Wall 165（-2.0%，弱）（OI 2.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/COIN_morning.json