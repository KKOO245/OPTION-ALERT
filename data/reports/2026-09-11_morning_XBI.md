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
🟡 **近现价集中开仓**: 09-18 156P ΔOI +998（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.82 → 今开 158.27（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 159.66 ｜ 低 156.83

Options: P/C成交量 6.54 | OI比 2.38 | ATM IV 27.3% | Skew 3.6pp | Term 1.06 | ExpMove ±3.9%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 3.6pp）｜当日成交偏 Put（P/C量 6.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 6.54×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±3.9% ｜ 09-25（14D）±10.4% ｜ 10-02（21D）±12.0% ｜ 10-09（28D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -54,107,017 | GEX Change vs 上次快照 2,051,685 | Flip: Primary Flip: 163.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 352 / LOW 163 / INVALID 345
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.79（全链重定价，覆盖 88%）
Put Wall 155（弱结构｜现价高于该位 2.0%） | Call Wall 170（弱结构｜现价低于该位 7.0%）
最近结构参考: Put Wall 155（现价高于该位 2.0%）
量化视角： 负 Gamma（5411万，无历史分位）｜负 Gamma 缓解（+205万）｜现价位于 Flip 下方 3.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（Put Wall，弱结构）；上方 161（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 155.0P — Vol 2,189 | 最新价 $0.55 | OI 4005→5866 (ΔOI +1861张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1861张（+46.5% vs前日OI），连续性待观察（方向未知）
09-11 156.0P — Vol 2,137 | 最新价 $0.75 | OI 368→2065 (ΔOI +1697张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1697张（+461.1% vs前日OI），连续性待观察（方向未知）
09-11 157.0P — Vol 1,640 | 最新价 $1.23 | OI 301→1789 (ΔOI +1488张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1488张（+494.4% vs前日OI），连续性待观察（方向未知）
09-18 156.0P — Vol 1,277 | 最新价 $2.35 | OI 2171→3169 (ΔOI +998张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增998张（+46.0% vs前日OI），连续性待观察（方向未知）
09-11 157.0C — Vol 517 | 最新价 $1.06 | OI 51→540 (ΔOI +489张) | ΔOI/Volume 94.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增489张（+958.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,533 张（Put 6,044 / Call 489），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.7k / P +0.7k ｜ Activity HIGH ｜ 7D
09-25  C +2 / P +0.1k ｜ Activity MEDIUM △ ｜ 14D
10-02  C +21 / P +33 ｜ Activity MEDIUM △ ｜ 21D
10-09  C +16 / P +10 ｜ Activity MEDIUM △ ｜ 28D

📆 09-18 Forward Structure
存量OI: C 71.2k / P 119.5k，今日变化ΔOI: C +0.7k / P +0.7k，平值价格ATM: C $2.60 / P $3.50 ｜ ATM IV 30.7%，净 delta 敞口 -15k shares
Top ΔOI: P 156 +998 ｜ P 155 -333 ｜ C 173 +232
仓位参考: Max Pain 158 ｜ Call Wall 155（-1.9%，弱）（OI 10.8k） ｜ Put Wall 158（-0.1%，弱）（OI 16.7k）
量化解读： 存量 Put 重｜ATM IV 30.7%｜历史 Rank 16%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 14,974 股

09-25（MEDIUM △）Top ΔOI: 151P +29 ｜ 160C +25
09-25（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 167（+5.6%）（OI 1.4k） ｜ Put Wall 154（-2.6%）（OI 1.2k）

10-02（MEDIUM △）Top ΔOI: 155P +16 ｜ 150P +6
10-02（MEDIUM △）仓位参考: Max Pain 161 ｜ Call Wall 165（+4.4%）（OI 0.2k） ｜ Put Wall 150（-5.1%，弱）（OI 0.2k）

10-09（MEDIUM △）Top ΔOI: 167C +13 ｜ 147P +7
10-09（MEDIUM △）仓位参考: Max Pain 160

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/XBI_morning.json