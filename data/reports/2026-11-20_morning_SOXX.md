# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $709.01 ｜ QQQ $630.00
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 136.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 137.95 → 今开 135.10（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 135.20 ｜ 低 130.30

Options: P/C成交量 2.00 | OI比 1.46 | ATM IV 80.6% | Skew -45.1pp | Term 0.78 | ExpMove ±3.1% | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -45.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.00）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.00×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.46×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ IV–VIX Spread: +53.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -43,548,992 | GEX Change vs 上次快照 nan | Flip: Candidates 136.15 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: VALID 575 / LOW 917 / INVALID 289
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈136（全链重定价，覆盖待盘点，CONDITIONAL）
最近结构参考: Flip 136（现价低于该位 3.6%）
量化视角： 负 Gamma（4355万，无历史分位）｜GEX 变化（nan万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 167（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 136（全链重定价，覆盖待盘点）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 150.0P — Vol 13,300 | 最新价 $15.55 | OI 19019→22417 (ΔOI +3398张) | ΔOI/Volume 25.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3398张（+17.9% vs前日OI），连续性待观察（方向未知）
12-18 160.0C — Vol 2,037 | 最新价 $2.00 | OI 4598→6378 (ΔOI +1780张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1780张（+38.7% vs前日OI），连续性待观察（方向未知）
12-18 140.0P — Vol 10,151 | 最新价 $10.02 | OI 10102→11750 (ΔOI +1648张) | ΔOI/Volume 16.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1648张（+16.3% vs前日OI），连续性待观察（方向未知）
12-18 130.0P — Vol 7,956 | 最新价 $6.15 | OI 10374→11887 (ΔOI +1513张) | ΔOI/Volume 19.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1513张（+14.6% vs前日OI），连续性待观察（方向未知）
12-18 170.0C — Vol 1,306 | 最新价 $0.90 | OI 54010→54998 (ΔOI +988张) | ΔOI/Volume 75.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增988张（+1.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,327 张（Put 6,559 / Call 2,768），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/SOXX_morning.json