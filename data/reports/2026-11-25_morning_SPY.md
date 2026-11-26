# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
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
🟡 **近现价集中开仓**: 11-27 735C ΔOI +13,533（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 665P ΔOI +11,509 占该期限总 OI 11.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 718.78 → 今开 703.20（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 705.05 ｜ 低 695.45

Options: P/C成交量 1.37 | OI比 0.73 | ATM IV 50.1% | Skew 4.4pp | Term 0.54 | ExpMove ±1.8%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价中性（Skew 4.4pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.73）+ 当日成交偏 Put（P/C量 1.37）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.37×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 28% ｜ P/C OI(近端) 0%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 28%）｜近端持仓极端 Call 重（P/C OI 分位 0%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-27（2D）±1.8% ｜ 11-30（5D）±2.5% ｜ 12-01（6D）±2.9% ｜ 12-02（7D）±3.2%
   ⇒ IV–VIX Spread: +18.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,265,558,625 | GEX Change vs 上次快照 -398,552,773 | Flip: Primary Flip: 729.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3336 / LOW 493 / INVALID 1849
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 729.93（全链重定价，覆盖 97%）
Put Wall 700（弱结构｜现价高于该位 0.5%）
最近结构参考: Put Wall 700（现价高于该位 0.5%）
量化视角： 负 Gamma（12.66亿，历史分位 28%，中性区）｜负 Gamma 加深（3.99亿）｜现价位于 Flip 下方 3.65%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 715（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 730（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 735.0C — Vol 59,414 | 最新价 $0.42 | OI 12890→26423 (ΔOI +13533张) | ΔOI/Volume 22.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13533张（+105.0% vs前日OI），连续性待观察（方向未知）
12-11 675.0P — Vol 12,332 | 最新价 $4.14 | OI 35069→48322 (ΔOI +13253张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13253张（+37.8% vs前日OI），连续性待观察（方向未知）
12-11 700.0P — Vol 12,980 | 最新价 $8.44 | OI 36373→49087 (ΔOI +12714张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12714张（+35.0% vs前日OI），连续性待观察（方向未知）
12-02 665.0P — Vol 12,306 | 最新价 $1.06 | OI 648→12157 (ΔOI +11509张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11509张（+1776.1% vs前日OI），连续性待观察（方向未知）
12-07 700.0P — Vol 12,589 | 最新价 $6.26 | OI 33808→45059 (ΔOI +11251张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11251张（+33.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 62,260 张（Put 48,727 / Call 13,533），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $24M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 248.4k / P 181.1k，今日成交量: C 670.6k / P 920.0k，平值价格ATM: C $4.41 / P $3.26 ｜ ATM IV 50.1%，预期波动 ±1.1%，Max Pain 715
Top ΔOI: P 734 -12,045 ｜ C 730 +11,064 ｜ C 725 +6,343

📆 Forward Expiration Structure

11-27  C +65.2k / P +16.9k ｜ Activity HIGH ｜ 2D
11-30  C +34.8k / P +36.5k ｜ Activity HIGH ｜ 5D
12-01  C +10.4k / P +16.7k ｜ Activity HIGH ｜ 6D
12-02  C +12.2k / P +29.1k ｜ Activity HIGH ｜ 7D

📆 11-27 Forward Structure
存量OI: C 477.7k / P 372.7k，今日变化ΔOI: C +65.2k / P +16.9k，平值价格ATM: C $7.16 / P $5.77 ｜ ATM IV 29.6%，净 delta 敞口 1.0M shares
Top ΔOI: C 735 +13,533 ｜ C 730 +9,991 ｜ P 657 +7,063
仓位参考: Max Pain 721 ｜ Call Wall 720（+2.4%，弱）（OI 11.9k） ｜ Put Wall 700（-0.5%，弱）（OI 35.1k）
量化解读： 存量 Call 重｜ATM IV 29.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,001,034 股

📆 11-30 Forward Structure
存量OI: C 380.7k / P 718.1k，今日变化ΔOI: C +34.8k / P +36.5k，平值价格ATM: C $9.72 / P $8.24 ｜ ATM IV 26.5%，净 delta 敞口 655k shares
Top ΔOI: P 696 +10,163 ｜ P 639 +6,434 ｜ C 735 +6,425
仓位参考: Max Pain 730 ｜ Put Wall 700（-0.5%，弱）（OI 30.3k）
量化解读： 存量 Put 重｜ATM IV 26.5%｜历史 Rank 99%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 654,812 股

📆 12-01 Forward Structure
存量OI: C 62.9k / P 45.9k，今日变化ΔOI: C +10.4k / P +16.7k，平值价格ATM: C $11.17 / P $9.45 ｜ ATM IV 27.9%，净 delta 敞口 -349k shares
Top ΔOI: P 675 +3,158 ｜ P 685 +2,459 ｜ P 665 +1,571
仓位参考: Max Pain 720 ｜ Call Wall 717（+2.0%，弱）（OI 0.8k） ｜ Put Wall 703（-0.0%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.9%｜历史 Rank 99%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 349,377 股

📆 12-02 Forward Structure
存量OI: C 43.9k / P 59.3k，今日变化ΔOI: C +12.2k / P +29.1k，平值价格ATM: C $12.02 / P $10.45 ｜ ATM IV 28.7%，净 delta 敞口 -344k shares
Top ΔOI: P 665 +11,509 ｜ P 660 +5,635 ｜ P 570 +3,367
仓位参考: Max Pain 715 ｜ Call Wall 717（+2.0%，弱）（OI 1.5k） ｜ Put Wall 700（-0.5%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜ATM IV 28.7%｜历史 Rank 99%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 343,816 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SPY_morning.json