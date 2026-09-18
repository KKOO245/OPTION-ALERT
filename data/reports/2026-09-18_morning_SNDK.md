# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $759.22 ｜ QQQ $717.48
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 1650C ΔOI +73（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 1600C ΔOI +4,061 占该期限总 OI 16.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,614.39 → 今开 1,624.06（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 1710.97 ｜ 低 1616.00

Options: P/C成交量 0.58 | OI比 1.11 | ATM IV 95.8% | Skew -7.6pp | Term 0.74 | ExpMove ±7.7%（近端） | Rank 47%
量化视角： IV 中性（Rank 47%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.11×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±7.7% ｜ 10-02（14D）±11.6% ｜ 10-09（21D）±14.1% ｜ 10-16（28D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,990,926 | GEX Change vs 上次快照 6,742,861 | Flip: Primary Flip: 1621.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 1828 / LOW 537 / INVALID 1053
结构观察区: Primary Flip 1621.03（全链重定价，覆盖 90%）
Call Wall 1,600（弱结构｜现价高于该位 6.2%）
最近结构参考: Flip 1621（现价高于该位 4.8%）
量化视角： 正 Gamma（1299万，无历史分位）｜正 Gamma 增强（+674万）｜现价位于 Flip 上方 4.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（MaxPain，仅结算参考） / 1,600（Call Wall，弱结构）。
• Gamma 区域：切换参考 1621（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 1600.0C — Vol 18 | 最新价 $125.00 | OI 500→4561 (ΔOI +4061张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4061张（+812.2% vs前日OI），连续性待观察（方向未知）
09-25 800.0P — Vol 2,126（Yahoo补） | 最新价 $0.05 | OI 116→1820 (ΔOI +1704张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1704张（+1469.0% vs前日OI），连续性待观察（方向未知）
09-25 1850.0C — Vol 421 | 最新价 $11.58 | OI 266→1035 (ΔOI +769张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增769张（+289.1% vs前日OI），连续性待观察（方向未知）
09-18 1500.0P — Vol 298 | 最新价 $0.23 | OI 3851→4550 (ΔOI +699张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增699张（+18.1% vs前日OI），值得跟踪（方向未知）
10-02 1800.0C — Vol 135 | 最新价 $42.80 | OI 517→1102 (ΔOI +585张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增585张（+113.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,818 张（Put 2,403 / Call 5,415），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 95.6k / P 106.3k，今日成交量: C 55.8k / P 32.4k，平值价格ATM: C $16.80 / P $17.45 ｜ ATM IV 95.8%，预期波动 ±2.0%，Max Pain 1,500
Top ΔOI: C 1800 -878 ｜ P 1500 +699 ｜ P 1480 +530

📆 Forward Expiration Structure

09-25  C +3.8k / P +4.5k ｜ Activity HIGH ｜ 7D
10-02  C +5.5k / P +0.5k ｜ Activity HIGH ｜ 14D
10-09  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
10-16  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 19.3k / P 25.0k，今日变化ΔOI: C +3.8k / P +4.5k，平值价格ATM: C $66.55 / P $64.56 ｜ ATM IV 68.4%，净 delta 敞口 100k shares
Top ΔOI: C 1850 +769 ｜ P 1550 +445
仓位参考: Max Pain 1,580 ｜ Call Wall 1850（+8.9%，弱）（OI 1.0k） ｜ Put Wall 1550（-8.8%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 68.4%｜历史 Rank 47%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 100,231 股

📆 10-02 Forward Structure
存量OI: C 14.6k / P 10.8k，今日变化ΔOI: C +5.5k / P +0.5k，平值价格ATM: C $100.00 / P $96.16 ｜ ATM IV 73.7%，净 delta 敞口 321k shares
Top ΔOI: C 1600 +4,061 ｜ C 1800 +585 ｜ C 2000 +126
仓位参考: Max Pain 1,590 ｜ Call Wall 1600（-5.8%）（OI 4.6k） ｜ Put Wall 1540（-9.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 73.7%｜历史 Rank 47%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 321,372 股

10-09（MEDIUM △）Top ΔOI: 1490P +43 ｜ 1410P +39
10-09（MEDIUM △）仓位参考: Max Pain 1,600 ｜ Call Wall 1600（-5.8%，弱）（OI 0.1k） ｜ Put Wall 1540（-9.3%，弱）（OI 0.2k）

📆 10-16 Forward Structure
存量OI: C 28.5k / P 36.7k，今日变化ΔOI: C +0.6k / P +0.2k，平值价格ATM: C $138.77 / P $131.60 ｜ ATM IV 71.2%，净 delta 敞口 12k shares
Top ΔOI: P 1460 -171 ｜ C 1650 +73
仓位参考: Max Pain 1,600 ｜ Call Wall 1800（+6.0%，弱）（OI 1.1k） ｜ Put Wall 1600（-5.8%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.2%｜历史 Rank 47%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 12,466 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SNDK_morning.json