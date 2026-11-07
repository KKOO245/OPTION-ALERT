# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-09 283P ΔOI -7,534（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-11 255P ΔOI +4,451 占该期限总 OI 12.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 270.98 → 今开 271.98（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 273.65 ｜ 低 270.24

Options: P/C成交量 0.90 | OI比 1.17 | ATM IV 41.3% | Skew 5.9pp | Term 0.53 | ExpMove ±1.6%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价中性（Skew 5.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-09（3D）±1.6% ｜ 11-10（4D）±2.0% ｜ 11-11（5D）±2.3% ｜ 11-12（6D）±2.4%
   ⇒ IV–VIX Spread: +16.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,029,736,154 | GEX Change vs 上次快照 76,842,962 | Flip: Primary Flip: 283.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1302 / LOW 216 / INVALID 1030
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.40（全链重定价，覆盖 94%）
Put Wall 270（弱结构｜现价高于该位 0.7%） | Call Wall 290（弱结构｜现价低于该位 6.2%）
最近结构参考: Put Wall 270（现价高于该位 0.7%）
量化视角： 负 Gamma（10.30亿，无历史分位）｜负 Gamma 缓解（+7684万）｜现价位于 Flip 下方 4.04%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 277（MaxPain，仅结算参考） / 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 283（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 259.0P — Vol 43,901 | 最新价 $2.67 | OI 21547→54508 (ΔOI +32961张) | ΔOI/Volume 75.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32961张（+153.0% vs前日OI），连续性待观察（方向未知）
11-06 281.0C — Vol 26,856 | 最新价 $0.06 | OI 4091→25349 (ΔOI +21258张) | ΔOI/Volume 79.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21258张（+519.6% vs前日OI），连续性待观察（方向未知）
11-06 279.0C — Vol 25,367 | 最新价 $0.13 | OI 1631→21391 (ΔOI +19760张) | ΔOI/Volume 77.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19760张（+1211.5% vs前日OI），连续性待观察（方向未知）
11-20 250.0P — Vol 47,233 | 最新价 $1.56 | OI 56933→70145 (ΔOI +13212张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13212张（+23.2% vs前日OI），连续性待观察（方向未知）
11-20 275.0C — Vol 9,156 | 最新价 $4.05 | OI 4761→9761 (ΔOI +5000张) | ΔOI/Volume 54.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5000张（+105.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 92,191 张（Put 46,173 / Call 46,018），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 232.0k / P 271.1k，今日成交量: C 85.1k / P 76.2k，平值价格ATM: C $1.12 / P $1.31 ｜ ATM IV 41.3%，预期波动 ±0.9%，Max Pain 277
Top ΔOI: C 281 +21,258 ｜ C 279 +19,760 ｜ P 277 -14,752

📆 Forward Expiration Structure

11-09  C +15.3k / P +7.0k ｜ Activity HIGH ｜ 3D
11-10  C +4.8k / P +6.6k ｜ Activity HIGH ｜ 4D
11-11  C +2.2k / P +11.1k ｜ Activity HIGH ｜ 5D
11-12  C +2.3k / P +3.4k ｜ Activity HIGH ｜ 6D

📆 11-09 Forward Structure
存量OI: C 38.7k / P 42.9k，今日变化ΔOI: C +15.3k / P +7.0k，平值价格ATM: C $2.08 / P $2.23 ｜ ATM IV 20.9%，净 delta 敞口 722k shares
Top ΔOI: P 283 -7,534 ｜ C 283 +3,690 ｜ P 268 +2,384
仓位参考: Max Pain 277 ｜ Call Wall 285（+4.8%）（OI 7.4k） ｜ Put Wall 275（+1.1%，弱）（OI 3.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 20.9%｜历史 Rank 97%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 721,921 股

📆 11-10 Forward Structure
存量OI: C 24.2k / P 26.7k，今日变化ΔOI: C +4.8k / P +6.6k，平值价格ATM: C $2.65 / P $2.76 ｜ ATM IV 23.3%，净 delta 敞口 2k shares
Top ΔOI: P 265 +3,229 ｜ C 271 +776 ｜ P 272 +723
仓位参考: Max Pain 280 ｜ Call Wall 290（+6.6%，弱）（OI 4.2k） ｜ Put Wall 265（-2.6%，弱）（OI 4.1k）
量化解读： 存量两侧均衡｜ATM IV 23.3%｜历史 Rank 97%（近端代理）｜净 delta 敞口 正 2,249 股

📆 11-11 Forward Structure
存量OI: C 12.3k / P 23.5k，今日变化ΔOI: C +2.2k / P +11.1k，平值价格ATM: C $3.05 / P $3.10 ｜ ATM IV 23.7%，净 delta 敞口 -152k shares
Top ΔOI: P 255 +4,451 ｜ P 266 +4,387 ｜ P 268 +1,071
仓位参考: Max Pain 280 ｜ Call Wall 286（+5.2%）（OI 3.2k） ｜ Put Wall 266（-2.2%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 23.7%｜历史 Rank 97%（近端代理）｜净 delta 敞口 负 152,292 股

📆 11-12 Forward Structure
存量OI: C 7.7k / P 9.0k，今日变化ΔOI: C +2.3k / P +3.4k，平值价格ATM: C $3.35 / P $3.27 ｜ ATM IV 24.0%，净 delta 敞口 -66k shares
Top ΔOI: P 271 +435 ｜ P 267 +378 ｜ P 269 +300
仓位参考: Max Pain 279 ｜ Call Wall 287（+5.5%，弱）（OI 1.3k） ｜ Put Wall 271（-0.4%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 24.0%｜历史 Rank 97%（近端代理）｜净 delta 敞口 负 65,743 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/IWM_morning.json