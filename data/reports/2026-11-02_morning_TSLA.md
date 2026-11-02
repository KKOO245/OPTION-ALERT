# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $753.20 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 397P ΔOI +2,387（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 399.81 → 今开 404.74（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 410.45 ｜ 低 397.67

Options: P/C成交量 0.51 | OI比 0.74 | ATM IV 64.7% | Skew 2.9pp | Term 0.66 | ExpMove ±3.7%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-04（2D）±3.7% ｜ 11-06（4D）±4.6% ｜ 11-09（7D）±5.2% ｜ 11-11（9D）±5.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 83,928,199 | GEX Change vs 上次快照 35,628,198 | Flip: Primary Flip: 383.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1338 / LOW 111 / INVALID 867
结构观察区: Primary Flip 383.49（全链重定价，覆盖 97%）
Call Wall 400（现价高于该位 0.6%）
最近结构参考: Call Wall 400（现价高于该位 0.6%）
量化视角： 正 Gamma（8393万，无历史分位）｜正 Gamma 增强（+3563万）｜现价位于 Flip 上方 4.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 398（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 383（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 240.0P — Vol 25,827 | 最新价 $0.07 | OI 2345→25767 (ΔOI +23422张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23422张（+998.8% vs前日OI），连续性待观察（方向未知）
11-06 140.0P — Vol 20,398 | 最新价 $0.01 | OI 1926→22318 (ΔOI +20392张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20392张（+1058.8% vs前日OI），连续性待观察（方向未知）
11-06 220.0P — Vol 15,554 | 最新价 $0.06 | OI 1709→16242 (ΔOI +14533张) | ΔOI/Volume 93.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14533张（+850.4% vs前日OI），连续性待观察（方向未知）
11-02 250.0P — Vol 13,371 | 最新价 $0.02 | OI 39→13381 (ΔOI +13342张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13342张（+34210.3% vs前日OI），连续性待观察（方向未知）
11-06 150.0P — Vol 10,825 | 最新价 $0.01 | OI 4895→15218 (ΔOI +10323张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10323张（+210.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 82,012 张（Put 82,012 / Call 0），跨 2 个期限｜远端彩票/名义（5 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 88.6k / P 65.6k，今日成交量: C 325.8k / P 166.1k，平值价格ATM: C $2.97 / P $2.67 ｜ ATM IV 64.7%，预期波动 ±1.4%，Max Pain 398
Top ΔOI: P 250 +13,342 ｜ P 397 +2,985 ｜ C 400 +2,692

📆 Forward Expiration Structure

11-04  C +8.7k / P +13.6k ｜ Activity HIGH ｜ 2D
11-06  C +39.6k / P +102.3k ｜ Activity HIGH ｜ 4D
11-09  C +2.5k / P +1.8k ｜ Activity HIGH ｜ 7D
11-11  C +2.5k / P +1.0k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 22.5k / P 26.6k，今日变化ΔOI: C +8.7k / P +13.6k，平值价格ATM: C $7.66 / P $7.25 ｜ ATM IV 58.8%，净 delta 敞口 139k shares
Top ΔOI: P 397 +2,387 ｜ P 395 +1,381
仓位参考: Max Pain 398 ｜ Call Wall 420（+4.4%，弱）（OI 1.9k） ｜ Put Wall 397.5（-1.2%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 58.8%｜历史 Rank 78%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 139,498 股

📆 11-06 Forward Structure
存量OI: C 122.4k / P 205.8k，今日变化ΔOI: C +39.6k / P +102.3k，平值价格ATM: C $9.67 / P $8.95 ｜ ATM IV 53.9%，净 delta 敞口 1.0M shares
Top ΔOI: P 240 +23,422 ｜ P 220 +14,533
仓位参考: Max Pain 390 ｜ Call Wall 410（+1.9%，弱）（OI 9.7k） ｜ Put Wall 380（-5.5%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜ATM IV 53.9%｜历史 Rank 78%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,037,012 股

📆 11-09 Forward Structure
存量OI: C 5.5k / P 5.9k，今日变化ΔOI: C +2.5k / P +1.8k，平值价格ATM: C $10.84 / P $10.04 ｜ ATM IV 45.9%，净 delta 敞口 74k shares
Top ΔOI: C 400 +749 ｜ P 367 +332 ｜ P 372 +310
仓位参考: Max Pain 395 ｜ Call Wall 400（-0.6%，弱）（OI 1.0k） ｜ Put Wall 380（-5.5%）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.9%｜历史 Rank 78%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 正 73,563 股

📆 11-11 Forward Structure
存量OI: C 4.8k / P 2.8k，今日变化ΔOI: C +2.5k / P +1.0k，平值价格ATM: C $12.03 / P $11.19 ｜ ATM IV 46.4%，净 delta 敞口 38k shares
Top ΔOI: C 450 +738 ｜ P 362 +206
仓位参考: Max Pain 395 ｜ Call Wall 405（+0.7%，弱）（OI 0.7k） ｜ Put Wall 395（-1.8%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 46.4%｜历史 Rank 78%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 正 38,103 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/TSLA_morning.json