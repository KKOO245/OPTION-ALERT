# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.36 ｜ QQQ $737.38
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 73.3% vs 10-09 60.1%（差 +13.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 180P ΔOI -2,185（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 186.41 → 今开 186.07（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 192.30 ｜ 低 185.88

Options: P/C成交量 0.22 | OI比 0.58 | ATM IV 73.3% | Skew -3.0pp | Term 0.91 | ExpMove ±3.5%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -3.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.22×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±3.5% ｜ 10-09（8D）±7.2% ｜ 10-16（15D）±10.6% ｜ 10-23（22D）±11.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,308,332 | GEX Change vs 上次快照 10,060,045 | Flip: Primary Flip: 182.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 505 / LOW 139 / INVALID 248
结构观察区: Primary Flip 182.58（全链重定价，覆盖 99%）
Call Wall 202（弱结构｜现价低于该位 7.0%）
最近结构参考: Flip 183（现价高于该位 3.2%）
量化视角： 正 Gamma（1231万，无历史分位）｜正 Gamma 增强（+1006万）｜现价位于 Flip 上方 3.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考） / 202（Call Wall，弱结构）。
• Gamma 区域：切换参考 183（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 200.0C — Vol 16,459 | 最新价 $0.56 | OI 3665→5722 (ΔOI +2057张) | ΔOI/Volume 12.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2057张（+56.1% vs前日OI），连续性待观察（方向未知）
10-02 205.0C — Vol 6,217 | 最新价 $0.28 | OI 3980→5544 (ΔOI +1564张) | ΔOI/Volume 25.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1564张（+39.3% vs前日OI），连续性待观察（方向未知）
10-09 200.0C — Vol 2,251 | 最新价 $2.68 | OI 1898→2938 (ΔOI +1040张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1040张（+54.8% vs前日OI），连续性待观察（方向未知）
10-02 190.0C — Vol 4,928 | 最新价 $2.35 | OI 1260→2029 (ΔOI +769张) | ΔOI/Volume 15.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增769张（+61.0% vs前日OI），连续性待观察（方向未知）
10-02 210.0C — Vol 3,324 | 最新价 $0.15 | OI 6178→6738 (ΔOI +560张) | ΔOI/Volume 16.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增560张（+9.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,990 张（Put 0 / Call 5,990），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +5.1k / P -1.9k ｜ Activity HIGH ｜ 1D
10-09  C +2.7k / P +1.9k ｜ Activity HIGH ｜ 8D
10-16  C +13 / P -0.4k ｜ Activity LOW ｜ 15D
10-23  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 78.0k / P 45.0k，今日变化ΔOI: C +5.1k / P -1.9k，平值价格ATM: C $3.25 / P $3.30 ｜ ATM IV 73.3%，净 delta 敞口 204k shares
Top ΔOI: P 180 -2,185 ｜ C 200 +2,057 ｜ C 205 +1,564
仓位参考: Max Pain 190 ｜ Call Wall 202.5（+7.5%，弱）（OI 16.1k） ｜ Put Wall 180（-4.4%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 73.3%｜历史 Rank 40%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 204,496 股

📆 10-09 Forward Structure
存量OI: C 12.7k / P 23.7k，今日变化ΔOI: C +2.7k / P +1.9k，平值价格ATM: C $7.05 / P $6.61 ｜ ATM IV 60.1%，净 delta 敞口 18k shares
Top ΔOI: C 200 +1,040 ｜ P 182 +376 ｜ P 187 +343
仓位参考: Max Pain 190 ｜ Call Wall 200（+6.2%）（OI 2.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 60.1%｜历史 Rank 40%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 18,377 股

10-16（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 200（+6.2%，弱）（OI 6.4k） ｜ Put Wall 200（+6.2%，弱）（OI 3.9k）

10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 190（+0.9%，弱）（OI 0.5k） ｜ Put Wall 192.5（+2.2%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 73.3% vs 10-09 60.1%（差 +13.2pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/COIN_morning.json