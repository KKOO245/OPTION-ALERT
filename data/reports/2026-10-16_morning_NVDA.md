# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 225C ΔOI +7,388（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 217.23 → 今开 216.56（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 216.94 ｜ 低 215.07

Options: P/C成交量 0.63 | OI比 0.85 | ATM IV 46.7% | Skew 2.8pp | Term 0.72 | ExpMove ±2.0%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.0% ｜ 10-21（5D）±3.0% ｜ 10-23（7D）±3.8% ｜ 10-26（10D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 140,982,816 | GEX Change vs 上次快照 124,869,887 | Flip: Primary Flip: 213.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 719 / LOW 191 / INVALID 572
结构观察区: Primary Flip 213.63（全链重定价，覆盖 91%）
最近结构参考: Flip 214（现价高于该位 1.3%）
量化视角： 正 Gamma（1.41亿，无历史分位）｜正 Gamma 增强（+1.25亿）｜现价位于 Flip 上方 1.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 218（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 214（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 260.0C — Vol 74,417 | 最新价 $0.79 | OI 29605→97741 (ΔOI +68136张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增68136张（+230.2% vs前日OI），连续性待观察（方向未知）
11-20 190.0P — Vol 72,845 | 最新价 $2.29 | OI 29705→89689 (ΔOI +59984张) | ΔOI/Volume 82.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增59984张（+201.9% vs前日OI），连续性待观察（方向未知）
11-20 230.0C — Vol 81,149 | 最新价 $5.75 | OI 63859→98507 (ΔOI +34648张) | ΔOI/Volume 42.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34648张（+54.3% vs前日OI），连续性待观察（方向未知）
11-20 295.0C — Vol 70,291 | 最新价 $0.14 | OI 71672→89611 (ΔOI +17939张) | ΔOI/Volume 25.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17939张（+25.0% vs前日OI），连续性待观察（方向未知）
10-23 225.0C — Vol 34,028 | 最新价 $1.78 | OI 10379→26565 (ΔOI +16186张) | ΔOI/Volume 47.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16186张（+155.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 196,893 张（Put 59,984 / Call 136,909），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 1035.9k / P 881.6k，今日成交量: C 137.6k / P 87.3k，平值价格ATM: C $0.71 / P $1.58 ｜ ATM IV 46.7%，预期波动 ±1.1%，Max Pain 218
Top ΔOI: C 180 -29,403 ｜ C 237 -18,794 ｜ C 222 +10,528

📆 Forward Expiration Structure

10-19  C +26.0k / P +11.9k ｜ Activity HIGH ｜ 3D
10-21  C +11.1k / P +9.1k ｜ Activity HIGH ｜ 5D
10-23  C +44.9k / P +32.1k ｜ Activity HIGH ｜ 7D
10-26  C +2.9k / P +3.8k ｜ Activity HIGH ｜ 10D

📆 10-19 Forward Structure
存量OI: C 84.1k / P 48.4k，今日变化ΔOI: C +26.0k / P +11.9k，平值价格ATM: C $1.76 / P $2.62 ｜ ATM IV 26.3%，净 delta 敞口 915k shares
Top ΔOI: C 225 +7,388 ｜ C 220 +5,185 ｜ P 210 +3,350
仓位参考: Max Pain 220 ｜ Call Wall 225（+4.0%，弱）（OI 12.0k） ｜ Put Wall 215（-0.7%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 26.3%｜历史 Rank 63%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 915,251 股

📆 10-21 Forward Structure
存量OI: C 39.2k / P 26.1k，今日变化ΔOI: C +11.1k / P +9.1k，平值价格ATM: C $2.79 / P $3.75 ｜ ATM IV 31.5%，净 delta 敞口 246k shares
Top ΔOI: C 222 +3,148 ｜ P 200 +2,935
仓位参考: Max Pain 220 ｜ Call Wall 230（+6.3%，弱）（OI 5.6k） ｜ Put Wall 220（+1.6%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 31.5%｜历史 Rank 63%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 246,010 股

📆 10-23 Forward Structure
存量OI: C 237.1k / P 187.3k，今日变化ΔOI: C +44.9k / P +32.1k，平值价格ATM: C $3.72 / P $4.40 ｜ ATM IV 33.0%，净 delta 敞口 911k shares
Top ΔOI: C 225 +16,186 ｜ C 220 +9,348 ｜ C 230 +5,523
仓位参考: Max Pain 222 ｜ Call Wall 225（+4.0%，弱）（OI 26.6k） ｜ Put Wall 220（+1.6%，弱）（OI 14.4k）
量化解读： 存量 Call 重｜ATM IV 33.0%｜历史 Rank 63%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 910,720 股

📆 10-26 Forward Structure
存量OI: C 17.3k / P 5.9k，今日变化ΔOI: C +2.9k / P +3.8k，平值价格ATM: C $4.16 / P $5.04 ｜ ATM IV 31.5%，净 delta 敞口 6k shares
Top ΔOI: P 200 +1,570 ｜ C 225 +1,246 ｜ P 215 +735
仓位参考: Max Pain 220 ｜ Call Wall 237.5（+9.7%）（OI 9.1k） ｜ Put Wall 200（-7.6%）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.5%｜历史 Rank 63%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 6,377 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/NVDA_morning.json