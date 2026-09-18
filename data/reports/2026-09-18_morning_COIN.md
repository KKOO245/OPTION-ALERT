# 期权晨报 2026-09-18（快照 10:20 ET）

📊 市场环境

SPY $758.97 ｜ QQQ $716.72
VIX 15.53 ↑0.6%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 177C ΔOI +2,349（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 173.97 → 今开 178.15（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 188.71 ｜ 低 177.67

Options: P/C成交量 0.28 | OI比 0.51 | ATM IV 109.3% | Skew -9.5pp | Term 0.58 | ExpMove ±7.3%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±7.3% ｜ 10-02（14D）±9.9% ｜ 10-09（21D）±12.8% ｜ 10-16（28D）±14.3%
   ⇒ IV–VIX Spread: +93.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,997,037 | GEX Change vs 上次快照 21,214,699 | Flip: Primary Flip: 167.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 462 / LOW 130 / INVALID 400
结构观察区: Primary Flip 167.51（全链重定价，覆盖 95%）
Call Wall 200（弱结构｜现价低于该位 7.2%）
最近结构参考: Call Wall 200（现价低于该位 7.2%）
量化视角： 正 Gamma（3700万，无历史分位）｜正 Gamma 增强（+2121万）｜现价位于 Flip 上方 10.83%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 172（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 177.5C — Vol 52 | 最新价 $7.92 | OI 445→2794 (ΔOI +2349张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2349张（+527.9% vs前日OI），连续性待观察（方向未知）
09-25 185.0C — Vol 150 | 最新价 $4.60 | OI 2372→4337 (ΔOI +1965张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1965张（+82.8% vs前日OI），连续性待观察（方向未知）
09-25 175.0C — Vol 205 | 最新价 $9.70 | OI 593→1916 (ΔOI +1323张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1323张（+223.1% vs前日OI），连续性待观察（方向未知）
09-18 200.0C — Vol 292 | 最新价 $0.03 | OI 7652→8846 (ΔOI +1194张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1194张（+15.6% vs前日OI），值得跟踪（方向未知）
09-25 182.5C — Vol 489 | 最新价 $5.80 | OI 398→1472 (ΔOI +1074张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1074张（+269.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,905 张（Put 0 / Call 7,905），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 227.8k / P 117.0k，今日成交量: C 52.9k / P 14.6k，平值价格ATM: C $2.35 / P $2.02 ｜ ATM IV 109.3%，预期波动 ±2.4%，Max Pain 172
Top ΔOI: C 200 +1,194 ｜ P 150 -892 ｜ P 167 +752

📆 Forward Expiration Structure

09-25  C +8.5k / P +2.1k ｜ Activity HIGH ｜ 7D
10-02  C +1.4k / P +0.9k ｜ Activity HIGH ｜ 14D
10-09  C +0.5k / P +45 ｜ Activity MEDIUM △ ｜ 21D
10-16  C +0.7k / P +1.1k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 31.7k / P 20.5k，今日变化ΔOI: C +8.5k / P +2.1k，平值价格ATM: C $6.85 / P $6.65 ｜ ATM IV 62.9%，净 delta 敞口 497k shares
Top ΔOI: C 177 +2,349 ｜ C 185 +1,965 ｜ C 175 +1,323
仓位参考: Max Pain 172 ｜ Call Wall 185（-0.4%）（OI 4.3k） ｜ Put Wall 170（-8.4%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 62.9%｜历史 Rank 90%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 正 496,812 股

📆 10-02 Forward Structure
存量OI: C 13.6k / P 18.0k，今日变化ΔOI: C +1.4k / P +0.9k，平值价格ATM: C $9.33 / P $9.05 ｜ ATM IV 62.7%，净 delta 敞口 73k shares
Top ΔOI: C 175 +202 ｜ C 190 +201
仓位参考: Max Pain 182 ｜ Call Wall 187.5（+1.0%，弱）（OI 1.3k） ｜ Put Wall 172.5（-7.1%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.7%｜历史 Rank 90%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 正 73,063 股

10-09（MEDIUM △）Top ΔOI: 180C +133 ｜ 182C +50
10-09（MEDIUM △）仓位参考: Max Pain 182 ｜ Call Wall 185（-0.4%，弱）（OI 0.2k） ｜ Put Wall 187.5（+1.0%，弱）（OI 0.4k）

📆 10-16 Forward Structure
存量OI: C 61.9k / P 53.4k，今日变化ΔOI: C +0.7k / P +1.1k，平值价格ATM: C $14.10 / P $12.45 ｜ ATM IV 63.5%，净 delta 敞口 6k shares
Top ΔOI: C 195 +292 ｜ P 155 +218
仓位参考: Max Pain 170 ｜ Call Wall 200（+7.7%，弱）（OI 5.5k） ｜ Put Wall 200（+7.7%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 63.5%｜历史 Rank 90%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 正 6,144 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/COIN_morning.json