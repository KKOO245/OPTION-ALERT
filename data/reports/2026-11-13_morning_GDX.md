# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.60
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 79P ΔOI +788（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 79P ΔOI +788 占该期限总 OI 12.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 81.84 → 今开 81.90（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 82.89 ｜ 低 81.65

Options: P/C成交量 1.65 | OI比 0.57 | ATM IV 61.3% | Skew 3.0pp | Term 0.69 | ExpMove ±2.7%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 3.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.57）+ 当日成交偏 Put（P/C量 1.65）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.65×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±2.7% ｜ 11-18（5D）±4.1% ｜ 11-20（7D）±4.8% ｜ 11-23（10D）±5.7%
   ⇒ IV–VIX Spread: +41.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -22,534,245 | GEX Change vs 上次快照 25,299,670 | Flip: Primary Flip: 83.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 584 / LOW 231 / INVALID 443
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 83.28（全链重定价，覆盖 89%）
最近结构参考: Flip 83（现价低于该位 1.3%）
量化视角： 负 Gamma（2253万，无历史分位）｜负 Gamma 缓解（+2530万）｜现价位于 Flip 下方 1.32%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 83（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 83（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 87.0C — Vol 13,415 | 最新价 $0.48 | OI 1959→12414 (ΔOI +10455张) | ΔOI/Volume 77.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10455张（+533.7% vs前日OI），连续性待观察（方向未知）
11-20 84.0C — Vol 10,258 | 最新价 $1.25 | OI 8476→17690 (ΔOI +9214张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9214张（+108.7% vs前日OI），连续性待观察（方向未知）
11-20 88.0C — Vol 5,148 | 最新价 $0.37 | OI 1308→6216 (ΔOI +4908张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4908张（+375.2% vs前日OI），连续性待观察（方向未知）
11-20 85.0C — Vol 6,394 | 最新价 $1.09 | OI 3246→7501 (ΔOI +4255张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4255张（+131.1% vs前日OI），连续性待观察（方向未知）
12-18 100.0C — Vol 1,155 | 最新价 $0.47 | OI 41422→44813 (ΔOI +3391张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增3391张（+8.2% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,223 张（Put 0 / Call 32,223），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 75.3k / P 43.2k，今日成交量: C 2.9k / P 4.8k，平值价格ATM: C $0.60 / P $0.48 ｜ ATM IV 61.3%，预期波动 ±1.3%，Max Pain 83
Top ΔOI: C 92 -4,754 ｜ C 89 -4,418 ｜ P 80 +2,477

📆 Forward Expiration Structure

11-16  C +0.8k / P +0.8k ｜ Activity HIGH ｜ 3D
11-18  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 5D
11-20  C +33.7k / P -0.4k ｜ Activity HIGH ｜ 7D
11-23  C +28 / P +90 ｜ Activity MEDIUM △ ｜ 10D

📆 11-16 Forward Structure
存量OI: C 3.3k / P 2.9k，今日变化ΔOI: C +0.8k / P +0.8k，平值价格ATM: C $1.20 / P $1.05 ｜ ATM IV 34.5%，净 delta 敞口 11k shares
Top ΔOI: P 79 +788 ｜ C 87 +528 ｜ P 80 +103
仓位参考: Max Pain 85 ｜ Call Wall 87（+5.9%，弱）（OI 1.0k） ｜ Put Wall 79（-3.9%）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.5%｜历史 Rank 94%（近端代理）｜IV/RV 0.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,690 股

11-18（MEDIUM △）Top ΔOI: 80P +153 ｜ 87C +94
11-18（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 87（+5.9%，弱）（OI 0.2k） ｜ Put Wall 84（+2.2%，弱）（OI 0.2k）

📆 11-20 Forward Structure
存量OI: C 135.1k / P 170.4k，今日变化ΔOI: C +33.7k / P -0.4k，平值价格ATM: C $2.36 / P $1.60 ｜ ATM IV 42.1%，净 delta 敞口 1.0M shares
Top ΔOI: C 87 +10,455 ｜ C 84 +9,214 ｜ C 88 +4,908
仓位参考: Max Pain 85 ｜ Call Wall 84（+2.2%，弱）（OI 17.7k） ｜ Put Wall 80（-2.7%，弱）（OI 24.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.1%｜历史 Rank 94%（近端代理）｜IV/RV 0.74×（近似）｜净 delta 敞口 正 1,004,213 股

11-23（MEDIUM △）Top ΔOI: 83P +29 ｜ 78P +22
11-23（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 83（+1.0%，弱）（OI 24） ｜ Put Wall 83（+1.0%，弱）（OI 33）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/GDX_morning.json