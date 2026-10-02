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
🟡 **近现价集中开仓**: 10-09 85P ΔOI +3,875（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 82P ΔOI +6,182 占该期限总 OI 14.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 86.74 → 今开 88.15（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 88.69 ｜ 低 87.73

Options: P/C成交量 0.88 | OI比 0.54 | ATM IV 56.2% | Skew 2.0pp | Term 0.71 | ExpMove ±4.3%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价中性（Skew 2.0pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±4.3% ｜ 10-16（14D）±6.2% ｜ 10-23（21D）±7.2% ｜ 10-30（28D）±8.6%
   ⇒ IV–VIX Spread: +40.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,080,176 | GEX Change vs 上次快照 32,543,991 | Flip: Primary Flip: 89.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 396 / LOW 139 / INVALID 329
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 89.49（全链重定价，覆盖 86%）
Put Wall 90（弱结构｜现价低于该位 1.7%）
最近结构参考: Flip 89（现价低于该位 1.1%）
量化视角： 负 Gamma（1208万，无历史分位）｜负 Gamma 缓解（+3254万）｜现价位于 Flip 下方 1.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 90（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 89（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 82.0P — Vol 6,196 | 最新价 $0.42 | OI 93→6275 (ΔOI +6182张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6182张（+6647.3% vs前日OI），连续性待观察（方向未知）
10-09 85.0P — Vol 3,992 | 最新价 $1.15 | OI 1751→5626 (ΔOI +3875张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3875张（+221.3% vs前日OI），连续性待观察（方向未知）
10-09 90.0C — Vol 3,503 | 最新价 $0.89 | OI 355→3462 (ΔOI +3107张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3107张（+875.2% vs前日OI），连续性待观察（方向未知）
10-16 85.0P — Vol 3,453 | 最新价 $1.85 | OI 5683→8502 (ΔOI +2819张) | ΔOI/Volume 81.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2819张（+49.6% vs前日OI），连续性待观察（方向未知）
10-02 89.0C — Vol 3,359 | 最新价 $0.16 | OI 495→2757 (ΔOI +2262张) | ΔOI/Volume 67.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2262张（+457.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,245 张（Put 12,876 / Call 5,369），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 78.2k / P 42.6k，今日成交量: C 2.8k / P 2.5k，平值价格ATM: C $0.58 / P $0.52 ｜ ATM IV 56.2%，预期波动 ±1.2%，Max Pain 90
Top ΔOI: C 94 -12,221 ｜ C 97 -8,234 ｜ P 97 -6,327

📆 Forward Expiration Structure

10-09  C +5.7k / P +11.1k ｜ Activity HIGH ｜ 7D
10-16  C +1.8k / P +2.5k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.2k / P +0.2k ｜ Activity LOW ｜ 21D
10-30  C +0.2k / P +37 ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 15.6k / P 28.7k，今日变化ΔOI: C +5.7k / P +11.1k，平值价格ATM: C $1.75 / P $2.05 ｜ ATM IV 39.5%，净 delta 敞口 65k shares
Top ΔOI: P 82 +6,182 ｜ P 85 +3,875 ｜ C 90 +3,107
仓位参考: Max Pain 90 ｜ Call Wall 90（+1.7%）（OI 3.5k） ｜ Put Wall 85（-4.0%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 39.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 65,258 股

10-16（MEDIUM △）Top ΔOI: 85P +2,819 ｜ 90C +938
10-16（MEDIUM △）仓位参考: Max Pain 92 ｜ Call Wall 90（+1.7%，弱）（OI 6.7k） ｜ Put Wall 90（+1.7%，弱）（OI 10.7k）

10-23（Activity LOW）仓位参考: Max Pain 94 ｜ Call Wall 90（+1.7%，弱）（OI 0.4k） ｜ Put Wall 93（+5.1%，弱）（OI 1.3k）

10-30（MEDIUM △）Top ΔOI: 85P -99 ｜ 82P +42
10-30（MEDIUM △）仓位参考: Max Pain 93 ｜ Put Wall 90（+1.7%，弱）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/GDX_morning.json