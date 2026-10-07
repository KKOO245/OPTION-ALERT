# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.04 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 148P ΔOI +1,281（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 150.90 → 今开 149.37（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 151.30 ｜ 低 148.64

Options: P/C成交量 N/A | OI比 2.37 | ATM IV N/A | Skew N/A | Term N/A | ExpMove ±2.8%（近端） | Rank — (历史不足)
量化视角： 存量 OI 比 2.37——观察点，非方向信号
   ⇒ Put/Call Volume: 数据不足 → 方向 Unknown
   ⇒ Put/Call OI: 2.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.8% ｜ 10-16（9D）±4.5% ｜ 10-23（16D）±6.1% ｜ 10-30（23D）±3.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: MIXED（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 0%（带内） ｜ IV 有效性: VALID 0 / LOW 0 / INVALID 740
结构观察区: NO_CROSS
Put Wall 150（现价高于该位 0.5%）
最近结构参考: Put Wall 150（现价高于该位 0.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 155（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 155.0C — Vol 1,893 | 最新价 $1.55 | OI 1161→2724 (ΔOI +1563张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1563张（+134.6% vs前日OI），连续性待观察（方向未知）
10-09 148.0P — Vol 1,649 | 最新价 $0.97 | OI 3251→4532 (ΔOI +1281张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1281张（+39.4% vs前日OI），连续性待观察（方向未知）
10-16 145.0C — Vol 1,038 | 最新价 $6.90 | OI 29→1004 (ΔOI +975张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增975张（+3362.1% vs前日OI），连续性待观察（方向未知）
10-09 150.0P — Vol 970 | 最新价 $1.44 | OI 455→942 (ΔOI +487张) | ΔOI/Volume 50.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增487张（+107.0% vs前日OI），连续性待观察（方向未知）
10-09 158.0C — Vol 976 | 最新价 $0.18 | OI 272→630 (ΔOI +358张) | ΔOI/Volume 36.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增358张（+131.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,664 张（Put 1,768 / Call 2,896），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.3k / P +2.3k ｜ Activity HIGH ｜ 2D
10-16  C +2.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 9D
10-23  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 16D
10-30  C +0.2k / P +27 ｜ Activity MEDIUM △ ｜ 23D

📆 10-09 Forward Structure
存量OI: C 5.5k / P 13.1k，今日变化ΔOI: C +1.3k / P +2.3k，平值价格ATM: C $1.95 / P $2.19 ｜ ATM IV 0.0%，净 delta 敞口 0 shares
Top ΔOI: P 148 +1,281 ｜ P 150 +487 ｜ C 158 +358
仓位参考: Max Pain 155 ｜ Call Wall 145（-3.8%）（OI 1.0k） ｜ Put Wall 148（-1.8%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜净 delta 敞口 正 0 股

10-16（MEDIUM △）Top ΔOI: 155C +1,563 ｜ 145C +975
10-16（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 155（+2.8%，弱）（OI 2.7k） ｜ Put Wall 150（-0.5%）（OI 22.6k）

10-23（MEDIUM △）Top ΔOI: 149P +107 ｜ 156C +49
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 154（+2.2%，弱）（OI 89） ｜ Put Wall 153（+1.5%，弱）（OI 0.4k）

10-30（MEDIUM △）Top ΔOI: 140P -612 ｜ 149P +347
10-30（MEDIUM △）仓位参考: Max Pain 154 ｜ Call Wall 159（+5.5%，弱）（OI 0.4k） ｜ Put Wall 150（-0.5%，弱）（OI 7.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime MIXED（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/XBI_morning.json