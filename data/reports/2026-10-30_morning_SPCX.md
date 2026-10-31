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
🟡 **近现价集中开仓**: 11-04 140P ΔOI +1,866（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 143.89 → 今开 137.82（-4.2%） | 较昨收变动（含盘初走势） ｜ 今日高 138.99 ｜ 低 135.91

Options: P/C成交量 0.51 | OI比 0.67 | ATM IV 74.6% | Skew 3.1pp | Term 0.67 | ExpMove ±3.1%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±3.1% ｜ 11-04（5D）±5.1% ｜ 11-06（7D）±6.0% ｜ 11-09（10D）±6.6%
   ⇒ IV–VIX Spread: +55.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -75,231,747 | GEX Change vs 上次快照 -19,207,766 | Flip: Primary Flip: 144.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 750 / LOW 157 / INVALID 621
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 144.15（全链重定价，覆盖 99%）
Put Wall 140（弱结构｜现价低于该位 1.1%）
最近结构参考: Put Wall 140（现价低于该位 1.1%）
量化视角： 负 Gamma（7523万，无历史分位）｜负 Gamma 加深（1921万）｜现价位于 Flip 下方 3.92%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 140（Put Wall，弱结构） / 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 165.0C — Vol 10,335 | 最新价 $0.80 | OI 5565→15117 (ΔOI +9552张) | ΔOI/Volume 92.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9552张（+171.6% vs前日OI），连续性待观察（方向未知）
11-13 160.0C — Vol 6,730 | 最新价 $1.25 | OI 2368→7104 (ΔOI +4736张) | ΔOI/Volume 70.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4736张（+200.0% vs前日OI），连续性待观察（方向未知）
11-06 144.0P — Vol 4,766 | 最新价 $4.30 | OI 4665→8325 (ΔOI +3660张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3660张（+78.5% vs前日OI），连续性待观察（方向未知）
11-06 140.0P — Vol 6,313 | 最新价 $2.59 | OI 11823→14776 (ΔOI +2953张) | ΔOI/Volume 46.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2953张（+25.0% vs前日OI），连续性待观察（方向未知）
11-06 135.0P — Vol 5,591 | 最新价 $1.20 | OI 7872→10615 (ΔOI +2743张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2743张（+34.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,644 张（Put 9,356 / Call 14,288），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 289.9k / P 193.1k，今日成交量: C 64.4k / P 32.9k，平值价格ATM: C $1.55 / P $0.77 ｜ ATM IV 74.6%，预期波动 ±1.7%，Max Pain 148
Top ΔOI: C 160 -4,496 ｜ P 155 -3,261 ｜ P 150 -3,054

📆 Forward Expiration Structure

11-02  C +7.1k / P +1.6k ｜ Activity HIGH ｜ 3D
11-04  C +2.8k / P +4.3k ｜ Activity HIGH ｜ 5D
11-06  C +10.2k / P +17.8k ｜ Activity HIGH ｜ 7D
11-09  C +1.1k / P +0.6k ｜ Activity HIGH ｜ 10D

📆 11-02 Forward Structure
存量OI: C 34.4k / P 17.3k，今日变化ΔOI: C +7.1k / P +1.6k，平值价格ATM: C $2.55 / P $1.72 ｜ ATM IV 39.8%，净 delta 敞口 152 shares
Top ΔOI: C 147 +601
仓位参考: Max Pain 145 ｜ Call Wall 150（+8.3%，弱）（OI 3.1k） ｜ Put Wall 145（+4.7%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 39.8%｜历史 Rank 90%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 152 股

📆 11-04 Forward Structure
存量OI: C 13.5k / P 11.7k，今日变化ΔOI: C +2.8k / P +4.3k，平值价格ATM: C $3.90 / P $3.20 ｜ ATM IV 51.5%，净 delta 敞口 -157k shares
Top ΔOI: P 140 +1,866 ｜ C 145 +1,358 ｜ C 150 +613
仓位参考: Max Pain 146 ｜ Call Wall 150（+8.3%，弱）（OI 1.6k） ｜ Put Wall 140（+1.1%）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.5%｜历史 Rank 90%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 157,204 股

📆 11-06 Forward Structure
存量OI: C 138.0k / P 100.7k，今日变化ΔOI: C +10.2k / P +17.8k，平值价格ATM: C $4.45 / P $3.80 ｜ ATM IV 53.7%，净 delta 敞口 -559k shares
Top ΔOI: P 144 +3,660 ｜ P 140 +2,953 ｜ P 135 +2,743
仓位参考: Max Pain 148 ｜ Call Wall 150（+8.3%，弱）（OI 9.4k） ｜ Put Wall 140（+1.1%，弱）（OI 14.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.7%｜历史 Rank 90%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 559,017 股

📆 11-09 Forward Structure
存量OI: C 4.0k / P 2.5k，今日变化ΔOI: C +1.1k / P +0.6k，平值价格ATM: C $4.80 / P $4.40 ｜ ATM IV 50.2%，净 delta 敞口 -7k shares
Top ΔOI: C 145 +411 ｜ P 135 +175
仓位参考: Max Pain 144 ｜ Call Wall 145（+4.7%，弱）（OI 0.6k） ｜ Put Wall 134（-3.2%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 50.2%｜历史 Rank 90%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 负 6,567 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SPCX_morning.json