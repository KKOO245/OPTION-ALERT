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
🟡 **近现价集中开仓**: 11-16 700C ΔOI +1,654（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-19 585P ΔOI +12,107 占该期限总 OI 21.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 688.17 → 今开 688.51（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 688.75 ｜ 低 673.10

Options: P/C成交量 1.24 | OI比 1.36 | ATM IV 43.3% | Skew 6.5pp | Term 0.59 | ExpMove ±1.8%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价显著（Skew 6.5pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.36×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 21% ｜ P/C OI(近端) 25%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 21%）｜近端持仓结构中性（P/C OI 分位 25%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-16（3D）±1.8% ｜ 11-17（4D）±2.3% ｜ 11-18（5D）±2.7% ｜ 11-19（6D）±3.1%
   ⇒ IV–VIX Spread: +23.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -472,700,937 | GEX Change vs 上次快照 -309,503,699 | Flip: Primary Flip: 690.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3677 / LOW 459 / INVALID 1476
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 690.40（全链重定价，覆盖 96%）
Put Wall 680（弱结构｜现价低于该位 0.2%）
最近结构参考: Put Wall 680（现价低于该位 0.2%）
量化视角： 负 Gamma（4.73亿，历史分位偏负区，比 79% 的交易日更负）｜负 Gamma 加深（3.10亿）｜现价位于 Flip 下方 1.75%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 680（Put Wall，弱结构） / 686（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 690（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 750.0C — Vol 22,499 | 最新价 $2.16 | OI 34636→54290 (ΔOI +19654张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19654张（+56.7% vs前日OI），连续性待观察（方向未知）
11-19 585.0P — Vol 12,921 | 最新价 $0.26 | OI 16→12123 (ΔOI +12107张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12107张（+75668.8% vs前日OI），连续性待观察（方向未知）
11-13 700.0C — Vol 64,298 | 最新价 $0.69 | OI 14383→26461 (ΔOI +12078张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12078张（+84.0% vs前日OI），连续性待观察（方向未知）
12-11 685.0P — Vol 9,075 | 最新价 $17.01 | OI 281→9031 (ΔOI +8750张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8750张（+3113.9% vs前日OI），连续性待观察（方向未知）
12-11 705.0C — Vol 8,837 | 最新价 $12.20 | OI 832→9486 (ΔOI +8654张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8654张（+1040.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 61,243 张（Put 20,857 / Call 40,386），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $15M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 386.9k / P 524.6k，今日成交量: C 480.8k / P 594.7k，平值价格ATM: C $3.75 / P $2.66 ｜ ATM IV 43.3%，预期波动 ±0.9%，Max Pain 686
Top ΔOI: C 700 +12,078 ｜ P 685 +6,473 ｜ C 695 +5,047

📆 Forward Expiration Structure

11-16  C +13.1k / P +28.1k ｜ Activity HIGH ｜ 3D
11-17  C +5.1k / P +18.6k ｜ Activity HIGH ｜ 4D
11-18  C +3.9k / P +2.9k ｜ Activity HIGH ｜ 5D
11-19  C +3.9k / P +26.6k ｜ Activity HIGH ｜ 6D

📆 11-16 Forward Structure
存量OI: C 70.2k / P 91.1k，今日变化ΔOI: C +13.1k / P +28.1k，平值价格ATM: C $6.57 / P $5.47 ｜ ATM IV 23.3%，净 delta 敞口 -508k shares
Top ΔOI: P 640 +5,718 ｜ P 634 +2,230 ｜ C 700 +1,654
仓位参考: Max Pain 686 ｜ Call Wall 690（+1.7%，弱）（OI 2.2k） ｜ Put Wall 685（+1.0%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 23.3%｜历史 Rank 97%（近端代理）｜IV/RV 0.66×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 508,413 股

📆 11-17 Forward Structure
存量OI: C 43.2k / P 59.0k，今日变化ΔOI: C +5.1k / P +18.6k，平值价格ATM: C $8.23 / P $7.22 ｜ ATM IV 26.7%，净 delta 敞口 -475k shares
Top ΔOI: P 680 +5,136 ｜ P 675 +2,727
仓位参考: Max Pain 680 ｜ Put Wall 680（+0.2%）（OI 5.7k）
量化解读： 存量 Put 重｜ATM IV 26.7%｜历史 Rank 97%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 474,619 股

📆 11-18 Forward Structure
存量OI: C 24.8k / P 63.2k，今日变化ΔOI: C +3.9k / P +2.9k，平值价格ATM: C $9.85 / P $8.70 ｜ ATM IV 28.7%，净 delta 敞口 -88k shares
Top ΔOI: C 719 +984 ｜ P 625 -783
仓位参考: Max Pain 680 ｜ Call Wall 695（+2.5%，弱）（OI 0.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.7%｜历史 Rank 97%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 87,944 股

📆 11-19 Forward Structure
存量OI: C 17.0k / P 39.5k，今日变化ΔOI: C +3.9k / P +26.6k，平值价格ATM: C $10.96 / P $9.99 ｜ ATM IV 29.5%，净 delta 敞口 -109k shares
Top ΔOI: P 585 +12,107 ｜ P 575 +7,962
仓位参考: Max Pain 680 ｜ Call Wall 680（+0.2%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 29.5%｜历史 Rank 97%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 108,573 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/QQQ_morning.json