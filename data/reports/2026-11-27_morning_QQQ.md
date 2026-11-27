# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $642.16
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
🟡 **近现价集中开仓**: 11-30 610P ΔOI +22,894（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 630P ΔOI +15,477 占该期限总 OI 17.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 633.93 → 今开 645.72（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 645.89 ｜ 低 636.72

Options: P/C成交量 1.11 | OI比 0.87 | ATM IV 53.6% | Skew 8.1pp | Term 0.61 | ExpMove ±2.4%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 8.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-30（3D）±2.4% ｜ 12-01（4D）±3.0% ｜ 12-02（5D）±3.5% ｜ 12-03（6D）±4.0%
   ⇒ IV–VIX Spread: +26.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -225,167,399 | GEX Change vs 上次快照 205,146,563 | Flip: Primary Flip: 647.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3434 / LOW 373 / INVALID 2415
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 647.15（全链重定价，覆盖 96%）
最近结构参考: Flip 647（现价低于该位 1.5%）
量化视角： 负 Gamma（2.25亿，历史分位 35%，中性区）｜负 Gamma 缓解（+2.05亿）｜现价位于 Flip 下方 1.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 635（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 647（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 545.0P — Vol 24,284 | 最新价 $1.07 | OI 637→24134 (ΔOI +23497张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23497张（+3688.7% vs前日OI），连续性待观察（方向未知）
12-04 590.0P — Vol 25,752 | 最新价 $4.30 | OI 4629→27998 (ΔOI +23369张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23369张（+504.8% vs前日OI），连续性待观察（方向未知）
11-30 610.0P — Vol 41,532 | 最新价 $3.41 | OI 5006→27900 (ΔOI +22894张) | ΔOI/Volume 55.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22894张（+457.3% vs前日OI），连续性待观察（方向未知）
12-18 580.0P — Vol 28,663 | 最新价 $7.92 | OI 67327→86057 (ΔOI +18730张) | ΔOI/Volume 65.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18730张（+27.8% vs前日OI），连续性待观察（方向未知）
12-18 600.0P — Vol 33,372 | 最新价 $11.79 | OI 68681→84692 (ΔOI +16011张) | ΔOI/Volume 48.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16011张（+23.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 104,501 张（Put 104,501 / Call 0），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $54M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 368.8k / P 320.5k，今日成交量: C 466.7k / P 516.3k，平值价格ATM: C $2.36 / P $3.06 ｜ ATM IV 53.6%，预期波动 ±0.9%，Max Pain 635
Top ΔOI: P 610 +5,578 ｜ C 641 +4,612 ｜ C 650 +3,512

📆 Forward Expiration Structure

11-30  C +51.3k / P +44.7k ｜ Activity HIGH ｜ 3D
12-01  C +10.9k / P +7.8k ｜ Activity HIGH ｜ 4D
12-02  C +7.6k / P +39.6k ｜ Activity HIGH ｜ 5D
12-03  C +11.6k / P +14.9k ｜ Activity HIGH ｜ 6D

📆 11-30 Forward Structure
存量OI: C 410.0k / P 389.4k，今日变化ΔOI: C +51.3k / P +44.7k，平值价格ATM: C $7.53 / P $8.04 ｜ ATM IV 32.4%，净 delta 敞口 2.2M shares
Top ΔOI: P 610 +22,894 ｜ C 675 +13,863 ｜ P 680 -12,556
仓位参考: Max Pain 655 ｜ Call Wall 650（+2.0%，弱）（OI 20.0k） ｜ Put Wall 650（+2.0%，弱）（OI 19.3k）
量化解读： 存量两侧均衡｜ATM IV 32.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.70×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,197,797 股

📆 12-01 Forward Structure
存量OI: C 40.3k / P 53.8k，今日变化ΔOI: C +10.9k / P +7.8k，平值价格ATM: C $9.68 / P $9.65 ｜ ATM IV 35.6%，净 delta 敞口 232k shares
Top ΔOI: C 615 +1,462 ｜ C 655 +922
仓位参考: Max Pain 635 ｜ Call Wall 630（-1.2%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.6%｜历史 Rank 98%（近端代理）｜IV/RV 0.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 232,093 股

📆 12-02 Forward Structure
存量OI: C 28.9k / P 58.9k，今日变化ΔOI: C +7.6k / P +39.6k，平值价格ATM: C $11.27 / P $11.31 ｜ ATM IV 36.9%，净 delta 敞口 -426k shares
Top ΔOI: P 630 +15,477
仓位参考: Max Pain 635 ｜ Call Wall 650（+2.0%）（OI 4.0k） ｜ Put Wall 630（-1.2%）（OI 15.8k）
量化解读： 存量 Put 重｜ATM IV 36.9%｜历史 Rank 98%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 负 426,227 股

📆 12-03 Forward Structure
存量OI: C 25.1k / P 45.3k，今日变化ΔOI: C +11.6k / P +14.9k，平值价格ATM: C $12.57 / P $12.77 ｜ ATM IV 37.5%，净 delta 敞口 211k shares
Top ΔOI: P 535 +6,611 ｜ C 665 +3,967 ｜ C 655 +3,817
仓位参考: Max Pain 638 ｜ Call Wall 655（+2.7%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 37.5%｜历史 Rank 98%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 211,217 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/QQQ_morning.json