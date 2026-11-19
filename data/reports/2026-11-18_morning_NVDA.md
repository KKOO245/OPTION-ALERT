# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $735.61 ｜ QQQ $nan
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-23 150P ΔOI +1,863（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 155.46 → 今开 159.19（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 159.70 ｜ 低 153.26

Options: P/C成交量 0.77 | OI比 0.78 | ATM IV 116.2% | Skew 3.7pp | Term 0.35 | ExpMove ±0.6%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.35，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±0.6% ｜ 11-23（5D）±6.2% ｜ 11-25（7D）±7.4% ｜ 11-27（9D）±0.0%
   ⇒ IV–VIX Spread: +91.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,235,049 | GEX Change vs 上次快照 6,500,220 | Flip: Primary Flip: 156.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1128 / LOW 325 / INVALID 659
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 156.28（全链重定价，覆盖 100%）
最近结构参考: Flip 156（现价低于该位 0.9%）
量化视角： 负 Gamma（3324万，无历史分位）｜负 Gamma 缓解（+650万）｜现价位于 Flip 下方 0.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 158（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 156（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-18 100.0P — Vol 41,135 | 最新价 $0.07 | OI 4044→31274 (ΔOI +27230张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27230张（+673.3% vs前日OI），连续性待观察（方向未知）
11-20 170.0C — Vol 57,139 | 最新价 $2.51 | OI 56583→72286 (ΔOI +15703张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15703张（+27.8% vs前日OI），连续性待观察（方向未知）
11-18 185.0C — Vol 33,003 | 最新价 $0.54 | OI 9736→25339 (ΔOI +15603张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15603张（+160.3% vs前日OI），连续性待观察（方向未知）
11-18 170.0C — Vol 70,174 | 最新价 $1.77 | OI 16157→31212 (ΔOI +15055张) | ΔOI/Volume 21.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15055张（+93.2% vs前日OI），连续性待观察（方向未知）
11-18 200.0C — Vol 40,176 | 最新价 $0.26 | OI 17352→31767 (ΔOI +14415张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14415张（+83.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 88,006 张（Put 27,230 / Call 60,776），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 469.5k / P 366.7k，今日成交量: C 409.9k / P 315.0k，平值价格ATM: C $1.96 / P $1.92 ｜ ATM IV 116.2%，预期波动 ±2.5%，Max Pain 158
Top ΔOI: P 100 +27,230 ｜ C 185 +15,603 ｜ C 170 +15,055

📆 Forward Expiration Structure

11-20  C +118.6k / P +47.0k ｜ Activity HIGH ｜ 2D
11-23  C +11.1k / P +10.3k ｜ Activity HIGH ｜ 5D
11-25  C +5.5k / P +3.7k ｜ Activity HIGH ｜ 7D
11-27  C +27.7k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 11-20 Forward Structure
存量OI: C 1572.1k / P 1012.1k，今日变化ΔOI: C +118.6k / P +47.0k，平值价格ATM: C $0.49 / P $0.40 ｜ ATM IV 42.2%，净 delta 敞口 4.6M shares
Top ΔOI: C 170 +15,703 ｜ C 185 +12,841 ｜ P 135 +12,036
仓位参考: Max Pain 180 ｜ Call Wall 170（+9.7%，弱）（OI 72.3k） ｜ Put Wall 150（-3.2%，弱）（OI 51.0k）
量化解读： 存量 Call 重｜ATM IV 42.2%｜历史 Rank 98%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,591,381 股

📆 11-23 Forward Structure
存量OI: C 55.2k / P 34.6k，今日变化ΔOI: C +11.1k / P +10.3k，平值价格ATM: C $4.83 / P $4.80 ｜ ATM IV 64.1%，净 delta 敞口 120k shares
Top ΔOI: P 135 +2,004 ｜ P 150 +1,863 ｜ P 140 +1,429
仓位参考: Max Pain 160 ｜ Call Wall 160（+3.3%，弱）（OI 4.2k） ｜ Put Wall 150（-3.2%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 64.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 119,615 股

📆 11-25 Forward Structure
存量OI: C 31.7k / P 12.3k，今日变化ΔOI: C +5.5k / P +3.7k，平值价格ATM: C $5.80 / P $5.65 ｜ ATM IV 65.2%，净 delta 敞口 35k shares
Top ΔOI: C 165 -533
仓位参考: Max Pain 158 ｜ Call Wall 165（+6.5%，弱）（OI 2.6k） ｜ Put Wall 140（-9.6%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 65.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,318 股

📆 11-27 Forward Structure
存量OI: C 225.3k / P 163.8k，今日变化ΔOI: C +27.7k / P +0.5k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 35.2%，净 delta 敞口 675k shares
Top ΔOI: C 185 +8,028 ｜ P 145 -5,553 ｜ C 182 -3,797
仓位参考: Max Pain 178 ｜ Call Wall 170（+9.7%，弱）（OI 7.7k） ｜ Put Wall 165（+6.5%，弱）（OI 12.7k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 98%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 正 674,824 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/NVDA_morning.json