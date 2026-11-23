# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.39 ｜ QQQ $651.03
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 40.3）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 33.95 → 今开 36.42（+7.3%） | 较昨收变动（含盘初走势） ｜ 今日高 36.51 ｜ 低 34.27

Options: P/C成交量 N/A | OI比 0.51 | ATM IV N/A | Skew N/A | Term N/A | ExpMove ±8.7%（近端） | Rank — (历史不足)
量化视角： 存量 OI 比 0.51——观察点，非方向信号
   ⇒ Put/Call Volume: 数据不足 → 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±8.7% ｜ 12-04（11D）±7.9% ｜ 12-11（18D）±0.0% ｜ 12-18（25D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 40.29 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 0%（带内） ｜ IV 有效性: VALID 0 / LOW 0 / INVALID 498
结构观察区: ≈40（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
Put Wall 35（弱结构｜现价低于该位 1.3%）
最近结构参考: Put Wall 35（现价低于该位 1.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 35（Put Wall，弱结构） / 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 40（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 30.0P — Vol 2,299 | 最新价 $1.27 | OI 2311→3483 (ΔOI +1172张) | ΔOI/Volume 51.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1172张（+50.7% vs前日OI），连续性待观察（方向未知）
12-18 25.0P — Vol 2,505 | 最新价 $0.33 | OI 444→1511 (ΔOI +1067张) | ΔOI/Volume 42.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1067张（+240.3% vs前日OI），连续性待观察（方向未知）
11-27 30.0P — Vol 624 | 最新价 $0.32 | OI 151→513 (ΔOI +362张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增362张（+239.7% vs前日OI），连续性待观察（方向未知）
12-04 40.0C — Vol 448 | 最新价 $0.40 | OI 329→540 (ΔOI +211张) | ΔOI/Volume 47.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增211张（+64.1% vs前日OI），连续性待观察（方向未知）
12-11 42.0P — Vol 218 | 最新价 $8.05 | OI 264→472 (ΔOI +208张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增208张（+78.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,020 张（Put 2,809 / Call 211），跨 4 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.6k / P +0.7k ｜ Activity MEDIUM △ ｜ 4D
12-04  C +0.3k / P +3 ｜ Activity MEDIUM △ ｜ 11D
12-11  C +65 / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
12-18  C -12.1k / P +2.2k ｜ Activity MEDIUM △ ｜ 25D

📆 11-27 Forward Structure
存量OI: C 12.6k / P 6.5k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $1.15 / P $1.84 ｜ ATM IV 0.0%，净 delta 敞口 31k shares
Top ΔOI: C 35 +196
仓位参考: Max Pain 37 ｜ Put Wall 33（-4.4%）（OI 2.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜净 delta 敞口 正 31,221 股

12-04（MEDIUM △）Top ΔOI: 42P -121 ｜ 34C +34
12-04（MEDIUM △）仓位参考: Max Pain 36 ｜ Call Wall 35（+1.4%，弱）（OI 0.6k） ｜ Put Wall 34（-1.5%，弱）（OI 0.2k）

12-11（MEDIUM △）Top ΔOI: 42P +208
12-11（MEDIUM △）仓位参考: Max Pain 38

12-18（MEDIUM △）Top ΔOI: 45C -6,019 ｜ 40C -5,620
12-18（MEDIUM △）仓位参考: Max Pain 45 ｜ Put Wall 35（+1.4%，弱）（OI 6.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/MP_morning.json