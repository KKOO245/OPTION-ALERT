# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $773.28 ｜ QQQ $725.20
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 220C ΔOI +5,307（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 216.47 → 今开 220.96（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 222.16 ｜ 低 217.66

Options: P/C成交量 0.53 | OI比 0.76 | ATM IV 48.6% | Skew 1.6pp | Term 0.82 | ExpMove ±2.5%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±2.5% ｜ 10-26（5D）±3.1% ｜ 10-28（7D）±3.9% ｜ 10-30（9D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 357,046,194 | GEX Change vs 上次快照 238,459,604 | Flip: Primary Flip: 213.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 781 / LOW 225 / INVALID 556
结构观察区: Primary Flip 213.08（全链重定价，覆盖 97%）
Call Wall 230（弱结构｜现价低于该位 4.2%）
最近结构参考: Flip 213（现价高于该位 3.4%）
量化视角： 正 Gamma（3.57亿，无历史分位）｜正 Gamma 增强（+2.38亿）｜现价位于 Flip 上方 3.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 218（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-21 222.5C — Vol 66,482 | 最新价 $0.23 | OI 11857→24512 (ΔOI +12655张) | ΔOI/Volume 19.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12655张（+106.7% vs前日OI），连续性待观察（方向未知）
10-21 220.0C — Vol 154,496 | 最新价 $0.60 | OI 11749→23980 (ΔOI +12231张) | ΔOI/Volume 7.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12231张（+104.1% vs前日OI），连续性待观察（方向未知）
10-21 190.0P — Vol 15,456 | 最新价 $0.01 | OI 3599→13816 (ΔOI +10217张) | ΔOI/Volume 66.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10217张（+283.9% vs前日OI），连续性待观察（方向未知）
10-21 225.0C — Vol 55,964 | 最新价 $0.09 | OI 11287→19787 (ΔOI +8500张) | ΔOI/Volume 15.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8500张（+75.3% vs前日OI），连续性待观察（方向未知）
10-21 215.0P — Vol 99,788 | 最新价 $1.25 | OI 4269→11557 (ΔOI +7288张) | ΔOI/Volume 7.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7288张（+170.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 50,891 张（Put 17,505 / Call 33,386），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 147.0k / P 111.9k，今日成交量: C 214.5k / P 114.0k，平值价格ATM: C $1.33 / P $0.99 ｜ ATM IV 48.6%，预期波动 ±1.1%，Max Pain 218
Top ΔOI: C 222 +12,655 ｜ C 220 +12,231 ｜ P 190 +10,217

📆 Forward Expiration Structure

10-23  C +21.7k / P +11.0k ｜ Activity HIGH ｜ 2D
10-26  C +9.6k / P +11.4k ｜ Activity HIGH ｜ 5D
10-28  C +3.3k / P +3.3k ｜ Activity HIGH ｜ 7D
10-30  C +18.4k / P +12.8k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 441.7k / P 355.4k，今日变化ΔOI: C +21.7k / P +11.0k，平值价格ATM: C $3.05 / P $2.56 ｜ ATM IV 40.1%，净 delta 敞口 925k shares
Top ΔOI: C 220 +5,307 ｜ C 222 +3,409
仓位参考: Max Pain 220 ｜ Call Wall 240（+8.9%，弱）（OI 58.3k） ｜ Put Wall 210（-4.7%，弱）（OI 18.6k）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 69%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 925,296 股

📆 10-26 Forward Structure
存量OI: C 39.7k / P 32.0k，今日变化ΔOI: C +9.6k / P +11.4k，平值价格ATM: C $3.69 / P $3.05 ｜ ATM IV 32.4%，净 delta 敞口 126k shares
Top ΔOI: P 200 +2,480 ｜ P 210 +1,738 ｜ P 220 +1,502
仓位参考: Max Pain 218 ｜ Call Wall 237.5（+7.7%）（OI 10.1k） ｜ Put Wall 200（-9.3%）（OI 7.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.47×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 126,270 股

📆 10-28 Forward Structure
存量OI: C 13.5k / P 12.4k，今日变化ΔOI: C +3.3k / P +3.3k，平值价格ATM: C $4.68 / P $4.00 ｜ ATM IV 34.9%，净 delta 敞口 80k shares
Top ΔOI: P 212 +1,227 ｜ C 222 +505 ｜ C 220 +503
仓位参考: Max Pain 218 ｜ Call Wall 230（+4.3%）（OI 4.8k） ｜ Put Wall 215（-2.5%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.9%｜历史 Rank 69%（近端代理）｜IV/RV 1.58×（近似）｜净 delta 敞口 正 79,585 股

📆 10-30 Forward Structure
存量OI: C 194.8k / P 169.4k，今日变化ΔOI: C +18.4k / P +12.8k，平值价格ATM: C $5.50 / P $4.71 ｜ ATM IV 36.4%，净 delta 敞口 391k shares
Top ΔOI: C 220 +3,755 ｜ C 230 +3,568
仓位参考: Max Pain 220 ｜ Call Wall 240（+8.9%）（OI 27.7k） ｜ Put Wall 200（-9.3%，弱）（OI 12.4k）
量化解读： 存量两侧均衡｜ATM IV 36.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.65×（近似）｜净 delta 敞口 正 391,209 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/NVDA_morning.json