# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.55 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 195C ΔOI +6,306（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 189.40 → 今开 191.00（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 194.56 ｜ 低 190.25

Options: P/C成交量 0.23 | OI比 0.62 | ATM IV 46.5% | Skew 2.0pp | Term 1.24 | ExpMove ±3.5%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常偏陡（Term 1.24）｜保护溢价薄（Skew 2.0pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±3.5% ｜ 10-16（10D）±5.7% ｜ 10-23（17D）±7.2% ｜ 10-30（24D）±8.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 78,087,748 | GEX Change vs 上次快照 34,408,049 | Flip: Primary Flip: 180.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 575 / LOW 66 / INVALID 171
结构观察区: Primary Flip 180.68（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 3.3%）
最近结构参考: Call Wall 200（现价低于该位 3.3%）
量化视角： 正 Gamma（7809万，无历史分位）｜正 Gamma 增强（+3441万）｜现价位于 Flip 上方 7.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 205.0C — Vol 13,628 | 最新价 $0.23 | OI 10212→20461 (ΔOI +10249张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10249张（+100.4% vs前日OI），连续性待观察（方向未知）
10-09 195.0C — Vol 14,701 | 最新价 $1.43 | OI 11635→17941 (ΔOI +6306张) | ΔOI/Volume 42.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6306张（+54.2% vs前日OI），连续性待观察（方向未知）
10-09 202.5C — Vol 10,367 | 最新价 $0.35 | OI 10221→13035 (ΔOI +2814张) | ΔOI/Volume 27.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2814张（+27.5% vs前日OI），连续性待观察（方向未知）
10-09 200.0C — Vol 9,242 | 最新价 $0.55 | OI 9320→11060 (ΔOI +1740张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1740张（+18.7% vs前日OI），连续性待观察（方向未知）
10-16 192.5C — Vol 3,436 | 最新价 $4.13 | OI 1282→2411 (ΔOI +1129张) | ΔOI/Volume 32.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1129张（+88.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,238 张（Put 0 / Call 22,238），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +26.4k / P +7.5k ｜ Activity HIGH ｜ 3D
10-16  C -2.1k / P +4.2k ｜ Activity HIGH ｜ 10D
10-23  C +1.4k / P +1.9k ｜ Activity HIGH ｜ 17D
10-30  C +1.4k / P +1.3k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 117.1k / P 72.7k，今日变化ΔOI: C +26.4k / P +7.5k，平值价格ATM: C $3.37 / P $3.40 ｜ ATM IV 46.6%，净 delta 敞口 441k shares
Top ΔOI: C 205 +10,249 ｜ C 195 +6,306 ｜ C 202 +2,814
仓位参考: Max Pain 188 ｜ Call Wall 205（+6.0%，弱）（OI 20.5k） ｜ Put Wall 185（-4.4%，弱）（OI 7.0k）
量化解读： 存量 Call 重｜ATM IV 46.6%｜历史 Rank 28%（近端代理）｜IV/RV 2.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 440,672 股

📆 10-16 Forward Structure
存量OI: C 155.3k / P 192.1k，今日变化ΔOI: C -2.1k / P +4.2k，平值价格ATM: C $5.61 / P $5.45 ｜ ATM IV 42.5%，净 delta 敞口 -481k shares
Top ΔOI: C 170 -6,445 ｜ C 192 +1,129 ｜ C 182 +1,061
仓位参考: Max Pain 170 ｜ Call Wall 200（+3.4%）（OI 16.4k） ｜ Put Wall 175（-9.5%，弱）（OI 9.0k）
量化解读： 存量 Put 重｜ATM IV 42.5%｜历史 Rank 28%（近端代理）｜IV/RV 1.89×（近似）｜净 delta 敞口 负 481,127 股

📆 10-23 Forward Structure
存量OI: C 23.7k / P 18.1k，今日变化ΔOI: C +1.4k / P +1.9k，平值价格ATM: C $7.35 / P $6.55 ｜ ATM IV 42.4%，净 delta 敞口 34k shares
Top ΔOI: C 192 +609 ｜ P 175 +301
仓位参考: Max Pain 180 ｜ Call Wall 180（-6.9%）（OI 4.6k） ｜ Put Wall 175（-9.5%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.4%｜历史 Rank 28%（近端代理）｜IV/RV 1.88×（近似）｜净 delta 敞口 正 33,801 股

10-30（MEDIUM △）Top ΔOI: 185C +471 ｜ 187P +296
10-30（MEDIUM △）仓位参考: Max Pain 182 ｜ Call Wall 192.5（-0.5%，弱）（OI 2.7k） ｜ Put Wall 180（-6.9%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/PLTR_morning.json