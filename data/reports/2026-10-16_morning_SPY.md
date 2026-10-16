# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.51 ｜ QQQ $721.38
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-20 784C ΔOI +4,584（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 655P ΔOI +57,154 占该期限总 OI 14.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 771.79 → 今开 773.24（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 773.23 ｜ 低 770.48

Options: P/C成交量 1.26 | OI比 3.03 | ATM IV 14.8% | Skew 1.4pp | Term 0.84 | ExpMove ±0.6%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价薄（Skew 1.4pp）｜当日成交偏 Put（P/C量 1.26）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.03×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 38% ｜ P/C OI(近端) 96%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 38%）｜近端 Put 显著偏重（P/C OI 分位 96%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-19（3D）±0.6% ｜ 10-20（4D）±0.7% ｜ 10-21（5D）±0.9% ｜ 10-22（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -810,857,350 | GEX Change vs 上次快照 125,800,679 | Flip: Primary Flip: 774.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 2740 / LOW 433 / INVALID 1635
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 774.60（全链重定价，覆盖 87%）
最近结构参考: Flip 775（现价低于该位 0.4%）
量化视角： 负 Gamma（8.11亿，历史分位 38%，中性区）｜负 Gamma 缓解（+1.26亿）｜现价位于 Flip 下方 0.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 770（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-19 655.0P — Vol 57,157 | 最新价 $0.03 | OI 3→57157 (ΔOI +57154张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增57154张（+1905133.3% vs前日OI），连续性待观察（方向未知）
10-30 760.0P — Vol 80,692 | 最新价 $3.66 | OI 22740→75524 (ΔOI +52784张) | ΔOI/Volume 65.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52784张（+232.1% vs前日OI），连续性待观察（方向未知）
10-19 660.0P — Vol 52,220 | 最新价 $0.03 | OI 65→52245 (ΔOI +52180张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52180张（+80276.9% vs前日OI），连续性待观察（方向未知）
10-30 745.0P — Vol 56,802 | 最新价 $1.72 | OI 25729→73004 (ΔOI +47275张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47275张（+183.7% vs前日OI），连续性待观察（方向未知）
10-20 731.0P — Vol 22,004 | 最新价 $0.14 | OI 29→19269 (ΔOI +19240张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19240张（+66344.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 228,633 张（Put 228,633 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $27M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 851.2k / P 2575.8k，今日成交量: C 498.8k / P 628.5k，平值价格ATM: C $0.97 / P $1.54 ｜ ATM IV 14.8%，预期波动 ±0.3%，Max Pain 770
Top ΔOI: P 754 +13,301 ｜ C 773 +11,275 ｜ C 779 +10,964

📆 Forward Expiration Structure

10-19  C +26.2k / P +201.9k ｜ Activity HIGH ｜ 3D
10-20  C +17.8k / P +45.5k ｜ Activity HIGH ｜ 4D
10-21  C +17.8k / P +43.8k ｜ Activity HIGH ｜ 5D
10-22  C +12.5k / P +10.6k ｜ Activity HIGH ｜ 6D

📆 10-19 Forward Structure
存量OI: C 94.1k / P 295.8k，今日变化ΔOI: C +26.2k / P +201.9k，平值价格ATM: C $2.02 / P $2.50 ｜ ATM IV 7.7%，净 delta 敞口 77k shares
Top ΔOI: P 655 +57,154 ｜ P 660 +52,180 ｜ P 731 +17,363
仓位参考: Max Pain 773 ｜ Call Wall 782（+1.3%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜ATM IV 7.7%｜历史 Rank 65%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 77,262 股

📆 10-20 Forward Structure
存量OI: C 62.3k / P 132.5k，今日变化ΔOI: C +17.8k / P +45.5k，平值价格ATM: C $2.60 / P $3.13 ｜ ATM IV 8.6%，净 delta 敞口 187k shares
Top ΔOI: P 731 +19,240 ｜ P 695 +8,642 ｜ C 784 +4,584
仓位参考: Max Pain 773 ｜ Call Wall 784（+1.6%，弱）（OI 5.9k） ｜ Put Wall 751（-2.7%，弱）（OI 12.4k）
量化解读： 存量 Put 重｜ATM IV 8.6%｜历史 Rank 65%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 187,431 股

📆 10-21 Forward Structure
存量OI: C 57.5k / P 123.1k，今日变化ΔOI: C +17.8k / P +43.8k，平值价格ATM: C $3.29 / P $3.45 ｜ ATM IV 9.3%，净 delta 敞口 196k shares
Top ΔOI: P 746 +9,044 ｜ P 748 +7,995
仓位参考: Max Pain 771 ｜ Call Wall 788（+2.1%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 9.3%｜历史 Rank 65%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 195,715 股

📆 10-22 Forward Structure
存量OI: C 32.6k / P 31.9k，今日变化ΔOI: C +12.5k / P +10.6k，平值价格ATM: C $3.85 / P $4.14 ｜ ATM IV 9.8%，净 delta 敞口 86k shares
Top ΔOI: C 804 +2,065 ｜ P 734 +1,617 ｜ C 802 +1,405
仓位参考: Max Pain 774 ｜ Call Wall 790（+2.4%，弱）（OI 1.6k） ｜ Put Wall 759（-1.6%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜ATM IV 9.8%｜历史 Rank 65%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 86,196 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SPY_morning.json