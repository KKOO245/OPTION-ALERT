# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $692.49 ｜ QQQ $608.45
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-23 130P ΔOI +721（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 138.43 → 今开 131.93（-4.7%） | 较昨收变动（含盘初走势） ｜ 今日高 133.84 ｜ 低 129.52

Options: P/C成交量 0.75 | OI比 0.79 | ATM IV 66.7% | Skew -43.9pp | Term 0.89 | ExpMove ±5.0%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -43.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±5.0% ｜ 11-25（5D）±6.8% ｜ 11-27（7D）±7.1% ｜ 12-04（14D）±9.9%
   ⇒ IV–VIX Spread: +39.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -139,327,219 | GEX Change vs 上次快照 -88,705,802 | Flip: Primary Flip: 133.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 614 / LOW 222 / INVALID 77
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 133.20（全链重定价，覆盖 100%）
Put Wall 140（弱结构｜现价低于该位 7.0%）
最近结构参考: Flip 133（现价低于该位 2.2%）
量化视角： 负 Gamma（1.39亿，无历史分位）｜负 Gamma 加深（8871万）｜现价位于 Flip 下方 2.24%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 140（Put Wall，弱结构） / 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 130.0P — Vol 10,838 | 最新价 $5.40 | OI 24685→27684 (ΔOI +2999张) | ΔOI/Volume 27.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2999张（+12.2% vs前日OI），连续性待观察（方向未知）
11-20 144.0P — Vol 10,501 | 最新价 $5.75 | OI 2076→5017 (ΔOI +2941张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2941张（+141.7% vs前日OI），连续性待观察（方向未知）
11-23 140.0C — Vol 3,707 | 最新价 $2.62 | OI 481→2224 (ΔOI +1743张) | ΔOI/Volume 47.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1743张（+362.4% vs前日OI），连续性待观察（方向未知）
12-18 125.0P — Vol 5,686 | 最新价 $4.00 | OI 27569→29304 (ΔOI +1735张) | ΔOI/Volume 30.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1735张（+6.3% vs前日OI），连续性待观察（方向未知）
11-27 85.0P — Vol 1,706 | 最新价 $0.04 | OI 3593→5264 (ΔOI +1671张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1671张（+46.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,089 张（Put 9,346 / Call 1,743），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 548.9k / P 432.8k，今日成交量: C 56.7k / P 42.4k，平值价格ATM: C $3.02 / P $0.58 ｜ ATM IV 66.7%，预期波动 ±2.8%，Max Pain 141
Top ΔOI: P 155 -6,657 ｜ P 160 -5,020 ｜ C 150 -3,914

📆 Forward Expiration Structure

11-23  C +7.4k / P +4.0k ｜ Activity HIGH ｜ 3D
11-25  C +4.3k / P +3.6k ｜ Activity HIGH ｜ 5D
11-27  C +6.0k / P +7.0k ｜ Activity MEDIUM △ ｜ 7D
12-04  C +2.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 14D

📆 11-23 Forward Structure
存量OI: C 20.5k / P 13.6k，今日变化ΔOI: C +7.4k / P +4.0k，平值价格ATM: C $4.80 / P $1.74 ｜ ATM IV 58.4%，净 delta 敞口 -216k shares
Top ΔOI: C 140 +1,743 ｜ P 130 +721
仓位参考: Max Pain 140 ｜ Call Wall 140（+7.5%，弱）（OI 2.2k） ｜ Put Wall 126（-3.2%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 58.4%｜历史 Rank 68%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 215,956 股

📆 11-25 Forward Structure
存量OI: C 9.9k / P 7.6k，今日变化ΔOI: C +4.3k / P +3.6k，平值价格ATM: C $6.00 / P $2.85 ｜ ATM IV 65.2%，净 delta 敞口 -181k shares
Top ΔOI: C 146 +1,311 ｜ P 137 +494
仓位参考: Max Pain 140 ｜ Call Wall 143（+9.8%，弱）（OI 0.5k） ｜ Put Wall 130（-0.2%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 65.2%｜历史 Rank 68%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 180,825 股

11-27（MEDIUM △）Top ΔOI: 139C +1,259 ｜ 125P +997
11-27（MEDIUM △）仓位参考: Max Pain 140 ｜ Put Wall 120（-7.8%，弱）（OI 5.6k）

12-04（MEDIUM △）Top ΔOI: 150C +1,649 ｜ 140C +237
12-04（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 140（+7.5%，弱）（OI 5.2k） ｜ Put Wall 140（+7.5%）（OI 11.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/SPCX_morning.json