# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 09-18 150P ΔOI +5,152（距现价 -4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 157P ΔOI +3,007 占该期限总 OI 20.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.20 → 今开 156.86（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 157.94 ｜ 低 156.32

Options: P/C成交量 3.39 | OI比 1.74 | ATM IV 27.4% | Skew 0.3pp | Term 1.01 | ExpMove ±3.0%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 1.01）｜保护溢价薄（Skew 0.3pp）｜当日成交偏 Put（P/C量 3.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.39×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±3.0% ｜ 09-25（11D）±4.6% ｜ 10-02（18D）±5.9% ｜ 10-09（25D）±1.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -67,114,139 | GEX Change vs 上次快照 1,768,873 | Flip: Primary Flip: 163.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 378 / LOW 107 / INVALID 347
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.65（全链重定价，覆盖 94%）
Put Wall 150（弱结构｜现价高于该位 4.3%） | Call Wall 170（弱结构｜现价低于该位 8.0%）
最近结构参考: Put Wall 150（现价高于该位 4.3%）
量化视角： 负 Gamma（6711万，无历史分位）｜负 Gamma 缓解（+177万）｜现价位于 Flip 下方 4.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 158（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 150.0P — Vol 6,171 | 最新价 $0.53 | OI 15850→21002 (ΔOI +5152张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5152张（+32.5% vs前日OI），连续性待观察（方向未知）
09-18 155.0P — Vol 8,020 | 最新价 $1.81 | OI 15405→20209 (ΔOI +4804张) | ΔOI/Volume 59.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4804张（+31.2% vs前日OI），连续性待观察（方向未知）
09-25 157.0P — Vol 3,341 | 最新价 $3.35 | OI 15→3022 (ΔOI +3007张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3007张（+20046.7% vs前日OI），连续性待观察（方向未知）
09-25 150.0P — Vol 3,255 | 最新价 $1.13 | OI 84→3085 (ΔOI +3001张) | ΔOI/Volume 92.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3001张（+3572.6% vs前日OI），连续性待观察（方向未知）
09-25 170.0C — Vol 3,006 | 最新价 $0.29 | OI 71→3071 (ΔOI +3000张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3000张（+4225.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,964 张（Put 15,964 / Call 3,000），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +3.1k / P +9.6k ｜ Activity HIGH ｜ 4D
09-25  C +3.1k / P +6.4k ｜ Activity HIGH ｜ 11D
10-02  C +41 / P +0.4k ｜ Activity HIGH ｜ 18D
10-09  C +5 / P +33 ｜ Activity MEDIUM △ ｜ 25D

📆 09-18 Forward Structure
存量OI: C 74.4k / P 129.1k，今日变化ΔOI: C +3.1k / P +9.6k，平值价格ATM: C $2.74 / P $2.00 ｜ ATM IV 27.4%，净 delta 敞口 -69k shares
Top ΔOI: P 150 +5,152 ｜ P 155 +4,804 ｜ C 162 +1,059
仓位参考: Max Pain 158 ｜ Call Wall 155（-0.9%，弱）（OI 10.8k） ｜ Put Wall 150（-4.1%，弱）（OI 21.0k）
量化解读： 存量 Put 重｜ATM IV 27.4%｜历史 Rank 16%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 69,135 股

📆 09-25 Forward Structure
存量OI: C 6.1k / P 8.9k，今日变化ΔOI: C +3.1k / P +6.4k，平值价格ATM: C $4.40 / P $2.85 ｜ ATM IV 30.9%，净 delta 敞口 -208k shares
Top ΔOI: P 157 +3,007 ｜ P 150 +3,001 ｜ C 170 +3,000
仓位参考: Max Pain 160 ｜ Call Wall 170（+8.7%）（OI 3.1k） ｜ Put Wall 150（-4.1%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 30.9%｜历史 Rank 16%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 207,914 股

📆 10-02 Forward Structure
存量OI: C 0.8k / P 1.3k，今日变化ΔOI: C +41 / P +0.4k，平值价格ATM: C $5.42 / P $3.86 ｜ ATM IV 28.9%，净 delta 敞口 -12k shares
Top ΔOI: P 147 +200 ｜ P 157 +194 ｜ C 157 +13
仓位参考: Max Pain 160 ｜ Call Wall 165（+5.5%）（OI 0.2k） ｜ Put Wall 157（+0.4%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 28.9%｜历史 Rank 16%（近端代理）｜净 delta 敞口 负 11,559 股

10-09（MEDIUM △）Top ΔOI: 151P +5
10-09（MEDIUM △）仓位参考: Max Pain 160

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/XBI_morning.json