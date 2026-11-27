# 期权晚报 2026-11-27（快照 16:40 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-30 727P ΔOI -7,008（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-03 635P ΔOI +10,977 占该期限总 OI 13.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 725.86 → 收盘 728.32（+0.3%） ｜ 今日高 729.15 ｜ 低 719.62 ｜ 昨收 716.70 → 收盘 728.32（+1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.97 | OI比 0.97 | ATM IV 17.8% | Skew 2.6pp | Term 1.12 | ExpMove ±1.2%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构正常（Term 1.12）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 51% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 51%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-30（3D）±1.2% ｜ 12-01（4D）±1.6% ｜ 12-02（5D）±1.9% ｜ 12-03（6D）±2.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -232,116,345 | GEX Change vs 上次快照 236,715,008 | Flip: Primary Flip: 733.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 2961 / LOW 589 / INVALID 2100
结构观察区: Primary Flip 733.07（全链重定价，覆盖 89%）
最近结构参考: Flip 733（现价低于该位 0.6%）
量化视角： 负 Gamma（2.32亿，历史分位 51%，中性区）｜负 Gamma 缓解（+2.37亿）｜现价位于 Flip 下方 0.65%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 717（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +39.4k / P +10.7k ｜ Activity HIGH ｜ 3D
12-01  C +22.1k / P +14.2k ｜ Activity HIGH ｜ 4D
12-02  C +23.5k / P +30.6k ｜ Activity HIGH ｜ 5D
12-03  C +5.3k / P +34.9k ｜ Activity HIGH ｜ 6D

📆 11-30 Forward Structure
存量OI: C 420.2k / P 728.8k，今日变化ΔOI: C +39.4k / P +10.7k，平值价格ATM: C $4.39 / P $4.21 ｜ ATM IV 16.0%，净 delta 敞口 3.0M shares
Top ΔOI: P 727 -7,008 ｜ P 685 -4,148
仓位参考: Max Pain 727 ｜ Call Wall 750（+3.0%，弱）（OI 13.2k） ｜ Put Wall 727（-0.2%，弱）（OI 16.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.0%｜历史 Rank 75%（近端代理）｜IV/RV 0.51×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,970,698 股

📆 12-01 Forward Structure
存量OI: C 85.0k / P 60.1k，今日变化ΔOI: C +22.1k / P +14.2k，平值价格ATM: C $6.05 / P $5.60 ｜ ATM IV 18.8%，净 delta 敞口 1.1M shares
Top ΔOI: C 724 +3,964 ｜ C 719 +3,584
仓位参考: Max Pain 718 ｜ Call Wall 724（-0.6%，弱）（OI 4.6k） ｜ Put Wall 720（-1.1%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 18.8%｜历史 Rank 75%（近端代理）｜IV/RV 0.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,100,173 股

📆 12-02 Forward Structure
存量OI: C 67.4k / P 90.0k，今日变化ΔOI: C +23.5k / P +30.6k，平值价格ATM: C $7.19 / P $6.68 ｜ ATM IV 19.9%，净 delta 敞口 1.3M shares
Top ΔOI: C 715 +8,670
仓位参考: Max Pain 710 ｜ Call Wall 715（-1.8%）（OI 9.0k）
量化解读： 存量 Put 重｜ATM IV 19.9%｜历史 Rank 75%（近端代理）｜IV/RV 0.64×（近似）｜净 delta 敞口 正 1,348,043 股

📆 12-03 Forward Structure
存量OI: C 27.4k / P 52.9k，今日变化ΔOI: C +5.3k / P +34.9k，平值价格ATM: C $8.19 / P $7.48 ｜ ATM IV 20.7%，净 delta 敞口 92k shares
Top ΔOI: P 635 +10,977 ｜ P 640 +6,792 ｜ P 630 +3,215
仓位参考: Max Pain 715 ｜ Call Wall 725（-0.5%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 20.7%｜历史 Rank 75%（近端代理）｜IV/RV 0.66×（近似）｜净 delta 敞口 正 92,380 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SPY_evening.json