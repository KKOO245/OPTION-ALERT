# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.68 ｜ QQQ $718.03
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 38.95 → 今开 38.31（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 39.52 ｜ 低 37.94

Options: P/C成交量 1.50 | OI比 0.93 | ATM IV 66.1% | Skew 4.5pp | Term 0.98 | ExpMove ±5.1%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 0.98）｜保护溢价中性（Skew 4.5pp）｜当日成交偏 Put（P/C量 1.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.50×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±5.1% ｜ 10-30（10D）±8.9% ｜ 11-06（17D）±14.9% ｜ 11-13（24D）±6.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,840,867 | GEX Change vs 上次快照 670,117 | Flip: Primary Flip: 40.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 318 / LOW 72 / INVALID 134
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 40.88（全链重定价，覆盖 100%）
Put Wall 40（弱结构｜现价低于该位 2.7%）
最近结构参考: Put Wall 40（现价低于该位 2.7%）
量化视角： 负 Gamma（284万，无历史分位）｜负 Gamma 缓解（+67万）｜现价位于 Flip 下方 4.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 41（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 42.0C — Vol 845 | 最新价 $0.28 | OI 240→1006 (ΔOI +766张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增766张（+319.2% vs前日OI），连续性待观察（方向未知）
10-23 43.0C — Vol 651 | 最新价 $0.11 | OI 206→735 (ΔOI +529张) | ΔOI/Volume 81.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增529张（+256.8% vs前日OI），连续性待观察（方向未知）
10-23 49.0C — Vol 374 | 最新价 $0.04 | OI 145→429 (ΔOI +284张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增284张（+195.9% vs前日OI），连续性待观察（方向未知）
10-23 38.0P — Vol 289 | 最新价 $0.52 | OI 155→427 (ΔOI +272张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增272张（+175.5% vs前日OI），连续性待观察（方向未知）
10-23 37.5P — Vol 256 | 最新价 $0.42 | OI 9→249 (ΔOI +240张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增240张（+2666.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,091 张（Put 512 / Call 1,579），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.8k / P -39 ｜ Activity HIGH ｜ 3D
10-30  C +0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 10D
11-06  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 17D
11-13  C +0.2k / P -38 ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 9.1k / P 8.5k，今日变化ΔOI: C +2.8k / P -39，平值价格ATM: C $0.81 / P $1.19 ｜ ATM IV 66.1%，净 delta 敞口 96k shares
Top ΔOI: C 42 +766 ｜ P 42 -356
仓位参考: Max Pain 42 ｜ Call Wall 42（+7.9%，弱）（OI 1.0k） ｜ Put Wall 36.5（-6.2%）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 66.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.34×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 95,529 股

10-30（MEDIUM △）Top ΔOI: 42P +209 ｜ 42P +137
10-30（MEDIUM △）仓位参考: Max Pain 45 ｜ Put Wall 42（+7.9%，弱）（OI 0.6k）

11-06（MEDIUM △）仓位参考: Max Pain 43 ｜ Call Wall 40（+2.8%，弱）（OI 0.3k） ｜ Put Wall 38（-2.3%）（OI 0.8k）

11-13（MEDIUM △）Top ΔOI: 39P -87
11-13（MEDIUM △）仓位参考: Max Pain 48 ｜ Put Wall 39（+0.2%）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/MP_morning.json