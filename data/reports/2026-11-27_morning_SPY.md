# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $642.15
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-30 727P ΔOI -7,008（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-03 635P ΔOI +10,977 占该期限总 OI 13.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 716.70 → 今开 725.86（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 726.03 ｜ 低 719.62

Options: P/C成交量 1.65 | OI比 0.97 | ATM IV 40.2% | Skew 6.0pp | Term 0.56 | ExpMove ±1.6%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价显著（Skew 6.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.65×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 45% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 45%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-30（3D）±1.6% ｜ 12-01（4D）±2.0% ｜ 12-02（5D）±2.4% ｜ 12-03（6D）±2.6%
   ⇒ IV–VIX Spread: +12.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -468,831,353 | GEX Change vs 上次快照 501,037,403 | Flip: Primary Flip: 729.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3289 / LOW 481 / INVALID 1880
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 729.13（全链重定价，覆盖 95%）
Put Wall 700（弱结构｜现价高于该位 2.9%）
最近结构参考: Flip 729（现价低于该位 1.2%）
量化视角： 负 Gamma（4.69亿，历史分位 45%，中性区）｜负 Gamma 缓解（+5.01亿）｜现价位于 Flip 下方 1.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 717（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 729（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-09 685.0P — Vol 45,534 | 最新价 $5.47 | OI 0→44656 (ΔOI +44656张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44656张（前日OI缺失），连续性待观察（方向未知）
12-09 660.0P — Vol 44,890 | 最新价 $2.70 | OI 0→44596 (ΔOI +44596张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44596张（前日OI缺失），连续性待观察（方向未知）
12-11 660.0P — Vol 46,923 | 最新价 $3.40 | OI 7796→51556 (ΔOI +43760张) | ΔOI/Volume 93.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43760张（+561.3% vs前日OI），连续性待观察（方向未知）
12-11 685.0P — Vol 46,104 | 最新价 $6.34 | OI 1920→45484 (ΔOI +43564张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43564张（+2269.0% vs前日OI），连续性待观察（方向未知）
12-31 775.0C — Vol 37,110 | 最新价 $0.87 | OI 64105→96460 (ΔOI +32355张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32355张（+50.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 208,931 张（Put 176,576 / Call 32,355），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $79M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 583.1k / P 563.9k，今日成交量: C 567.5k / P 937.7k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 40.2%，预期波动 ±0.0%，Max Pain 717
Top ΔOI: P 690 +22,741 ｜ C 725 +13,567 ｜ P 700 +13,563

📆 Forward Expiration Structure

11-30  C +39.4k / P +10.7k ｜ Activity HIGH ｜ 3D
12-01  C +22.1k / P +14.2k ｜ Activity HIGH ｜ 4D
12-02  C +23.5k / P +30.6k ｜ Activity HIGH ｜ 5D
12-03  C +5.3k / P +34.9k ｜ Activity HIGH ｜ 6D

📆 11-30 Forward Structure
存量OI: C 420.2k / P 728.8k，今日变化ΔOI: C +39.4k / P +10.7k，平值价格ATM: C $5.80 / P $5.78 ｜ ATM IV 21.3%，净 delta 敞口 2.7M shares
Top ΔOI: P 727 -7,008 ｜ P 685 -4,148
仓位参考: Max Pain 727 ｜ Call Wall 740（+2.7%，弱）（OI 11.4k） ｜ Put Wall 700（-2.8%，弱）（OI 27.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.3%｜历史 Rank 99%（近端代理）｜IV/RV 0.68×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,749,133 股

📆 12-01 Forward Structure
存量OI: C 85.0k / P 60.1k，今日变化ΔOI: C +22.1k / P +14.2k，平值价格ATM: C $7.41 / P $7.27 ｜ ATM IV 23.6%，净 delta 敞口 719k shares
Top ΔOI: C 724 +3,964 ｜ C 719 +3,584
仓位参考: Max Pain 718 ｜ Call Wall 724（+0.5%，弱）（OI 4.6k） ｜ Put Wall 703（-2.4%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 23.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 719,202 股

📆 12-02 Forward Structure
存量OI: C 67.4k / P 90.0k，今日变化ΔOI: C +23.5k / P +30.6k，平值价格ATM: C $8.89 / P $8.30 ｜ ATM IV 24.4%，净 delta 敞口 995k shares
Top ΔOI: C 715 +8,670
仓位参考: Max Pain 710 ｜ Call Wall 715（-0.7%）（OI 9.0k） ｜ Put Wall 700（-2.8%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜ATM IV 24.4%｜历史 Rank 99%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 994,763 股

📆 12-03 Forward Structure
存量OI: C 27.4k / P 52.9k，今日变化ΔOI: C +5.3k / P +34.9k，平值价格ATM: C $9.57 / P $9.34 ｜ ATM IV 25.1%，净 delta 敞口 -29k shares
Top ΔOI: P 635 +10,977 ｜ P 640 +6,792 ｜ P 630 +3,215
仓位参考: Max Pain 715 ｜ Call Wall 725（+0.7%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 25.1%｜历史 Rank 99%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 28,902 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SPY_morning.json