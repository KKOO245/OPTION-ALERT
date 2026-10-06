# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.55 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 88C ΔOI +1,058（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 93C ΔOI +62 占该期限总 OI 57.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 87.42 → 今开 87.72（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 87.93 ｜ 低 86.75

Options: P/C成交量 0.46 | OI比 0.34 | ATM IV 43.6% | Skew -3.1pp | Term 0.92 | ExpMove ±3.3%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -3.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±3.3% ｜ 10-16（10D）±5.4% ｜ 10-19（13D）±5.8% ｜ 10-21（15D）±3.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,402,656 | GEX Change vs 上次快照 -7,299,634 | Flip: Primary Flip: 85.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 434 / LOW 112 / INVALID 414
结构观察区: Primary Flip 85.28（全链重定价，覆盖 97%）
Put Wall 85（弱结构｜现价高于该位 2.1%） | Call Wall 90（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 85（现价高于该位 1.8%）
量化视角： 正 Gamma（2440万，无历史分位）｜正 Gamma 减弱（730万）｜现价位于 Flip 上方 1.79%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构）；上方 87（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 81.0P — Vol 2,079 | 最新价 $0.37 | OI 527→2380 (ΔOI +1853张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1853张（+351.6% vs前日OI），连续性待观察（方向未知）
10-16 88.0C — Vol 1,398 | 最新价 $2.30 | OI 799→1857 (ΔOI +1058张) | ΔOI/Volume 75.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1058张（+132.4% vs前日OI），连续性待观察（方向未知）
10-16 93.0C — Vol 1,663 | 最新价 $0.68 | OI 3103→4023 (ΔOI +920张) | ΔOI/Volume 55.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增920张（+29.6% vs前日OI），连续性待观察（方向未知）
10-09 92.0C — Vol 1,436 | 最新价 $0.30 | OI 10550→11419 (ΔOI +869张) | ΔOI/Volume 60.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+8.2% vs前日OI），连续性待观察（方向未知）
10-16 84.0P — Vol 859 | 最新价 $0.86 | OI 5502→6000 (ΔOI +498张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增498张（+9.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,198 张（Put 2,351 / Call 2,847），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +2.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 3D
10-16  C +2.5k / P +1.0k ｜ Activity MEDIUM △ ｜ 10D
10-19  C +83 / P +24 ｜ Activity LOW ｜ 13D
10-21  C N/A / P N/A ｜ Activity LOW ｜ 15D（新上架）

📆 10-09 Forward Structure
存量OI: C 91.0k / P 31.1k，今日变化ΔOI: C +2.2k / P +0.4k，平值价格ATM: C $1.39 / P $1.47 ｜ ATM IV 43.6%，净 delta 敞口 44k shares
Top ΔOI: C 92 +869 ｜ C 90 +435
仓位参考: Max Pain 87 ｜ Call Wall 88（+1.4%，弱）（OI 16.3k） ｜ Put Wall 82（-5.5%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 43.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 正 44,055 股

10-16（MEDIUM △）Top ΔOI: 81P +1,853 ｜ 88C +1,058
10-16（MEDIUM △）仓位参考: Max Pain 91 ｜ Call Wall 90（+3.7%，弱）（OI 8.5k） ｜ Put Wall 90（+3.7%，弱）（OI 10.5k）

10-19（Activity LOW）仓位参考: Max Pain 90 ｜ Put Wall 87（+0.2%，弱）（OI 10）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/GDX_morning.json