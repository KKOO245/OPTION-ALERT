# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.73 ｜ QQQ $737.93
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-30 736P ΔOI +9,844（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 660P ΔOI +11,559 占该期限总 OI 10.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 736.53 → 今开 740.17（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 740.58 ｜ 低 736.27

Options: P/C成交量 1.22 | OI比 1.90 | ATM IV 23.6% | Skew 1.3pp | Term 0.82 | ExpMove ±1.0%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交偏 Put（P/C量 1.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.22×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.90×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 41% ｜ P/C OI(近端) 70%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 41%）｜近端持仓结构中性（P/C OI 分位 70%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-30（1D）±1.0% ｜ 10-01（2D）±1.4% ｜ 10-02（3D）±1.6% ｜ 10-05（6D）±1.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -147,600,618 | GEX Change vs 上次快照 126,521,818 | Flip: Primary Flip: 739.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3200 / LOW 399 / INVALID 1665
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 739.46（全链重定价，覆盖 98%）
Put Wall 730（弱结构｜现价高于该位 1.1%） | Call Wall 760（现价低于该位 2.9%）
最近结构参考: Flip 739（现价低于该位 0.2%）
量化视角： 负 Gamma（1.48亿，历史分位 41%，中性区）｜负 Gamma 缓解（+1.27亿）｜现价位于 Flip 下方 0.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 730（Put Wall，弱结构） / 736（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 739（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-29 735.0P — Vol 90,087 | 最新价 $2.09 | OI 3354→39284 (ΔOI +35930张) | ΔOI/Volume 39.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35930张（+1071.3% vs前日OI），连续性待观察（方向未知）
10-30 690.0P — Vol 30,480 | 最新价 $4.50 | OI 5393→29585 (ΔOI +24192张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24192张（+448.6% vs前日OI），连续性待观察（方向未知）
10-30 640.0P — Vol 25,097 | 最新价 $1.46 | OI 8228→29772 (ΔOI +21544张) | ΔOI/Volume 85.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21544张（+261.8% vs前日OI），连续性待观察（方向未知）
10-30 720.0P — Vol 22,735 | 最新价 $10.00 | OI 5970→26370 (ΔOI +20400张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20400张（+341.7% vs前日OI），连续性待观察（方向未知）
10-02 650.0P — Vol 20,006 | 最新价 $0.05 | OI 2762→21289 (ΔOI +18527张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18527张（+670.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 120,593 张（Put 120,593 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $42M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 137.7k / P 262.1k，今日成交量: C 409.6k / P 501.2k，平值价格ATM: C $2.07 / P $1.71 ｜ ATM IV 23.6%，预期波动 ±0.5%，Max Pain 736
Top ΔOI: P 735 +35,930 ｜ P 732 +9,050 ｜ C 737 +7,470

📆 Forward Expiration Structure

09-30  C +17.0k / P +42.7k ｜ Activity HIGH ｜ 1D
10-01  C +10.2k / P +12.5k ｜ Activity HIGH ｜ 2D
10-02  C +28.6k / P +58.6k ｜ Activity MEDIUM △ ｜ 3D
10-05  C +7.5k / P +58.9k ｜ Activity HIGH ｜ 6D

📆 09-30 Forward Structure
存量OI: C 330.4k / P 588.3k，今日变化ΔOI: C +17.0k / P +42.7k，平值价格ATM: C $3.99 / P $3.52 ｜ ATM IV 21.5%，净 delta 敞口 -578k shares
Top ΔOI: P 736 +9,844
仓位参考: Max Pain 726 ｜ Call Wall 726（-1.6%）（OI 35.6k） ｜ Put Wall 730（-1.1%，弱）（OI 46.5k）
量化解读： 存量 Put 重｜ATM IV 21.5%｜历史 Rank 75%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 578,444 股

📆 10-01 Forward Structure
存量OI: C 48.5k / P 64.4k，今日变化ΔOI: C +10.2k / P +12.5k，平值价格ATM: C $5.24 / P $4.87 ｜ ATM IV 21.4%，净 delta 敞口 96k shares
Top ΔOI: C 747 +1,297 ｜ C 755 +1,164 ｜ C 736 +1,100
仓位参考: Max Pain 739 ｜ Call Wall 740（+0.3%）（OI 6.2k） ｜ Put Wall 740（+0.3%，弱）（OI 4.7k）
量化解读： 存量 Put 重｜ATM IV 21.4%｜历史 Rank 75%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 95,866 股

10-02（MEDIUM △）Top ΔOI: 650P +18,527 ｜ 705P +4,177
10-02（MEDIUM △）仓位参考: Max Pain 730 ｜ Call Wall 725（-1.7%）（OI 34.3k） ｜ Put Wall 730（-1.1%，弱）（OI 51.2k）

📆 10-05 Forward Structure
存量OI: C 25.7k / P 83.1k，今日变化ΔOI: C +7.5k / P +58.9k，平值价格ATM: C $7.20 / P $6.51 ｜ ATM IV 17.5%，净 delta 敞口 -40k shares
Top ΔOI: P 660 +11,559
仓位参考: Max Pain 739 ｜ Call Wall 755（+2.3%）（OI 8.2k）
量化解读： 存量 Put 重｜ATM IV 17.5%｜历史 Rank 75%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 40,034 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/QQQ_morning.json