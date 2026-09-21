# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 154P ΔOI +4,758（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 158.49 → 收盘 158.23（-0.2%） ｜ 今日高 159.57 ｜ 低 156.58 ｜ 昨收 156.72 → 收盘 158.23（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.59 | OI比 3.93 | ATM IV 32.8% | Skew 2.0pp | Term 0.94 | ExpMove ±2.5%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 2.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 3.93×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±2.5% ｜ 10-02（11D）±3.8% ｜ 10-09（18D）±6.6% ｜ 10-16（25D）±5.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,091,974 | GEX Change vs 上次快照 -4,456,622 | Flip: Primary Flip: 166.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 362 / LOW 62 / INVALID 344
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.22（全链重定价，覆盖 100%）
Put Wall 150（现价高于该位 5.5%）
最近结构参考: Flip 166（现价低于该位 4.8%）
量化视角： 负 Gamma（2409万，无历史分位）｜负 Gamma 加深（446万）｜现价位于 Flip 下方 4.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 144.0P — Vol 14 | 最新价 $0.80 | OI 51→5049 (ΔOI +4998张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4998张（+9800.0% vs前日OI），连续性待观察（方向未知）
10-16 154.0P — Vol 46 | 最新价 $3.18 | OI 398→5156 (ΔOI +4758张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4758张（+1195.5% vs前日OI），连续性待观察（方向未知）
09-25 150.0P — Vol 12 | 最新价 $0.22 | OI 9586→14266 (ΔOI +4680张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4680张（+48.8% vs前日OI），连续性待观察（方向未知）
09-25 150.0C — Vol 1 | 最新价 $8.83 | OI 41→1042 (ΔOI +1001张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1001张（+2441.5% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 47（Yahoo补） | 最新价 $3.72 | OI 421→951 (ΔOI +530张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增530张（+125.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,967 张（Put 14,436 / Call 1,531），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +2.3k / P +5.0k ｜ Activity HIGH ｜ 4D
10-02  C -17 / P +81 ｜ Activity MEDIUM △ ｜ 11D
10-09  C +4 / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
10-16  C -0.1k / P +10.6k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 9.5k / P 37.3k，今日变化ΔOI: C +2.3k / P +5.0k，平值价格ATM: C $2.14 / P $1.81 ｜ ATM IV 32.8%，净 delta 敞口 117k shares
Top ΔOI: P 150 +4,680 ｜ C 150 +1,001 ｜ C 157 +450
仓位参考: Max Pain 157 ｜ Call Wall 160（+1.1%，弱）（OI 2.4k） ｜ Put Wall 150（-5.2%，弱）（OI 14.3k）
量化解读： 存量 Put 重｜ATM IV 32.8%｜历史 Rank 49%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 116,898 股

10-02（MEDIUM △）Top ΔOI: 165C -31 ｜ 157P -17
10-02（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 165（+4.3%）（OI 0.7k） ｜ Put Wall 157（-0.8%，弱）（OI 0.2k）

10-09（MEDIUM △）Top ΔOI: 150P +50 ｜ 158P +9
10-09（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+1.1%，弱）（OI 18） ｜ Put Wall 150（-5.2%，弱）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 144P +4,998 ｜ 154P +4,758
10-16（MEDIUM △）仓位参考: Max Pain 165 ｜ Call Wall 165（+4.3%，弱）（OI 2.3k） ｜ Put Wall 150（-5.2%）（OI 17.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/XBI_evening.json