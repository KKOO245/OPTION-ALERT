# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $766.83 ｜ QQQ $740.72
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
🟡 **近现价集中开仓**: 09-28 787C ΔOI +14,937（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-01 665P ΔOI +8,931 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 767.18 → 今开 768.78（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 770.31 ｜ 低 766.29

Options: P/C成交量 0.67 | OI比 1.83 | ATM IV 17.1% | Skew 1.9pp | Term 0.73 | ExpMove ±0.7%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.83×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 57% ｜ P/C OI(近端) 50%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 57%）｜近端持仓结构中性（P/C OI 分位 50%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-28（3D）±0.7% ｜ 09-29（4D）±0.8% ｜ 09-30（5D）±1.0% ｜ 10-01（6D）±1.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 34,194,944 | GEX Change vs 上次快照 228,830,648 | Flip: Primary Flip: 768.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2942 / LOW 422 / INVALID 1748
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.62（全链重定价，覆盖 96%）
Call Wall 785（现价低于该位 2.1%）
最近结构参考: Flip 769（现价高于该位 0.0%）
量化视角： 正 Gamma（3419万，历史分位 57%，中性区）｜由负转正（+2.29亿）｜现价位于 Flip 上方 0.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 766（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 649.0P — Vol 52,516 | 最新价 $0.02 | OI 29718→60521 (ΔOI +30803张) | ΔOI/Volume 58.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30803张（+103.7% vs前日OI），连续性待观察（方向未知）
09-30 648.0P — Vol 45,492 | 最新价 $0.02 | OI 30327→56034 (ΔOI +25707张) | ΔOI/Volume 56.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25707张（+84.8% vs前日OI），连续性待观察（方向未知）
09-30 646.0P — Vol 25,610 | 最新价 $0.02 | OI 451→25625 (ΔOI +25174张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25174张（+5581.8% vs前日OI），连续性待观察（方向未知）
10-16 730.0P — Vol 47,150 | 最新价 $1.87 | OI 43786→67444 (ΔOI +23658张) | ΔOI/Volume 50.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23658张（+54.0% vs前日OI），连续性待观察（方向未知）
09-25 764.0P — Vol 80,263 | 最新价 $1.14 | OI 3209→18261 (ΔOI +15052张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15052张（+469.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 120,394 张（Put 120,394 / Call 0），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 418.5k / P 767.8k，今日成交量: C 819.7k / P 550.9k，平值价格ATM: C $0.83 / P $2.23 ｜ ATM IV 17.1%，预期波动 ±0.4%，Max Pain 766
Top ΔOI: P 764 +15,052 ｜ C 780 +13,301 ｜ C 775 +11,958

📆 Forward Expiration Structure

09-28  C +39.8k / P +31.3k ｜ Activity HIGH ｜ 3D
09-29  C +11.4k / P +12.6k ｜ Activity HIGH ｜ 4D
09-30  C +61.4k / P +139.2k ｜ Activity HIGH ｜ 5D
10-01  C +14.7k / P +21.0k ｜ Activity HIGH ｜ 6D

📆 09-28 Forward Structure
存量OI: C 105.3k / P 114.2k，今日变化ΔOI: C +39.8k / P +31.3k，平值价格ATM: C $1.93 / P $3.22 ｜ ATM IV 8.6%，净 delta 敞口 272k shares
Top ΔOI: C 787 +14,937 ｜ P 763 +4,242 ｜ P 757 +4,039
仓位参考: Max Pain 767 ｜ Call Wall 787（+2.4%，弱）（OI 16.2k） ｜ Put Wall 760（-1.1%，弱）（OI 6.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 8.6%｜历史 Rank 75%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 271,605 股

📆 09-29 Forward Structure
存量OI: C 47.6k / P 88.0k，今日变化ΔOI: C +11.4k / P +12.6k，平值价格ATM: C $2.70 / P $3.85 ｜ ATM IV 9.6%，净 delta 敞口 9k shares
Top ΔOI: P 763 +2,023 ｜ C 782 +1,213 ｜ P 747 +1,211
仓位参考: Max Pain 765 ｜ Call Wall 783（+1.9%，弱）（OI 2.2k） ｜ Put Wall 763（-0.7%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 9.6%｜历史 Rank 75%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 8,746 股

📆 09-30 Forward Structure
存量OI: C 560.5k / P 1796.8k，今日变化ΔOI: C +61.4k / P +139.2k，平值价格ATM: C $3.41 / P $4.50 ｜ ATM IV 10.6%，净 delta 敞口 237k shares
Top ΔOI: P 649 +30,803 ｜ P 648 +25,707 ｜ P 646 +25,174
仓位参考: Max Pain 761 ｜ Call Wall 786（+2.2%，弱）（OI 22.1k）
量化解读： 存量 Put 重｜ATM IV 10.6%｜历史 Rank 75%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 236,669 股

📆 10-01 Forward Structure
存量OI: C 34.3k / P 53.1k，今日变化ΔOI: C +14.7k / P +21.0k，平值价格ATM: C $4.02 / P $4.81 ｜ ATM IV 11.0%，净 delta 敞口 399k shares
Top ΔOI: P 741 +1,966 ｜ P 715 +1,026
仓位参考: Max Pain 766 ｜ Call Wall 780（+1.5%，弱）（OI 1.6k） ｜ Put Wall 770（+0.2%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 11.0%｜历史 Rank 75%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 398,809 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SPY_morning.json