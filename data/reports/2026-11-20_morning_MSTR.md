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
🟡 **近现价集中开仓**: 11-27 80P ΔOI +1,992（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 86.13 → 今开 86.45（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 87.95 ｜ 低 82.27

Options: P/C成交量 3.39 | OI比 0.45 | ATM IV 63.3% | Skew -59.6pp | Term 1.51 | ExpMove ±10.8%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常偏陡（Term 1.51）｜Put 保护异常便宜（Skew -59.6pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.45）+ 当日成交偏 Put（P/C量 3.39）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 3.39×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±10.8% ｜ 12-04（14D）±15.6% ｜ 12-11（21D）±19.3% ｜ 12-18（28D）±21.5%
   ⇒ IV–VIX Spread: +35.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -27,085,338 | GEX Change vs 上次快照 18,631,530 | Flip: Primary Flip: 90.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 393 / LOW 277 / INVALID 158
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 90.88（全链重定价，覆盖 100%）
Put Wall 90（弱结构｜现价低于该位 7.9%）
最近结构参考: Put Wall 90（现价低于该位 7.9%）
量化视角： 负 Gamma（2709万，无历史分位）｜负 Gamma 缓解（+1863万）｜现价位于 Flip 下方 8.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 97（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 91（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 95.0C — Vol 9,675 | 最新价 $0.19 | OI 1546→5483 (ΔOI +3937张) | ΔOI/Volume 40.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3937张（+254.7% vs前日OI），连续性待观察（方向未知）
12-18 55.0P — Vol 4,678 | 最新价 $1.18 | OI 2738→5738 (ΔOI +3000张) | ΔOI/Volume 64.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3000张（+109.6% vs前日OI），连续性待观察（方向未知）
12-18 60.0P — Vol 4,240 | 最新价 $1.67 | OI 6299→8394 (ΔOI +2095张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2095张（+33.3% vs前日OI），连续性待观察（方向未知）
11-27 80.0P — Vol 4,073 | 最新价 $2.49 | OI 6247→8239 (ΔOI +1992张) | ΔOI/Volume 48.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1992张（+31.9% vs前日OI），连续性待观察（方向未知）
11-20 91.0C — Vol 6,660 | 最新价 $0.67 | OI 507→2390 (ΔOI +1883张) | ΔOI/Volume 28.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1883张（+371.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,907 张（Put 7,087 / Call 5,820），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 290.3k / P 130.0k，今日成交量: C 9.7k / P 32.9k，平值价格ATM: C $1.31 / P $1.73 ｜ ATM IV 63.3%，预期波动 ±3.7%，Max Pain 97
Top ΔOI: P 110 -7,368 ｜ P 100 -6,659 ｜ C 95 +3,937

📆 Forward Expiration Structure

11-27  C +4.6k / P +1.8k ｜ Activity HIGH ｜ 7D
12-04  C +1.5k / P -2.4k ｜ Activity MEDIUM △ ｜ 14D
12-11  C +1.1k / P -32 ｜ Activity MEDIUM △ ｜ 21D
12-18  C +3.1k / P -1.4k ｜ Activity HIGH ｜ 28D

📆 11-27 Forward Structure
存量OI: C 55.4k / P 82.1k，今日变化ΔOI: C +4.6k / P +1.8k，平值价格ATM: C $4.50 / P $4.45 ｜ ATM IV 88.1%，净 delta 敞口 327k shares
Top ΔOI: P 80 +1,992 ｜ C 100 +1,606 ｜ C 90 +1,292
仓位参考: Max Pain 100 ｜ Call Wall 90（+8.6%，弱）（OI 1.5k） ｜ Put Wall 90（+8.6%）（OI 14.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.1%｜历史 Rank 16%（近端代理）｜IV/RV 1.32×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 326,541 股

12-04（MEDIUM △）Top ΔOI: 135P -2,025 ｜ 140P -1,978
12-04（MEDIUM △）仓位参考: Max Pain 115 ｜ Put Wall 85（+2.6%，弱）（OI 6.8k）

12-11（MEDIUM △）Top ΔOI: 60P +984 ｜ 145P -825
12-11（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 90（+8.6%，弱）（OI 0.2k） ｜ Put Wall 80（-3.5%，弱）（OI 3.2k）

📆 12-18 Forward Structure
存量OI: C 231.3k / P 182.1k，今日变化ΔOI: C +3.1k / P -1.4k，平值价格ATM: C $9.05 / P $8.80 ｜ ATM IV 95.5%，净 delta 敞口 638k shares
Top ΔOI: P 55 +3,000 ｜ P 155 -2,663 ｜ P 160 -2,324
仓位参考: Max Pain 135 ｜ Put Wall 80（-3.5%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜ATM IV 95.5%｜历史 Rank 16%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 637,511 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/MSTR_morning.json