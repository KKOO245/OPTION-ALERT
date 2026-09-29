# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.73 ｜ QQQ $737.93
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-30 370C ΔOI +4,871（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 390C ΔOI +8,946 占该期限总 OI 20.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 357.45 → 今开 358.42（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 358.74 ｜ 低 352.01

Options: P/C成交量 1.17 | OI比 0.59 | ATM IV 43.8% | Skew -1.5pp | Term 1.01 | ExpMove ±2.1%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.59）+ 当日成交偏 Put（P/C量 1.17）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.17×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（1D）±2.1% ｜ 10-02（3D）±3.6% ｜ 10-05（6D）±4.1% ｜ 10-07（8D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -4,297,088 | GEX Change vs 上次快照 -4,689,447 | Flip: Primary Flip: 353.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1163 / LOW 79 / INVALID 682
结构观察区: Primary Flip 353.19（全链重定价，覆盖 100%）
最近结构参考: Flip 353（现价低于该位 0.2%）
量化视角： 负 Gamma（430万，无历史分位）｜由正转负（469万）｜现价位于 Flip 下方 0.17%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 362（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 353（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-05 390.0C — Vol 10,071 | 最新价 $0.79 | OI 1401→10347 (ΔOI +8946张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8946张（+638.5% vs前日OI），连续性待观察（方向未知）
09-30 420.0C — Vol 7,780 | 最新价 $0.04 | OI 992→6381 (ΔOI +5389张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5389张（+543.2% vs前日OI），连续性待观察（方向未知）
09-30 385.0C — Vol 18,937 | 最新价 $0.17 | OI 1744→7117 (ΔOI +5373张) | ΔOI/Volume 28.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5373张（+308.1% vs前日OI），连续性待观察（方向未知）
09-30 370.0C — Vol 22,021 | 最新价 $0.88 | OI 1661→6532 (ΔOI +4871张) | ΔOI/Volume 22.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4871张（+293.3% vs前日OI），连续性待观察（方向未知）
10-16 500.0C — Vol 6,421 | 最新价 $0.18 | OI 13342→17747 (ΔOI +4405张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4405张（+33.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 28,984 张（Put 0 / Call 28,984），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-30  C +50.7k / P +25.3k ｜ Activity HIGH ｜ 1D
10-02  C +45.5k / P +24.2k ｜ Activity HIGH ｜ 3D
10-05  C +17.1k / P +6.9k ｜ Activity HIGH ｜ 6D
10-07  C +4.6k / P +1.3k ｜ Activity HIGH ｜ 8D

📆 09-30 Forward Structure
存量OI: C 89.5k / P 52.6k，今日变化ΔOI: C +50.7k / P +25.3k，平值价格ATM: C $4.30 / P $3.10 ｜ ATM IV 43.8%，净 delta 敞口 -333k shares
Top ΔOI: C 385 +5,373 ｜ C 370 +4,871
仓位参考: Max Pain 362 ｜ Call Wall 385（+9.2%，弱）（OI 7.1k） ｜ Put Wall 355（+0.7%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 43.8%｜历史 Rank 18%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 332,966 股

📆 10-02 Forward Structure
存量OI: C 214.9k / P 242.2k，今日变化ΔOI: C +45.5k / P +24.2k，平值价格ATM: C $6.90 / P $5.80 ｜ ATM IV 47.2%，净 delta 敞口 60k shares
Top ΔOI: C 365 +4,011 ｜ C 385 +3,981 ｜ C 370 +3,901
仓位参考: Max Pain 362 ｜ Call Wall 385（+9.2%，弱）（OI 14.2k） ｜ Put Wall 350（-0.7%，弱）（OI 6.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.2%｜历史 Rank 18%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,359 股

📆 10-05 Forward Structure
存量OI: C 28.5k / P 14.5k，今日变化ΔOI: C +17.1k / P +6.9k，平值价格ATM: C $7.80 / P $6.54 ｜ ATM IV 38.5%，净 delta 敞口 149k shares
Top ΔOI: C 390 +8,946 ｜ C 370 +1,338
仓位参考: Max Pain 365 ｜ Put Wall 325（-7.8%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 38.5%｜历史 Rank 18%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 148,642 股

📆 10-07 Forward Structure
存量OI: C 6.3k / P 2.0k，今日变化ΔOI: C +4.6k / P +1.3k，平值价格ATM: C $8.62 / P $7.45 ｜ ATM IV 39.3%，净 delta 敞口 51k shares
Top ΔOI: C 375 +762 ｜ C 367 +676 ｜ C 377 +444
仓位参考: Max Pain 360 ｜ Call Wall 375（+6.4%，弱）（OI 0.9k） ｜ Put Wall 360（+2.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 39.3%｜历史 Rank 18%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 51,070 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/TSLA_morning.json