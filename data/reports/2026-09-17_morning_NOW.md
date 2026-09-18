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
🟡 **近现价集中开仓**: 09-18 140C ΔOI -417（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 139.82 → 今开 139.07（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 140.54 ｜ 低 136.00

Options: P/C成交量 0.46 | OI比 0.98 | ATM IV 62.0% | Skew -1.6pp | Term 0.85 | ExpMove ±2.8%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.8% ｜ 09-25（8D）±6.5% ｜ 10-02（15D）±8.7% ｜ 10-09（22D）±10.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,854,525 | GEX Change vs 上次快照 951,118 | Flip: Primary Flip: 127.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 588 / LOW 94 / INVALID 132
结构观察区: Primary Flip 127.59（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 7.0%）
最近结构参考: Call Wall 150（现价低于该位 7.0%）
量化视角： 正 Gamma（2285万，无历史分位）｜正 Gamma 增强（+95万）｜现价位于 Flip 上方 9.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 122（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 128（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 129.0P — Vol 932 | 最新价 $0.16 | OI 1062→1629 (ΔOI +567张) | ΔOI/Volume 60.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增567张（+53.4% vs前日OI），连续性待观察（方向未知）
09-18 141.0C — Vol 914 | 最新价 $2.00 | OI 826→1220 (ΔOI +394张) | ΔOI/Volume 43.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增394张（+47.7% vs前日OI），连续性待观察（方向未知）
09-18 143.0C — Vol 874 | 最新价 $1.30 | OI 802→1067 (ΔOI +265张) | ΔOI/Volume 30.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增265张（+33.0% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 581 | 最新价 $2.51 | OI 2257→2427 (ΔOI +170张) | ΔOI/Volume 29.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增170张（+7.5% vs前日OI），连续性待观察（方向未知）
09-25 130.0P — Vol 277 | 最新价 $1.33 | OI 724→883 (ΔOI +159张) | ΔOI/Volume 57.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增159张（+22.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,555 张（Put 726 / Call 829），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 1D
09-25  C +0.4k / P +0.8k ｜ Activity MEDIUM △ ｜ 8D
10-02  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
10-09  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 22D

📆 09-18 Forward Structure
存量OI: C 114.0k / P 112.2k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $2.35 / P $1.50 ｜ ATM IV 62.0%，净 delta 敞口 17k shares
Top ΔOI: P 129 +567 ｜ C 140 -417 ｜ C 141 +394
仓位参考: Max Pain 122 ｜ Call Wall 150（+7.6%，弱）（OI 7.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.0%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,676 股

09-25（MEDIUM △）Top ΔOI: 130P +159 ｜ 150C +115
09-25（MEDIUM △）仓位参考: Max Pain 136 ｜ Call Wall 145（+4.0%，弱）（OI 2.4k） ｜ Put Wall 130（-6.8%，弱）（OI 0.9k）

10-02（MEDIUM △）Top ΔOI: 138C +87 ｜ 139C +69
10-02（MEDIUM △）仓位参考: Max Pain 132 ｜ Call Wall 150（+7.6%）（OI 1.8k） ｜ Put Wall 130（-6.8%，弱）（OI 0.7k）

📆 10-09 Forward Structure
存量OI: C 2.8k / P 4.0k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $7.75 / P $6.45 ｜ ATM IV 53.1%，净 delta 敞口 4k shares
Top ΔOI: C 142 +45 ｜ P 127 +38 ｜ P 142 +30
仓位参考: Max Pain 140 ｜ Call Wall 150（+7.6%，弱）（OI 0.2k） ｜ Put Wall 140（+0.4%）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.1%｜历史 Rank 54%（近端代理）｜净 delta 敞口 正 4,042 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 62.0% vs 09-25 53.7%（差 +8.3pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/NOW_morning.json