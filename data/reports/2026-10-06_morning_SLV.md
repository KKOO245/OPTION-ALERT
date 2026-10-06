# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.74 ｜ QQQ $760.84
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 56C ΔOI +2,451（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 72C ΔOI +837 占该期限总 OI 13.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 55.13 → 今开 55.30（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 55.37 ｜ 低 54.90

Options: P/C成交量 0.82 | OI比 0.48 | ATM IV 32.0% | Skew 0.9pp | Term 1.00 | ExpMove ±1.5%（近端） | Rank 47%
量化视角： IV 中性（Rank 47%）｜期限结构正常（Term 1.00）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-07（1D）±1.5% ｜ 10-09（3D）±2.4% ｜ 10-12（6D）±2.9% ｜ 10-14（8D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,889,675 | GEX Change vs 上次快照 7,354,567 | Flip: Primary Flip: 54.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 669 / LOW 135 / INVALID 474
结构观察区: Primary Flip 54.33（全链重定价，覆盖 98%）
Put Wall 60（弱结构｜现价低于该位 8.3%）
最近结构参考: Flip 54（现价高于该位 1.3%）
量化视角： 正 Gamma（2889万，无历史分位）｜正 Gamma 增强（+735万）｜现价位于 Flip 上方 1.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（MaxPain，仅结算参考）；上方 60（Put Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-07 56.0C — Vol 3,967 | 最新价 $0.18 | OI 1107→3558 (ΔOI +2451张) | ΔOI/Volume 61.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2451张（+221.4% vs前日OI），连续性待观察（方向未知）
10-30 67.0C — Vol 1,687 | 最新价 $0.11 | OI 547→2206 (ΔOI +1659张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1659张（+303.3% vs前日OI），连续性待观察（方向未知）
10-16 59.5C — Vol 1,734 | 最新价 $0.18 | OI 520→2170 (ΔOI +1650张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1650张（+317.3% vs前日OI），连续性待观察（方向未知）
10-16 51.0P — Vol 2,132 | 最新价 $0.13 | OI 3469→5101 (ΔOI +1632张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1632张（+47.0% vs前日OI），连续性待观察（方向未知）
10-09 58.0C — Vol 2,060 | 最新价 $0.07 | OI 3128→4645 (ΔOI +1517张) | ΔOI/Volume 73.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1517张（+48.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,909 张（Put 1,632 / Call 7,277），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-07  C +8.2k / P +3.0k ｜ Activity HIGH ｜ 1D
10-09  C +4.6k / P +1.7k ｜ Activity MEDIUM △ ｜ 3D
10-12  C +1.5k / P +3.1k ｜ Activity HIGH ｜ 6D
10-14  C +1.2k / P +2.1k ｜ Activity HIGH ｜ 8D

📆 10-07 Forward Structure
存量OI: C 30.5k / P 14.6k，今日变化ΔOI: C +8.2k / P +3.0k，平值价格ATM: C $0.45 / P $0.37 ｜ ATM IV 32.0%，净 delta 敞口 157k shares
Top ΔOI: C 56 +2,451 ｜ C 56 +1,309 ｜ C 57 +1,149
仓位参考: Max Pain 55 ｜ Call Wall 56（+1.7%，弱）（OI 3.6k） ｜ Put Wall 51.5（-6.4%）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 32.0%｜历史 Rank 47%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 157,024 股

10-09（MEDIUM △）Top ΔOI: 58C +1,517 ｜ 56C +847
10-09（MEDIUM △）仓位参考: Max Pain 56 ｜ Call Wall 60（+9.0%，弱）（OI 5.1k） ｜ Put Wall 55（-0.1%，弱）（OI 3.3k）

📆 10-12 Forward Structure
存量OI: C 3.7k / P 7.3k，今日变化ΔOI: C +1.5k / P +3.1k，平值价格ATM: C $0.90 / P $0.69 ｜ ATM IV 26.3%，净 delta 敞口 -39k shares
Top ΔOI: P 53 +939 ｜ P 52 +597 ｜ P 50 +519
仓位参考: Max Pain 56 ｜ Call Wall 58（+5.4%，弱）（OI 0.5k） ｜ Put Wall 54（-1.9%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 26.3%｜历史 Rank 47%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 38,541 股

📆 10-14 Forward Structure
存量OI: C 2.8k / P 3.3k，今日变化ΔOI: C +1.2k / P +2.1k，平值价格ATM: C $1.07 / P $0.89 ｜ ATM IV 29.1%，净 delta 敞口 -35k shares
Top ΔOI: P 53 +525
仓位参考: Max Pain 56 ｜ Call Wall 58（+5.4%，弱）（OI 0.4k） ｜ Put Wall 54（-1.9%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 29.1%｜历史 Rank 47%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 35,402 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SLV_morning.json