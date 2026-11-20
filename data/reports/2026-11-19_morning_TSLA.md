# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 405C ΔOI +3,016（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 383.72 → 今开 389.90（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 393.60 ｜ 低 383.51

Options: P/C成交量 0.51 | OI比 1.40 | ATM IV 58.6% | Skew 5.8pp | Term 0.61 | ExpMove ±2.7%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价中性（Skew 5.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.7% ｜ 11-23（4D）±4.1% ｜ 11-25（6D）±5.1% ｜ 11-27（8D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 60,239,676 | GEX Change vs 上次快照 19,936,271 | Flip: Primary Flip: 377.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1251 / LOW 293 / INVALID 894
结构观察区: Primary Flip 377.40（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 3.3%）
最近结构参考: Flip 377（现价高于该位 2.5%）
量化视角： 正 Gamma（6024万，无历史分位）｜正 Gamma 增强（+1994万）｜现价位于 Flip 上方 2.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 378（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 377（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 405.0C — Vol 11,089 | 最新价 $0.84 | OI 8659→11675 (ΔOI +3016张) | ΔOI/Volume 27.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3016张（+34.8% vs前日OI），连续性待观察（方向未知）
11-23 312.5P — Vol 3,011 | 最新价 $0.18 | OI 9→3011 (ΔOI +3002张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3002张（+33355.6% vs前日OI），连续性待观察（方向未知）
11-20 232.5P — Vol 3,349 | 最新价 $0.04 | OI 23→3005 (ΔOI +2982张) | ΔOI/Volume 89.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2982张（+12965.2% vs前日OI），连续性待观察（方向未知）
11-20 400.0C — Vol 20,280 | 最新价 $1.50 | OI 26314→28766 (ΔOI +2452张) | ΔOI/Volume 12.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2452张（+9.3% vs前日OI），连续性待观察（方向未知）
11-20 390.0P — Vol 17,850 | 最新价 $10.46 | OI 5925→8256 (ΔOI +2331张) | ΔOI/Volume 13.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2331张（+39.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,783 张（Put 8,315 / Call 5,468），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +12.2k / P +16.4k ｜ Activity HIGH ｜ 1D
11-23  C +2.3k / P +4.8k ｜ Activity HIGH ｜ 4D
11-25  C +1.2k / P +2.6k ｜ Activity HIGH ｜ 6D
11-27  C +3.4k / P +3.5k ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 375.5k / P 524.6k，今日变化ΔOI: C +12.2k / P +16.4k，平值价格ATM: C $5.00 / P $5.55 ｜ ATM IV 58.6%，净 delta 敞口 197k shares
Top ΔOI: C 405 +3,016 ｜ C 400 +2,452
仓位参考: Max Pain 378 ｜ Call Wall 400（+3.4%，弱）（OI 28.8k）
量化解读： 存量 Put 重｜ATM IV 58.6%｜历史 Rank 69%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 196,838 股

📆 11-23 Forward Structure
存量OI: C 26.3k / P 16.8k，今日变化ΔOI: C +2.3k / P +4.8k，平值价格ATM: C $7.44 / P $8.40 ｜ ATM IV 45.1%，净 delta 敞口 16k shares
Top ΔOI: C 410 +546
仓位参考: Max Pain 385 ｜ Put Wall 357.5（-7.6%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.1%｜历史 Rank 69%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 16,303 股

📆 11-25 Forward Structure
存量OI: C 5.0k / P 7.3k，今日变化ΔOI: C +1.2k / P +2.6k，平值价格ATM: C $9.75 / P $10.05 ｜ ATM IV 48.2%，净 delta 敞口 -49k shares
Top ΔOI: P 382 +711 ｜ P 385 +563
仓位参考: Max Pain 385 ｜ Call Wall 400（+3.4%，弱）（OI 0.6k） ｜ Put Wall 382.5（-1.2%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 48.2%｜历史 Rank 69%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 49,040 股

📆 11-27 Forward Structure
存量OI: C 65.4k / P 60.3k，今日变化ΔOI: C +3.4k / P +3.5k，平值价格ATM: C $10.40 / P $10.64 ｜ ATM IV 45.5%，净 delta 敞口 18k shares
Top ΔOI: C 425 +752
仓位参考: Max Pain 375 ｜ Call Wall 410（+6.0%）（OI 9.4k） ｜ Put Wall 350（-9.6%，弱）（OI 2.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.5%｜历史 Rank 69%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 17,575 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/TSLA_morning.json