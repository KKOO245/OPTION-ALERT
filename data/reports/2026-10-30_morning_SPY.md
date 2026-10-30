# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $756.16 ｜ QQQ $690.49
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
🟡 **近现价集中开仓**: 11-02 775P ΔOI +9,353（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-03 665P ΔOI +19,139 占该期限总 OI 14.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 769.36 → 今开 761.38（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 761.46 ｜ 低 758.23

Options: P/C成交量 1.26 | OI比 2.24 | ATM IV 21.4% | Skew 1.0pp | Term 0.68 | ExpMove ±0.9%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜当日成交偏 Put（P/C量 1.26）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 18% ｜ P/C OI(近端) 77%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 18%）｜近端持仓结构中性（P/C OI 分位 77%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-02（3D）±0.9% ｜ 11-03（4D）±1.1% ｜ 11-04（5D）±1.4% ｜ 11-05（6D）±1.5%
   ⇒ IV–VIX Spread: +2.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,876,412,591 | GEX Change vs 上次快照 -1,208,933,907 | Flip: Primary Flip: 772.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 2593 / LOW 401 / INVALID 1206
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 772.38（全链重定价，覆盖 90%）
最近结构参考: Flip 772（现价低于该位 1.6%）
量化视角： 负 Gamma（18.76亿，历史分位偏负区，比 82% 的交易日更负）｜负 Gamma 加深（12.09亿）｜现价位于 Flip 下方 1.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 765（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 772（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 757.0P — Vol 37,382 | 最新价 $6.92 | OI 1881→37286 (ΔOI +35405张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35405张（+1882.2% vs前日OI），连续性待观察（方向未知）
11-20 725.0P — Vol 38,063 | 最新价 $2.33 | OI 75626→108209 (ΔOI +32583张) | ΔOI/Volume 85.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32583张（+43.1% vs前日OI），连续性待观察（方向未知）
11-20 730.0P — Vol 28,911 | 最新价 $2.70 | OI 58867→84381 (ΔOI +25514张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25514张（+43.3% vs前日OI），连续性待观察（方向未知）
11-03 665.0P — Vol 19,431 | 最新价 $0.02 | OI 292→19431 (ΔOI +19139张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19139张（+6554.4% vs前日OI），连续性待观察（方向未知）
10-30 775.0C — Vol 57,193 | 最新价 $0.13 | OI 14149→25133 (ΔOI +10984张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10984张（+77.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 123,625 张（Put 112,641 / Call 10,984），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $39M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 760.3k / P 1702.0k，今日成交量: C 434.5k / P 546.3k，平值价格ATM: C $1.94 / P $1.56 ｜ ATM IV 21.4%，预期波动 ±0.5%，Max Pain 765
Top ΔOI: C 775 +10,984 ｜ C 774 +9,444 ｜ P 769 +9,113

📆 Forward Expiration Structure

11-02  C +29.9k / P +38.5k ｜ Activity HIGH ｜ 3D
11-03  C +16.9k / P +38.4k ｜ Activity HIGH ｜ 4D
11-04  C +22.6k / P +19.5k ｜ Activity HIGH ｜ 5D
11-05  C +5.8k / P +7.6k ｜ Activity HIGH ｜ 6D

📆 11-02 Forward Structure
存量OI: C 68.4k / P 115.1k，今日变化ΔOI: C +29.9k / P +38.5k，平值价格ATM: C $3.55 / P $3.03 ｜ ATM IV 11.3%，净 delta 敞口 -1.6M shares
Top ΔOI: P 775 +9,353 ｜ C 774 +4,353 ｜ P 757 +2,872
仓位参考: Max Pain 772 ｜ Call Wall 774（+1.8%，弱）（OI 4.8k） ｜ Put Wall 775（+1.9%）（OI 15.3k）
量化解读： 存量 Put 重｜ATM IV 11.3%｜历史 Rank 88%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,554,097 股

📆 11-03 Forward Structure
存量OI: C 43.3k / P 87.4k，今日变化ΔOI: C +16.9k / P +38.4k，平值价格ATM: C $4.50 / P $3.89 ｜ ATM IV 12.5%，净 delta 敞口 -371k shares
Top ΔOI: P 740 +5,519 ｜ P 754 +2,292
仓位参考: Max Pain 769 ｜ Call Wall 780（+2.6%，弱）（OI 3.2k） ｜ Put Wall 740（-2.7%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 12.5%｜历史 Rank 88%（近端代理）｜IV/RV 1.39×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 371,262 股

📆 11-04 Forward Structure
存量OI: C 39.3k / P 86.1k，今日变化ΔOI: C +22.6k / P +19.5k，平值价格ATM: C $5.58 / P $4.85 ｜ ATM IV 14.2%，净 delta 敞口 -707k shares
Top ΔOI: P 767 +7,215 ｜ P 755 +4,047 ｜ C 776 +3,740
仓位参考: Max Pain 769 ｜ Call Wall 776（+2.1%，弱）（OI 4.0k） ｜ Put Wall 767（+0.9%）（OI 37.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.2%｜历史 Rank 88%（近端代理）｜IV/RV 1.58×（近似）｜净 delta 敞口 负 707,260 股

📆 11-05 Forward Structure
存量OI: C 23.7k / P 17.4k，今日变化ΔOI: C +5.8k / P +7.6k，平值价格ATM: C $6.25 / P $5.40 ｜ ATM IV 14.6%，净 delta 敞口 -110k shares
Top ΔOI: C 790 +1,748 ｜ P 710 +1,480 ｜ P 740 +1,444
仓位参考: Max Pain 765 ｜ Call Wall 780（+2.6%）（OI 10.4k） ｜ Put Wall 760（-0.0%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 14.6%｜历史 Rank 88%（近端代理）｜IV/RV 1.62×（近似）｜净 delta 敞口 负 109,750 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SPY_morning.json