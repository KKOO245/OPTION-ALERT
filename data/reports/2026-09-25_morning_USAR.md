# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.42
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.38 → 今开 15.41（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 15.41 ｜ 低 15.02

Options: P/C成交量 0.44 | OI比 0.52 | ATM IV 91.5% | Skew 26.8pp | Term 0.73 | ExpMove ±8.4%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 26.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±8.4% ｜ 10-09（14D）±10.3% ｜ 10-16（21D）±12.8% ｜ 10-23（28D）±16.0%
   ⇒ IV–VIX Spread: +75.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,101,566 | GEX Change vs 上次快照 2,939,670 | Flip: Primary Flip: 15.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 190 / LOW 68 / INVALID 184
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.63（全链重定价，覆盖 86%）
Put Wall 15（现价高于该位 0.6%）
最近结构参考: Put Wall 15（现价高于该位 0.6%）
量化视角： 负 Gamma（310万，无历史分位）｜负 Gamma 缓解（+294万）｜现价位于 Flip 下方 3.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 16.5P — Vol 1,103 | 最新价 $1.34 | OI 438→1483 (ΔOI +1045张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1045张（+238.6% vs前日OI），连续性待观察（方向未知）
09-25 15.0P — Vol 1,137 | 最新价 $0.08 | OI 1880→2787 (ΔOI +907张) | ΔOI/Volume 79.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增907张（+48.2% vs前日OI），连续性待观察（方向未知）
10-16 18.5C — Vol 567 | 最新价 $0.23 | OI 56→597 (ΔOI +541张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增541张（+966.1% vs前日OI），连续性待观察（方向未知）
10-02 16.0C — Vol 603 | 最新价 $0.36 | OI 400→797 (ΔOI +397张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增397张（+99.2% vs前日OI），连续性待观察（方向未知）
09-25 15.5C — Vol 1,019 | 最新价 $0.20 | OI 352→721 (ΔOI +369张) | ΔOI/Volume 36.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增369张（+104.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,259 张（Put 1,952 / Call 1,307），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 30.4k / P 15.7k，今日成交量: C 0.5k / P 0.2k，平值价格ATM: C $0.26 / P $0.07 ｜ ATM IV 91.5%，预期波动 ±2.2%，Max Pain 16
Top ΔOI: P 15 +907 ｜ P 16 -508 ｜ C 15 +369

📆 Forward Expiration Structure

10-02  C +0.9k / P +1.6k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +28 / P +0.5k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +1.1k / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 20.1k / P 10.7k，今日变化ΔOI: C +0.9k / P +1.6k，平值价格ATM: C $0.82 / P $0.45 ｜ ATM IV 62.1%，净 delta 敞口 -78k shares
Top ΔOI: P 16 +1,045 ｜ C 16 +397 ｜ C 16 +320
仓位参考: Max Pain 17 ｜ Put Wall 16（+6.0%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.1%｜历史 Rank 16%（近端代理）｜IV/RV 1.12×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 78,258 股

10-09（MEDIUM △）Top ΔOI: 17P +293 ｜ 16P +131
10-09（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 16（+6.0%）（OI 1.3k）

10-16（MEDIUM △）Top ΔOI: 15P +253
10-16（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 15（-0.6%）（OI 5.6k）

10-23（MEDIUM △）Top ΔOI: 14P +129
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（-0.6%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/USAR_morning.json