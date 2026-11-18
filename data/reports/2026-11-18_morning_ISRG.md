# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.00 ｜ QQQ $659.51
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 46.5% vs 11-27 36.5%（差 +10.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 12-11 485C ΔOI +71 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 430.53 → 今开 430.20（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 437.33 ｜ 低 427.67

Options: P/C成交量 0.67 | OI比 1.02 | ATM IV 46.5% | Skew 8.8pp | Term 0.77 | ExpMove ±3.1%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±3.1% ｜ 11-27（9D）±3.7% ｜ 12-04（16D）±0.0% ｜ 12-11（23D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,006,216 | GEX Change vs 上次快照 92,718 | Flip: Primary Flip: 419.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 269 / LOW 180 / INVALID 517
结构观察区: Primary Flip 419.34（全链重定价，覆盖 90%）
最近结构参考: Flip 419（现价高于该位 3.3%）
量化视角： 正 Gamma（201万，无历史分位）｜正 Gamma 增强（+9万）｜现价位于 Flip 上方 3.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 419（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-11 485.0C — Vol 71 | 最新价 $1.50 | OI 6→77 (ΔOI +71张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增71张（+1183.3% vs前日OI），连续性待观察（方向未知）
12-18 470.0C — Vol 69 | 最新价 $5.20 | OI 318→358 (ΔOI +40张) | ΔOI/Volume 58.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增40张（+12.6% vs前日OI），值得跟踪（方向未知）
11-20 395.0P — Vol 44 | 最新价 $0.50 | OI 258→287 (ΔOI +29张) | ΔOI/Volume 65.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增29张（+11.2% vs前日OI），值得跟踪（方向未知）
11-20 400.0P — Vol 56 | 最新价 $0.50 | OI 277→305 (ΔOI +28张) | ΔOI/Volume 50.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增28张（+10.1% vs前日OI），值得跟踪（方向未知）
12-18 465.0C — Vol 32 | 最新价 $5.94 | OI 205→226 (ΔOI +21张) | ΔOI/Volume 65.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增21张（+10.2% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 189 张（Put 57 / Call 132），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -0.2k / P +66 ｜ Activity MEDIUM △ ｜ 2D
11-27  C +25 / P +14 ｜ Activity LOW ｜ 9D
12-04  C +19 / P -15 ｜ Activity LOW ｜ 16D
12-11  C +67 / P +22 ｜ Activity HIGH ｜ 23D

📆 11-20 Forward Structure
存量OI: C 10.5k / P 10.7k，今日变化ΔOI: C -0.2k / P +66，平值价格ATM: C $5.70 / P $7.86 ｜ ATM IV 46.5%，净 delta 敞口 -4k shares
Top ΔOI: C 440 -79 ｜ C 470 -57 ｜ P 395 +29
仓位参考: Max Pain 410 ｜ Call Wall 420（-3.1%，弱）（OI 0.8k） ｜ Put Wall 410（-5.4%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 46.5%｜历史 Rank 82%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,172 股

11-27（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 430（-0.8%，弱）（OI 64） ｜ Put Wall 395（-8.9%，弱）（OI 0.2k）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 475（+9.6%，弱）（OI 71） ｜ Put Wall 405（-6.5%，弱）（OI 24）

📆 12-11 Forward Structure
存量OI: C 0.4k / P 0.1k，今日变化ΔOI: C +67 / P +22，平值价格ATM: C $15.30 / P $17.34 ｜ ATM IV 35.8%，净 delta 敞口 -133 shares
Top ΔOI: P 435 +12 ｜ P 415 +4
仓位参考: Max Pain 440 ｜ Call Wall 450（+3.8%）（OI 0.1k） ｜ Put Wall 435（+0.4%）（OI 35）
量化解读： 存量 Call 重｜ATM IV 35.8%｜历史 Rank 82%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 133 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 46.5% vs 11-27 36.5%（差 +10.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/ISRG_morning.json