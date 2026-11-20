# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 77C ΔOI +7,761（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-23 65P ΔOI +367 占该期限总 OI 12.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 74.82 → 今开 74.33（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 74.97 ｜ 低 73.80

Options: P/C成交量 0.19 | OI比 0.93 | ATM IV 59.7% | Skew 11.6pp | Term 0.77 | ExpMove ±2.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 11.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.8% ｜ 11-23（4D）±4.2% ｜ 11-25（6D）±2.1% ｜ 11-27（8D）±5.6%
   ⇒ IV–VIX Spread: +37.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -74,791,096 | GEX Change vs 上次快照 6,727,271 | Flip: Primary Flip: 79.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 567 / LOW 256 / INVALID 437
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 79.36（全链重定价，覆盖 94%）
最近结构参考: Flip 79（现价低于该位 6.3%）
量化视角： 负 Gamma（7479万，无历史分位）｜负 Gamma 缓解（+673万）｜现价位于 Flip 下方 6.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 80（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 77.0C — Vol 8,270 | 最新价 $1.33 | OI 18→7779 (ΔOI +7761张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7761张（+43116.7% vs前日OI），连续性待观察（方向未知）
11-27 80.0C — Vol 7,800 | 最新价 $0.72 | OI 102→7683 (ΔOI +7581张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7581张（+7432.4% vs前日OI），连续性待观察（方向未知）
12-18 70.0P — Vol 7,716 | 最新价 $1.80 | OI 19942→25934 (ΔOI +5992张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5992张（+30.1% vs前日OI），连续性待观察（方向未知）
12-04 70.0P — Vol 5,954 | 最新价 $1.18 | OI 431→6286 (ΔOI +5855张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5855张（+1358.5% vs前日OI），连续性待观察（方向未知）
12-18 90.0C — Vol 8,115 | 最新价 $0.41 | OI 19786→25345 (ΔOI +5559张) | ΔOI/Volume 68.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5559张（+28.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,748 张（Put 11,847 / Call 20,901），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -11.1k / P -26.3k ｜ Activity MEDIUM △ ｜ 1D
11-23  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 4D
11-25  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 6D
11-27  C +16.3k / P +0.3k ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 165.7k / P 153.8k，今日变化ΔOI: C -11.1k / P -26.3k，平值价格ATM: C $1.20 / P $0.87 ｜ ATM IV 59.7%，净 delta 敞口 3.0M shares
Top ΔOI: P 90 -9,851
仓位参考: Max Pain 80 ｜ Call Wall 78（+4.9%，弱）（OI 2.7k） ｜ Put Wall 70（-5.9%，弱）（OI 24.3k）
量化解读： 存量两侧均衡｜ATM IV 59.7%｜历史 Rank 94%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,956,610 股

📆 11-23 Forward Structure
存量OI: C 1.4k / P 1.6k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $1.94 / P $1.16 ｜ ATM IV 43.8%，净 delta 敞口 13k shares
Top ΔOI: C 80 +159 ｜ C 76 +117
仓位参考: Max Pain 79 ｜ Call Wall 76（+2.2%，弱）（OI 0.1k） ｜ Put Wall 72（-3.2%）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.8%｜历史 Rank 94%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 正 13,488 股

11-25（MEDIUM △）Top ΔOI: 78C +255 ｜ 69P +238
11-25（MEDIUM △）仓位参考: Max Pain 78 ｜ Call Wall 78（+4.9%，弱）（OI 0.3k） ｜ Put Wall 72（-3.2%，弱）（OI 0.2k）

📆 11-27 Forward Structure
存量OI: C 30.2k / P 7.8k，今日变化ΔOI: C +16.3k / P +0.3k，平值价格ATM: C $2.54 / P $1.61 ｜ ATM IV 45.2%，净 delta 敞口 419k shares
Top ΔOI: C 77 +7,761 ｜ C 80 +7,581
仓位参考: Max Pain 77 ｜ Call Wall 77（+3.6%，弱）（OI 7.8k） ｜ Put Wall 70（-5.9%）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 45.2%｜历史 Rank 94%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 418,972 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/GDX_morning.json