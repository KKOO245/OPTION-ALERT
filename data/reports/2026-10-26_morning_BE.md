# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 195C ΔOI +1,748（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 230P ΔOI -1,854 占该期限总 OI 12.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 193.30 → 今开 203.01（+5.0%） | 较昨收变动（含盘初走势） ｜ 今日高 206.00 ｜ 低 189.00

Options: P/C成交量 0.55 | OI比 0.76 | ATM IV 85.2% | Skew 3.3pp | Term 0.90 | ExpMove ±9.0%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构正常（Term 0.90）｜保护溢价中性（Skew 3.3pp）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±9.0% ｜ 11-06（11D）±13.6% ｜ 11-13（18D）±15.2% ｜ 11-20（25D）±17.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,237,057 | GEX Change vs 上次快照 3,912,558 | Flip: Primary Flip: 213.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 560 / LOW 74 / INVALID 246
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 213.94（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 3.9%）
最近结构参考: Put Wall 190（现价高于该位 3.9%）
量化视角： 负 Gamma（524万，无历史分位）｜负 Gamma 缓解（+391万）｜现价位于 Flip 下方 7.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构）；上方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 214（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 230.0C — Vol 4,330 | 最新价 $0.85 | OI 1437→3277 (ΔOI +1840张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1840张（+128.0% vs前日OI），连续性待观察（方向未知）
10-30 195.0C — Vol 4,391 | 最新价 $8.30 | OI 11→1759 (ΔOI +1748张) | ΔOI/Volume 39.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1748张（+15890.9% vs前日OI），连续性待观察（方向未知）
10-30 200.0C — Vol 4,920 | 最新价 $6.29 | OI 254→1890 (ΔOI +1636张) | ΔOI/Volume 33.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1636张（+644.1% vs前日OI），连续性待观察（方向未知）
10-30 165.0C — Vol 1,505 | 最新价 $30.98 | OI 3→1505 (ΔOI +1502张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1502张（+50066.7% vs前日OI），连续性待观察（方向未知）
11-06 200.0C — Vol 3,058 | 最新价 $9.50 | OI 19→1450 (ΔOI +1431张) | ΔOI/Volume 46.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1431张（+7531.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,157 张（Put 0 / Call 8,157），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +17.6k / P +8.2k ｜ Activity HIGH ｜ 4D
11-06  C +3.7k / P +1.8k ｜ Activity HIGH ｜ 11D
11-13  C +1.1k / P -0.9k ｜ Activity HIGH ｜ 18D
11-20  C +4.9k / P +2.7k ｜ Activity HIGH ｜ 25D

📆 10-30 Forward Structure
存量OI: C 52.3k / P 40.0k，今日变化ΔOI: C +17.6k / P +8.2k，平值价格ATM: C $7.30 / P $10.50 ｜ ATM IV 85.2%，净 delta 敞口 442k shares
Top ΔOI: C 230 +1,840 ｜ C 195 +1,748 ｜ C 200 +1,636
仓位参考: Max Pain 215 ｜ Call Wall 200（+1.3%，弱）（OI 1.9k） ｜ Put Wall 190（-3.8%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 85.2%｜历史 Rank 46%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 441,799 股

📆 11-06 Forward Structure
存量OI: C 14.7k / P 14.1k，今日变化ΔOI: C +3.7k / P +1.8k，平值价格ATM: C $11.75 / P $15.15 ｜ ATM IV 83.4%，净 delta 敞口 91k shares
Top ΔOI: C 200 +1,431 ｜ C 205 +709 ｜ C 190 +455
仓位参考: Max Pain 235 ｜ Call Wall 200（+1.3%，弱）（OI 1.4k） ｜ Put Wall 215（+8.9%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 83.4%｜历史 Rank 46%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 91,193 股

📆 11-13 Forward Structure
存量OI: C 6.5k / P 7.8k，今日变化ΔOI: C +1.1k / P -0.9k，平值价格ATM: C $15.03 / P $14.92 ｜ ATM IV 80.4%，净 delta 敞口 160k shares
Top ΔOI: P 230 -1,854 ｜ P 160 +194
仓位参考: Max Pain 245 ｜ Call Wall 215（+8.9%，弱）（OI 0.2k） ｜ Put Wall 200（+1.3%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.4%｜历史 Rank 46%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 160,071 股

📆 11-20 Forward Structure
存量OI: C 55.8k / P 67.9k，今日变化ΔOI: C +4.9k / P +2.7k，平值价格ATM: C $16.27 / P $17.55 ｜ ATM IV 80.0%，净 delta 敞口 108k shares
Top ΔOI: C 200 +901 ｜ P 195 +418
仓位参考: Max Pain 235 ｜ Call Wall 200（+1.3%，弱）（OI 1.6k） ｜ Put Wall 200（+1.3%，弱）（OI 5.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.0%｜历史 Rank 46%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 108,038 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/BE_morning.json