# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $709.58 ｜ QQQ $630.97
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 145.98 → 今开 143.57（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 143.73 ｜ 低 138.84

Options: P/C成交量 0.86 | OI比 0.46 | ATM IV 66.8% | Skew -43.3pp | Term 0.83 | ExpMove ±2.8% | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -43.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ⇒ IV–VIX Spread: +39.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -198,412,983 | GEX Change vs 上次快照 nan | Flip: Primary Flip: 142.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1058 / LOW 292 / INVALID 279
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 142.07（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价低于该位 7.1%）
最近结构参考: Flip 142（现价低于该位 1.9%）
量化视角： 负 Gamma（1.98亿，无历史分位）｜GEX 变化（nan万）｜现价位于 Flip 下方 1.95%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 142（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 170.0C — Vol 107 | 最新价 $1.65 | OI 100929→149816 (ΔOI +48887张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增48887张（+48.4% vs前日OI），连续性待观察（方向未知）
11-27 160.0C — Vol 183 | 最新价 $0.83 | OI 13010→27881 (ΔOI +14871张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14871张（+114.3% vs前日OI），连续性待观察（方向未知）
11-20 155.0C — Vol 2,095 | 最新价 $0.25 | OI 26979→41315 (ΔOI +14336张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14336张（+53.1% vs前日OI），连续性待观察（方向未知）
11-27 167.5C — Vol 2 | 最新价 $0.27 | OI 4561→18639 (ΔOI +14078张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14078张（+308.7% vs前日OI），连续性待观察（方向未知）
11-27 162.5C — Vol 7 | 最新价 $0.59 | OI 3799→16928 (ΔOI +13129张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13129张（+345.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 105,301 张（Put 0 / Call 105,301），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 1631.1k / P 745.4k，今日成交量: C 407.8k / P 352.9k，平值价格ATM: C $3.20 / P $0.69 ｜ ATM IV 66.8%，预期波动 ±2.8%，Max Pain 160
Top ΔOI: P 190 -39,049 ｜ P 175 -17,295 ｜ C 175 -16,235

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/NVDA_morning.json