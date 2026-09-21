# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $767.46 ｜ QQQ $734.29
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 32.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 180C ΔOI +18,464（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 180C ΔOI +18,464 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 177.64 → 今开 178.73（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 182.15 ｜ 低 176.76

Options: P/C成交量 0.21 | OI比 0.81 | ATM IV 52.5% | Skew 0.1pp | Term 0.91 | ExpMove ±4.6%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构正常（Term 0.91）｜保护溢价薄（Skew 0.1pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±4.6% ｜ 10-02（11D）±6.9% ｜ 10-09（18D）±8.9% ｜ 10-16（25D）±10.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 53,804,237 | GEX Change vs 上次快照 38,668,845 | Flip: Primary Flip: 168.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 613 / LOW 56 / INVALID 171
结构观察区: Primary Flip 168.81（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 6.8%） | Call Wall 180（弱结构｜现价高于该位 0.9%）
最近结构参考: Call Wall 180（现价高于该位 0.9%）
量化视角： 正 Gamma（5380万，无历史分位）｜正 Gamma 增强（+3867万）｜现价位于 Flip 上方 7.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 172（MaxPain，仅结算参考） / 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 169（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 180.0C — Vol 28,470 | 最新价 $3.27 | OI 4391→22855 (ΔOI +18464张) | ΔOI/Volume 64.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18464张（+420.5% vs前日OI），连续性待观察（方向未知）
09-25 185.0C — Vol 29,094 | 最新价 $1.67 | OI 4917→20849 (ΔOI +15932张) | ΔOI/Volume 54.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15932张（+324.0% vs前日OI），连续性待观察（方向未知）
09-25 182.5C — Vol 10,610 | 最新价 $2.36 | OI 2017→7085 (ΔOI +5068张) | ΔOI/Volume 47.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5068张（+251.3% vs前日OI），连续性待观察（方向未知）
09-25 165.0P — Vol 6,498 | 最新价 $0.76 | OI 5185→9823 (ΔOI +4638张) | ΔOI/Volume 71.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4638张（+89.5% vs前日OI），连续性待观察（方向未知）
09-25 177.5C — Vol 9,560 | 最新价 $4.43 | OI 1153→4922 (ΔOI +3769张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3769张（+326.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 47,871 张（Put 4,638 / Call 43,233），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +53.8k / P +22.8k ｜ Activity HIGH ｜ 4D
10-02  C +2.4k / P +6.0k ｜ Activity HIGH ｜ 11D
10-09  C +3.5k / P +3.1k ｜ Activity HIGH ｜ 18D
10-16  C +1.9k / P +2.1k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 101.7k / P 82.7k，今日变化ΔOI: C +53.8k / P +22.8k，平值价格ATM: C $3.95 / P $4.35 ｜ ATM IV 52.5%，净 delta 敞口 2.4M shares
Top ΔOI: C 180 +18,464 ｜ C 185 +15,932 ｜ C 182 +5,068
仓位参考: Max Pain 172 ｜ Call Wall 180（-0.9%，弱）（OI 22.9k） ｜ Put Wall 165（-9.1%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 52.5%｜历史 Rank 43%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,413,601 股

📆 10-02 Forward Structure
存量OI: C 26.9k / P 32.2k，今日变化ΔOI: C +2.4k / P +6.0k，平值价格ATM: C $6.00 / P $6.55 ｜ ATM IV 48.6%，净 delta 敞口 -8k shares
仓位参考: Max Pain 175 ｜ Call Wall 180（-0.9%，弱）（OI 3.4k） ｜ Put Wall 170（-6.4%）（OI 5.3k）
量化解读： 存量 Put 重｜ATM IV 48.6%｜历史 Rank 43%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,232 股

📆 10-09 Forward Structure
存量OI: C 14.7k / P 23.2k，今日变化ΔOI: C +3.5k / P +3.1k，平值价格ATM: C $7.75 / P $8.34 ｜ ATM IV 47.8%，净 delta 敞口 160k shares
Top ΔOI: C 177 +2,722 ｜ P 175 +1,204
仓位参考: Max Pain 175 ｜ Call Wall 177.5（-2.2%）（OI 3.1k） ｜ Put Wall 170（-6.4%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.8%｜历史 Rank 43%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 159,975 股

📆 10-16 Forward Structure
存量OI: C 129.0k / P 153.7k，今日变化ΔOI: C +1.9k / P +2.1k，平值价格ATM: C $9.01 / P $9.70 ｜ ATM IV 47.6%，净 delta 敞口 54k shares
Top ΔOI: C 180 +646 ｜ C 170 -453
仓位参考: Max Pain 160 ｜ Call Wall 170（-6.4%，弱）（OI 15.9k） ｜ Put Wall 170（-6.4%，弱）（OI 14.7k）
量化解读： 存量 Put 重｜ATM IV 47.6%｜历史 Rank 43%（近端代理）｜净 delta 敞口 正 54,310 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/PLTR_morning.json