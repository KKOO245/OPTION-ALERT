# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.05 ｜ QQQ $706.83
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 148P ΔOI -3,008（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 144.75 → 今开 147.93（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 148.59 ｜ 低 144.09

Options: P/C成交量 0.55 | OI比 0.86 | ATM IV 94.6% | Skew 0.4pp | Term 0.57 | ExpMove ±3.8%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-26（3D）±3.8% ｜ 10-28（5D）±5.4% ｜ 10-30（7D）±6.5% ｜ 11-02（10D）±8.5%
   ⇒ IV–VIX Spread: +74.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,803,649 | GEX Change vs 上次快照 60,560,609 | Flip: Primary Flip: 149.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 838 / LOW 125 / INVALID 513
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 149.41（全链重定价，覆盖 96%）
Put Wall 140（弱结构｜现价高于该位 5.8%） | Call Wall 160（弱结构｜现价低于该位 7.4%）
最近结构参考: Flip 149（现价低于该位 0.9%）
量化视角： 负 Gamma（1880万，无历史分位）｜负 Gamma 缓解（+6056万）｜现价位于 Flip 下方 0.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 135.0P — Vol 21,839 | 最新价 $4.90 | OI 15182→31953 (ΔOI +16771张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16771张（+110.5% vs前日OI），连续性待观察（方向未知）
10-23 160.0C — Vol 68,640 | 最新价 $0.07 | OI 13375→25723 (ΔOI +12348张) | ΔOI/Volume 18.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12348张（+92.3% vs前日OI），连续性待观察（方向未知）
11-20 130.0P — Vol 19,968 | 最新价 $3.25 | OI 25400→34492 (ΔOI +9092张) | ΔOI/Volume 45.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9092张（+35.8% vs前日OI），连续性待观察（方向未知）
10-23 155.0C — Vol 53,765 | 最新价 $0.19 | OI 9140→17076 (ΔOI +7936张) | ΔOI/Volume 14.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7936张（+86.8% vs前日OI），连续性待观察（方向未知）
10-26 140.0P — Vol 13,679 | 最新价 $1.50 | OI 794→8613 (ΔOI +7819张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7819张（+984.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 53,966 张（Put 33,682 / Call 20,284），跨 3 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 255.1k / P 220.5k，今日成交量: C 100.1k / P 54.8k，平值价格ATM: C $1.59 / P $1.44 ｜ ATM IV 94.6%，预期波动 ±2.0%，Max Pain 150
Top ΔOI: C 160 +12,348 ｜ C 155 +7,936 ｜ C 152 +7,571

📆 Forward Expiration Structure

10-26  C +16.8k / P +17.9k ｜ Activity HIGH ｜ 3D
10-28  C +8.2k / P -1.1k ｜ Activity HIGH ｜ 5D
10-30  C +14.8k / P +8.4k ｜ Activity HIGH ｜ 7D
11-02  C +3.8k / P +0.9k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 41.7k / P 44.3k，今日变化ΔOI: C +16.8k / P +17.9k，平值价格ATM: C $2.92 / P $2.75 ｜ ATM IV 49.7%，净 delta 敞口 378k shares
Top ΔOI: P 140 +7,819 ｜ C 160 +4,455 ｜ P 138 +4,000
仓位参考: Max Pain 152 ｜ Call Wall 160（+8.0%，弱）（OI 6.3k） ｜ Put Wall 140（-5.5%）（OI 8.6k）
量化解读： 存量两侧均衡｜ATM IV 49.7%｜历史 Rank 96%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 377,934 股

📆 10-28 Forward Structure
存量OI: C 17.8k / P 20.1k，今日变化ΔOI: C +8.2k / P -1.1k，平值价格ATM: C $4.15 / P $3.90 ｜ ATM IV 55.4%，净 delta 敞口 523k shares
Top ΔOI: P 148 -3,008 ｜ P 160 -2,887 ｜ C 155 +1,507
仓位参考: Max Pain 155 ｜ Call Wall 160（+8.0%，弱）（OI 2.2k） ｜ Put Wall 160（+8.0%）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 55.4%｜历史 Rank 96%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 522,841 股

📆 10-30 Forward Structure
存量OI: C 166.3k / P 137.2k，今日变化ΔOI: C +14.8k / P +8.4k，平值价格ATM: C $4.90 / P $4.70 ｜ ATM IV 56.9%，净 delta 敞口 279k shares
Top ΔOI: C 155 +3,822 ｜ C 157 +3,706 ｜ P 144 +3,277
仓位参考: Max Pain 155 ｜ Call Wall 160（+8.0%，弱）（OI 10.3k） ｜ Put Wall 150（+1.3%）（OI 14.6k）
量化解读： 存量 Call 重｜ATM IV 56.9%｜历史 Rank 96%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 278,731 股

📆 11-02 Forward Structure
存量OI: C 8.9k / P 5.0k，今日变化ΔOI: C +3.8k / P +0.9k，平值价格ATM: C $4.90 / P $7.75 ｜ ATM IV 53.0%，净 delta 敞口 81k shares
Top ΔOI: C 155 +643 ｜ C 150 +544
仓位参考: Max Pain 150 ｜ Call Wall 160（+8.0%）（OI 1.3k） ｜ Put Wall 155（+4.7%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 53.0%｜历史 Rank 96%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 81,140 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SPCX_morning.json