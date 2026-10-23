# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.05 ｜ QQQ $706.86
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 12P ΔOI +159（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.53 → 今开 12.40（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 12.45 ｜ 低 11.95

Options: P/C成交量 8.53 | OI比 0.14 | ATM IV 85.2% | Skew 24.9pp | Term 0.90 | ExpMove ±11.4%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价显著（Skew 24.9pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.14）+ 当日成交偏 Put（P/C量 8.53）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 8.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.14×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±11.4% ｜ 11-06（14D）±13.9% ｜ 11-13（21D）±14.2% ｜ 11-20（28D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 759,404 | GEX Change vs 上次快照 -137,372 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 155 / LOW 95 / INVALID 156
结构观察区: NO_CROSS
量化视角： 正 Gamma（76万，无历史分位）｜正 Gamma 减弱（14万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 12.0P — Vol 164 | 最新价 $0.35 | OI 114→273 (ΔOI +159张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增159张（+139.5% vs前日OI），连续性待观察（方向未知）
10-23 13.0C — Vol 131 | 最新价 $0.05 | OI 158→259 (ΔOI +101张) | ΔOI/Volume 77.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增101张（+63.9% vs前日OI），连续性待观察（方向未知）
11-06 14.0P — Vol 37 | 最新价 $1.76 | OI 22→56 (ΔOI +34张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34张（+154.6% vs前日OI），连续性待观察（方向未知）
10-30 13.0C — Vol 67 | 最新价 $0.34 | OI 74→101 (ΔOI +27张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27张（+36.5% vs前日OI），连续性待观察（方向未知）
10-23 12.5C — Vol 30 | 最新价 $0.18 | OI 42→60 (ΔOI +18张) | ΔOI/Volume 60.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18张（+42.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 339 张（Put 193 / Call 146），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 7.2k / P 1.0k，今日成交量: C 0.2k / P 1.6k，平值价格ATM: C $0.20 / P $0.25 ｜ ATM IV 85.2%，预期波动 ±3.6%，Max Pain 14
Top ΔOI: P 15 -164 ｜ C 13 +101 ｜ P 16 -63

📆 Forward Expiration Structure

10-30  C +31 / P +0.1k ｜ Activity HIGH ｜ 7D
11-06  C +0 / P +45 ｜ Activity MEDIUM △ ｜ 14D
11-13  C +4 / P +5 ｜ Activity MEDIUM △ ｜ 21D
11-20  C +24 / P +14 ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 7.1k / P 1.5k，今日变化ΔOI: C +31 / P +0.1k，平值价格ATM: C $0.91 / P $0.50 ｜ ATM IV 76.1%，净 delta 敞口 850 shares
Top ΔOI: P 12 +159 ｜ C 13 +27
仓位参考: Max Pain 14 ｜ Put Wall 12（-2.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.1%｜历史 Rank 18%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 正 850 股

11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（+5.4%，弱）（OI 78）

11-13（MEDIUM △）Top ΔOI: 12C +7 ｜ 13P +4
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+9.5%，弱）（OI 51） ｜ Put Wall 13（+5.4%，弱）（OI 70）

11-20（MEDIUM △）Top ΔOI: 13C +15
11-20（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 12（-2.7%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/NNE_morning.json