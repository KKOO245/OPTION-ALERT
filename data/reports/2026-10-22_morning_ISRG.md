# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.84
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 455C ΔOI +126（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 428.12 → 今开 430.67（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 439.87 ｜ 低 427.47

Options: P/C成交量 0.45 | OI比 0.98 | ATM IV 51.8% | Skew 7.9pp | Term 0.63 | ExpMove ±2.4%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 7.9pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.4% ｜ 10-30（8D）±5.3% ｜ 11-06（15D）±5.2% ｜ 11-13（22D）±6.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,664,871 | GEX Change vs 上次快照 2,185,605 | Flip: Primary Flip: 422.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 290 / LOW 192 / INVALID 484
结构观察区: Primary Flip 422.34（全链重定价，覆盖 87%）
Call Wall 475（弱结构｜现价低于该位 8.6%）
最近结构参考: Flip 422（现价高于该位 2.8%）
量化视角： 正 Gamma（366万，无历史分位）｜正 Gamma 增强（+219万）｜现价位于 Flip 上方 2.83%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 425（MaxPain，仅结算参考）；上方 475（Call Wall，弱结构）。
• Gamma 区域：切换参考 422（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 440.0C — Vol 588 | 最新价 $1.80 | OI 233→433 (ΔOI +200张) | ΔOI/Volume 34.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增200张（+85.8% vs前日OI），连续性待观察（方向未知）
10-23 460.0C — Vol 263 | 最新价 $0.10 | OI 535→677 (ΔOI +142张) | ΔOI/Volume 54.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增142张（+26.5% vs前日OI），连续性待观察（方向未知）
10-23 455.0C — Vol 218 | 最新价 $0.30 | OI 155→281 (ΔOI +126张) | ΔOI/Volume 57.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增126张（+81.3% vs前日OI），连续性待观察（方向未知）
11-06 430.0C — Vol 147 | 最新价 $10.10 | OI 16→137 (ΔOI +121张) | ΔOI/Volume 82.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增121张（+756.2% vs前日OI），连续性待观察（方向未知）
11-06 440.0C — Vol 144 | 最新价 $6.80 | OI 11→119 (ΔOI +108张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增108张（+981.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 697 张（Put 0 / Call 697），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.1k / P -0.1k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 8D
11-06  C +0.3k / P +48 ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 8.7k / P 8.5k，今日变化ΔOI: C +0.1k / P -0.1k，平值价格ATM: C $3.20 / P $7.30 ｜ ATM IV 51.8%，净 delta 敞口 14k shares
Top ΔOI: C 440 +200 ｜ C 460 +142 ｜ C 455 +126
仓位参考: Max Pain 425 ｜ Call Wall 475（+9.4%）（OI 1.2k） ｜ Put Wall 400（-7.9%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 51.8%｜历史 Rank 80%（近端代理）｜IV/RV 2.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,572 股

10-30（MEDIUM △）Top ΔOI: 470C -86 ｜ 440C +54
10-30（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 450（+3.6%，弱）（OI 0.2k） ｜ Put Wall 397.5（-8.5%，弱）（OI 0.1k）

11-06（MEDIUM △）Top ΔOI: 430C +121 ｜ 440C +108
11-06（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 430（-1.0%，弱）（OI 0.1k） ｜ Put Wall 400（-7.9%，弱）（OI 77）

11-13（MEDIUM △）Top ΔOI: 435C +86 ｜ 440C +53
11-13（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 435（+0.2%）（OI 0.1k） ｜ Put Wall 420（-3.3%，弱）（OI 76）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/ISRG_morning.json