# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $759.94 ｜ QQQ $692.83
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-02 402C ΔOI +1,003（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 403.30 → 今开 393.04（-2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 398.19 ｜ 低 387.52

Options: P/C成交量 0.82 | OI比 1.22 | ATM IV 58.1% | Skew 3.7pp | Term 0.66 | ExpMove ±2.3%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.3% ｜ 11-04（5D）±3.8% ｜ 11-06（7D）±4.7% ｜ 11-09（10D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 89,348,385 | GEX Change vs 上次快照 -45,328,520 | Flip: Primary Flip: 384.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 1228 / LOW 170 / INVALID 948
结构观察区: Primary Flip 384.31（全链重定价，覆盖 95%）
Call Wall 420（弱结构｜现价低于该位 5.4%）
最近结构参考: Flip 384（现价高于该位 3.3%）
量化视角： 正 Gamma（8935万，无历史分位）｜正 Gamma 减弱（4533万）｜现价位于 Flip 上方 3.34%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 388（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 384（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-02 455.0C — Vol 5,137 | 最新价 $0.07 | OI 10288→15243 (ΔOI +4955张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4955张（+48.2% vs前日OI），连续性待观察（方向未知）
11-06 425.0C — Vol 6,395 | 最新价 $2.35 | OI 2628→7204 (ΔOI +4576张) | ΔOI/Volume 71.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4576张（+174.1% vs前日OI），连续性待观察（方向未知）
10-30 405.0P — Vol 46,754 | 最新价 $4.15 | OI 3049→7291 (ΔOI +4242张) | ΔOI/Volume 9.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4242张（+139.1% vs前日OI），连续性待观察（方向未知）
11-06 412.5C — Vol 4,480 | 最新价 $5.45 | OI 870→5029 (ΔOI +4159张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4159张（+478.1% vs前日OI），连续性待观察（方向未知）
11-06 150.0P — Vol 4,144 | 最新价 $0.01 | OI 983→4895 (ΔOI +3912张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3912张（+398.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,844 张（Put 8,154 / Call 13,690），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 240.0k / P 292.6k，今日成交量: C 236.2k / P 194.5k，平值价格ATM: C $2.54 / P $2.44 ｜ ATM IV 58.1%，预期波动 ±1.3%，Max Pain 388
Top ΔOI: P 405 +4,242 ｜ P 400 +3,345 ｜ P 390 +2,644

📆 Forward Expiration Structure

11-02  C +10.8k / P +5.8k ｜ Activity HIGH ｜ 3D
11-04  C +2.8k / P +3.0k ｜ Activity HIGH ｜ 5D
11-06  C +21.5k / P +22.3k ｜ Activity HIGH ｜ 7D
11-09  C +1.4k / P +1.4k ｜ Activity HIGH ｜ 10D

📆 11-02 Forward Structure
存量OI: C 60.4k / P 27.5k，今日变化ΔOI: C +10.8k / P +5.8k，平值价格ATM: C $4.65 / P $4.65 ｜ ATM IV 30.9%，净 delta 敞口 -44k shares
Top ΔOI: C 402 +1,003
仓位参考: Max Pain 395 ｜ Call Wall 410（+3.2%，弱）（OI 3.3k） ｜ Put Wall 400（+0.7%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 30.9%｜历史 Rank 68%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 43,803 股

📆 11-04 Forward Structure
存量OI: C 13.9k / P 12.9k，今日变化ΔOI: C +2.8k / P +3.0k，平值价格ATM: C $7.50 / P $7.48 ｜ ATM IV 39.0%，净 delta 敞口 -55k shares
Top ΔOI: P 402 +1,038 ｜ P 370 +552
仓位参考: Max Pain 400 ｜ Call Wall 410（+3.2%，弱）（OI 1.6k） ｜ Put Wall 400（+0.7%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.0%｜历史 Rank 68%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 54,937 股

📆 11-06 Forward Structure
存量OI: C 82.7k / P 103.5k，今日变化ΔOI: C +21.5k / P +22.3k，平值价格ATM: C $9.50 / P $9.20 ｜ ATM IV 41.0%，净 delta 敞口 125k shares
Top ΔOI: C 425 +4,576 ｜ C 412 +4,159
仓位参考: Max Pain 390 ｜ Call Wall 425（+7.0%，弱）（OI 7.2k） ｜ Put Wall 400（+0.7%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜ATM IV 41.0%｜历史 Rank 68%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 124,614 股

📆 11-09 Forward Structure
存量OI: C 3.0k / P 4.1k，今日变化ΔOI: C +1.4k / P +1.4k，平值价格ATM: C $9.32 / P $11.45 ｜ ATM IV 37.4%，净 delta 敞口 -8k shares
Top ΔOI: C 420 +693 ｜ P 380 +595 ｜ P 405 +240
仓位参考: Max Pain 400 ｜ Call Wall 420（+5.8%）（OI 0.8k） ｜ Put Wall 380（-4.3%）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 37.4%｜历史 Rank 68%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 7,712 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/TSLA_morning.json