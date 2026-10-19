# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.01
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 180C ΔOI +4,745（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 90P ΔOI +2,810 占该期限总 OI 17.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 173.16 → 今开 175.58（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 176.26 ｜ 低 170.96

Options: P/C成交量 0.67 | OI比 0.70 | ATM IV 72.7% | Skew 1.5pp | Term 0.97 | ExpMove ±6.3%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±6.3% ｜ 10-30（11D）±11.8% ｜ 11-06（18D）±14.4% ｜ 11-13（25D）±15.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,952,121 | GEX Change vs 上次快照 4,887,782 | Flip: Primary Flip: 162.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 452 / LOW 93 / INVALID 261
结构观察区: Primary Flip 162.73（全链重定价，覆盖 99%）
Call Wall 170（弱结构｜现价高于该位 1.0%）
最近结构参考: Call Wall 170（现价高于该位 1.0%）
量化视角： 正 Gamma（895万，无历史分位）｜正 Gamma 增强（+489万）｜现价位于 Flip 上方 5.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Call Wall，弱结构）；上方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 180.0C — Vol 7,322 | 最新价 $3.62 | OI 1156→5901 (ΔOI +4745张) | ΔOI/Volume 64.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4745张（+410.5% vs前日OI），连续性待观察（方向未知）
10-23 187.5C — Vol 5,211 | 最新价 $1.82 | OI 1077→5470 (ΔOI +4393张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4393张（+407.9% vs前日OI），连续性待观察（方向未知）
10-23 182.5C — Vol 4,796 | 最新价 $2.90 | OI 335→3836 (ΔOI +3501张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3501张（+1045.1% vs前日OI），连续性待观察（方向未知）
10-23 177.5C — Vol 3,955 | 最新价 $4.51 | OI 288→3644 (ΔOI +3356张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3356张（+1165.3% vs前日OI），连续性待观察（方向未知）
11-06 90.0P — Vol 2,820 | 最新价 $0.13 | OI 1→2811 (ΔOI +2810张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2810张（+281000.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,805 张（Put 2,810 / Call 15,995），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +23.3k / P +12.0k ｜ Activity HIGH ｜ 4D
10-30  C +1.2k / P +2.7k ｜ Activity HIGH ｜ 11D
11-06  C +0.4k / P +3.1k ｜ Activity HIGH ｜ 18D
11-13  C +2.0k / P +0.4k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 54.0k / P 37.9k，今日变化ΔOI: C +23.3k / P +12.0k，平值价格ATM: C $5.12 / P $5.66 ｜ ATM IV 72.7%，净 delta 敞口 295k shares
Top ΔOI: C 180 +4,745 ｜ C 187 +4,393 ｜ C 182 +3,501
仓位参考: Max Pain 178 ｜ Call Wall 180（+4.9%，弱）（OI 5.9k）
量化解读： 存量 Call 重｜ATM IV 72.7%｜历史 Rank 40%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 294,726 股

📆 10-30 Forward Structure
存量OI: C 15.7k / P 16.4k，今日变化ΔOI: C +1.2k / P +2.7k，平值价格ATM: C $11.00 / P $9.27 ｜ ATM IV 81.3%，净 delta 敞口 2k shares
Top ΔOI: C 200 +469
仓位参考: Max Pain 180 ｜ Call Wall 185（+7.8%，弱）（OI 1.6k） ｜ Put Wall 180（+4.9%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 81.3%｜历史 Rank 40%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,880 股

📆 11-06 Forward Structure
存量OI: C 5.5k / P 10.5k，今日变化ΔOI: C +0.4k / P +3.1k，平值价格ATM: C $12.70 / P $12.05 ｜ ATM IV 75.5%，净 delta 敞口 3k shares
Top ΔOI: P 165 +126
仓位参考: Max Pain 175 ｜ Call Wall 175（+1.9%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 75.5%｜历史 Rank 40%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,417 股

📆 11-13 Forward Structure
存量OI: C 4.7k / P 6.5k，今日变化ΔOI: C +2.0k / P +0.4k，平值价格ATM: C $13.58 / P $12.62 ｜ ATM IV 72.7%，净 delta 敞口 55k shares
Top ΔOI: C 177 +1,093 ｜ C 205 +370
仓位参考: Max Pain 178 ｜ Call Wall 177.5（+3.4%）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.7%｜历史 Rank 40%（近端代理）｜IV/RV 1.50×（近似）｜净 delta 敞口 正 55,236 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/COIN_morning.json