# 期权晚报 2026-09-15（快照 18:31 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 157.08 → 收盘 154.03（-1.9%） ｜ 今日高 157.53 ｜ 低 152.63 ｜ 昨收 157.60 → 收盘 154.03（-2.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-18，窗口结束前不做对错判定）

Options: P/C成交量 7.34 | OI比 1.71 | ATM IV 35.9% | Skew 1.8pp | Term 0.85 | ExpMove ±2.7%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜当日成交偏 Put（P/C量 7.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 7.34×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.71×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±2.7% ｜ 09-25（10D）±4.0% ｜ 10-02（17D）±2.6% ｜ 10-09（24D）±5.6%
   ⇒ IV–VIX Spread: +18.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -66,088,721 | GEX Change vs 上次快照 3,612,118 | Flip: Primary Flip: 164.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 380 / LOW 109 / INVALID 343
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.11（全链重定价，覆盖 94%）
Put Wall 150（弱结构｜现价高于该位 2.7%）
最近结构参考: Put Wall 150（现价高于该位 2.7%）
量化视角： 负 Gamma（6609万，无历史分位）｜负 Gamma 缓解（+361万）｜现价位于 Flip 下方 6.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 158（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 156.0P — Vol 1,236 | 最新价 $3.20 | OI 3212→4029 (ΔOI +817张) | ΔOI/Volume 66.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增817张（+25.4% vs前日OI），连续性待观察（方向未知）
10-02 165.0C — Vol 13 | 最新价 $0.70 | OI 246→792 (ΔOI +546张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增546张（+221.9% vs前日OI），连续性待观察（方向未知）
10-16 162.0P — Vol 108 | 最新价 $10.20 | OI 210→643 (ΔOI +433张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增433张（+206.2% vs前日OI），值得跟踪（方向未知）
09-18 160.0C — Vol 520 | 最新价 $0.28 | OI 3351→3648 (ΔOI +297张) | ΔOI/Volume 57.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增297张（+8.9% vs前日OI），连续性待观察（方向未知）
09-18 155.0P — Vol 15,061 | 最新价 $2.76 | OI 20209→20445 (ΔOI +236张) | ΔOI/Volume 1.6% | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增仓仅占量1.6%，以日内换手为主
量化视角： 5 个事件合计 ΔOI ≈ 2,329 张（Put 1,486 / Call 843），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-18 Forward Structure
存量OI: C 74.7k / P 128.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.93 / P $2.29 ｜ ATM IV 35.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 158 ｜ Call Wall 155（+0.6%，弱）（OI 10.8k） ｜ Put Wall 155（+0.6%，弱）（OI 20.4k）
量化解读： 存量 Put 重｜ATM IV 35.9%｜历史 Rank 66%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 167（+8.4%，弱）（OI 1.4k） ｜ Put Wall 150（-2.6%，弱）（OI 3.1k）

10-02（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 165（+7.1%）（OI 0.8k） ｜ Put Wall 157（+1.9%，弱）（OI 0.2k）

10-09（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 167（+8.4%，弱）（OI 20） ｜ Put Wall 160（+3.9%，弱）（OI 57）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/XBI_evening.json