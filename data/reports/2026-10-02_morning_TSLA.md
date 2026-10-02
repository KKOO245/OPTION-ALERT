# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-05 377C ΔOI -7,933（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 420C ΔOI +9,983 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 354.11 → 今开 360.08（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 373.54 ｜ 低 359.41

Options: P/C成交量 0.50 | OI比 0.98 | ATM IV 62.0% | Skew 0.5pp | Term 0.72 | ExpMove ±2.4%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-05（3D）±2.4% ｜ 10-07（5D）±3.6% ｜ 10-09（7D）±4.3% ｜ 10-12（10D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 179,830,273 | GEX Change vs 上次快照 129,666,768 | Flip: Primary Flip: 349.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 993 / LOW 201 / INVALID 666
结构观察区: Primary Flip 349.03（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 7.3%）
最近结构参考: Flip 349（现价高于该位 6.3%）
量化视角： 正 Gamma（1.80亿，无历史分位）｜正 Gamma 增强（+1.30亿）｜现价位于 Flip 上方 6.29%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 358（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 349（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 150.0P — Vol 18,453 | 最新价 $0.01 | OI 422→18544 (ΔOI +18122张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18122张（+4294.3% vs前日OI），连续性待观察（方向未知）
10-05 420.0C — Vol 10,070 | 最新价 $0.08 | OI 6537→16520 (ΔOI +9983张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9983张（+152.7% vs前日OI），连续性待观察（方向未知）
10-02 365.0C — Vol 69,175 | 最新价 $1.17 | OI 11966→18024 (ΔOI +6058张) | ΔOI/Volume 8.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6058张（+50.6% vs前日OI），连续性待观察（方向未知）
10-09 375.0C — Vol 10,486 | 最新价 $2.20 | OI 3550→7781 (ΔOI +4231张) | ΔOI/Volume 40.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4231张（+119.2% vs前日OI），连续性待观察（方向未知）
10-09 362.5C — Vol 5,769 | 最新价 $5.20 | OI 926→4943 (ΔOI +4017张) | ΔOI/Volume 69.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4017张（+433.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 42,411 张（Put 18,122 / Call 24,289），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 285.6k / P 279.5k，今日成交量: C 377.7k / P 187.5k，平值价格ATM: C $3.20 / P $1.90 ｜ ATM IV 62.0%，预期波动 ±1.4%，Max Pain 358
Top ΔOI: C 365 +6,058 ｜ C 377 -5,232 ｜ C 390 -3,804

📆 Forward Expiration Structure

10-05  C +12.8k / P +5.4k ｜ Activity HIGH ｜ 3D
10-07  C +2.7k / P +2.1k ｜ Activity HIGH ｜ 5D
10-09  C +18.8k / P +24.7k ｜ Activity HIGH ｜ 7D
10-12  C +1.0k / P +3.0k ｜ Activity HIGH ｜ 10D

📆 10-05 Forward Structure
存量OI: C 69.7k / P 29.7k，今日变化ΔOI: C +12.8k / P +5.4k，平值价格ATM: C $5.13 / P $3.77 ｜ ATM IV 31.6%，净 delta 敞口 157k shares
Top ΔOI: C 420 +9,983 ｜ C 377 -7,933
仓位参考: Max Pain 355 ｜ Call Wall 377.5（+1.8%，弱）（OI 7.8k） ｜ Put Wall 350（-5.7%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 31.6%｜历史 Rank 74%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 157,055 股

📆 10-07 Forward Structure
存量OI: C 14.3k / P 7.5k，今日变化ΔOI: C +2.7k / P +2.1k，平值价格ATM: C $7.33 / P $5.90 ｜ ATM IV 36.8%，净 delta 敞口 123k shares
Top ΔOI: C 370 +514 ｜ C 357 +476 ｜ P 357 +328
仓位参考: Max Pain 355 ｜ Call Wall 370（-0.3%，弱）（OI 1.4k） ｜ Put Wall 347.5（-6.3%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 36.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 123,173 股

📆 10-09 Forward Structure
存量OI: C 90.6k / P 83.7k，今日变化ΔOI: C +18.8k / P +24.7k，平值价格ATM: C $8.85 / P $7.15 ｜ ATM IV 38.3%，净 delta 敞口 719k shares
Top ΔOI: C 375 +4,231 ｜ C 362 +4,017
仓位参考: Max Pain 355 ｜ Call Wall 375（+1.1%，弱）（OI 7.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.3%｜历史 Rank 74%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 718,945 股

📆 10-12 Forward Structure
存量OI: C 6.0k / P 5.1k，今日变化ΔOI: C +1.0k / P +3.0k，平值价格ATM: C $9.80 / P $7.87 ｜ ATM IV 35.8%，净 delta 敞口 33k shares
Top ΔOI: P 320 +2,136 ｜ C 360 +133
仓位参考: Max Pain 352 ｜ Call Wall 370（-0.3%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 正 32,603 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/TSLA_morning.json