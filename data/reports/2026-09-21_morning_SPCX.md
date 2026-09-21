# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $773.06 ｜ QQQ $741.47
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 160C ΔOI +4,754（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 152.71 → 今开 154.77（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 156.40 ｜ 低 153.23

Options: P/C成交量 0.51 | OI比 1.10 | ATM IV 55.2% | Skew -4.4pp | Term 0.90 | ExpMove ±4.8%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -4.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±4.8% ｜ 10-02（11D）±7.2% ｜ 10-09（18D）±9.0% ｜ 10-16（25D）±10.4%
   ⇒ IV–VIX Spread: +40.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 34,776,004 | GEX Change vs 上次快照 19,388,222 | Flip: Primary Flip: 151.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 590 / LOW 71 / INVALID 329
结构观察区: Primary Flip 151.21（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 2.7%）
最近结构参考: Call Wall 160（现价低于该位 2.7%）
量化视角： 正 Gamma（3478万，无历史分位）｜正 Gamma 增强（+1939万）｜现价位于 Flip 上方 3.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 135.0P — Vol 22,295 | 最新价 $1.90 | OI 44263→64225 (ΔOI +19962张) | ΔOI/Volume 89.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19962张（+45.1% vs前日OI），连续性待观察（方向未知）
09-25 170.0C — Vol 26,222 | 最新价 $0.32 | OI 6699→22147 (ΔOI +15448张) | ΔOI/Volume 58.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15448张（+230.6% vs前日OI），连续性待观察（方向未知）
09-25 180.0C — Vol 21,771 | 最新价 $0.08 | OI 8211→22456 (ΔOI +14245张) | ΔOI/Volume 65.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14245张（+173.5% vs前日OI），连续性待观察（方向未知）
10-16 155.0P — Vol 16,632 | 最新价 $9.25 | OI 35469→49448 (ΔOI +13979张) | ΔOI/Volume 84.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13979张（+39.4% vs前日OI），连续性待观察（方向未知）
10-02 90.0P — Vol 9,510 | 最新价 $0.03 | OI 344→9574 (ΔOI +9230张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9230张（+2683.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 72,864 张（Put 43,171 / Call 29,693），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $17M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +56.8k / P +33.1k ｜ Activity HIGH ｜ 4D
10-02  C +13.1k / P +15.4k ｜ Activity HIGH ｜ 11D
10-09  C +1.0k / P +3.9k ｜ Activity HIGH ｜ 18D
10-16  C -12.6k / P +42.8k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 156.5k / P 171.8k，今日变化ΔOI: C +56.8k / P +33.1k，平值价格ATM: C $4.07 / P $3.39 ｜ ATM IV 55.2%，净 delta 敞口 847k shares
Top ΔOI: C 170 +15,448 ｜ C 180 +14,245 ｜ C 160 +4,754
仓位参考: Max Pain 150 ｜ Call Wall 170（+9.1%，弱）（OI 22.1k） ｜ Put Wall 150（-3.7%，弱）（OI 15.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 55.2%｜历史 Rank 26%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 847,480 股

📆 10-02 Forward Structure
存量OI: C 52.6k / P 64.9k，今日变化ΔOI: C +13.1k / P +15.4k，平值价格ATM: C $6.00 / P $5.20 ｜ ATM IV 51.6%，净 delta 敞口 207k shares
Top ΔOI: C 170 +2,077 ｜ C 180 +1,764
仓位参考: Max Pain 150 ｜ Call Wall 170（+9.1%，弱）（OI 6.8k） ｜ Put Wall 150（-3.7%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 51.6%｜历史 Rank 26%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 206,812 股

📆 10-09 Forward Structure
存量OI: C 20.6k / P 23.6k，今日变化ΔOI: C +1.0k / P +3.9k，平值价格ATM: C $7.49 / P $6.50 ｜ ATM IV 50.3%，净 delta 敞口 -1k shares
Top ΔOI: C 155 +230
仓位参考: Max Pain 149 ｜ Call Wall 165（+5.9%，弱）（OI 1.9k） ｜ Put Wall 150（-3.7%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 50.3%｜历史 Rank 26%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,003 股

📆 10-16 Forward Structure
存量OI: C 295.7k / P 388.7k，今日变化ΔOI: C -12.6k / P +42.8k，平值价格ATM: C $8.70 / P $7.54 ｜ ATM IV 50.3%，净 delta 敞口 -1.1M shares
Top ΔOI: P 135 +19,962 ｜ C 200 -19,791 ｜ P 155 +13,979
仓位参考: Max Pain 150 ｜ Call Wall 160（+2.7%，弱）（OI 34.1k） ｜ Put Wall 155（-0.5%，弱）（OI 49.4k）
量化解读： 存量 Put 重｜ATM IV 50.3%｜历史 Rank 26%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 1,110,122 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SPCX_morning.json