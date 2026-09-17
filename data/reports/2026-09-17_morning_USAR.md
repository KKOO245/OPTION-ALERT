# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.94
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

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 15C ΔOI +659（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.10 → 今开 15.55（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 15.88 ｜ 低 15.40

Options: P/C成交量 0.36 | OI比 0.50 | ATM IV 78.8% | Skew -11.6pp | Term 0.95 | ExpMove ±3.4%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -11.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.4% ｜ 09-25（8D）±8.8% ｜ 10-02（15D）±11.7% ｜ 10-09（22D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,242,292 | GEX Change vs 上次快照 5,614,742 | Flip: Primary Flip: 15.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 216 / LOW 90 / INVALID 162
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.88（全链重定价，覆盖 95%）
Put Wall 15（弱结构｜现价高于该位 3.4%）
最近结构参考: Flip 16（现价低于该位 2.3%）
量化视角： 负 Gamma（524万，无历史分位）｜负 Gamma 缓解（+561万）｜现价位于 Flip 下方 2.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 17.0P — Vol 888 | 最新价 $2.25 | OI 339→1196 (ΔOI +857张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增857张（+252.8% vs前日OI），连续性待观察（方向未知）
09-18 15.5C — Vol 918 | 最新价 $0.20 | OI 572→1231 (ΔOI +659张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增659张（+115.2% vs前日OI），连续性待观察（方向未知）
09-25 17.0C — Vol 637 | 最新价 $0.18 | OI 1297→1569 (ΔOI +272张) | ΔOI/Volume 42.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增272张（+21.0% vs前日OI），连续性待观察（方向未知）
09-18 16.0C — Vol 943 | 最新价 $0.08 | OI 1922→2180 (ΔOI +258张) | ΔOI/Volume 27.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增258张（+13.4% vs前日OI），连续性待观察（方向未知）
09-18 17.0C — Vol 919 | 最新价 $0.03 | OI 2644→2827 (ΔOI +183张) | ΔOI/Volume 19.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增183张（+6.9% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,229 张（Put 857 / Call 1,372），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +1.1k / P -2.8k ｜ Activity HIGH ｜ 1D
09-25  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 8D
10-02  C +0.1k / P +1.0k ｜ Activity HIGH ｜ 15D
10-09  C +0.1k / P +21 ｜ Activity MEDIUM △ ｜ 22D

📆 09-18 Forward Structure
存量OI: C 123.2k / P 61.6k，今日变化ΔOI: C +1.1k / P -2.8k，平值价格ATM: C $0.28 / P $0.25 ｜ ATM IV 78.8%，净 delta 敞口 322k shares
Top ΔOI: C 15 +659 ｜ P 25 -640 ｜ P 17 -530
仓位参考: Max Pain 18 ｜ Put Wall 15（-3.3%，弱）（OI 9.5k）
量化解读： 存量 Call 重｜ATM IV 78.8%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 321,981 股

09-25（MEDIUM △）Top ΔOI: 17P -577 ｜ 17C +272
09-25（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 17（+9.6%，弱）（OI 1.6k） ｜ Put Wall 17（+9.6%，弱）（OI 1.4k）

📆 10-02 Forward Structure
存量OI: C 9.9k / P 4.5k，今日变化ΔOI: C +0.1k / P +1.0k，平值价格ATM: C $0.89 / P $0.92 ｜ ATM IV 74.8%，净 delta 敞口 -60k shares
Top ΔOI: P 17 +857 ｜ P 15 +80
仓位参考: Max Pain 18 ｜ Put Wall 17（+9.6%）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.8%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 60,254 股

10-09（MEDIUM △）Top ΔOI: 15C +85 ｜ 16C +48
10-09（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 16（+3.2%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/USAR_morning.json