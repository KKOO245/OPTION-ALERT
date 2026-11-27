# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $730.70 ｜ QQQ $650.99
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 152C ΔOI +23,677（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 149.30 → 今开 151.94（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 151.98 ｜ 低 145.39

Options: P/C成交量 0.89 | OI比 0.68 | ATM IV 132.4% | Skew 0.4pp | Term 0.54 | ExpMove ±5.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±5.5% ｜ 12-02（5D）±8.5% ｜ 12-04（7D）±10.4% ｜ 12-07（10D）±11.2%
   ⇒ IV–VIX Spread: +104.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 99,180,481 | GEX Change vs 上次快照 52,182,541 | Flip: Primary Flip: 137.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1391 / LOW 215 / INVALID 966
结构观察区: Primary Flip 137.93（全链重定价，覆盖 97%）
最近结构参考: Flip 138（现价高于该位 5.8%）
量化视角： 正 Gamma（9918万，无历史分位）｜正 Gamma 增强（+5218万）｜现价位于 Flip 上方 5.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 152.5C — Vol 31,962 | 最新价 $7.00 | OI 2393→26070 (ΔOI +23677张) | ΔOI/Volume 74.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23677张（+989.4% vs前日OI），连续性待观察（方向未知）
12-04 160.0C — Vol 45,793 | 最新价 $4.05 | OI 16121→39283 (ΔOI +23162张) | ΔOI/Volume 50.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23162张（+143.7% vs前日OI），连续性待观察（方向未知）
12-04 75.0P — Vol 25,433 | 最新价 $0.07 | OI 6973→28823 (ΔOI +21850张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21850张（+313.4% vs前日OI），连续性待观察（方向未知）
12-04 155.0C — Vol 22,249 | 最新价 $5.70 | OI 6382→22074 (ΔOI +15692张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15692张（+245.9% vs前日OI），连续性待观察（方向未知）
12-04 148.0C — Vol 17,459 | 最新价 $9.00 | OI 1071→16025 (ΔOI +14954张) | ΔOI/Volume 85.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14954张（+1396.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 99,335 张（Put 21,850 / Call 77,485），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 659.6k / P 450.5k，今日成交量: C 328.2k / P 291.3k，平值价格ATM: C $1.35 / P $1.74 ｜ ATM IV 132.4%，预期波动 ±2.1%，Max Pain 150
Top ΔOI: C 210 +11,522 ｜ C 167 -8,121 ｜ C 155 +7,857

📆 Forward Expiration Structure

11-30  C +33.5k / P +39.6k ｜ Activity HIGH ｜ 3D
12-02  C +13.4k / P +9.7k ｜ Activity HIGH ｜ 5D
12-04  C +111.0k / P +70.9k ｜ Activity HIGH ｜ 7D
12-07  C +5.3k / P +2.7k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 139.9k / P 109.1k，今日变化ΔOI: C +33.5k / P +39.6k，平值价格ATM: C $3.86 / P $4.14 ｜ ATM IV 71.7%，净 delta 敞口 -155k shares
Top ΔOI: C 160 +5,590 ｜ P 128 +5,018
仓位参考: Max Pain 150 ｜ Call Wall 160（+9.6%，弱）（OI 10.7k） ｜ Put Wall 135（-7.5%，弱）（OI 7.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 71.7%｜历史 Rank 98%（近端代理）｜IV/RV 0.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 154,608 股

📆 12-02 Forward Structure
存量OI: C 80.7k / P 33.4k，今日变化ΔOI: C +13.4k / P +9.7k，平值价格ATM: C $5.95 / P $6.50 ｜ ATM IV 88.4%，净 delta 敞口 127k shares
Top ΔOI: C 155 +8,751 ｜ C 167 -7,693 ｜ C 160 +2,482
仓位参考: Max Pain 152 ｜ Call Wall 155（+6.2%，弱）（OI 10.4k） ｜ Put Wall 145（-0.7%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 88.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 127,215 股

📆 12-04 Forward Structure
存量OI: C 385.0k / P 250.7k，今日变化ΔOI: C +111.0k / P +70.9k，平值价格ATM: C $7.40 / P $7.75 ｜ ATM IV 92.5%，净 delta 敞口 3.4M shares
Top ΔOI: C 152 +23,677 ｜ C 160 +23,162 ｜ P 75 +21,850
仓位参考: Max Pain 150 ｜ Call Wall 160（+9.6%）（OI 39.3k） ｜ Put Wall 160（+9.6%，弱）（OI 10.5k）
量化解读： 存量 Call 重｜ATM IV 92.5%｜历史 Rank 98%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,408,918 股

📆 12-07 Forward Structure
存量OI: C 22.3k / P 8.8k，今日变化ΔOI: C +5.3k / P +2.7k，平值价格ATM: C $7.94 / P $8.35 ｜ ATM IV 83.0%，净 delta 敞口 154k shares
Top ΔOI: C 160 +867 ｜ C 155 +699
仓位参考: Max Pain 150 ｜ Call Wall 160（+9.6%，弱）（OI 2.3k） ｜ Put Wall 150（+2.8%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 83.0%｜历史 Rank 98%（近端代理）｜IV/RV 0.66×（近似）｜净 delta 敞口 正 154,283 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/NVDA_morning.json