# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-16 162C ΔOI -5,424（距现价 -5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 158.99 → 收盘 171.09（+7.6%） ｜ 今日高 172.47 ｜ 低 158.62 ｜ 昨收 158.96 → 收盘 171.09（+7.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 1.01 | ATM IV 54.3% | Skew -2.5pp | Term 0.93 | ExpMove ±4.6%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.6% ｜ 10-12（7D）±5.2% ｜ 10-16（11D）±6.7% ｜ 10-19（14D）±7.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 111,935,937 | GEX Change vs 上次快照 5,714,537 | Flip: Primary Flip: 151.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 469 / LOW 68 / INVALID 483
结构观察区: Primary Flip 151.02（全链重定价，覆盖 99%）
Call Wall 160（弱结构｜现价高于该位 6.9%）
最近结构参考: Call Wall 160（现价高于该位 6.9%）
量化视角： 正 Gamma（1.12亿，无历史分位）｜正 Gamma 增强（+571万）｜现价位于 Flip 上方 13.29%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 172.5C — Vol 25,739 | 最新价 $8.07 | OI 507→21964 (ΔOI +21457张) | ΔOI/Volume 83.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21457张（+4232.1% vs前日OI），连续性待观察（方向未知）
10-09 160.0C — Vol 28,783 | 最新价 $11.95 | OI 8277→18082 (ΔOI +9805张) | ΔOI/Volume 34.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9805张（+118.5% vs前日OI），连续性待观察（方向未知）
10-09 150.0P — Vol 24,027 | 最新价 $0.15 | OI 4131→13294 (ΔOI +9163张) | ΔOI/Volume 38.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9163张（+221.8% vs前日OI），连续性待观察（方向未知）
10-09 155.0P — Vol 24,314 | 最新价 $0.27 | OI 1391→9959 (ΔOI +8568张) | ΔOI/Volume 35.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8568张（+616.0% vs前日OI），连续性待观察（方向未知）
10-09 157.5P — Vol 41,707 | 最新价 $0.40 | OI 471→7570 (ΔOI +7099张) | ΔOI/Volume 17.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7099张（+1507.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,092 张（Put 24,830 / Call 31,262），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +31.3k / P +55.5k ｜ Activity HIGH ｜ 4D
10-12  C N/A / P N/A ｜ Activity LOW ｜ 7D（新上架）
10-16  C -2.3k / P +12.8k ｜ Activity MEDIUM △ ｜ 11D
10-19  C N/A / P N/A ｜ Activity LOW ｜ 14D（新上架）

📆 10-09 Forward Structure
存量OI: C 129.3k / P 130.4k，今日变化ΔOI: C +31.3k / P +55.5k，平值价格ATM: C $4.50 / P $3.35 ｜ ATM IV 54.3%，净 delta 敞口 1.9M shares
Top ΔOI: C 160 +9,805 ｜ P 150 +9,163 ｜ P 155 +8,568
仓位参考: Max Pain 155 ｜ Call Wall 160（-6.5%，弱）（OI 18.1k） ｜ Put Wall 155（-9.4%，弱）（OI 10.0k）
量化解读： 存量两侧均衡｜ATM IV 54.3%｜历史 Rank 48%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,855,842 股

10-16（MEDIUM △）Top ΔOI: 162C -5,424 ｜ 170C +4,933
10-16（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 160（-6.5%，弱）（OI 39.7k） ｜ Put Wall 155（-9.4%，弱）（OI 12.1k）

📅 事件差分（观察，非因果）: 10-09（4D）ATM IV 54.3% vs 10-12 46.9%（差 +7.4pp）——覆盖 ISM 非制造业 PMI、美联储议息会议 Minutes 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SPCX_evening.json