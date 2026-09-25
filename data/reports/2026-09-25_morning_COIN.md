# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.42
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 200C ΔOI +947（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 199.21 → 今开 199.30（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 199.75 ｜ 低 192.78

Options: P/C成交量 0.26 | OI比 0.52 | ATM IV 82.2% | Skew -1.3pp | Term 0.74 | ExpMove ±6.8%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±6.8% ｜ 10-09（14D）±9.2% ｜ 10-16（21D）±11.4% ｜ 10-23（28D）±15.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,179,352 | GEX Change vs 上次快照 -4,704,575 | Flip: Primary Flip: 180.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 496 / LOW 154 / INVALID 262
结构观察区: Primary Flip 180.00（全链重定价，覆盖 97%）
最近结构参考: Flip 180（现价高于该位 7.9%）
量化视角： 正 Gamma（3118万，无历史分位）｜正 Gamma 减弱（470万）｜现价位于 Flip 上方 7.88%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 180（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 110.0P — Vol 2,004 | 最新价 $0.04 | OI 2386→4373 (ΔOI +1987张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1987张（+83.3% vs前日OI），连续性待观察（方向未知）
09-25 210.0C — Vol 11,124 | 最新价 $0.52 | OI 10135→11902 (ΔOI +1767张) | ΔOI/Volume 15.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1767张（+17.4% vs前日OI），连续性待观察（方向未知）
10-02 217.5C — Vol 1,408 | 最新价 $2.50 | OI 115→1417 (ΔOI +1302张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1302张（+1132.2% vs前日OI），连续性待观察（方向未知）
10-02 207.5C — Vol 1,568 | 最新价 $4.55 | OI 311→1567 (ΔOI +1256张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1256张（+403.9% vs前日OI），连续性待观察（方向未知）
10-09 200.0C — Vol 1,264 | 最新价 $10.53 | OI 408→1355 (ΔOI +947张) | ΔOI/Volume 74.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增947张（+232.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,259 张（Put 1,987 / Call 5,272），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 95.3k / P 49.5k，今日成交量: C 25.4k / P 6.5k，平值价格ATM: C $1.08 / P $2.58 ｜ ATM IV 82.2%，预期波动 ±1.9%，Max Pain 185
Top ΔOI: C 210 +1,767 ｜ P 180 -1,506 ｜ C 205 +941

📆 Forward Expiration Structure

10-02  C +5.6k / P +2.5k ｜ Activity HIGH ｜ 7D
10-09  C +1.2k / P +2.2k ｜ Activity HIGH ｜ 14D
10-16  C +1.1k / P +0.5k ｜ Activity HIGH ｜ 21D
10-23  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 27.7k / P 35.6k，今日变化ΔOI: C +5.6k / P +2.5k，平值价格ATM: C $6.15 / P $7.09 ｜ ATM IV 59.8%，净 delta 敞口 26k shares
Top ΔOI: C 217 +1,302 ｜ C 207 +1,256 ｜ C 210 +775
仓位参考: Max Pain 190 ｜ Call Wall 210（+8.1%，弱）（OI 1.6k） ｜ Put Wall 190（-2.2%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 59.8%｜历史 Rank 65%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 正 25,537 股

📆 10-09 Forward Structure
存量OI: C 6.5k / P 14.2k，今日变化ΔOI: C +1.2k / P +2.2k，平值价格ATM: C $8.80 / P $9.00 ｜ ATM IV 60.0%，净 delta 敞口 39k shares
Top ΔOI: C 200 +947 ｜ P 197 +101
仓位参考: Max Pain 188 ｜ Call Wall 200（+3.0%）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 60.0%｜历史 Rank 65%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 正 38,561 股

📆 10-16 Forward Structure
存量OI: C 80.3k / P 73.3k，今日变化ΔOI: C +1.1k / P +0.5k，平值价格ATM: C $10.94 / P $11.21 ｜ ATM IV 59.9%，净 delta 敞口 14k shares
Top ΔOI: P 190 +673 ｜ P 195 -230 ｜ C 210 +203
仓位参考: Max Pain 175 ｜ Call Wall 200（+3.0%，弱）（OI 6.1k） ｜ Put Wall 200（+3.0%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜ATM IV 59.9%｜历史 Rank 65%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 正 13,727 股

10-23（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 210（+8.1%，弱）（OI 0.2k） ｜ Put Wall 190（-2.2%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/COIN_morning.json