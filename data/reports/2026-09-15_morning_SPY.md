# 期权晨报 2026-09-15（快照 10:20 ET）

📊 市场环境

SPY $759.03 ｜ QQQ $706.26
VIX 17.08 ↓0.1%（5D +8.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-16 731P ΔOI +11,011（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 760.88 → 今开 760.12（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 760.34 ｜ 低 757.88

Options: P/C成交量 1.43 | OI比 3.19 | ATM IV 13.7% | Skew 1.5pp | Term 1.00 | ExpMove ±0.8%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 1.00）｜保护溢价薄（Skew 1.5pp）｜当日成交偏 Put（P/C量 1.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.43×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.19×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 18% ｜ P/C OI(近端) 97%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 18%）｜近端 Put 显著偏重（P/C OI 分位 97%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-16（1D）±0.8% ｜ 09-17（2D）±1.1% ｜ 09-18（3D）±1.3% ｜ 09-21（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,838,111,568 | GEX Change vs 上次快照 -39,014,796 | Flip: Primary Flip: 768.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3369 / LOW 342 / INVALID 1919
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.28（全链重定价，覆盖 96%）
Call Wall 800（弱结构｜现价低于该位 5.1%）
最近结构参考: Flip 768（现价低于该位 1.2%）
量化视角： 负 Gamma（18.38亿，历史分位偏负区，比 82% 的交易日更负）｜负 Gamma 加深（3901万）｜现价位于 Flip 下方 1.16%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 761（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 768（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-15 727.0P — Vol 31,606 | 最新价 $0.05 | OI 343→29180 (ΔOI +28837张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28837张（+8407.3% vs前日OI），连续性待观察（方向未知）
09-15 721.0P — Vol 26,736 | 最新价 $0.04 | OI 229→22309 (ΔOI +22080张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22080张（+9641.9% vs前日OI），连续性待观察（方向未知）
09-15 720.0P — Vol 29,825 | 最新价 $0.04 | OI 188→19970 (ΔOI +19782张) | ΔOI/Volume 66.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19782张（+10522.3% vs前日OI），连续性待观察（方向未知）
09-15 730.0P — Vol 24,018 | 最新价 $0.05 | OI 584→19303 (ΔOI +18719张) | ΔOI/Volume 77.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18719张（+3205.3% vs前日OI），连续性待观察（方向未知）
09-15 731.0P — Vol 20,033 | 最新价 $0.05 | OI 150→18305 (ΔOI +18155张) | ΔOI/Volume 90.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18155张（+12103.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 107,573 张（Put 107,573 / Call 0），跨 1 个期限｜彩票/名义 5 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 113.5k / P 361.7k，今日成交量: C 383.5k / P 575.1k，平值价格ATM: C $1.15 / P $1.08 ｜ ATM IV 13.7%，预期波动 ±0.3%，Max Pain 761
Top ΔOI: P 727 +28,837 ｜ P 721 +22,080 ｜ P 720 +19,782

📆 Forward Expiration Structure

09-16  C +22.9k / P +58.7k ｜ Activity HIGH ｜ 1D
09-17  C +12.0k / P +26.0k ｜ Activity HIGH ｜ 2D
09-18  C +55.4k / P +22.9k ｜ Activity HIGH ｜ 3D
09-21  C +11.4k / P +16.8k ｜ Activity HIGH ｜ 6D

📆 09-16 Forward Structure
存量OI: C 60.5k / P 103.9k，今日变化ΔOI: C +22.9k / P +58.7k，平值价格ATM: C $3.22 / P $3.08 ｜ ATM IV 17.7%，净 delta 敞口 -90k shares
Top ΔOI: P 721 +12,865 ｜ P 731 +11,011 ｜ P 726 +9,312
仓位参考: Max Pain 761 ｜ Call Wall 766（+0.9%，弱）（OI 5.0k） ｜ Put Wall 721（-5.1%，弱）（OI 12.9k）
量化解读： 存量 Put 重｜ATM IV 17.7%｜历史 Rank 56%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 89,652 股

📆 09-17 Forward Structure
存量OI: C 54.0k / P 84.9k，今日变化ΔOI: C +12.0k / P +26.0k，平值价格ATM: C $4.24 / P $4.12 ｜ ATM IV 17.3%，净 delta 敞口 -24k shares
仓位参考: Max Pain 760 ｜ Call Wall 775（+2.1%，弱）（OI 4.7k） ｜ Put Wall 750（-1.2%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 17.3%｜历史 Rank 56%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,617 股

📆 09-18 Forward Structure
存量OI: C 1164.6k / P 3841.1k，今日变化ΔOI: C +55.4k / P +22.9k，平值价格ATM: C $4.38 / P $5.54 ｜ ATM IV 16.3%，净 delta 敞口 399k shares
Top ΔOI: C 804 +8,451 ｜ C 800 +6,704 ｜ C 803 +6,645
仓位参考: Max Pain 755 ｜ Call Wall 790（+4.0%，弱）（OI 56.1k） ｜ Put Wall 750（-1.2%，弱）（OI 134.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.3%｜历史 Rank 56%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 399,100 股

📆 09-21 Forward Structure
存量OI: C 38.0k / P 41.4k，今日变化ΔOI: C +11.4k / P +16.8k，平值价格ATM: C $4.80 / P $6.12 ｜ ATM IV 13.5%，净 delta 敞口 80k shares
Top ΔOI: P 720 +1,576 ｜ P 722 +1,459 ｜ P 685 +1,457
仓位参考: Max Pain 757 ｜ Call Wall 760（+0.1%）（OI 4.2k） ｜ Put Wall 755（-0.6%）（OI 4.0k）
量化解读： 存量两侧均衡｜ATM IV 13.5%｜历史 Rank 56%（近端代理）｜净 delta 敞口 正 79,878 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SPY_morning.json