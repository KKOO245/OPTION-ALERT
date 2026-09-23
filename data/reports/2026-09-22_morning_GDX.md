# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 99C ΔOI +3,582（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 85P ΔOI +1,190 占该期限总 OI 11.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 94.43 → 今开 94.51（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 96.31 ｜ 低 94.50

Options: P/C成交量 0.77 | OI比 0.43 | ATM IV 44.8% | Skew -5.7pp | Term 0.92 | ExpMove ±3.2%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -5.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±3.2% ｜ 10-02（10D）±6.7% ｜ 10-09（17D）±0.0% ｜ 10-16（24D）±8.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 43,246,991 | GEX Change vs 上次快照 20,329,306 | Flip: Primary Flip: 92.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 542 / LOW 94 / INVALID 226
结构观察区: Primary Flip 92.85（全链重定价，覆盖 99%）
Put Wall 90（弱结构｜现价高于该位 6.3%） | Call Wall 100（现价低于该位 4.3%）
最近结构参考: Flip 93（现价高于该位 3.0%）
量化视角： 正 Gamma（4325万，无历史分位）｜正 Gamma 增强（+2033万）｜现价位于 Flip 上方 3.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构） / 95（MaxPain，仅结算参考）；上方 100（Call Wall）。
• Gamma 区域：切换参考 93（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 99.0C — Vol 5,567 | 最新价 $0.50 | OI 10562→14144 (ΔOI +3582张) | ΔOI/Volume 64.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3582张（+33.9% vs前日OI），连续性待观察（方向未知）
09-25 65.0P — Vol 3,515 | 最新价 $0.01 | OI 15→3529 (ΔOI +3514张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3514张（+23426.7% vs前日OI），连续性待观察（方向未知）
09-25 80.5P — Vol 2,863 | 最新价 $0.02 | OI 146→2863 (ΔOI +2717张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2717张（+1861.0% vs前日OI），连续性待观察（方向未知）
09-25 82.0P — Vol 2,656 | 最新价 $0.03 | OI 125→2730 (ΔOI +2605张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2605张（+2084.0% vs前日OI），连续性待观察（方向未知）
09-25 97.0C — Vol 2,636 | 最新价 $0.87 | OI 17842→19715 (ΔOI +1873张) | ΔOI/Volume 71.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1873张（+10.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,291 张（Put 8,836 / Call 5,455），跨 1 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +10.9k / P +15.2k ｜ Activity HIGH ｜ 3D
10-02  C +1.9k / P +2.4k ｜ Activity MEDIUM △ ｜ 10D
10-09  C +0.3k / P +1.3k ｜ Activity HIGH ｜ 17D
10-16  C +4.3k / P +4.4k ｜ Activity MEDIUM △ ｜ 24D

📆 09-25 Forward Structure
存量OI: C 117.5k / P 50.1k，今日变化ΔOI: C +10.9k / P +15.2k，平值价格ATM: C $1.35 / P $1.70 ｜ ATM IV 44.8%，净 delta 敞口 165k shares
Top ΔOI: C 99 +3,582
仓位参考: Max Pain 95 ｜ Call Wall 100（+4.5%，弱）（OI 20.9k） ｜ Put Wall 93（-2.8%）（OI 8.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.8%｜历史 Rank 72%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 165,142 股

10-02（MEDIUM △）Top ΔOI: 94P +1,620 ｜ 94C +481
10-02（MEDIUM △）仓位参考: Max Pain 97 ｜ Call Wall 100（+4.5%）（OI 6.3k） ｜ Put Wall 97（+1.4%）（OI 11.4k）

📆 10-09 Forward Structure
存量OI: C 4.2k / P 6.2k，今日变化ΔOI: C +0.3k / P +1.3k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 41.6%，净 delta 敞口 -8k shares
Top ΔOI: P 85 +1,190 ｜ C 102 +108 ｜ C 100 +48
仓位参考: Max Pain 94 ｜ Call Wall 94（-1.7%，弱）（OI 0.7k） ｜ Put Wall 90（-5.9%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 41.6%｜历史 Rank 72%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,300 股

10-16（MEDIUM △）Top ΔOI: 95P +1,760 ｜ 88P +1,565
10-16（MEDIUM △）仓位参考: Max Pain 93 ｜ Call Wall 100（+4.5%，弱）（OI 11.0k） ｜ Put Wall 90（-5.9%，弱）（OI 9.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/GDX_morning.json