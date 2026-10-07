# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 50C ΔOI +765（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 56C ΔOI +822 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 46.84 → 今开 47.40（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 48.65 ｜ 低 47.30

Options: P/C成交量 0.75 | OI比 0.84 | ATM IV 62.2% | Skew -4.7pp | Term 0.93 | ExpMove ±4.6%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.6% ｜ 10-16（10D）±7.3% ｜ 10-23（17D）±9.0% ｜ 10-30（24D）±12.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -30,253 | GEX Change vs 上次快照 3,036,023 | Flip: Primary Flip: 48.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 264 / LOW 55 / INVALID 117
结构观察区: Primary Flip 48.19（全链重定价，覆盖 97%）
Put Wall 45（现价高于该位 7.1%） | Call Wall 50（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 48（现价低于该位 0.0%）
量化视角： 负 Gamma（3万，无历史分位）｜负 Gamma 缓解（+304万）｜现价位于 Flip 下方 0.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall） / 48（MaxPain，仅结算参考）；上方 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 56.0C — Vol 868 | 最新价 $0.46 | OI 260→1082 (ΔOI +822张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增822张（+316.1% vs前日OI），连续性待观察（方向未知）
10-09 45.5P — Vol 842 | 最新价 $0.52 | OI 380→1189 (ΔOI +809张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增809张（+212.9% vs前日OI），连续性待观察（方向未知）
10-09 50.0C — Vol 1,168 | 最新价 $0.27 | OI 1006→1771 (ΔOI +765张) | ΔOI/Volume 65.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增765张（+76.0% vs前日OI），连续性待观察（方向未知）
10-09 45.0P — Vol 717 | 最新价 $0.38 | OI 585→1207 (ΔOI +622张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增622张（+106.3% vs前日OI），连续性待观察（方向未知）
10-09 51.0C — Vol 899 | 最新价 $0.14 | OI 239→743 (ΔOI +504张) | ΔOI/Volume 56.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增504张（+210.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,522 张（Put 1,431 / Call 2,091），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +2.5k / P +2.2k ｜ Activity HIGH ｜ 3D
10-16  C +0.3k / P +32 ｜ Activity MEDIUM △ ｜ 10D
10-23  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 17D
10-30  C +1.3k / P +48 ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 10.9k / P 9.2k，今日变化ΔOI: C +2.5k / P +2.2k，平值价格ATM: C $1.34 / P $0.88 ｜ ATM IV 62.2%，净 delta 敞口 57k shares
Top ΔOI: P 45 +809 ｜ C 50 +765 ｜ P 45 +622
仓位参考: Max Pain 48 ｜ Call Wall 50（+3.8%，弱）（OI 1.8k） ｜ Put Wall 47（-2.4%）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 62.2%｜历史 Rank 40%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,477 股

10-16（MEDIUM △）Top ΔOI: 52C +90
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+3.8%，弱）（OI 4.0k） ｜ Put Wall 45（-6.6%，弱）（OI 4.4k）

10-23（MEDIUM △）仓位参考: Max Pain 51 ｜ Call Wall 50（+3.8%，弱）（OI 0.2k） ｜ Put Wall 45（-6.6%，弱）（OI 0.2k）

📆 10-30 Forward Structure
存量OI: C 4.3k / P 2.1k，今日变化ΔOI: C +1.3k / P +48，平值价格ATM: C $2.59 / P $3.25 ｜ ATM IV 58.6%，净 delta 敞口 33k shares
Top ΔOI: C 49 +242
仓位参考: Max Pain 49 ｜ Call Wall 49（+1.7%，弱）（OI 0.3k） ｜ Put Wall 45（-6.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 58.6%｜历史 Rank 40%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 33,168 股

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 62.2% vs 10-16 56.1%（差 +6.1pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/MP_morning.json