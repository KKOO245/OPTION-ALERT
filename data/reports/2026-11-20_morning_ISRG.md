# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $692.49 ｜ QQQ $608.45
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
🟡 **近现价集中开仓**: 12-04 420C ΔOI +16（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 407.24 → 今开 406.44（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 410.00 ｜ 低 405.44

Options: P/C成交量 0.73 | OI比 0.90 | ATM IV 52.3% | Skew 1.0pp | Term 0.76 | ExpMove ±3.2%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（7D）±3.2% ｜ 12-18（28D）±8.1%
   ⇒ IV–VIX Spread: +24.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -588,366 | GEX Change vs 上次快照 200,638 | Flip: Primary Flip: 409.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 240 / LOW 208 / INVALID 78
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 409.73（全链重定价，覆盖 88%）
最近结构参考: Flip 410（现价低于该位 0.6%）
量化视角： 负 Gamma（59万，无历史分位）｜负 Gamma 缓解（+20万）｜现价位于 Flip 下方 0.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 400（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 410（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 405.0P — Vol 208 | 最新价 $3.90 | OI 363→552 (ΔOI +189张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增189张（+52.1% vs前日OI），连续性待观察（方向未知）
12-18 435.0C — Vol 142 | 最新价 $6.00 | OI 199→336 (ΔOI +137张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增137张（+68.8% vs前日OI），连续性待观察（方向未知）
11-27 420.0C — Vol 92 | 最新价 $4.08 | OI 6→77 (ΔOI +71张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增71张（+1183.3% vs前日OI），连续性待观察（方向未知）
11-20 410.0P — Vol 61 | 最新价 $5.15 | OI 475→513 (ΔOI +38张) | ΔOI/Volume 62.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增38张（+8.0% vs前日OI），值得跟踪（方向未知）
12-04 445.0C — Vol 23 | 最新价 $1.45 | OI 4→24 (ΔOI +20张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20张（+500.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 455 张（Put 227 / Call 228），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 10.1k / P 9.0k，今日成交量: C 0.6k / P 0.4k，平值价格ATM: C $3.15 / P $3.10 ｜ ATM IV 52.3%，预期波动 ±1.5%，Max Pain 400
Top ΔOI: P 427 -325 ｜ P 405 +189 ｜ P 440 -186

📆 Forward Expiration Structure

11-27  C +0.1k / P +13 ｜ Activity MEDIUM △ ｜ 7D
12-04  C +60 / P -3 ｜ Activity MEDIUM △ ｜ 14D
12-11  C +20 / P +4 ｜ Activity LOW ｜ 21D
12-18  C +0.1k / P -0.1k ｜ Activity LOW ｜ 28D

📆 11-27 Forward Structure
存量OI: C 0.9k / P 0.7k，今日变化ΔOI: C +0.1k / P +13，平值价格ATM: C $9.00 / P $4.00 ｜ ATM IV 39.0%，净 delta 敞口 4k shares
Top ΔOI: C 420 +71 ｜ C 440 +14
仓位参考: Max Pain 420 ｜ Call Wall 420（+3.2%，弱）（OI 77） ｜ Put Wall 395（-3.0%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 39.0%｜历史 Rank 86%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 3,929 股

12-04（MEDIUM △）Top ΔOI: 445C +20 ｜ 420C +16
12-04（MEDIUM △）仓位参考: Max Pain 440 ｜ Call Wall 445（+9.3%，弱）（OI 24） ｜ Put Wall 405（-0.5%，弱）（OI 25）

12-11（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 445（+9.3%，弱）（OI 52） ｜ Put Wall 435（+6.8%）（OI 36）

12-18（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 400（-1.8%，弱）（OI 1.5k） ｜ Put Wall 420（+3.2%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/ISRG_morning.json