# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $709.30 ｜ QQQ $630.45
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 10C ΔOI +11（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 9.97 → 今开 9.62（-3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 10.09 ｜ 低 9.46

Options: P/C成交量 4.25 | OI比 0.24 | ATM IV 57.8% | Skew -35.3pp | Term 1.59 | ExpMove N/A | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 1.59）｜Put 保护异常便宜（Skew -35.3pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.24）+ 当日成交偏 Put（P/C量 4.25）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 4.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（14D）±18.1% ｜ 12-11（21D）±28.1% ｜ 12-18（28D）±18.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 349,168 | GEX Change vs 上次快照 -245,002 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 142 / LOW 81 / INVALID 16
结构观察区: NO_CROSS
Put Wall 10（弱结构｜现价低于该位 4.1%）
最近结构参考: Put Wall 10（现价低于该位 4.1%）
量化视角： 正 Gamma（35万，无历史分位）｜正 Gamma 减弱（25万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 9.0P — Vol 151 | 最新价 $0.55 | OI 27→170 (ΔOI +143张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增143张（+529.6% vs前日OI），连续性待观察（方向未知）
12-04 12.0C — Vol 42 | 最新价 $0.21 | OI 12→52 (ΔOI +40张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40张（+333.3% vs前日OI），连续性待观察（方向未知）
12-11 12.0C — Vol 30 | 最新价 $0.40 | OI 16→46 (ΔOI +30张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30张（+187.5% vs前日OI），连续性待观察（方向未知）
11-20 11.0C — Vol 54 | 最新价 $0.04 | OI 321→348 (ΔOI +27张) | ΔOI/Volume 50.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增27张（+8.4% vs前日OI），值得跟踪（方向未知）
12-04 10.0P — Vol 25 | 最新价 $0.50 | OI 93→110 (ΔOI +17张) | ΔOI/Volume 68.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增17张（+18.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 257 张（Put 160 / Call 97），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 7.2k / P 1.7k，今日成交量: C 0.2k / P 1.0k，平值价格ATM: C N/A / P $0.07 ｜ ATM IV 57.8%，Max Pain 12
Top ΔOI: P 12 -67 ｜ P 13 -36 ｜ P 16 -30

📆 Forward Expiration Structure

11-27  C -4 / P -7 ｜ Activity LOW ｜ 7D
12-04  C +42 / P +16 ｜ Activity LOW ｜ 14D
12-11  C +31 / P +0 ｜ Activity LOW ｜ 21D
12-18  C -2 / P +0.1k ｜ Activity HIGH ｜ 28D

📆 11-27 Forward Structure
存量OI: C 5.0k / P 0.8k，今日变化ΔOI: C -4 / P -7，ATM IV 69.9%，净 delta 敞口 2k shares
Top ΔOI: C 10 +11
仓位参考: Max Pain 12 ｜ Put Wall 10（+4.3%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 69.9%｜历史 Rank 20%（近端代理）｜IV/RV 0.73×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,552 股

12-04（Activity LOW）仓位参考: Max Pain 12 ｜ Put Wall 9.5（-0.9%）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 11 ｜ Call Wall 10（+4.3%，弱）（OI 34） ｜ Put Wall 9（-6.2%，弱）（OI 8）

📆 12-18 Forward Structure
存量OI: C 1.2k / P 0.7k，今日变化ΔOI: C -2 / P +0.1k，平值价格ATM: C $0.95 / P $0.85 ｜ ATM IV 92.1%，净 delta 敞口 -4k shares
Top ΔOI: P 9 +143
仓位参考: Max Pain 11 ｜ Call Wall 10（+4.3%，弱）（OI 60） ｜ Put Wall 9（-6.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 92.1%｜历史 Rank 20%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 负 4,342 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/NNE_morning.json