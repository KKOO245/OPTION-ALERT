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
🔵 **期限 OI 集中**: 10-09 100P ΔOI +3,000 占该期限总 OI 11.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 172.56 → 今开 170.39（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 172.84 ｜ 低 168.96

Options: P/C成交量 0.70 | OI比 0.84 | ATM IV 58.6% | Skew 0.1pp | Term 0.83 | ExpMove ±3.7%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 0.1pp）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±3.7% ｜ 09-25（9D）±6.4% ｜ 10-02（16D）±8.3% ｜ 10-09（23D）±9.9%
   ⇒ IV–VIX Spread: +41.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 57,781,075 | GEX Change vs 上次快照 -4,206,195 | Flip: Primary Flip: 164.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 618 / LOW 72 / INVALID 130
结构观察区: Primary Flip 164.88（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 1.0%） | Call Wall 180（弱结构｜现价低于该位 4.6%）
最近结构参考: Put Wall 170（现价高于该位 1.0%）
量化视角： 正 Gamma（5778万，无历史分位）｜正 Gamma 减弱（421万）｜现价位于 Flip 上方 4.19%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 158（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 160.0P — Vol 22,574 | 最新价 $0.49 | OI 14037→20771 (ΔOI +6734张) | ΔOI/Volume 29.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6734张（+48.0% vs前日OI），连续性待观察（方向未知）
10-16 185.0C — Vol 6,254 | 最新价 $5.38 | OI 4575→9970 (ΔOI +5395张) | ΔOI/Volume 86.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5395张（+117.9% vs前日OI），连续性待观察（方向未知）
10-09 100.0P — Vol 3,000 | 最新价 $0.14 | OI 14→3014 (ΔOI +3000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3000张（+21428.6% vs前日OI），连续性待观察（方向未知）
10-16 100.0P — Vol 4,161 | 最新价 $0.15 | OI 8206→11150 (ΔOI +2944张) | ΔOI/Volume 70.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2944张（+35.9% vs前日OI），连续性待观察（方向未知）
09-18 190.0C — Vol 9,067 | 最新价 $0.20 | OI 14240→16944 (ΔOI +2704张) | ΔOI/Volume 29.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2704张（+19.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,777 张（Put 12,678 / Call 8,099），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -2.9k / P +15.1k ｜ Activity HIGH ｜ 2D
09-25  C +3.6k / P +2.3k ｜ Activity HIGH ｜ 9D
10-02  C +1.0k / P +1.2k ｜ Activity HIGH ｜ 16D
10-09  C +0.6k / P +3.8k ｜ Activity HIGH ｜ 23D

📆 09-18 Forward Structure
存量OI: C 348.7k / P 291.5k，今日变化ΔOI: C -2.9k / P +15.1k，平值价格ATM: C $2.89 / P $3.52 ｜ ATM IV 58.6%，净 delta 敞口 -737k shares
Top ΔOI: P 160 +6,734 ｜ C 85 -3,962
仓位参考: Max Pain 158 ｜ Call Wall 180（+4.8%，弱）（OI 31.0k） ｜ Put Wall 160（-6.9%，弱）（OI 20.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.6%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 737,365 股

📆 09-25 Forward Structure
存量OI: C 36.4k / P 43.0k，今日变化ΔOI: C +3.6k / P +2.3k，平值价格ATM: C $5.25 / P $5.76 ｜ ATM IV 49.8%，净 delta 敞口 46k shares
Top ΔOI: C 185 +749 ｜ C 187 +391
仓位参考: Max Pain 172 ｜ Call Wall 185（+7.7%，弱）（OI 3.4k） ｜ Put Wall 170（-1.0%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.8%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,299 股

📆 10-02 Forward Structure
存量OI: C 20.0k / P 24.7k，今日变化ΔOI: C +1.0k / P +1.2k，平值价格ATM: C $6.93 / P $7.35 ｜ ATM IV 48.8%，净 delta 敞口 9k shares
仓位参考: Max Pain 175 ｜ Call Wall 180（+4.8%，弱）（OI 2.8k） ｜ Put Wall 170（-1.0%）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 48.8%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,693 股

📆 10-09 Forward Structure
存量OI: C 10.1k / P 15.6k，今日变化ΔOI: C +0.6k / P +3.8k，平值价格ATM: C $7.75 / P $9.23 ｜ ATM IV 48.4%，净 delta 敞口 -3k shares
Top ΔOI: P 170 +409
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+0.4%，弱）（OI 0.5k） ｜ Put Wall 170（-1.0%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 48.4%｜历史 Rank 86%（近端代理）｜净 delta 敞口 负 2,530 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 58.6% vs 09-25 49.8%（差 +8.8pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/PLTR_morning.json