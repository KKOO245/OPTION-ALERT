# 期权晚报 2026-09-15（快照 18:31 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 502.65 → 收盘 498.85（-0.8%） ｜ 今日高 504.74 ｜ 低 496.58 ｜ 昨收 497.40 → 收盘 498.85（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.53 | OI比 0.96 | ATM IV 40.0% | Skew 5.2pp | Term 0.91 | ExpMove ±3.0%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 5.2pp）｜当日成交偏 Put（P/C量 1.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（3D）±3.0% ｜ 09-25（10D）±5.0% ｜ 10-02（17D）±6.2% ｜ 10-09（24D）±7.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -45,438,896 | GEX Change vs 上次快照 -2,856,930 | Flip: Primary Flip: 523.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 558 / LOW 353 / INVALID 715
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 523.73（全链重定价，覆盖 92%）
Put Wall 450（弱结构｜现价高于该位 10.9%）
最近结构参考: Flip 524（现价低于该位 4.8%）
量化视角： 负 Gamma（4544万，无历史分位）｜负 Gamma 加深（286万）｜现价位于 Flip 下方 4.75%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 450（Put Wall，弱结构）；上方 525（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 524（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 430.0P — Vol 12 | 最新价 $3.50 | OI 1823→5131 (ΔOI +3308张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3308张（+181.5% vs前日OI），连续性待观察（方向未知）
10-16 460.0P — Vol 241 | 最新价 $7.60 | OI 272→3103 (ΔOI +2831张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2831张（+1040.8% vs前日OI），连续性待观察（方向未知）
09-18 457.5P — Vol 2 | 最新价 $0.30 | OI 0→2394 (ΔOI +2394张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2394张（前日OI缺失），值得跟踪（方向未知）
10-16 475.0P — Vol 92 | 最新价 $11.45 | OI 950→3055 (ΔOI +2105张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2105张（+221.6% vs前日OI），连续性待观察（方向未知）
10-16 470.0P — Vol 48 | 最新价 $10.27 | OI 2653→4591 (ΔOI +1938张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1938张（+73.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,576 张（Put 12,576 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-18 Forward Structure
存量OI: C 102.0k / P 97.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.76 / P $8.10 ｜ ATM IV 40.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 525 ｜ Call Wall 535（+7.2%，弱）（OI 3.6k） ｜ Put Wall 450（-9.8%，弱）（OI 11.5k）
量化解读： 存量两侧均衡｜ATM IV 40.0%｜历史 Rank 70%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 522 ｜ Put Wall 480（-3.8%，弱）（OI 2.0k）

10-02（Activity LOW）仓位参考: Max Pain 515 ｜ Call Wall 542.5（+8.8%，弱）（OI 2.8k） ｜ Put Wall 470（-5.8%）（OI 3.0k）

10-09（Activity LOW）仓位参考: Max Pain 510 ｜ Call Wall 525（+5.2%）（OI 1.6k） ｜ Put Wall 465（-6.8%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SOXX_evening.json