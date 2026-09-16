# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.93
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 141.90 → 今开 139.20（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 141.49 ｜ 低 138.33

Options: P/C成交量 0.62 | OI比 0.98 | ATM IV 61.4% | Skew 2.4pp | Term 0.86 | ExpMove ±3.9%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±3.9% ｜ 09-25（9D）±7.0% ｜ 10-02（16D）±9.0% ｜ 10-09（23D）±10.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,056,117 | GEX Change vs 上次快照 -1,561,384 | Flip: Primary Flip: 129.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 585 / LOW 85 / INVALID 132
结构观察区: Primary Flip 129.45（全链重定价，覆盖 94%）
Call Wall 150（弱结构｜现价低于该位 6.3%）
最近结构参考: Call Wall 150（现价低于该位 6.3%）
量化视角： 正 Gamma（2206万，无历史分位）｜正 Gamma 减弱（156万）｜现价位于 Flip 上方 8.56%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 129（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 140.0C — Vol 2,144 | 最新价 $10.15 | OI 2235→3256 (ΔOI +1021张) | ΔOI/Volume 47.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1021张（+45.7% vs前日OI），连续性待观察（方向未知）
10-16 150.0C — Vol 2,091 | 最新价 $5.90 | OI 8776→9520 (ΔOI +744张) | ΔOI/Volume 35.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增744张（+8.5% vs前日OI），连续性待观察（方向未知）
10-16 125.0P — Vol 999 | 最新价 $2.52 | OI 2555→3276 (ΔOI +721张) | ΔOI/Volume 72.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增721张（+28.2% vs前日OI），连续性待观察（方向未知）
09-18 165.0C — Vol 788 | 最新价 $0.06 | OI 1479→2192 (ΔOI +713张) | ΔOI/Volume 90.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增713张（+48.2% vs前日OI），连续性待观察（方向未知）
09-25 160.0C — Vol 1,391 | 最新价 $0.78 | OI 770→1356 (ΔOI +586张) | ΔOI/Volume 42.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增586张（+76.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,785 张（Put 721 / Call 3,064），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -1.1k / P +1.3k ｜ Activity HIGH ｜ 2D
09-25  C +3.4k / P +1.2k ｜ Activity HIGH ｜ 9D
10-02  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 16D
10-09  C +0.3k / P +53 ｜ Activity MEDIUM △ ｜ 23D

📆 09-18 Forward Structure
存量OI: C 113.4k / P 111.4k，今日变化ΔOI: C -1.1k / P +1.3k，平值价格ATM: C $2.59 / P $2.95 ｜ ATM IV 61.4%，净 delta 敞口 -226k shares
Top ΔOI: C 125 -943 ｜ C 140 -324
仓位参考: Max Pain 120 ｜ Call Wall 150（+6.7%，弱）（OI 7.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.4%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 226,342 股

📆 09-25 Forward Structure
存量OI: C 15.4k / P 10.6k，今日变化ΔOI: C +3.4k / P +1.2k，平值价格ATM: C $4.84 / P $5.00 ｜ ATM IV 53.9%，净 delta 敞口 23k shares
Top ΔOI: C 150 +471
仓位参考: Max Pain 135 ｜ Call Wall 145（+3.2%，弱）（OI 2.4k） ｜ Put Wall 130（-7.5%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 53.9%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,952 股

📆 10-02 Forward Structure
存量OI: C 8.7k / P 8.4k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $6.20 / P $6.40 ｜ ATM IV 53.5%，净 delta 敞口 10k shares
Top ΔOI: C 150 +278 ｜ P 130 +141
仓位参考: Max Pain 132 ｜ Call Wall 150（+6.7%）（OI 1.8k） ｜ Put Wall 130（-7.5%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 53.5%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,522 股

10-09（MEDIUM △）Top ΔOI: 149C +52 ｜ 144P +51
10-09（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 145（+3.2%，弱）（OI 0.2k） ｜ Put Wall 140（-0.4%）（OI 0.5k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 61.4% vs 09-25 53.9%（差 +7.5pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/NOW_morning.json