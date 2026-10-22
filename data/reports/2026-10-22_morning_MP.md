# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.89
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
🟡 **近现价集中开仓**: 10-23 40C ΔOI +735（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 39.50 → 今开 38.01（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 38.96 ｜ 低 37.96

Options: P/C成交量 1.37 | OI比 0.74 | ATM IV 71.8% | Skew 0.1pp | Term 0.89 | ExpMove ±5.3%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价薄（Skew 0.1pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.74）+ 当日成交偏 Put（P/C量 1.37）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.37×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±5.3% ｜ 10-30（8D）±7.3% ｜ 11-06（15D）±13.0% ｜ 11-13（22D）±15.3%
   ⇒ IV–VIX Spread: +53.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,754,737 | GEX Change vs 上次快照 -20,525 | Flip: Primary Flip: 39.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 323 / LOW 81 / INVALID 120
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 39.62（全链重定价，覆盖 96%）
Put Wall 40（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 40（现价低于该位 2.7%）
量化视角： 负 Gamma（275万，无历史分位）｜负 Gamma 加深（2万）｜现价位于 Flip 下方 2.74%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 40（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 40.0C — Vol 836 | 最新价 $0.61 | OI 271→1006 (ΔOI +735张) | ΔOI/Volume 87.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增735张（+271.2% vs前日OI），连续性待观察（方向未知）
10-30 42.0C — Vol 462 | 最新价 $0.66 | OI 71→500 (ΔOI +429张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增429张（+604.2% vs前日OI），连续性待观察（方向未知）
10-23 41.5C — Vol 398 | 最新价 $0.24 | OI 392→755 (ΔOI +363张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增363张（+92.6% vs前日OI），连续性待观察（方向未知）
10-30 51.0C — Vol 220 | 最新价 $0.05 | OI 711→898 (ΔOI +187张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增187张（+26.3% vs前日OI），连续性待观察（方向未知）
10-23 42.5C — Vol 197 | 最新价 $0.07 | OI 257→433 (ΔOI +176张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增176张（+68.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,890 张（Put 0 / Call 1,890），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +1.2k / P -0.5k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +0.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 8D
11-06  C +0.3k / P +70 ｜ Activity MEDIUM △ ｜ 15D
11-13  C +58 / P +9 ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 10.7k / P 7.9k，今日变化ΔOI: C +1.2k / P -0.5k，平值价格ATM: C $1.40 / P $0.63 ｜ ATM IV 71.8%，净 delta 敞口 63k shares
Top ΔOI: C 40 +735 ｜ C 41 +363
仓位参考: Max Pain 40 ｜ Call Wall 42（+9.0%，弱）（OI 1.1k） ｜ Put Wall 36.5（-5.3%）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 71.8%｜历史 Rank 59%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 63,309 股

10-30（MEDIUM △）Top ΔOI: 42C +429
10-30（MEDIUM △）仓位参考: Max Pain 44 ｜ Call Wall 42（+9.0%，弱）（OI 0.5k） ｜ Put Wall 42（+9.0%，弱）（OI 0.7k）

11-06（MEDIUM △）仓位参考: Max Pain 43 ｜ Call Wall 40（+3.8%，弱）（OI 0.4k） ｜ Put Wall 38（-1.4%）（OI 0.8k）

11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 35（-9.2%，弱）（OI 0.5k） ｜ Put Wall 39（+1.2%）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/MP_morning.json