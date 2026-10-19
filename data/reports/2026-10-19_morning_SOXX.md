# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.30
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 515C ΔOI +886（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 360P ΔOI +13,001 占该期限总 OI 15.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 493.39 → 今开 511.30（+3.6%） | 较昨收变动（含盘初走势） ｜ 今日高 511.30 ｜ 低 501.58

Options: P/C成交量 0.63 | OI比 1.93 | ATM IV 49.5% | Skew 1.4pp | Term 0.82 | ExpMove ±4.5%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价薄（Skew 1.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.93×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±4.5% ｜ 10-30（11D）±5.9% ｜ 11-06（18D）±4.2% ｜ 11-13（25D）±4.8%
   ⇒ IV–VIX Spread: +31.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -30,055,569 | GEX Change vs 上次快照 -3,455,324 | Flip: Primary Flip: 560.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 582 / LOW 230 / INVALID 704
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 560.96（全链重定价，覆盖 98%）
Put Wall 480（弱结构｜现价高于该位 4.6%）
最近结构参考: Put Wall 480（现价高于该位 4.6%）
量化视角： 负 Gamma（3006万，无历史分位）｜负 Gamma 加深（346万）｜现价位于 Flip 下方 10.48%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 480（Put Wall，弱结构）；上方 522（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 561（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 360.0P — Vol 13,003 | 最新价 $0.40 | OI 9→13010 (ΔOI +13001张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13001张（+144455.6% vs前日OI），连续性待观察（方向未知）
10-30 480.0P — Vol 6,985 | 最新价 $11.60 | OI 6970→13557 (ΔOI +6587张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6587张（+94.5% vs前日OI），连续性待观察（方向未知）
10-30 520.0C — Vol 3,839 | 最新价 $7.60 | OI 80→3632 (ΔOI +3552张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3552张（+4440.0% vs前日OI），连续性待观察（方向未知）
10-30 450.0P — Vol 6,579 | 最新价 $4.40 | OI 4711→7493 (ΔOI +2782张) | ΔOI/Volume 42.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2782张（+59.0% vs前日OI），连续性待观察（方向未知）
11-20 400.0P — Vol 2,425 | 最新价 $3.20 | OI 920→2879 (ΔOI +1959张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1959张（+212.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,881 张（Put 24,329 / Call 3,552），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.8k / P +3.2k ｜ Activity HIGH ｜ 4D
10-30  C +4.4k / P +22.5k ｜ Activity HIGH ｜ 11D
11-06  C +1.0k / P +1.6k ｜ Activity HIGH ｜ 18D
11-13  C +31 / P +73 ｜ Activity LOW ｜ 25D

📆 10-23 Forward Structure
存量OI: C 9.7k / P 18.7k，今日变化ΔOI: C +2.8k / P +3.2k，平值价格ATM: C $13.70 / P $9.00 ｜ ATM IV 49.5%，净 delta 敞口 42k shares
Top ΔOI: C 515 +886 ｜ P 480 +694 ｜ C 512 +534
仓位参考: Max Pain 522 ｜ Call Wall 500（-0.4%，弱）（OI 1.4k） ｜ Put Wall 510（+1.6%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 49.5%｜历史 Rank 86%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,339 股

📆 10-30 Forward Structure
存量OI: C 19.2k / P 67.5k，今日变化ΔOI: C +4.4k / P +22.5k，平值价格ATM: C $17.20 / P $12.60 ｜ ATM IV 43.3%，净 delta 敞口 -55k shares
Top ΔOI: P 360 +13,001 ｜ P 480 +6,587 ｜ C 520 +3,552
仓位参考: Max Pain 540 ｜ Call Wall 520（+3.5%，弱）（OI 3.6k） ｜ Put Wall 480（-4.4%，弱）（OI 13.6k）
量化解读： 存量 Put 重｜ATM IV 43.3%｜历史 Rank 86%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 54,524 股

📆 11-06 Forward Structure
存量OI: C 3.9k / P 4.1k，今日变化ΔOI: C +1.0k / P +1.6k，平值价格ATM: C $0.00 / P $21.32 ｜ ATM IV 42.5%，净 delta 敞口 -5k shares
Top ΔOI: C 537 +905 ｜ P 470 +891 ｜ P 450 +430
仓位参考: Max Pain 538 ｜ Put Wall 470（-6.4%）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 42.5%｜历史 Rank 86%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,958 股

11-13（Activity LOW）仓位参考: Max Pain 560 ｜ Put Wall 490（-2.4%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 49.5% vs 10-30 43.3%（差 +6.2pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SOXX_morning.json