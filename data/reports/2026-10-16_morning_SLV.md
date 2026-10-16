# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.51 ｜ QQQ $721.47
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 53C ΔOI +979（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 48P ΔOI +2,573 占该期限总 OI 12.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 51.92 → 今开 51.85（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 52.22 ｜ 低 51.73

Options: P/C成交量 0.32 | OI比 0.32 | ATM IV 38.3% | Skew -0.7pp | Term 0.88 | ExpMove ±1.8%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±1.8% ｜ 10-21（5D）±2.9% ｜ 10-23（7D）±3.2% ｜ 10-26（10D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 91,054,676 | GEX Change vs 上次快照 58,239,260 | Flip: Primary Flip: 49.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 737 / LOW 179 / INVALID 332
结构观察区: Primary Flip 49.74（全链重定价，覆盖 90%）
Put Wall 50（弱结构｜现价高于该位 4.2%）
最近结构参考: Put Wall 50（现价高于该位 4.2%）
量化视角： 正 Gamma（9105万，无历史分位）｜正 Gamma 增强（+5824万）｜现价位于 Flip 上方 4.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 52（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 55.0C — Vol 7,447 | 最新价 $1.20 | OI 14901→19624 (ΔOI +4723张) | ΔOI/Volume 63.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4723张（+31.7% vs前日OI），连续性待观察（方向未知）
10-16 52.0C — Vol 12,261 | 最新价 $0.44 | OI 4793→8736 (ΔOI +3943张) | ΔOI/Volume 32.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3943张（+82.3% vs前日OI），连续性待观察（方向未知）
10-23 51.5P — Vol 3,821 | 最新价 $0.79 | OI 627→3623 (ΔOI +2996张) | ΔOI/Volume 78.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2996张（+477.8% vs前日OI），连续性待观察（方向未知）
10-23 52.0C — Vol 4,616 | 最新价 $0.97 | OI 1265→3980 (ΔOI +2715张) | ΔOI/Volume 58.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2715张（+214.6% vs前日OI），连续性待观察（方向未知）
10-21 48.0P — Vol 2,847 | 最新价 $0.09 | OI 251→2824 (ΔOI +2573张) | ΔOI/Volume 90.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2573张（+1025.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,950 张（Put 5,569 / Call 11,381），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 502.1k / P 161.8k，今日成交量: C 13.3k / P 4.2k，平值价格ATM: C $0.21 / P $0.22 ｜ ATM IV 38.3%，预期波动 ±0.8%，Max Pain 52
Top ΔOI: P 57 -7,270 ｜ P 56 -5,598 ｜ P 60 -5,429

📆 Forward Expiration Structure

10-19  C +2.6k / P +3.3k ｜ Activity HIGH ｜ 3D
10-21  C +1.6k / P +3.3k ｜ Activity HIGH ｜ 5D
10-23  C +4.5k / P +7.7k ｜ Activity MEDIUM △ ｜ 7D
10-26  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 10D

📆 10-19 Forward Structure
存量OI: C 11.6k / P 9.4k，今日变化ΔOI: C +2.6k / P +3.3k，平值价格ATM: C $0.45 / P $0.46 ｜ ATM IV 23.8%，净 delta 敞口 56k shares
Top ΔOI: P 49 +1,521 ｜ C 53 +979 ｜ C 52 +601
仓位参考: Max Pain 52 ｜ Call Wall 53（+1.7%，弱）（OI 1.5k） ｜ Put Wall 49（-6.0%）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 23.8%｜历史 Rank 62%（近端代理）｜IV/RV 0.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 55,529 股

📆 10-21 Forward Structure
存量OI: C 11.6k / P 8.5k，今日变化ΔOI: C +1.6k / P +3.3k，平值价格ATM: C $0.79 / P $0.72 ｜ ATM IV 28.6%，净 delta 敞口 13k shares
Top ΔOI: P 48 +2,573 ｜ C 52 +517 ｜ C 54 +371
仓位参考: Max Pain 51 ｜ Call Wall 51（-2.1%，弱）（OI 0.9k） ｜ Put Wall 48（-7.9%）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 28.6%｜历史 Rank 62%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,019 股

10-23（MEDIUM △）Top ΔOI: 51P +2,996 ｜ 52C +2,715
10-23（MEDIUM △）仓位参考: Max Pain 54 ｜ Call Wall 57（+9.4%，弱）（OI 7.1k） ｜ Put Wall 50（-4.1%，弱）（OI 4.5k）

10-26（MEDIUM △）Top ΔOI: 50P +273 ｜ 55C +131
10-26（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50.5（-3.1%）（OI 1.4k） ｜ Put Wall 49（-6.0%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SLV_morning.json