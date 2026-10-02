# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $753.79
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 165C ΔOI +2,577（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 160.50 → 今开 165.85（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 170.17 ｜ 低 163.10

Options: P/C成交量 0.27 | OI比 0.79 | ATM IV 100.2% | Skew -0.9pp | Term 0.66 | ExpMove ±7.1%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±7.1% ｜ 10-16（14D）±10.3% ｜ 10-23（21D）±12.5% ｜ 10-30（28D）±14.8%
   ⇒ IV–VIX Spread: +84.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 122,015,444 | GEX Change vs 上次快照 23,690,107 | Flip: Primary Flip: 149.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 691 / LOW 148 / INVALID 211
结构观察区: Primary Flip 149.06（全链重定价，覆盖 99%）
Call Wall 165（弱结构｜现价高于该位 0.7%）
最近结构参考: Call Wall 165（现价高于该位 0.7%）
量化视角： 正 Gamma（1.22亿，无历史分位）｜正 Gamma 增强（+2369万）｜现价位于 Flip 上方 11.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考） / 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 172.5C — Vol 7,426 | 最新价 $5.97 | OI 77→5753 (ΔOI +5676张) | ΔOI/Volume 76.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5676张（+7371.4% vs前日OI），连续性待观察（方向未知）
10-02 167.5C — Vol 17,053 | 最新价 $0.71 | OI 19772→23569 (ΔOI +3797张) | ΔOI/Volume 22.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3797张（+19.2% vs前日OI），连续性待观察（方向未知）
10-23 85.0P — Vol 2,791 | 最新价 $0.11 | OI 112→2694 (ΔOI +2582张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2582张（+2305.4% vs前日OI），连续性待观察（方向未知）
10-09 165.0C — Vol 5,324 | 最新价 $4.37 | OI 5508→8085 (ΔOI +2577张) | ΔOI/Volume 48.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2577张（+46.8% vs前日OI），连续性待观察（方向未知）
10-09 172.5C — Vol 3,004 | 最新价 $2.46 | OI 2435→4518 (ΔOI +2083张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2083张（+85.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,715 张（Put 2,582 / Call 14,133），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 241.7k / P 190.1k，今日成交量: C 100.2k / P 27.3k，平值价格ATM: C $2.42 / P $1.29 ｜ ATM IV 100.2%，预期波动 ±2.2%，Max Pain 152
Top ΔOI: C 170 -7,771 ｜ C 167 +3,797 ｜ C 172 -3,304

📆 Forward Expiration Structure

10-09  C +13.4k / P +9.6k ｜ Activity HIGH ｜ 7D
10-16  C +4.0k / P +7.9k ｜ Activity HIGH ｜ 14D
10-23  C +5.9k / P +5.1k ｜ Activity HIGH ｜ 21D
10-30  C +0.6k / P +2.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 65.1k / P 73.9k，今日变化ΔOI: C +13.4k / P +9.6k，平值价格ATM: C $6.67 / P $5.20 ｜ ATM IV 63.4%，净 delta 敞口 366k shares
Top ΔOI: C 165 +2,577 ｜ C 172 +2,083 ｜ C 207 +1,991
仓位参考: Max Pain 150 ｜ Call Wall 165（-0.7%，弱）（OI 8.1k） ｜ Put Wall 155（-6.7%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.4%｜历史 Rank 80%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 365,694 股

📆 10-16 Forward Structure
存量OI: C 179.3k / P 153.7k，今日变化ΔOI: C +4.0k / P +7.9k，平值价格ATM: C $9.22 / P $7.85 ｜ ATM IV 64.1%，净 delta 敞口 176k shares
Top ΔOI: C 200 -2,556 ｜ C 172 +1,788 ｜ P 150 +1,698
仓位参考: Max Pain 125 ｜ Call Wall 155（-6.7%，弱）（OI 10.4k） ｜ Put Wall 150（-9.8%，弱）（OI 6.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.1%｜历史 Rank 80%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 175,626 股

📆 10-23 Forward Structure
存量OI: C 26.6k / P 32.3k，今日变化ΔOI: C +5.9k / P +5.1k，平值价格ATM: C $11.35 / P $9.40 ｜ ATM IV 64.4%，净 delta 敞口 223k shares
Top ΔOI: C 172 +5,676
仓位参考: Max Pain 160 ｜ Call Wall 172.5（+3.8%）（OI 5.8k） ｜ Put Wall 155（-6.7%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.4%｜历史 Rank 80%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 223,408 股

10-30（MEDIUM △）Top ΔOI: 155P +281
10-30（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 180（+8.3%，弱）（OI 1.1k） ｜ Put Wall 160（-3.7%，弱）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/MSTR_morning.json