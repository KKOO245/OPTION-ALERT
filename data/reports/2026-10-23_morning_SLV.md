# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $760.75 ｜ QQQ $704.40
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-26 50C ΔOI +960（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 50C ΔOI +2,252 占该期限总 OI 13.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 49.34 → 今开 48.60（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 48.87 ｜ 低 47.87

Options: P/C成交量 0.96 | OI比 0.44 | ATM IV 44.3% | Skew 1.1pp | Term 0.85 | ExpMove ±2.2%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.96×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.2% ｜ 10-28（5D）±3.7% ｜ 10-30（7D）±4.5% ｜ 11-02（10D）±5.0%
   ⇒ IV–VIX Spread: +24.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,644,777 | GEX Change vs 上次快照 3,479,482 | Flip: Primary Flip: 48.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 714 / LOW 135 / INVALID 351
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.95（全链重定价，覆盖 93%）
Put Wall 50（弱结构｜现价低于该位 2.5%）
最近结构参考: Flip 49（现价低于该位 0.4%）
量化视角： 负 Gamma（564万，无历史分位）｜负 Gamma 缓解（+348万）｜现价位于 Flip 下方 0.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 48.0P — Vol 15,851 | 最新价 $1.50 | OI 4141→16222 (ΔOI +12081张) | ΔOI/Volume 76.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12081张（+291.7% vs前日OI），连续性待观察（方向未知）
11-20 50.0P — Vol 14,092 | 最新价 $2.43 | OI 17278→25126 (ΔOI +7848张) | ΔOI/Volume 55.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7848张（+45.4% vs前日OI），连续性待观察（方向未知）
11-20 52.0C — Vol 5,537 | 最新价 $1.18 | OI 2094→7114 (ΔOI +5020张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5020张（+239.7% vs前日OI），连续性待观察（方向未知）
11-20 55.0C — Vol 7,368 | 最新价 $0.55 | OI 21747→25912 (ΔOI +4165张) | ΔOI/Volume 56.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4165张（+19.1% vs前日OI），连续性待观察（方向未知）
10-23 50.0C — Vol 8,309 | 最新价 $0.26 | OI 487→3393 (ΔOI +2906张) | ΔOI/Volume 35.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2906张（+596.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,020 张（Put 19,929 / Call 12,091），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 86.7k / P 38.5k，今日成交量: C 5.5k / P 5.3k，平值价格ATM: C $0.15 / P $0.33 ｜ ATM IV 44.3%，预期波动 ±1.0%，Max Pain 50
Top ΔOI: C 50 +2,906 ｜ P 55 -2,638 ｜ C 50 +2,365

📆 Forward Expiration Structure

10-26  C +4.6k / P +5.2k ｜ Activity HIGH ｜ 3D
10-28  C +3.5k / P +2.8k ｜ Activity HIGH ｜ 5D
10-30  C +4.4k / P +32 ｜ Activity MEDIUM △ ｜ 7D
11-02  C +0.7k / P +0.3k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 12.0k / P 12.1k，今日变化ΔOI: C +4.6k / P +5.2k，平值价格ATM: C $0.43 / P $0.63 ｜ ATM IV 28.6%，净 delta 敞口 -25k shares
Top ΔOI: P 45 +1,002 ｜ C 50 +960
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+3.6%）（OI 2.3k） ｜ Put Wall 48.5（-0.5%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 28.6%｜历史 Rank 75%（近端代理）｜IV/RV 0.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 25,199 股

📆 10-28 Forward Structure
存量OI: C 8.9k / P 8.2k，今日变化ΔOI: C +3.5k / P +2.8k，平值价格ATM: C $0.79 / P $1.02 ｜ ATM IV 37.7%，净 delta 敞口 24k shares
Top ΔOI: C 50 +2,252 ｜ P 44 +635 ｜ P 48 +441
仓位参考: Max Pain 50 ｜ Call Wall 50（+2.5%）（OI 2.4k） ｜ Put Wall 48（-1.6%）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 37.7%｜历史 Rank 75%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,165 股

10-30（MEDIUM △）Top ΔOI: 50C +1,144
10-30（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 53.5（+9.7%，弱）（OI 1.6k） ｜ Put Wall 50（+2.5%，弱）（OI 3.5k）

📆 11-02 Forward Structure
存量OI: C 1.4k / P 0.9k，今日变化ΔOI: C +0.7k / P +0.3k，平值价格ATM: C $1.10 / P $1.32 ｜ ATM IV 36.4%，净 delta 敞口 8k shares
Top ΔOI: C 50 +330 ｜ C 50 +147
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+3.6%）（OI 0.3k） ｜ Put Wall 46（-5.7%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 36.4%｜历史 Rank 75%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 7,547 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SLV_morning.json