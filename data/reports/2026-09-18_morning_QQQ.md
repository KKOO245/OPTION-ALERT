# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $759.22 ｜ QQQ $717.51
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-21 715P ΔOI +13,509（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-24 655P ΔOI +7,773 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 716.92 → 今开 718.84（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 719.54 ｜ 低 715.90

Options: P/C成交量 1.19 | OI比 1.33 | ATM IV 17.5% | Skew 2.4pp | Term 0.96 | ExpMove ±0.8%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常（Term 0.96）｜保护溢价中性（Skew 2.4pp）｜当日成交偏 Put（P/C量 1.19）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.19×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.33×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 53% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 53%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-21（3D）±0.8% ｜ 09-22（4D）±1.1% ｜ 09-23（5D）±1.3% ｜ 09-24（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 12,538,280 | GEX Change vs 上次快照 -169,915,048 | Flip: Primary Flip: 716.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 2836 / LOW 435 / INVALID 1965
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 716.86（全链重定价，覆盖 88%）
Put Wall 690（弱结构｜现价高于该位 3.9%） | Call Wall 720（弱结构｜现价低于该位 0.4%）
最近结构参考: Flip 717（现价高于该位 0.0%）
量化视角： 正 Gamma（1254万，历史分位 53%，中性区）｜正 Gamma 减弱（1.70亿）｜现价位于 Flip 上方 0.01%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 690（Put Wall，弱结构） / 701（MaxPain，仅结算参考）；上方 720（Call Wall，弱结构）。
• Gamma 区域：切换参考 717（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 705.0P — Vol 231 | 最新价 $8.15 | OI 13301→30645 (ΔOI +17344张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17344张（+130.4% vs前日OI），连续性待观察（方向未知）
09-21 715.0P — Vol 1,464 | 最新价 $1.68 | OI 7266→20775 (ΔOI +13509张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13509张（+185.9% vs前日OI），连续性待观察（方向未知）
10-16 660.0P — Vol 41 | 最新价 $2.23 | OI 22338→34383 (ΔOI +12045张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12045张（+53.9% vs前日OI），连续性待观察（方向未知）
10-02 690.0P — Vol 37 | 最新价 $2.31 | OI 27918→39732 (ΔOI +11814张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11814张（+42.3% vs前日OI），连续性待观察（方向未知）
10-02 725.0C — Vol 117 | 最新价 $6.01 | OI 1336→11487 (ΔOI +10151张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10151张（+759.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 64,863 张（Put 54,712 / Call 10,151），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $22M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 1186.9k / P 1576.4k，今日成交量: C 610.6k / P 728.3k，平值价格ATM: C $1.17 / P $1.46 ｜ ATM IV 17.5%，预期波动 ±0.4%，Max Pain 701
Top ΔOI: P 700 -16,210 ｜ P 716 +10,108 ｜ C 710 -8,420

📆 Forward Expiration Structure

09-21  C +31.1k / P +55.7k ｜ Activity HIGH ｜ 3D
09-22  C +13.1k / P +9.9k ｜ Activity HIGH ｜ 4D
09-23  C +6.1k / P +12.4k ｜ Activity HIGH ｜ 5D
09-24  C +7.9k / P +19.9k ｜ Activity HIGH ｜ 6D

📆 09-21 Forward Structure
存量OI: C 62.9k / P 153.6k，今日变化ΔOI: C +31.1k / P +55.7k，平值价格ATM: C $2.33 / P $3.30 ｜ ATM IV 9.8%，净 delta 敞口 -818k shares
Top ΔOI: P 715 +13,509 ｜ P 710 +7,470 ｜ C 735 +5,980
仓位参考: Max Pain 715 ｜ Call Wall 735（+2.5%）（OI 8.2k） ｜ Put Wall 715（-0.3%）（OI 20.8k）
量化解读： 存量 Put 重｜ATM IV 9.8%｜历史 Rank 45%（近端代理）｜IV/RV 0.78×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 818,310 股

📆 09-22 Forward Structure
存量OI: C 39.5k / P 40.5k，今日变化ΔOI: C +13.1k / P +9.9k，平值价格ATM: C $3.28 / P $4.22 ｜ ATM IV 11.9%，净 delta 敞口 -21k shares
Top ΔOI: C 740 +1,298
仓位参考: Max Pain 713 ｜ Call Wall 758（+5.7%，弱）（OI 3.4k） ｜ Put Wall 685（-4.5%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.9%｜历史 Rank 45%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 21,134 股

📆 09-23 Forward Structure
存量OI: C 23.8k / P 36.8k，今日变化ΔOI: C +6.1k / P +12.4k，平值价格ATM: C $4.16 / P $4.97 ｜ ATM IV 13.1%，净 delta 敞口 -213k shares
Top ΔOI: P 697 +2,411 ｜ P 717 +1,520
仓位参考: Max Pain 714 ｜ Call Wall 735（+2.5%，弱）（OI 2.2k） ｜ Put Wall 697（-2.8%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 13.1%｜历史 Rank 45%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 212,820 股

📆 09-24 Forward Structure
存量OI: C 16.9k / P 35.7k，今日变化ΔOI: C +7.9k / P +19.9k，平值价格ATM: C $4.83 / P $5.45 ｜ ATM IV 14.0%，净 delta 敞口 -144k shares
Top ΔOI: P 655 +7,773 ｜ C 729 +1,302 ｜ P 699 +1,262
仓位参考: Max Pain 715 ｜ Call Wall 729（+1.7%，弱）（OI 1.4k） ｜ Put Wall 655（-8.6%）（OI 7.8k）
量化解读： 存量 Put 重｜ATM IV 14.0%｜历史 Rank 45%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 143,940 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/QQQ_morning.json