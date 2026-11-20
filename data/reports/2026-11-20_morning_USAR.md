# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $708.73 ｜ QQQ $630.11
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 7C ΔOI +147（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 6.87 → 今开 6.69（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 7.09 ｜ 低 6.62

Options: P/C成交量 0.29 | OI比 0.41 | ATM IV 87.9% | Skew -108.2pp | Term 1.24 | ExpMove ±11.5%（近端） | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构正常偏陡（Term 1.24）｜Put 保护异常便宜（Skew -108.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±11.5% ｜ 12-04（14D）±18.8% ｜ 12-11（21D）±21.9% ｜ 12-18（28D）±23.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,199,064 | GEX Change vs 上次快照 2,150,057 | Flip: Primary Flip: 5.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 218 / LOW 111 / INVALID 33
结构观察区: Primary Flip 5.82（全链重定价，覆盖 99%）
最近结构参考: Flip 6（现价高于该位 16.2%）
量化视角： 正 Gamma（220万，无历史分位）｜正 Gamma 增强（+215万）｜现价位于 Flip 上方 16.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 9（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 6（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 7.5C — Vol 1,595 | 最新价 $0.04 | OI 1515→1997 (ΔOI +482张) | ΔOI/Volume 30.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增482张（+31.8% vs前日OI），连续性待观察（方向未知）
12-18 7.0P — Vol 438 | 最新价 $0.91 | OI 4194→4605 (ΔOI +411张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增411张（+9.8% vs前日OI），连续性待观察（方向未知）
11-20 8.0C — Vol 1,318 | 最新价 $0.01 | OI 3894→4252 (ΔOI +358张) | ΔOI/Volume 27.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增358张（+9.2% vs前日OI），连续性待观察（方向未知）
11-27 8.0C — Vol 871 | 最新价 $0.11 | OI 3705→4062 (ΔOI +357张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增357张（+9.6% vs前日OI），连续性待观察（方向未知）
11-27 7.0C — Vol 370 | 最新价 $0.39 | OI 703→894 (ΔOI +191张) | ΔOI/Volume 51.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增191张（+27.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,799 张（Put 411 / Call 1,388），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 61.0k / P 25.1k，今日成交量: C 1.3k / P 0.4k，平值价格ATM: C $0.15 / P $0.16 ｜ ATM IV 87.9%，预期波动 ±4.6%，Max Pain 9
Top ΔOI: C 7 +482 ｜ C 8 +358 ｜ P 10 -330

📆 Forward Expiration Structure

11-27  C +0.8k / P +0.1k ｜ Activity MEDIUM △ ｜ 7D
12-04  C +0.3k / P -40 ｜ Activity MEDIUM △ ｜ 14D
12-11  C +60 / P +18 ｜ Activity LOW ｜ 21D
12-18  C +0.3k / P -0.6k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 18.8k / P 4.1k，今日变化ΔOI: C +0.8k / P +0.1k，平值价格ATM: C $0.38 / P $0.40 ｜ ATM IV 99.0%，净 delta 敞口 27k shares
Top ΔOI: C 7 +191
仓位参考: Max Pain 8 ｜ Put Wall 7（+3.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 99.0%｜历史 Rank 19%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 27,404 股

12-04（MEDIUM △）Top ΔOI: 7C +147
12-04（MEDIUM △）仓位参考: Max Pain 8 ｜ Call Wall 7（+3.6%，弱）（OI 0.3k） ｜ Put Wall 7（+3.6%）（OI 0.6k）

12-11（Activity LOW）仓位参考: Max Pain 8 ｜ Put Wall 7（+3.6%，弱）（OI 0.1k）

12-18（MEDIUM △）Top ΔOI: 7P +411 ｜ 19P -402
12-18（MEDIUM △）仓位参考: Max Pain 11 ｜ Put Wall 7（+3.6%，弱）（OI 4.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/USAR_morning.json