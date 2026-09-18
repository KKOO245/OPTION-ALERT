# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 42.2% vs 09-21 31.7%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-21 58P ΔOI +2,021（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-21 58P ΔOI +2,021 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 57.05 → 今开 59.04（+3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 59.74 ｜ 低 58.94

Options: P/C成交量 0.70 | OI比 0.45 | ATM IV 42.2% | Skew -0.5pp | Term 0.94 | ExpMove ±2.0%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.45）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.0% ｜ 09-21（4D）±2.9% ｜ 09-23（6D）±3.8% ｜ 09-25（8D）±4.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 111,046,499 | GEX Change vs 上次快照 99,553,201 | Flip: Primary Flip: 57.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 909 / LOW 224 / INVALID 383
结构观察区: Primary Flip 57.70（全链重定价，覆盖 94%）
最近结构参考: Flip 58（现价高于该位 2.8%）
量化视角： 正 Gamma（1.11亿，无历史分位）｜正 Gamma 增强（+9955万）｜现价位于 Flip 上方 2.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 58（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 58（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 60.0C — Vol 10,232 | 最新价 $1.69 | OI 40399→44636 (ΔOI +4237张) | ΔOI/Volume 41.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4237张（+10.5% vs前日OI），连续性待观察（方向未知）
09-18 56.0P — Vol 6,275 | 最新价 $0.46 | OI 11164→13262 (ΔOI +2098张) | ΔOI/Volume 33.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2098张（+18.8% vs前日OI），连续性待观察（方向未知）
10-16 50.0P — Vol 2,687 | 最新价 $0.45 | OI 18987→21038 (ΔOI +2051张) | ΔOI/Volume 76.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2051张（+10.8% vs前日OI），连续性待观察（方向未知）
09-21 58.0P — Vol 2,155 | 最新价 $1.63 | OI 177→2198 (ΔOI +2021张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2021张（+1141.8% vs前日OI），连续性待观察（方向未知）
09-21 57.0P — Vol 1,887 | 最新价 $1.05 | OI 409→1863 (ΔOI +1454张) | ΔOI/Volume 77.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1454张（+355.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,861 张（Put 7,624 / Call 4,237），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -1.9k / P -24.2k ｜ Activity MEDIUM △ ｜ 1D
09-21  C +2.8k / P +5.1k ｜ Activity HIGH ｜ 4D
09-23  C +0.8k / P +2.3k ｜ Activity HIGH ｜ 6D
09-25  C +4.2k / P +4.1k ｜ Activity HIGH ｜ 8D

📆 09-18 Forward Structure
存量OI: C 976.1k / P 443.5k，今日变化ΔOI: C -1.9k / P -24.2k，平值价格ATM: C $0.49 / P $0.70 ｜ ATM IV 42.2%，净 delta 敞口 2.3M shares
Top ΔOI: C 63 -6,726 ｜ P 70 -6,725 ｜ P 75 -3,262
仓位参考: Max Pain 58 ｜ Call Wall 65（+9.6%，弱）（OI 46.6k） ｜ Put Wall 55（-7.3%，弱）（OI 22.1k）
量化解读： 存量 Call 重｜ATM IV 42.2%｜历史 Rank 70%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,261,410 股

📆 09-21 Forward Structure
存量OI: C 10.9k / P 8.9k，今日变化ΔOI: C +2.8k / P +5.1k，平值价格ATM: C $0.75 / P $0.95 ｜ ATM IV 31.7%，净 delta 敞口 59k shares
Top ΔOI: P 58 +2,021 ｜ P 57 +1,454 ｜ C 61 +1,069
仓位参考: Max Pain 57 ｜ Call Wall 57（-3.9%）（OI 3.4k） ｜ Put Wall 58（-2.2%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.7%｜历史 Rank 70%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 59,092 股

📆 09-23 Forward Structure
存量OI: C 3.7k / P 7.4k，今日变化ΔOI: C +0.8k / P +2.3k，平值价格ATM: C $1.01 / P $1.22 ｜ ATM IV 35.9%，净 delta 敞口 -3k shares
Top ΔOI: P 54 +1,130 ｜ P 55 +197 ｜ P 58 +193
仓位参考: Max Pain 59 ｜ Call Wall 61.5（+3.7%，弱）（OI 0.5k） ｜ Put Wall 55（-7.3%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 35.9%｜历史 Rank 70%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 3,073 股

📆 09-25 Forward Structure
存量OI: C 92.9k / P 32.6k，今日变化ΔOI: C +4.2k / P +4.1k，平值价格ATM: C $1.23 / P $1.40 ｜ ATM IV 37.0%，净 delta 敞口 64k shares
Top ΔOI: C 60 +1,028 ｜ C 64 +941 ｜ P 55 +847
仓位参考: Max Pain 60 ｜ Put Wall 55（-7.3%）（OI 6.0k）
量化解读： 存量 Call 重｜ATM IV 37.0%｜历史 Rank 70%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 63,852 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 42.2% vs 09-21 31.7%（差 +10.4pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SLV_morning.json