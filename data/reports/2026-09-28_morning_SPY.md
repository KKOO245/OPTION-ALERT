# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.40
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.8（fear）
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-29 780C ΔOI +2,453（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 771.35 → 今开 768.35（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 768.59 ｜ 低 766.98

Options: P/C成交量 1.28 | OI比 1.24 | ATM IV 15.0% | Skew 1.3pp | Term 0.88 | ExpMove ±0.6%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交偏 Put（P/C量 1.28）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.28×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 47% ｜ P/C OI(近端) 8%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 47%）｜近端持仓极端 Call 重（P/C OI 分位 8%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-29（1D）±0.6% ｜ 09-30（2D）±0.8% ｜ 10-01（3D）±1.0% ｜ 10-02（4D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -407,072,661 | GEX Change vs 上次快照 -737,640,958 | Flip: Primary Flip: 770.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3126 / LOW 443 / INVALID 1587
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.15（全链重定价，覆盖 97%）
Call Wall 785（现价低于该位 2.1%）
最近结构参考: Flip 770（现价低于该位 0.2%）
量化视角： 负 Gamma（4.07亿，历史分位 47%，中性区）｜由正转负（7.38亿）｜现价位于 Flip 下方 0.25%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考） / 785（Call Wall）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 755.0P — Vol 56,329 | 最新价 $6.18 | OI 6152→61252 (ΔOI +55100张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55100张（+895.6% vs前日OI），连续性待观察（方向未知）
10-30 725.0P — Vol 55,929 | 最新价 $2.45 | OI 7494→62021 (ΔOI +54527张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54527张（+727.6% vs前日OI），连续性待观察（方向未知）
10-02 595.0P — Vol 30,000 | 最新价 $0.02 | OI 311→30311 (ΔOI +30000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30000张（+9646.3% vs前日OI），连续性待观察（方向未知）
10-16 736.0P — Vol 27,434 | 最新价 $1.53 | OI 30776→55001 (ΔOI +24225张) | ΔOI/Volume 88.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24225张（+78.7% vs前日OI），连续性待观察（方向未知）
09-30 816.0C — Vol 22,296 | 最新价 $0.01 | OI 10437→31791 (ΔOI +21354张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21354张（+204.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 185,206 张（Put 163,852 / Call 21,354），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $51M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 179.7k / P 222.8k，今日成交量: C 419.5k / P 536.5k，平值价格ATM: C $1.06 / P $1.44 ｜ ATM IV 15.0%，预期波动 ±0.3%，Max Pain 770
Top ΔOI: C 777 +11,767 ｜ P 718 +10,639 ｜ P 719 +9,426

📆 Forward Expiration Structure

09-29  C +19.3k / P +18.5k ｜ Activity HIGH ｜ 1D
09-30  C +65.0k / P +47.2k ｜ Activity MEDIUM △ ｜ 2D
10-01  C +13.7k / P +6.6k ｜ Activity HIGH ｜ 3D
10-02  C +39.5k / P +63.9k ｜ Activity HIGH ｜ 4D

📆 09-29 Forward Structure
存量OI: C 66.9k / P 106.5k，今日变化ΔOI: C +19.3k / P +18.5k，平值价格ATM: C $2.14 / P $2.43 ｜ ATM IV 12.6%，净 delta 敞口 -596k shares
Top ΔOI: C 780 +2,453 ｜ P 771 +1,833 ｜ C 777 +1,735
仓位参考: Max Pain 768 ｜ Call Wall 780（+1.5%，弱）（OI 4.4k） ｜ Put Wall 755（-1.7%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 596,199 股

09-30（MEDIUM △）Top ΔOI: 816C +21,354 ｜ 817C +12,168
09-30（MEDIUM △）仓位参考: Max Pain 762 ｜ Call Wall 786（+2.3%，弱）（OI 23.2k）

📆 10-01 Forward Structure
存量OI: C 48.0k / P 59.6k，今日变化ΔOI: C +13.7k / P +6.6k，平值价格ATM: C $3.79 / P $3.78 ｜ ATM IV 13.0%，净 delta 敞口 286k shares
Top ΔOI: C 780 +1,095 ｜ C 783 +955 ｜ C 800 +885
仓位参考: Max Pain 765 ｜ Call Wall 780（+1.5%，弱）（OI 2.7k） ｜ Put Wall 770（+0.2%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.0%｜历史 Rank 64%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 286,187 股

📆 10-02 Forward Structure
存量OI: C 238.1k / P 326.2k，今日变化ΔOI: C +39.5k / P +63.9k，平值价格ATM: C $4.57 / P $4.41 ｜ ATM IV 13.4%，净 delta 敞口 -277k shares
Top ΔOI: C 818 +6,019 ｜ C 817 +5,894
仓位参考: Max Pain 766 ｜ Call Wall 785（+2.2%）（OI 60.8k） ｜ Put Wall 750（-2.4%，弱）（OI 16.0k）
量化解读： 存量 Put 重｜ATM IV 13.4%｜历史 Rank 64%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 负 277,468 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/SPY_morning.json