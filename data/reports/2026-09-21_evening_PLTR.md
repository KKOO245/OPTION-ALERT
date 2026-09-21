# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 180C ΔOI +18,464（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 180C ΔOI +18,464 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 178.73 → 收盘 183.09（+2.4%） ｜ 今日高 183.38 ｜ 低 176.76 ｜ 昨收 177.64 → 收盘 183.09（+3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.34 | OI比 0.81 | ATM IV 50.8% | Skew 1.0pp | Term 0.93 | ExpMove ±4.2%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.93）｜保护溢价薄（Skew 1.0pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±4.2% ｜ 10-02（11D）±6.7% ｜ 10-09（18D）±8.3% ｜ 10-16（25D）±9.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 58,813,457 | GEX Change vs 上次快照 5,009,220 | Flip: Primary Flip: 168.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 595 / LOW 71 / INVALID 174
结构观察区: Primary Flip 168.98（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 7.7%） | Call Wall 180（弱结构｜现价高于该位 1.7%）
最近结构参考: Call Wall 180（现价高于该位 1.7%）
量化视角： 正 Gamma（5881万，无历史分位）｜正 Gamma 增强（+501万）｜现价位于 Flip 上方 8.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 172（MaxPain，仅结算参考） / 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 169（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 180.0C — Vol 21,374 | 最新价 $5.68 | OI 4391→22855 (ΔOI +18464张) | ΔOI/Volume 86.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18464张（+420.5% vs前日OI），连续性待观察（方向未知）
09-25 185.0C — Vol 23,707 | 最新价 $3.05 | OI 4917→20849 (ΔOI +15932张) | ΔOI/Volume 67.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15932张（+324.0% vs前日OI），连续性待观察（方向未知）
09-25 182.5C — Vol 11,704 | 最新价 $4.25 | OI 2017→7085 (ΔOI +5068张) | ΔOI/Volume 43.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5068张（+251.3% vs前日OI），连续性待观察（方向未知）
09-25 165.0P — Vol 3,854 | 最新价 $0.22 | OI 5185→9823 (ΔOI +4638张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4638张（+89.5% vs前日OI），连续性待观察（方向未知）
09-25 177.5C — Vol 6,640 | 最新价 $7.35 | OI 1153→4922 (ΔOI +3769张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3769张（+326.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 47,871 张（Put 4,638 / Call 43,233），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +53.8k / P +22.8k ｜ Activity HIGH ｜ 4D
10-02  C +2.4k / P +6.0k ｜ Activity HIGH ｜ 11D
10-09  C +3.5k / P +3.1k ｜ Activity HIGH ｜ 18D
10-16  C +1.9k / P +2.1k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 101.7k / P 82.7k，今日变化ΔOI: C +53.8k / P +22.8k，平值价格ATM: C $4.25 / P $3.54 ｜ ATM IV 50.8%，净 delta 敞口 2.6M shares
Top ΔOI: C 180 +18,464 ｜ C 185 +15,932 ｜ C 182 +5,068
仓位参考: Max Pain 172 ｜ Call Wall 180（-1.7%，弱）（OI 22.9k） ｜ Put Wall 165（-9.9%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 50.8%｜历史 Rank 29%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,643,254 股

📆 10-02 Forward Structure
存量OI: C 26.9k / P 32.2k，今日变化ΔOI: C +2.4k / P +6.0k，平值价格ATM: C $6.53 / P $5.70 ｜ ATM IV 47.8%，净 delta 敞口 2k shares
仓位参考: Max Pain 175 ｜ Call Wall 180（-1.7%，弱）（OI 3.4k） ｜ Put Wall 170（-7.1%）（OI 5.3k）
量化解读： 存量 Put 重｜ATM IV 47.8%｜历史 Rank 29%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,301 股

📆 10-09 Forward Structure
存量OI: C 14.7k / P 23.2k，今日变化ΔOI: C +3.5k / P +3.1k，平值价格ATM: C $8.07 / P $7.20 ｜ ATM IV 47.2%，净 delta 敞口 171k shares
Top ΔOI: C 177 +2,722 ｜ P 175 +1,204
仓位参考: Max Pain 175 ｜ Call Wall 177.5（-3.1%）（OI 3.1k） ｜ Put Wall 170（-7.1%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.2%｜历史 Rank 29%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 170,868 股

10-16（MEDIUM △）Top ΔOI: 180C +646 ｜ 170C -453
10-16（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 170（-7.1%，弱）（OI 15.9k） ｜ Put Wall 170（-7.1%，弱）（OI 14.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/PLTR_evening.json