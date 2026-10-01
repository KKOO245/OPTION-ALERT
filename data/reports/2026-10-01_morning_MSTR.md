# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.36 ｜ QQQ $737.43
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.7（fear）
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
🔴 **事件差分**: 10-02（1D）ATM IV 82.6% vs 10-09 64.4%（差 +18.1pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 162P ΔOI -3,487（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 153.09 → 今开 153.77（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 159.06 ｜ 低 152.84

Options: P/C成交量 0.34 | OI比 0.75 | ATM IV 82.6% | Skew -7.0pp | Term 0.80 | ExpMove ±3.9%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±3.9% ｜ 10-09（8D）±7.9% ｜ 10-16（15D）±10.7% ｜ 10-23（22D）±12.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 61,202,143 | GEX Change vs 上次快照 49,790,920 | Flip: Primary Flip: 150.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 639 / LOW 131 / INVALID 280
结构观察区: Primary Flip 150.40（全链重定价，覆盖 99%）
Call Wall 170（弱结构｜现价低于该位 7.6%）
最近结构参考: Flip 150（现价高于该位 4.5%）
量化视角： 正 Gamma（6120万，无历史分位）｜正 Gamma 增强（+4979万）｜现价位于 Flip 上方 4.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 180.0C — Vol 6,738 | 最新价 $0.05 | OI 6513→9319 (ΔOI +2806张) | ΔOI/Volume 41.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2806张（+43.1% vs前日OI），连续性待观察（方向未知）
10-02 155.0C — Vol 9,911 | 最新价 $2.60 | OI 1567→3938 (ΔOI +2371张) | ΔOI/Volume 23.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2371张（+151.3% vs前日OI），连续性待观察（方向未知）
10-09 160.0C — Vol 6,167 | 最新价 $3.50 | OI 4456→6594 (ΔOI +2138张) | ΔOI/Volume 34.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2138张（+48.0% vs前日OI），连续性待观察（方向未知）
10-09 170.0C — Vol 9,601 | 最新价 $1.62 | OI 1618→3460 (ΔOI +1842张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1842张（+113.8% vs前日OI），连续性待观察（方向未知）
10-02 160.0C — Vol 11,901 | 最新价 $1.20 | OI 5937→7744 (ΔOI +1807张) | ΔOI/Volume 15.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1807张（+30.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,964 张（Put 0 / Call 10,964），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +10.5k / P -6.8k ｜ Activity HIGH ｜ 1D
10-09  C +8.6k / P +5.6k ｜ Activity MEDIUM △ ｜ 8D
10-16  C +2.4k / P +1.5k ｜ Activity HIGH ｜ 15D
10-23  C -2.0k / P +2.1k ｜ Activity HIGH ｜ 22D

📆 10-02 Forward Structure
存量OI: C 251.2k / P 187.6k，今日变化ΔOI: C +10.5k / P -6.8k，平值价格ATM: C $3.20 / P $2.93 ｜ ATM IV 82.6%，净 delta 敞口 631k shares
Top ΔOI: P 162 -3,487 ｜ C 170 -2,721
仓位参考: Max Pain 152 ｜ Call Wall 170（+8.2%，弱）（OI 38.3k） ｜ Put Wall 150（-4.6%，弱）（OI 9.2k）
量化解读： 存量 Call 重｜ATM IV 82.6%｜历史 Rank 54%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 630,934 股

10-09（MEDIUM △）Top ΔOI: 160C +2,138 ｜ 170C +1,842
10-09（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（+1.8%，弱）（OI 6.6k） ｜ Put Wall 155（-1.4%，弱）（OI 2.2k）

📆 10-16 Forward Structure
存量OI: C 175.3k / P 145.8k，今日变化ΔOI: C +2.4k / P +1.5k，平值价格ATM: C $8.80 / P $8.00 ｜ ATM IV 64.7%，净 delta 敞口 38k shares
Top ΔOI: P 150 +746 ｜ C 160 +579
仓位参考: Max Pain 120 ｜ Call Wall 155（-1.4%，弱）（OI 10.3k） ｜ Put Wall 160（+1.8%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 64.7%｜历史 Rank 54%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,084 股

📆 10-23 Forward Structure
存量OI: C 20.6k / P 27.2k，今日变化ΔOI: C -2.0k / P +2.1k，平值价格ATM: C $10.30 / P $9.68 ｜ ATM IV 64.2%，净 delta 敞口 -134k shares
Top ΔOI: C 165 -3,140 ｜ C 160 +584 ｜ P 150 +571
仓位参考: Max Pain 160 ｜ Call Wall 165（+5.0%，弱）（OI 2.0k） ｜ Put Wall 155（-1.4%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 64.2%｜历史 Rank 54%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 133,738 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 82.6% vs 10-09 64.4%（差 +18.1pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/MSTR_morning.json