# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 735C ΔOI +8,519（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 728.00 → 今开 725.48（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 725.94 ｜ 低 719.77

Options: P/C成交量 1.20 | OI比 1.64 | ATM IV 25.6% | Skew 2.2pp | Term 0.78 | ExpMove ±1.1%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜当日成交偏 Put（P/C量 1.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.20×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 2% ｜ P/C OI(近端) 51%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 2%）｜近端持仓结构中性（P/C OI 分位 51%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-19（3D）±1.1% ｜ 10-20（4D）±1.3% ｜ 10-21（5D）±1.6% ｜ 10-22（6D）±1.8%
   ⇒ IV–VIX Spread: +9.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,281,158,485 | GEX Change vs 上次快照 -349,505,488 | Flip: Primary Flip: 734.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2831 / LOW 442 / INVALID 1581
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 734.91（全链重定价，覆盖 93%）
Put Wall 700（弱结构｜现价高于该位 3.1%）
最近结构参考: Flip 735（现价低于该位 1.8%）
量化视角： 负 Gamma（12.81亿，历史分位偏负区，比 98% 的交易日更负）｜负 Gamma 加深（3.50亿）｜现价位于 Flip 下方 1.82%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 727（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 735（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 715.0P — Vol 68,161 | 最新价 $7.20 | OI 44330→95625 (ΔOI +51295张) | ΔOI/Volume 75.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增51295张（+115.7% vs前日OI），连续性待观察（方向未知）
10-16 723.0P — Vol 58,420 | 最新价 $1.60 | OI 5550→25266 (ΔOI +19716张) | ΔOI/Volume 33.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19716张（+355.2% vs前日OI），连续性待观察（方向未知）
11-20 600.0P — Vol 21,164 | 最新价 $1.18 | OI 15924→34825 (ΔOI +18901张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18901张（+118.7% vs前日OI），连续性待观察（方向未知）
10-16 721.0P — Vol 49,007 | 最新价 $1.14 | OI 2790→19686 (ΔOI +16896张) | ΔOI/Volume 34.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16896张（+605.6% vs前日OI），连续性待观察（方向未知）
11-06 769.0C — Vol 15,083 | 最新价 $1.55 | OI 319→15342 (ΔOI +15023张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15023张（+4709.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 121,831 张（Put 106,808 / Call 15,023），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $44M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 847.5k / P 1388.6k，今日成交量: C 506.8k / P 607.2k，平值价格ATM: C $1.77 / P $2.24 ｜ ATM IV 25.6%，预期波动 ±0.6%，Max Pain 727
Top ΔOI: P 723 +19,716 ｜ P 721 +16,896 ｜ P 722 +14,027

📆 Forward Expiration Structure

10-19  C +34.7k / P +46.1k ｜ Activity HIGH ｜ 3D
10-20  C +16.5k / P +13.3k ｜ Activity HIGH ｜ 4D
10-21  C +7.9k / P +5.5k ｜ Activity HIGH ｜ 5D
10-22  C +7.9k / P +8.3k ｜ Activity HIGH ｜ 6D

📆 10-19 Forward Structure
存量OI: C 89.5k / P 132.8k，今日变化ΔOI: C +34.7k / P +46.1k，平值价格ATM: C $3.64 / P $4.03 ｜ ATM IV 14.0%，净 delta 敞口 364k shares
Top ΔOI: C 735 +8,519 ｜ P 700 +6,598
仓位参考: Max Pain 730 ｜ Call Wall 735（+1.9%）（OI 9.2k） ｜ Put Wall 700（-3.0%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜ATM IV 14.0%｜历史 Rank 81%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 364,400 股

📆 10-20 Forward Structure
存量OI: C 57.8k / P 59.4k，今日变化ΔOI: C +16.5k / P +13.3k，平值价格ATM: C $4.70 / P $4.82 ｜ ATM IV 15.6%，净 delta 敞口 186k shares
Top ΔOI: P 705 +5,910 ｜ C 750 +3,647 ｜ C 743 +1,791
仓位参考: Max Pain 728 ｜ Call Wall 733（+1.6%，弱）（OI 4.1k） ｜ Put Wall 705（-2.3%，弱）（OI 6.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.6%｜历史 Rank 81%（近端代理）｜IV/RV 1.32×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 185,831 股

📆 10-21 Forward Structure
存量OI: C 31.5k / P 39.4k，今日变化ΔOI: C +7.9k / P +5.5k，平值价格ATM: C $5.62 / P $6.04 ｜ ATM IV 16.8%，净 delta 敞口 188k shares
Top ΔOI: P 685 +1,349 ｜ C 740 +1,122 ｜ P 690 +1,110
仓位参考: Max Pain 733 ｜ Call Wall 740（+2.6%，弱）（OI 1.4k） ｜ Put Wall 710（-1.6%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.8%｜历史 Rank 81%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 正 187,536 股

📆 10-22 Forward Structure
存量OI: C 20.6k / P 29.4k，今日变化ΔOI: C +7.9k / P +8.3k，平值价格ATM: C $6.41 / P $6.90 ｜ ATM IV 17.6%，净 delta 敞口 67k shares
Top ΔOI: C 710 +1,346 ｜ P 710 +1,215 ｜ C 745 +984
仓位参考: Max Pain 727 ｜ Call Wall 710（-1.6%，弱）（OI 1.4k） ｜ Put Wall 705（-2.3%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 81%（近端代理）｜IV/RV 1.49×（近似）｜净 delta 敞口 正 67,052 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/QQQ_morning.json