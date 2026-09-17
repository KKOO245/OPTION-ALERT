# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 500C ΔOI +1,601（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 498.85 → 今开 507.50（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 509.77 ｜ 低 505.38

Options: P/C成交量 0.94 | OI比 0.90 | ATM IV 42.5% | Skew 4.9pp | Term 0.85 | ExpMove ±2.7%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 4.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±2.7% ｜ 09-25（9D）±6.9% ｜ 10-02（16D）±5.7% ｜ 10-09（23D）±6.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,129,659 | GEX Change vs 上次快照 12,309,237 | Flip: Primary Flip: 524.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 548 / LOW 356 / INVALID 722
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 524.97（全链重定价，覆盖 89%）
最近结构参考: Flip 525（现价低于该位 3.1%）
量化视角： 负 Gamma（3313万，无历史分位）｜负 Gamma 缓解（+1231万）｜现价位于 Flip 下方 3.11%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 520（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 525（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 500.0C — Vol 1,764 | 最新价 $6.76 | OI 1116→2717 (ΔOI +1601张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1601张（+143.5% vs前日OI），连续性待观察（方向未知）
10-16 400.0P — Vol 1,008 | 最新价 $1.65 | OI 2869→3677 (ΔOI +808张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增808张（+28.2% vs前日OI），连续性待观察（方向未知）
10-16 510.0C — Vol 779 | 最新价 $16.50 | OI 2072→2669 (ΔOI +597张) | ΔOI/Volume 76.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增597张（+28.8% vs前日OI），连续性待观察（方向未知）
10-16 320.0P — Vol 502 | 最新价 $0.30 | OI 1671→2171 (ΔOI +500张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+29.9% vs前日OI），连续性待观察（方向未知）
10-16 465.0P — Vol 468 | 最新价 $8.77 | OI 1041→1353 (ΔOI +312张) | ΔOI/Volume 66.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增312张（+30.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,818 张（Put 1,620 / Call 2,198），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.3k / P -3.7k ｜ Activity MEDIUM △ ｜ 2D
09-25  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 9D
10-02  C +26 / P +9 ｜ Activity MEDIUM △ ｜ 16D
10-09  C +33 / P +2 ｜ Activity LOW ｜ 23D

📆 09-18 Forward Structure
存量OI: C 104.3k / P 94.3k，今日变化ΔOI: C +2.3k / P -3.7k，平值价格ATM: C $7.30 / P $6.62 ｜ ATM IV 42.5%，净 delta 敞口 415k shares
Top ΔOI: C 500 +1,601 ｜ P 480 -943 ｜ P 540 -901
仓位参考: Max Pain 520 ｜ Call Wall 535（+5.2%，弱）（OI 3.8k） ｜ Put Wall 480（-5.6%，弱）（OI 8.0k）
量化解读： 存量两侧均衡｜ATM IV 42.5%｜历史 Rank 76%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 414,634 股

09-25（MEDIUM △）Top ΔOI: 480P +55 ｜ 520C +49
09-25（MEDIUM △）仓位参考: Max Pain 520 ｜ Put Wall 480（-5.6%，弱）（OI 2.0k）

10-02（MEDIUM △）Top ΔOI: 495P -18 ｜ 505C +17
10-02（MEDIUM △）仓位参考: Max Pain 512 ｜ Call Wall 542.5（+6.7%，弱）（OI 2.8k） ｜ Put Wall 470（-7.6%）（OI 3.0k）

10-09（Activity LOW）仓位参考: Max Pain 510 ｜ Call Wall 525（+3.2%）（OI 1.6k） ｜ Put Wall 465（-8.6%）（OI 0.4k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 42.5% vs 09-25 35.7%（差 +6.8pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SOXX_morning.json