# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $760.66 ｜ QQQ $698.94
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 155C ΔOI +1,167（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 154.14 → 今开 154.56（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 155.35 ｜ 低 145.88

Options: P/C成交量 0.42 | OI比 0.59 | ATM IV 121.7% | Skew 8.6pp | Term 0.85 | ExpMove ±10.8%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 8.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±10.8% ｜ 11-13（11D）±18.4% ｜ 11-20（18D）±21.0% ｜ 11-27（25D）±22.3%
   ⇒ IV–VIX Spread: +102.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,332,513 | GEX Change vs 上次快照 -702,828 | Flip: Primary Flip: 166.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 582 / LOW 45 / INVALID 109
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.43（全链重定价，覆盖 100%）
最近结构参考: Flip 166（现价低于该位 10.1%）
量化视角： 负 Gamma（733万，无历史分位）｜负 Gamma 加深（70万）｜现价位于 Flip 下方 10.05%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 200.0C — Vol 5,590 | 最新价 $0.47 | OI 3418→6596 (ΔOI +3178张) | ΔOI/Volume 56.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3178张（+93.0% vs前日OI），连续性待观察（方向未知）
11-13 225.0P — Vol 2,337 | 最新价 $74.01 | OI 360→2689 (ΔOI +2329张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2329张（+646.9% vs前日OI），连续性待观察（方向未知）
11-13 220.0P — Vol 2,036 | 最新价 $66.84 | OI 263→2269 (ΔOI +2006张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2006张（+762.7% vs前日OI），连续性待观察（方向未知）
11-06 185.0C — Vol 3,942 | 最新价 $1.13 | OI 1815→3695 (ΔOI +1880张) | ΔOI/Volume 47.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1880张（+103.6% vs前日OI），连续性待观察（方向未知）
11-13 230.0P — Vol 1,319 | 最新价 $77.80 | OI 134→1445 (ΔOI +1311张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1311张（+978.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,704 张（Put 5,646 / Call 5,058），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +13.0k / P +3.0k ｜ Activity HIGH ｜ 4D
11-13  C +2.1k / P +6.6k ｜ Activity HIGH ｜ 11D
11-20  C +2.6k / P +2.3k ｜ Activity MEDIUM △ ｜ 18D
11-27  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 65.4k / P 38.5k，今日变化ΔOI: C +13.0k / P +3.0k，平值价格ATM: C $7.80 / P $8.40 ｜ ATM IV 121.7%，净 delta 敞口 473k shares
Top ΔOI: C 200 +3,178 ｜ C 185 +1,880 ｜ P 225 -1,762
仓位参考: Max Pain 175 ｜ Call Wall 150（+0.2%，弱）（OI 1.7k） ｜ Put Wall 140（-6.5%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 121.7%｜历史 Rank 74%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 473,390 股

📆 11-13 Forward Structure
存量OI: C 23.2k / P 26.8k，今日变化ΔOI: C +2.1k / P +6.6k，平值价格ATM: C $13.48 / P $14.03 ｜ ATM IV 129.4%，净 delta 敞口 -491k shares
Top ΔOI: P 225 +2,329 ｜ P 220 +2,006 ｜ P 230 +1,311
仓位参考: Max Pain 200 ｜ Put Wall 150（+0.2%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 129.4%｜历史 Rank 74%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 491,361 股

11-20（MEDIUM △）Top ΔOI: 155C +1,167 ｜ 95P +725
11-20（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 155（+3.5%，弱）（OI 1.5k） ｜ Put Wall 150（+0.2%，弱）（OI 7.3k）

11-27（MEDIUM △）Top ΔOI: 185C +289
11-27（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 150（+0.2%，弱）（OI 0.5k） ｜ Put Wall 155（+3.5%）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/NBIS_morning.json