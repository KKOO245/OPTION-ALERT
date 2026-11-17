# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-18 400C ΔOI +2,321（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 379.74 → 今开 382.28（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 382.84 ｜ 低 378.94

Options: P/C成交量 0.63 | OI比 0.95 | ATM IV 62.4% | Skew 7.2pp | Term 0.61 | ExpMove ±2.9%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 7.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（1D）±2.9% ｜ 11-20（3D）±4.7% ｜ 11-23（6D）±5.6% ｜ 11-25（8D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 42,321,958 | GEX Change vs 上次快照 17,445,129 | Flip: Primary Flip: 372.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1345 / LOW 240 / INVALID 961
结构观察区: Primary Flip 372.57（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 373（现价高于该位 2.5%）
量化视角： 正 Gamma（4232万，无历史分位）｜正 Gamma 增强（+1745万）｜现价位于 Flip 上方 2.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 382（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 373（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 300.0P — Vol 9,779 | 最新价 $0.23 | OI 10949→17427 (ΔOI +6478张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6478张（+59.2% vs前日OI），连续性待观察（方向未知）
11-18 410.0C — Vol 5,921 | 最新价 $0.28 | OI 1552→4709 (ΔOI +3157张) | ΔOI/Volume 53.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3157张（+203.4% vs前日OI），连续性待观察（方向未知）
11-30 420.0C — Vol 3,157 | 最新价 $2.24 | OI 0→3084 (ΔOI +3084张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3084张（前日OI缺失），连续性待观察（方向未知）
11-18 400.0C — Vol 12,524 | 最新价 $0.85 | OI 1759→4080 (ΔOI +2321张) | ΔOI/Volume 18.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2321张（+131.9% vs前日OI），连续性待观察（方向未知）
11-20 410.0C — Vol 9,983 | 最新价 $1.22 | OI 17787→20047 (ΔOI +2260张) | ΔOI/Volume 22.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2260张（+12.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,300 张（Put 6,478 / Call 10,822），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-18  C +21.5k / P +17.0k ｜ Activity HIGH ｜ 1D
11-20  C +8.3k / P +25.0k ｜ Activity HIGH ｜ 3D
11-23  C +2.7k / P +1.8k ｜ Activity HIGH ｜ 6D
11-25  C +0.9k / P +0.7k ｜ Activity HIGH ｜ 8D

📆 11-18 Forward Structure
存量OI: C 41.1k / P 39.1k，今日变化ΔOI: C +21.5k / P +17.0k，平值价格ATM: C $5.10 / P $6.00 ｜ ATM IV 62.4%，净 delta 敞口 319k shares
Top ΔOI: C 410 +3,157 ｜ C 400 +2,321 ｜ P 350 +1,818
仓位参考: Max Pain 382 ｜ Call Wall 410（+7.3%，弱）（OI 4.7k） ｜ Put Wall 392.5（+2.7%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜ATM IV 62.4%｜历史 Rank 74%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 318,985 股

📆 11-20 Forward Structure
存量OI: C 353.4k / P 506.4k，今日变化ΔOI: C +8.3k / P +25.0k，平值价格ATM: C $8.67 / P $9.39 ｜ ATM IV 62.3%，净 delta 敞口 -62k shares
Top ΔOI: P 300 +6,478 ｜ C 410 +2,260
仓位参考: Max Pain 375 ｜ Call Wall 400（+4.7%，弱）（OI 27.1k）
量化解读： 存量 Put 重｜ATM IV 62.3%｜历史 Rank 74%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 62,099 股

📆 11-23 Forward Structure
存量OI: C 21.6k / P 6.9k，今日变化ΔOI: C +2.7k / P +1.8k，平值价格ATM: C $10.10 / P $11.15 ｜ ATM IV 52.1%，净 delta 敞口 52k shares
Top ΔOI: C 400 +449
仓位参考: Max Pain 385 ｜ Put Wall 360（-5.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 52.1%｜历史 Rank 74%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 52,224 股

📆 11-25 Forward Structure
存量OI: C 2.6k / P 3.9k，今日变化ΔOI: C +0.9k / P +0.7k，平值价格ATM: C $11.68 / P $12.31 ｜ ATM IV 53.1%，净 delta 敞口 12k shares
Top ΔOI: C 380 +146 ｜ P 345 +143 ｜ C 400 +117
仓位参考: Max Pain 382 ｜ Call Wall 400（+4.7%，弱）（OI 0.2k） ｜ Put Wall 345（-9.7%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.1%｜历史 Rank 74%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 12,297 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/TSLA_morning.json