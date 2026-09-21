# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $773.06 ｜ QQQ $741.47
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 1800C ΔOI +877（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 900C ΔOI +2,050 占该期限总 OI 19.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,791.82 → 今开 1,826.66（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 1834.49 ｜ 低 1767.14

Options: P/C成交量 0.95 | OI比 1.34 | ATM IV 76.6% | Skew -5.3pp | Term 0.92 | ExpMove ±6.5%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -5.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±6.5% ｜ 10-02（11D）±10.0% ｜ 10-09（18D）±13.4% ｜ 10-16（25D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,475,138 | GEX Change vs 上次快照 697,589 | Flip: Primary Flip: 1640.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1906 / LOW 348 / INVALID 890
结构观察区: Primary Flip 1640.98（全链重定价，覆盖 100%）
Call Wall 1,600（弱结构｜现价高于该位 11.0%）
最近结构参考: Flip 1641（现价高于该位 8.2%）
量化视角： 正 Gamma（648万，无历史分位）｜正 Gamma 增强（+70万）｜现价位于 Flip 上方 8.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,650（MaxPain，仅结算参考） / 1,600（Call Wall，弱结构）。
• Gamma 区域：切换参考 1641（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 900.0C — Vol 2,050 | 最新价 $827.95 | OI 0→2050 (ΔOI +2050张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2050张（前日OI缺失），连续性待观察（方向未知）
10-02 2250.0C — Vol 1,446 | 最新价 $9.76 | OI 35→1354 (ΔOI +1319张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1319张（+3768.6% vs前日OI），连续性待观察（方向未知）
09-25 1000.0P — Vol 1,700 | 最新价 $0.30 | OI 324→1454 (ΔOI +1130张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1130张（+348.8% vs前日OI），连续性待观察（方向未知）
09-25 1800.0C — Vol 4,385 | 最新价 $60.78 | OI 890→1767 (ΔOI +877张) | ΔOI/Volume 20.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增877张（+98.5% vs前日OI），连续性待观察（方向未知）
09-25 1900.0C — Vol 2,804 | 最新价 $27.00 | OI 484→1340 (ΔOI +856张) | ΔOI/Volume 30.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增856张（+176.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,232 张（Put 1,130 / Call 5,102），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +10.0k / P +14.1k ｜ Activity HIGH ｜ 4D
10-02  C +2.8k / P +2.1k ｜ Activity MEDIUM △ ｜ 11D
10-09  C +2.4k / P +0.2k ｜ Activity HIGH ｜ 18D
10-16  C +2.2k / P +3.0k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 29.3k / P 39.1k，今日变化ΔOI: C +10.0k / P +14.1k，平值价格ATM: C $55.40 / P $60.00 ｜ ATM IV 76.6%，净 delta 敞口 112k shares
Top ΔOI: C 1800 +877 ｜ C 1900 +856
仓位参考: Max Pain 1,650 ｜ Call Wall 1800（+1.4%，弱）（OI 1.8k） ｜ Put Wall 1700（-4.3%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 76.6%｜历史 Rank 31%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 111,589 股

10-02（MEDIUM △）Top ΔOI: 2250C +1,319 ｜ 2000C +269
10-02（MEDIUM △）仓位参考: Max Pain 1,600 ｜ Call Wall 1600（-9.9%）（OI 4.4k） ｜ Put Wall 1680（-5.4%，弱）（OI 0.2k）

📆 10-09 Forward Structure
存量OI: C 5.9k / P 4.7k，今日变化ΔOI: C +2.4k / P +0.2k，平值价格ATM: C $128.00 / P $110.60 ｜ ATM IV 71.7%，净 delta 敞口 209k shares
Top ΔOI: C 900 +2,050 ｜ C 1650 +47
仓位参考: Max Pain 1,440 ｜ Put Wall 1690（-4.8%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 71.7%｜历史 Rank 31%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 208,624 股

10-16（MEDIUM △）Top ΔOI: 2500C +419 ｜ 1610P +282
10-16（MEDIUM △）仓位参考: Max Pain 1,600 ｜ Call Wall 1800（+1.4%，弱）（OI 1.0k） ｜ Put Wall 1600（-9.9%，弱）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SNDK_morning.json