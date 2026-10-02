# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $754.02
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-05 245C ΔOI +5,566（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 230.86 → 今开 236.05（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 237.87 ｜ 低 234.53

Options: P/C成交量 0.50 | OI比 0.79 | ATM IV 41.5% | Skew 2.0pp | Term 0.72 | ExpMove ±1.7%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价薄（Skew 2.0pp）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-05（3D）±1.7% ｜ 10-07（5D）±2.5% ｜ 10-09（7D）±3.2% ｜ 10-12（10D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 809,743,471 | GEX Change vs 上次快照 230,320,502 | Flip: Primary Flip: 220.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 667 / LOW 211 / INVALID 442
结构观察区: Primary Flip 220.89（全链重定价，覆盖 95%）
Call Wall 250（弱结构｜现价低于该位 5.0%）
最近结构参考: Call Wall 250（现价低于该位 5.0%）
量化视角： 正 Gamma（8.10亿，无历史分位）｜正 Gamma 增强（+2.30亿）｜现价位于 Flip 上方 7.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 228（MaxPain，仅结算参考）；上方 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 221（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 235.0C — Vol 33,128 | 最新价 $2.36 | OI 12707→29942 (ΔOI +17235张) | ΔOI/Volume 52.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17235张（+135.6% vs前日OI），连续性待观察（方向未知）
10-09 242.5C — Vol 17,815 | 最新价 $0.60 | OI 2432→17666 (ΔOI +15234张) | ΔOI/Volume 85.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15234张（+626.4% vs前日OI），连续性待观察（方向未知）
10-09 105.0P — Vol 13,407 | 最新价 $0.01 | OI 1190→13951 (ΔOI +12761张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12761张（+1072.3% vs前日OI），连续性待观察（方向未知）
10-02 240.0C — Vol 84,413 | 最新价 $0.05 | OI 37812→49128 (ΔOI +11316张) | ΔOI/Volume 13.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11316张（+29.9% vs前日OI），连续性待观察（方向未知）
10-02 227.5P — Vol 111,245 | 最新价 $0.47 | OI 12163→22182 (ΔOI +10019张) | ΔOI/Volume 9.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10019张（+82.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 66,565 张（Put 22,780 / Call 43,785），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 546.4k / P 433.1k，今日成交量: C 404.3k / P 202.2k，平值价格ATM: C $0.94 / P $1.21 ｜ ATM IV 41.5%，预期波动 ±0.9%，Max Pain 228
Top ΔOI: C 227 -14,903 ｜ C 240 +11,316 ｜ P 227 +10,019

📆 Forward Expiration Structure

10-05  C +24.0k / P +23.3k ｜ Activity HIGH ｜ 3D
10-07  C +15.8k / P +7.8k ｜ Activity HIGH ｜ 5D
10-09  C +57.2k / P +49.2k ｜ Activity HIGH ｜ 7D
10-12  C +3.0k / P +1.6k ｜ Activity HIGH ｜ 10D

📆 10-05 Forward Structure
存量OI: C 73.3k / P 62.3k，今日变化ΔOI: C +24.0k / P +23.3k，平值价格ATM: C $1.88 / P $2.18 ｜ ATM IV 22.4%，净 delta 敞口 811k shares
Top ΔOI: C 245 +5,566
仓位参考: Max Pain 228 ｜ Call Wall 235（-1.1%）（OI 13.9k） ｜ Put Wall 220（-7.4%，弱）（OI 5.7k）
量化解读： 存量 Call 重｜ATM IV 22.4%｜历史 Rank 45%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 810,969 股

📆 10-07 Forward Structure
存量OI: C 30.7k / P 23.7k，今日变化ΔOI: C +15.8k / P +7.8k，平值价格ATM: C $2.91 / P $3.15 ｜ ATM IV 26.8%，净 delta 敞口 479k shares
Top ΔOI: C 247 +3,632 ｜ P 230 +2,991 ｜ C 235 +1,611
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+4.2%）（OI 7.4k） ｜ Put Wall 230（-3.2%）（OI 8.5k）
量化解读： 存量 Call 重｜ATM IV 26.8%｜历史 Rank 45%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 479,450 股

📆 10-09 Forward Structure
存量OI: C 189.8k / P 237.8k，今日变化ΔOI: C +57.2k / P +49.2k，平值价格ATM: C $3.70 / P $3.90 ｜ ATM IV 28.5%，净 delta 敞口 2.1M shares
Top ΔOI: C 235 +17,235 ｜ C 242 +15,234
仓位参考: Max Pain 228 ｜ Call Wall 235（-1.1%，弱）（OI 29.9k） ｜ Put Wall 220（-7.4%，弱）（OI 23.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.5%｜历史 Rank 45%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,089,263 股

📆 10-12 Forward Structure
存量OI: C 9.3k / P 4.0k，今日变化ΔOI: C +3.0k / P +1.6k，平值价格ATM: C $4.25 / P $4.15 ｜ ATM IV 25.9%，净 delta 敞口 135k shares
Top ΔOI: C 230 +708 ｜ C 247 +469 ｜ C 232 +393
仓位参考: Max Pain 230 ｜ Call Wall 240（+1.0%）（OI 2.9k） ｜ Put Wall 222.5（-6.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 25.9%｜历史 Rank 45%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 134,552 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NVDA_morning.json