# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.80 ｜ QQQ $679.89
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 268P ΔOI +2,820（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 278.44 → 今开 278.95（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 279.16 ｜ 低 274.81

Options: P/C成交量 2.59 | OI比 1.54 | ATM IV 30.9% | Skew 5.8pp | Term 0.63 | ExpMove ±1.2%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价中性（Skew 5.8pp）｜当日成交偏 Put（P/C量 2.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.59×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.54×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±1.2% ｜ 11-17（4D）±1.5% ｜ 11-18（5D）±1.8% ｜ 11-19（6D）±2.0%
   ⇒ IV–VIX Spread: +11.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,223,687,915 | GEX Change vs 上次快照 -346,381,123 | Flip: Primary Flip: 284.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1299 / LOW 251 / INVALID 1024
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.36（全链重定价，覆盖 97%）
Put Wall 270（弱结构｜现价高于该位 2.3%） | Call Wall 300（弱结构｜现价低于该位 7.9%）
最近结构参考: Put Wall 270（现价高于该位 2.3%）
量化视角： 负 Gamma（12.24亿，无历史分位）｜负 Gamma 加深（3.46亿）｜现价位于 Flip 下方 2.84%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 279（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 265.0P — Vol 32,691 | 最新价 $2.66 | OI 63230→87416 (ΔOI +24186张) | ΔOI/Volume 74.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24186张（+38.2% vs前日OI），连续性待观察（方向未知）
11-27 262.0P — Vol 23,891 | 最新价 $0.58 | OI 3179→23423 (ΔOI +20244张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20244张（+636.8% vs前日OI），连续性待观察（方向未知）
11-20 270.0P — Vol 39,381 | 最新价 $0.88 | OI 136015→155115 (ΔOI +19100张) | ΔOI/Volume 48.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19100张（+14.0% vs前日OI），连续性待观察（方向未知）
12-18 266.0P — Vol 26,249 | 最新价 $2.79 | OI 12313→25985 (ΔOI +13672张) | ΔOI/Volume 52.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13672张（+111.0% vs前日OI），连续性待观察（方向未知）
11-27 272.0P — Vol 14,841 | 最新价 $1.76 | OI 371→13627 (ΔOI +13256张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13256张（+3573.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 90,458 张（Put 90,458 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $13M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 126.4k / P 194.8k，今日成交量: C 52.5k / P 136.0k，平值价格ATM: C $1.07 / P $0.79 ｜ ATM IV 30.9%，预期波动 ±0.7%，Max Pain 279
Top ΔOI: P 267 +2,140 ｜ P 277 +1,722 ｜ C 285 +1,649

📆 Forward Expiration Structure

11-16  C +6.5k / P +8.9k ｜ Activity HIGH ｜ 3D
11-17  C +2.1k / P +1.7k ｜ Activity HIGH ｜ 4D
11-18  C +4.0k / P +6.3k ｜ Activity HIGH ｜ 5D
11-19  C +1.5k / P +2.7k ｜ Activity HIGH ｜ 6D

📆 11-16 Forward Structure
存量OI: C 21.5k / P 29.5k，今日变化ΔOI: C +6.5k / P +8.9k，平值价格ATM: C $1.83 / P $1.54 ｜ ATM IV 16.1%，净 delta 敞口 -227k shares
Top ΔOI: P 268 +2,820 ｜ C 285 +2,144 ｜ P 276 +1,179
仓位参考: Max Pain 280 ｜ Call Wall 285（+3.2%）（OI 4.4k） ｜ Put Wall 270（-2.3%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜ATM IV 16.1%｜历史 Rank 69%（近端代理）｜IV/RV 0.66×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 226,948 股

📆 11-17 Forward Structure
存量OI: C 9.6k / P 12.8k，今日变化ΔOI: C +2.1k / P +1.7k，平值价格ATM: C $2.31 / P $1.93 ｜ ATM IV 17.6%，净 delta 敞口 -87k shares
Top ΔOI: P 279 +736 ｜ C 282 +462 ｜ C 281 +451
仓位参考: Max Pain 280 ｜ Call Wall 283（+2.4%，弱）（OI 0.8k） ｜ Put Wall 260（-5.9%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.6%｜历史 Rank 69%（近端代理）｜IV/RV 0.72×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 87,198 股

📆 11-18 Forward Structure
存量OI: C 12.7k / P 12.9k，今日变化ΔOI: C +4.0k / P +6.3k，平值价格ATM: C $2.67 / P $2.36 ｜ ATM IV 18.7%，净 delta 敞口 -198k shares
Top ΔOI: P 268 +1,330 ｜ P 277 +1,047 ｜ P 276 +960
仓位参考: Max Pain 280 ｜ Call Wall 288（+4.2%，弱）（OI 1.4k） ｜ Put Wall 275（-0.5%）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 18.7%｜历史 Rank 69%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 负 198,417 股

📆 11-19 Forward Structure
存量OI: C 5.1k / P 8.4k，今日变化ΔOI: C +1.5k / P +2.7k，平值价格ATM: C $3.02 / P $2.42 ｜ ATM IV 19.6%，净 delta 敞口 -96k shares
Top ΔOI: P 281 +599 ｜ C 285 +495 ｜ P 275 +342
仓位参考: Max Pain 281 ｜ Call Wall 286（+3.5%，弱）（OI 0.8k） ｜ Put Wall 270（-2.3%）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 19.6%｜历史 Rank 69%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 负 95,533 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/IWM_morning.json