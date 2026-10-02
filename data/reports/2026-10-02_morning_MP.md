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
🟡 **近现价集中开仓**: 10-16 45P ΔOI +792（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 46.09 → 今开 47.00（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 47.21 ｜ 低 46.15

Options: P/C成交量 0.43 | OI比 0.58 | ATM IV 77.0% | Skew 4.6pp | Term 0.70 | ExpMove ±5.5%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价中性（Skew 4.6pp）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±5.5% ｜ 10-16（14D）±7.3% ｜ 10-23（21D）±11.6% ｜ 10-30（28D）±14.8%
   ⇒ IV–VIX Spread: +61.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -766,175 | GEX Change vs 上次快照 3,985,317 | Flip: Primary Flip: 46.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 275 / LOW 68 / INVALID 113
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 46.95（全链重定价，覆盖 92%）
Put Wall 45（现价高于该位 3.6%） | Call Wall 50（弱结构｜现价低于该位 6.8%）
最近结构参考: Flip 47（现价低于该位 0.7%）
量化视角： 负 Gamma（77万，无历史分位）｜负 Gamma 缓解（+399万）｜现价位于 Flip 下方 0.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall） / 46（MaxPain，仅结算参考）；上方 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 47（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 45.5P — Vol 1,979 | 最新价 $0.31 | OI 985→2647 (ΔOI +1662张) | ΔOI/Volume 84.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1662张（+168.7% vs前日OI），连续性待观察（方向未知）
10-02 46.0C — Vol 3,119 | 最新价 $0.64 | OI 170→1550 (ΔOI +1380张) | ΔOI/Volume 44.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1380张（+811.8% vs前日OI），连续性待观察（方向未知）
10-16 45.0P — Vol 1,232 | 最新价 $1.53 | OI 3595→4387 (ΔOI +792张) | ΔOI/Volume 64.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增792张（+22.0% vs前日OI），连续性待观察（方向未知）
10-16 44.0P — Vol 544 | 最新价 $1.38 | OI 302→730 (ΔOI +428张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增428张（+141.7% vs前日OI），连续性待观察（方向未知）
10-16 43.5P — Vol 332 | 最新价 $1.40 | OI 31→343 (ΔOI +312张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增312张（+1006.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,574 张（Put 3,194 / Call 1,380），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 15.1k / P 8.7k，今日成交量: C 0.5k / P 0.2k，平值价格ATM: C $0.35 / P $0.43 ｜ ATM IV 77.0%，预期波动 ±1.7%，Max Pain 46
Top ΔOI: P 45 +1,662 ｜ C 46 +1,380 ｜ P 50 -1,219

📆 Forward Expiration Structure

10-09  C +0.7k / P +0.7k ｜ Activity MEDIUM △ ｜ 7D
10-16  C -0.1k / P +1.8k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +46 / P +69 ｜ Activity LOW ｜ 21D
10-30  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 6.7k / P 6.2k，今日变化ΔOI: C +0.7k / P +0.7k，平值价格ATM: C $1.35 / P $1.23 ｜ ATM IV 53.7%，净 delta 敞口 17k shares
仓位参考: Max Pain 49 ｜ Call Wall 50（+7.2%，弱）（OI 0.5k） ｜ Put Wall 47（+0.8%）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 53.7%｜历史 Rank 67%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,742 股

10-16（MEDIUM △）Top ΔOI: 45P +792 ｜ 44P +428
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+7.2%，弱）（OI 3.8k） ｜ Put Wall 45（-3.5%，弱）（OI 4.4k）

10-23（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50（+7.2%，弱）（OI 0.2k） ｜ Put Wall 45（-3.5%，弱）（OI 0.2k）

10-30（MEDIUM △）Top ΔOI: 46C +86 ｜ 51C +62
10-30（MEDIUM △）仓位参考: Max Pain 49 ｜ Call Wall 51（+9.4%，弱）（OI 0.3k） ｜ Put Wall 45（-3.5%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=39 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=39）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/MP_morning.json