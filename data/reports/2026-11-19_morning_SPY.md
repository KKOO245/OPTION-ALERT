# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 757P ΔOI -19,395（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 730.20 → 今开 737.46（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 739.90 ｜ 低 732.19

Options: P/C成交量 0.84 | OI比 1.15 | ATM IV 36.4% | Skew 3.7pp | Term 0.51 | ExpMove ±1.3%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.51，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 26% ｜ P/C OI(近端) 5%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 26%）｜近端持仓极端 Call 重（P/C OI 分位 5%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-20（1D）±1.3% ｜ 11-23（4D）±1.7% ｜ 11-24（5D）±1.9% ｜ 11-25（6D）±2.2%
   ⇒ IV–VIX Spread: +13.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,355,164,719 | GEX Change vs 上次快照 725,461,427 | Flip: Primary Flip: 748.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2890 / LOW 332 / INVALID 1714
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 748.03（全链重定价，覆盖 95%）
最近结构参考: Flip 748（现价低于该位 1.5%）
量化视角： 负 Gamma（13.55亿，历史分位 26%，中性区）｜负 Gamma 缓解（+7.25亿）｜现价位于 Flip 下方 1.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 733（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 748（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 725.0C — Vol 62,614 | 最新价 $9.12 | OI 2763→14700 (ΔOI +11937张) | ΔOI/Volume 19.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11937张（+432.0% vs前日OI），连续性待观察（方向未知）
11-19 700.0P — Vol 23,534 | 最新价 $0.08 | OI 2577→13706 (ΔOI +11129张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11129张（+431.9% vs前日OI），连续性待观察（方向未知）
11-20 715.0P — Vol 28,193 | 最新价 $1.46 | OI 37530→46762 (ΔOI +9232张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9232张（+24.6% vs前日OI），连续性待观察（方向未知）
12-18 500.0P — Vol 10,143 | 最新价 $0.40 | OI 21455→29554 (ΔOI +8099张) | ΔOI/Volume 79.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8099张（+37.8% vs前日OI），连续性待观察（方向未知）
11-27 727.0P — Vol 64,749 | 最新价 $8.00 | OI 347→8346 (ΔOI +7999张) | ΔOI/Volume 12.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7999张（+2305.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,396 张（Put 36,459 / Call 11,937），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 178.6k / P 204.7k，今日成交量: C 653.9k / P 546.8k，平值价格ATM: C $3.12 / P $2.66 ｜ ATM IV 36.4%，预期波动 ±0.8%，Max Pain 733
Top ΔOI: P 700 +11,129 ｜ P 707 -7,821 ｜ C 731 +4,570

📆 Forward Expiration Structure

11-20  C +49.1k / P -90.4k ｜ Activity HIGH ｜ 1D
11-23  C +24.1k / P +14.0k ｜ Activity HIGH ｜ 4D
11-24  C +15.6k / P +10.7k ｜ Activity HIGH ｜ 5D
11-25  C +11.9k / P +8.6k ｜ Activity HIGH ｜ 6D

📆 11-20 Forward Structure
存量OI: C 1035.2k / P 2849.2k，今日变化ΔOI: C +49.1k / P -90.4k，平值价格ATM: C $5.00 / P $4.45 ｜ ATM IV 27.1%，净 delta 敞口 12.2M shares
Top ΔOI: P 757 -19,395 ｜ P 760 -13,991 ｜ P 755 -12,809
仓位参考: Max Pain 745 ｜ Call Wall 750（+1.8%，弱）（OI 37.4k） ｜ Put Wall 725（-1.6%，弱）（OI 71.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 27.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,238,149 股

📆 11-23 Forward Structure
存量OI: C 93.1k / P 71.0k，今日变化ΔOI: C +24.1k / P +14.0k，平值价格ATM: C $6.55 / P $5.94 ｜ ATM IV 19.5%，净 delta 敞口 668k shares
Top ΔOI: P 709 +7,967 ｜ C 750 +3,272 ｜ C 791 +2,006
仓位参考: Max Pain 738 ｜ Call Wall 750（+1.8%，弱）（OI 4.4k） ｜ Put Wall 728（-1.2%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 19.5%｜历史 Rank 98%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 667,550 股

📆 11-24 Forward Structure
存量OI: C 52.5k / P 45.5k，今日变化ΔOI: C +15.6k / P +10.7k，平值价格ATM: C $7.50 / P $6.70 ｜ ATM IV 20.2%，净 delta 敞口 -23k shares
Top ΔOI: P 740 +6,813 ｜ C 758 +1,904 ｜ C 765 +1,004
仓位参考: Max Pain 740 ｜ Call Wall 754（+2.4%，弱）（OI 2.4k） ｜ Put Wall 740（+0.5%）（OI 8.2k）
量化解读： 存量两侧均衡｜ATM IV 20.2%｜历史 Rank 98%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 负 22,639 股

📆 11-25 Forward Structure
存量OI: C 47.9k / P 39.6k，今日变化ΔOI: C +11.9k / P +8.6k，平值价格ATM: C $8.41 / P $7.58 ｜ ATM IV 20.6%，净 delta 敞口 217k shares
Top ΔOI: C 750 +1,029 ｜ P 670 +994 ｜ P 680 +871
仓位参考: Max Pain 740 ｜ Call Wall 749（+1.7%）（OI 3.9k） ｜ Put Wall 726（-1.4%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 20.6%｜历史 Rank 98%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 217,288 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SPY_morning.json