# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.90
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 502.06 → 今开 517.53（+3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 520.42 ｜ 低 514.80

Options: P/C成交量 0.64 | OI比 0.88 | ATM IV 35.8% | Skew 5.3pp | Term 1.01 | ExpMove ±1.7%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 1.01）｜保护溢价中性（Skew 5.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±1.7% ｜ 09-25（8D）±4.0% ｜ 10-02（15D）±5.8% ｜ 10-09（22D）±7.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,850,282 | GEX Change vs 上次快照 25,514,780 | Flip: Primary Flip: 524.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 533 / LOW 361 / INVALID 732
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 524.83（全链重定价，覆盖 84%）
最近结构参考: Flip 525（现价低于该位 1.1%）
量化视角： 负 Gamma（1685万，无历史分位）｜负 Gamma 缓解（+2551万）｜现价位于 Flip 下方 1.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 518（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 525（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 465.0P — Vol 3,399 | 最新价 $8.30 | OI 1353→4711 (ΔOI +3358张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3358张（+248.2% vs前日OI），连续性待观察（方向未知）
09-25 450.0P — Vol 1,748 | 最新价 $1.00 | OI 375→2106 (ΔOI +1731张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1731张（+461.6% vs前日OI），连续性待观察（方向未知）
09-25 460.0P — Vol 1,243 | 最新价 $1.65 | OI 1130→2162 (ΔOI +1032张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1032张（+91.3% vs前日OI），连续性待观察（方向未知）
09-18 480.0P — Vol 3,019 | 最新价 $1.25 | OI 8017→8567 (ΔOI +550张) | ΔOI/Volume 18.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增550张（+6.9% vs前日OI），连续性待观察（方向未知）
10-16 320.0P — Vol 500 | 最新价 $0.10 | OI 2171→2671 (ΔOI +500张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+23.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,171 张（Put 7,171 / Call 0），跨 3 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.5k / P -2.2k ｜ Activity HIGH ｜ 1D
09-25  C +0.5k / P +2.9k ｜ Activity HIGH ｜ 8D
10-02  C -0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
10-09  C -11 / P +54 ｜ Activity MEDIUM △ ｜ 22D

📆 09-18 Forward Structure
存量OI: C 104.9k / P 92.1k，今日变化ΔOI: C +0.5k / P -2.2k，平值价格ATM: C $3.60 / P $5.41 ｜ ATM IV 35.8%，净 delta 敞口 83k shares
Top ΔOI: P 475 -1,116 ｜ P 480 +550 ｜ P 485 -532
仓位参考: Max Pain 518 ｜ Call Wall 560（+7.9%，弱）（OI 14.6k） ｜ Put Wall 480（-7.5%，弱）（OI 8.6k）
量化解读： 存量两侧均衡｜ATM IV 35.8%｜历史 Rank 58%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 82,923 股

📆 09-25 Forward Structure
存量OI: C 9.6k / P 14.9k，今日变化ΔOI: C +0.5k / P +2.9k，平值价格ATM: C $9.20 / P $11.33 ｜ ATM IV 33.2%，净 delta 敞口 12k shares
Top ΔOI: P 450 +1,731 ｜ P 460 +1,032 ｜ P 490 +262
仓位参考: Max Pain 515 ｜ Put Wall 480（-7.5%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 33.2%｜历史 Rank 58%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,549 股

10-02（MEDIUM △）Top ΔOI: 570C -153 ｜ 505C +136
10-02（MEDIUM △）仓位参考: Max Pain 505 ｜ Call Wall 542.5（+4.6%，弱）（OI 2.8k） ｜ Put Wall 470（-9.4%）（OI 3.0k）

10-09（MEDIUM △）Top ΔOI: 520C -19
10-09（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 525（+1.2%）（OI 1.6k） ｜ Put Wall 485（-6.5%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SOXX_morning.json