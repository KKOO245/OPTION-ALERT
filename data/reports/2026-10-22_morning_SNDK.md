# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $764.28 ｜ QQQ $704.47
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 1380P ΔOI +635（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,378.22 → 今开 1,317.26（-4.4%） | 较昨收变动（含盘初走势） ｜ 今日高 1355.00 ｜ 低 1297.10

Options: P/C成交量 0.52 | OI比 0.84 | ATM IV 83.7% | Skew 1.7pp | Term 0.88 | ExpMove ±4.0%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±4.0% ｜ 10-30（8D）±10.4% ｜ 11-06（15D）±14.4% ｜ 11-13（22D）±15.7%
   ⇒ IV–VIX Spread: +65.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,267,731 | GEX Change vs 上次快照 -3,715,914 | Flip: Primary Flip: 1389.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1865 / LOW 584 / INVALID 1037
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1389.29（全链重定价，覆盖 100%）
最近结构参考: Flip 1389（现价低于该位 2.5%）
量化视角： 负 Gamma（427万，无历史分位）｜负 Gamma 加深（372万）｜现价位于 Flip 下方 2.52%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,400（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1389（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 1380.0P — Vol 1,974 | 最新价 $32.55 | OI 353→988 (ΔOI +635张) | ΔOI/Volume 32.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增635张（+179.9% vs前日OI），连续性待观察（方向未知）
10-23 1700.0C — Vol 707 | 最新价 $0.18 | OI 1220→1753 (ΔOI +533张) | ΔOI/Volume 75.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增533张（+43.7% vs前日OI），连续性待观察（方向未知）
10-23 1500.0C — Vol 7,556 | 最新价 $3.50 | OI 3221→3683 (ΔOI +462张) | ΔOI/Volume 6.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增462张（+14.3% vs前日OI），值得跟踪（方向未知）
10-30 1800.0C — Vol 593 | 最新价 $3.90 | OI 569→1023 (ΔOI +454张) | ΔOI/Volume 76.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增454张（+79.8% vs前日OI），连续性待观察（方向未知）
10-23 1350.0P — Vol 2,614 | 最新价 $20.00 | OI 734→1155 (ΔOI +421张) | ΔOI/Volume 16.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增421张（+57.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,505 张（Put 1,056 / Call 1,449），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +3.2k / P +3.0k ｜ Activity HIGH ｜ 1D
10-30  C +2.2k / P +1.3k ｜ Activity HIGH ｜ 8D
11-06  C +0.8k / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 50.4k / P 42.2k，今日变化ΔOI: C +3.2k / P +3.0k，平值价格ATM: C $25.98 / P $27.50 ｜ ATM IV 83.7%，净 delta 敞口 -48k shares
Top ΔOI: P 1380 +635
仓位参考: Max Pain 1,400 ｜ Call Wall 1450（+7.1%，弱）（OI 1.6k） ｜ Put Wall 1250（-7.7%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 83.7%｜历史 Rank 42%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 48,390 股

📆 10-30 Forward Structure
存量OI: C 28.2k / P 18.5k，今日变化ΔOI: C +2.2k / P +1.3k，平值价格ATM: C $73.90 / P $66.70 ｜ ATM IV 91.9%，净 delta 敞口 27k shares
Top ΔOI: C 1800 +454 ｜ P 1300 +216
仓位参考: Max Pain 1,480 ｜ Call Wall 1400（+3.4%，弱）（OI 0.8k） ｜ Put Wall 1350（-0.3%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 91.9%｜历史 Rank 42%（近端代理）｜IV/RV 1.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,670 股

11-06（MEDIUM △）Top ΔOI: 1700C +99
11-06（MEDIUM △）仓位参考: Max Pain 1,495 ｜ Call Wall 1400（+3.4%，弱）（OI 0.6k） ｜ Put Wall 1400（+3.4%，弱）（OI 0.4k）

11-13（MEDIUM △）Top ΔOI: 1320C +51
11-13（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Call Wall 1480（+9.3%，弱）（OI 0.2k） ｜ Put Wall 1300（-4.0%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SNDK_morning.json