# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.43
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **期限 OI 集中**: 11-13 35C ΔOI +506 占该期限总 OI 11.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 39.05 → 今开 39.58（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 39.85 ｜ 低 39.34

Options: P/C成交量 0.50 | OI比 0.88 | ATM IV 70.0% | Skew 1.3pp | Term 0.91 | ExpMove ±4.0%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.91）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±4.0% ｜ 10-30（9D）±8.9% ｜ 11-06（16D）±11.2% ｜ 11-13（23D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,970,643 | GEX Change vs 上次快照 1,236,780 | Flip: Primary Flip: 40.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 340 / LOW 79 / INVALID 105
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 40.89（全链重定价，覆盖 99%）
Put Wall 40（弱结构｜现价低于该位 1.0%）
最近结构参考: Put Wall 40（现价低于该位 1.0%）
量化视角： 负 Gamma（197万，无历史分位）｜负 Gamma 缓解（+124万）｜现价位于 Flip 下方 3.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 41（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 46.0C — Vol 1,092 | 最新价 $0.89 | OI 18→594 (ΔOI +576张) | ΔOI/Volume 52.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增576张（+3200.0% vs前日OI），连续性待观察（方向未知）
11-13 35.0C — Vol 1,010 | 最新价 $5.23 | OI 3→509 (ΔOI +506张) | ΔOI/Volume 50.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增506张（+16866.7% vs前日OI），连续性待观察（方向未知）
11-20 45.0C — Vol 379 | 最新价 $1.09 | OI 789→1078 (ΔOI +289张) | ΔOI/Volume 76.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增289张（+36.6% vs前日OI），连续性待观察（方向未知）
10-23 41.0C — Vol 228 | 最新价 $0.31 | OI 253→423 (ΔOI +170张) | ΔOI/Volume 74.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增170张（+67.2% vs前日OI），连续性待观察（方向未知）
11-20 38.0C — Vol 300 | 最新价 $3.90 | OI 0→150 (ΔOI +150张) | ΔOI/Volume 50.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增150张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,691 张（Put 0 / Call 1,691），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.5k / P -25 ｜ Activity MEDIUM △ ｜ 2D
10-30  C +0.2k / P +0.1k ｜ Activity LOW ｜ 9D
11-06  C +0.3k / P +49 ｜ Activity HIGH ｜ 16D
11-13  C +0.6k / P +75 ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 9.6k / P 8.4k，今日变化ΔOI: C +0.5k / P -25，平值价格ATM: C $0.85 / P $0.75 ｜ ATM IV 70.0%，净 delta 敞口 38k shares
Top ΔOI: C 41 +170 ｜ P 39 +133 ｜ C 41 +97
仓位参考: Max Pain 42 ｜ Call Wall 42（+6.0%，弱）（OI 1.0k） ｜ Put Wall 36.5（-7.9%）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 70.0%｜历史 Rank 56%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 37,614 股

10-30（Activity LOW）仓位参考: Max Pain 44 ｜ Put Wall 42（+6.0%，弱）（OI 0.7k）

📆 11-06 Forward Structure
存量OI: C 5.7k / P 3.7k，今日变化ΔOI: C +0.3k / P +49，平值价格ATM: C $1.90 / P $2.54 ｜ ATM IV 71.3%，净 delta 敞口 777 shares
仓位参考: Max Pain 43 ｜ Call Wall 43（+8.5%，弱）（OI 0.9k） ｜ Put Wall 38（-4.1%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 71.3%｜历史 Rank 56%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 正 777 股

📆 11-13 Forward Structure
存量OI: C 2.6k / P 1.9k，今日变化ΔOI: C +0.6k / P +75，平值价格ATM: C $2.61 / P $2.84 ｜ ATM IV 73.2%，净 delta 敞口 43k shares
Top ΔOI: C 35 +506 ｜ P 37 +77
仓位参考: Max Pain 42 ｜ Put Wall 39（-1.6%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 73.2%｜历史 Rank 56%（近端代理）｜IV/RV 1.55×（近似）｜净 delta 敞口 正 43,390 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/MP_morning.json