# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.74 ｜ QQQ $721.45
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 16P ΔOI +31（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 16.97 → 今开 16.96（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 17.17 ｜ 低 15.83

Options: P/C成交量 0.32 | OI比 0.39 | ATM IV 108.4% | Skew -2.4pp | Term 0.73 | ExpMove ±11.5%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±11.5% ｜ 10-02（14D）±8.6% ｜ 10-09（21D）±18.7% ｜ 10-16（28D）±18.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -107,310 | GEX Change vs 上次快照 -1,467,904 | Flip: Primary Flip: 15.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 199 / LOW 96 / INVALID 155
结构观察区: Primary Flip 15.95（全链重定价，覆盖 86%）
Put Wall 15（现价高于该位 5.8%）
最近结构参考: Flip 16（现价低于该位 0.5%）
量化视角： 负 Gamma（11万，无历史分位）｜由正转负（147万）｜现价位于 Flip 下方 0.51%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 18.0C — Vol 1,240 | 最新价 $1.15 | OI 295→1429 (ΔOI +1134张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1134张（+384.4% vs前日OI），连续性待观察（方向未知）
09-18 18.0C — Vol 214 | 最新价 $0.05 | OI 440→644 (ΔOI +204张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增204张（+46.4% vs前日OI），连续性待观察（方向未知）
09-18 17.5C — Vol 224 | 最新价 $0.15 | OI 250→436 (ΔOI +186张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增186张（+74.4% vs前日OI），连续性待观察（方向未知）
09-18 17.0C — Vol 645 | 最新价 $0.35 | OI 481→624 (ΔOI +143张) | ΔOI/Volume 22.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增143张（+29.7% vs前日OI），连续性待观察（方向未知）
10-23 21.5C — Vol 341 | 最新价 $0.50 | OI 10→127 (ΔOI +117张) | ΔOI/Volume 34.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增117张（+1170.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,784 张（Put 0 / Call 1,784），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 9.7k / P 3.8k，今日成交量: C 1.4k / P 0.4k，平值价格ATM: C $1.07 / P $0.05 ｜ ATM IV 108.4%，预期波动 ±7.1%，Max Pain 18
Top ΔOI: C 18 +204 ｜ C 17 +186 ｜ C 17 +143

📆 Forward Expiration Structure

09-25  C +0.3k / P +0.1k ｜ Activity HIGH ｜ 7D
10-02  C +98 / P +44 ｜ Activity MEDIUM △ ｜ 14D
10-09  C +35 / P +15 ｜ Activity MEDIUM △ ｜ 21D
10-16  C +1.4k / P -0.2k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 5.5k / P 2.4k，今日变化ΔOI: C +0.3k / P +0.1k，平值价格ATM: C $1.44 / P $0.39 ｜ ATM IV 83.2%，净 delta 敞口 3k shares
仓位参考: Max Pain 18 ｜ Put Wall 15（-5.5%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 83.2%｜历史 Rank 48%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,107 股

10-02（MEDIUM △）Top ΔOI: 16P +31
10-02（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（-5.5%）（OI 0.2k）

10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+0.8%）（OI 0.1k）

📆 10-16 Forward Structure
存量OI: C 19.7k / P 6.0k，今日变化ΔOI: C +1.4k / P -0.2k，平值价格ATM: C $1.95 / P $1.04 ｜ ATM IV 78.8%，净 delta 敞口 69k shares
Top ΔOI: C 18 +1,134 ｜ P 34 -100
仓位参考: Max Pain 20 ｜ Put Wall 15（-5.5%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 78.8%｜历史 Rank 48%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 69,018 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NNE_morning.json