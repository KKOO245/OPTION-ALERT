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
🟡 **近现价集中开仓**: 09-25 156P ΔOI +3,016（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 158.23 → 今开 159.11（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 161.43 ｜ 低 158.42

Options: P/C成交量 2.27 | OI比 3.66 | ATM IV 32.1% | Skew 1.8pp | Term 0.95 | ExpMove ±3.8%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 1.8pp）｜当日成交偏 Put（P/C量 2.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.66×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±3.8% ｜ 10-02（10D）±4.6% ｜ 10-09（17D）±8.2% ｜ 10-16（24D）±6.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,442,573 | GEX Change vs 上次快照 12,073,742 | Flip: Primary Flip: 163.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 370 / LOW 66 / INVALID 332
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.96（全链重定价，覆盖 94%）
最近结构参考: Flip 164（现价低于该位 1.7%）
量化视角： 负 Gamma（1044万，无历史分位）｜负 Gamma 缓解（+1207万）｜现价位于 Flip 下方 1.73%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 156.0P — Vol 3,032 | 最新价 $1.36 | OI 200→3216 (ΔOI +3016张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3016张（+1508.0% vs前日OI），连续性待观察（方向未知）
09-25 151.0P — Vol 3,019 | 最新价 $0.29 | OI 692→3118 (ΔOI +2426张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2426张（+350.6% vs前日OI），连续性待观察（方向未知）
10-16 170.0C — Vol 2,143 | 最新价 $1.29 | OI 3064→5021 (ΔOI +1957张) | ΔOI/Volume 91.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1957张（+63.9% vs前日OI），连续性待观察（方向未知）
09-25 165.0C — Vol 1,583 | 最新价 $0.33 | OI 142→1650 (ΔOI +1508张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1508张（+1062.0% vs前日OI），连续性待观察（方向未知）
10-16 150.0P — Vol 1,098 | 最新价 $2.06 | OI 17551→18063 (ΔOI +512张) | ΔOI/Volume 46.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增512张（+2.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,419 张（Put 5,954 / Call 3,465），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +2.4k / P +6.1k ｜ Activity HIGH ｜ 3D
10-02  C +0.4k / P +36 ｜ Activity HIGH ｜ 10D
10-09  C +21 / P +35 ｜ Activity MEDIUM △ ｜ 17D
10-16  C +2.7k / P +0.8k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 11.8k / P 43.4k，今日变化ΔOI: C +2.4k / P +6.1k，平值价格ATM: C $1.00 / P $5.10 ｜ ATM IV 32.1%，净 delta 敞口 -94k shares
Top ΔOI: P 156 +3,016 ｜ P 151 +2,426 ｜ C 165 +1,508
仓位参考: Max Pain 157 ｜ Call Wall 160（-0.7%，弱）（OI 2.7k） ｜ Put Wall 156（-3.2%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 32.1%｜历史 Rank 44%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 93,699 股

📆 10-02 Forward Structure
存量OI: C 2.1k / P 1.7k，今日变化ΔOI: C +0.4k / P +36，平值价格ATM: C $2.79 / P $4.62 ｜ ATM IV 28.7%，净 delta 敞口 9k shares
Top ΔOI: C 165 +338 ｜ C 171 +27
仓位参考: Max Pain 160 ｜ Call Wall 165（+2.4%）（OI 1.0k） ｜ Put Wall 157（-2.6%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 28.7%｜历史 Rank 44%（近端代理）｜IV/RV 1.35×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 8,993 股

10-09（MEDIUM △）Top ΔOI: 150P +26 ｜ 157P +12
10-09（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（-0.7%，弱）（OI 18）

📆 10-16 Forward Structure
存量OI: C 35.9k / P 64.9k，今日变化ΔOI: C +2.7k / P +0.8k，平值价格ATM: C $3.90 / P $6.35 ｜ ATM IV 31.4%，净 delta 敞口 46k shares
Top ΔOI: C 170 +1,957 ｜ P 150 +512 ｜ C 168 +243
仓位参考: Max Pain 165 ｜ Call Wall 170（+5.5%，弱）（OI 5.0k） ｜ Put Wall 153（-5.0%，弱）（OI 6.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.4%｜历史 Rank 44%（近端代理）｜IV/RV 1.47×（近似）｜净 delta 敞口 正 46,463 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/XBI_morning.json