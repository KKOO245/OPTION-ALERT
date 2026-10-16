# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.51 ｜ QQQ $721.56
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,394.83 → 今开 1,348.82（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 1362.34 ｜ 低 1324.37

Options: P/C成交量 0.72 | OI比 0.66 | ATM IV 99.3% | Skew -1.9pp | Term 0.72 | ExpMove ±7.5%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±7.5% ｜ 10-30（14D）±12.5% ｜ 11-06（21D）±14.6% ｜ 11-13（28D）±16.8%
   ⇒ IV–VIX Spread: +83.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,009,792 | GEX Change vs 上次快照 5,243,599 | Flip: Primary Flip: 1372.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1936 / LOW 481 / INVALID 1097
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1372.54（全链重定价，覆盖 99%）
最近结构参考: Flip 1373（现价低于该位 2.7%）
量化视角： 负 Gamma（501万，无历史分位）｜负 Gamma 缓解（+524万）｜现价位于 Flip 下方 2.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,440（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1373（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 1675.0C — Vol 4,903 | 最新价 $0.30 | OI 2404→7059 (ΔOI +4655张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4655张（+193.6% vs前日OI），连续性待观察（方向未知）
10-16 1500.0C — Vol 8,350 | 最新价 $3.37 | OI 2057→4019 (ΔOI +1962张) | ΔOI/Volume 23.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1962张（+95.4% vs前日OI），连续性待观察（方向未知）
11-20 1500.0C — Vol 2,191 | 最新价 $85.50 | OI 528→2322 (ΔOI +1794张) | ΔOI/Volume 81.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1794张（+339.8% vs前日OI），连续性待观察（方向未知）
10-16 1400.0C — Vol 9,938 | 最新价 $25.61 | OI 363→2082 (ΔOI +1719张) | ΔOI/Volume 17.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1719张（+473.6% vs前日OI），连续性待观察（方向未知）
10-16 1325.0C — Vol 6,292 | 最新价 $76.00 | OI 2→1235 (ΔOI +1233张) | ΔOI/Volume 19.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1233张（+61650.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,363 张（Put 0 / Call 11,363），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 95.4k / P 62.7k，今日成交量: C 23.0k / P 16.5k，平值价格ATM: C $16.55 / P $12.15 ｜ ATM IV 99.3%，预期波动 ±2.1%，Max Pain 1,440
Top ΔOI: C 1675 +4,655 ｜ C 1500 +1,962 ｜ C 1400 +1,719

📆 Forward Expiration Structure

10-23  C +4.2k / P +4.0k ｜ Activity HIGH ｜ 7D
10-30  C +4.2k / P +1.4k ｜ Activity HIGH ｜ 14D
11-06  C +1.2k / P +0.4k ｜ Activity HIGH ｜ 21D
11-13  C +0.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 28.4k / P 23.2k，今日变化ΔOI: C +4.2k / P +4.0k，平值价格ATM: C $50.73 / P $49.22 ｜ ATM IV 66.3%，净 delta 敞口 65k shares
Top ΔOI: P 1250 +499 ｜ P 1300 +358
仓位参考: Max Pain 1,500 ｜ Call Wall 1450（+8.6%，弱）（OI 0.4k） ｜ Put Wall 1250（-6.4%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 66.3%｜历史 Rank 55%（近端代理）｜IV/RV 1.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 65,420 股

📆 10-30 Forward Structure
存量OI: C 20.0k / P 14.2k，今日变化ΔOI: C +4.2k / P +1.4k，平值价格ATM: C $78.50 / P $88.20 ｜ ATM IV 78.4%，净 delta 敞口 34k shares
Top ΔOI: C 1650 +314
仓位参考: Max Pain 1,550 ｜ Put Wall 1400（+4.8%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 78.4%｜历史 Rank 55%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,368 股

📆 11-06 Forward Structure
存量OI: C 6.2k / P 6.3k，今日变化ΔOI: C +1.2k / P +0.4k，平值价格ATM: C $99.11 / P $96.20 ｜ ATM IV 74.4%，净 delta 敞口 6k shares
Top ΔOI: C 1950 +313 ｜ C 2000 +87
仓位参考: Max Pain 1,600 ｜ Put Wall 1400（+4.8%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.4%｜历史 Rank 55%（近端代理）｜IV/RV 1.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,877 股

11-13（MEDIUM △）Top ΔOI: 1430C +100 ｜ 1500C +66
11-13（MEDIUM △）仓位参考: Max Pain 1,550 ｜ Call Wall 1430（+7.1%，弱）（OI 0.1k） ｜ Put Wall 1370（+2.6%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SNDK_morning.json