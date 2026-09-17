# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-17 737P ΔOI +6,248（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 757.39 → 今开 759.50（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 761.03 ｜ 低 758.72

Options: P/C成交量 0.92 | OI比 2.14 | ATM IV 31.6% | Skew 4.8pp | Term 0.42 | ExpMove ±0.9%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.42，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.14×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 26% ｜ P/C OI(近端) 71%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 26%）｜近端持仓结构中性（P/C OI 分位 71%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-17（1D）±0.9% ｜ 09-18（2D）±1.2% ｜ 09-21（5D）±1.3% ｜ 09-22（6D）±1.4%
   ⇒ IV–VIX Spread: +14.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,359,266,664 | GEX Change vs 上次快照 562,812,838 | Flip: Primary Flip: 768.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3114 / LOW 311 / INVALID 2145
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.05（全链重定价，覆盖 96%）
Call Wall 800（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 768（现价低于该位 1.0%）
量化视角： 负 Gamma（13.59亿，历史分位 26%，中性区）｜负 Gamma 缓解（+5.63亿）｜现价位于 Flip 下方 0.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 758（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 768（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-16 718.0P — Vol 57,489 | 最新价 $0.05 | OI 397→53308 (ΔOI +52911张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52911张（+13327.7% vs前日OI），连续性待观察（方向未知）
09-18 606.0P — Vol 52,407 | 最新价 $0.02 | OI 553→49162 (ΔOI +48609张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增48609张（+8790.0% vs前日OI），连续性待观察（方向未知）
09-18 607.0P — Vol 48,520 | 最新价 $0.03 | OI 660→45237 (ΔOI +44577张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44577张（+6754.1% vs前日OI），连续性待观察（方向未知）
09-25 730.0P — Vol 34,493 | 最新价 $1.62 | OI 2297→35915 (ΔOI +33618张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33618张（+1463.6% vs前日OI），连续性待观察（方向未知）
09-25 745.0P — Vol 34,029 | 最新价 $3.57 | OI 26167→58544 (ΔOI +32377张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32377张（+123.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 212,092 张（Put 212,092 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $17M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 112.8k / P 241.6k，今日成交量: C 661.9k / P 607.1k，平值价格ATM: C $2.02 / P $2.76 ｜ ATM IV 31.6%，预期波动 ±0.6%，Max Pain 758
Top ΔOI: P 718 +52,911 ｜ P 750 +7,118 ｜ C 770 +6,264

📆 Forward Expiration Structure

09-17  C +13.1k / P +31.3k ｜ Activity HIGH ｜ 1D
09-18  C +92.0k / P +180.4k ｜ Activity HIGH ｜ 2D
09-21  C +21.6k / P +24.9k ｜ Activity HIGH ｜ 5D
09-22  C +7.9k / P +7.0k ｜ Activity HIGH ｜ 6D

📆 09-17 Forward Structure
存量OI: C 67.1k / P 116.2k，今日变化ΔOI: C +13.1k / P +31.3k，平值价格ATM: C $3.13 / P $3.73 ｜ ATM IV 19.4%，净 delta 敞口 213k shares
Top ΔOI: P 737 +6,248 ｜ P 736 +3,842 ｜ P 738 +3,341
仓位参考: Max Pain 759 ｜ Call Wall 760（-0.1%，弱）（OI 4.8k） ｜ Put Wall 737（-3.1%，弱）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 19.4%｜历史 Rank 98%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 212,839 股

📆 09-18 Forward Structure
存量OI: C 1256.6k / P 4021.5k，今日变化ΔOI: C +92.0k / P +180.4k，平值价格ATM: C $3.48 / P $5.39 ｜ ATM IV 17.5%，净 delta 敞口 -241k shares
Top ΔOI: P 606 +48,609 ｜ P 607 +44,577 ｜ P 745 +27,389
仓位参考: Max Pain 757 ｜ Call Wall 790（+3.9%，弱）（OI 57.4k） ｜ Put Wall 760（-0.1%，弱）（OI 127.0k）
量化解读： 存量 Put 重｜ATM IV 17.5%｜历史 Rank 98%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 240,887 股

📆 09-21 Forward Structure
存量OI: C 59.6k / P 66.3k，今日变化ΔOI: C +21.6k / P +24.9k，平值价格ATM: C $4.00 / P $5.90 ｜ ATM IV 13.3%，净 delta 敞口 -326k shares
Top ΔOI: P 755 +7,431 ｜ C 789 +6,817 ｜ C 790 +6,297
仓位参考: Max Pain 758 ｜ Call Wall 789（+3.7%，弱）（OI 7.0k） ｜ Put Wall 755（-0.7%）（OI 11.5k）
量化解读： 存量两侧均衡｜ATM IV 13.3%｜历史 Rank 98%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 326,002 股

📆 09-22 Forward Structure
存量OI: C 20.9k / P 22.9k，今日变化ΔOI: C +7.9k / P +7.0k，平值价格ATM: C $4.46 / P $6.49 ｜ ATM IV 13.2%，净 delta 敞口 113k shares
Top ΔOI: C 825 +1,098 ｜ P 690 +762
仓位参考: Max Pain 760 ｜ Call Wall 785（+3.2%，弱）（OI 1.3k） ｜ Put Wall 760（-0.1%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.2%｜历史 Rank 98%（近端代理）｜净 delta 敞口 正 113,151 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SPY_morning.json