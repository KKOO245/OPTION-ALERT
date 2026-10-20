# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $768.68 ｜ QQQ $720.04
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 168.45 → 今开 166.06（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 172.49 ｜ 低 165.90

Options: P/C成交量 0.40 | OI比 0.67 | ATM IV 71.9% | Skew 0.0pp | Term 0.97 | ExpMove ±5.3%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 0.0pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±5.3% ｜ 10-30（10D）±11.0% ｜ 11-06（17D）±13.7% ｜ 11-13（24D）±15.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,103,215 | GEX Change vs 上次快照 2,967,337 | Flip: Primary Flip: 164.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 430 / LOW 125 / INVALID 287
结构观察区: Primary Flip 164.40（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 0.2%）
最近结构参考: Call Wall 170（现价低于该位 0.2%）
量化视角： 正 Gamma（710万，无历史分位）｜正 Gamma 增强（+297万）｜现价位于 Flip 上方 3.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 178（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 192.5C — Vol 2,691 | 最新价 $0.27 | OI 3175→5617 (ΔOI +2442张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2442张（+76.9% vs前日OI），连续性待观察（方向未知）
10-23 180.0C — Vol 2,541 | 最新价 $1.20 | OI 5901→7074 (ΔOI +1173张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1173张（+19.9% vs前日OI），连续性待观察（方向未知）
10-23 175.0C — Vol 1,387 | 最新价 $2.35 | OI 996→1546 (ΔOI +550张) | ΔOI/Volume 39.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增550张（+55.2% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 609 | 最新价 $1.15 | OI 461→976 (ΔOI +515张) | ΔOI/Volume 84.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增515张（+111.7% vs前日OI），连续性待观察（方向未知）
11-20 220.0C — Vol 947 | 最新价 $1.98 | OI 2860→3373 (ΔOI +513张) | ΔOI/Volume 54.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增513张（+17.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,193 张（Put 515 / Call 4,678），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +6.5k / P +2.9k ｜ Activity MEDIUM △ ｜ 3D
10-30  C +1.7k / P +1.1k ｜ Activity MEDIUM △ ｜ 10D
11-06  C +0.7k / P +51 ｜ Activity MEDIUM △ ｜ 17D
11-13  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 60.5k / P 40.7k，今日变化ΔOI: C +6.5k / P +2.9k，平值价格ATM: C $4.45 / P $4.60 ｜ ATM IV 71.9%，净 delta 敞口 108k shares
Top ΔOI: C 192 +2,442 ｜ C 180 +1,173
仓位参考: Max Pain 178 ｜ Call Wall 180（+6.0%，弱）（OI 7.1k）
量化解读： 存量 Call 重｜ATM IV 71.9%｜历史 Rank 38%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 108,159 股

10-30（MEDIUM △）Top ΔOI: 140P +515 ｜ 150P +457
10-30（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 185（+9.0%，弱）（OI 1.8k） ｜ Put Wall 160（-5.7%，弱）（OI 0.9k）

11-06（MEDIUM △）Top ΔOI: 175C +97
11-06（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+3.1%，弱）（OI 0.3k）

11-13（MEDIUM △）Top ΔOI: 170P +231
11-13（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 177.5（+4.6%）（OI 1.1k） ｜ Put Wall 170（+0.2%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/COIN_morning.json