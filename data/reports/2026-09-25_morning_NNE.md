# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.39
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
🟡 **近现价集中开仓**: 10-02 17P ΔOI +102（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.02 → 今开 17.15（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 17.42 ｜ 低 16.77

Options: P/C成交量 0.64 | OI比 0.51 | ATM IV 119.3% | Skew 4.3pp | Term 0.60 | ExpMove ±8.7%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 4.3pp）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±8.7% ｜ 10-09（14D）±10.8% ｜ 10-16（21D）±15.7% ｜ 10-23（28D）±18.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,184,570 | GEX Change vs 上次快照 -830,810 | Flip: Primary Flip: 14.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 164 / LOW 91 / INVALID 201
结构观察区: Primary Flip 14.67（全链重定价，覆盖 84%）
Put Wall 17（弱结构｜现价低于该位 0.7%）
最近结构参考: Put Wall 17（现价低于该位 0.7%）
量化视角： 正 Gamma（118万，无历史分位）｜正 Gamma 减弱（83万）｜现价位于 Flip 上方 15.09%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 17（Put Wall，弱结构） / 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 17.0C — Vol 201 | 最新价 $0.30 | OI 517→662 (ΔOI +145张) | ΔOI/Volume 72.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增145张（+28.1% vs前日OI），连续性待观察（方向未知）
10-09 14.5P — Vol 140 | 最新价 $0.23 | OI 32→172 (ΔOI +140张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+437.5% vs前日OI），连续性待观察（方向未知）
10-02 18.0C — Vol 137 | 最新价 $0.39 | OI 333→460 (ΔOI +127张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+38.1% vs前日OI），连续性待观察（方向未知）
10-02 17.5P — Vol 102 | 最新价 $1.19 | OI 13→115 (ΔOI +102张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增102张（+784.6% vs前日OI），连续性待观察（方向未知）
10-02 15.5P — Vol 69 | 最新价 $0.20 | OI 92→160 (ΔOI +68张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增68张（+73.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 582 张（Put 310 / Call 272），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 8.1k / P 4.2k，今日成交量: C 59 / P 38，平值价格ATM: C $0.22 / P $0.25 ｜ ATM IV 119.3%，预期波动 ±2.8%，Max Pain 17
Top ΔOI: C 17 +145 ｜ C 18 -83 ｜ P 16 -25

📆 Forward Expiration Structure

10-02  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +86 / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +0.1k / P -77 ｜ Activity LOW ｜ 21D
10-23  C +7 / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 4.2k / P 1.5k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $0.79 / P $0.67 ｜ ATM IV 67.9%，净 delta 敞口 -5k shares
Top ΔOI: C 18 +127 ｜ P 17 +102 ｜ P 15 +68
仓位参考: Max Pain 18 ｜ Call Wall 18（+6.6%，弱）（OI 0.5k） ｜ Put Wall 16（-5.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 67.9%｜历史 Rank 64%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,122 股

10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（-5.2%，弱）（OI 0.1k）

10-16（Activity LOW）仓位参考: Max Pain 20 ｜ Put Wall 17（+0.7%，弱）（OI 0.7k）

10-23（MEDIUM △）Top ΔOI: 17P +35 ｜ 18P +18
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Call Wall 18（+6.6%，弱）（OI 75） ｜ Put Wall 15.5（-8.2%）（OI 95）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NNE_morning.json