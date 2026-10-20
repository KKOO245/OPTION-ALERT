# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.58 ｜ QQQ $717.63
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 225C ΔOI +7,320（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 217.09 → 今开 215.97（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 217.54 ｜ 低 212.77

Options: P/C成交量 1.03 | OI比 0.82 | ATM IV 40.9% | Skew 2.7pp | Term 0.99 | ExpMove ±1.9%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常（Term 0.99）｜保护溢价中性（Skew 2.7pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-21（1D）±1.9% ｜ 10-23（3D）±3.0% ｜ 10-26（6D）±3.6% ｜ 10-28（8D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 71,086,368 | GEX Change vs 上次快照 -43,518,374 | Flip: Primary Flip: 212.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 656 / LOW 182 / INVALID 678
结构观察区: Primary Flip 212.86（全链重定价，覆盖 99%）
Call Wall 230（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 213（现价高于该位 1.0%）
量化视角： 正 Gamma（7109万，无历史分位）｜正 Gamma 减弱（4352万）｜现价位于 Flip 上方 1.02%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 220（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 180.0P — Vol 9,653 | 最新价 $0.04 | OI 7435→16456 (ΔOI +9021张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9021张（+121.3% vs前日OI），连续性待观察（方向未知）
10-21 225.0C — Vol 26,115 | 最新价 $0.20 | OI 3967→11287 (ΔOI +7320张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7320张（+184.5% vs前日OI），连续性待观察（方向未知）
10-21 227.5C — Vol 13,851 | 最新价 $0.10 | OI 2569→9860 (ΔOI +7291张) | ΔOI/Volume 52.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7291张（+283.8% vs前日OI），连续性待观察（方向未知）
10-23 230.0C — Vol 53,127 | 最新价 $0.21 | OI 47405→53714 (ΔOI +6309张) | ΔOI/Volume 11.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6309张（+13.3% vs前日OI），连续性待观察（方向未知）
10-21 170.0P — Vol 11,493 | 最新价 $0.02 | OI 188→6409 (ΔOI +6221张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6221张（+3309.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,162 张（Put 15,242 / Call 20,920），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-21  C +35.3k / P +38.6k ｜ Activity HIGH ｜ 1D
10-23  C +38.1k / P +29.4k ｜ Activity HIGH ｜ 3D
10-26  C +7.5k / P +8.6k ｜ Activity HIGH ｜ 6D
10-28  C +2.5k / P +1.9k ｜ Activity HIGH ｜ 8D

📆 10-21 Forward Structure
存量OI: C 97.3k / P 80.2k，今日变化ΔOI: C +35.3k / P +38.6k，平值价格ATM: C $2.35 / P $1.80 ｜ ATM IV 40.9%，净 delta 敞口 -19k shares
Top ΔOI: C 225 +7,320 ｜ C 227 +7,291
仓位参考: Max Pain 220 ｜ Call Wall 222.5（+3.5%，弱）（OI 11.9k） ｜ Put Wall 200（-7.0%，弱）（OI 8.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.9%｜历史 Rank 44%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,097 股

📆 10-23 Forward Structure
存量OI: C 420.0k / P 344.4k，今日变化ΔOI: C +38.1k / P +29.4k，平值价格ATM: C $3.56 / P $2.96 ｜ ATM IV 39.8%，净 delta 敞口 779k shares
Top ΔOI: C 230 +6,309 ｜ P 195 +5,921
仓位参考: Max Pain 220 ｜ Call Wall 230（+7.0%，弱）（OI 53.7k） ｜ Put Wall 210（-2.3%，弱）（OI 16.1k）
量化解读： 存量 Call 重｜ATM IV 39.8%｜历史 Rank 44%（近端代理）｜IV/RV 1.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 778,529 股

📆 10-26 Forward Structure
存量OI: C 30.0k / P 20.6k，今日变化ΔOI: C +7.5k / P +8.6k，平值价格ATM: C $4.15 / P $3.70 ｜ ATM IV 33.8%，净 delta 敞口 -85k shares
Top ΔOI: P 200 +3,078 ｜ C 230 +1,385 ｜ C 225 +1,378
仓位参考: Max Pain 218 ｜ Call Wall 225（+4.6%，弱）（OI 3.6k） ｜ Put Wall 200（-7.0%）（OI 5.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.8%｜历史 Rank 44%（近端代理）｜IV/RV 1.46×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 84,614 股

📆 10-28 Forward Structure
存量OI: C 10.3k / P 9.1k，今日变化ΔOI: C +2.5k / P +1.9k，平值价格ATM: C $4.90 / P $4.45 ｜ ATM IV 35.9%，净 delta 敞口 18k shares
Top ΔOI: P 207 +406 ｜ C 225 +384 ｜ C 217 +356
仓位参考: Max Pain 218 ｜ Call Wall 230（+7.0%）（OI 4.6k） ｜ Put Wall 215（-0.0%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 35.9%｜历史 Rank 44%（近端代理）｜IV/RV 1.55×（近似）｜净 delta 敞口 正 17,659 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/NVDA_morning.json