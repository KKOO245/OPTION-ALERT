# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $716.47 ｜ QQQ $633.93
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 275P ΔOI -14,600（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 260P ΔOI +2,291 占该期限总 OI 15.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 267.14 → 今开 263.23（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 263.51 ｜ 低 260.84

Options: P/C成交量 2.44 | OI比 1.42 | ATM IV 41.3% | Skew 5.3pp | Term 0.65 | ExpMove ±1.6%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜当日成交偏 Put（P/C量 2.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.44×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.42×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±1.6% ｜ 11-30（5D）±2.4% ｜ 12-01（6D）±2.5% ｜ 12-02（7D）±3.2%
   ⇒ IV–VIX Spread: +9.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -964,971,635 | GEX Change vs 上次快照 -182,648,686 | Flip: Primary Flip: 283.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1228 / LOW 244 / INVALID 1230
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.56（全链重定价，覆盖 98%）
Put Wall 250（弱结构｜现价高于该位 5.2%）
最近结构参考: Put Wall 250（现价高于该位 5.2%）
量化视角： 负 Gamma（9.65亿，无历史分位）｜负 Gamma 加深（1.83亿）｜现价位于 Flip 下方 7.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（Put Wall，弱结构）；上方 267（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 254.0P — Vol 33,885 | 最新价 $3.17 | OI 5403→35400 (ΔOI +29997张) | ΔOI/Volume 88.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29997张（+555.2% vs前日OI），连续性待观察（方向未知）
12-18 258.0P — Vol 22,070 | 最新价 $3.90 | OI 24255→45757 (ΔOI +21502张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21502张（+88.7% vs前日OI），连续性待观察（方向未知）
11-30 252.5P — Vol 8,373 | 最新价 $0.23 | OI 908→8704 (ΔOI +7796张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7796张（+858.6% vs前日OI），连续性待观察（方向未知）
11-25 267.0P — Vol 15,485 | 最新价 $1.72 | OI 1681→8879 (ΔOI +7198张) | ΔOI/Volume 46.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7198张（+428.2% vs前日OI），连续性待观察（方向未知）
12-18 255.0P — Vol 55,419 | 最新价 $3.35 | OI 77230→82307 (ΔOI +5077张) | ΔOI/Volume 9.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5077张（+6.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 71,570 张（Put 71,570 / Call 0），跨 3 个期限｜近端保护（5 档，距现价 ≤5%，权利金合计约 $21M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 44.5k / P 63.1k，今日成交量: C 66.1k / P 161.5k，平值价格ATM: C $1.27 / P $1.10 ｜ ATM IV 41.3%，预期波动 ±0.9%，Max Pain 267
Top ΔOI: P 267 +7,198 ｜ P 265 +4,656 ｜ C 268 +3,139

📆 Forward Expiration Structure

11-27  C +12.0k / P -15.4k ｜ Activity HIGH ｜ 2D
11-30  C +3.7k / P +14.2k ｜ Activity HIGH ｜ 5D
12-01  C +0.8k / P +1.0k ｜ Activity HIGH ｜ 6D
12-02  C +1.7k / P +3.8k ｜ Activity HIGH ｜ 7D

📆 11-27 Forward Structure
存量OI: C 124.0k / P 224.9k，今日变化ΔOI: C +12.0k / P -15.4k，平值价格ATM: C $2.24 / P $2.01 ｜ ATM IV 25.9%，净 delta 敞口 1.9M shares
Top ΔOI: P 275 -14,600 ｜ P 276 -4,614 ｜ C 276 +3,671
仓位参考: Max Pain 270 ｜ Call Wall 270（+2.6%，弱）（OI 9.8k） ｜ Put Wall 270（+2.6%，弱）（OI 35.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 25.9%｜历史 Rank 92%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 1,927,002 股

📆 11-30 Forward Structure
存量OI: C 25.3k / P 75.5k，今日变化ΔOI: C +3.7k / P +14.2k，平值价格ATM: C $3.08 / P $3.12 ｜ ATM IV 24.3%，净 delta 敞口 -419k shares
Top ΔOI: P 252 +7,796 ｜ P 261 +3,635 ｜ P 264 +3,467
仓位参考: Max Pain 269 ｜ Call Wall 276（+4.9%，弱）（OI 3.9k） ｜ Put Wall 260（-1.2%，弱）（OI 8.9k）
量化解读： 存量 Put 重｜ATM IV 24.3%｜历史 Rank 92%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 419,041 股

📆 12-01 Forward Structure
存量OI: C 14.5k / P 15.5k，今日变化ΔOI: C +0.8k / P +1.0k，平值价格ATM: C $3.03 / P $3.44 ｜ ATM IV 25.9%，净 delta 敞口 -25k shares
Top ΔOI: C 270 +298 ｜ P 247 +232 ｜ P 250 +188
仓位参考: Max Pain 265 ｜ Call Wall 270（+2.6%，弱）（OI 3.4k） ｜ Put Wall 260（-1.2%）（OI 6.0k）
量化解读： 存量两侧均衡｜ATM IV 25.9%｜历史 Rank 92%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 负 24,965 股

📆 12-02 Forward Structure
存量OI: C 4.1k / P 10.7k，今日变化ΔOI: C +1.7k / P +3.8k，平值价格ATM: C $4.15 / P $4.22 ｜ ATM IV 26.9%，净 delta 敞口 -138k shares
Top ΔOI: P 260 +2,291 ｜ C 273 +431 ｜ C 271 +293
仓位参考: Max Pain 265 ｜ Call Wall 273（+3.8%，弱）（OI 0.6k） ｜ Put Wall 260（-1.2%）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 26.9%｜历史 Rank 92%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 137,736 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/IWM_morning.json