# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -5.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 500P ΔOI +561（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 527.07 → 今开 497.58（-5.6%） | 较昨收变动（含盘初走势） ｜ 今日高 503.15 ｜ 低 495.15

Options: P/C成交量 1.72 | OI比 0.94 | ATM IV 35.7% | Skew 3.7pp | Term 1.06 | ExpMove ±6.1%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 3.7pp）｜当日成交偏 Put（P/C量 1.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.72×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±6.1% ｜ 09-25（11D）±7.2% ｜ 10-02（18D）±7.5% ｜ 10-09（25D）±9.0%
   ⇒ IV–VIX Spread: +18.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -46,595,205 | GEX Change vs 上次快照 -45,674,709 | Flip: Primary Flip: 529.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 616 / LOW 303 / INVALID 707
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 529.58（全链重定价，覆盖 96%）
Put Wall 450（弱结构｜现价高于该位 11.0%）
最近结构参考: Flip 530（现价低于该位 5.7%）
量化视角： 负 Gamma（4660万，无历史分位）｜负 Gamma 加深（4567万）｜现价位于 Flip 下方 5.67%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 450（Put Wall，弱结构）；上方 530（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 530（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 440.0P — Vol 4,205 | 最新价 $2.57 | OI 179→4148 (ΔOI +3969张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3969张（+2217.3% vs前日OI），连续性待观察（方向未知）
10-16 600.0C — Vol 3,163 | 最新价 $3.60 | OI 5497→8468 (ΔOI +2971张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2971张（+54.0% vs前日OI），连续性待观察（方向未知）
10-16 585.0C — Vol 2,803 | 最新价 $5.90 | OI 65→2860 (ΔOI +2795张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2795张（+4300.0% vs前日OI），连续性待观察（方向未知）
10-16 550.0C — Vol 2,057 | 最新价 $14.50 | OI 1064→3056 (ΔOI +1992张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1992张（+187.2% vs前日OI），连续性待观察（方向未知）
10-16 490.0P — Vol 2,042 | 最新价 $9.96 | OI 3068→5033 (ΔOI +1965张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1965张（+64.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,692 张（Put 5,934 / Call 7,758），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.8k / P +1.5k ｜ Activity HIGH ｜ 4D
09-25  C +0.5k / P +1.2k ｜ Activity HIGH ｜ 11D
10-02  C +0.2k / P +90 ｜ Activity MEDIUM △ ｜ 18D
10-09  C -13 / P +14 ｜ Activity MEDIUM △ ｜ 25D

📆 09-18 Forward Structure
存量OI: C 100.0k / P 93.8k，今日变化ΔOI: C +0.8k / P +1.5k，平值价格ATM: C $28.50 / P $2.12 ｜ ATM IV 35.7%，净 delta 敞口 -25k shares
Top ΔOI: P 500 +561 ｜ C 552 +449 ｜ P 470 +305
仓位参考: Max Pain 530 ｜ Put Wall 450（-9.9%，弱）（OI 12.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.7%｜历史 Rank 58%（近端代理）｜IV/RV 1.23×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 25,407 股

📆 09-25 Forward Structure
存量OI: C 8.5k / P 10.4k，今日变化ΔOI: C +0.5k / P +1.2k，平值价格ATM: C $31.40 / P $4.78 ｜ ATM IV 33.7%，净 delta 敞口 9k shares
Top ΔOI: P 460 +942 ｜ C 550 +125 ｜ C 555 +110
仓位参考: Max Pain 530 ｜ Put Wall 480（-3.9%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 33.7%｜历史 Rank 58%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 8,925 股

10-02（MEDIUM △）Top ΔOI: 570C +138 ｜ 500P +32
10-02（MEDIUM △）仓位参考: Max Pain 525 ｜ Call Wall 542.5（+8.6%，弱）（OI 2.8k） ｜ Put Wall 470（-5.9%）（OI 2.8k）

10-09（MEDIUM △）Top ΔOI: 530C -8
10-09（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 525（+5.1%）（OI 1.6k） ｜ Put Wall 465（-6.9%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SOXX_morning.json