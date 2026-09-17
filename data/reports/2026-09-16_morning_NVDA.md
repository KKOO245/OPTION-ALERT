# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 220C ΔOI +8,388（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 212.17 → 今开 214.14（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 216.30 ｜ 低 213.31

Options: P/C成交量 0.47 | OI比 0.74 | ATM IV 46.7% | Skew 5.4pp | Term 0.71 | ExpMove ±2.5%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价中性（Skew 5.4pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±2.5% ｜ 09-21（5D）±3.0% ｜ 09-23（7D）±3.8% ｜ 09-25（9D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 412,594,585 | GEX Change vs 上次快照 270,486,356 | Flip: Primary Flip: 208.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 743 / LOW 205 / INVALID 592
结构观察区: Primary Flip 208.64（全链重定价，覆盖 99%）
Put Wall 200（现价高于该位 8.0%） | Call Wall 220（弱结构｜现价低于该位 1.9%）
最近结构参考: Call Wall 220（现价低于该位 1.9%）
量化视角： 正 Gamma（4.13亿，无历史分位）｜正 Gamma 增强（+2.70亿）｜现价位于 Flip 上方 3.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall） / 212（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 209（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 220.0C — Vol 47,647 | 最新价 $1.83 | OI 9132→35247 (ΔOI +26115张) | ΔOI/Volume 54.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26115张（+286.0% vs前日OI），连续性待观察（方向未知）
09-16 215.0C — Vol 211,873 | 最新价 $0.70 | OI 12115→36585 (ΔOI +24470张) | ΔOI/Volume 11.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24470张（+202.0% vs前日OI），连续性待观察（方向未知）
09-16 217.5C — Vol 74,326 | 最新价 $0.24 | OI 8629→17702 (ΔOI +9073张) | ΔOI/Volume 12.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9073张（+105.2% vs前日OI），连续性待观察（方向未知）
09-18 220.0C — Vol 49,657 | 最新价 $0.56 | OI 66061→74449 (ΔOI +8388张) | ΔOI/Volume 16.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8388张（+12.7% vs前日OI），连续性待观察（方向未知）
09-18 222.5C — Vol 24,346 | 最新价 $0.30 | OI 50883→58946 (ΔOI +8063张) | ΔOI/Volume 33.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8063张（+15.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 76,109 张（Put 0 / Call 76,109），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 173.1k / P 127.7k，今日成交量: C 364.2k / P 173.1k，平值价格ATM: C $1.56 / P $0.58 ｜ ATM IV 46.7%，预期波动 ±1.0%，Max Pain 212
Top ΔOI: C 215 +24,470 ｜ C 217 +9,073 ｜ C 212 +5,931

📆 Forward Expiration Structure

09-18  C +21.1k / P +10.9k ｜ Activity MEDIUM △ ｜ 2D
09-21  C +11.4k / P +8.2k ｜ Activity HIGH ｜ 5D
09-23  C +1.2k / P +3.6k ｜ Activity HIGH ｜ 7D
09-25  C +40.3k / P +18.7k ｜ Activity HIGH ｜ 9D

📆 09-18 Forward Structure
存量OI: C 1345.5k / P 1124.6k，今日变化ΔOI: C +21.1k / P +10.9k，平值价格ATM: C $3.30 / P $2.20 ｜ ATM IV 40.2%，净 delta 敞口 793k shares
Top ΔOI: C 220 +8,388 ｜ C 222 +8,063 ｜ C 225 +4,571
仓位参考: Max Pain 205 ｜ Call Wall 230（+6.5%，弱）（OI 95.5k） ｜ Put Wall 200（-7.4%，弱）（OI 58.9k）
量化解读： 存量 Call 重｜ATM IV 40.2%｜历史 Rank 61%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 792,724 股

📆 09-21 Forward Structure
存量OI: C 35.0k / P 30.8k，今日变化ΔOI: C +11.4k / P +8.2k，平值价格ATM: C $3.75 / P $2.79 ｜ ATM IV 31.6%，净 delta 敞口 341k shares
Top ΔOI: P 200 +4,792 ｜ C 217 +2,173 ｜ C 220 +1,743
仓位参考: Max Pain 212 ｜ Call Wall 230（+6.5%，弱）（OI 5.4k） ｜ Put Wall 200（-7.4%，弱）（OI 7.1k）
量化解读： 存量两侧均衡｜ATM IV 31.6%｜历史 Rank 61%（近端代理）｜IV/RV 0.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 341,452 股

📆 09-23 Forward Structure
存量OI: C 22.5k / P 9.2k，今日变化ΔOI: C +1.2k / P +3.6k，平值价格ATM: C $4.60 / P $3.50 ｜ ATM IV 33.0%，净 delta 敞口 69k shares
Top ΔOI: P 195 +2,153 ｜ C 230 -891 ｜ C 212 +678
仓位参考: Max Pain 215 ｜ Call Wall 230（+6.5%）（OI 8.8k） ｜ Put Wall 195（-9.7%）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.0%｜历史 Rank 61%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 68,771 股

📆 09-25 Forward Structure
存量OI: C 228.0k / P 159.1k，今日变化ΔOI: C +40.3k / P +18.7k，平值价格ATM: C $5.30 / P $4.05 ｜ ATM IV 33.6%，净 delta 敞口 1.2M shares
Top ΔOI: C 220 +26,115 ｜ C 225 +4,646 ｜ C 212 +2,875
仓位参考: Max Pain 218 ｜ Call Wall 220（+1.9%）（OI 35.2k） ｜ Put Wall 210（-2.7%，弱）（OI 17.4k）
量化解读： 存量 Call 重｜ATM IV 33.6%｜历史 Rank 61%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 1,188,671 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 40.2% vs 09-21 31.6%（差 +8.7pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/NVDA_morning.json