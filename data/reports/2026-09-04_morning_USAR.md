# 期权晨报 2026-09-04（快照 10:20 ET）

📊 市场环境

SPY $772.01 ｜ QQQ $719.80
VIX 14.05 ↓1.9%（5D -2.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 43.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 18C ΔOI +84（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 23C ΔOI +4,029 占该期限总 OI 44.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 17.69 → 今开 18.65（+5.4%） | 较昨收变动（含盘初走势） ｜ 今日高 19.30 ｜ 低 17.63

Options: P/C成交量 0.23 | OI比 0.31 | ATM IV 129.8% | Skew -18.3pp | Term 0.63 | ExpMove ±8.0%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜Put 保护异常便宜（Skew -18.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±8.0% ｜ 09-18（14D）±11.5% ｜ 09-25（21D）±17.3% ｜ 10-02（28D）±20.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,489,836 | GEX Change vs 上次快照 4,706,103 | Flip: Primary Flip: 16.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 224 / LOW 104 / INVALID 200
结构观察区: Primary Flip 16.53（全链重定价，覆盖 95%）
最近结构参考: Flip 17（现价高于该位 8.2%）
量化视角： 正 Gamma（949万，无历史分位）｜正 Gamma 增强（+471万）｜现价位于 Flip 上方 8.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 23.0C — Vol 6,262（Yahoo补） | 最新价 $0.31 | OI 50→4079 (ΔOI +4029张) | ΔOI/Volume 64.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4029张（+8058.0% vs前日OI），连续性待观察（方向未知）
10-09 22.0C — Vol 3 | 最新价 $0.70 | OI 14→3013 (ΔOI +2999张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2999张（+21421.4% vs前日OI），连续性待观察（方向未知）
09-18 20.5C — Vol 1 | 最新价 $0.46 | OI 156→698 (ΔOI +542张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增542张（+347.4% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 38 | 最新价 $0.33 | OI 519→966 (ΔOI +447张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增447张（+86.1% vs前日OI），值得跟踪（方向未知）
09-18 21.0C — Vol 25 | 最新价 $0.31 | OI 1406→1792 (ΔOI +386张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增386张（+27.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,403 张（Put 447 / Call 7,956），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.6k / P +1.0k ｜ Activity HIGH ｜ 7D
09-18  C +1.2k / P -0.6k ｜ Activity HIGH ｜ 14D
09-25  C +77 / P -84 ｜ Activity MEDIUM △ ｜ 21D
10-02  C +4.2k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 16.5k / P 4.6k
今日变化ΔOI: C +0.6k / P +1.0k
平值价格ATM:  C 0.68 / P 0.75
隐含波动率 ATM IV:  72.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +447 ｜ $0.33 ｜ 名义 $14.8k* ｜ -4.9%
C 19 ｜ +167 ｜ $0.34 ｜ 名义 $5.7k* ｜ +6.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+6.2%） / 17（-4.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.0%｜历史 Rank 62%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 15,232 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 113.8k / P 63.9k
今日变化ΔOI: C +1.2k / P -0.6k
平值价格ATM:  C 1.05 / P 1.00
隐含波动率 ATM IV:  76.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 103k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ -305 ｜ $1.00 ｜ 名义 $-30.5k* ｜ +0.6%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 76.0%｜历史 Rank 62%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 102,704 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 29P -168

📆 10-02 Forward Structure
存量OI:      C 7.0k / P 2.0k
今日变化ΔOI: C +4.2k / P +0.5k
平值价格ATM:  C 2.10 / P 1.64
隐含波动率 ATM IV:  81.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 78k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 23 ｜ +4,029 ｜ $0.31 ｜ 名义 $124.9k* ｜ +28.6%
C 18 ｜ +84 ｜ $2.10 ｜ 名义 $17.6k* ｜ +0.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：23（+28.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 81.9%｜历史 Rank 62%（近端代理）｜净 delta 敞口 正 78,490 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/USAR_morning.json