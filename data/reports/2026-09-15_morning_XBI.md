# 期权晨报 2026-09-15（快照 10:20 ET）

📊 市场环境

SPY $759.03 ｜ QQQ $706.30
VIX 17.08 ↓0.1%（5D +8.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 150P ΔOI -2,380（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 165C ΔOI +546 占该期限总 OI 19.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 157.60 → 今开 157.08（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 157.53 ｜ 低 153.26

Options: P/C成交量 10.12 | OI比 1.71 | ATM IV 36.6% | Skew -0.2pp | Term 0.84 | ExpMove ±3.5%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 10.12）——观察点，非方向信号
   ⇒ Put/Call Volume: 10.12×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.71×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±3.5% ｜ 09-25（10D）±6.6% ｜ 10-02（17D）±1.9% ｜ 10-09（24D）±11.2%
   ⇒ IV–VIX Spread: +19.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -70,362,666 | GEX Change vs 上次快照 -14,754,617 | Flip: Primary Flip: 164.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 395 / LOW 108 / INVALID 329
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.05（全链重定价，覆盖 92%）
Put Wall 150（弱结构｜现价高于该位 2.8%）
最近结构参考: Put Wall 150（现价高于该位 2.8%）
量化视角： 负 Gamma（7036万，无历史分位）｜负 Gamma 加深（1475万）｜现价位于 Flip 下方 5.97%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 158（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 156.0P — Vol 4,009 | 最新价 $1.40 | OI 3212→4029 (ΔOI +817张) | ΔOI/Volume 20.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增817张（+25.4% vs前日OI），连续性待观察（方向未知）
10-02 165.0C — Vol 605 | 最新价 $1.80 | OI 246→792 (ΔOI +546张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增546张（+221.9% vs前日OI），连续性待观察（方向未知）
10-16 162.0P — Vol 454 | 最新价 $7.45 | OI 210→643 (ΔOI +433张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增433张（+206.2% vs前日OI），连续性待观察（方向未知）
09-18 160.0C — Vol 818 | 最新价 $1.31 | OI 3351→3648 (ΔOI +297张) | ΔOI/Volume 36.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增297张（+8.9% vs前日OI），连续性待观察（方向未知）
09-18 155.0P — Vol 4,697 | 最新价 $1.28 | OI 20209→20445 (ΔOI +236张) | ΔOI/Volume 5.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增236张（+1.2% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,329 张（Put 1,486 / Call 843），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.4k / P -1.0k ｜ Activity MEDIUM △ ｜ 3D
09-25  C +80 / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
10-02  C +0.6k / P +65 ｜ Activity HIGH ｜ 17D
10-09  C +0.2k / P +21 ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 74.7k / P 128.1k，今日变化ΔOI: C +0.4k / P -1.0k，平值价格ATM: C $4.50 / P $0.90 ｜ ATM IV 36.5%，净 delta 敞口 -3k shares
Top ΔOI: P 150 -2,380 ｜ P 156 +817 ｜ C 160 +297
仓位参考: Max Pain 158 ｜ Call Wall 155（+0.5%，弱）（OI 10.8k） ｜ Put Wall 155（+0.5%，弱）（OI 20.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.5%｜历史 Rank 69%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,896 股

09-25（MEDIUM △）Top ΔOI: 155P +92 ｜ 161C +17
09-25（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 167（+8.3%，弱）（OI 1.4k） ｜ Put Wall 150（-2.8%，弱）（OI 3.1k）

📆 10-02 Forward Structure
存量OI: C 1.4k / P 1.3k，今日变化ΔOI: C +0.6k / P +65，平值价格ATM: C $0.00 / P $2.87 ｜ ATM IV 31.4%，净 delta 敞口 13k shares
Top ΔOI: C 165 +546 ｜ P 154 +37 ｜ P 156 +30
仓位参考: Max Pain 160 ｜ Call Wall 165（+7.0%）（OI 0.8k） ｜ Put Wall 157（+1.8%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 31.4%｜历史 Rank 69%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,484 股

📆 10-09 Forward Structure
存量OI: C 0.3k / P 0.6k，今日变化ΔOI: C +0.2k / P +21，平值价格ATM: C $13.92 / P $3.38 ｜ ATM IV 31.2%，净 delta 敞口 2k shares
仓位参考: Max Pain 160 ｜ Call Wall 167（+8.3%，弱）（OI 20） ｜ Put Wall 160（+3.7%，弱）（OI 57）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.2%｜历史 Rank 69%（近端代理）｜净 delta 敞口 正 1,689 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/XBI_morning.json