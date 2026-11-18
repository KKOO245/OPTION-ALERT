# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.20 ｜ QQQ $659.46
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 26.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 119.8% vs 11-27 94.4%（差 +25.4pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 96.50 → 今开 95.02（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 95.51 ｜ 低 91.20

Options: P/C成交量 0.32 | OI比 0.58 | ATM IV 119.8% | Skew 10.2pp | Term 0.74 | ExpMove ±7.5%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 10.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±7.5% ｜ 11-27（9D）±12.1% ｜ 12-04（16D）±15.1% ｜ 12-11（23D）±18.0%
   ⇒ IV–VIX Spread: +95.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,867,863 | GEX Change vs 上次快照 4,243,407 | Flip: Primary Flip: 102.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 518 / LOW 217 / INVALID 399
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 102.68（全链重定价，覆盖 99%）
Put Wall 90（弱结构｜现价高于该位 5.3%）
最近结构参考: Put Wall 90（现价高于该位 5.3%）
量化视角： 负 Gamma（3387万，无历史分位）｜负 Gamma 缓解（+424万）｜现价位于 Flip 下方 7.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 110（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 103（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 87.0P — Vol 4,530 | 最新价 $2.46 | OI 0→4426 (ΔOI +4426张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4426张（前日OI缺失），连续性待观察（方向未知）
11-27 93.0P — Vol 4,454 | 最新价 $4.15 | OI 0→4410 (ΔOI +4410张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4410张（前日OI缺失），连续性待观察（方向未知）
11-20 100.0C — Vol 8,607 | 最新价 $2.53 | OI 1202→5023 (ΔOI +3821张) | ΔOI/Volume 44.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3821张（+317.9% vs前日OI），连续性待观察（方向未知）
12-18 40.0P — Vol 3,293 | 最新价 $0.48 | OI 1699→3836 (ΔOI +2137张) | ΔOI/Volume 64.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2137张（+125.8% vs前日OI），连续性待观察（方向未知）
12-18 200.0C — Vol 2,154 | 最新价 $0.14 | OI 13604→15621 (ΔOI +2017张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2017张（+14.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,811 张（Put 10,973 / Call 5,838），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -11.3k / P -8.0k ｜ Activity HIGH ｜ 2D
11-27  C +6.4k / P +13.6k ｜ Activity MEDIUM △ ｜ 9D
12-04  C +3.3k / P +2.6k ｜ Activity HIGH ｜ 16D
12-11  C +0.3k / P +4.2k ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 325.3k / P 188.1k，今日变化ΔOI: C -11.3k / P -8.0k，平值价格ATM: C $3.29 / P $3.85 ｜ ATM IV 119.8%，净 delta 敞口 1.2M shares
仓位参考: Max Pain 110 ｜ Put Wall 90（-5.0%，弱）（OI 14.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 119.8%｜历史 Rank 90%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,195,440 股

11-27（MEDIUM △）Top ΔOI: 87P +4,426 ｜ 93P +4,410
11-27（MEDIUM △）仓位参考: Max Pain 112 ｜ Put Wall 90（-5.0%，弱）（OI 14.8k）

📆 12-04 Forward Structure
存量OI: C 20.6k / P 49.9k，今日变化ΔOI: C +3.3k / P +2.6k，平值价格ATM: C $7.25 / P $7.10 ｜ ATM IV 91.2%，净 delta 敞口 272k shares
Top ΔOI: P 160 -1,567 ｜ C 107 +775
仓位参考: Max Pain 135 ｜ Put Wall 90（-5.0%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 91.2%｜历史 Rank 90%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 272,412 股

12-11（MEDIUM △）Top ΔOI: 65P +791 ｜ 60P +709
12-11（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 100（+5.5%，弱）（OI 0.2k） ｜ Put Wall 100（+5.5%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 119.8% vs 11-27 94.4%（差 +25.4pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/MSTR_morning.json