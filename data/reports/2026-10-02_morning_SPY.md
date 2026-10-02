# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $753.63
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-05 793C ΔOI +9,123（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-08 660P ΔOI +9,653 占该期限总 OI 13.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 763.99 → 今开 770.58（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 772.28 ｜ 低 769.07

Options: P/C成交量 0.98 | OI比 1.56 | ATM IV 18.6% | Skew 2.1pp | Term 0.69 | ExpMove ±0.7%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 64% ｜ P/C OI(近端) 28%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 64%）｜近端持仓结构中性（P/C OI 分位 28%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-05（3D）±0.7% ｜ 10-06（4D）±0.8% ｜ 10-07（5D）±1.0% ｜ 10-08（6D）±1.1%
   ⇒ IV–VIX Spread: +3.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 417,151,678 | GEX Change vs 上次快照 1,259,468,148 | Flip: Primary Flip: 768.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2589 / LOW 370 / INVALID 1773
结构观察区: Primary Flip 768.86（全链重定价，覆盖 95%）
Call Wall 785（现价低于该位 1.8%）
最近结构参考: Flip 769（现价高于该位 0.3%）
量化视角： 正 Gamma（4.17亿，历史分位 64%，中性区）｜由负转正（+12.59亿）｜现价位于 Flip 上方 0.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 764（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 755.0P — Vol 23,713 | 最新价 $7.62 | OI 61128→83398 (ΔOI +22270张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22270张（+36.4% vs前日OI），连续性待观察（方向未知）
10-30 725.0P — Vol 23,086 | 最新价 $2.78 | OI 61844→83928 (ΔOI +22084张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22084张（+35.7% vs前日OI），连续性待观察（方向未知）
10-16 734.0P — Vol 25,778 | 最新价 $1.43 | OI 14246→35627 (ΔOI +21381张) | ΔOI/Volume 82.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21381张（+150.1% vs前日OI），连续性待观察（方向未知）
10-07 802.0C — Vol 16,896 | 最新价 $0.02 | OI 33→16881 (ΔOI +16848张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16848张（+51054.6% vs前日OI），连续性待观察（方向未知）
10-07 801.0C — Vol 14,126 | 最新价 $0.01 | OI 18→14115 (ΔOI +14097张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14097张（+78316.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 96,680 张（Put 65,735 / Call 30,945），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $26M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 415.5k / P 647.5k，今日成交量: C 738.8k / P 720.7k，平值价格ATM: C $1.58 / P $1.52 ｜ ATM IV 18.6%，预期波动 ±0.4%，Max Pain 764
Top ΔOI: P 761 +8,212 ｜ P 755 +8,058 ｜ P 733 +6,479

📆 Forward Expiration Structure

10-05  C +46.1k / P +24.0k ｜ Activity HIGH ｜ 3D
10-06  C +17.2k / P +22.3k ｜ Activity HIGH ｜ 4D
10-07  C +59.8k / P +15.0k ｜ Activity HIGH ｜ 5D
10-08  C +10.3k / P +29.3k ｜ Activity HIGH ｜ 6D

📆 10-05 Forward Structure
存量OI: C 95.2k / P 101.2k，今日变化ΔOI: C +46.1k / P +24.0k，平值价格ATM: C $2.67 / P $2.54 ｜ ATM IV 9.0%，净 delta 敞口 1.6M shares
Top ΔOI: C 793 +9,123 ｜ P 760 +2,518 ｜ C 780 +2,095
仓位参考: Max Pain 763 ｜ Call Wall 793（+2.9%）（OI 9.4k） ｜ Put Wall 750（-2.7%，弱）（OI 8.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 9.0%｜历史 Rank 81%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,607,026 股

📆 10-06 Forward Structure
存量OI: C 139.6k / P 60.9k，今日变化ΔOI: C +17.2k / P +22.3k，平值价格ATM: C $3.35 / P $3.08 ｜ ATM IV 9.7%，净 delta 敞口 522k shares
Top ΔOI: P 705 +3,052 ｜ P 760 +2,223 ｜ C 840 +1,809
仓位参考: Max Pain 764 ｜ Put Wall 760（-1.4%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 9.7%｜历史 Rank 81%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 521,810 股

📆 10-07 Forward Structure
存量OI: C 108.6k / P 80.5k，今日变化ΔOI: C +59.8k / P +15.0k，平值价格ATM: C $4.00 / P $3.59 ｜ ATM IV 10.3%，净 delta 敞口 479k shares
Top ΔOI: C 802 +16,848 ｜ C 801 +14,097 ｜ P 760 -5,271
仓位参考: Max Pain 764 ｜ Put Wall 760（-1.4%，弱）（OI 9.3k）
量化解读： 存量 Call 重｜ATM IV 10.3%｜历史 Rank 81%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 479,341 股

📆 10-08 Forward Structure
存量OI: C 24.1k / P 48.6k，今日变化ΔOI: C +10.3k / P +29.3k，平值价格ATM: C $4.36 / P $4.10 ｜ ATM IV 10.7%，净 delta 敞口 235k shares
Top ΔOI: C 810 +2,037
仓位参考: Max Pain 765 ｜ Call Wall 787（+2.1%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 10.7%｜历史 Rank 81%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 234,616 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SPY_morning.json