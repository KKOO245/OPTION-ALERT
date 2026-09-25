# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.58
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,753.62 → 今开 1,791.80（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1815.00 ｜ 低 1742.95

Options: P/C成交量 0.45 | OI比 0.98 | ATM IV 88.9% | Skew -5.2pp | Term 0.77 | ExpMove ±8.1%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（7D）±8.1% ｜ 10-09（14D）±10.8% ｜ 10-16（21D）±14.2% ｜ 10-23（28D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,632,851 | GEX Change vs 上次快照 9,256,419 | Flip: Primary Flip: 1719.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 1942 / LOW 522 / INVALID 982
结构观察区: Primary Flip 1719.34（全链重定价，覆盖 95%）
最近结构参考: Flip 1719（现价高于该位 3.0%）
量化视角： 正 Gamma（963万，无历史分位）｜正 Gamma 增强（+926万）｜现价位于 Flip 上方 3.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,750（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1719（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 1825.0C — Vol 7,664 | 最新价 $6.59 | OI 476→1966 (ΔOI +1490张) | ΔOI/Volume 19.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1490张（+313.0% vs前日OI），连续性待观察（方向未知）
09-25 1900.0C — Vol 8,932 | 最新价 $1.70 | OI 2688→4040 (ΔOI +1352张) | ΔOI/Volume 15.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1352张（+50.3% vs前日OI），连续性待观察（方向未知）
09-25 1820.0C — Vol 2,816 | 最新价 $7.20 | OI 406→1147 (ΔOI +741张) | ΔOI/Volume 26.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增741张（+182.5% vs前日OI），连续性待观察（方向未知）
09-25 1800.0C — Vol 14,107 | 最新价 $10.80 | OI 2183→2878 (ΔOI +695张) | ΔOI/Volume 4.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增695张（+31.8% vs前日OI），连续性待观察（方向未知）
09-25 1790.0C — Vol 2,305 | 最新价 $13.20 | OI 215→874 (ΔOI +659张) | ΔOI/Volume 28.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增659张（+306.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,937 张（Put 0 / Call 4,937），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 67.0k / P 65.5k，今日成交量: C 37.0k / P 16.6k，平值价格ATM: C $14.35 / P $19.85 ｜ ATM IV 88.9%，预期波动 ±1.9%，Max Pain 1,750
Top ΔOI: C 1825 +1,490 ｜ C 1900 +1,352 ｜ C 1820 +741

📆 Forward Expiration Structure

10-02  C +1.5k / P +3.5k ｜ Activity HIGH ｜ 7D
10-09  C +0.9k / P +0.6k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +1.2k / P +1.0k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.3k / P +0.5k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 25.5k / P 23.5k，今日变化ΔOI: C +1.5k / P +3.5k，平值价格ATM: C $71.04 / P $71.50 ｜ ATM IV 71.1%，净 delta 敞口 -153k shares
Top ΔOI: C 1600 -2,493 ｜ C 2000 +650 ｜ P 1550 +393
仓位参考: Max Pain 1,690 ｜ Call Wall 1600（-9.7%，弱）（OI 1.8k） ｜ Put Wall 1600（-9.7%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 71.1%｜历史 Rank 42%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 153,077 股

10-09（MEDIUM △）Top ΔOI: 1550P +117 ｜ 1750C +84
10-09（MEDIUM △）仓位参考: Max Pain 1,570 ｜ Put Wall 1600（-9.7%，弱）（OI 0.2k）

10-16（MEDIUM △）Top ΔOI: 2500C +174 ｜ 1580P +151
10-16（MEDIUM △）仓位参考: Max Pain 1,640 ｜ Call Wall 1800（+1.6%，弱）（OI 1.2k） ｜ Put Wall 1600（-9.7%，弱）（OI 1.5k）

10-23（MEDIUM △）Top ΔOI: 1540P +81 ｜ 1500P +48
10-23（MEDIUM △）仓位参考: Max Pain 1,750 ｜ Call Wall 1840（+3.9%，弱）（OI 0.2k） ｜ Put Wall 1650（-6.9%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SNDK_morning.json