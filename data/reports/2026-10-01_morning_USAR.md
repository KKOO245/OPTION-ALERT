# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.36 ｜ QQQ $737.38
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 14.08 → 今开 14.09（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 14.20 ｜ 低 13.61

Options: P/C成交量 N/A | OI比 0.43 | ATM IV N/A | Skew N/A | Term N/A | ExpMove ±6.2%（近端） | Rank — (历史不足)
量化视角： 存量 OI 比 0.43——观察点，非方向信号
   ⇒ Put/Call Volume: 数据不足 → 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±6.2% ｜ 10-09（8D）±10.7% ｜ 10-16（15D）±13.7% ｜ 10-23（22D）±13.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: MIXED（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 0%（带内） ｜ IV 有效性: VALID 0 / LOW 0 / INVALID 404
结构观察区: NO_CROSS
Put Wall 15（弱结构｜现价低于该位 8.8%）
最近结构参考: Put Wall 15（现价低于该位 8.8%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 16（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 16.0C — Vol 8,423 | 最新价 $0.28 | OI 1546→6316 (ΔOI +4770张) | ΔOI/Volume 56.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4770张（+308.5% vs前日OI），连续性待观察（方向未知）
10-02 16.0C — Vol 1,060 | 最新价 $0.03 | OI 1665→2177 (ΔOI +512张) | ΔOI/Volume 48.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增512张（+30.8% vs前日OI），连续性待观察（方向未知）
10-02 15.0C — Vol 678 | 最新价 $0.07 | OI 1666→2049 (ΔOI +383张) | ΔOI/Volume 56.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增383张（+23.0% vs前日OI），连续性待观察（方向未知）
10-30 18.5C — Vol 363 | 最新价 $0.22 | OI 767→1125 (ΔOI +358张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增358张（+46.7% vs前日OI），连续性待观察（方向未知）
10-02 15.5C — Vol 674 | 最新价 $0.04 | OI 1347→1649 (ΔOI +302张) | ΔOI/Volume 44.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增302张（+22.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,325 张（Put 0 / Call 6,325），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.3k / P -0.5k ｜ Activity MEDIUM △ ｜ 1D
10-09  C +0.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 8D
10-16  C +5.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +0.1k / P -2 ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 26.7k / P 11.5k，今日变化ΔOI: C +1.3k / P -0.5k，平值价格ATM: C $0.80 / P $0.05 ｜ ATM IV 0.0%，净 delta 敞口 0 shares
Top ΔOI: P 16 -420 ｜ C 15 +383
仓位参考: Max Pain 16 ｜ Call Wall 15（+9.7%，弱）（OI 2.0k） ｜ Put Wall 14（+2.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜净 delta 敞口 正 0 股

10-09（MEDIUM △）Top ΔOI: 15C +214
10-09（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 15（+9.7%，弱）（OI 0.9k） ｜ Put Wall 14（+2.4%，弱）（OI 0.7k）

10-16（MEDIUM △）Top ΔOI: 16C +4,770 ｜ 14C +206
10-16（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15（+9.7%）（OI 5.6k）

10-23（Activity LOW）仓位参考: Max Pain 17 ｜ Put Wall 15（+9.7%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime MIXED（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/USAR_morning.json