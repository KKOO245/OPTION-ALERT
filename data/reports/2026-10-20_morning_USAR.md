# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $768.68 ｜ QQQ $719.95
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


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.09 → 今开 9.87（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 10.24 ｜ 低 9.72

Options: P/C成交量 0.48 | OI比 0.30 | ATM IV 87.9% | Skew 4.3pp | Term 1.00 | ExpMove ±6.5%（近端） | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构正常（Term 1.00）｜保护溢价中性（Skew 4.3pp）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±6.5% ｜ 10-30（10D）±10.8% ｜ 11-06（17D）±15.7% ｜ 11-13（24D）±18.7%
   ⇒ IV–VIX Spread: +69.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -411,074 | GEX Change vs 上次快照 670,107 | Flip: Primary Flip: 9.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 239 / LOW 87 / INVALID 110
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.99（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价低于该位 1.2%）
最近结构参考: Flip 10（现价低于该位 1.1%）
量化视角： 负 Gamma（41万，无历史分位）｜负 Gamma 缓解（+67万）｜现价位于 Flip 下方 1.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 11（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 11.5C — Vol 2,686 | 最新价 $0.15 | OI 202→2598 (ΔOI +2396张) | ΔOI/Volume 89.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2396张（+1186.1% vs前日OI），连续性待观察（方向未知）
10-30 12.0C — Vol 2,481 | 最新价 $0.09 | OI 311→2527 (ΔOI +2216张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2216张（+712.5% vs前日OI），连续性待观察（方向未知）
10-30 11.0C — Vol 2,403 | 最新价 $0.26 | OI 394→2534 (ΔOI +2140张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2140张（+543.1% vs前日OI），连续性待观察（方向未知）
10-23 10.5C — Vol 1,547 | 最新价 $0.20 | OI 699→1522 (ΔOI +823张) | ΔOI/Volume 53.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增823张（+117.7% vs前日OI），连续性待观察（方向未知）
10-23 11.0C — Vol 1,770 | 最新价 $0.09 | OI 1147→1841 (ΔOI +694张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增694张（+60.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,269 张（Put 0 / Call 8,269），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.5k / P -0.2k ｜ Activity MEDIUM △ ｜ 3D
10-30  C +7.1k / P -0.4k ｜ Activity HIGH ｜ 10D
11-06  C +0.3k / P -0.5k ｜ Activity MEDIUM △ ｜ 17D
11-13  C +0.2k / P -37 ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 21.1k / P 6.3k，今日变化ΔOI: C +2.5k / P -0.2k，平值价格ATM: C $0.28 / P $0.36 ｜ ATM IV 87.9%，净 delta 敞口 112k shares
Top ΔOI: C 10 +823
仓位参考: Max Pain 11 ｜ Call Wall 10.5（+6.2%，弱）（OI 1.5k） ｜ Put Wall 9.5（-3.9%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 87.9%｜历史 Rank 19%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 111,949 股

📆 10-30 Forward Structure
存量OI: C 17.3k / P 8.9k，今日变化ΔOI: C +7.1k / P -0.4k，平值价格ATM: C $0.49 / P $0.58 ｜ ATM IV 79.8%，净 delta 敞口 187k shares
仓位参考: Max Pain 12 ｜ Put Wall 9（-9.0%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 79.8%｜历史 Rank 19%（近端代理）｜IV/RV 1.45×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 187,083 股

11-06（MEDIUM △）Top ΔOI: 17P -341
11-06（MEDIUM △）仓位参考: Max Pain 13 ｜ Put Wall 9（-9.0%）（OI 1.5k）

11-13（MEDIUM △）仓位参考: Max Pain 15 ｜ Call Wall 10.5（+6.2%，弱）（OI 0.2k） ｜ Put Wall 10.5（+6.2%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 87.9% vs 10-30 79.8%（差 +8.2pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=59 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=59）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/USAR_morning.json