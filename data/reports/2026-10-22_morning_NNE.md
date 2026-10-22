# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $764.28 ｜ QQQ $704.47
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 13P ΔOI +149（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 13.33 → 今开 12.64（-5.2%） | 较昨收变动（含盘初走势） ｜ 今日高 13.01 ｜ 低 12.58

Options: P/C成交量 1.05 | OI比 0.19 | ATM IV 89.8% | Skew 13.6pp | Term 0.81 | ExpMove ±5.2%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 13.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.19）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.19×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±5.2% ｜ 10-30（8D）±9.4% ｜ 11-06（15D）±14.4% ｜ 11-13（22D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 663,048 | GEX Change vs 上次快照 -455,085 | Flip: Primary Flip: 11.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 164 / LOW 90 / INVALID 148
结构观察区: Primary Flip 11.45（全链重定价，覆盖 98%）
Put Wall 14（现价低于该位 8.5%）
最近结构参考: Put Wall 14（现价低于该位 8.5%）
量化视角： 正 Gamma（66万，无历史分位）｜正 Gamma 减弱（46万）｜现价位于 Flip 上方 11.84%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 13.5P — Vol 181 | 最新价 $0.72 | OI 15→186 (ΔOI +171张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增171张（+1140.0% vs前日OI），连续性待观察（方向未知）
10-23 14.0C — Vol 244 | 最新价 $0.10 | OI 525→678 (ΔOI +153张) | ΔOI/Volume 62.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增153张（+29.1% vs前日OI），连续性待观察（方向未知）
10-30 13.0P — Vol 191 | 最新价 $0.45 | OI 78→227 (ΔOI +149张) | ΔOI/Volume 78.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增149张（+191.0% vs前日OI），连续性待观察（方向未知）
10-30 13.5C — Vol 118 | 最新价 $0.51 | OI 99→186 (ΔOI +87张) | ΔOI/Volume 73.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增87张（+87.9% vs前日OI），连续性待观察（方向未知）
11-20 17.0C — Vol 95 | 最新价 $0.20 | OI 428→498 (ΔOI +70张) | ΔOI/Volume 73.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增70张（+16.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 630 张（Put 320 / Call 310），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.2k / P -0.2k ｜ Activity HIGH ｜ 1D
10-30  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 8D
11-06  C +41 / P +5 ｜ Activity MEDIUM △ ｜ 15D
11-13  C +15 / P +3 ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 7.0k / P 1.4k，今日变化ΔOI: C +0.2k / P -0.2k，平值价格ATM: C $0.50 / P $0.17 ｜ ATM IV 89.8%，净 delta 敞口 27k shares
Top ΔOI: C 14 +153 ｜ P 14 -85
仓位参考: Max Pain 14 ｜ Put Wall 14（+9.3%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 89.8%｜历史 Rank 23%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,981 股

📆 10-30 Forward Structure
存量OI: C 7.1k / P 1.4k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $0.75 / P $0.45 ｜ ATM IV 74.1%，净 delta 敞口 -7k shares
Top ΔOI: P 13 +171 ｜ P 13 +149 ｜ C 13 +87
仓位参考: Max Pain 14 ｜ Put Wall 14（+9.3%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.1%｜历史 Rank 23%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 7,471 股

11-06（MEDIUM △）Top ΔOI: 12P +5
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（+1.5%，弱）（OI 77）

11-13（MEDIUM △）Top ΔOI: 12P +5 ｜ 13P -5
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+5.4%，弱）（OI 51） ｜ Put Wall 12.5（-2.4%，弱）（OI 66）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/NNE_morning.json