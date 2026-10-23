# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $760.80 ｜ QQQ $704.40
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-26 750P ΔOI +82,662（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 750P ΔOI +82,662 占该期限总 OI 20.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 763.96 → 今开 759.90（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 761.32 ｜ 低 758.84

Options: P/C成交量 1.13 | OI比 1.41 | ATM IV 23.9% | Skew 1.8pp | Term 0.65 | ExpMove ±1.0%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.13×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 16% ｜ P/C OI(近端) 17%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 16%）｜近端持仓结构中性（P/C OI 分位 17%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-26（3D）±1.0% ｜ 10-27（4D）±1.2% ｜ 10-28（5D）±1.5% ｜ 10-29（6D）±1.8%
   ⇒ IV–VIX Spread: +4.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,947,972,670 | GEX Change vs 上次快照 -288,638,561 | Flip: Primary Flip: 772.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3277 / LOW 317 / INVALID 1412
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 772.93（全链重定价，覆盖 96%）
最近结构参考: Flip 773（现价低于该位 1.6%）
量化视角： 负 Gamma（19.48亿，历史分位偏负区，比 84% 的交易日更负）｜负 Gamma 加深（2.89亿）｜现价位于 Flip 下方 1.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 766（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-26 750.0P — Vol 103,663 | 最新价 $0.79 | OI 4146→86808 (ΔOI +82662张) | ΔOI/Volume 79.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增82662张（+1993.8% vs前日OI），连续性待观察（方向未知）
10-26 755.0P — Vol 87,025 | 最新价 $1.44 | OI 2945→84931 (ΔOI +81986张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81986张（+2783.9% vs前日OI），连续性待观察（方向未知）
10-30 735.0P — Vol 27,142 | 最新价 $1.30 | OI 53118→74772 (ΔOI +21654张) | ΔOI/Volume 79.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21654张（+40.8% vs前日OI），连续性待观察（方向未知）
10-28 741.0P — Vol 22,309 | 最新价 $0.97 | OI 237→20252 (ΔOI +20015张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20015张（+8445.1% vs前日OI），连续性待观察（方向未知）
11-20 726.0P — Vol 33,616 | 最新价 $4.04 | OI 14318→27860 (ΔOI +13542张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13542张（+94.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 219,859 张（Put 219,859 / Call 0），跨 4 个期限｜近端保护（5 档，距现价 ≤5%，权利金合计约 $20M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 435.8k / P 612.9k，今日成交量: C 463.7k / P 525.1k，平值价格ATM: C $1.75 / P $2.17 ｜ ATM IV 23.9%，预期波动 ±0.5%，Max Pain 766
Top ΔOI: C 767 +10,326 ｜ C 770 +9,802 ｜ P 755 +9,632

📆 Forward Expiration Structure

10-26  C +27.1k / P +170.6k ｜ Activity HIGH ｜ 3D
10-27  C +9.5k / P +11.7k ｜ Activity HIGH ｜ 4D
10-28  C +10.2k / P +26.6k ｜ Activity HIGH ｜ 5D
10-29  C +10.5k / P +8.9k ｜ Activity HIGH ｜ 6D

📆 10-26 Forward Structure
存量OI: C 102.5k / P 298.1k，今日变化ΔOI: C +27.1k / P +170.6k，平值价格ATM: C $3.48 / P $3.83 ｜ ATM IV 12.7%，净 delta 敞口 -2.4M shares
Top ΔOI: P 750 +82,662 ｜ P 755 +81,986 ｜ P 766 -7,921
仓位参考: Max Pain 766 ｜ Call Wall 780（+2.5%，弱）（OI 5.3k） ｜ Put Wall 750（-1.4%，弱）（OI 86.8k）
量化解读： 存量 Put 重｜ATM IV 12.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.37×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,439,954 股

📆 10-27 Forward Structure
存量OI: C 60.3k / P 115.1k，今日变化ΔOI: C +9.5k / P +11.7k，平值价格ATM: C $4.42 / P $4.62 ｜ ATM IV 13.8%，净 delta 敞口 383k shares
Top ΔOI: P 767 -7,824 ｜ P 750 +4,686 ｜ P 762 +4,388
仓位参考: Max Pain 767 ｜ Call Wall 780（+2.5%，弱）（OI 2.5k） ｜ Put Wall 767（+0.8%）（OI 29.4k）
量化解读： 存量 Put 重｜ATM IV 13.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.49×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 382,671 股

📆 10-28 Forward Structure
存量OI: C 47.9k / P 85.6k，今日变化ΔOI: C +10.2k / P +26.6k，平值价格ATM: C $5.63 / P $5.62 ｜ ATM IV 15.6%，净 delta 敞口 -268k shares
Top ΔOI: P 741 +20,015 ｜ P 765 +1,051 ｜ C 781 +716
仓位参考: Max Pain 769 ｜ Call Wall 772（+1.5%，弱）（OI 2.1k） ｜ Put Wall 741（-2.6%）（OI 20.3k）
量化解读： 存量 Put 重｜ATM IV 15.6%｜历史 Rank 93%（近端代理）｜IV/RV 1.68×（近似）｜净 delta 敞口 负 268,383 股

📆 10-29 Forward Structure
存量OI: C 34.5k / P 39.3k，今日变化ΔOI: C +10.5k / P +8.9k，平值价格ATM: C $6.51 / P $6.78 ｜ ATM IV 16.3%，净 delta 敞口 -5k shares
Top ΔOI: C 789 +1,149 ｜ C 763 +1,121 ｜ C 780 +963
仓位参考: Max Pain 767 ｜ Call Wall 780（+2.5%，弱）（OI 1.5k） ｜ Put Wall 744（-2.2%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.3%｜历史 Rank 93%（近端代理）｜IV/RV 1.76×（近似）｜净 delta 敞口 负 4,630 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SPY_morning.json