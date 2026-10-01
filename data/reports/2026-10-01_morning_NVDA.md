# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.23 ｜ QQQ $737.58
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
🟡 **近现价集中开仓**: 10-05 235C ΔOI +3,095（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 230P ΔOI +5,005 占该期限总 OI 16.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 228.38 → 今开 229.95（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 231.91 ｜ 低 228.38

Options: P/C成交量 0.49 | OI比 0.74 | ATM IV 37.0% | Skew 2.8pp | Term 0.86 | ExpMove ±1.8%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±1.8% ｜ 10-05（4D）±2.4% ｜ 10-07（6D）±3.2% ｜ 10-09（8D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 507,094,395 | GEX Change vs 上次快照 3,786,497 | Flip: Primary Flip: 219.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 713 / LOW 185 / INVALID 422
结构观察区: Primary Flip 219.85（全链重定价，覆盖 98%）
Call Wall 250（弱结构｜现价低于该位 8.0%）
最近结构参考: Flip 220（现价高于该位 4.6%）
量化视角： 正 Gamma（5.07亿，无历史分位）｜正 Gamma 增强（+379万）｜现价位于 Flip 上方 4.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 228（MaxPain，仅结算参考）；上方 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 220（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 220.0P — Vol 19,144 | 最新价 $1.55 | OI 6433→20799 (ΔOI +14366张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14366张（+223.3% vs前日OI），连续性待观察（方向未知）
10-09 207.5P — Vol 15,116 | 最新价 $0.36 | OI 1828→15419 (ΔOI +13591张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13591张（+743.5% vs前日OI），连续性待观察（方向未知）
10-02 247.5C — Vol 54,555 | 最新价 $0.01 | OI 14326→22831 (ΔOI +8505张) | ΔOI/Volume 15.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8505张（+59.4% vs前日OI），连续性待观察（方向未知）
10-02 245.0C — Vol 62,190 | 最新价 $0.03 | OI 27161→35481 (ΔOI +8320张) | ΔOI/Volume 13.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8320张（+30.6% vs前日OI），连续性待观察（方向未知）
10-02 250.0C — Vol 31,993 | 最新价 $0.01 | OI 63280→70060 (ΔOI +6780张) | ΔOI/Volume 21.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6780张（+10.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 51,562 张（Put 27,957 / Call 23,605），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +42.5k / P +5.9k ｜ Activity HIGH ｜ 1D
10-05  C +7.0k / P +13.3k ｜ Activity HIGH ｜ 4D
10-07  C +4.2k / P +9.2k ｜ Activity HIGH ｜ 6D
10-09  C +11.2k / P +44.3k ｜ Activity HIGH ｜ 8D

📆 10-02 Forward Structure
存量OI: C 533.5k / P 394.5k，今日变化ΔOI: C +42.5k / P +5.9k，平值价格ATM: C $2.28 / P $1.74 ｜ ATM IV 37.0%，净 delta 敞口 -377k shares
Top ΔOI: P 215 -10,426 ｜ C 247 +8,505 ｜ C 245 +8,320
仓位参考: Max Pain 228 ｜ Call Wall 227.5（-1.0%，弱）（OI 78.1k） ｜ Put Wall 230（+0.0%，弱）（OI 22.6k）
量化解读： 存量 Call 重｜ATM IV 37.0%｜历史 Rank 26%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 376,960 股

📆 10-05 Forward Structure
存量OI: C 49.3k / P 38.9k，今日变化ΔOI: C +7.0k / P +13.3k，平值价格ATM: C $3.05 / P $2.43 ｜ ATM IV 27.5%，净 delta 敞口 -12k shares
Top ΔOI: C 235 +3,095 ｜ P 215 +1,640
仓位参考: Max Pain 225 ｜ Call Wall 235（+2.2%）（OI 10.3k） ｜ Put Wall 220（-4.3%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.5%｜历史 Rank 26%（近端代理）｜IV/RV 1.15×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 11,882 股

📆 10-07 Forward Structure
存量OI: C 14.9k / P 16.0k，今日变化ΔOI: C +4.2k / P +9.2k，平值价格ATM: C $3.98 / P $3.30 ｜ ATM IV 30.0%，净 delta 敞口 -184k shares
Top ΔOI: P 230 +5,005 ｜ P 210 +1,056 ｜ C 242 +824
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+7.7%）（OI 3.8k） ｜ Put Wall 230（+0.0%）（OI 5.5k）
量化解读： 存量两侧均衡｜ATM IV 30.0%｜历史 Rank 26%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 184,461 股

📆 10-09 Forward Structure
存量OI: C 132.6k / P 188.6k，今日变化ΔOI: C +11.2k / P +44.3k，平值价格ATM: C $4.66 / P $3.90 ｜ ATM IV 31.1%，净 delta 敞口 -557k shares
Top ΔOI: P 220 +14,366 ｜ P 207 +13,591 ｜ P 230 +5,969
仓位参考: Max Pain 225 ｜ Call Wall 250（+8.7%，弱）（OI 17.6k） ｜ Put Wall 220（-4.3%，弱）（OI 20.8k）
量化解读： 存量 Put 重｜ATM IV 31.1%｜历史 Rank 26%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 负 556,751 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 37.0% vs 10-05 27.5%（差 +9.6pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/NVDA_morning.json