# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.71 ｜ QQQ $756.20
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 197C ΔOI +6,366（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 188.75 → 今开 189.15（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 192.69 ｜ 低 187.95

Options: P/C成交量 0.49 | OI比 0.72 | ATM IV 46.3% | Skew 2.0pp | Term 1.26 | ExpMove ±4.0%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构正常偏陡（Term 1.26）｜保护溢价中性（Skew 2.0pp）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.0% ｜ 10-16（11D）±6.0% ｜ 10-23（18D）±7.6% ｜ 10-30（25D）±9.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 41,487,325 | GEX Change vs 上次快照 7,541,661 | Flip: Primary Flip: 178.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 577 / LOW 56 / INVALID 179
结构观察区: Primary Flip 178.37（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 11.1%） | Call Wall 200（现价低于该位 5.6%）
最近结构参考: Call Wall 200（现价低于该位 5.6%）
量化视角： 正 Gamma（4149万，无历史分位）｜正 Gamma 增强（+754万）｜现价位于 Flip 上方 5.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 188（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 178（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 197.5C — Vol 9,931 | 最新价 $1.17 | OI 6352→12718 (ΔOI +6366张) | ΔOI/Volume 64.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6366张（+100.2% vs前日OI），连续性待观察（方向未知）
10-09 195.0C — Vol 10,719 | 最新价 $1.70 | OI 6225→11635 (ΔOI +5410张) | ΔOI/Volume 50.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5410张（+86.9% vs前日OI），连续性待观察（方向未知）
10-09 202.5C — Vol 6,412 | 最新价 $0.50 | OI 5003→10221 (ΔOI +5218张) | ΔOI/Volume 81.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5218张（+104.3% vs前日OI），连续性待观察（方向未知）
10-16 30.0P — Vol 4,030 | 最新价 $0.01 | OI 137→4167 (ΔOI +4030张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4030张（+2941.6% vs前日OI），连续性待观察（方向未知）
10-16 35.0P — Vol 3,588 | 最新价 $0.01 | OI 67→3654 (ΔOI +3587张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3587张（+5353.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,611 张（Put 7,617 / Call 16,994），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +30.5k / P +13.4k ｜ Activity HIGH ｜ 4D
10-16  C +1.5k / P +18.6k ｜ Activity HIGH ｜ 11D
10-23  C +1.1k / P +1.0k ｜ Activity HIGH ｜ 18D
10-30  C +2.9k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 90.8k / P 65.2k，今日变化ΔOI: C +30.5k / P +13.4k，平值价格ATM: C $3.29 / P $4.30 ｜ ATM IV 46.3%，净 delta 敞口 306k shares
Top ΔOI: C 197 +6,366 ｜ C 195 +5,410 ｜ C 202 +5,218
仓位参考: Max Pain 188 ｜ Call Wall 197.5（+4.6%，弱）（OI 12.7k） ｜ Put Wall 190（+0.6%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 46.3%｜历史 Rank 23%（近端代理）｜IV/RV 2.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 305,741 股

📆 10-16 Forward Structure
存量OI: C 157.5k / P 187.9k，今日变化ΔOI: C +1.5k / P +18.6k，平值价格ATM: C $5.30 / P $6.11 ｜ ATM IV 43.2%，净 delta 敞口 -54k shares
仓位参考: Max Pain 170 ｜ Call Wall 200（+5.9%，弱）（OI 16.2k） ｜ Put Wall 170（-10.0%，弱）（OI 14.8k）
量化解读： 存量 Put 重｜ATM IV 43.2%｜历史 Rank 23%（近端代理）｜IV/RV 1.92×（近似）｜净 delta 敞口 负 53,828 股

📆 10-23 Forward Structure
存量OI: C 22.3k / P 16.2k，今日变化ΔOI: C +1.1k / P +1.0k，平值价格ATM: C $6.83 / P $7.59 ｜ ATM IV 42.6%，净 delta 敞口 18k shares
Top ΔOI: C 210 +384
仓位参考: Max Pain 180 ｜ Call Wall 180（-4.7%）（OI 4.6k） ｜ Put Wall 175（-7.3%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 42.6%｜历史 Rank 23%（近端代理）｜IV/RV 1.90×（近似）｜净 delta 敞口 正 17,551 股

📆 10-30 Forward Structure
存量OI: C 24.8k / P 16.5k，今日变化ΔOI: C +2.9k / P +0.6k，平值价格ATM: C $8.38 / P $8.93 ｜ ATM IV 43.6%，净 delta 敞口 110k shares
Top ΔOI: C 192 +1,940 ｜ C 200 +204
仓位参考: Max Pain 180 ｜ Call Wall 192.5（+1.9%，弱）（OI 2.7k） ｜ Put Wall 170（-10.0%）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 43.6%｜历史 Rank 23%（近端代理）｜IV/RV 1.94×（近似）｜净 delta 敞口 正 109,819 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/PLTR_morning.json