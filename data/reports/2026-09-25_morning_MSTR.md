# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.47
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


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 161.61 → 今开 162.75（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 162.75 ｜ 低 157.42

Options: P/C成交量 0.14 | OI比 0.75 | ATM IV 90.4% | Skew -4.7pp | Term 0.72 | ExpMove ±7.3%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±7.3% ｜ 10-09（14D）±10.6% ｜ 10-16（21D）±12.7% ｜ 10-23（28D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,633,263 | GEX Change vs 上次快照 4,101,136 | Flip: Primary Flip: 137.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 838 / LOW 100 / INVALID 206
结构观察区: Primary Flip 137.96（全链重定价，覆盖 98%）
最近结构参考: Flip 138（现价高于该位 14.7%）
量化视角： 正 Gamma（7463万，无历史分位）｜正 Gamma 增强（+410万）｜现价位于 Flip 上方 14.73%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 167.5C — Vol 15,608 | 最新价 $4.35 | OI 755→14996 (ΔOI +14241张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14241张（+1886.2% vs前日OI），连续性待观察（方向未知）
10-02 175.0C — Vol 13,029 | 最新价 $2.65 | OI 4076→13339 (ΔOI +9263张) | ΔOI/Volume 71.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9263张（+227.3% vs前日OI），连续性待观察（方向未知）
10-02 90.0P — Vol 4,989 | 最新价 $0.04 | OI 10380→14863 (ΔOI +4483张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4483张（+43.2% vs前日OI），连续性待观察（方向未知）
10-02 172.5C — Vol 4,408 | 最新价 $3.05 | OI 720→4624 (ΔOI +3904张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3904张（+542.2% vs前日OI），连续性待观察（方向未知）
10-02 170.0C — Vol 5,318 | 最新价 $3.95 | OI 3110→5891 (ΔOI +2781张) | ΔOI/Volume 52.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2781张（+89.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 34,672 张（Put 4,483 / Call 30,189），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 306.1k / P 230.4k，今日成交量: C 92.6k / P 12.7k，平值价格ATM: C $1.66 / P $1.44 ｜ ATM IV 90.4%，预期波动 ±2.0%，Max Pain 142
Top ΔOI: C 180 -4,058 ｜ P 150 +1,995 ｜ C 162 -1,480

📆 Forward Expiration Structure

10-02  C +34.8k / P +12.0k ｜ Activity HIGH ｜ 7D
10-09  C +1.3k / P +3.2k ｜ Activity HIGH ｜ 14D
10-16  C +3.7k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.8k / P +2.0k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 98.8k / P 119.1k，今日变化ΔOI: C +34.8k / P +12.0k，平值价格ATM: C $5.95 / P $5.55 ｜ ATM IV 64.6%，净 delta 敞口 597k shares
Top ΔOI: C 167 +14,241 ｜ C 175 +9,263
仓位参考: Max Pain 155 ｜ Call Wall 167.5（+5.8%，弱）（OI 15.0k） ｜ Put Wall 150（-5.2%，弱）（OI 11.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.6%｜历史 Rank 67%（近端代理）｜IV/RV 0.66×（近似）｜净 delta 敞口 正 596,948 股

📆 10-09 Forward Structure
存量OI: C 31.4k / P 47.6k，今日变化ΔOI: C +1.3k / P +3.2k，平值价格ATM: C $9.25 / P $7.50 ｜ ATM IV 64.0%，净 delta 敞口 8k shares
Top ΔOI: C 160 +512
仓位参考: Max Pain 144 ｜ Call Wall 160（+1.1%，弱）（OI 5.6k） ｜ Put Wall 155（-2.1%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 64.0%｜历史 Rank 67%（近端代理）｜IV/RV 0.65×（近似）｜净 delta 敞口 正 7,653 股

10-16（MEDIUM △）Top ΔOI: 95C +2,059 ｜ 200C +607
10-16（MEDIUM △）仓位参考: Max Pain 120 ｜ Call Wall 155（-2.1%，弱）（OI 10.4k） ｜ Put Wall 160（+1.1%，弱）（OI 4.1k）

10-23（MEDIUM △）Top ΔOI: 160P +306 ｜ 165P +247
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 170（+7.4%，弱）（OI 1.0k） ｜ Put Wall 155（-2.1%，弱）（OI 1.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/MSTR_morning.json