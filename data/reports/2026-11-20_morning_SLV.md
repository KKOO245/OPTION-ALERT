# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $693.35 ｜ QQQ $608.45
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-25 38P ΔOI +698（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 39.64 → 今开 37.97（-4.2%） | 较昨收变动（含盘初走势） ｜ 今日高 38.47 ｜ 低 37.50

Options: P/C成交量 2.37 | OI比 0.15 | ATM IV 37.2% | Skew -40.3pp | Term 1.39 | ExpMove ±4.0%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构正常偏陡（Term 1.39）｜Put 保护异常便宜（Skew -40.3pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.15）+ 当日成交偏 Put（P/C量 2.37）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.37×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.15×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±4.0% ｜ 11-25（5D）±5.6% ｜ 11-27（7D）±7.2% ｜ 12-04（14D）±9.4%
   ⇒ IV–VIX Spread: +9.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,402,650 | GEX Change vs 上次快照 49,367,575 | Flip: Primary Flip: 37.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 482 / LOW 228 / INVALID 118
结构观察区: Primary Flip 37.48（全链重定价，覆盖 90%）
Put Wall 40（现价低于该位 6.0%）
最近结构参考: Flip 37（现价高于该位 0.4%）
量化视角： 正 Gamma（340万，无历史分位）｜由负转正（+4937万）｜现价位于 Flip 上方 0.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall） / 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 37（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 41.5C — Vol 20,533 | 最新价 $0.06 | OI 2310→16727 (ΔOI +14417张) | ΔOI/Volume 70.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14417张（+624.1% vs前日OI），连续性待观察（方向未知）
12-18 30.0P — Vol 11,535 | 最新价 $0.14 | OI 726→10723 (ΔOI +9997张) | ΔOI/Volume 86.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9997张（+1377.0% vs前日OI），连续性待观察（方向未知）
11-20 41.0C — Vol 15,782 | 最新价 $0.11 | OI 4075→13108 (ΔOI +9033张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9033张（+221.7% vs前日OI），连续性待观察（方向未知）
12-18 35.0P — Vol 8,755 | 最新价 $0.64 | OI 4406→10243 (ΔOI +5837张) | ΔOI/Volume 66.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5837张（+132.5% vs前日OI），连续性待观察（方向未知）
12-04 44.0C — Vol 6,126 | 最新价 $0.29 | OI 1255→6461 (ΔOI +5206张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5206张（+414.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 44,490 张（Put 15,834 / Call 28,656），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 632.9k / P 94.3k，今日成交量: C 7.8k / P 18.6k，平值价格ATM: C $0.42 / P $0.23 ｜ ATM IV 37.2%，预期波动 ±1.7%，Max Pain 42
Top ΔOI: C 41 +14,417 ｜ P 45 -12,182 ｜ C 41 +9,033

📆 Forward Expiration Structure

11-23  C +6.8k / P +0.2k ｜ Activity HIGH ｜ 3D
11-25  C +5.0k / P +1.2k ｜ Activity HIGH ｜ 5D
11-27  C +5.8k / P -2.4k ｜ Activity MEDIUM △ ｜ 7D
12-04  C +8.6k / P +78 ｜ Activity MEDIUM △ ｜ 14D

📆 11-23 Forward Structure
存量OI: C 26.2k / P 6.6k，今日变化ΔOI: C +6.8k / P +0.2k，平值价格ATM: C $0.85 / P $0.65 ｜ ATM IV 43.6%，净 delta 敞口 83k shares
Top ΔOI: C 41 +1,279
仓位参考: Max Pain 41 ｜ Call Wall 41（+9.0%，弱）（OI 2.6k） ｜ Put Wall 40（+6.3%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 43.6%｜历史 Rank 59%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 82,858 股

📆 11-25 Forward Structure
存量OI: C 20.4k / P 8.3k，今日变化ΔOI: C +5.0k / P +1.2k，平值价格ATM: C $1.14 / P $0.96 ｜ ATM IV 53.7%，净 delta 敞口 -40k shares
Top ΔOI: P 38 +698
仓位参考: Max Pain 42 ｜ Put Wall 39（+3.7%）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 53.7%｜历史 Rank 59%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 40,048 股

11-27（MEDIUM △）Top ΔOI: 40C +1,239
11-27（MEDIUM △）仓位参考: Max Pain 43 ｜ Call Wall 40（+6.3%，弱）（OI 1.9k） ｜ Put Wall 40（+6.3%）（OI 9.4k）

12-04（MEDIUM △）Top ΔOI: 44C +5,206 ｜ 43C +2,024
12-04（MEDIUM △）仓位参考: Max Pain 43 ｜ Put Wall 40（+6.3%）（OI 4.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/SLV_morning.json