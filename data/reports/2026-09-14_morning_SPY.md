# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-15 760P ΔOI +21,148（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-15 760P ΔOI +21,148 占该期限总 OI 10.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 764.29 → 今开 759.00（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 761.11 ｜ 低 758.45

Options: P/C成交量 1.03 | OI比 2.08 | ATM IV 14.2% | Skew 2.5pp | Term 0.97 | ExpMove ±0.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.08×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 18% ｜ P/C OI(近端) 67%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 18%）｜近端持仓结构中性（P/C OI 分位 67%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-15（1D）±0.6% ｜ 09-16（2D）±1.0% ｜ 09-17（3D）±1.2% ｜ 09-18（4D）±1.4%
   ⇒ IV–VIX Spread: -3.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,846,856,159 | GEX Change vs 上次快照 -1,254,637,979 | Flip: Primary Flip: 769.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3288 / LOW 302 / INVALID 2040
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 769.37（全链重定价，覆盖 97%）
Call Wall 800（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 769（现价低于该位 1.2%）
量化视角： 负 Gamma（18.47亿，历史分位偏负区，比 82% 的交易日更负）｜负 Gamma 加深（12.55亿）｜现价位于 Flip 下方 1.16%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 764（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-14 719.0P — Vol 33,238 | 最新价 $0.03 | OI 52→30540 (ΔOI +30488张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30488张（+58630.8% vs前日OI），连续性待观察（方向未知）
09-25 740.0P — Vol 26,498 | 最新价 $1.92 | OI 3316→25536 (ΔOI +22220张) | ΔOI/Volume 83.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22220张（+670.1% vs前日OI），连续性待观察（方向未知）
09-15 760.0P — Vol 29,150 | 最新价 $1.32 | OI 21967→43115 (ΔOI +21148张) | ΔOI/Volume 72.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21148张（+96.3% vs前日OI），连续性待观察（方向未知）
09-25 785.0C — Vol 23,150 | 最新价 $0.39 | OI 3952→24898 (ΔOI +20946张) | ΔOI/Volume 90.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20946张（+530.0% vs前日OI），连续性待观察（方向未知）
09-18 743.0P — Vol 23,152 | 最新价 $1.12 | OI 28452→49229 (ΔOI +20777张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20777张（+73.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 115,579 张（Put 94,633 / Call 20,946），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 129.2k / P 268.6k，今日成交量: C 469.4k / P 483.8k，平值价格ATM: C $1.42 / P $0.95 ｜ ATM IV 14.2%，预期波动 ±0.3%，Max Pain 764
Top ΔOI: P 719 +30,488 ｜ P 724 +16,918 ｜ P 722 +14,628

📆 Forward Expiration Structure

09-15  C +18.2k / P +50.8k ｜ Activity HIGH ｜ 1D
09-16  C +12.5k / P +17.0k ｜ Activity HIGH ｜ 2D
09-17  C +13.0k / P +32.5k ｜ Activity HIGH ｜ 3D
09-18  C -3.7k / P +23.6k ｜ Activity HIGH ｜ 4D

📆 09-15 Forward Structure
存量OI: C 50.5k / P 153.0k，今日变化ΔOI: C +18.2k / P +50.8k，平值价格ATM: C $2.56 / P $2.05 ｜ ATM IV 12.8%，净 delta 敞口 -1.9M shares
Top ΔOI: P 760 +21,148 ｜ P 734 +4,828 ｜ P 750 +4,600
仓位参考: Max Pain 764 ｜ Call Wall 770（+1.3%，弱）（OI 5.1k） ｜ Put Wall 760（-0.1%）（OI 43.1k）
量化解读： 存量 Put 重｜ATM IV 12.8%｜历史 Rank 60%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,884,361 股

📆 09-16 Forward Structure
存量OI: C 37.6k / P 45.2k，今日变化ΔOI: C +12.5k / P +17.0k，平值价格ATM: C $4.03 / P $3.47 ｜ ATM IV 15.6%，净 delta 敞口 -485k shares
Top ΔOI: P 760 +2,532 ｜ P 749 +2,493 ｜ C 780 +2,285
仓位参考: Max Pain 764 ｜ Call Wall 775（+1.9%，弱）（OI 3.5k） ｜ Put Wall 760（-0.1%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 15.6%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 484,896 股

📆 09-17 Forward Structure
存量OI: C 42.0k / P 58.9k，今日变化ΔOI: C +13.0k / P +32.5k，平值价格ATM: C $4.84 / P $4.20 ｜ ATM IV 15.7%，净 delta 敞口 -311k shares
Top ΔOI: P 750 +3,325
仓位参考: Max Pain 762 ｜ Call Wall 775（+1.9%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 15.7%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 310,884 股

📆 09-18 Forward Structure
存量OI: C 1109.2k / P 3818.2k，今日变化ΔOI: C -3.7k / P +23.6k，平值价格ATM: C $5.02 / P $5.52 ｜ ATM IV 15.1%，净 delta 敞口 -2.2M shares
Top ΔOI: P 750 -51,310 ｜ P 730 -33,105 ｜ P 743 +20,777
仓位参考: Max Pain 755 ｜ Call Wall 790（+3.9%，弱）（OI 57.7k）
量化解读： 存量 Put 重｜ATM IV 15.1%｜历史 Rank 60%（近端代理）｜净 delta 敞口 负 2,232,468 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SPY_morning.json