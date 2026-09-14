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
🟡 **单日价格波动**: -3.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 93.93 → 收盘 94.14（+0.2%） ｜ 今日高 95.08 ｜ 低 92.85 ｜ 昨收 97.10 → 收盘 94.14（-3.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-17，窗口结束前不做对错判定）

Options: P/C成交量 1.78 | OI比 1.31 | ATM IV 51.5% | Skew 0.9pp | Term 0.86 | ExpMove ±4.3%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜当日成交偏 Put（P/C量 1.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.78×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.31×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±4.3% ｜ 09-25（11D）±6.3% ｜ 10-02（18D）±8.0% ｜ 10-09（25D）±9.5%
   ⇒ IV–VIX Spread: +34.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -29,331,890 | GEX Change vs 上次快照 11,920,457 | Flip: Primary Flip: 95.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 579 / LOW 118 / INVALID 205
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 95.84（全链重定价，覆盖 98%）
最近结构参考: Flip 96（现价低于该位 1.8%）
量化视角： 负 Gamma（2933万，无历史分位）｜负 Gamma 缓解（+1192万）｜现价位于 Flip 下方 1.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 92（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 96（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 101.0C — Vol 218 | 最新价 $0.27 | OI 1475→25513 (ΔOI +24038张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24038张（+1629.7% vs前日OI），连续性待观察（方向未知）
09-18 105.0C — Vol 1,553 | 最新价 $0.07 | OI 10923→34698 (ΔOI +23775张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23775张（+217.7% vs前日OI），连续性待观察（方向未知）
09-25 105.0C — Vol 866 | 最新价 $0.48 | OI 691→7356 (ΔOI +6665张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6665张（+964.5% vs前日OI），连续性待观察（方向未知）
09-18 92.0P — Vol 2,206 | 最新价 $1.12 | OI 6856→12581 (ΔOI +5725张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5725张（+83.5% vs前日OI），连续性待观察（方向未知）
09-18 100.0C — Vol 4,005 | 最新价 $0.37 | OI 23467→28162 (ΔOI +4695张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4695张（+20.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 64,898 张（Put 5,725 / Call 59,173），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 334.5k / P 439.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.13 / P $1.95 ｜ ATM IV 51.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 92 ｜ Call Wall 100（+6.2%，弱）（OI 28.2k） ｜ Put Wall 90（-4.4%，弱）（OI 43.4k）
量化解读： 存量 Put 重｜ATM IV 51.5%｜历史 Rank 84%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 95 ｜ Put Wall 87（-7.6%，弱）（OI 1.5k）

10-02（Activity LOW）仓位参考: Max Pain 99 ｜ Call Wall 100（+6.2%，弱）（OI 1.1k） ｜ Put Wall 97（+3.0%）（OI 15.1k）

10-09（Activity LOW）仓位参考: Max Pain 98 ｜ Call Wall 85（-9.7%）（OI 0.2k） ｜ Put Wall 85（-9.7%）（OI 0.4k）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 51.5% vs 09-25 45.1%（差 +6.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/GDX_evening.json