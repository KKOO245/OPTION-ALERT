# 期权晨报 2026-09-15（快照 10:20 ET）

📊 市场环境

SPY $759.03 ｜ QQQ $706.29
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
🟡 **近现价集中开仓**: 09-16 726C ΔOI +5,019（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 709.18 → 今开 708.76（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 709.53 ｜ 低 706.82

Options: P/C成交量 1.00 | OI比 2.56 | ATM IV 17.8% | Skew 2.3pp | Term 1.05 | ExpMove ±1.0%（近端） | Rank 47%
量化视角： IV 中性（Rank 47%）｜期限结构正常（Term 1.05）｜保护溢价中性（Skew 2.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 11% ｜ P/C OI(近端) 93%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 11%）｜近端 Put 显著偏重（P/C OI 分位 93%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-16（1D）±1.0% ｜ 09-17（2D）±1.4% ｜ 09-18（3D）±1.6% ｜ 09-21（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -775,644,649 | GEX Change vs 上次快照 98,470,037 | Flip: Primary Flip: 717.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3073 / LOW 494 / INVALID 2213
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 717.30（全链重定价，覆盖 96%）
Put Wall 700（弱结构｜现价高于该位 1.3%） | Call Wall 750（弱结构｜现价低于该位 5.5%）
最近结构参考: Flip 717（现价低于该位 1.2%）
量化视角： 负 Gamma（7.76亿，历史分位偏负区，比 89% 的交易日更负）｜负 Gamma 缓解（+9847万）｜现价位于 Flip 下方 1.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 710（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 717（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 615.0P — Vol 22,178 | 最新价 $0.11 | OI 22413→42415 (ΔOI +20002张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20002张（+89.2% vs前日OI），连续性待观察（方向未知）
10-16 685.0P — Vol 15,307 | 最新价 $7.85 | OI 10883→18823 (ΔOI +7940张) | ΔOI/Volume 51.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7940张（+73.0% vs前日OI），连续性待观察（方向未知）
09-15 710.0C — Vol 49,622 | 最新价 $2.29 | OI 849→8464 (ΔOI +7615张) | ΔOI/Volume 15.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7615张（+896.9% vs前日OI），连续性待观察（方向未知）
09-15 709.0P — Vol 40,384 | 最新价 $2.20 | OI 3929→11430 (ΔOI +7501张) | ΔOI/Volume 18.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7501张（+190.9% vs前日OI），连续性待观察（方向未知）
09-15 705.0P — Vol 49,447 | 最新价 $1.02 | OI 10115→17376 (ΔOI +7261张) | ΔOI/Volume 14.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7261张（+71.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 50,319 张（Put 42,704 / Call 7,615），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 98.0k / P 250.5k，今日成交量: C 369.0k / P 370.7k，平值价格ATM: C $1.04 / P $1.73 ｜ ATM IV 17.8%，预期波动 ±0.4%，Max Pain 710
Top ΔOI: C 710 +7,615 ｜ P 709 +7,501 ｜ P 705 +7,261

📆 Forward Expiration Structure

09-16  C +32.3k / P +79.2k ｜ Activity HIGH ｜ 1D
09-17  C +9.6k / P +28.8k ｜ Activity HIGH ｜ 2D
09-18  C +11.7k / P +26.8k ｜ Activity HIGH ｜ 3D
09-21  C +6.0k / P +17.1k ｜ Activity HIGH ｜ 6D

📆 09-16 Forward Structure
存量OI: C 57.3k / P 123.6k，今日变化ΔOI: C +32.3k / P +79.2k，平值价格ATM: C $3.24 / P $3.90 ｜ ATM IV 21.5%，净 delta 敞口 -195k shares
Top ΔOI: C 726 +5,019
仓位参考: Max Pain 710 ｜ Call Wall 725（+2.3%，弱）（OI 5.6k） ｜ Put Wall 700（-1.2%，弱）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 21.5%｜历史 Rank 47%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 194,817 股

📆 09-17 Forward Structure
存量OI: C 25.7k / P 75.7k，今日变化ΔOI: C +9.6k / P +28.8k，平值价格ATM: C $4.56 / P $5.16 ｜ ATM IV 21.7%，净 delta 敞口 -64k shares
Top ΔOI: P 649 +4,474 ｜ P 644 +3,722 ｜ P 650 +2,947
仓位参考: Max Pain 712 ｜ Call Wall 727（+2.6%，弱）（OI 2.2k） ｜ Put Wall 650（-8.3%）（OI 9.5k）
量化解读： 存量 Put 重｜ATM IV 21.7%｜历史 Rank 47%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 63,732 股

📆 09-18 Forward Structure
存量OI: C 1115.5k / P 1531.6k，今日变化ΔOI: C +11.7k / P +26.8k，平值价格ATM: C $5.54 / P $6.10 ｜ ATM IV 21.5%，净 delta 敞口 1.1M shares
Top ΔOI: P 615 +20,002 ｜ P 735 -4,421 ｜ C 725 -2,933
仓位参考: Max Pain 700 ｜ Call Wall 750（+5.8%，弱）（OI 50.6k） ｜ Put Wall 700（-1.2%）（OI 117.7k）
量化解读： 存量 Put 重｜ATM IV 21.5%｜历史 Rank 47%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,107,338 股

📆 09-21 Forward Structure
存量OI: C 18.4k / P 38.7k，今日变化ΔOI: C +6.0k / P +17.1k，平值价格ATM: C $6.30 / P $6.73 ｜ ATM IV 17.6%，净 delta 敞口 -119k shares
Top ΔOI: P 660 +1,829 ｜ P 655 +1,780 ｜ P 673 +870
仓位参考: Max Pain 715 ｜ Call Wall 735（+3.7%，弱）（OI 2.1k） ｜ Put Wall 715（+0.9%）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 47%（近端代理）｜净 delta 敞口 负 118,906 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/QQQ_morning.json