# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $nan
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
🟡 **近现价集中开仓**: 10-09 160C ΔOI +9,805（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 158.96 → 今开 158.99（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 166.75 ｜ 低 158.62

Options: P/C成交量 0.55 | OI比 1.01 | ATM IV 52.6% | Skew -1.6pp | Term 0.95 | ExpMove ±4.5%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.5% ｜ 10-12（7D）±5.0% ｜ 10-16（11D）±6.5% ｜ 10-19（14D）±7.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 106,221,400 | GEX Change vs 上次快照 30,581,906 | Flip: Primary Flip: 150.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 475 / LOW 67 / INVALID 478
结构观察区: Primary Flip 150.99（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价高于该位 3.6%）
最近结构参考: Call Wall 160（现价高于该位 3.6%）
量化视角： 正 Gamma（1.06亿，无历史分位）｜正 Gamma 增强（+3058万）｜现价位于 Flip 上方 9.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 172.5C — Vol 29,763 | 最新价 $3.20 | OI 507→21964 (ΔOI +21457张) | ΔOI/Volume 72.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21457张（+4232.1% vs前日OI），连续性待观察（方向未知）
10-09 160.0C — Vol 45,904 | 最新价 $3.15 | OI 8277→18082 (ΔOI +9805张) | ΔOI/Volume 21.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9805张（+118.5% vs前日OI），连续性待观察（方向未知）
10-09 150.0P — Vol 29,755 | 最新价 $0.76 | OI 4131→13294 (ΔOI +9163张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9163张（+221.8% vs前日OI），连续性待观察（方向未知）
10-09 155.0P — Vol 28,935 | 最新价 $1.90 | OI 1391→9959 (ΔOI +8568张) | ΔOI/Volume 29.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8568张（+616.0% vs前日OI），连续性待观察（方向未知）
10-09 157.5P — Vol 19,602 | 最新价 $2.83 | OI 471→7570 (ΔOI +7099张) | ΔOI/Volume 36.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7099张（+1507.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,092 张（Put 24,830 / Call 31,262），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +31.3k / P +55.5k ｜ Activity HIGH ｜ 4D
10-12  C N/A / P N/A ｜ Activity LOW ｜ 7D（新上架）
10-16  C -2.3k / P +12.8k ｜ Activity HIGH ｜ 11D
10-19  C N/A / P N/A ｜ Activity LOW ｜ 14D（新上架）

📆 10-09 Forward Structure
存量OI: C 129.3k / P 130.4k，今日变化ΔOI: C +31.3k / P +55.5k，平值价格ATM: C $4.01 / P $3.45 ｜ ATM IV 52.6%，净 delta 敞口 1.1M shares
Top ΔOI: C 160 +9,805 ｜ P 150 +9,163 ｜ P 155 +8,568
仓位参考: Max Pain 155 ｜ Call Wall 160（-3.5%，弱）（OI 18.1k） ｜ Put Wall 150（-9.5%，弱）（OI 13.3k）
量化解读： 存量两侧均衡｜ATM IV 52.6%｜历史 Rank 38%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,065,184 股

📆 10-16 Forward Structure
存量OI: C 343.5k / P 354.7k，今日变化ΔOI: C -2.3k / P +12.8k，平值价格ATM: C $5.71 / P $5.10 ｜ ATM IV 46.6%，净 delta 敞口 -710k shares
Top ΔOI: C 162 -5,424 ｜ C 170 +4,933
仓位参考: Max Pain 145 ｜ Call Wall 160（-3.5%，弱）（OI 39.7k） ｜ Put Wall 150（-9.5%，弱）（OI 20.5k）
量化解读： 存量两侧均衡｜ATM IV 46.6%｜历史 Rank 38%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 710,087 股

📅 事件差分（观察，非因果）: 10-09（4D）ATM IV 52.6% vs 10-12 45.0%（差 +7.7pp）——覆盖 ISM 非制造业 PMI、美联储议息会议 Minutes 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SPCX_morning.json