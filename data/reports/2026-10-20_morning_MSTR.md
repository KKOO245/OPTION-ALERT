# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.68 ｜ QQQ $718.03
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 145C ΔOI +5,930（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 136.02 → 今开 133.76（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 142.65 ｜ 低 133.60

Options: P/C成交量 0.46 | OI比 0.76 | ATM IV 79.2% | Skew 0.3pp | Term 0.88 | ExpMove ±6.0%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 0.3pp）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±6.0% ｜ 10-30（10D）±10.4% ｜ 11-06（17D）±13.5% ｜ 11-13（24D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,069,755 | GEX Change vs 上次快照 14,645,883 | Flip: Primary Flip: 132.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 570 / LOW 91 / INVALID 243
结构观察区: Primary Flip 132.42（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 2.5%）
最近结构参考: Call Wall 135（现价高于该位 2.5%）
量化视角： 正 Gamma（3107万，无历史分位）｜正 Gamma 增强（+1465万）｜现价位于 Flip 上方 4.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 150.0C — Vol 11,574 | 最新价 $0.62 | OI 7386→13708 (ΔOI +6322张) | ΔOI/Volume 54.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6322张（+85.6% vs前日OI），连续性待观察（方向未知）
10-23 145.0C — Vol 12,010 | 最新价 $1.31 | OI 6198→12128 (ΔOI +5930张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5930张（+95.7% vs前日OI），连续性待观察（方向未知）
10-30 115.0P — Vol 4,264 | 最新价 $1.04 | OI 5015→9062 (ΔOI +4047张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4047张（+80.7% vs前日OI），连续性待观察（方向未知）
10-23 141.0C — Vol 4,712 | 最新价 $2.30 | OI 10774→13012 (ΔOI +2238张) | ΔOI/Volume 47.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2238张（+20.8% vs前日OI），连续性待观察（方向未知）
10-30 100.0P — Vol 1,918 | 最新价 $0.39 | OI 2188→3842 (ΔOI +1654张) | ΔOI/Volume 86.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1654张（+75.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,191 张（Put 5,701 / Call 14,490），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +21.6k / P +3.7k ｜ Activity HIGH ｜ 3D
10-30  C +2.5k / P +8.1k ｜ Activity HIGH ｜ 10D
11-06  C +1.3k / P +3.3k ｜ Activity MEDIUM △ ｜ 17D
11-13  C +1.5k / P +3.6k ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 230.3k / P 174.5k，今日变化ΔOI: C +21.6k / P +3.7k，平值价格ATM: C $4.65 / P $3.60 ｜ ATM IV 79.2%，净 delta 敞口 575k shares
Top ΔOI: C 150 +6,322 ｜ C 145 +5,930 ｜ C 141 +2,238
仓位参考: Max Pain 141 ｜ Call Wall 148（+6.9%，弱）（OI 24.3k） ｜ Put Wall 140（+1.2%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 79.2%｜历史 Rank 49%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 575,141 股

📆 10-30 Forward Structure
存量OI: C 47.1k / P 78.1k，今日变化ΔOI: C +2.5k / P +8.1k，平值价格ATM: C $7.55 / P $6.81 ｜ ATM IV 75.2%，净 delta 敞口 41k shares
Top ΔOI: P 115 +4,047 ｜ P 125 -1,011
仓位参考: Max Pain 155 ｜ Call Wall 150（+8.4%，弱）（OI 1.1k） ｜ Put Wall 125（-9.7%，弱）（OI 11.2k）
量化解读： 存量 Put 重｜ATM IV 75.2%｜历史 Rank 49%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 40,738 股

11-06（MEDIUM △）Top ΔOI: 105P +666
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（+8.4%，弱）（OI 2.3k）

11-13（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 144（+4.0%，弱）（OI 0.7k） ｜ Put Wall 150（+8.4%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/MSTR_morning.json