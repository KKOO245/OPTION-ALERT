# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $768.68 ｜ QQQ $719.90
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,371.12 → 今开 1,336.96（-2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 1381.53 ｜ 低 1330.51

Options: P/C成交量 0.83 | OI比 0.86 | ATM IV 77.8% | Skew 3.4pp | Term 0.94 | ExpMove ±6.0%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 3.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±6.0% ｜ 10-30（10D）±12.2% ｜ 11-06（17D）±15.1% ｜ 11-13（24D）±14.8%
   ⇒ IV–VIX Spread: +59.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,863,770 | GEX Change vs 上次快照 -14,062 | Flip: Primary Flip: 1401.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1985 / LOW 423 / INVALID 1046
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1401.99（全链重定价，覆盖 100%）
最近结构参考: Flip 1402（现价低于该位 2.8%）
量化视角： 负 Gamma（286万，无历史分位）｜负 Gamma 加深（1万）｜现价位于 Flip 下方 2.77%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,445（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1402（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 1500.0C — Vol 5,967 | 最新价 $8.00 | OI 2237→2941 (ΔOI +704张) | ΔOI/Volume 11.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增704张（+31.5% vs前日OI），连续性待观察（方向未知）
10-23 1450.0C — Vol 2,573 | 最新价 $16.32 | OI 584→1132 (ΔOI +548张) | ΔOI/Volume 21.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增548张（+93.8% vs前日OI），连续性待观察（方向未知）
10-23 1200.0P — Vol 1,699 | 最新价 $3.30 | OI 551→1092 (ΔOI +541张) | ΔOI/Volume 31.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增541张（+98.2% vs前日OI），连续性待观察（方向未知）
10-23 1550.0C — Vol 3,009 | 最新价 $3.85 | OI 1387→1898 (ΔOI +511张) | ΔOI/Volume 17.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增511张（+36.8% vs前日OI），连续性待观察（方向未知）
10-30 2860.0C — Vol 454 | 最新价 $0.20 | OI 902→1337 (ΔOI +435张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增435张（+48.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,739 张（Put 541 / Call 2,198），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +7.3k / P +4.0k ｜ Activity HIGH ｜ 3D
10-30  C +2.3k / P +1.2k ｜ Activity MEDIUM △ ｜ 10D
11-06  C +0.7k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
11-13  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 43.4k / P 37.3k，今日变化ΔOI: C +7.3k / P +4.0k，平值价格ATM: C $41.68 / P $39.80 ｜ ATM IV 77.8%，净 delta 敞口 56k shares
Top ΔOI: C 1500 +704 ｜ C 1450 +548 ｜ P 1200 +541
仓位参考: Max Pain 1,445 ｜ Call Wall 1450（+6.4%，弱）（OI 1.1k） ｜ Put Wall 1250（-8.3%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 77.8%｜历史 Rank 36%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 56,353 股

10-30（MEDIUM △）Top ΔOI: 1400C +384 ｜ 1450C +298
10-30（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Call Wall 1400（+2.7%，弱）（OI 0.6k） ｜ Put Wall 1350（-1.0%，弱）（OI 0.7k）

11-06（MEDIUM △）Top ΔOI: 1465C +101
11-06（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Call Wall 1400（+2.7%，弱）（OI 0.6k） ｜ Put Wall 1400（+2.7%，弱）（OI 0.4k）

11-13（MEDIUM △）Top ΔOI: 1830C +65 ｜ 1535C +41
11-13（MEDIUM △）仓位参考: Max Pain 1,510 ｜ Call Wall 1480（+8.6%，弱）（OI 0.2k） ｜ Put Wall 1300（-4.6%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=59 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=59）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SNDK_morning.json