# 期权晨报 2026-09-18（快照 10:20 ET）

📊 市场环境

SPY $758.97 ｜ QQQ $716.78
VIX 15.53 ↑0.6%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 16P ΔOI +200（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 18C ΔOI +1,856 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.63 → 今开 15.90（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 16.08 ｜ 低 15.21

Options: P/C成交量 0.36 | OI比 0.36 | ATM IV 74.7% | Skew -10.2pp | Term 1.00 | ExpMove ±8.2%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -10.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.36）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.36×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±8.2% ｜ 10-02（14D）±11.6% ｜ 10-09（21D）±14.4% ｜ 10-16（28D）±16.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,174,515 | GEX Change vs 上次快照 -1,495,816 | Flip: Primary Flip: 15.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 232 / LOW 94 / INVALID 142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.80（全链重定价，覆盖 90%）
Put Wall 15（弱结构｜现价高于该位 2.5%）
最近结构参考: Put Wall 15（现价高于该位 2.5%）
量化视角： 负 Gamma（717万，无历史分位）｜负 Gamma 加深（150万）｜现价位于 Flip 下方 2.71%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 18.5C — Vol 1,924 | 最新价 $0.19 | OI 89→1945 (ΔOI +1856张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1856张（+2085.4% vs前日OI），连续性待观察（方向未知）
10-16 20.0C — Vol 1,493 | 最新价 $0.25 | OI 1950→2855 (ΔOI +905张) | ΔOI/Volume 60.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增905张（+46.4% vs前日OI），连续性待观察（方向未知）
09-25 18.0C — Vol 978 | 最新价 $0.11 | OI 1623→2392 (ΔOI +769张) | ΔOI/Volume 78.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增769张（+47.4% vs前日OI），连续性待观察（方向未知）
10-02 19.0C — Vol 615 | 最新价 $0.12 | OI 346→864 (ΔOI +518张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增518张（+149.7% vs前日OI），连续性待观察（方向未知）
09-25 19.0C — Vol 649 | 最新价 $0.05 | OI 730→1203 (ΔOI +473张) | ΔOI/Volume 72.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增473张（+64.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,521 张（Put 0 / Call 4,521），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 123.6k / P 44.6k，今日成交量: C 8.4k / P 3.0k，平值价格ATM: C $0.34 / P $0.17 ｜ ATM IV 74.7%，预期波动 ±3.3%，Max Pain 16
Top ΔOI: P 20 -6,107 ｜ P 18 -3,106 ｜ P 25 -3,008

📆 Forward Expiration Structure

09-25  C +2.1k / P +0.3k ｜ Activity HIGH ｜ 7D
10-02  C +2.5k / P +0.3k ｜ Activity HIGH ｜ 14D
10-09  C +77 / P -0.1k ｜ Activity MEDIUM △ ｜ 21D
10-16  C +1.2k / P +0.4k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 18.2k / P 7.9k，今日变化ΔOI: C +2.1k / P +0.3k，平值价格ATM: C $0.72 / P $0.54 ｜ ATM IV 69.2%，净 delta 敞口 24k shares
仓位参考: Max Pain 16 ｜ Call Wall 16.5（+7.3%，弱）（OI 1.4k） ｜ Put Wall 16.5（+7.3%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 69.2%｜历史 Rank 3%（近端代理）｜IV/RV 1.54×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 24,254 股

📆 10-02 Forward Structure
存量OI: C 12.4k / P 4.8k，今日变化ΔOI: C +2.5k / P +0.3k，平值价格ATM: C $1.00 / P $0.78 ｜ ATM IV 67.5%，净 delta 敞口 27k shares
Top ΔOI: P 16 +200
仓位参考: Max Pain 17 ｜ Put Wall 16（+4.1%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 67.5%｜历史 Rank 3%（近端代理）｜IV/RV 1.50×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 26,586 股

10-09（MEDIUM △）Top ΔOI: 15P +65
10-09（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 16（+4.1%）（OI 1.2k）

📆 10-16 Forward Structure
存量OI: C 30.8k / P 11.8k，今日变化ΔOI: C +1.2k / P +0.4k，平值价格ATM: C $1.69 / P $0.90 ｜ ATM IV 74.9%，净 delta 敞口 7k shares
Top ΔOI: P 19 +185
仓位参考: Max Pain 17 ｜ Put Wall 15（-2.4%）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 74.9%｜历史 Rank 3%（近端代理）｜IV/RV 1.67×（近似）｜净 delta 敞口 正 6,723 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/USAR_morning.json