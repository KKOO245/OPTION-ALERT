# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.77
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 439.89 → 今开 443.69（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 448.77 ｜ 低 441.00

Options: P/C成交量 0.00 | OI比 0.78 | ATM IV N/A | Skew N/A | Term N/A | ExpMove ±2.7%（近端） | Rank — (历史不足)
量化视角： 存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.00×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±2.7% ｜ 11-27（14D）±3.2% ｜ 12-04（21D）±5.3% ｜ 12-11（28D）±6.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: MIXED（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 0%（带内） ｜ IV 有效性: VALID 0 / LOW 0 / INVALID 1010
结构观察区: NO_CROSS
Call Wall 480（弱结构｜现价低于该位 6.8%）
最近结构参考: Call Wall 480（现价低于该位 6.8%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 450.0C — Vol 87 | 最新价 $0.82 | OI 66→134 (ΔOI +68张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增68张（+103.0% vs前日OI），连续性待观察（方向未知）
11-13 452.5C — Vol 54 | 最新价 $0.55 | OI 4→58 (ΔOI +54张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+1350.0% vs前日OI），连续性待观察（方向未知）
11-20 460.0C — Vol 49 | 最新价 $2.10 | OI 234→260 (ΔOI +26张) | ΔOI/Volume 53.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增26张（+11.1% vs前日OI），值得跟踪（方向未知）
12-18 460.0C — Vol 29 | 最新价 $11.40 | OI 371→393 (ΔOI +22张) | ΔOI/Volume 75.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增22张（+5.9% vs前日OI），值得跟踪（方向未知）
12-18 480.0C — Vol 28 | 最新价 $5.90 | OI 1384→1406 (ΔOI +22张) | ΔOI/Volume 78.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增22张（+1.6% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 192 张（Put 0 / Call 192），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 1.8k / P 1.4k，今日成交量: C 89 / P 0，平值价格ATM: C $1.55 / P $6.00，预期波动 ±1.7%，Max Pain 435
Top ΔOI: P 462 -144 ｜ C 450 +68 ｜ C 452 +54

📆 Forward Expiration Structure

11-20  C +11 / P -11 ｜ Activity MEDIUM △ ｜ 7D
11-27  C +23 / P +3 ｜ Activity LOW ｜ 14D
12-04  C +6 / P +4 ｜ Activity MEDIUM △ ｜ 21D
12-11  C +2 / P +7 ｜ Activity LOW ｜ 28D

📆 11-20 Forward Structure
存量OI: C 10.4k / P 10.4k，今日变化ΔOI: C +11 / P -11，平值价格ATM: C $6.20 / P $5.80 ｜ ATM IV 0.0%，净 delta 敞口 0 shares
Top ΔOI: C 460 +26 ｜ C 480 -26 ｜ P 460 -17
仓位参考: Max Pain 410 ｜ Call Wall 420（-6.1%，弱）（OI 0.8k） ｜ Put Wall 410（-8.3%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 430（-3.8%，弱）（OI 64） ｜ Put Wall 410（-8.3%，弱）（OI 42）

12-04（MEDIUM △）Top ΔOI: 430P +3 ｜ 450C +2
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 475（+6.2%，弱）（OI 82） ｜ Put Wall 405（-9.4%，弱）（OI 25）

12-11（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 450（+0.6%）（OI 0.1k） ｜ Put Wall 435（-2.7%）（OI 22）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/ISRG_morning.json