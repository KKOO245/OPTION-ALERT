# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 700P ΔOI +1,307（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 715.34 → 今开 697.13（-2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 698.63 ｜ 低 694.05

Options: P/C成交量 0.80 | OI比 1.70 | ATM IV 33.9% | Skew 0.9pp | Term 0.67 | ExpMove ±1.4%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.70×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 2% ｜ P/C OI(近端) 56%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 2%）｜近端持仓结构中性（P/C OI 分位 56%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-02（3D）±1.4% ｜ 11-03（4D）±1.9% ｜ 11-04（5D）±2.4% ｜ 11-05（6D）±2.7%
   ⇒ IV–VIX Spread: +15.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,286,683,870 | GEX Change vs 上次快照 -656,291,104 | Flip: Primary Flip: 721.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2522 / LOW 300 / INVALID 1010
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 721.75（全链重定价，覆盖 94%）
Put Wall 680（弱结构｜现价高于该位 2.5%）
最近结构参考: Put Wall 680（现价高于该位 2.5%）
量化视角： 负 Gamma（12.87亿，历史分位偏负区，比 98% 的交易日更负）｜负 Gamma 加深（6.56亿）｜现价位于 Flip 下方 3.41%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 680（Put Wall，弱结构）；上方 716（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 722（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 723.0C — Vol 38,907 | 最新价 $0.19 | OI 1627→28029 (ΔOI +26402张) | ΔOI/Volume 67.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26402张（+1622.7% vs前日OI），连续性待观察（方向未知）
10-30 705.0P — Vol 64,573 | 最新价 $3.87 | OI 18002→44388 (ΔOI +26386张) | ΔOI/Volume 40.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26386张（+146.6% vs前日OI），连续性待观察（方向未知）
10-30 727.0C — Vol 34,667 | 最新价 $0.06 | OI 2891→28900 (ΔOI +26009张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26009张（+899.6% vs前日OI），连续性待观察（方向未知）
10-30 700.0P — Vol 92,089 | 最新价 $2.24 | OI 42068→60245 (ΔOI +18177张) | ΔOI/Volume 19.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18177张（+43.2% vs前日OI），连续性待观察（方向未知）
11-02 555.0P — Vol 7,586 | 最新价 $0.01 | OI 10→7167 (ΔOI +7157张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7157张（+71570.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 104,131 张（Put 51,720 / Call 52,411），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $14M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 499.9k / P 850.3k，今日成交量: C 529.6k / P 421.2k，平值价格ATM: C $2.88 / P $2.26 ｜ ATM IV 33.9%，预期波动 ±0.7%，Max Pain 716
Top ΔOI: C 723 +26,402 ｜ P 705 +26,386 ｜ C 727 +26,009

📆 Forward Expiration Structure

11-02  C +23.7k / P +50.8k ｜ Activity HIGH ｜ 3D
11-03  C +6.6k / P +39.1k ｜ Activity HIGH ｜ 4D
11-04  C +5.8k / P +8.9k ｜ Activity HIGH ｜ 5D
11-05  C +3.3k / P +4.9k ｜ Activity HIGH ｜ 6D

📆 11-02 Forward Structure
存量OI: C 71.5k / P 116.4k，今日变化ΔOI: C +23.7k / P +50.8k，平值价格ATM: C $5.37 / P $4.70 ｜ ATM IV 18.9%，净 delta 敞口 -625k shares
仓位参考: Max Pain 715 ｜ Put Wall 695（-0.3%，弱）（OI 8.7k）
量化解读： 存量 Put 重｜ATM IV 18.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 625,432 股

📆 11-03 Forward Structure
存量OI: C 29.7k / P 91.6k，今日变化ΔOI: C +6.6k / P +39.1k，平值价格ATM: C $7.01 / P $6.27 ｜ ATM IV 21.5%，净 delta 敞口 -262k shares
Top ΔOI: P 625 +6,041 ｜ P 640 +4,329 ｜ P 635 +3,739
仓位参考: Max Pain 713 ｜ Call Wall 710（+1.8%）（OI 2.7k） ｜ Put Wall 680（-2.5%）（OI 17.2k）
量化解读： 存量 Put 重｜ATM IV 21.5%｜历史 Rank 94%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 261,870 股

📆 11-04 Forward Structure
存量OI: C 22.5k / P 38.2k，今日变化ΔOI: C +5.8k / P +8.9k，平值价格ATM: C $8.72 / P $7.78 ｜ ATM IV 24.1%，净 delta 敞口 -176k shares
Top ΔOI: P 700 +1,307 ｜ P 710 +1,040 ｜ P 635 +1,021
仓位参考: Max Pain 718 ｜ Call Wall 710（+1.8%，弱）（OI 0.6k） ｜ Put Wall 700（+0.4%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜ATM IV 24.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 176,016 股

📆 11-05 Forward Structure
存量OI: C 14.5k / P 14.9k，今日变化ΔOI: C +3.3k / P +4.9k，平值价格ATM: C $10.78 / P $7.79 ｜ ATM IV 25.1%，净 delta 敞口 -138k shares
Top ΔOI: P 695 +886 ｜ C 730 +803 ｜ P 700 +768
仓位参考: Max Pain 710 ｜ Call Wall 710（+1.8%）（OI 2.6k） ｜ Put Wall 685（-1.7%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 25.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 负 138,064 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/QQQ_morning.json