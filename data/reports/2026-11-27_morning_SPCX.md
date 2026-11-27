# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $641.98
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 12-02 134C ΔOI +1,160（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-07 140C ΔOI +467 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 127.44 → 今开 131.20（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 131.29 ｜ 低 129.10

Options: P/C成交量 0.48 | OI比 0.44 | ATM IV 112.3% | Skew 5.8pp | Term 0.56 | ExpMove ±4.5%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价中性（Skew 5.8pp）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±4.5% ｜ 12-02（5D）±6.3% ｜ 12-04（7D）±8.1% ｜ 12-07（10D）±8.8%
   ⇒ IV–VIX Spread: +84.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 30,784,598 | GEX Change vs 上次快照 60,507,777 | Flip: Primary Flip: 125.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 865 / LOW 183 / INVALID 882
结构观察区: Primary Flip 125.81（全链重定价，覆盖 93%）
最近结构参考: Flip 126（现价高于该位 2.9%）
量化视角： 正 Gamma（3078万，无历史分位）｜由负转正（+6051万）｜现价位于 Flip 上方 2.92%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 128（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 126（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 100.0P — Vol 28,305 | 最新价 $1.48 | OI 18602→29919 (ΔOI +11317张) | ΔOI/Volume 40.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11317张（+60.8% vs前日OI），连续性待观察（方向未知）
12-11 105.0P — Vol 10,615 | 最新价 $1.60 | OI 660→10471 (ΔOI +9811张) | ΔOI/Volume 92.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9811张（+1486.5% vs前日OI），连续性待观察（方向未知）
11-30 75.0P — Vol 6,884 | 最新价 $0.03 | OI 3→6483 (ΔOI +6480张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6480张（+216000.0% vs前日OI），连续性待观察（方向未知）
11-30 115.0P — Vol 9,297 | 最新价 $0.59 | OI 5197→11142 (ΔOI +5945张) | ΔOI/Volume 64.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5945张（+114.4% vs前日OI），连续性待观察（方向未知）
11-30 95.0P — Vol 6,034 | 最新价 $0.05 | OI 20→5288 (ΔOI +5268张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5268张（+26340.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 38,821 张（Put 38,821 / Call 0），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（5 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 242.3k / P 105.7k，今日成交量: C 68.9k / P 33.3k，平值价格ATM: C $1.29 / P $1.02 ｜ ATM IV 112.3%，预期波动 ±1.8%，Max Pain 128
Top ΔOI: C 121 +4,168 ｜ P 140 -2,866 ｜ C 125 +2,063

📆 Forward Expiration Structure

11-30  C +12.0k / P +27.2k ｜ Activity HIGH ｜ 3D
12-02  C +7.3k / P +4.0k ｜ Activity HIGH ｜ 5D
12-04  C +8.7k / P +8.0k ｜ Activity HIGH ｜ 7D
12-07  C +1.3k / P +0.8k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 38.1k / P 43.1k，今日变化ΔOI: C +12.0k / P +27.2k，平值价格ATM: C $3.15 / P $2.64 ｜ ATM IV 58.4%，净 delta 敞口 627k shares
Top ΔOI: P 115 +5,945
仓位参考: Max Pain 125 ｜ Call Wall 140（+8.1%）（OI 6.6k） ｜ Put Wall 117（-9.6%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜ATM IV 58.4%｜历史 Rank 96%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 627,093 股

📆 12-02 Forward Structure
存量OI: C 17.8k / P 7.6k，今日变化ΔOI: C +7.3k / P +4.0k，平值价格ATM: C $4.35 / P $3.85 ｜ ATM IV 67.7%，净 delta 敞口 290k shares
Top ΔOI: C 134 +1,160 ｜ C 126 +956 ｜ C 135 +764
仓位参考: Max Pain 125 ｜ Call Wall 135（+4.3%，弱）（OI 1.8k） ｜ Put Wall 120（-7.3%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 67.7%｜历史 Rank 96%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 289,716 股

📆 12-04 Forward Structure
存量OI: C 124.3k / P 99.5k，今日变化ΔOI: C +8.7k / P +8.0k，平值价格ATM: C $5.45 / P $5.00 ｜ ATM IV 71.4%，净 delta 敞口 509k shares
Top ΔOI: P 110 +3,636 ｜ P 130 -2,163 ｜ P 119 +1,219
仓位参考: Max Pain 135 ｜ Call Wall 137（+5.8%，弱）（OI 10.5k） ｜ Put Wall 140（+8.1%，弱）（OI 11.7k）
量化解读： 存量 Call 重｜ATM IV 71.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 508,511 股

📆 12-07 Forward Structure
存量OI: C 3.0k / P 1.6k，今日变化ΔOI: C +1.3k / P +0.8k，平值价格ATM: C $5.98 / P $5.38 ｜ ATM IV 64.7%，净 delta 敞口 42k shares
Top ΔOI: C 140 +467 ｜ C 125 +272
仓位参考: Max Pain 125 ｜ Call Wall 140（+8.1%）（OI 0.7k） ｜ Put Wall 130（+0.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 64.7%｜历史 Rank 96%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 41,990 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SPCX_morning.json