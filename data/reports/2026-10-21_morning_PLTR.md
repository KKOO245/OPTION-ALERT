# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $772.65 ｜ QQQ $726.22
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 190P ΔOI +1,095（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 192.60 → 今开 191.45（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 197.85 ｜ 低 189.88

Options: P/C成交量 0.32 | OI比 0.95 | ATM IV 57.1% | Skew 4.6pp | Term 1.12 | ExpMove ±3.6%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构正常（Term 1.12）｜保护溢价中性（Skew 4.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±3.6% ｜ 10-30（9D）±6.5% ｜ 11-06（16D）±12.5% ｜ 11-13（23D）±13.8%
   ⇒ IV–VIX Spread: +39.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 48,477,889 | GEX Change vs 上次快照 15,976,774 | Flip: Primary Flip: 187.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 662 / LOW 65 / INVALID 185
结构观察区: Primary Flip 187.01（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 3.3%） | Call Wall 200（弱结构｜现价低于该位 1.9%）
最近结构参考: Call Wall 200（现价低于该位 1.9%）
量化视角： 正 Gamma（4848万，无历史分位）｜正 Gamma 增强（+1598万）｜现价位于 Flip 上方 4.92%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构） / 190（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 187（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 185.0P — Vol 8,858 | 最新价 $1.23 | OI 4988→6766 (ΔOI +1778张) | ΔOI/Volume 20.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1778张（+35.6% vs前日OI），连续性待观察（方向未知）
10-30 160.0P — Vol 2,264 | 最新价 $0.39 | OI 1266→2795 (ΔOI +1529张) | ΔOI/Volume 67.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1529张（+120.8% vs前日OI），连续性待观察（方向未知）
10-23 212.5C — Vol 2,381 | 最新价 $0.10 | OI 2669→3866 (ΔOI +1197张) | ΔOI/Volume 50.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1197张（+44.9% vs前日OI），连续性待观察（方向未知）
10-23 190.0P — Vol 11,688 | 最新价 $2.60 | OI 6438→7533 (ΔOI +1095张) | ΔOI/Volume 9.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1095张（+17.0% vs前日OI），连续性待观察（方向未知）
11-06 145.0P — Vol 1,011 | 最新价 $0.78 | OI 1337→2239 (ΔOI +902张) | ΔOI/Volume 89.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增902张（+67.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,501 张（Put 5,304 / Call 1,197），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +4.0k / P +8.9k ｜ Activity HIGH ｜ 2D
10-30  C +2.1k / P +4.1k ｜ Activity HIGH ｜ 9D
11-06  C +1.5k / P +3.1k ｜ Activity HIGH ｜ 16D
11-13  C +0.8k / P +1.2k ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 131.6k / P 124.7k，今日变化ΔOI: C +4.0k / P +8.9k，平值价格ATM: C $4.04 / P $3.05 ｜ ATM IV 57.1%，净 delta 敞口 3k shares
Top ΔOI: P 185 +1,778 ｜ C 212 +1,197 ｜ P 190 +1,095
仓位参考: Max Pain 190 ｜ Call Wall 205（+4.5%，弱）（OI 16.9k） ｜ Put Wall 190（-3.2%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.1%｜历史 Rank 91%（近端代理）｜IV/RV 1.40×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,946 股

📆 10-30 Forward Structure
存量OI: C 50.5k / P 80.4k，今日变化ΔOI: C +2.1k / P +4.1k，平值价格ATM: C $6.97 / P $5.80 ｜ ATM IV 50.7%，净 delta 敞口 79k shares
Top ΔOI: P 190 -698 ｜ P 182 +432
仓位参考: Max Pain 190 ｜ Call Wall 200（+1.9%，弱）（OI 3.9k） ｜ Put Wall 190（-3.2%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 50.7%｜历史 Rank 91%（近端代理）｜IV/RV 1.24×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 79,299 股

📆 11-06 Forward Structure
存量OI: C 26.4k / P 27.6k，今日变化ΔOI: C +1.5k / P +3.1k，平值价格ATM: C $12.90 / P $11.70 ｜ ATM IV 75.3%，净 delta 敞口 29k shares
Top ΔOI: P 145 +902
仓位参考: Max Pain 190 ｜ Call Wall 205（+4.5%，弱）（OI 1.8k） ｜ Put Wall 190（-3.2%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜ATM IV 75.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,808 股

11-13（MEDIUM △）Top ΔOI: 240C +246
11-13（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 210（+7.0%，弱）（OI 1.1k） ｜ Put Wall 180（-8.3%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/PLTR_morning.json