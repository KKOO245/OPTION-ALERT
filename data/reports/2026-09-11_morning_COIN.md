# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.27 ｜ QQQ $714.88
VIX 15.78 ↓11.6%（5D +8.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.2　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 3.4 ｜ 前值 3.4　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 2.4 ｜ 前值 2.5　✅ 今日已公布
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 47.8 ｜ 前值 51.7　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: +4.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 182C ΔOI +4,962（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 172.28 → 今开 174.05（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 181.85 ｜ 低 172.80

Options: P/C成交量 0.44 | OI比 0.68 | ATM IV 103.8% | Skew -10.1pp | Term 0.66 | ExpMove ±7.6%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±7.6% ｜ 09-25（14D）±10.2% ｜ 10-02（21D）±12.8% ｜ 10-09（28D）±15.5%
   ⇒ IV–VIX Spread: +88.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,726,156 | GEX Change vs 上次快照 17,893,320 | Flip: Primary Flip: 163.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 499 / LOW 180 / INVALID 329
结构观察区: Primary Flip 163.81（全链重定价，覆盖 99%）
最近结构参考: Flip 164（现价高于该位 10.3%）
量化视角： 正 Gamma（2773万，无历史分位）｜正 Gamma 增强（+1789万）｜现价位于 Flip 上方 10.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 182.5C — Vol 5,075 | 最新价 $3.65 | OI 4373→9335 (ΔOI +4962张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4962张（+113.5% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 5,782 | 最新价 $5.75 | OI 3204→8022 (ΔOI +4818张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4818张（+150.4% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 3,967 | 最新价 $4.95 | OI 671→3760 (ΔOI +3089张) | ΔOI/Volume 77.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3089张（+460.4% vs前日OI），连续性待观察（方向未知）
09-18 190.0C — Vol 3,102 | 最新价 $1.97 | OI 7298→9029 (ΔOI +1731张) | ΔOI/Volume 55.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1731张（+23.7% vs前日OI），连续性待观察（方向未知）
09-18 187.5C — Vol 1,642 | 最新价 $2.50 | OI 698→1845 (ΔOI +1147张) | ΔOI/Volume 69.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1147张（+164.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,747 张（Put 0 / Call 15,747），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +15.0k / P -0.8k ｜ Activity HIGH ｜ 7D
09-25  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 14D
10-02  C +91 / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI: C 203.4k / P 97.0k，今日变化ΔOI: C +15.0k / P -0.8k，平值价格ATM: C $7.10 / P $6.60 ｜ ATM IV 67.1%，净 delta 敞口 904k shares
Top ΔOI: C 182 +4,962 ｜ C 175 +4,818 ｜ C 177 +3,089
仓位参考: Max Pain 175 ｜ Call Wall 182.5（+1.0%，弱）（OI 9.3k）
量化解读： 存量 Call 重｜ATM IV 67.1%｜历史 Rank 88%（近端代理）｜净 delta 敞口 正 903,836 股

📆 09-25 Forward Structure
存量OI: C 11.4k / P 9.2k，今日变化ΔOI: C +0.7k / P +0.4k，平值价格ATM: C $9.70 / P $8.80 ｜ ATM IV 65.7%，净 delta 敞口 19k shares
Top ΔOI: C 200 +171 ｜ C 175 +108
仓位参考: Max Pain 170 ｜ Call Wall 185（+2.4%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 65.7%｜历史 Rank 88%（近端代理）｜净 delta 敞口 正 19,234 股

10-02（MEDIUM △）仓位参考: Max Pain 188 ｜ Put Wall 172.5（-4.6%，弱）（OI 1.1k）

📆 10-09 Forward Structure
存量OI: C 1.8k / P 2.5k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $14.40 / P $13.68 ｜ ATM IV 68.3%，净 delta 敞口 3k shares
仓位参考: Max Pain 182 ｜ Call Wall 185（+2.4%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 68.3%｜历史 Rank 88%（近端代理）｜净 delta 敞口 正 2,535 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/COIN_morning.json