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
🟡 **近现价集中开仓**: 09-25 392C ΔOI +46（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 393.33 → 今开 393.89（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 395.29 ｜ 低 391.04

Options: P/C成交量 0.51 | OI比 0.54 | ATM IV 31.0% | Skew 0.9pp | Term 1.35 | ExpMove ±3.5%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常偏陡（Term 1.35）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±3.5% ｜ 10-02（11D）±9.1% ｜ 10-09（18D）±6.4% ｜ 10-16（25D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,389,188 | GEX Change vs 上次快照 696,121 | Flip: Primary Flip: 382.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 260 / LOW 151 / INVALID 479
结构观察区: Primary Flip 382.62（全链重定价，覆盖 96%）
Call Wall 400（弱结构｜现价低于该位 1.4%）
最近结构参考: Call Wall 400（现价低于该位 1.4%）
量化视角： 正 Gamma（139万，无历史分位）｜正 Gamma 增强（+70万）｜现价位于 Flip 上方 3.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 383（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 410.0C — Vol 241 | 最新价 $4.30 | OI 23→243 (ΔOI +220张) | ΔOI/Volume 91.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增220张（+956.5% vs前日OI），连续性待观察（方向未知）
10-02 415.0C — Vol 148 | 最新价 $3.05 | OI 48→187 (ΔOI +139张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+289.6% vs前日OI），连续性待观察（方向未知）
10-16 430.0C — Vol 170 | 最新价 $3.80 | OI 135→243 (ΔOI +108张) | ΔOI/Volume 63.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增108张（+80.0% vs前日OI），连续性待观察（方向未知）
10-16 420.0C — Vol 117 | 最新价 $5.94 | OI 414→475 (ΔOI +61张) | ΔOI/Volume 52.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增61张（+14.7% vs前日OI），连续性待观察（方向未知）
09-25 392.5C — Vol 50 | 最新价 $8.35 | OI 8→54 (ΔOI +46张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增46张（+575.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 574 张（Put 0 / Call 574），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 4D
10-02  C +0.4k / P +23 ｜ Activity HIGH ｜ 11D
10-09  C +25 / P +9 ｜ Activity MEDIUM △ ｜ 18D
10-16  C +0.3k / P -9 ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 1.9k / P 1.0k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $6.30 / P $7.55 ｜ ATM IV 31.0%，净 delta 敞口 3k shares
Top ΔOI: C 392 +46 ｜ C 395 +42 ｜ C 400 +39
仓位参考: Max Pain 375 ｜ Call Wall 430（+9.1%，弱）（OI 0.3k） ｜ Put Wall 360（-8.7%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 31.0%｜历史 Rank 10%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,935 股

📆 10-02 Forward Structure
存量OI: C 1.0k / P 2.9k，今日变化ΔOI: C +0.4k / P +23，平值价格ATM: C $9.72 / P $26.18 ｜ ATM IV 31.6%，净 delta 敞口 10k shares
Top ΔOI: C 410 +220 ｜ C 415 +139 ｜ C 420 +17
仓位参考: Max Pain 365 ｜ Call Wall 410（+4.0%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.6%｜历史 Rank 10%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,276 股

10-09（MEDIUM △）Top ΔOI: 390C +18 ｜ 395C +5
10-09（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 380（-3.6%）（OI 0.1k） ｜ Put Wall 385（-2.4%）（OI 0.2k）

10-16（MEDIUM △）Top ΔOI: 430C +108 ｜ 420C +61
10-16（MEDIUM △）仓位参考: Max Pain 385 ｜ Call Wall 400（+1.5%，弱）（OI 0.5k） ｜ Put Wall 380（-3.6%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/ISRG_morning.json