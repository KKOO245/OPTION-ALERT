# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $764.48 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 731P ΔOI +10,358（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-06 810C ΔOI +44,167 占该期限总 OI 27.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 762.63 → 今开 764.36（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 765.33 ｜ 低 759.72

Options: P/C成交量 1.53 | OI比 1.23 | ATM IV 24.1% | Skew 1.6pp | Term 0.61 | ExpMove ±0.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜当日成交偏 Put（P/C量 1.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 28% ｜ P/C OI(近端) 8%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 28%）｜近端持仓极端 Call 重（P/C OI 分位 8%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-02（1D）±0.9% ｜ 10-05（4D）±1.1% ｜ 10-06（5D）±1.3% ｜ 10-07（6D）±1.5%
   ⇒ IV–VIX Spread: +6.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,255,571,656 | GEX Change vs 上次快照 -208,533,795 | Flip: Primary Flip: 767.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2804 / LOW 324 / INVALID 1672
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 767.73（全链重定价，覆盖 98%）
最近结构参考: Flip 768（现价低于该位 1.0%）
量化视角： 负 Gamma（12.56亿，历史分位 28%，中性区）｜负 Gamma 加深（2.09亿）｜现价位于 Flip 下方 0.96%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 764（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 768（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-06 810.0C — Vol 44,711 | 最新价 $0.02 | OI 250→44417 (ΔOI +44167张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44167张（+17666.8% vs前日OI），连续性待观察（方向未知）
10-06 809.0C — Vol 42,086 | 最新价 $0.03 | OI 1→41675 (ΔOI +41674张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增41674张（+4167400.0% vs前日OI），连续性待观察（方向未知）
10-16 733.0P — Vol 29,546 | 最新价 $1.62 | OI 6919→29974 (ΔOI +23055张) | ΔOI/Volume 78.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23055张（+333.2% vs前日OI），连续性待观察（方向未知）
10-30 800.0C — Vol 21,549 | 最新价 $1.10 | OI 19911→36843 (ΔOI +16932张) | ΔOI/Volume 78.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16932张（+85.0% vs前日OI），连续性待观察（方向未知）
10-01 768.0C — Vol 107,001 | 最新价 $0.58 | OI 2415→16308 (ΔOI +13893张) | ΔOI/Volume 13.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13893张（+575.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 139,721 张（Put 23,055 / Call 116,666），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 192.6k / P 236.8k，今日成交量: C 579.7k / P 885.2k，平值价格ATM: C $2.02 / P $1.90 ｜ ATM IV 24.1%，预期波动 ±0.5%，Max Pain 764
Top ΔOI: C 768 +13,893 ｜ P 732 +12,576 ｜ P 733 +11,938

📆 Forward Expiration Structure

10-02  C +41.6k / P +64.3k ｜ Activity HIGH ｜ 1D
10-05  C +11.0k / P +12.0k ｜ Activity HIGH ｜ 4D
10-06  C +96.6k / P +7.1k ｜ Activity HIGH ｜ 5D
10-07  C +33.3k / P +13.0k ｜ Activity HIGH ｜ 6D

📆 10-02 Forward Structure
存量OI: C 351.5k / P 550.3k，今日变化ΔOI: C +41.6k / P +64.3k，平值价格ATM: C $3.70 / P $3.23 ｜ ATM IV 19.4%，净 delta 敞口 122k shares
Top ΔOI: P 730 +11,738 ｜ P 731 +10,358 ｜ P 729 +6,093
仓位参考: Max Pain 765 ｜ Call Wall 775（+1.9%，弱）（OI 17.6k） ｜ Put Wall 745（-2.0%，弱）（OI 68.1k）
量化解读： 存量 Put 重｜ATM IV 19.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 121,846 股

📆 10-05 Forward Structure
存量OI: C 49.1k / P 77.2k，今日变化ΔOI: C +11.0k / P +12.0k，平值价格ATM: C $4.62 / P $4.11 ｜ ATM IV 13.4%，净 delta 敞口 -165k shares
Top ΔOI: P 735 +2,278 ｜ C 795 +1,878 ｜ C 794 +1,856
仓位参考: Max Pain 766 ｜ Call Wall 775（+1.9%，弱）（OI 2.6k） ｜ Put Wall 750（-1.4%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜ATM IV 13.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 164,930 股

📆 10-06 Forward Structure
存量OI: C 122.3k / P 38.6k，今日变化ΔOI: C +96.6k / P +7.1k，平值价格ATM: C $5.35 / P $4.72 ｜ ATM IV 13.7%，净 delta 敞口 -35k shares
Top ΔOI: C 810 +44,167 ｜ C 809 +41,674 ｜ C 825 +2,872
仓位参考: Max Pain 766
量化解读： 存量 Call 重｜ATM IV 13.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 负 34,703 股

📆 10-07 Forward Structure
存量OI: C 48.8k / P 65.5k，今日变化ΔOI: C +33.3k / P +13.0k，平值价格ATM: C $5.95 / P $5.20 ｜ ATM IV 14.0%，净 delta 敞口 277k shares
Top ΔOI: C 810 +11,654 ｜ P 690 +8,030
仓位参考: Max Pain 766 ｜ Put Wall 760（-0.0%，弱）（OI 14.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.0%｜历史 Rank 93%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 277,000 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 19.4% vs 10-05 13.4%（差 +6.0pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=38 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=38）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SPY_morning.json