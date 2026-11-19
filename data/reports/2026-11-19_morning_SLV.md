# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $735.18 ｜ QQQ $663.98
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-23 41C ΔOI +1,320（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 46C ΔOI +8,468 占该期限总 OI 37.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 40.70 → 今开 40.79（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 41.10 ｜ 低 40.52

Options: P/C成交量 0.38 | OI比 0.21 | ATM IV 52.8% | Skew 6.9pp | Term 0.84 | ExpMove ±2.6%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价显著（Skew 6.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.21×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.6% ｜ 11-23（4D）±3.5% ｜ 11-25（6D）±4.9% ｜ 11-27（8D）±5.1%
   ⇒ IV–VIX Spread: +30.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -26,014,744 | GEX Change vs 上次快照 21,963,972 | Flip: Primary Flip: 41.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 651 / LOW 197 / INVALID 446
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 41.56（全链重定价，覆盖 96%）
Put Wall 40（现价高于该位 2.3%）
最近结构参考: Flip 42（现价低于该位 1.6%）
量化视角： 负 Gamma（2601万，无历史分位）｜负 Gamma 缓解（+2196万）｜现价位于 Flip 下方 1.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall）；上方 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 42（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-30 45.0C — Vol 14,198 | 最新价 $0.15 | OI 3045→16894 (ΔOI +13849张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13849张（+454.8% vs前日OI），连续性待观察（方向未知）
11-25 46.5C — Vol 8,630 | 最新价 $0.04 | OI 158→8626 (ΔOI +8468张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8468张（+5359.5% vs前日OI），连续性待观察（方向未知）
12-11 45.5C — Vol 4,547 | 最新价 $0.45 | OI 267→4632 (ΔOI +4365张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4365张（+1634.8% vs前日OI），连续性待观察（方向未知）
11-20 40.0P — Vol 10,318 | 最新价 $0.37 | OI 15088→19195 (ΔOI +4107张) | ΔOI/Volume 39.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4107张（+27.2% vs前日OI），连续性待观察（方向未知）
11-20 41.0C — Vol 9,412 | 最新价 $0.50 | OI 88→4075 (ΔOI +3987张) | ΔOI/Volume 42.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3987张（+4530.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 34,776 张（Put 4,107 / Call 30,669），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +7.4k / P -26.2k ｜ Activity HIGH ｜ 1D
11-23  C +3.7k / P +1.6k ｜ Activity HIGH ｜ 4D
11-25  C +10.6k / P +3.8k ｜ Activity HIGH ｜ 6D
11-27  C +18.8k / P -65 ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 608.1k / P 128.8k，今日变化ΔOI: C +7.4k / P -26.2k，平值价格ATM: C $0.53 / P $0.55 ｜ ATM IV 52.8%，净 delta 敞口 3.8M shares
Top ΔOI: P 49 -10,339 ｜ P 50 -6,683 ｜ P 48 -4,492
仓位参考: Max Pain 45 ｜ Put Wall 40（-2.2%，弱）（OI 19.2k）
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 86%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,767,373 股

📆 11-23 Forward Structure
存量OI: C 19.6k / P 6.5k，今日变化ΔOI: C +3.7k / P +1.6k，平值价格ATM: C $0.71 / P $0.71 ｜ ATM IV 40.8%，净 delta 敞口 128k shares
Top ΔOI: C 41 +1,320 ｜ C 41 +1,156 ｜ P 40 +850
仓位参考: Max Pain 42 ｜ Call Wall 41（+0.2%，弱）（OI 1.4k） ｜ Put Wall 40（-2.2%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 86%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 128,265 股

📆 11-25 Forward Structure
存量OI: C 15.6k / P 7.1k，今日变化ΔOI: C +10.6k / P +3.8k，平值价格ATM: C $1.00 / P $1.00 ｜ ATM IV 44.7%，净 delta 敞口 4k shares
Top ΔOI: P 39 +2,452
仓位参考: Max Pain 42 ｜ Put Wall 39（-4.7%）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 44.7%｜历史 Rank 86%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,733 股

📆 11-27 Forward Structure
存量OI: C 87.9k / P 30.6k，今日变化ΔOI: C +18.8k / P -65，平值价格ATM: C $1.05 / P $1.02 ｜ ATM IV 43.4%，净 delta 敞口 477k shares
Top ΔOI: C 41 +2,349 ｜ C 44 +1,928
仓位参考: Max Pain 44 ｜ Call Wall 44（+7.6%，弱）（OI 3.9k） ｜ Put Wall 40（-2.2%）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 43.4%｜历史 Rank 86%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 476,693 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SLV_morning.json