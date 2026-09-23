# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-23 62C ΔOI +2,736（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 59.63 → 今开 59.31（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 59.67 ｜ 低 59.26

Options: P/C成交量 0.45 | OI比 0.71 | ATM IV 35.3% | Skew -2.6pp | Term 1.00 | ExpMove ±1.7%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-23（1D）±1.7% ｜ 09-25（3D）±2.6% ｜ 09-28（6D）±3.2% ｜ 09-30（8D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 83,495,193 | GEX Change vs 上次快照 206,146 | Flip: Primary Flip: 57.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 820 / LOW 173 / INVALID 361
结构观察区: Primary Flip 57.09（全链重定价，覆盖 98%）
Put Wall 60（弱结构｜现价低于该位 0.8%）
最近结构参考: Put Wall 60（现价低于该位 0.8%）
量化视角： 正 Gamma（8350万，无历史分位）｜正 Gamma 增强（+21万）｜现价位于 Flip 上方 4.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 59（MaxPain，仅结算参考）；上方 60（Put Wall，弱结构）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 56.0P — Vol 2,945 | 最新价 $0.28 | OI 833→3759 (ΔOI +2926张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2926张（+351.3% vs前日OI），连续性待观察（方向未知）
09-23 62.0C — Vol 3,625 | 最新价 $0.07 | OI 868→3604 (ΔOI +2736张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2736张（+315.2% vs前日OI），连续性待观察（方向未知）
10-16 59.0P — Vol 3,516 | 最新价 $1.79 | OI 6443→9141 (ΔOI +2698张) | ΔOI/Volume 76.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2698张（+41.9% vs前日OI），连续性待观察（方向未知）
10-02 60.0C — Vol 2,131 | 最新价 $1.34 | OI 5926→7607 (ΔOI +1681张) | ΔOI/Volume 78.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1681张（+28.4% vs前日OI），连续性待观察（方向未知）
10-02 59.0P — Vol 1,499 | 最新价 $1.08 | OI 609→1938 (ΔOI +1329张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1329张（+218.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,370 张（Put 6,953 / Call 4,417），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-23  C +11.0k / P +4.8k ｜ Activity HIGH ｜ 1D
09-25  C +5.2k / P +4.0k ｜ Activity MEDIUM △ ｜ 3D
09-28  C +1.3k / P +2.4k ｜ Activity HIGH ｜ 6D
09-30  C +0.8k / P +0.6k ｜ Activity MEDIUM △ ｜ 8D

📆 09-23 Forward Structure
存量OI: C 25.2k / P 18.0k，今日变化ΔOI: C +11.0k / P +4.8k，平值价格ATM: C $0.46 / P $0.55 ｜ ATM IV 35.3%，净 delta 敞口 29k shares
Top ΔOI: C 62 +2,736 ｜ C 60 +1,231 ｜ P 59 +1,195
仓位参考: Max Pain 59 ｜ Call Wall 62（+4.2%）（OI 3.6k） ｜ Put Wall 55（-7.5%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 35.3%｜历史 Rank 57%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,308 股

09-25（MEDIUM △）Top ΔOI: 60C +1,071 ｜ 55P +646
09-25（MEDIUM △）仓位参考: Max Pain 60 ｜ Put Wall 55（-7.5%，弱）（OI 4.7k）

📆 09-28 Forward Structure
存量OI: C 6.2k / P 6.3k，今日变化ΔOI: C +1.3k / P +2.4k，平值价格ATM: C $0.99 / P $0.91 ｜ ATM IV 29.7%，净 delta 敞口 -2k shares
Top ΔOI: P 56 +1,229 ｜ C 58 +398 ｜ P 60 +350
仓位参考: Max Pain 60 ｜ Call Wall 62.5（+5.1%）（OI 2.2k） ｜ Put Wall 56（-5.9%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 29.7%｜历史 Rank 57%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,716 股

09-30（MEDIUM △）Top ΔOI: 58P +899 ｜ 73P -422
09-30（MEDIUM △）仓位参考: Max Pain 62 ｜ Put Wall 58（-2.5%，弱）（OI 3.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SLV_morning.json