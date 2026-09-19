# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.85 ｜ QQQ $nan
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-21 770C ΔOI +28,265（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-21 770C ΔOI +28,265 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 762.60 → 今开 761.31（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 761.76 ｜ 低 758.75

Options: P/C成交量 1.43 | OI比 3.76 | ATM IV 14.3% | Skew 2.0pp | Term 0.87 | ExpMove ±0.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 2.0pp）｜当日成交偏 Put（P/C量 1.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.43×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.76×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 20% ｜ P/C OI(近端) 99%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 20%）｜近端 Put 显著偏重（P/C OI 分位 99%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-21（3D）±0.6% ｜ 09-22（4D）±0.8% ｜ 09-23（5D）±0.9% ｜ 09-24（6D）±1.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,772,134,423 | GEX Change vs 上次快照 -1,002,410,288 | Flip: Primary Flip: 765.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 2559 / LOW 617 / INVALID 2088
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 765.35（全链重定价，覆盖 86%）
Call Wall 800（弱结构｜现价低于该位 5.1%）
最近结构参考: Flip 765（现价低于该位 0.8%）
量化视角： 负 Gamma（17.72亿，历史分位偏负区，比 80% 的交易日更负）｜负 Gamma 加深（10.02亿）｜现价位于 Flip 下方 0.76%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 765（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 765（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-21 770.0C — Vol 880 | 最新价 $0.09 | OI 3239→31504 (ΔOI +28265张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28265张（+872.6% vs前日OI），连续性待观察（方向未知）
09-25 772.0C — Vol 201 | 最新价 $0.71 | OI 2403→26482 (ΔOI +24079张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24079张（+1002.0% vs前日OI），连续性待观察（方向未知）
09-25 790.0C — Vol 18,237（Yahoo补） | 最新价 $0.05 | OI 11643→29665 (ΔOI +18022张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18022张（+154.8% vs前日OI），连续性待观察（方向未知）
10-16 724.0P — Vol 14 | 最新价 $2.55 | OI 12716→29473 (ΔOI +16757张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16757张（+131.8% vs前日OI），连续性待观察（方向未知）
09-30 736.0P — Vol 3 | 最新价 $1.20 | OI 750→16120 (ΔOI +15370张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15370张（+2049.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 102,493 张（Put 32,127 / Call 70,366），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 1086.8k / P 4088.7k，今日成交量: C 723.4k / P 1035.1k，平值价格ATM: C $0.76 / P $1.58 ｜ ATM IV 14.3%，预期波动 ±0.3%，Max Pain 765
Top ΔOI: C 750 -34,338 ｜ C 730 -29,746 ｜ C 755 -19,838

📆 Forward Expiration Structure

09-21  C +37.6k / P +32.6k ｜ Activity HIGH ｜ 3D
09-22  C +36.4k / P +9.9k ｜ Activity HIGH ｜ 4D
09-23  C +3.8k / P +7.9k ｜ Activity HIGH ｜ 5D
09-24  C +4.3k / P +15.4k ｜ Activity HIGH ｜ 6D

📆 09-21 Forward Structure
存量OI: C 117.1k / P 121.6k，今日变化ΔOI: C +37.6k / P +32.6k，平值价格ATM: C $1.82 / P $2.66 ｜ ATM IV 7.7%，净 delta 敞口 -1.3M shares
Top ΔOI: C 770 +28,265 ｜ P 745 +5,948 ｜ C 765 +3,425
仓位参考: Max Pain 760 ｜ Call Wall 770（+1.4%）（OI 31.5k） ｜ Put Wall 755（-0.6%）（OI 13.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 7.7%｜历史 Rank 60%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,286,079 股

📆 09-22 Forward Structure
存量OI: C 75.1k / P 48.4k，今日变化ΔOI: C +36.4k / P +9.9k，平值价格ATM: C $2.58 / P $3.35 ｜ ATM IV 9.0%，净 delta 敞口 -298k shares
Top ΔOI: C 789 +13,152 ｜ C 788 +11,539 ｜ C 772 +2,801
仓位参考: Max Pain 760 ｜ Call Wall 789（+3.9%，弱）（OI 13.2k） ｜ Put Wall 750（-1.3%，弱）（OI 6.9k）
量化解读： 存量 Call 重｜ATM IV 9.0%｜历史 Rank 60%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 297,701 股

📆 09-23 Forward Structure
存量OI: C 44.6k / P 39.0k，今日变化ΔOI: C +3.8k / P +7.9k，平值价格ATM: C $3.18 / P $3.90 ｜ ATM IV 9.7%，净 delta 敞口 -373k shares
Top ΔOI: P 762 +2,282 ｜ C 762 +1,090 ｜ C 778 +1,025
仓位参考: Max Pain 760 ｜ Call Wall 807（+6.3%，弱）（OI 5.4k） ｜ Put Wall 750（-1.3%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 9.7%｜历史 Rank 60%（近端代理）｜IV/RV 1.07×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 372,709 股

📆 09-24 Forward Structure
存量OI: C 33.5k / P 45.1k，今日变化ΔOI: C +4.3k / P +15.4k，平值价格ATM: C $3.88 / P $4.41 ｜ ATM IV 10.3%，净 delta 敞口 -412k shares
Top ΔOI: P 735 +2,415 ｜ P 739 -1,915
仓位参考: Max Pain 759 ｜ Call Wall 805（+6.0%，弱）（OI 2.4k） ｜ Put Wall 752（-1.0%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 10.3%｜历史 Rank 60%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 412,375 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SPY_morning.json