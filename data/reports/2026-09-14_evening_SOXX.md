# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **单日价格波动**: -5.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 497.58 → 收盘 497.40（-0.0%） ｜ 今日高 503.18 ｜ 低 495.15 ｜ 昨收 527.07 → 收盘 497.40（-5.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-17，窗口结束前不做对错判定）

Options: P/C成交量 3.83 | OI比 0.94 | ATM IV 40.4% | Skew 4.2pp | Term 0.90 | ExpMove ±3.6%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构正常（Term 0.90）｜保护溢价中性（Skew 4.2pp）｜当日成交偏 Put（P/C量 3.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.83×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±3.6% ｜ 09-25（11D）±4.9% ｜ 10-02（18D）±8.3% ｜ 10-09（25D）±7.7%
   ⇒ IV–VIX Spread: +23.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -40,045,603 | GEX Change vs 上次快照 6,549,602 | Flip: Primary Flip: 521.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 538 / LOW 344 / INVALID 744
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 521.58（全链重定价，覆盖 92%）
Put Wall 450（弱结构｜现价高于该位 10.5%）
最近结构参考: Flip 522（现价低于该位 4.6%）
量化视角： 负 Gamma（4005万，无历史分位）｜负 Gamma 缓解（+655万）｜现价位于 Flip 下方 4.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 450（Put Wall，弱结构）；上方 530（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 522（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 440.0P — Vol 72 | 最新价 $4.55 | OI 179→4148 (ΔOI +3969张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3969张（+2217.3% vs前日OI），连续性待观察（方向未知）
10-16 600.0C — Vol 210 | 最新价 $1.05 | OI 5497→8468 (ΔOI +2971张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2971张（+54.0% vs前日OI），连续性待观察（方向未知）
10-16 585.0C — Vol 10 | 最新价 $1.86 | OI 65→2860 (ΔOI +2795张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2795张（+4300.0% vs前日OI），连续性待观察（方向未知）
10-16 550.0C — Vol 226 | 最新价 $5.29 | OI 1064→3056 (ΔOI +1992张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1992张（+187.2% vs前日OI），连续性待观察（方向未知）
10-16 490.0P — Vol 24 | 最新价 $17.00 | OI 3068→5033 (ΔOI +1965张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1965张（+64.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,692 张（Put 5,934 / Call 7,758），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $5M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 100.0k / P 93.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $10.00 / P $7.97 ｜ ATM IV 40.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 530 ｜ Call Wall 535（+7.6%，弱）（OI 3.5k） ｜ Put Wall 450（-9.5%，弱）（OI 12.1k）
量化解读： 存量两侧均衡｜ATM IV 40.4%｜历史 Rank 71%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 530 ｜ Put Wall 480（-3.5%，弱）（OI 1.9k）

10-02（Activity LOW）仓位参考: Max Pain 525 ｜ Call Wall 542.5（+9.1%，弱）（OI 2.8k） ｜ Put Wall 470（-5.5%）（OI 2.8k）

10-09（Activity LOW）仓位参考: Max Pain 510 ｜ Call Wall 525（+5.5%）（OI 1.6k） ｜ Put Wall 465（-6.5%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SOXX_evening.json