# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.91
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 78.8% vs 09-25 66.2%（差 +12.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 130C ΔOI +2,712（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 126.18 → 今开 129.88（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 133.11 ｜ 低 127.82

Options: P/C成交量 0.71 | OI比 0.59 | ATM IV 78.8% | Skew -5.7pp | Term 0.84 | ExpMove ±3.6%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.6% ｜ 09-25（8D）±8.0% ｜ 10-02（15D）±11.0% ｜ 10-09（22D）±12.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 50,064,257 | GEX Change vs 上次快照 43,874,306 | Flip: Primary Flip: 124.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 808 / LOW 114 / INVALID 276
结构观察区: Primary Flip 124.06（全链重定价，覆盖 98%）
最近结构参考: Flip 124（现价高于该位 4.0%）
量化视角： 正 Gamma（5006万，无历史分位）｜正 Gamma 增强（+4387万）｜现价位于 Flip 上方 4.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 124（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 115.0P — Vol 4,731 | 最新价 $1.48 | OI 1703→5575 (ΔOI +3872张) | ΔOI/Volume 81.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3872张（+227.4% vs前日OI），连续性待观察（方向未知）
09-18 130.0C — Vol 9,154 | 最新价 $1.58 | OI 8912→11624 (ΔOI +2712张) | ΔOI/Volume 29.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2712张（+30.4% vs前日OI），连续性待观察（方向未知）
09-25 132.0C — Vol 2,996 | 最新价 $3.10 | OI 300→2458 (ΔOI +2158张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2158张（+719.3% vs前日OI），连续性待观察（方向未知）
09-18 150.0C — Vol 6,162 | 最新价 $0.03 | OI 16503→18329 (ΔOI +1826张) | ΔOI/Volume 29.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1826张（+11.1% vs前日OI），连续性待观察（方向未知）
10-16 180.0C — Vol 2,324 | 最新价 $0.85 | OI 9299→10894 (ΔOI +1595张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1595张（+17.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,163 张（Put 3,872 / Call 8,291），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +8.3k / P -14.6k ｜ Activity HIGH ｜ 1D
09-25  C +6.9k / P +7.6k ｜ Activity HIGH ｜ 8D
10-02  C +1.8k / P +3.3k ｜ Activity HIGH ｜ 15D
10-09  C +0.3k / P +3.1k ｜ Activity MEDIUM △ ｜ 22D

📆 09-18 Forward Structure
存量OI: C 484.0k / P 283.2k，今日变化ΔOI: C +8.3k / P -14.6k，平值价格ATM: C $1.93 / P $2.75 ｜ ATM IV 78.8%，净 delta 敞口 844k shares
Top ΔOI: P 120 -6,241 ｜ C 130 +2,712 ｜ C 135 -2,599
仓位参考: Max Pain 120 ｜ Call Wall 140（+8.5%，弱）（OI 24.9k） ｜ Put Wall 125（-3.1%，弱）（OI 9.7k）
量化解读： 存量 Call 重｜ATM IV 78.8%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 843,733 股

📆 09-25 Forward Structure
存量OI: C 39.1k / P 64.8k，今日变化ΔOI: C +6.9k / P +7.6k，平值价格ATM: C $4.88 / P $5.41 ｜ ATM IV 66.2%，净 delta 敞口 115k shares
Top ΔOI: P 115 +3,872 ｜ C 132 +2,158
仓位参考: Max Pain 127 ｜ Call Wall 132（+2.3%，弱）（OI 2.5k） ｜ Put Wall 120（-7.0%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 66.2%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 115,206 股

📆 10-02 Forward Structure
存量OI: C 26.5k / P 44.3k，今日变化ΔOI: C +1.8k / P +3.3k，平值价格ATM: C $8.20 / P $6.00 ｜ ATM IV 66.3%，净 delta 敞口 39k shares
仓位参考: Max Pain 130 ｜ Call Wall 140（+8.5%，弱）（OI 1.1k） ｜ Put Wall 130（+0.7%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 66.3%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,796 股

10-09（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 140（+8.5%，弱）（OI 1.2k） ｜ Put Wall 130（+0.7%，弱）（OI 2.5k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 78.8% vs 09-25 66.2%（差 +12.6pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/MSTR_morning.json