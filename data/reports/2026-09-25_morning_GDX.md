# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $771.10 ｜ QQQ $744.50
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 95C ΔOI +3,407（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 92.35 → 今开 92.44（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 92.61 ｜ 低 91.34

Options: P/C成交量 1.39 | OI比 0.57 | ATM IV 47.1% | Skew -5.9pp | Term 0.88 | ExpMove ±4.6%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.9pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.57）+ 当日成交偏 Put（P/C量 1.39）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.39×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±4.6% ｜ 10-09（14D）±6.4% ｜ 10-16（21D）±7.8% ｜ 10-23（28D）±9.4%
   ⇒ IV–VIX Spread: +31.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,335,348 | GEX Change vs 上次快照 4,741,796 | Flip: Primary Flip: 93.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 498 / LOW 137 / INVALID 227
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 93.33（全链重定价，覆盖 83%）
Put Wall 90（弱结构｜现价高于该位 2.2%）
最近结构参考: Flip 93（现价低于该位 1.5%）
量化视角： 负 Gamma（1634万，无历史分位）｜负 Gamma 缓解（+474万）｜现价位于 Flip 下方 1.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 93（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 93（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 95.0C — Vol 3,658 | 最新价 $1.09 | OI 1549→4956 (ΔOI +3407张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3407张（+219.9% vs前日OI），连续性待观察（方向未知）
10-02 86.0P — Vol 3,220 | 最新价 $0.37 | OI 137→3243 (ΔOI +3106张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3106张（+2267.2% vs前日OI），连续性待观察（方向未知）
10-16 80.0P — Vol 2,565 | 最新价 $0.39 | OI 6295→8820 (ΔOI +2525张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2525张（+40.1% vs前日OI），连续性待观察（方向未知）
09-25 96.0C — Vol 3,065 | 最新价 $0.05 | OI 4771→6642 (ΔOI +1871张) | ΔOI/Volume 61.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1871张（+39.2% vs前日OI），连续性待观察（方向未知）
10-16 100.0C — Vol 2,526 | 最新价 $1.31 | OI 11166→12738 (ΔOI +1572张) | ΔOI/Volume 62.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1572张（+14.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,481 张（Put 5,631 / Call 6,850），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 100.7k / P 57.7k，今日成交量: C 1.2k / P 1.7k，平值价格ATM: C $0.33 / P $0.63 ｜ ATM IV 47.1%，预期波动 ±1.0%，Max Pain 93
Top ΔOI: C 97 -14,932 ｜ C 100 -12,811 ｜ P 86 -3,296

📆 Forward Expiration Structure

10-02  C +5.9k / P +3.8k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +2.9k / P +3.4k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.2k / P +0.1k ｜ Activity LOW ｜ 28D

📆 10-02 Forward Structure
存量OI: C 39.2k / P 43.2k，今日变化ΔOI: C +5.9k / P +3.8k，平值价格ATM: C $2.08 / P $2.14 ｜ ATM IV 39.9%，净 delta 敞口 120k shares
Top ΔOI: C 95 +3,407 ｜ P 86 +3,106 ｜ C 92 +957
仓位参考: Max Pain 97 ｜ Call Wall 95（+3.3%，弱）（OI 5.0k） ｜ Put Wall 97（+5.5%，弱）（OI 8.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.9%｜历史 Rank 76%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 120,180 股

10-09（MEDIUM △）Top ΔOI: 90P +122 ｜ 85P +97
10-09（MEDIUM △）仓位参考: Max Pain 94 ｜ Call Wall 94（+2.2%，弱）（OI 0.7k） ｜ Put Wall 90（-2.1%，弱）（OI 2.0k）

10-16（MEDIUM △）Top ΔOI: 80P +2,525 ｜ 100C +1,572
10-16（MEDIUM △）仓位参考: Max Pain 93 ｜ Call Wall 95（+3.3%，弱）（OI 6.0k） ｜ Put Wall 90（-2.1%，弱）（OI 10.0k）

10-23（Activity LOW）仓位参考: Max Pain 95 ｜ Call Wall 96.5（+5.0%，弱）（OI 0.8k） ｜ Put Wall 93（+1.2%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/GDX_morning.json