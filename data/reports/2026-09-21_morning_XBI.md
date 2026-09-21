# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $773.06 ｜ QQQ $741.47
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 157C ΔOI +450（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.72 → 今开 158.49（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 159.04 ｜ 低 156.58

Options: P/C成交量 2.44 | OI比 3.93 | ATM IV 30.9% | Skew 2.9pp | Term 0.95 | ExpMove ±3.4%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 2.9pp）｜当日成交偏 Put（P/C量 2.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.44×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.93×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±3.4% ｜ 10-02（11D）±5.6% ｜ 10-09（18D）±2.7% ｜ 10-16（25D）±6.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -19,635,352 | GEX Change vs 上次快照 3,942,329 | Flip: Primary Flip: 165.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 349 / LOW 69 / INVALID 350
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.68（全链重定价，覆盖 99%）
Put Wall 150（现价高于该位 5.8%）
最近结构参考: Flip 166（现价低于该位 4.2%）
量化视角： 负 Gamma（1964万，无历史分位）｜负 Gamma 缓解（+394万）｜现价位于 Flip 下方 4.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 144.0P — Vol 5,003 | 最新价 $1.22 | OI 51→5049 (ΔOI +4998张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4998张（+9800.0% vs前日OI），连续性待观察（方向未知）
10-16 154.0P — Vol 5,100 | 最新价 $3.75 | OI 398→5156 (ΔOI +4758张) | ΔOI/Volume 93.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4758张（+1195.5% vs前日OI），连续性待观察（方向未知）
09-25 150.0P — Vol 5,049 | 最新价 $0.58 | OI 9586→14266 (ΔOI +4680张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4680张（+48.8% vs前日OI），连续性待观察（方向未知）
09-25 150.0C — Vol 1,002 | 最新价 $7.05 | OI 41→1042 (ΔOI +1001张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1001张（+2441.5% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 675 | 最新价 $3.72 | OI 421→951 (ΔOI +530张) | ΔOI/Volume 78.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增530张（+125.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,967 张（Put 14,436 / Call 1,531），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +2.3k / P +5.0k ｜ Activity HIGH ｜ 4D
10-02  C -17 / P +81 ｜ Activity HIGH ｜ 11D
10-09  C +4 / P +0.1k ｜ Activity HIGH ｜ 18D
10-16  C -0.1k / P +10.6k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 9.5k / P 37.3k，今日变化ΔOI: C +2.3k / P +5.0k，平值价格ATM: C $1.55 / P $3.78 ｜ ATM IV 30.9%，净 delta 敞口 61k shares
Top ΔOI: P 150 +4,680 ｜ C 150 +1,001 ｜ C 157 +450
仓位参考: Max Pain 157 ｜ Call Wall 160（+0.8%，弱）（OI 2.4k） ｜ Put Wall 150（-5.5%，弱）（OI 14.3k）
量化解读： 存量 Put 重｜ATM IV 30.9%｜历史 Rank 38%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,794 股

📆 10-02 Forward Structure
存量OI: C 1.7k / P 1.7k，今日变化ΔOI: C -17 / P +81，平值价格ATM: C $3.50 / P $5.35 ｜ ATM IV 29.7%，净 delta 敞口 -651 shares
Top ΔOI: C 165 -31 ｜ P 157 -17
仓位参考: Max Pain 160 ｜ Call Wall 165（+3.9%）（OI 0.7k） ｜ Put Wall 157（-1.1%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.7%｜历史 Rank 38%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 651 股

📆 10-09 Forward Structure
存量OI: C 0.4k / P 1.4k，今日变化ΔOI: C +4 / P +0.1k，平值价格ATM: C $0.00 / P $4.35 ｜ ATM IV 29.6%，净 delta 敞口 -3k shares
Top ΔOI: P 150 +50 ｜ P 158 +9
仓位参考: Max Pain 160 ｜ Call Wall 160（+0.8%，弱）（OI 18） ｜ Put Wall 150（-5.5%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 29.6%｜历史 Rank 38%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,529 股

📆 10-16 Forward Structure
存量OI: C 33.2k / P 64.2k，今日变化ΔOI: C -0.1k / P +10.6k，平值价格ATM: C $3.87 / P $5.95 ｜ ATM IV 29.2%，净 delta 敞口 -317k shares
Top ΔOI: P 144 +4,998 ｜ P 154 +4,758 ｜ C 155 -682
仓位参考: Max Pain 165 ｜ Call Wall 165（+3.9%，弱）（OI 2.3k） ｜ Put Wall 150（-5.5%）（OI 17.6k）
量化解读： 存量 Put 重｜ATM IV 29.2%｜历史 Rank 38%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 316,610 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/XBI_morning.json