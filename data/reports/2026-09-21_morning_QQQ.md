# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $767.46 ｜ QQQ $734.21
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 32.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-22 731C ΔOI +3,845（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 721.45 → 今开 727.95（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 733.81 ｜ 低 727.82

Options: P/C成交量 0.99 | OI比 1.81 | ATM IV 15.7% | Skew 2.7pp | Term 1.12 | ExpMove ±0.7%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 1.12）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.81×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 97% ｜ P/C OI(近端) 64%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 97%）｜近端持仓结构中性（P/C OI 分位 64%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-22（1D）±0.7% ｜ 09-23（2D）±0.9% ｜ 09-24（3D）±1.2% ｜ 09-25（4D）±1.4%
   ⇒ IV–VIX Spread: +0.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 846,575,827 | GEX Change vs 上次快照 670,656,088 | Flip: Primary Flip: 719.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3104 / LOW 340 / INVALID 1812
结构观察区: Primary Flip 719.56（全链重定价，覆盖 99%）
Call Wall 725（弱结构｜现价高于该位 1.0%）
最近结构参考: Call Wall 725（现价高于该位 1.0%）
量化视角： 正 Gamma（8.47亿，历史分位偏正区，比 97% 的交易日更正）｜正 Gamma 增强（+6.71亿）｜现价位于 Flip 上方 1.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 719（MaxPain，仅结算参考） / 725（Call Wall，弱结构）。
• Gamma 区域：切换参考 720（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 705.0P — Vol 33,631 | 最新价 $1.34 | OI 3066→32706 (ΔOI +29640张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29640张（+966.7% vs前日OI），连续性待观察（方向未知）
09-21 730.0C — Vol 34,123 | 最新价 $0.29 | OI 2549→30242 (ΔOI +27693张) | ΔOI/Volume 81.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27693张（+1086.4% vs前日OI），连续性待观察（方向未知）
10-02 725.0C — Vol 26,098 | 最新价 $7.55 | OI 11487→34735 (ΔOI +23248张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23248张（+202.4% vs前日OI），连续性待观察（方向未知）
10-16 695.0P — Vol 19,127 | 最新价 $5.15 | OI 24205→37683 (ΔOI +13478张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13478张（+55.7% vs前日OI），连续性待观察（方向未知）
10-16 705.0P — Vol 20,362 | 最新价 $7.01 | OI 30645→43833 (ΔOI +13188张) | ΔOI/Volume 64.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13188张（+43.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 107,247 张（Put 56,306 / Call 50,941），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $20M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 140.9k / P 255.1k，今日成交量: C 488.2k / P 484.6k，平值价格ATM: C $1.04 / P $1.48 ｜ ATM IV 15.7%，预期波动 ±0.3%，Max Pain 719
Top ΔOI: C 730 +27,693 ｜ C 725 +11,992 ｜ P 717 +8,794

📆 Forward Expiration Structure

09-22  C +21.0k / P +23.5k ｜ Activity HIGH ｜ 1D
09-23  C +21.7k / P +12.3k ｜ Activity HIGH ｜ 2D
09-24  C +10.2k / P +4.6k ｜ Activity HIGH ｜ 3D
09-25  C +28.8k / P +46.8k ｜ Activity HIGH ｜ 4D

📆 09-22 Forward Structure
存量OI: C 60.5k / P 64.0k，今日变化ΔOI: C +21.0k / P +23.5k，平值价格ATM: C $2.33 / P $2.72 ｜ ATM IV 14.6%，净 delta 敞口 1.3M shares
Top ΔOI: C 731 +3,845 ｜ C 732 +2,703 ｜ C 730 +2,235
仓位参考: Max Pain 718 ｜ Call Wall 731（-0.2%，弱）（OI 4.8k） ｜ Put Wall 715（-2.4%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜ATM IV 14.6%｜历史 Rank 33%（近端代理）｜IV/RV 1.24×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,314,062 股

📆 09-23 Forward Structure
存量OI: C 45.5k / P 49.2k，今日变化ΔOI: C +21.7k / P +12.3k，平值价格ATM: C $3.29 / P $3.64 ｜ ATM IV 14.9%，净 delta 敞口 1.4M shares
Top ΔOI: C 720 +8,604 ｜ P 699 +2,528 ｜ P 696 +2,418
仓位参考: Max Pain 717 ｜ Call Wall 720（-1.7%）（OI 10.5k） ｜ Put Wall 717（-2.1%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,360,565 股

📆 09-24 Forward Structure
存量OI: C 27.1k / P 40.2k，今日变化ΔOI: C +10.2k / P +4.6k，平值价格ATM: C $4.13 / P $4.40 ｜ ATM IV 15.5%，净 delta 敞口 531k shares
Top ΔOI: C 732 +4,300 ｜ C 730 +1,402 ｜ C 735 +669
仓位参考: Max Pain 716 ｜ Call Wall 732（-0.1%）（OI 4.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.5%｜历史 Rank 33%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 531,227 股

📆 09-25 Forward Structure
存量OI: C 121.0k / P 359.4k，今日变化ΔOI: C +28.8k / P +46.8k，平值价格ATM: C $5.06 / P $5.10 ｜ ATM IV 15.9%，净 delta 敞口 998k shares
Top ΔOI: P 705 +29,640 ｜ P 665 -18,605 ｜ P 690 -9,335
仓位参考: Max Pain 718 ｜ Call Wall 730（-0.4%）（OI 11.1k）
量化解读： 存量 Put 重｜ATM IV 15.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 正 997,509 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/QQQ_morning.json