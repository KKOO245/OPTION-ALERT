# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **单日价格波动**: +2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 373.85 → 收盘 377.94（+1.1%） ｜ 今日高 378.58 ｜ 低 372.15 ｜ 昨收 369.15 → 收盘 377.94（+2.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.40 | OI比 1.02 | ATM IV 34.2% | Skew -2.1pp | Term 1.04 | ExpMove ±4.5%（近端） | Rank — (历史不足)
量化视角： 期限结构正常（Term 1.04）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±4.5% ｜ 09-25（11D）±1.5% ｜ 10-02（18D）±3.0% ｜ 10-09（25D）±8.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -422,607 | GEX Change vs 上次快照 -50,911 | Flip: Primary Flip: 379.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 292 / LOW 183 / INVALID 459
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 379.53（全链重定价，覆盖 96%）
Call Wall 400（弱结构｜现价低于该位 5.5%）
最近结构参考: Flip 380（现价低于该位 0.4%）
量化视角： 负 Gamma（42万，无历史分位）｜负 Gamma 加深（5万）｜现价位于 Flip 下方 0.42%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 380（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 380.0C — Vol 2 | 最新价 $11.20 | OI 22→109 (ΔOI +87张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增87张（+395.4% vs前日OI），值得跟踪（方向未知）
09-18 370.0C — Vol 21 | 最新价 $10.09 | OI 391→465 (ΔOI +74张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增74张（+18.9% vs前日OI），值得跟踪（方向未知）
09-18 420.0C — Vol 23 | 最新价 $0.08 | OI 711→774 (ΔOI +63张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增63张（+8.9% vs前日OI），值得跟踪（方向未知）
09-18 385.0C — Vol 9 | 最新价 $2.46 | OI 170→207 (ΔOI +37张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增37张（+21.8% vs前日OI），值得跟踪（方向未知）
09-25 400.0C — Vol 4 | 最新价 $2.10 | OI 61→92 (ΔOI +31张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增31张（+50.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 292 张（Put 0 / Call 292），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 15.9k / P 16.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.10 / P $13.11 ｜ ATM IV 34.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 370 ｜ Call Wall 400（+5.8%，弱）（OI 1.1k） ｜ Put Wall 350（-7.4%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 34.2%｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 365 ｜ Call Wall 405（+7.2%，弱）（OI 0.2k） ｜ Put Wall 360（-4.7%，弱）（OI 0.2k）

10-02（Activity LOW）仓位参考: Max Pain 365 ｜ Call Wall 405（+7.2%，弱）（OI 53）

10-09（Activity LOW）仓位参考: Max Pain 350 ｜ Call Wall 380（+0.5%）（OI 0.1k） ｜ Put Wall 345（-8.7%，弱）（OI 17）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/ISRG_evening.json