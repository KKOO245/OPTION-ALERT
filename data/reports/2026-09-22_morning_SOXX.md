# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.90 ｜ QQQ $745.45
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 560C ΔOI +225（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 559.34 → 今开 553.76（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 566.05 ｜ 低 553.44

Options: P/C成交量 0.61 | OI比 1.49 | ATM IV 36.4% | Skew -0.6pp | Term 1.05 | ExpMove ±3.1%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.49×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±3.1% ｜ 10-02（10D）±2.4% ｜ 10-09（17D）±2.5% ｜ 10-16（24D）±8.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,596,079 | GEX Change vs 上次快照 570,340 | Flip: Primary Flip: 547.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 578 / LOW 254 / INVALID 674
结构观察区: Primary Flip 547.22（全链重定价，覆盖 98%）
最近结构参考: Flip 547（现价高于该位 2.9%）
量化视角： 正 Gamma（860万，无历史分位）｜正 Gamma 增强（+57万）｜现价位于 Flip 上方 2.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 530（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 547（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 600.0C — Vol 5,825 | 最新价 $8.25 | OI 9087→13585 (ΔOI +4498张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4498张（+49.5% vs前日OI），连续性待观察（方向未知）
10-23 510.0P — Vol 2,975 | 最新价 $7.50 | OI 59→2967 (ΔOI +2908张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2908张（+4928.8% vs前日OI），连续性待观察（方向未知）
10-16 530.0P — Vol 1,319 | 最新价 $9.90 | OI 1321→2403 (ΔOI +1082张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1082张（+81.9% vs前日OI），连续性待观察（方向未知）
10-16 605.0C — Vol 309 | 最新价 $6.25 | OI 56→353 (ΔOI +297张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增297张（+530.4% vs前日OI），连续性待观察（方向未知）
10-16 595.0C — Vol 307 | 最新价 $8.20 | OI 56→352 (ΔOI +296张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增296张（+528.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,081 张（Put 3,990 / Call 5,091），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.5k / P +1.2k ｜ Activity MEDIUM △ ｜ 3D
10-02  C +0.6k / P +0.8k ｜ Activity MEDIUM △ ｜ 10D
10-09  C +0.1k / P +57 ｜ Activity LOW ｜ 17D
10-16  C +3.9k / P +1.2k ｜ Activity MEDIUM △ ｜ 24D

📆 09-25 Forward Structure
存量OI: C 11.5k / P 17.2k，今日变化ΔOI: C +0.5k / P +1.2k，平值价格ATM: C $8.28 / P $9.30 ｜ ATM IV 36.4%，净 delta 敞口 -22k shares
Top ΔOI: P 522 +288 ｜ P 550 +261 ｜ C 560 +225
仓位参考: Max Pain 530 ｜ Call Wall 580（+3.0%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 36.4%｜历史 Rank 60%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 负 22,110 股

10-02（MEDIUM △）Top ΔOI: 600C +134
10-02（MEDIUM △）仓位参考: Max Pain 520 ｜ Call Wall 542.5（-3.7%，弱）（OI 2.8k）

10-09（Activity LOW）仓位参考: Max Pain 518 ｜ Call Wall 537.5（-4.6%，弱）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 600C +4,498 ｜ 550C -1,157
10-16（MEDIUM △）仓位参考: Max Pain 525 ｜ Put Wall 530（-5.9%，弱）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SOXX_morning.json