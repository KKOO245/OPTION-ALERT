# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $760.51 ｜ QQQ $703.68
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 20.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-26 283C ΔOI +10,088（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 283C ΔOI +10,088 占该期限总 OI 11.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 276.67 → 今开 274.85（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 275.39 ｜ 低 273.44

Options: P/C成交量 1.31 | OI比 1.37 | ATM IV 27.7% | Skew 0.8pp | Term 0.76 | ExpMove ±1.2%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜当日成交偏 Put（P/C量 1.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.31×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±1.2% ｜ 10-27（4D）±1.5% ｜ 10-28（5D）±2.0% ｜ 10-29（6D）±2.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -633,171,656 | GEX Change vs 上次快照 -151,582,726 | Flip: Primary Flip: 280.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1294 / LOW 204 / INVALID 1202
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 280.54（全链重定价，覆盖 96%）
Put Wall 270（弱结构｜现价高于该位 2.0%） | Call Wall 280（弱结构｜现价低于该位 1.7%）
最近结构参考: Call Wall 280（现价低于该位 1.7%）
量化视角： 负 Gamma（6.33亿，无历史分位）｜负 Gamma 加深（1.52亿）｜现价位于 Flip 下方 1.87%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 277（MaxPain，仅结算参考） / 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 251.0P — Vol 15,196 | 最新价 $0.01 | OI 4853→20025 (ΔOI +15172张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15172张（+312.6% vs前日OI），连续性待观察（方向未知）
10-23 250.0P — Vol 15,174 | 最新价 $0.01 | OI 7352→21594 (ΔOI +14242张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14242张（+193.7% vs前日OI），连续性待观察（方向未知）
10-26 283.0C — Vol 17,718 | 最新价 $0.17 | OI 5178→15266 (ΔOI +10088张) | ΔOI/Volume 56.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10088张（+194.8% vs前日OI），连续性待观察（方向未知）
10-30 270.0P — Vol 13,137 | 最新价 $1.38 | OI 33986→42454 (ΔOI +8468张) | ΔOI/Volume 64.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8468张（+24.9% vs前日OI），连续性待观察（方向未知）
10-30 260.0P — Vol 11,319 | 最新价 $0.38 | OI 78256→86466 (ΔOI +8210张) | ΔOI/Volume 72.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8210张（+10.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,180 张（Put 46,092 / Call 10,088），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 188.8k / P 258.1k，今日成交量: C 56.1k / P 103.7k，平值价格ATM: C $0.88 / P $0.78 ｜ ATM IV 27.7%，预期波动 ±0.6%，Max Pain 277
Top ΔOI: P 251 +15,172 ｜ P 250 +14,242 ｜ C 281 -10,775

📆 Forward Expiration Structure

10-26  C +16.3k / P +13.6k ｜ Activity HIGH ｜ 3D
10-27  C +1.7k / P +3.4k ｜ Activity HIGH ｜ 4D
10-28  C +1.4k / P +4.8k ｜ Activity HIGH ｜ 5D
10-29  C +2.0k / P +4.9k ｜ Activity HIGH ｜ 6D

📆 10-26 Forward Structure
存量OI: C 43.1k / P 44.2k，今日变化ΔOI: C +16.3k / P +13.6k，平值价格ATM: C $1.72 / P $1.55 ｜ ATM IV 15.5%，净 delta 敞口 119k shares
Top ΔOI: C 283 +10,088 ｜ P 270 +2,014 ｜ P 263 +1,538
仓位参考: Max Pain 274 ｜ Call Wall 283（+2.8%）（OI 15.3k） ｜ Put Wall 269（-2.3%）（OI 5.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.5%｜期限正常（远月高于近端）｜净 delta 敞口 正 119,152 股

📆 10-27 Forward Structure
存量OI: C 20.4k / P 20.3k，今日变化ΔOI: C +1.7k / P +3.4k，平值价格ATM: C $2.14 / P $1.93 ｜ ATM IV 17.1%，净 delta 敞口 -51k shares
Top ΔOI: P 272 +1,585 ｜ C 280 +425 ｜ P 273 +399
仓位参考: Max Pain 274 ｜ Call Wall 284（+3.2%）（OI 4.3k） ｜ Put Wall 272（-1.2%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 17.1%｜期限正常（远月高于近端）｜净 delta 敞口 负 51,414 股

📆 10-28 Forward Structure
存量OI: C 10.6k / P 20.7k，今日变化ΔOI: C +1.4k / P +4.8k，平值价格ATM: C $2.89 / P $2.64 ｜ ATM IV 21.1%，净 delta 敞口 -45k shares
Top ΔOI: P 270 +1,015 ｜ P 260 +973 ｜ P 265 +653
仓位参考: Max Pain 275 ｜ Call Wall 275（-0.1%）（OI 2.8k） ｜ Put Wall 260（-5.6%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 21.1%｜净 delta 敞口 负 44,557 股

📆 10-29 Forward Structure
存量OI: C 44.0k / P 11.4k，今日变化ΔOI: C +2.0k / P +4.9k，平值价格ATM: C $2.95 / P $3.27 ｜ ATM IV 22.0%，净 delta 敞口 -94k shares
Top ΔOI: P 270 +699 ｜ C 282 +646 ｜ P 273 +613
仓位参考: Max Pain 276 ｜ Call Wall 280（+1.7%，弱）（OI 15.3k） ｜ Put Wall 267（-3.0%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 22.0%｜净 delta 敞口 负 93,607 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/IWM_morning.json