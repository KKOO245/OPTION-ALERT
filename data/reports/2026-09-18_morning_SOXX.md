# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.85 ｜ QQQ $nan
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
🟡 **近现价集中开仓**: 09-25 520C ΔOI +199（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 524.2）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 519.10 → 今开 523.06（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 526.94 ｜ 低 522.87

Options: P/C成交量 2.70 | OI比 0.86 | ATM IV 29.2% | Skew -0.6pp | Term 1.20 | ExpMove ±4.1%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常偏陡（Term 1.20）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.70×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±4.1% ｜ 10-02（14D）±5.8% ｜ 10-09（21D）±9.5% ｜ 10-16（28D）±8.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 5,170,918 | GEX Change vs 上次快照 18,213,826 | Flip: Candidates 524.16 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 524 / LOW 397 / INVALID 731
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈524（全链重定价，覆盖 80%，CONDITIONAL）
Put Wall 480（弱结构｜现价高于该位 9.5%） | Call Wall 575（弱结构｜现价低于该位 8.6%）
最近结构参考: Flip 524（现价高于该位 0.3%）
量化视角： 正 Gamma（517万，无历史分位）｜由负转正（+1821万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 480（Put Wall，弱结构） / 515（MaxPain，仅结算参考）；上方 575（Call Wall，弱结构）。
• Gamma 区域：切换参考 524（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 480.0P — Vol 7,787 | 最新价 $6.82 | OI 5192→11149 (ΔOI +5957张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5957张（+114.7% vs前日OI），连续性待观察（方向未知）
10-16 510.0P — Vol 3,798 | 最新价 $15.46 | OI 2790→4973 (ΔOI +2183张) | ΔOI/Volume 57.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2183张（+78.2% vs前日OI），连续性待观察（方向未知）
10-16 450.0P — Vol 697 | 最新价 $2.92 | OI 5858→6345 (ΔOI +487张) | ΔOI/Volume 69.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增487张（+8.3% vs前日OI），连续性待观察（方向未知）
10-16 500.0P — Vol 637 | 最新价 $11.92 | OI 4128→4577 (ΔOI +449张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增449张（+10.9% vs前日OI），连续性待观察（方向未知）
10-02 520.0C — Vol 784 | 最新价 $14.50 | OI 74→475 (ΔOI +401张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增401张（+541.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,477 张（Put 9,076 / Call 401），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 104.6k / P 90.2k，今日成交量: C 3.0k / P 8.0k，平值价格ATM: C $1.00 / P $6.80 ｜ ATM IV 29.2%，预期波动 ±1.5%，Max Pain 515
Top ΔOI: P 560 -550 ｜ P 540 -548 ｜ P 515 +350

📆 Forward Expiration Structure

09-25  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 7D
10-02  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 14D
10-09  C +76 / P +48 ｜ Activity MEDIUM △ ｜ 21D
10-16  C -0.2k / P +9.0k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 10.4k / P 15.1k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $7.40 / P $14.30 ｜ ATM IV 31.5%，净 delta 敞口 3k shares
Top ΔOI: P 490 -250 ｜ C 520 +199
仓位参考: Max Pain 520 ｜ Put Wall 480（-8.7%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.5%｜历史 Rank 32%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,497 股

📆 10-02 Forward Structure
存量OI: C 11.3k / P 10.5k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $12.49 / P $18.20 ｜ ATM IV 33.9%，净 delta 敞口 21k shares
Top ΔOI: C 520 +401 ｜ P 542 +100 ｜ C 517 +71
仓位参考: Max Pain 512 ｜ Call Wall 542.5（+3.2%，弱）（OI 2.8k） ｜ Put Wall 475（-9.6%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜ATM IV 33.9%｜历史 Rank 32%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 21,365 股

10-09（MEDIUM △）Top ΔOI: 522C +31 ｜ 525C +16
10-09（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 525（-0.1%）（OI 1.6k） ｜ Put Wall 485（-7.7%，弱）（OI 0.2k）

📆 10-16 Forward Structure
存量OI: C 41.5k / P 79.9k，今日变化ΔOI: C -0.2k / P +9.0k，平值价格ATM: C $18.86 / P $24.25 ｜ ATM IV 35.0%，净 delta 敞口 -248k shares
Top ΔOI: P 480 +5,957 ｜ P 510 +2,183 ｜ P 450 +487
仓位参考: Max Pain 515 ｜ Call Wall 550（+4.6%，弱）（OI 3.5k） ｜ Put Wall 480（-8.7%）（OI 11.1k）
量化解读： 存量 Put 重｜ATM IV 35.0%｜历史 Rank 32%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 247,934 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SOXX_morning.json