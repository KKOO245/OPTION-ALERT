# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.74 ｜ QQQ $721.45
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
🟡 **近现价集中开仓**: 09-21 59P ΔOI +2,301（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-23 55P ΔOI +2,897 占该期限总 OI 14.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 58.97 → 今开 60.08（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 60.11 ｜ 低 59.58

Options: P/C成交量 0.68 | OI比 0.41 | ATM IV 41.9% | Skew -0.1pp | Term 0.89 | ExpMove ±1.8%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-21（3D）±1.8% ｜ 09-23（5D）±3.4% ｜ 09-25（7D）±4.0% ｜ 09-28（10D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 191,588,727 | GEX Change vs 上次快照 88,937,333 | Flip: Primary Flip: 56.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 879 / LOW 245 / INVALID 392
结构观察区: Primary Flip 56.63（全链重定价，覆盖 88%）
最近结构参考: Flip 57（现价高于该位 5.5%）
量化视角： 正 Gamma（1.92亿，无历史分位）｜正 Gamma 增强（+8894万）｜现价位于 Flip 上方 5.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 56（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 56.0P — Vol 79 | 最新价 $0.96 | OI 2178→8570 (ΔOI +6392张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6392张（+293.5% vs前日OI），连续性待观察（方向未知）
10-16 60.0C — Vol 483 | 最新价 $2.62 | OI 44636→49669 (ΔOI +5033张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增5033张（+11.3% vs前日OI），值得跟踪（方向未知）
10-16 66.0C — Vol 3 | 最新价 $0.86 | OI 3118→7362 (ΔOI +4244张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4244张（+136.1% vs前日OI），连续性待观察（方向未知）
10-02 67.0C — Vol 95 | 最新价 $0.26 | OI 143→4247 (ΔOI +4104张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4104张（+2869.9% vs前日OI），连续性待观察（方向未知）
10-16 68.0C — Vol 16 | 最新价 $0.60 | OI 2265→6280 (ΔOI +4015张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4015张（+177.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,788 张（Put 6,392 / Call 17,396），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 983.5k / P 406.8k，今日成交量: C 17.0k / P 11.5k，平值价格ATM: C $0.40 / P $0.16 ｜ ATM IV 41.9%，预期波动 ±0.9%，Max Pain 56
Top ΔOI: P 70 -18,224 ｜ P 65 -9,590 ｜ P 59 +2,826

📆 Forward Expiration Structure

09-21  C +6.4k / P +3.6k ｜ Activity HIGH ｜ 3D
09-23  C +4.3k / P +5.1k ｜ Activity HIGH ｜ 5D
09-25  C +5.5k / P +5.6k ｜ Activity MEDIUM △ ｜ 7D
09-28  C +0.8k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 09-21 Forward Structure
存量OI: C 17.3k / P 12.5k，今日变化ΔOI: C +6.4k / P +3.6k，平值价格ATM: C $0.64 / P $0.44 ｜ ATM IV 25.4%，净 delta 敞口 -14k shares
Top ΔOI: P 59 +2,301
仓位参考: Max Pain 58 ｜ Call Wall 57（-4.6%，弱）（OI 3.3k） ｜ Put Wall 59（-1.3%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 25.4%｜历史 Rank 69%（近端代理）｜IV/RV 0.70×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 14,241 股

📆 09-23 Forward Structure
存量OI: C 7.9k / P 12.6k，今日变化ΔOI: C +4.3k / P +5.1k，平值价格ATM: C $1.21 / P $0.82 ｜ ATM IV 32.1%，净 delta 敞口 37k shares
Top ΔOI: P 55 +2,897 ｜ C 65 +1,962 ｜ P 56 +1,469
仓位参考: Max Pain 59 ｜ Call Wall 65（+8.8%）（OI 2.0k） ｜ Put Wall 55（-7.9%）（OI 4.4k）
量化解读： 存量 Put 重｜ATM IV 32.1%｜历史 Rank 69%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,620 股

09-25（MEDIUM △）Top ΔOI: 55P +1,424 ｜ 57P +1,266
09-25（MEDIUM △）仓位参考: Max Pain 60 ｜ Put Wall 55（-7.9%，弱）（OI 5.5k）

📆 09-28 Forward Structure
存量OI: C 1.9k / P 1.4k，今日变化ΔOI: C +0.8k / P +0.4k，平值价格ATM: C $1.37 / P $1.13 ｜ ATM IV 31.7%，净 delta 敞口 12k shares
Top ΔOI: C 59 +201 ｜ C 64 +125 ｜ C 62 +95
仓位参考: Max Pain 59 ｜ Call Wall 61（+2.1%，弱）（OI 0.3k） ｜ Put Wall 58（-2.9%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 31.7%｜历史 Rank 69%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 11,976 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SLV_morning.json