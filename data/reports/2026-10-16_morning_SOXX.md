# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $762.90 ｜ QQQ $709.80
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
🟡 **近现价集中开仓**: 10-23 500C ΔOI +975（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 580C ΔOI +700 占该期限总 OI 13.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 514.71 → 今开 505.01（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 507.87 ｜ 低 501.10

Options: P/C成交量 2.01 | OI比 2.24 | ATM IV 65.7% | Skew 8.9pp | Term 0.61 | ExpMove ±4.2%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.01）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.01×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±4.2% ｜ 10-30（14D）±6.0% ｜ 11-06（21D）±8.2% ｜ 11-13（28D）±8.9%
   ⇒ IV–VIX Spread: +49.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -51,674,520 | GEX Change vs 上次快照 -3,275,869 | Flip: Primary Flip: 558.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 621 / LOW 322 / INVALID 709
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 558.80（全链重定价，覆盖 89%）
Put Wall 500（弱结构｜现价高于该位 0.8%）
最近结构参考: Put Wall 500（现价高于该位 0.8%）
量化视角： 负 Gamma（5167万，无历史分位）｜负 Gamma 加深（328万）｜现价位于 Flip 下方 9.79%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall，弱结构）；上方 530（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 559（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 480.0P — Vol 3,544 | 最新价 $5.90 | OI 3488→6970 (ΔOI +3482张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3482张（+99.8% vs前日OI），连续性待观察（方向未知）
10-30 600.0C — Vol 3,508 | 最新价 $0.61 | OI 263→3076 (ΔOI +2813张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2813张（+1069.6% vs前日OI），连续性待观察（方向未知）
10-30 585.0C — Vol 1,502 | 最新价 $1.42 | OI 48→1547 (ΔOI +1499张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1499张（+3122.9% vs前日OI），连续性待观察（方向未知）
11-20 460.0P — Vol 1,256 | 最新价 $8.16 | OI 2741→3813 (ΔOI +1072张) | ΔOI/Volume 85.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1072张（+39.1% vs前日OI），连续性待观察（方向未知）
10-30 580.0C — Vol 1,005 | 最新价 $1.57 | OI 79→1064 (ΔOI +985张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增985张（+1246.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,851 张（Put 4,554 / Call 5,297），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 45.1k / P 100.9k，今日成交量: C 0.7k / P 1.4k，平值价格ATM: C $2.83 / P $4.35 ｜ ATM IV 65.7%，预期波动 ±1.4%，Max Pain 530
Top ΔOI: C 600 -1,674 ｜ P 520 -1,227 ｜ P 510 -874

📆 Forward Expiration Structure

10-23  C +2.8k / P +1.0k ｜ Activity HIGH ｜ 7D
10-30  C +7.1k / P -3.5k ｜ Activity HIGH ｜ 14D
11-06  C +1.5k / P +0.3k ｜ Activity HIGH ｜ 21D
11-13  C +76 / P -37 ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 6.9k / P 15.5k，今日变化ΔOI: C +2.8k / P +1.0k，平值价格ATM: C $11.00 / P $10.25 ｜ ATM IV 38.9%，净 delta 敞口 93k shares
Top ΔOI: C 500 +975 ｜ P 490 +807 ｜ C 510 +298
仓位参考: Max Pain 548 ｜ Call Wall 500（-0.8%，弱）（OI 1.1k） ｜ Put Wall 510（+1.2%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.9%｜历史 Rank 95%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 93,353 股

📆 10-30 Forward Structure
存量OI: C 14.8k / P 45.0k，今日变化ΔOI: C +7.1k / P -3.5k，平值价格ATM: C $16.56 / P $13.80 ｜ ATM IV 41.3%，净 delta 敞口 247k shares
Top ΔOI: P 500 -5,051 ｜ P 480 +3,482 ｜ C 600 +2,813
仓位参考: Max Pain 550 ｜ Put Wall 500（-0.8%）（OI 12.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 247,168 股

📆 11-06 Forward Structure
存量OI: C 2.9k / P 2.4k，今日变化ΔOI: C +1.5k / P +0.3k，平值价格ATM: C $21.25 / P $20.34 ｜ ATM IV 41.2%，净 delta 敞口 16k shares
Top ΔOI: C 580 +700 ｜ C 550 +411 ｜ C 585 +286
仓位参考: Max Pain 550 ｜ Call Wall 535（+6.1%，弱）（OI 0.2k） ｜ Put Wall 500（-0.8%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 41.2%｜历史 Rank 95%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,628 股

11-13（MEDIUM △）Top ΔOI: 515P -43 ｜ 520C +26
11-13（MEDIUM △）仓位参考: Max Pain 560 ｜ Put Wall 520（+3.2%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SOXX_morning.json