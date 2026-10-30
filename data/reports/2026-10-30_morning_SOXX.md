# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $756.16 ｜ QQQ $690.49
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 492P ΔOI +4,485（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 500P ΔOI +1,033 占该期限总 OI 11.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 513.86 → 今开 479.36（-6.7%） | 较昨收变动（含盘初走势） ｜ 今日高 483.39 ｜ 低 475.69

Options: P/C成交量 9.10 | OI比 6.15 | ATM IV 73.9% | Skew 4.2pp | Term 0.60 | ExpMove ±5.2%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 4.2pp）｜当日成交偏 Put（P/C量 9.10）——观察点，非方向信号
   ⇒ Put/Call Volume: 9.10×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 6.15×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±5.2% ｜ 11-13（14D）±7.4% ｜ 11-20（21D）±8.8% ｜ 11-27（28D）±14.8%
   ⇒ IV–VIX Spread: +55.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -55,751,686 | GEX Change vs 上次快照 -69,407,942 | Flip: Primary Flip: 506.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 538 / LOW 314 / INVALID 740
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 506.13（全链重定价，覆盖 91%）
最近结构参考: Flip 506（现价低于该位 5.3%）
量化视角： 负 Gamma（5575万，无历史分位）｜由正转负（6941万）｜现价位于 Flip 下方 5.34%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 502（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 506（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 475.0P — Vol 4,825 | 最新价 $8.80 | OI 1716→6233 (ΔOI +4517张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4517张（+263.2% vs前日OI），连续性待观察（方向未知）
11-06 492.5P — Vol 4,500 | 最新价 $5.95 | OI 26→4511 (ΔOI +4485张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4485张（+17250.0% vs前日OI），连续性待观察（方向未知）
11-06 460.0P — Vol 4,540 | 最新价 $1.60 | OI 410→4851 (ΔOI +4441张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4441张（+1083.2% vs前日OI），连续性待观察（方向未知）
11-27 500.0P — Vol 1,061 | 最新价 $17.55 | OI 1077→2110 (ΔOI +1033张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1033张（+95.9% vs前日OI），连续性待观察（方向未知）
11-20 465.0P — Vol 1 | 最新价 $6.30 | OI 266→1164 (ΔOI +898张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增898张（+337.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,374 张（Put 15,374 / Call 0），跨 3 个期限｜近端保护（5 档，距现价 ≤5%，权利金合计约 $10M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 28.9k / P 177.8k，今日成交量: C 1.5k / P 13.9k，平值价格ATM: C $3.88 / P $3.80 ｜ ATM IV 73.9%，预期波动 ±1.6%，Max Pain 502
Top ΔOI: P 470 -3,797 ｜ P 500 -2,810 ｜ P 550 -2,588

📆 Forward Expiration Structure

11-06  C +0.7k / P +9.2k ｜ Activity HIGH ｜ 7D
11-13  C -0.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 14D
11-20  C +2.3k / P +6.3k ｜ Activity HIGH ｜ 21D
11-27  C +42 / P +1.1k ｜ Activity HIGH ｜ 28D

📆 11-06 Forward Structure
存量OI: C 38.6k / P 19.4k，今日变化ΔOI: C +0.7k / P +9.2k，平值价格ATM: C $13.07 / P $12.00 ｜ ATM IV 48.3%，净 delta 敞口 -392k shares
Top ΔOI: P 492 +4,485 ｜ P 460 +4,441 ｜ P 500 +239
仓位参考: Max Pain 505 ｜ Put Wall 460（-4.0%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.3%｜历史 Rank 98%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 391,503 股

11-13（MEDIUM △）Top ΔOI: 480P +378 ｜ 500C -90
11-13（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 510（+6.5%，弱）（OI 9.6k） ｜ Put Wall 460（-4.0%）（OI 3.3k）

📆 11-20 Forward Structure
存量OI: C 41.7k / P 69.4k，今日变化ΔOI: C +2.3k / P +6.3k，平值价格ATM: C $20.90 / P $21.49 ｜ ATM IV 46.0%，净 delta 敞口 -219k shares
Top ΔOI: P 475 +4,517 ｜ P 465 +898 ｜ C 575 +745
仓位参考: Max Pain 530 ｜ Call Wall 505（+5.4%，弱）（OI 2.7k） ｜ Put Wall 460（-4.0%，弱）（OI 7.0k）
量化解读： 存量 Put 重｜ATM IV 46.0%｜历史 Rank 98%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 219,322 股

📆 11-27 Forward Structure
存量OI: C 4.1k / P 5.1k，今日变化ΔOI: C +42 / P +1.1k，平值价格ATM: C $48.00 / P $22.95 ｜ ATM IV 44.5%，净 delta 敞口 -64k shares
Top ΔOI: P 500 +1,033 ｜ P 520 +13
仓位参考: Max Pain 505 ｜ Call Wall 505（+5.4%，弱）（OI 0.9k） ｜ Put Wall 500（+4.4%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 44.5%｜历史 Rank 98%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 63,576 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SOXX_morning.json