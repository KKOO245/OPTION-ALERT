# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.74 ｜ QQQ $721.45
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 141C ΔOI +11,861（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 132.25 → 今开 136.58（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 147.22 ｜ 低 136.43

Options: P/C成交量 0.51 | OI比 0.59 | ATM IV 125.4% | Skew -5.1pp | Term 0.55 | ExpMove ±8.1%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±8.1% ｜ 10-02（14D）±10.8% ｜ 10-09（21D）±13.5% ｜ 10-16（28D）±14.9%
   ⇒ IV–VIX Spread: +109.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 119,741,594 | GEX Change vs 上次快照 35,207,623 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 807 / LOW 72 / INVALID 325
结构观察区: NO_CROSS
量化视角： 正 Gamma（1.20亿，无历史分位）｜正 Gamma 增强（+3521万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 141.0C — Vol 147 | 最新价 $5.00 | OI 248→12109 (ΔOI +11861张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11861张（+4782.7% vs前日OI），连续性待观察（方向未知）
09-25 70.0P — Vol 12,412（Yahoo补） | 最新价 $0.02 | OI 1613→13317 (ΔOI +11704张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11704张（+725.6% vs前日OI），连续性待观察（方向未知）
09-25 135.0C — Vol 186 | 最新价 $8.35 | OI 1634→11243 (ΔOI +9609张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9609张（+588.1% vs前日OI），连续性待观察（方向未知）
09-25 136.0C — Vol 426 | 最新价 $7.27 | OI 531→2846 (ΔOI +2315张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2315张（+436.0% vs前日OI），连续性待观察（方向未知）
09-18 128.0P — Vol 151 | 最新价 $0.05 | OI 1519→3542 (ΔOI +2023张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2023张（+133.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 37,512 张（Put 13,727 / Call 23,785），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 481.0k / P 281.7k，今日成交量: C 167.7k / P 84.9k，平值价格ATM: C $1.96 / P $1.88 ｜ ATM IV 125.4%，预期波动 ±2.6%，Max Pain 120
Top ΔOI: C 140 -3,409 ｜ P 128 +2,023 ｜ C 146 -1,593

📆 Forward Expiration Structure

09-25  C +29.7k / P +18.8k ｜ Activity HIGH ｜ 7D
10-02  C +0.7k / P +4.7k ｜ Activity HIGH ｜ 14D
10-09  C +1.0k / P +3.1k ｜ Activity HIGH ｜ 21D
10-16  C +2.4k / P +1.5k ｜ Activity MEDIUM △ ｜ 28D

📆 09-25 Forward Structure
存量OI: C 68.7k / P 83.5k，今日变化ΔOI: C +29.7k / P +18.8k，平值价格ATM: C $6.10 / P $5.70 ｜ ATM IV 71.7%，净 delta 敞口 1.9M shares
Top ΔOI: C 141 +11,861 ｜ C 135 +9,609
仓位参考: Max Pain 129 ｜ Call Wall 141（-3.7%，弱）（OI 12.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.7%｜历史 Rank 92%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,947,010 股

📆 10-02 Forward Structure
存量OI: C 27.2k / P 49.0k，今日变化ΔOI: C +0.7k / P +4.7k，平值价格ATM: C $8.33 / P $7.54 ｜ ATM IV 69.6%，净 delta 敞口 46k shares
Top ΔOI: C 160 +872
仓位参考: Max Pain 130 ｜ Call Wall 145（-1.0%，弱）（OI 2.9k） ｜ Put Wall 135（-7.8%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 69.6%｜历史 Rank 92%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,433 股

📆 10-09 Forward Structure
存量OI: C 9.7k / P 29.1k，今日变化ΔOI: C +1.0k / P +3.1k，平值价格ATM: C $10.25 / P $9.46 ｜ ATM IV 69.3%，净 delta 敞口 28k shares
仓位参考: Max Pain 135 ｜ Call Wall 150（+2.4%，弱）（OI 1.2k） ｜ Put Wall 135（-7.8%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 69.3%｜历史 Rank 92%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,260 股

10-16（MEDIUM △）Top ΔOI: 145C +532 ｜ 130P +430
10-16（MEDIUM △）仓位参考: Max Pain 100 ｜ Call Wall 150（+2.4%，弱）（OI 9.4k） ｜ Put Wall 135（-7.8%，弱）（OI 3.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/MSTR_morning.json