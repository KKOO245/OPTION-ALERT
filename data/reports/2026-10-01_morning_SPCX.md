# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 150P ΔOI +4,877（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 150.86 → 今开 150.45（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 152.40 ｜ 低 150.15

Options: P/C成交量 0.57 | OI比 1.02 | ATM IV 51.6% | Skew 0.7pp | Term 0.81 | ExpMove ±2.5%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.5% ｜ 10-09（8D）±5.1% ｜ 10-16（15D）±6.9% ｜ 10-23（22D）±8.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,180,068 | GEX Change vs 上次快照 628,123 | Flip: Primary Flip: 148.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 523 / LOW 90 / INVALID 309
结构观察区: Primary Flip 148.59（全链重定价，覆盖 100%）
Call Wall 160（现价低于该位 5.2%）
最近结构参考: Flip 149（现价高于该位 2.1%）
量化视角： 正 Gamma（7418万，无历史分位）｜正 Gamma 增强（+63万）｜现价位于 Flip 上方 2.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）；上方 160（Call Wall）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 150.0P — Vol 39,656 | 最新价 $1.71 | OI 8564→13441 (ΔOI +4877张) | ΔOI/Volume 12.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4877张（+57.0% vs前日OI），连续性待观察（方向未知）
10-16 170.0C — Vol 9,931 | 最新价 $0.66 | OI 16044→19100 (ΔOI +3056张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3056张（+19.1% vs前日OI），连续性待观察（方向未知）
10-02 149.0P — Vol 11,907 | 最新价 $1.33 | OI 3389→6246 (ΔOI +2857张) | ΔOI/Volume 24.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2857张（+84.3% vs前日OI），连续性待观察（方向未知）
10-02 155.0C — Vol 52,912 | 最新价 $0.75 | OI 21464→24311 (ΔOI +2847张) | ΔOI/Volume 5.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2847张（+13.3% vs前日OI），连续性待观察（方向未知）
10-16 145.0C — Vol 684 | 最新价 $9.25 | OI 9227→11972 (ΔOI +2745张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2745张（+29.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,382 张（Put 7,734 / Call 8,648），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +5.9k / P +9.4k ｜ Activity HIGH ｜ 1D
10-09  C +7.9k / P +8.3k ｜ Activity MEDIUM △ ｜ 8D
10-16  C +9.2k / P +2.5k ｜ Activity HIGH ｜ 15D
10-23  C -12 / P +0.7k ｜ Activity HIGH ｜ 22D

📆 10-02 Forward Structure
存量OI: C 205.0k / P 208.9k，今日变化ΔOI: C +5.9k / P +9.4k，平值价格ATM: C $1.60 / P $2.13 ｜ ATM IV 51.6%，净 delta 敞口 -359k shares
Top ΔOI: P 150 +4,877 ｜ P 149 +2,857 ｜ C 155 +2,847
仓位参考: Max Pain 150 ｜ Call Wall 160（+5.5%，弱）（OI 24.9k） ｜ Put Wall 140（-7.7%，弱）（OI 18.8k）
量化解读： 存量两侧均衡｜ATM IV 51.6%｜历史 Rank 27%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 359,192 股

10-09（MEDIUM △）Top ΔOI: 152P +2,095 ｜ 150P +1,898
10-09（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（+5.5%，弱）（OI 6.7k） ｜ Put Wall 140（-7.7%，弱）（OI 3.9k）

📆 10-16 Forward Structure
存量OI: C 343.5k / P 342.7k，今日变化ΔOI: C +9.2k / P +2.5k，平值价格ATM: C $5.06 / P $5.40 ｜ ATM IV 42.0%，净 delta 敞口 308k shares
Top ΔOI: C 170 +3,056 ｜ C 145 +2,745 ｜ C 165 +1,749
仓位参考: Max Pain 143 ｜ Call Wall 160（+5.5%）（OI 42.7k） ｜ Put Wall 150（-1.1%，弱）（OI 20.5k）
量化解读： 存量两侧均衡｜ATM IV 42.0%｜历史 Rank 27%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 308,053 股

📆 10-23 Forward Structure
存量OI: C 27.5k / P 24.7k，今日变化ΔOI: C -12 / P +0.7k，平值价格ATM: C $6.21 / P $6.45 ｜ ATM IV 42.0%，净 delta 敞口 8k shares
Top ΔOI: C 170 -755 ｜ P 140 +420
仓位参考: Max Pain 148 ｜ Call Wall 150（-1.1%，弱）（OI 3.5k） ｜ Put Wall 140（-7.7%）（OI 4.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.0%｜历史 Rank 27%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 7,788 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 51.6% vs 10-09 42.0%（差 +9.6pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SPCX_morning.json