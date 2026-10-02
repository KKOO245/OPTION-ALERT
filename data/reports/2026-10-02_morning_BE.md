# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 300C ΔOI +543（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 277.58 → 今开 284.00（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 297.59 ｜ 低 283.10

Options: P/C成交量 0.45 | OI比 1.16 | ATM IV 108.5% | Skew -1.6pp | Term 0.74 | ExpMove ±7.9%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（7D）±7.9% ｜ 10-16（14D）±11.1% ｜ 10-23（21D）±13.9% ｜ 10-30（28D）±18.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,408,386 | GEX Change vs 上次快照 7,999,436 | Flip: Primary Flip: 277.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 523 / LOW 117 / INVALID 250
结构观察区: Primary Flip 277.12（全链重定价，覆盖 97%）
Call Wall 300（弱结构｜现价低于该位 3.5%）
最近结构参考: Call Wall 300（现价低于该位 3.5%）
量化视角： 正 Gamma（1141万，无历史分位）｜正 Gamma 增强（+800万）｜现价位于 Flip 上方 4.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 278（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 277（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 275.0P — Vol 3,330 | 最新价 $14.30 | OI 200→3189 (ΔOI +2989张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2989张（+1494.5% vs前日OI），连续性待观察（方向未知）
10-02 250.0P — Vol 3,630 | 最新价 $0.08 | OI 3167→5260 (ΔOI +2093张) | ΔOI/Volume 57.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2093张（+66.1% vs前日OI），连续性待观察（方向未知）
10-16 277.5C — Vol 2,247 | 最新价 $16.20 | OI 137→2057 (ΔOI +1920张) | ΔOI/Volume 85.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1920张（+1401.5% vs前日OI），连续性待观察（方向未知）
10-02 275.0C — Vol 2,590 | 最新价 $6.10 | OI 1199→2049 (ΔOI +850张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增850张（+70.9% vs前日OI），连续性待观察（方向未知）
10-16 275.0C — Vol 1,465 | 最新价 $17.60 | OI 501→1303 (ΔOI +802张) | ΔOI/Volume 54.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增802张（+160.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,654 张（Put 5,082 / Call 3,572），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 52.2k / P 60.5k，今日成交量: C 21.2k / P 9.6k，平值价格ATM: C $2.81 / P $4.08 ｜ ATM IV 108.5%，预期波动 ±2.4%，Max Pain 278
Top ΔOI: P 250 +2,093 ｜ C 275 +850 ｜ C 280 -713

📆 Forward Expiration Structure

10-09  C +2.5k / P +2.4k ｜ Activity HIGH ｜ 7D
10-16  C +4.1k / P +4.1k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.9k / P +1.0k ｜ Activity HIGH ｜ 21D
10-30  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 17.6k / P 21.5k，今日变化ΔOI: C +2.5k / P +2.4k，平值价格ATM: C $10.75 / P $12.03 ｜ ATM IV 69.8%，净 delta 敞口 90k shares
Top ΔOI: C 300 +543 ｜ C 280 +310
仓位参考: Max Pain 272 ｜ Call Wall 300（+3.7%，弱）（OI 1.6k） ｜ Put Wall 290（+0.2%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.8%｜历史 Rank 67%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 90,213 股

10-16（MEDIUM △）Top ΔOI: 275P +2,989 ｜ 277C +1,920
10-16（MEDIUM △）仓位参考: Max Pain 265 ｜ Call Wall 270（-6.7%，弱）（OI 8.3k） ｜ Put Wall 275（-5.0%，弱）（OI 3.2k）

📆 10-23 Forward Structure
存量OI: C 12.2k / P 16.1k，今日变化ΔOI: C +0.9k / P +1.0k，平值价格ATM: C $19.44 / P $20.75 ｜ ATM IV 71.6%，净 delta 敞口 22k shares
Top ΔOI: C 300 +329
仓位参考: Max Pain 270 ｜ Call Wall 300（+3.7%，弱）（OI 1.4k） ｜ Put Wall 280（-3.2%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 71.6%｜历史 Rank 67%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,522 股

📆 10-30 Forward Structure
存量OI: C 8.6k / P 16.9k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $26.10 / P $26.00 ｜ ATM IV 80.1%，净 delta 敞口 -5k shares
Top ΔOI: P 250 +116
仓位参考: Max Pain 285 ｜ Call Wall 300（+3.7%，弱）（OI 1.2k） ｜ Put Wall 285（-1.5%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 80.1%｜历史 Rank 67%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 负 4,956 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/BE_morning.json