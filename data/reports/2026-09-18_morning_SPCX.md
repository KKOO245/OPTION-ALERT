# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $759.22 ｜ QQQ $717.44
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
🟡 **近现价集中开仓**: 09-25 150P ΔOI +8,037（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 154.81 → 今开 154.66（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 156.60 ｜ 低 150.91

Options: P/C成交量 0.49 | OI比 0.97 | ATM IV 77.5% | Skew -0.6pp | Term 0.61 | ExpMove ±5.4%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±5.4% ｜ 10-02（14D）±7.6% ｜ 10-09（21D）±9.2% ｜ 10-16（28D）±10.5%
   ⇒ IV–VIX Spread: +62.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 41,986,269 | GEX Change vs 上次快照 -169,433,487 | Flip: Primary Flip: 149.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 602 / LOW 104 / INVALID 368
结构观察区: Primary Flip 149.90（全链重定价，覆盖 99%）
Call Wall 160（弱结构｜现价低于该位 5.1%）
最近结构参考: Flip 150（现价高于该位 1.3%）
量化视角： 正 Gamma（4199万，无历史分位）｜正 Gamma 减弱（1.69亿）｜现价位于 Flip 上方 1.31%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 155.0P — Vol 14,814 | 最新价 $8.60 | OI 1670→35469 (ΔOI +33799张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33799张（+2023.9% vs前日OI），连续性待观察（方向未知）
10-16 135.0P — Vol 14,734 | 最新价 $1.90 | OI 19967→44263 (ΔOI +24296张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24296张（+121.7% vs前日OI），连续性待观察（方向未知）
09-18 147.0P — Vol 289 | 最新价 $0.11 | OI 1727→25830 (ΔOI +24103张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24103张（+1395.7% vs前日OI），连续性待观察（方向未知）
09-18 148.0P — Vol 154 | 最新价 $0.16 | OI 2575→19080 (ΔOI +16505张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16505张（+641.0% vs前日OI），连续性待观察（方向未知）
09-18 152.5P — Vol 7,035 | 最新价 $0.81 | OI 4488→13320 (ΔOI +8832张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8832张（+196.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 107,535 张（Put 107,535 / Call 0），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $34M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 688.5k / P 669.0k，今日成交量: C 167.7k / P 82.4k，平值价格ATM: C $0.91 / P $1.65 ｜ ATM IV 77.5%，预期波动 ±1.7%，Max Pain 150
Top ΔOI: P 147 +24,103 ｜ P 148 +16,505 ｜ C 155 -16,012

📆 Forward Expiration Structure

09-25  C +10.3k / P +19.5k ｜ Activity HIGH ｜ 7D
10-02  C +4.4k / P +2.7k ｜ Activity HIGH ｜ 14D
10-09  C +3.0k / P +2.0k ｜ Activity HIGH ｜ 21D
10-16  C +23.7k / P +65.1k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 99.7k / P 138.7k，今日变化ΔOI: C +10.3k / P +19.5k，平值价格ATM: C $3.75 / P $4.40 ｜ ATM IV 47.5%，净 delta 敞口 -480k shares
Top ΔOI: P 150 +8,037 ｜ P 142 +3,186
仓位参考: Max Pain 150 ｜ Call Wall 160（+5.4%，弱）（OI 10.2k） ｜ Put Wall 140（-7.8%，弱）（OI 12.8k）
量化解读： 存量 Put 重｜ATM IV 47.5%｜历史 Rank 97%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 480,034 股

📆 10-02 Forward Structure
存量OI: C 39.5k / P 49.5k，今日变化ΔOI: C +4.4k / P +2.7k，平值价格ATM: C $5.50 / P $6.00 ｜ ATM IV 48.0%，净 delta 敞口 -92k shares
Top ΔOI: C 160 +1,410 ｜ P 133 -1,025 ｜ P 155 +1,007
仓位参考: Max Pain 150 ｜ Call Wall 160（+5.4%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.0%｜历史 Rank 97%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 92,135 股

📆 10-09 Forward Structure
存量OI: C 19.7k / P 19.7k，今日变化ΔOI: C +3.0k / P +2.0k，平值价格ATM: C $6.85 / P $7.15 ｜ ATM IV 47.4%，净 delta 敞口 -27k shares
Top ΔOI: C 160 +518 ｜ P 157 +480
仓位参考: Max Pain 149 ｜ Call Wall 165（+8.7%，弱）（OI 1.9k） ｜ Put Wall 140（-7.8%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.4%｜历史 Rank 97%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 26,891 股

📆 10-16 Forward Structure
存量OI: C 308.2k / P 346.0k，今日变化ΔOI: C +23.7k / P +65.1k，平值价格ATM: C $9.10 / P $6.87 ｜ ATM IV 47.4%，净 delta 敞口 -344k shares
Top ΔOI: P 155 +33,799 ｜ P 135 +24,296 ｜ C 115 +6,469
仓位参考: Max Pain 145 ｜ Call Wall 160（+5.4%，弱）（OI 32.7k） ｜ Put Wall 155（+2.1%，弱）（OI 35.5k）
量化解读： 存量两侧均衡｜ATM IV 47.4%｜历史 Rank 97%（近端代理）｜净 delta 敞口 负 343,795 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SPCX_morning.json