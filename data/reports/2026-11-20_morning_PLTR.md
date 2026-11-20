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
🟡 **近现价集中开仓**: 12-11 150P ΔOI +679（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 153.68 → 今开 149.70（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 152.51 ｜ 低 147.55

Options: P/C成交量 1.24 | OI比 0.75 | ATM IV 78.4% | Skew -38.0pp | Term 0.76 | ExpMove ±7.5%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -38.0pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.75）+ 当日成交偏 Put（P/C量 1.24）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±7.5% ｜ 12-04（14D）±10.3% ｜ 12-11（21D）±11.9% ｜ 12-18（28D）±13.1%
   ⇒ IV–VIX Spread: +50.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -39,941,806 | GEX Change vs 上次快照 -14,546,727 | Flip: Primary Flip: 152.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 421 / LOW 203 / INVALID 134
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.66（全链重定价，覆盖 100%）
Put Wall 140（弱结构｜现价高于该位 6.6%）
最近结构参考: Flip 153（现价低于该位 2.3%）
量化视角： 负 Gamma（3994万，无历史分位）｜负 Gamma 加深（1455万）｜现价位于 Flip 下方 2.28%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 165.0C — Vol 6 | 最新价 $1.52 | OI 1878→5965 (ΔOI +4087张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4087张（+217.6% vs前日OI），连续性待观察（方向未知）
11-27 160.0C — Vol 4 | 最新价 $2.90 | OI 871→3547 (ΔOI +2676张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2676张（+307.2% vs前日OI），连续性待观察（方向未知）
11-20 170.0C — Vol 25 | 最新价 $0.07 | OI 10997→13119 (ΔOI +2122张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2122张（+19.3% vs前日OI），值得跟踪（方向未知）
11-20 157.5C — Vol 6 | 最新价 $1.33 | OI 1987→3918 (ΔOI +1931张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1931张（+97.2% vs前日OI），连续性待观察（方向未知）
11-27 177.5C — Vol 2,903 | 最新价 $0.26 | OI 453→2214 (ΔOI +1761张) | ΔOI/Volume 60.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1761张（+388.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,577 张（Put 0 / Call 12,577），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 239.4k / P 180.6k，今日成交量: C 20.3k / P 25.3k，平值价格ATM: C $3.83 / P $1.04 ｜ ATM IV 78.4%，预期波动 ±3.3%，Max Pain 160
Top ΔOI: P 180 -4,115 ｜ P 170 -3,185 ｜ P 175 -2,367

📆 Forward Expiration Structure

11-27  C +15.2k / P +0.2k ｜ Activity HIGH ｜ 7D
12-04  C +1.1k / P +42 ｜ Activity MEDIUM △ ｜ 14D
12-11  C +0.4k / P +1.5k ｜ Activity MEDIUM △ ｜ 21D
12-18  C -0.5k / P +51 ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 59.0k / P 39.1k，今日变化ΔOI: C +15.2k / P +0.2k，平值价格ATM: C $7.10 / P $4.07 ｜ ATM IV 61.5%，净 delta 敞口 155k shares
Top ΔOI: C 165 +4,087 ｜ C 160 +2,676
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+8.9%，弱）（OI 6.0k） ｜ Put Wall 150（+0.5%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 61.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 155,319 股

12-04（MEDIUM △）Top ΔOI: 200P -697 ｜ 155P +288
12-04（MEDIUM △）仓位参考: Max Pain 165 ｜ Call Wall 160（+7.3%，弱）（OI 0.9k） ｜ Put Wall 155（+3.9%）（OI 3.1k）

12-11（MEDIUM △）Top ΔOI: 150P +679 ｜ 135P +381
12-11（MEDIUM △）仓位参考: Max Pain 170 ｜ Put Wall 150（+0.5%，弱）（OI 1.9k）

12-18（MEDIUM △）Top ΔOI: 210P -1,302 ｜ 125P +638
12-18（MEDIUM △）仓位参考: Max Pain 140 ｜ Put Wall 140（-6.2%，弱）（OI 22.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/PLTR_morning.json