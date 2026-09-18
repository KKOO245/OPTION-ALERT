# 期权晨报 2026-09-18（快照 10:20 ET）

📊 市场环境

SPY $758.97 ｜ QQQ $716.80
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
🟡 **近现价集中开仓**: 09-25 50C ΔOI +216（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 49C ΔOI +849 占该期限总 OI 10.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 49.38 → 今开 49.99（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 50.19 ｜ 低 47.94

Options: P/C成交量 1.91 | OI比 0.63 | ATM IV 61.0% | Skew -15.7pp | Term 0.97 | ExpMove ±7.2%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -15.7pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.63）+ 当日成交偏 Put（P/C量 1.91）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.91×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±7.2% ｜ 10-02（14D）±11.0% ｜ 10-09（21D）±5.6% ｜ 10-16（28D）±13.6%
   ⇒ IV–VIX Spread: +45.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,958,437 | GEX Change vs 上次快照 757,372 | Flip: Primary Flip: 51.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 235 / LOW 79 / INVALID 132
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 51.23（全链重定价，覆盖 84%）
Put Wall 45（弱结构｜现价高于该位 7.5%）
最近结构参考: Flip 51（现价低于该位 5.6%）
量化视角： 负 Gamma（796万，无历史分位）｜负 Gamma 缓解（+76万）｜现价位于 Flip 下方 5.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构）；上方 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 50.0C — Vol 1,401 | 最新价 $3.08 | OI 1187→2284 (ΔOI +1097张) | ΔOI/Volume 78.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1097张（+92.4% vs前日OI），连续性待观察（方向未知）
10-02 49.0C — Vol 903 | 最新价 $2.66 | OI 7→856 (ΔOI +849张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增849张（+12128.6% vs前日OI），连续性待观察（方向未知）
10-16 55.0C — Vol 1,014 | 最新价 $1.50 | OI 1807→2331 (ΔOI +524张) | ΔOI/Volume 51.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增524张（+29.0% vs前日OI），连续性待观察（方向未知）
09-25 55.0C — Vol 624 | 最新价 $0.35 | OI 481→856 (ΔOI +375张) | ΔOI/Volume 60.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增375张（+78.0% vs前日OI），连续性待观察（方向未知）
09-18 49.0P — Vol 315 | 最新价 $0.50 | OI 875→1140 (ΔOI +265张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增265张（+30.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,110 张（Put 265 / Call 2,845），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 53.6k / P 33.7k，今日成交量: C 3.0k / P 5.8k，平值价格ATM: C $1.21 / P $0.24 ｜ ATM IV 61.0%，预期波动 ±3.0%，Max Pain 50
Top ΔOI: P 55 -6,364 ｜ P 60 -927 ｜ C 55 -393

📆 Forward Expiration Structure

09-25  C +1.2k / P +0.5k ｜ Activity HIGH ｜ 7D
10-02  C +1.1k / P +0.2k ｜ Activity HIGH ｜ 14D
10-09  C +0.4k / P +0.2k ｜ Activity HIGH ｜ 21D
10-16  C +1.8k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 7.2k / P 7.3k，今日变化ΔOI: C +1.2k / P +0.5k，平值价格ATM: C $2.30 / P $1.16 ｜ ATM IV 57.0%，净 delta 敞口 33k shares
Top ΔOI: C 50 +216 ｜ P 47 +197
仓位参考: Max Pain 52 ｜ Call Wall 50（+3.4%，弱）（OI 0.4k） ｜ Put Wall 50（+3.4%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 57.0%｜历史 Rank 38%（近端代理）｜IV/RV 1.63×（近似）｜净 delta 敞口 正 32,547 股

📆 10-02 Forward Structure
存量OI: C 4.5k / P 3.6k，今日变化ΔOI: C +1.1k / P +0.2k，平值价格ATM: C $2.81 / P $2.49 ｜ ATM IV 53.9%，净 delta 敞口 49k shares
Top ΔOI: C 49 +849 ｜ P 48 +161 ｜ P 46 +114
仓位参考: Max Pain 52 ｜ Call Wall 49（+1.3%，弱）（OI 0.9k） ｜ Put Wall 50（+3.4%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 53.9%｜历史 Rank 38%（近端代理）｜IV/RV 1.54×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 49,373 股

📆 10-09 Forward Structure
存量OI: C 2.8k / P 2.0k，今日变化ΔOI: C +0.4k / P +0.2k，平值价格ATM: C $0.00 / P $2.70 ｜ ATM IV 57.8%，净 delta 敞口 -2k shares
Top ΔOI: P 49 +97 ｜ P 52 +42
仓位参考: Max Pain 52 ｜ Put Wall 47（-2.8%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 57.8%｜历史 Rank 38%（近端代理）｜IV/RV 1.65×（近似）｜净 delta 敞口 负 1,962 股

📆 10-16 Forward Structure
存量OI: C 12.0k / P 10.1k，今日变化ΔOI: C +1.8k / P +0.5k，平值价格ATM: C $3.08 / P $3.50 ｜ ATM IV 59.4%，净 delta 敞口 61k shares
Top ΔOI: C 50 +1,097 ｜ C 55 +524 ｜ P 50 +261
仓位参考: Max Pain 55 ｜ Call Wall 50（+3.4%，弱）（OI 2.3k） ｜ Put Wall 45（-7.0%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 59.4%｜历史 Rank 38%（近端代理）｜IV/RV 1.70×（近似）｜净 delta 敞口 正 61,003 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=24 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=24）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/MP_morning.json