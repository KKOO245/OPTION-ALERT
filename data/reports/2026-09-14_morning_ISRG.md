# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 09-18 370C ΔOI +74（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 380C ΔOI +87 占该期限总 OI 15.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 369.15 → 今开 373.85（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 378.00 ｜ 低 372.18

Options: P/C成交量 1.49 | OI比 1.02 | ATM IV 35.6% | Skew -2.9pp | Term 0.99 | ExpMove ±4.6%（近端） | Rank — (历史不足)
量化视角： 期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.49×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±4.6% ｜ 09-25（11D）±1.5% ｜ 10-02（18D）±0.0% ｜ 10-09（25D）±7.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -371,696 | GEX Change vs 上次快照 1,983,464 | Flip: Primary Flip: 377.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 272 / LOW 196 / INVALID 466
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 377.80（全链重定价，覆盖 95%）
Call Wall 400（弱结构｜现价低于该位 5.9%）
最近结构参考: Flip 378（现价低于该位 0.4%）
量化视角： 负 Gamma（37万，无历史分位）｜负 Gamma 缓解（+198万）｜现价位于 Flip 下方 0.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 378（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 380.0C — Vol 172 | 最新价 $9.72 | OI 22→109 (ΔOI +87张) | ΔOI/Volume 50.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增87张（+395.4% vs前日OI），连续性待观察（方向未知）
09-18 370.0C — Vol 177 | 最新价 $7.90 | OI 391→465 (ΔOI +74张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增74张（+18.9% vs前日OI），连续性待观察（方向未知）
09-18 420.0C — Vol 73 | 最新价 $0.10 | OI 711→774 (ΔOI +63张) | ΔOI/Volume 86.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增63张（+8.9% vs前日OI），连续性待观察（方向未知）
09-18 385.0C — Vol 49 | 最新价 $1.22 | OI 170→207 (ΔOI +37张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增37张（+21.8% vs前日OI），连续性待观察（方向未知）
09-25 400.0C — Vol 35 | 最新价 $1.66 | OI 61→92 (ΔOI +31张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31张（+50.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 292 张（Put 0 / Call 292），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.3k / P -96 ｜ Activity MEDIUM △ ｜ 4D
09-25  C +54 / P -11 ｜ Activity MEDIUM △ ｜ 11D
10-02  C +20 / P +0 ｜ Activity MEDIUM △ ｜ 18D
10-09  C +90 / P +0 ｜ Activity HIGH ｜ 25D

📆 09-18 Forward Structure
存量OI: C 15.9k / P 16.3k，今日变化ΔOI: C +0.3k / P -96，平值价格ATM: C $4.25 / P $13.11 ｜ ATM IV 35.6%，净 delta 敞口 9k shares
Top ΔOI: C 370 +74 ｜ C 385 +37
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.3%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.6%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,322 股

09-25（MEDIUM △）Top ΔOI: 400C +31 ｜ 380P -10
09-25（MEDIUM △）仓位参考: Max Pain 365 ｜ Put Wall 360（-4.4%，弱）（OI 0.2k）

10-02（MEDIUM △）Top ΔOI: 375C +10 ｜ 400C +6
10-02（MEDIUM △）仓位参考: Max Pain 365 ｜ Call Wall 405（+7.6%，弱）（OI 53）

📆 10-09 Forward Structure
存量OI: C 0.4k / P 0.2k，今日变化ΔOI: C +90 / P +0，平值价格ATM: C $11.80 / P $17.84 ｜ ATM IV 31.8%，净 delta 敞口 4k shares
Top ΔOI: C 380 +87 ｜ P 365 +2
仓位参考: Max Pain 350 ｜ Call Wall 380（+0.9%）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 31.8%｜净 delta 敞口 正 3,519 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/ISRG_morning.json