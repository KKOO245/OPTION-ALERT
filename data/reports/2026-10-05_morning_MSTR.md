# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.78 ｜ QQQ $756.20
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
🟡 **近现价集中开仓**: 10-09 167C ΔOI +17,104（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 160.01 → 今开 164.68（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 166.20 ｜ 低 161.37

Options: P/C成交量 0.58 | OI比 0.75 | ATM IV 68.3% | Skew -5.2pp | Term 0.99 | ExpMove ±6.0%（近端） | Rank 25%
量化视角： IV 中性（Rank 25%）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -5.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±6.0% ｜ 10-16（11D）±8.9% ｜ 10-23（18D）±11.1% ｜ 10-30（25D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 71,187,475 | GEX Change vs 上次快照 54,140,968 | Flip: Primary Flip: 145.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 661 / LOW 91 / INVALID 180
结构观察区: Primary Flip 145.80（全链重定价，覆盖 100%）
最近结构参考: Flip 146（现价高于该位 12.3%）
量化视角： 正 Gamma（7119万，无历史分位）｜正 Gamma 增强（+5414万）｜现价位于 Flip 上方 12.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 95.0P — Vol 33,352 | 最新价 $0.04 | OI 4442→36356 (ΔOI +31914张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31914张（+718.5% vs前日OI），连续性待观察（方向未知）
10-09 175.0C — Vol 24,358 | 最新价 $1.14 | OI 1960→19361 (ΔOI +17401张) | ΔOI/Volume 71.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17401张（+887.8% vs前日OI），连续性待观察（方向未知）
10-09 167.5C — Vol 20,637 | 最新价 $2.43 | OI 975→18079 (ΔOI +17104张) | ΔOI/Volume 82.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17104张（+1754.3% vs前日OI），连续性待观察（方向未知）
10-09 172.5C — Vol 22,071 | 最新价 $1.49 | OI 4518→21591 (ΔOI +17073张) | ΔOI/Volume 77.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17073张（+377.9% vs前日OI），连续性待观察（方向未知）
10-09 165.0C — Vol 28,800 | 最新价 $3.15 | OI 8085→24569 (ΔOI +16484张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16484张（+203.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 99,976 张（Put 31,914 / Call 68,062），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +136.9k / P +76.8k ｜ Activity HIGH ｜ 4D
10-16  C -2.5k / P +8.3k ｜ Activity HIGH ｜ 11D
10-23  C -2.0k / P +2.6k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +4.1k / P +2.7k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 202.0k / P 150.6k，今日变化ΔOI: C +136.9k / P +76.8k，平值价格ATM: C $5.60 / P $4.18 ｜ ATM IV 68.3%，净 delta 敞口 4.7M shares
Top ΔOI: P 95 +31,914 ｜ C 175 +17,401 ｜ C 167 +17,104
仓位参考: Max Pain 152 ｜ Call Wall 165（+0.8%，弱）（OI 24.6k）
量化解读： 存量 Call 重｜ATM IV 68.3%｜历史 Rank 25%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,733,992 股

📆 10-16 Forward Structure
存量OI: C 176.8k / P 162.1k，今日变化ΔOI: C -2.5k / P +8.3k，平值价格ATM: C $7.98 / P $6.55 ｜ ATM IV 63.2%，净 delta 敞口 -340k shares
Top ΔOI: C 95 -3,146
仓位参考: Max Pain 130 ｜ Call Wall 155（-5.3%，弱）（OI 10.4k） ｜ Put Wall 150（-8.4%，弱）（OI 5.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 63.2%｜历史 Rank 25%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 339,578 股

10-23（MEDIUM △）Top ΔOI: 172C -3,218
10-23（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 172.5（+5.3%，弱）（OI 2.5k） ｜ Put Wall 155（-5.3%，弱）（OI 3.0k）

📆 10-30 Forward Structure
存量OI: C 19.7k / P 25.4k，今日变化ΔOI: C +4.1k / P +2.7k，平值价格ATM: C $12.20 / P $10.20 ｜ ATM IV 63.9%，净 delta 敞口 144k shares
Top ΔOI: C 162 +2,367 ｜ C 175 +368
仓位参考: Max Pain 160 ｜ Call Wall 162.5（-0.8%，弱）（OI 2.5k） ｜ Put Wall 160（-2.3%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.9%｜历史 Rank 25%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 144,466 股

📅 事件差分（观察，非因果）: 10-09（4D）ATM IV 68.3% vs 10-16 63.2%（差 +5.1pp）——覆盖 ISM 非制造业 PMI、美联储议息会议 Minutes 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/MSTR_morning.json