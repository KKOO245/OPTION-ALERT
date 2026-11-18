# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.20 ｜ QQQ $659.58
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 26.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 82.8% vs 11-27 61.1%（差 +21.7pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 162C ΔOI +1,725（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 156.56 → 今开 158.25（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 158.44 ｜ 低 154.37

Options: P/C成交量 0.22 | OI比 0.84 | ATM IV 82.8% | Skew 9.2pp | Term 0.69 | ExpMove ±5.1%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 9.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.22×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±5.1% ｜ 11-27（9D）±7.8% ｜ 12-04（16D）±10.5% ｜ 12-11（23D）±11.8%
   ⇒ IV–VIX Spread: +58.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,149,990 | GEX Change vs 上次快照 8,301,984 | Flip: Primary Flip: 160.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 434 / LOW 179 / INVALID 185
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 160.11（全链重定价，覆盖 96%）
最近结构参考: Flip 160（现价低于该位 2.1%）
量化视角： 负 Gamma（1415万，无历史分位）｜负 Gamma 缓解（+830万）｜现价位于 Flip 下方 2.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 165.0C — Vol 7,016 | 最新价 $1.68 | OI 9428→11456 (ΔOI +2028张) | ΔOI/Volume 28.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2028张（+21.5% vs前日OI），连续性待观察（方向未知）
12-18 175.0C — Vol 3,347 | 最新价 $3.73 | OI 3197→5046 (ΔOI +1849张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1849张（+57.8% vs前日OI），连续性待观察（方向未知）
11-20 162.5C — Vol 4,668 | 最新价 $2.38 | OI 649→2374 (ΔOI +1725张) | ΔOI/Volume 37.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1725张（+265.8% vs前日OI），连续性待观察（方向未知）
11-27 167.5C — Vol 1,922 | 最新价 $2.39 | OI 157→1716 (ΔOI +1559张) | ΔOI/Volume 81.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1559张（+993.0% vs前日OI），连续性待观察（方向未知）
11-27 135.0P — Vol 2,606 | 最新价 $1.05 | OI 1675→3228 (ΔOI +1553张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1553张（+92.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,714 张（Put 1,553 / Call 7,161），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +2.3k / P +2.3k ｜ Activity HIGH ｜ 2D
11-27  C +5.1k / P +2.1k ｜ Activity HIGH ｜ 9D
12-04  C +0.5k / P +0.9k ｜ Activity MEDIUM △ ｜ 16D
12-11  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 243.1k / P 205.0k，今日变化ΔOI: C +2.3k / P +2.3k，平值价格ATM: C $3.79 / P $4.26 ｜ ATM IV 82.8%，净 delta 敞口 220k shares
Top ΔOI: C 165 +2,028 ｜ C 162 +1,725
仓位参考: Max Pain 170 ｜ Call Wall 165（+5.2%，弱）（OI 11.5k） ｜ Put Wall 155（-1.1%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 82.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 219,568 股

📆 11-27 Forward Structure
存量OI: C 28.0k / P 37.7k，今日变化ΔOI: C +5.1k / P +2.1k，平值价格ATM: C $6.00 / P $6.15 ｜ ATM IV 61.1%，净 delta 敞口 152k shares
Top ΔOI: C 167 +1,559 ｜ P 135 +1,553 ｜ P 150 -1,322
仓位参考: Max Pain 168 ｜ Call Wall 167.5（+6.8%，弱）（OI 1.7k） ｜ Put Wall 150（-4.3%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 61.1%｜历史 Rank 92%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 151,617 股

12-04（MEDIUM △）Top ΔOI: 155P +522 ｜ 152P +424
12-04（MEDIUM △）仓位参考: Max Pain 170 ｜ Put Wall 155（-1.1%）（OI 2.8k）

12-11（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 170（+8.4%，弱）（OI 0.5k） ｜ Put Wall 150（-4.3%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 82.8% vs 11-27 61.1%（差 +21.7pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/PLTR_morning.json