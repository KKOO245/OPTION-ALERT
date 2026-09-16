# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.92
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

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 94.4% vs 09-25 81.2%（差 +13.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 10-09 240C ΔOI +1,468 占该期限总 OI 11.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 207.37 → 今开 212.09（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 218.93 ｜ 低 210.90

Options: P/C成交量 0.50 | OI比 1.30 | ATM IV 94.4% | Skew 1.8pp | Term 0.84 | ExpMove ±5.9%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±5.9% ｜ 09-25（9D）±10.4% ｜ 10-02（16D）±15.3% ｜ 10-09（23D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,961,478 | GEX Change vs 上次快照 2,396,785 | Flip: Primary Flip: 228.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 517 / LOW 70 / INVALID 179
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 228.07（全链重定价，覆盖 98%）
Put Wall 200（弱结构｜现价高于该位 8.5%）
最近结构参考: Flip 228（现价低于该位 4.8%）
量化视角： 负 Gamma（896万，无历史分位）｜负 Gamma 缓解（+240万）｜现价位于 Flip 下方 4.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 228（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 202.5C — Vol 1,830 | 最新价 $14.00 | OI 29→1855 (ΔOI +1826张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1826张（+6296.6% vs前日OI），连续性待观察（方向未知）
10-09 240.0C — Vol 1,647 | 最新价 $6.80 | OI 106→1574 (ΔOI +1468张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1468张（+1384.9% vs前日OI），连续性待观察（方向未知）
09-25 330.0C — Vol 597 | 最新价 $0.04 | OI 365→952 (ΔOI +587张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增587张（+160.8% vs前日OI），连续性待观察（方向未知）
09-25 130.0P — Vol 582 | 最新价 $0.08 | OI 2553→3087 (ΔOI +534张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增534张（+20.9% vs前日OI），连续性待观察（方向未知）
09-18 190.0P — Vol 1,109 | 最新价 $1.35 | OI 4017→4463 (ΔOI +446张) | ΔOI/Volume 40.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增446张（+11.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,861 张（Put 980 / Call 3,881），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -0.4k / P +1.2k ｜ Activity MEDIUM △ ｜ 2D
09-25  C +4.5k / P +2.3k ｜ Activity HIGH ｜ 9D
10-02  C +1.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
10-09  C +2.1k / P +0.2k ｜ Activity HIGH ｜ 23D

📆 09-18 Forward Structure
存量OI: C 140.1k / P 182.1k，今日变化ΔOI: C -0.4k / P +1.2k，平值价格ATM: C $6.20 / P $6.57 ｜ ATM IV 94.4%，净 delta 敞口 36k shares
Top ΔOI: C 197 -1,474 ｜ P 280 -910
仓位参考: Max Pain 220 ｜ Call Wall 200（-7.9%，弱）（OI 7.2k） ｜ Put Wall 210（-3.3%，弱）（OI 10.5k）
量化解读： 存量 Put 重｜ATM IV 94.4%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,956 股

📆 09-25 Forward Structure
存量OI: C 23.4k / P 23.5k，今日变化ΔOI: C +4.5k / P +2.3k，平值价格ATM: C $10.76 / P $11.75 ｜ ATM IV 81.2%，净 delta 敞口 161k shares
Top ΔOI: C 202 +1,826
仓位参考: Max Pain 212 ｜ Call Wall 227.5（+4.8%）（OI 3.0k） ｜ Put Wall 200（-7.9%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 81.2%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 160,666 股

10-02（MEDIUM △）Top ΔOI: 215C +274
10-02（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 210（-3.3%，弱）（OI 0.3k） ｜ Put Wall 200（-7.9%，弱）（OI 0.6k）

📆 10-09 Forward Structure
存量OI: C 6.1k / P 6.8k，今日变化ΔOI: C +2.1k / P +0.2k，平值价格ATM: C $18.63 / P $15.95 ｜ ATM IV 80.1%，净 delta 敞口 85k shares
Top ΔOI: C 240 +1,468 ｜ C 215 +324 ｜ C 190 +150
仓位参考: Max Pain 220 ｜ Call Wall 215（-1.0%，弱）（OI 0.4k） ｜ Put Wall 200（-7.9%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.1%｜历史 Rank 30%（近端代理）｜净 delta 敞口 正 85,480 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 94.4% vs 09-25 81.2%（差 +13.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/NBIS_morning.json