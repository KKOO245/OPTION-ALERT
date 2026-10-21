# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.52
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 180C ΔOI +1,129（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 171.45 → 今开 176.07（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 178.85 ｜ 低 164.00

Options: P/C成交量 0.43 | OI比 0.62 | ATM IV 106.1% | Skew 2.3pp | Term 0.87 | ExpMove ±6.7%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 2.3pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±6.7% ｜ 10-30（9D）±12.9% ｜ 11-06（16D）±15.4% ｜ 11-13（23D）±19.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,947,918 | GEX Change vs 上次快照 4,451,375 | Flip: Primary Flip: 174.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 552 / LOW 59 / INVALID 199
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 174.09（全链重定价，覆盖 100%）
最近结构参考: Flip 174（现价低于该位 1.5%）
量化视角： 负 Gamma（295万，无历史分位）｜负 Gamma 缓解（+445万）｜现价位于 Flip 下方 1.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 174（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 230.0C — Vol 3,360 | 最新价 $0.08 | OI 5408→7781 (ΔOI +2373张) | ΔOI/Volume 70.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2373张（+43.9% vs前日OI），连续性待观察（方向未知）
10-30 225.0C — Vol 2,310 | 最新价 $0.64 | OI 1998→3942 (ΔOI +1944张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1944张（+97.3% vs前日OI），连续性待观察（方向未知）
10-23 180.0C — Vol 9,847 | 最新价 $3.40 | OI 4332→5461 (ΔOI +1129张) | ΔOI/Volume 11.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1129张（+26.1% vs前日OI），连续性待观察（方向未知）
10-23 235.0C — Vol 2,869 | 最新价 $0.09 | OI 1514→2632 (ΔOI +1118张) | ΔOI/Volume 39.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1118张（+73.8% vs前日OI），连续性待观察（方向未知）
10-23 190.0C — Vol 8,470 | 最新价 $1.40 | OI 3689→4786 (ΔOI +1097张) | ΔOI/Volume 12.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1097张（+29.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,661 张（Put 0 / Call 7,661），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +10.1k / P +3.0k ｜ Activity HIGH ｜ 2D
10-30  C +6.4k / P +3.1k ｜ Activity MEDIUM △ ｜ 9D
11-06  C +1.8k / P +0.6k ｜ Activity HIGH ｜ 16D
11-13  C +0.6k / P +0.3k ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 105.4k / P 65.2k，今日变化ΔOI: C +10.1k / P +3.0k，平值价格ATM: C $5.17 / P $6.25 ｜ ATM IV 106.1%，净 delta 敞口 159k shares
Top ΔOI: C 180 +1,129
仓位参考: Max Pain 180 ｜ Call Wall 180（+5.0%，弱）（OI 5.5k） ｜ Put Wall 165（-3.8%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 106.1%｜历史 Rank 56%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 158,875 股

10-30（MEDIUM △）Top ΔOI: 225C +1,944 ｜ 170C +948
10-30（MEDIUM △）仓位参考: Max Pain 208 ｜ Call Wall 175（+2.1%，弱）（OI 1.4k） ｜ Put Wall 165（-3.8%，弱）（OI 2.1k）

📆 11-06 Forward Structure
存量OI: C 31.2k / P 17.1k，今日变化ΔOI: C +1.8k / P +0.6k，平值价格ATM: C $13.00 / P $13.50 ｜ ATM IV 90.6%，净 delta 敞口 7k shares
Top ΔOI: P 165 +229 ｜ C 200 +206
仓位参考: Max Pain 210 ｜ Put Wall 170（-0.9%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 90.6%｜历史 Rank 56%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,342 股

📆 11-13 Forward Structure
存量OI: C 12.3k / P 15.6k，今日变化ΔOI: C +0.6k / P +0.3k，平值价格ATM: C $17.80 / P $15.70 ｜ ATM IV 97.2%，净 delta 敞口 13k shares
Top ΔOI: P 165 +158 ｜ C 200 +147 ｜ C 170 +84
仓位参考: Max Pain 205 ｜ Call Wall 180（+5.0%，弱）（OI 0.4k） ｜ Put Wall 165（-3.8%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 97.2%｜历史 Rank 56%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 13,457 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/NBIS_morning.json