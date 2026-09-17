# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **事件差分**: 09-18（2D）ATM IV 100.9% vs 09-25 83.5%（差 +17.3pp），覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 259.35 → 今开 268.24（+3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 275.18 ｜ 低 263.50

Options: P/C成交量 0.51 | OI比 0.88 | ATM IV 100.9% | Skew -0.2pp | Term 0.80 | ExpMove ±6.2%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±6.2% ｜ 09-25（9D）±10.7% ｜ 10-02（16D）±14.0% ｜ 10-09（23D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,610,209 | GEX Change vs 上次快照 3,520,662 | Flip: Primary Flip: 240.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 612 / LOW 91 / INVALID 257
结构观察区: Primary Flip 240.13（全链重定价，覆盖 100%）
Call Wall 250（弱结构｜现价高于该位 7.9%）
最近结构参考: Call Wall 250（现价高于该位 7.9%）
量化视角： 正 Gamma（2361万，无历史分位）｜正 Gamma 增强（+352万）｜现价位于 Flip 上方 12.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 248（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 240（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 292.5C — Vol 6,230 | 最新价 $0.96 | OI 506→6349 (ΔOI +5843张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5843张（+1154.7% vs前日OI），连续性待观察（方向未知）
09-18 247.5P — Vol 5,726 | 最新价 $3.90 | OI 329→5944 (ΔOI +5615张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5615张（+1706.7% vs前日OI），连续性待观察（方向未知）
09-18 250.0P — Vol 8,076 | 最新价 $4.75 | OI 3615→8410 (ΔOI +4795张) | ΔOI/Volume 59.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4795张（+132.6% vs前日OI），连续性待观察（方向未知）
09-18 290.0C — Vol 6,630 | 最新价 $1.15 | OI 6148→10870 (ΔOI +4722张) | ΔOI/Volume 71.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4722张（+76.8% vs前日OI），连续性待观察（方向未知）
10-16 100.0P — Vol 1,454 | 最新价 $0.03 | OI 2545→3948 (ΔOI +1403张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1403张（+55.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,378 张（Put 11,813 / Call 10,565），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +13.4k / P +14.6k ｜ Activity HIGH ｜ 2D
09-25  C +0.9k / P +1.8k ｜ Activity HIGH ｜ 9D
10-02  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 16D
10-09  C +0.2k / P +26 ｜ Activity HIGH ｜ 23D

📆 09-18 Forward Structure
存量OI: C 159.8k / P 141.1k，今日变化ΔOI: C +13.4k / P +14.6k，平值价格ATM: C $8.80 / P $7.95 ｜ ATM IV 100.9%，净 delta 敞口 131k shares
Top ΔOI: C 292 +5,843 ｜ P 247 +5,615 ｜ P 250 +4,795
仓位参考: Max Pain 248 ｜ Call Wall 250（-7.3%）（OI 21.3k） ｜ Put Wall 250（-7.3%，弱）（OI 8.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 100.9%｜历史 Rank 62%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 130,735 股

📆 09-25 Forward Structure
存量OI: C 17.0k / P 21.3k，今日变化ΔOI: C +0.9k / P +1.8k，平值价格ATM: C $15.00 / P $13.75 ｜ ATM IV 83.5%，净 delta 敞口 9k shares
Top ΔOI: C 300 +443
仓位参考: Max Pain 245 ｜ Call Wall 280（+3.8%，弱）（OI 1.7k） ｜ Put Wall 250（-7.3%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 83.5%｜历史 Rank 62%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,002 股

10-02（MEDIUM △）仓位参考: Max Pain 245 ｜ Call Wall 275（+1.9%，弱）（OI 1.8k） ｜ Put Wall 245（-9.2%，弱）（OI 1.0k）

📆 10-09 Forward Structure
存量OI: C 2.8k / P 6.7k，今日变化ΔOI: C +0.2k / P +26，平值价格ATM: C $23.50 / P $21.00 ｜ ATM IV 80.8%，净 delta 敞口 1k shares
仓位参考: Max Pain 250 ｜ Call Wall 295（+9.3%）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.8%｜历史 Rank 62%（近端代理）｜净 delta 敞口 正 1,248 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 100.9% vs 09-25 83.5%（差 +17.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/BE_morning.json