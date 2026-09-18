# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
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
🟡 **近现价集中开仓**: 10-16 510P ΔOI +2,183（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 528.9）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 523.06 → 收盘 533.07（+1.9%） ｜ 今日高 533.21 ｜ 低 522.39 ｜ 昨收 519.10 → 收盘 533.07（+2.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-25，窗口结束前不做对错判定）

Options: P/C成交量 1.75 | OI比 0.86 | ATM IV 90.2% | Skew 1.7pp | Term 0.38 | ExpMove ±4.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.38，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜当日成交偏 Put（P/C量 1.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.75×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±4.4% ｜ 10-02（14D）±6.1% ｜ 10-09（21D）±8.3% ｜ 10-16（28D）±7.8%
   ⇒ IV–VIX Spread: +75.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 5,640,222 | GEX Change vs 上次快照 469,304 | Flip: Candidates 528.88 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 495 / LOW 295 / INVALID 862
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈529（全链重定价，覆盖 76%，CONDITIONAL）
最近结构参考: Flip 529（现价高于该位 0.8%）
量化视角： 正 Gamma（564万，无历史分位）｜正 Gamma 增强（+47万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 515（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 529（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 7D
10-02  C +0.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
10-09  C +76 / P +48 ｜ Activity MEDIUM △ ｜ 21D
10-16  C -0.2k / P +9.0k ｜ Activity MEDIUM △ ｜ 28D

📆 09-25 Forward Structure
存量OI: C 10.4k / P 15.1k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $5.30 / P $18.10 ｜ ATM IV 29.4%，净 delta 敞口 12k shares
Top ΔOI: P 490 -250 ｜ C 520 +199
仓位参考: Max Pain 520 ｜ Put Wall 510（-4.3%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 29.4%｜历史 Rank 100%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,571 股

10-02（MEDIUM △）Top ΔOI: 520C +401 ｜ 542P +100
10-02（MEDIUM △）仓位参考: Max Pain 512 ｜ Call Wall 542.5（+1.8%，弱）（OI 2.8k）

10-09（MEDIUM △）Top ΔOI: 522C +31 ｜ 525C +16
10-09（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 525（-1.5%）（OI 1.6k） ｜ Put Wall 510（-4.3%，弱）（OI 0.1k）

10-16（MEDIUM △）Top ΔOI: 480P +5,957 ｜ 510P +2,183
10-16（MEDIUM △）仓位参考: Max Pain 515 ｜ Call Wall 550（+3.2%，弱）（OI 3.5k） ｜ Put Wall 510（-4.3%，弱）（OI 5.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SOXX_evening.json