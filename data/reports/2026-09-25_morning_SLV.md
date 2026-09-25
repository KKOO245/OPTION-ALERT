# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.56
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
🟡 **近现价集中开仓**: 09-28 56P ΔOI +1,143（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 57.62 → 今开 57.80（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 57.94 ｜ 低 57.25

Options: P/C成交量 0.54 | OI比 0.33 | ATM IV 38.1% | Skew -2.4pp | Term 0.87 | ExpMove ±1.9%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-28（3D）±1.9% ｜ 09-30（5D）±3.0% ｜ 10-02（7D）±3.7% ｜ 10-05（10D）±4.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 70,699,114 | GEX Change vs 上次快照 31,661,898 | Flip: Primary Flip: 56.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 735 / LOW 225 / INVALID 302
结构观察区: Primary Flip 56.00（全链重定价，覆盖 94%）
Put Wall 60（弱结构｜现价低于该位 4.1%）
最近结构参考: Flip 56（现价高于该位 2.8%）
量化视角： 正 Gamma（7070万，无历史分位）｜正 Gamma 增强（+3166万）｜现价位于 Flip 上方 2.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 60（Put Wall，弱结构） / 58（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 75.0C — Vol 15,052 | 最新价 $0.01 | OI 3740→17990 (ΔOI +14250张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14250张（+381.0% vs前日OI），连续性待观察（方向未知）
10-02 59.0C — Vol 5,034 | 最新价 $0.62 | OI 955→5145 (ΔOI +4190张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4190张（+438.7% vs前日OI），连续性待观察（方向未知）
09-25 59.0C — Vol 6,334 | 最新价 $0.07 | OI 2373→5535 (ΔOI +3162张) | ΔOI/Volume 49.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3162张（+133.2% vs前日OI），连续性待观察（方向未知）
09-25 59.5C — Vol 3,572 | 最新价 $0.04 | OI 1354→4042 (ΔOI +2688张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2688张（+198.5% vs前日OI），连续性待观察（方向未知）
09-25 58.0C — Vol 9,173 | 最新价 $0.27 | OI 1529→4140 (ΔOI +2611张) | ΔOI/Volume 28.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2611张（+170.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,901 张（Put 0 / Call 26,901），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 134.3k / P 44.0k，今日成交量: C 9.4k / P 5.1k，平值价格ATM: C $0.18 / P $0.31 ｜ ATM IV 38.1%，预期波动 ±0.9%，Max Pain 58
Top ΔOI: P 60 -4,082 ｜ C 59 +3,162 ｜ C 59 +2,688

📆 Forward Expiration Structure

09-28  C +3.4k / P +2.2k ｜ Activity HIGH ｜ 3D
09-30  C +15.8k / P -6.6k ｜ Activity MEDIUM △ ｜ 5D
10-02  C +8.2k / P +1.6k ｜ Activity MEDIUM △ ｜ 7D
10-05  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 10D

📆 09-28 Forward Structure
存量OI: C 15.6k / P 11.1k，今日变化ΔOI: C +3.4k / P +2.2k，平值价格ATM: C $0.65 / P $0.46 ｜ ATM IV 23.1%，净 delta 敞口 54k shares
Top ΔOI: P 56 +1,143 ｜ C 58 +1,054 ｜ P 55 +711
仓位参考: Max Pain 58 ｜ Call Wall 62.5（+8.6%，弱）（OI 2.3k） ｜ Put Wall 56（-2.7%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 23.1%｜历史 Rank 62%（近端代理）｜IV/RV 0.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 54,378 股

09-30（MEDIUM △）Top ΔOI: 70P -2,737 ｜ 70P -2,220
09-30（MEDIUM △）仓位参考: Max Pain 57 ｜ Call Wall 60（+4.3%，弱）（OI 5.9k） ｜ Put Wall 53（-7.9%）（OI 13.4k）

10-02（MEDIUM △）Top ΔOI: 59C +4,190 ｜ 58C +2,424
10-02（MEDIUM △）仓位参考: Max Pain 58 ｜ Call Wall 60（+4.3%，弱）（OI 11.9k） ｜ Put Wall 56（-2.7%，弱）（OI 4.0k）

10-05（MEDIUM △）Top ΔOI: 53P +68 ｜ 57P +65
10-05（MEDIUM △）仓位参考: Max Pain 60 ｜ Call Wall 60（+4.3%，弱）（OI 0.2k） ｜ Put Wall 59.5（+3.4%）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SLV_morning.json