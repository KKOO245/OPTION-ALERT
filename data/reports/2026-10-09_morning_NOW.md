# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $776.00 ｜ QQQ $749.67
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 42.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 138C ΔOI +567（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 139.75 → 今开 141.26（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 142.47 ｜ 低 139.43

Options: P/C成交量 0.84 | OI比 0.70 | ATM IV 60.8% | Skew 1.2pp | Term 0.99 | ExpMove ±5.2%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±5.2% ｜ 10-23（14D）±7.3% ｜ 10-30（21D）±12.0% ｜ 11-06（28D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,303,514 | GEX Change vs 上次快照 746,864 | Flip: Primary Flip: 134.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 516 / LOW 66 / INVALID 116
结构观察区: Primary Flip 134.26（全链重定价，覆盖 94%）
Call Wall 150（现价低于该位 6.9%）
最近结构参考: Flip 134（现价高于该位 4.0%）
量化视角： 正 Gamma（2430万，无历史分位）｜正 Gamma 增强（+75万）｜现价位于 Flip 上方 4.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 150.0C — Vol 2,565 | 最新价 $1.03 | OI 14910→15862 (ΔOI +952张) | ΔOI/Volume 37.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增952张（+6.4% vs前日OI），连续性待观察（方向未知）
10-09 141.0C — Vol 2,415 | 最新价 $1.02 | OI 580→1290 (ΔOI +710张) | ΔOI/Volume 29.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增710张（+122.4% vs前日OI），连续性待观察（方向未知）
10-09 142.0C — Vol 3,565 | 最新价 $0.70 | OI 865→1450 (ΔOI +585张) | ΔOI/Volume 16.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增585张（+67.6% vs前日OI），连续性待观察（方向未知）
10-16 138.0C — Vol 995 | 最新价 $5.08 | OI 565→1132 (ΔOI +567张) | ΔOI/Volume 57.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增567张（+100.3% vs前日OI），连续性待观察（方向未知）
10-09 137.0P — Vol 1,454 | 最新价 $0.52 | OI 236→769 (ΔOI +533张) | ΔOI/Volume 36.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增533张（+225.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,347 张（Put 533 / Call 2,814），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 29.3k / P 20.5k，今日成交量: C 4.4k / P 3.7k，平值价格ATM: C $0.77 / P $1.07 ｜ ATM IV 60.8%，预期波动 ±1.3%，Max Pain 136
Top ΔOI: C 141 +710 ｜ C 144 -618 ｜ C 142 +585

📆 Forward Expiration Structure

10-16  C +2.3k / P +0.9k ｜ Activity HIGH ｜ 7D
10-23  C +1.3k / P +1.2k ｜ Activity MEDIUM △ ｜ 14D
10-30  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
11-06  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 85.3k / P 65.2k，今日变化ΔOI: C +2.3k / P +0.9k，平值价格ATM: C $3.55 / P $3.75 ｜ ATM IV 46.3%，净 delta 敞口 62k shares
Top ΔOI: C 150 +952 ｜ C 138 +567
仓位参考: Max Pain 130 ｜ Call Wall 150（+7.4%）（OI 15.9k） ｜ Put Wall 130（-6.9%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 46.3%｜历史 Rank 75%（近端代理）｜IV/RV 1.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 61,537 股

10-23（MEDIUM △）Top ΔOI: 145C +485 ｜ 142P +457
10-23（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 140（+0.3%，弱）（OI 1.3k）

10-30（MEDIUM △）Top ΔOI: 134P +83
10-30（MEDIUM △）仓位参考: Max Pain 134 ｜ Call Wall 150（+7.4%，弱）（OI 0.8k） ｜ Put Wall 130（-6.9%，弱）（OI 0.6k）

11-06（MEDIUM △）Top ΔOI: 139P +103 ｜ 142C +39
11-06（MEDIUM △）仓位参考: Max Pain 137 ｜ Call Wall 140（+0.3%，弱）（OI 0.3k） ｜ Put Wall 130（-6.9%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/NOW_morning.json