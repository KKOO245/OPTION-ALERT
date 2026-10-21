# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $772.65 ｜ QQQ $726.18
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-22 282C ΔOI +12,813（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-22 282C ΔOI +12,813 占该期限总 OI 16.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 275.78 → 今开 276.86（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 277.70 ｜ 低 275.84

Options: P/C成交量 0.66 | OI比 1.00 | ATM IV 22.8% | Skew 1.9pp | Term 0.83 | ExpMove ±0.9%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-22（1D）±0.9% ｜ 10-23（2D）±1.2% ｜ 10-26（5D）±1.6% ｜ 10-27（6D）±1.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -370,085,996 | GEX Change vs 上次快照 29,038,788 | Flip: Primary Flip: 279.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1301 / LOW 200 / INVALID 1373
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 279.31（全链重定价，覆盖 99%）
Put Wall 260（弱结构｜现价高于该位 6.4%） | Call Wall 280（弱结构｜现价低于该位 1.2%）
最近结构参考: Flip 279（现价低于该位 1.0%）
量化视角： 负 Gamma（3.70亿，无历史分位）｜负 Gamma 缓解（+2904万）｜现价位于 Flip 下方 1.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 275（MaxPain，仅结算参考）；上方 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 279（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 261.0P — Vol 64,239 | 最新价 $1.82 | OI 25921→52091 (ΔOI +26170张) | ΔOI/Volume 40.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26170张（+101.0% vs前日OI），连续性待观察（方向未知）
11-20 262.0P — Vol 54,111 | 最新价 $1.97 | OI 45262→67361 (ΔOI +22099张) | ΔOI/Volume 40.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22099张（+48.8% vs前日OI），连续性待观察（方向未知）
10-30 269.0P — Vol 18,444 | 最新价 $1.35 | OI 10169→28028 (ΔOI +17859张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17859张（+175.6% vs前日OI），连续性待观察（方向未知）
10-30 258.0P — Vol 18,153 | 最新价 $0.36 | OI 12049→29744 (ΔOI +17695张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17695张（+146.9% vs前日OI），连续性待观察（方向未知）
10-22 282.0C — Vol 13,525 | 最新价 $0.07 | OI 360→13173 (ΔOI +12813张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12813张（+3559.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 96,636 张（Put 83,823 / Call 12,813），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $12M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 42.6k / P 42.5k，今日成交量: C 125.5k / P 83.4k，平值价格ATM: C $0.41 / P $1.04 ｜ ATM IV 22.8%，预期波动 ±0.5%，Max Pain 275
Top ΔOI: C 275 -5,811 ｜ C 280 +5,061 ｜ C 277 -4,028

📆 Forward Expiration Structure

10-22  C +35.9k / P +4.4k ｜ Activity HIGH ｜ 1D
10-23  C +13.3k / P +13.1k ｜ Activity HIGH ｜ 2D
10-26  C +7.7k / P +5.0k ｜ Activity HIGH ｜ 5D
10-27  C +4.3k / P +2.5k ｜ Activity HIGH ｜ 6D

📆 10-22 Forward Structure
存量OI: C 48.3k / P 27.8k，今日变化ΔOI: C +35.9k / P +4.4k，平值价格ATM: C $1.00 / P $1.58 ｜ ATM IV 19.4%，净 delta 敞口 255k shares
Top ΔOI: C 282 +12,813 ｜ C 283 +9,347 ｜ C 280 +9,345
仓位参考: Max Pain 274 ｜ Call Wall 282（+2.0%，弱）（OI 13.2k） ｜ Put Wall 267（-3.4%）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 19.4%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 254,709 股

📆 10-23 Forward Structure
存量OI: C 156.2k / P 189.8k，今日变化ΔOI: C +13.3k / P +13.1k，平值价格ATM: C $1.44 / P $1.94 ｜ ATM IV 19.3%，净 delta 敞口 -84k shares
Top ΔOI: P 273 +8,064 ｜ C 278 +5,102 ｜ C 280 +4,592
仓位参考: Max Pain 276 ｜ Call Wall 280（+1.3%，弱）（OI 14.2k） ｜ Put Wall 267（-3.4%，弱）（OI 17.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 83,994 股

📆 10-26 Forward Structure
存量OI: C 24.2k / P 20.5k，今日变化ΔOI: C +7.7k / P +5.0k，平值价格ATM: C $2.12 / P $2.23 ｜ ATM IV 15.7%，净 delta 敞口 123k shares
Top ΔOI: C 280 +2,570 ｜ C 283 +1,681 ｜ C 278 +1,414
仓位参考: Max Pain 274 ｜ Call Wall 283（+2.3%，弱）（OI 5.1k） ｜ Put Wall 267（-3.4%）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 15.7%｜净 delta 敞口 正 123,329 股

📆 10-27 Forward Structure
存量OI: C 16.5k / P 13.7k，今日变化ΔOI: C +4.3k / P +2.5k，平值价格ATM: C $2.46 / P $2.20 ｜ ATM IV 16.2%，净 delta 敞口 67k shares
Top ΔOI: C 282 +1,835 ｜ C 279 +744 ｜ C 285 +584
仓位参考: Max Pain 272 ｜ Call Wall 284（+2.7%）（OI 4.3k） ｜ Put Wall 262（-5.2%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 16.2%｜净 delta 敞口 正 66,997 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/IWM_morning.json