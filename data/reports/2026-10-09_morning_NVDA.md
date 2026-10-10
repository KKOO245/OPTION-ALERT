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
🟡 **近现价集中开仓**: 10-12 230C ΔOI +4,181（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 250C ΔOI +8,883 占该期限总 OI 30.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 230.48 → 今开 233.88（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 233.89 ｜ 低 230.61

Options: P/C成交量 0.69 | OI比 1.11 | ATM IV 40.5% | Skew 2.8pp | Term 0.74 | ExpMove ±1.7%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.11×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-12（3D）±1.7% ｜ 10-14（5D）±2.7% ｜ 10-16（7D）±3.4% ｜ 10-19（10D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 290,064,167 | GEX Change vs 上次快照 164,530,340 | Flip: Primary Flip: 223.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 708 / LOW 198 / INVALID 534
结构观察区: Primary Flip 223.91（全链重定价，覆盖 94%）
Put Wall 220（弱结构｜现价高于该位 4.9%） | Call Wall 240（弱结构｜现价低于该位 3.8%）
最近结构参考: Flip 224（现价高于该位 3.1%）
量化视角： 正 Gamma（2.90亿，无历史分位）｜正 Gamma 增强（+1.65亿）｜现价位于 Flip 上方 3.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 230（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 242.5C — Vol 23,346 | 最新价 $0.71 | OI 7390→22250 (ΔOI +14860张) | ΔOI/Volume 63.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14860张（+201.1% vs前日OI），连续性待观察（方向未知）
10-23 125.0P — Vol 14,145 | 最新价 $0.04 | OI 1572→15321 (ΔOI +13749张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13749张（+874.6% vs前日OI），连续性待观察（方向未知）
10-09 232.5C — Vol 95,211 | 最新价 $0.92 | OI 4189→16185 (ΔOI +11996张) | ΔOI/Volume 12.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11996张（+286.4% vs前日OI），连续性待观察（方向未知）
10-09 235.0C — Vol 171,589 | 最新价 $0.34 | OI 32009→43719 (ΔOI +11710张) | ΔOI/Volume 6.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11710张（+36.6% vs前日OI），连续性待观察（方向未知）
10-16 235.0C — Vol 41,441 | 最新价 $2.45 | OI 43217→53070 (ΔOI +9853张) | ΔOI/Volume 23.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9853张（+22.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 62,168 张（Put 13,749 / Call 48,419），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 431.5k / P 478.2k，今日成交量: C 169.2k / P 115.9k，平值价格ATM: C $1.54 / P $0.61 ｜ ATM IV 40.5%，预期波动 ±0.9%，Max Pain 230
Top ΔOI: C 245 -14,091 ｜ C 232 +11,996 ｜ C 235 +11,710

📆 Forward Expiration Structure

10-12  C +16.1k / P +21.6k ｜ Activity HIGH ｜ 3D
10-14  C +13.6k / P +5.4k ｜ Activity HIGH ｜ 5D
10-16  C +38.3k / P +32.0k ｜ Activity HIGH ｜ 7D
10-19  C +19.9k / P +1.3k ｜ Activity HIGH ｜ 10D

📆 10-12 Forward Structure
存量OI: C 55.0k / P 54.9k，今日变化ΔOI: C +16.1k / P +21.6k，平值价格ATM: C $2.43 / P $1.49 ｜ ATM IV 22.0%，净 delta 敞口 284k shares
Top ΔOI: C 230 +4,181 ｜ C 232 +3,378
仓位参考: Max Pain 232 ｜ Call Wall 240（+4.0%，弱）（OI 7.3k） ｜ Put Wall 220（-4.7%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 22.0%｜历史 Rank 42%（近端代理）｜IV/RV 1.04×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 283,813 股

📆 10-14 Forward Structure
存量OI: C 32.6k / P 16.0k，今日变化ΔOI: C +13.6k / P +5.4k，平值价格ATM: C $3.60 / P $2.59 ｜ ATM IV 27.6%，净 delta 敞口 151k shares
Top ΔOI: C 250 +2,532 ｜ C 240 +2,208 ｜ C 245 +2,062
仓位参考: Max Pain 232 ｜ Call Wall 250（+8.3%，弱）（OI 5.3k） ｜ Put Wall 237.5（+2.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 27.6%｜历史 Rank 42%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 151,471 股

📆 10-16 Forward Structure
存量OI: C 949.1k / P 710.1k，今日变化ΔOI: C +38.3k / P +32.0k，平值价格ATM: C $4.43 / P $3.30 ｜ ATM IV 29.6%，净 delta 敞口 556k shares
Top ΔOI: C 242 +14,860 ｜ C 235 +9,853 ｜ C 232 +8,235
仓位参考: Max Pain 215 ｜ Call Wall 220（-4.7%，弱）（OI 99.2k） ｜ Put Wall 220（-4.7%，弱）（OI 54.8k）
量化解读： 存量 Call 重｜ATM IV 29.6%｜历史 Rank 42%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 555,867 股

📆 10-19 Forward Structure
存量OI: C 24.4k / P 4.3k，今日变化ΔOI: C +19.9k / P +1.3k，平值价格ATM: C $4.75 / P $3.70 ｜ ATM IV 27.2%，净 delta 敞口 142k shares
Top ΔOI: C 250 +8,883 ｜ C 247 +8,776 ｜ C 235 +480
仓位参考: Max Pain 235 ｜ Call Wall 250（+8.3%，弱）（OI 9.4k） ｜ Put Wall 220（-4.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 27.2%｜历史 Rank 42%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 142,185 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/NVDA_morning.json