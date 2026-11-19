# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $714.27 ｜ QQQ $645.04
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 10C ΔOI +38（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 9.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 10.35 → 今开 10.66（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 10.86 ｜ 低 10.37

Options: P/C成交量 0.35 | OI比 0.28 | ATM IV 103.5% | Skew -5.9pp | Term 0.86 | ExpMove ±6.6%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.28）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.28×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±6.6% ｜ 11-27（8D）±11.9% ｜ 12-04（15D）±20.7% ｜ 12-11（22D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,047,828 | GEX Change vs 上次快照 282,140 | Flip: Candidates 9.13 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 74%（带内） ｜ IV 有效性: VALID 126 / LOW 73 / INVALID 167
结构观察区: ≈9（全链重定价，覆盖 74%，CONDITIONAL）
Put Wall 10（弱结构｜现价高于该位 5.4%）
最近结构参考: Put Wall 10（现价高于该位 5.4%）
量化视角： 正 Gamma（105万，无历史分位）｜正 Gamma 增强（+28万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 74%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 10.0P — Vol 81 | 最新价 $0.55 | OI 15→93 (ΔOI +78张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增78张（+520.0% vs前日OI），连续性待观察（方向未知）
11-20 12.0C — Vol 63 | 最新价 $0.05 | OI 894→949 (ΔOI +55张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55张（+6.2% vs前日OI），连续性待观察（方向未知）
11-20 10.5C — Vol 61 | 最新价 $0.30 | OI 65→103 (ΔOI +38张) | ΔOI/Volume 62.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38张（+58.5% vs前日OI），连续性待观察（方向未知）
11-20 11.0C — Vol 128 | 最新价 $0.12 | OI 284→321 (ΔOI +37张) | ΔOI/Volume 28.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增37张（+13.0% vs前日OI），值得跟踪（方向未知）
11-27 9.0P — Vol 26 | 最新价 $0.12 | OI 8→34 (ΔOI +26张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26张（+325.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 234 张（Put 104 / Call 130），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +0.2k / P -88 ｜ Activity MEDIUM △ ｜ 1D
11-27  C +23 / P +26 ｜ Activity MEDIUM △ ｜ 8D
12-04  C +12 / P +87 ｜ Activity HIGH ｜ 15D
12-11  C +4 / P +2 ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 7.2k / P 2.0k，今日变化ΔOI: C +0.2k / P -88，平值价格ATM: C $0.30 / P $0.40 ｜ ATM IV 103.5%，净 delta 敞口 18k shares
Top ΔOI: C 10 +38
仓位参考: Max Pain 12 ｜ Call Wall 11.5（+9.1%，弱）（OI 0.4k） ｜ Put Wall 10（-5.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 103.5%｜历史 Rank 50%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,838 股

11-27（MEDIUM △）Top ΔOI: 11C +13
11-27（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 10（-5.1%，弱）（OI 0.1k）

📆 12-04 Forward Structure
存量OI: C 0.6k / P 0.5k，今日变化ΔOI: C +12 / P +87，平值价格ATM: C $1.25 / P $0.93 ｜ ATM IV 84.4%，净 delta 敞口 -4k shares
Top ΔOI: P 10 +78
仓位参考: Max Pain 12 ｜ Call Wall 11（+4.4%，弱）（OI 65） ｜ Put Wall 9.5（-9.9%）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 84.4%｜历史 Rank 50%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,553 股

12-11（MEDIUM △）Top ΔOI: 11P +2
12-11（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 11（+4.4%，弱）（OI 41） ｜ Put Wall 11（+4.4%，弱）（OI 15）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/NNE_morning.json