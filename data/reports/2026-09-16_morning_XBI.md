# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.92
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 155P ΔOI -8,282（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 145P ΔOI +14,998 占该期限总 OI 43.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 154.03 → 今开 154.37（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 156.04 ｜ 低 154.19

Options: P/C成交量 0.84 | OI比 1.38 | ATM IV 36.8% | Skew 1.1pp | Term 0.83 | ExpMove ±2.3%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±2.3% ｜ 09-25（9D）±4.6% ｜ 10-02（16D）±7.5% ｜ 10-09（23D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -59,205,732 | GEX Change vs 上次快照 6,882,989 | Flip: Primary Flip: 163.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 384 / LOW 123 / INVALID 325
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.18（全链重定价，覆盖 90%）
Put Wall 150（弱结构｜现价高于该位 3.4%） | Call Wall 170（弱结构｜现价低于该位 8.8%）
最近结构参考: Put Wall 150（现价高于该位 3.4%）
量化视角： 负 Gamma（5921万，无历史分位）｜负 Gamma 缓解（+688万）｜现价位于 Flip 下方 4.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 156（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 150.0P — Vol 15,143 | 最新价 $3.85 | OI 1096→16101 (ΔOI +15005张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15005张（+1369.1% vs前日OI），连续性待观察（方向未知）
09-25 145.0P — Vol 15,659 | 最新价 $0.70 | OI 175→15173 (ΔOI +14998张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14998张（+8570.3% vs前日OI），连续性待观察（方向未知）
09-18 151.0P — Vol 5,524 | 最新价 $0.90 | OI 427→5931 (ΔOI +5504张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5504张（+1289.0% vs前日OI），连续性待观察（方向未知）
09-18 146.0P — Vol 3,017 | 最新价 $0.15 | OI 1737→4276 (ΔOI +2539张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2539张（+146.2% vs前日OI），连续性待观察（方向未知）
09-25 170.0C — Vol 3,037 | 最新价 $0.12 | OI 3073→4899 (ΔOI +1826张) | ΔOI/Volume 60.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1826张（+59.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 39,872 张（Put 38,046 / Call 1,826），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.0k / P -21.9k ｜ Activity MEDIUM △ ｜ 2D
09-25  C +3.4k / P +15.8k ｜ Activity HIGH ｜ 9D
10-02  C +18 / P +25 ｜ Activity MEDIUM △ ｜ 16D
10-09  C +10 / P +0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 09-18 Forward Structure
存量OI: C 76.7k / P 106.2k，今日变化ΔOI: C +2.0k / P -21.9k，平值价格ATM: C $1.80 / P $1.74 ｜ ATM IV 36.8%，净 delta 敞口 1.1M shares
Top ΔOI: P 155 -8,282 ｜ P 150 -8,263 ｜ P 140 -6,000
仓位参考: Max Pain 156 ｜ Call Wall 155（-0.0%，弱）（OI 10.8k） ｜ Put Wall 155（-0.0%，弱）（OI 12.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.8%｜历史 Rank 71%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,108,571 股

📆 09-25 Forward Structure
存量OI: C 9.5k / P 24.8k，今日变化ΔOI: C +3.4k / P +15.8k，平值价格ATM: C $3.01 / P $4.10 ｜ ATM IV 32.0%，净 delta 敞口 -145k shares
Top ΔOI: P 145 +14,998 ｜ C 170 +1,826 ｜ C 160 +1,390
仓位参考: Max Pain 159 ｜ Call Wall 170（+9.6%）（OI 4.9k） ｜ Put Wall 145（-6.5%）（OI 15.2k）
量化解读： 存量 Put 重｜ATM IV 32.0%｜历史 Rank 71%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 145,059 股

10-02（MEDIUM △）Top ΔOI: 152P +30 ｜ 150P -4
10-02（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 165（+6.4%）（OI 0.8k） ｜ Put Wall 157（+1.3%，弱）（OI 0.2k）

10-09（MEDIUM △）Top ΔOI: 150P +106 ｜ 140P +102
10-09（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+3.2%，弱）（OI 18） ｜ Put Wall 140（-9.7%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/XBI_morning.json