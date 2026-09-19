# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $nan
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **期限 OI 集中**: 10-02 18C ΔOI +1,856 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 15.9）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 15.90 → 收盘 15.37（-3.3%） ｜ 今日高 16.08 ｜ 低 15.15 ｜ 昨收 15.63 → 收盘 15.37（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-23，窗口结束前不做对错判定）

Options: P/C成交量 0.47 | OI比 0.36 | ATM IV 173.6% | Skew -7.1pp | Term 0.41 | ExpMove ±7.9%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.41，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.36）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.36×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±7.9% ｜ 10-02（14D）±10.7% ｜ 10-09（21D）±14.1% ｜ 10-16（28D）±15.6%
   ⇒ IV–VIX Spread: +158.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,633,939 | GEX Change vs 上次快照 -394,066 | Flip: Candidates 15.90 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 70%（带内） ｜ IV 有效性: VALID 173 / LOW 70 / INVALID 225
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈16（全链重定价，覆盖 70%，CONDITIONAL）
Put Wall 15（弱结构｜现价高于该位 2.5%）
最近结构参考: Put Wall 15（现价高于该位 2.5%）
量化视角： 负 Gamma（163万，无历史分位）｜负 Gamma 加深（39万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 70%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +2.1k / P +0.3k ｜ Activity HIGH ｜ 7D
10-02  C +2.5k / P +0.3k ｜ Activity HIGH ｜ 14D
10-09  C +77 / P -0.1k ｜ Activity MEDIUM △ ｜ 21D
10-16  C +1.2k / P +0.4k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 18.2k / P 7.9k，今日变化ΔOI: C +2.1k / P +0.3k，平值价格ATM: C $0.55 / P $0.66 ｜ ATM IV 64.8%，净 delta 敞口 13k shares
仓位参考: Max Pain 16 ｜ Call Wall 16.5（+7.4%，弱）（OI 1.4k） ｜ Put Wall 16.5（+7.4%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 64.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.44×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 12,739 股

📆 10-02 Forward Structure
存量OI: C 12.4k / P 4.8k，今日变化ΔOI: C +2.5k / P +0.3k，平值价格ATM: C $0.79 / P $0.86 ｜ ATM IV 67.8%，净 delta 敞口 18k shares
Top ΔOI: P 16 +200
仓位参考: Max Pain 17 ｜ Put Wall 16（+4.1%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.51×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 18,214 股

10-09（MEDIUM △）Top ΔOI: 15P +65
10-09（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 16（+4.1%）（OI 1.2k）

📆 10-16 Forward Structure
存量OI: C 30.8k / P 11.8k，今日变化ΔOI: C +1.2k / P +0.4k，平值价格ATM: C $1.43 / P $0.97 ｜ ATM IV 71.6%，净 delta 敞口 2k shares
Top ΔOI: P 19 +185
仓位参考: Max Pain 17 ｜ Put Wall 15（-2.4%）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 71.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.59×（近似）｜净 delta 敞口 正 2,215 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=24 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=24）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/USAR_evening.json