# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.94
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 180C ΔOI +2,044（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 174.34 → 今开 175.76（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 177.66 ｜ 低 172.61

Options: P/C成交量 0.48 | OI比 0.84 | ATM IV 55.9% | Skew 0.9pp | Term 0.86 | ExpMove ±2.7%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.7% ｜ 09-25（8D）±5.8% ｜ 10-02（15D）±7.7% ｜ 10-09（22D）±9.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 105,696,079 | GEX Change vs 上次快照 18,929,309 | Flip: Primary Flip: 166.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 577 / LOW 84 / INVALID 159
结构观察区: Primary Flip 166.76（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 3.6%） | Call Wall 180（弱结构｜现价低于该位 2.1%）
最近结构参考: Call Wall 180（现价低于该位 2.1%）
量化视角： 正 Gamma（1.06亿，无历史分位）｜正 Gamma 增强（+1893万）｜现价位于 Flip 上方 5.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 160（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 165.0P — Vol 16,752 | 最新价 $0.44 | OI 10202→15405 (ΔOI +5203张) | ΔOI/Volume 31.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5203张（+51.0% vs前日OI），连续性待观察（方向未知）
09-18 180.0C — Vol 16,880 | 最新价 $1.01 | OI 31047→33091 (ΔOI +2044张) | ΔOI/Volume 12.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2044张（+6.6% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 21,732 | 最新价 $2.67 | OI 19537→21323 (ΔOI +1786张) | ΔOI/Volume 8.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1786张（+9.1% vs前日OI），连续性待观察（方向未知）
09-25 145.0P — Vol 2,152 | 最新价 $0.26 | OI 693→2368 (ΔOI +1675张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1675张（+241.7% vs前日OI），连续性待观察（方向未知）
10-16 250.0C — Vol 1,690 | 最新价 $0.17 | OI 4940→6412 (ΔOI +1472张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1472张（+29.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,180 张（Put 6,878 / Call 5,302），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +1.8k / P +3.6k ｜ Activity MEDIUM △ ｜ 1D
09-25  C +5.0k / P +4.3k ｜ Activity HIGH ｜ 8D
10-02  C +0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 15D
10-09  C +0.6k / P +0.4k ｜ Activity HIGH ｜ 22D

📆 09-18 Forward Structure
存量OI: C 350.5k / P 295.2k，今日变化ΔOI: C +1.8k / P +3.6k，平值价格ATM: C $3.14 / P $1.60 ｜ ATM IV 55.9%，净 delta 敞口 34k shares
Top ΔOI: P 165 +5,203 ｜ C 180 +2,044 ｜ P 160 -1,897
仓位参考: Max Pain 160 ｜ Call Wall 180（+2.2%）（OI 33.1k） ｜ Put Wall 160（-9.2%，弱）（OI 18.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.9%｜历史 Rank 75%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,700 股

📆 09-25 Forward Structure
存量OI: C 41.4k / P 47.3k，今日变化ΔOI: C +5.0k / P +4.3k，平值价格ATM: C $5.95 / P $4.35 ｜ ATM IV 48.1%，净 delta 敞口 132k shares
Top ΔOI: C 190 +1,080 ｜ C 180 +687
仓位参考: Max Pain 172 ｜ Call Wall 190（+7.9%，弱）（OI 4.8k） ｜ Put Wall 170（-3.5%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.1%｜历史 Rank 75%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 131,938 股

10-02（MEDIUM △）Top ΔOI: 160P +104 ｜ 190C +96
10-02（MEDIUM △）仓位参考: Max Pain 172 ｜ Call Wall 180（+2.2%，弱）（OI 2.9k） ｜ Put Wall 170（-3.5%）（OI 4.5k）

📆 10-09 Forward Structure
存量OI: C 10.7k / P 16.0k，今日变化ΔOI: C +0.6k / P +0.4k，平值价格ATM: C $9.10 / P $7.59 ｜ ATM IV 47.8%，净 delta 敞口 -4k shares
Top ΔOI: C 197 +253 ｜ P 180 +124 ｜ C 190 +124
仓位参考: Max Pain 170 ｜ Call Wall 190（+7.9%，弱）（OI 0.7k） ｜ Put Wall 170（-3.5%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.8%｜历史 Rank 75%（近端代理）｜净 delta 敞口 负 4,121 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 55.9% vs 09-25 48.1%（差 +7.8pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/PLTR_morning.json