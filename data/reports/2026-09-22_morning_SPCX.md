# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.25 ｜ QQQ $747.46
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 160C ΔOI +11,373（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 151.85 → 今开 151.70（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 154.47 ｜ 低 150.55

Options: P/C成交量 0.38 | OI比 0.88 | ATM IV 56.4% | Skew 0.6pp | Term 0.87 | ExpMove ±4.3%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 0.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（3D）±4.3% ｜ 10-02（10D）±7.0% ｜ 10-09（17D）±8.8% ｜ 10-16（24D）±10.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,369,054 | GEX Change vs 上次快照 33,237,692 | Flip: Primary Flip: 151.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 601 / LOW 90 / INVALID 299
结构观察区: Primary Flip 151.02（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 151（现价高于该位 2.2%）
量化视角： 正 Gamma（3937万，无历史分位）｜正 Gamma 增强（+3324万）｜现价位于 Flip 上方 2.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 172.5C — Vol 21,415 | 最新价 $0.16 | OI 2148→17160 (ΔOI +15012张) | ΔOI/Volume 70.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15012张（+698.9% vs前日OI），连续性待观察（方向未知）
10-16 172.5C — Vol 14,742 | 最新价 $2.11 | OI 0→11473 (ΔOI +11473张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11473张（前日OI缺失），连续性待观察（方向未知）
09-25 160.0C — Vol 62,425 | 最新价 $1.06 | OI 14941→26314 (ΔOI +11373张) | ΔOI/Volume 18.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11373张（+76.1% vs前日OI），连续性待观察（方向未知）
09-25 170.0C — Vol 25,544 | 最新价 $0.22 | OI 22147→29702 (ΔOI +7555张) | ΔOI/Volume 29.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7555张（+34.1% vs前日OI），连续性待观察（方向未知）
09-25 165.0C — Vol 20,201 | 最新价 $0.49 | OI 8730→15259 (ΔOI +6529张) | ΔOI/Volume 32.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6529张（+74.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 51,942 张（Put 0 / Call 51,942），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +65.3k / P +23.4k ｜ Activity HIGH ｜ 3D
10-02  C +13.0k / P +12.6k ｜ Activity HIGH ｜ 10D
10-09  C +3.5k / P +3.3k ｜ Activity MEDIUM △ ｜ 17D
10-16  C +19.1k / P +9.3k ｜ Activity MEDIUM △ ｜ 24D

📆 09-25 Forward Structure
存量OI: C 221.8k / P 195.2k，今日变化ΔOI: C +65.3k / P +23.4k，平值价格ATM: C $2.70 / P $3.95 ｜ ATM IV 56.4%，净 delta 敞口 576k shares
Top ΔOI: C 172 +15,012 ｜ C 160 +11,373 ｜ C 170 +7,555
仓位参考: Max Pain 150 ｜ Call Wall 160（+3.7%，弱）（OI 26.3k） ｜ Put Wall 140（-9.3%，弱）（OI 16.8k）
量化解读： 存量两侧均衡｜ATM IV 56.4%｜历史 Rank 35%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 575,852 股

📆 10-02 Forward Structure
存量OI: C 65.6k / P 77.4k，今日变化ΔOI: C +13.0k / P +12.6k，平值价格ATM: C $4.83 / P $5.90 ｜ ATM IV 51.9%，净 delta 敞口 -12k shares
Top ΔOI: P 135 +3,471 ｜ C 190 +2,277 ｜ C 175 +1,999
仓位参考: Max Pain 150 ｜ Call Wall 160（+3.7%，弱）（OI 5.7k） ｜ Put Wall 150（-2.8%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.9%｜历史 Rank 35%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,960 股

10-09（MEDIUM △）Top ΔOI: 160C +909 ｜ 135P +632
10-09（MEDIUM △）仓位参考: Max Pain 149 ｜ Call Wall 160（+3.7%，弱）（OI 2.5k） ｜ Put Wall 140（-9.3%，弱）（OI 1.5k）

10-16（MEDIUM △）Top ΔOI: 172C +11,473 ｜ 157P +4,126
10-16（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（+3.7%，弱）（OI 35.2k） ｜ Put Wall 155（+0.5%，弱）（OI 49.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SPCX_morning.json