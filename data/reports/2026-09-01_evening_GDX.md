# 期权晚报 2026-09-01（快照 16:40 ET）

📊 市场环境

SPY $761.78 ｜ QQQ $707.64
VIX 16.34 ↑9.5%（5D +5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-04 93P ΔOI +2,932（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 95.15 → 收盘 94.67（-0.5%） ｜ 今日高 98.26 ｜ 低 94.49
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-04，窗口结束前不做对错判定）

Options: P/C成交量 0.98 | OI比 0.85 | ATM IV 50.6% | Skew 0.2pp | Term 0.90 | ExpMove ±3.8%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（3D）±3.8% ｜ 09-11（10D）±5.4% ｜ 09-18（17D）±7.8% ｜ 09-25（24D）±9.1%
   ⇒ IV–VIX Spread: +34.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -37,800,231 | GEX Change vs 上次快照 -12,641,709 | Flip: Primary Flip: 97.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 555 / LOW 178 / INVALID 243
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 97.98（全链重定价，覆盖 97%）
最近结构参考: Flip 98（现价低于该位 3.4%）
量化视角： 负 Gamma（3780万，无历史分位）｜负 Gamma 加深（1264万）｜现价位于 Flip 下方 3.38%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 98（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 90.0P — Vol 4,216 | 最新价 $1.68 | OI 38031→41924 (ΔOI +3893张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3893张（+10.2% vs前日OI），连续性待观察（方向未知）
09-18 92.0P — Vol 1,650 | 最新价 $2.30 | OI 1911→5398 (ΔOI +3487张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3487张（+182.5% vs前日OI），连续性待观察（方向未知）
09-18 108.0C — Vol 1,837 | 最新价 $0.54 | OI 3058→6118 (ΔOI +3060张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3060张（+100.1% vs前日OI），连续性待观察（方向未知）
09-04 93.0P — Vol 10,487 | 最新价 $1.07 | OI 1214→4146 (ΔOI +2932张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2932张（+241.5% vs前日OI），连续性待观察（方向未知）
09-04 96.0P — Vol 4,722 | 最新价 $2.39 | OI 11210→12625 (ΔOI +1415张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1415张（+12.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,787 张（Put 11,727 / Call 3,060），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +6.1k / P +5.8k ｜ Activity HIGH ｜ 3D
09-11  C +1.7k / P +2.6k ｜ Activity HIGH ｜ 10D
09-18  C +4.0k / P +8.5k ｜ Activity HIGH ｜ 17D
09-25  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 97.5k / P 82.4k
今日变化ΔOI: C +6.1k / P +5.8k
平值价格ATM:  C 1.65 / P 1.90
隐含波动率 ATM IV:  50.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -139k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 93 ｜ +2,932 ｜ $1.07 ｜ 名义 $313.7k* ｜ -1.8%
P 96 ｜ +1,415 ｜ $2.39 ｜ 名义 $338.2k* ｜ +1.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：96（+1.4%） / 93（-1.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 50.6%｜历史 Rank 84%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 139,428 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 15.9k / P 25.9k
今日变化ΔOI: C +1.7k / P +2.6k
平值价格ATM:  C 2.60 / P 2.48
隐含波动率 ATM IV:  43.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 90 ｜ +1,141 ｜ $0.92 ｜ 名义 $105.0k* ｜ -4.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：90（-4.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 43.4%｜历史 Rank 84%（近端代理）｜净 delta 敞口 负 26,951 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 245.3k / P 399.1k
今日变化ΔOI: C +4.0k / P +8.5k
平值价格ATM:  C 3.60 / P 3.80
隐含波动率 ATM IV:  44.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -324k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 90 ｜ +3,893 ｜ $1.68 ｜ 名义 $654.0k* ｜ -4.9%
P 92 ｜ +3,487 ｜ $2.30 ｜ 名义 $802.0k* ｜ -2.8%
C 108 ｜ +3,060 ｜ $0.54 ｜ 名义 $165.2k* ｜ +14.1%
结构参考：108（+14.1%） / 90（-4.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 44.7%｜历史 Rank 84%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 324,152 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 5.6k / P 6.5k
今日变化ΔOI: C +0.4k / P +0.4k
平值价格ATM:  C 4.40 / P 4.23
隐含波动率 ATM IV:  43.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 93 ｜ +512 ｜ $3.28 ｜ 名义 $167.9k* ｜ -1.8%
P 95 ｜ -120 ｜ $4.23 ｜ 名义 $-50.8k* ｜ +0.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：93（-1.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.7%｜历史 Rank 84%（近端代理）｜净 delta 敞口 负 5,478 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 50.6% vs 09-11 43.4%（差 +7.3pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/GDX_evening.json