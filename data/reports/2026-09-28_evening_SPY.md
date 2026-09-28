# 期权晚报 2026-09-28（快照 16:40 ET）

📊 市场环境

SPY $765.61 ｜ QQQ $736.53
VIX 16.07 ↑8.1%（5D +8.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-29 780C ΔOI +2,453（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 768.35 → 收盘 765.61（-0.4%） ｜ 今日高 769.54 ｜ 低 763.72 ｜ 昨收 771.35 → 收盘 765.61（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.05 | OI比 1.24 | ATM IV 15.9% | Skew 0.3pp | Term 0.84 | ExpMove ±0.5%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价薄（Skew 0.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 36% ｜ P/C OI(近端) 8%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 36%）｜近端持仓极端 Call 重（P/C OI 分位 8%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-29（1D）±0.5% ｜ 09-30（2D）±0.8% ｜ 10-01（3D）±1.0% ｜ 10-02（4D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -857,124,330 | GEX Change vs 上次快照 -450,051,669 | Flip: Primary Flip: 770.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2889 / LOW 502 / INVALID 1765
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.56（全链重定价，覆盖 93%）
Call Wall 785（现价低于该位 2.5%）
最近结构参考: Flip 771（现价低于该位 0.6%）
量化视角： 负 Gamma（8.57亿，历史分位 36%，中性区）｜负 Gamma 加深（4.50亿）｜现价位于 Flip 下方 0.64%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考） / 785（Call Wall）。
• Gamma 区域：切换参考 771（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 755.0P — Vol 911 | 最新价 $7.53 | OI 6152→61252 (ΔOI +55100张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55100张（+895.6% vs前日OI），连续性待观察（方向未知）
10-30 725.0P — Vol 690 | 最新价 $2.90 | OI 7494→62021 (ΔOI +54527张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54527张（+727.6% vs前日OI），连续性待观察（方向未知）
10-02 595.0P — Vol 12 | 最新价 $0.01 | OI 311→30311 (ΔOI +30000张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30000张（+9646.3% vs前日OI），连续性待观察（方向未知）
10-16 736.0P — Vol 27,639 | 最新价 $1.95 | OI 30776→55001 (ΔOI +24225张) | ΔOI/Volume 87.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24225张（+78.7% vs前日OI），连续性待观察（方向未知）
09-30 816.0C — Vol 4,949 | 最新价 $0.01 | OI 10437→31791 (ΔOI +21354张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21354张（+204.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 185,206 张（Put 163,852 / Call 21,354），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $62M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-29  C +19.3k / P +18.5k ｜ Activity HIGH ｜ 1D
09-30  C +65.0k / P +47.2k ｜ Activity HIGH ｜ 2D
10-01  C +13.7k / P +6.6k ｜ Activity HIGH ｜ 3D
10-02  C +39.5k / P +63.9k ｜ Activity HIGH ｜ 4D

📆 09-29 Forward Structure
存量OI: C 66.9k / P 106.5k，今日变化ΔOI: C +19.3k / P +18.5k，平值价格ATM: C $1.74 / P $2.30 ｜ ATM IV 12.5%，净 delta 敞口 -821k shares
Top ΔOI: C 780 +2,453 ｜ P 771 +1,833 ｜ C 777 +1,735
仓位参考: Max Pain 768 ｜ Call Wall 780（+1.9%，弱）（OI 4.4k） ｜ Put Wall 755（-1.4%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.5%｜历史 Rank 69%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 821,319 股

📆 09-30 Forward Structure
存量OI: C 625.5k / P 1844.0k，今日变化ΔOI: C +65.0k / P +47.2k，平值价格ATM: C $2.81 / P $3.22 ｜ ATM IV 13.3%，净 delta 敞口 -473k shares
Top ΔOI: C 816 +21,354 ｜ C 817 +12,168 ｜ P 698 +7,647
仓位参考: Max Pain 762 ｜ Call Wall 786（+2.7%，弱）（OI 23.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.3%｜历史 Rank 69%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 负 472,632 股

📆 10-01 Forward Structure
存量OI: C 48.0k / P 59.6k，今日变化ΔOI: C +13.7k / P +6.6k，平值价格ATM: C $3.52 / P $3.92 ｜ ATM IV 13.3%，净 delta 敞口 219k shares
Top ΔOI: C 780 +1,095 ｜ C 783 +955 ｜ C 800 +885
仓位参考: Max Pain 765 ｜ Call Wall 780（+1.9%，弱）（OI 2.7k） ｜ Put Wall 770（+0.6%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.3%｜历史 Rank 69%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 218,821 股

📆 10-02 Forward Structure
存量OI: C 238.1k / P 326.2k，今日变化ΔOI: C +39.5k / P +63.9k，平值价格ATM: C $4.41 / P $4.50 ｜ ATM IV 13.8%，净 delta 敞口 -421k shares
Top ΔOI: C 818 +6,019 ｜ C 817 +5,894
仓位参考: Max Pain 766 ｜ Call Wall 785（+2.5%）（OI 60.8k） ｜ Put Wall 750（-2.0%，弱）（OI 16.0k）
量化解读： 存量 Put 重｜ATM IV 13.8%｜历史 Rank 69%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 负 420,838 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/SPY_evening.json