# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-05 736P ΔOI +18,082（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-08 675P ΔOI +5,959 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 742.03 → 今开 751.31（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 754.19 ｜ 低 749.10

Options: P/C成交量 0.87 | OI比 2.06 | ATM IV 24.0% | Skew 3.3pp | Term 0.79 | ExpMove ±1.0%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.06×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 92% ｜ P/C OI(近端) 80%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 92%）｜近端持仓结构中性（P/C OI 分位 80%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-05（3D）±1.0% ｜ 10-06（4D）±1.2% ｜ 10-07（5D）±1.5% ｜ 10-08（6D）±1.8%
   ⇒ IV–VIX Spread: +8.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 571,666,260 | GEX Change vs 上次快照 551,757,295 | Flip: Primary Flip: 745.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2836 / LOW 250 / INVALID 1798
结构观察区: Primary Flip 745.03（全链重定价，覆盖 96%）
Call Wall 760（现价低于该位 0.9%）
最近结构参考: Call Wall 760（现价低于该位 0.9%）
量化视角： 正 Gamma（5.72亿，历史分位偏正区，比 92% 的交易日更正）｜正 Gamma 增强（+5.52亿）｜现价位于 Flip 上方 1.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 738（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 745（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 738.0P — Vol 88,656 | 最新价 $1.59 | OI 9843→31406 (ΔOI +21563张) | ΔOI/Volume 24.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21563张（+219.1% vs前日OI），连续性待观察（方向未知）
10-09 754.0C — Vol 23,511 | 最新价 $3.32 | OI 871→20514 (ΔOI +19643张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19643张（+2255.2% vs前日OI），连续性待观察（方向未知）
10-05 736.0P — Vol 34,982 | 最新价 $2.30 | OI 7551→25633 (ΔOI +18082张) | ΔOI/Volume 51.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18082张（+239.5% vs前日OI），连续性待观察（方向未知）
10-02 740.0P — Vol 80,857 | 最新价 $2.15 | OI 13421→31326 (ΔOI +17905张) | ΔOI/Volume 22.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17905张（+133.4% vs前日OI），连续性待观察（方向未知）
10-02 727.0P — Vol 29,053 | 最新价 $0.26 | OI 2344→19012 (ΔOI +16668张) | ΔOI/Volume 57.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16668张（+711.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 93,861 张（Put 74,218 / Call 19,643），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 295.5k / P 607.4k，今日成交量: C 526.8k / P 460.6k，平值价格ATM: C $1.94 / P $1.96 ｜ ATM IV 24.0%，预期波动 ±0.5%，Max Pain 738
Top ΔOI: P 738 +21,563 ｜ P 740 +17,905 ｜ P 727 +16,668

📆 Forward Expiration Structure

10-05  C +26.9k / P +55.0k ｜ Activity HIGH ｜ 3D
10-06  C +5.1k / P +17.8k ｜ Activity HIGH ｜ 4D
10-07  C +8.6k / P +12.1k ｜ Activity HIGH ｜ 5D
10-08  C +5.9k / P +26.8k ｜ Activity HIGH ｜ 6D

📆 10-05 Forward Structure
存量OI: C 71.0k / P 174.5k，今日变化ΔOI: C +26.9k / P +55.0k，平值价格ATM: C $3.71 / P $3.60 ｜ ATM IV 12.7%，净 delta 敞口 1.0M shares
Top ΔOI: P 736 +18,082 ｜ P 735 +10,960 ｜ C 755 +6,007
仓位参考: Max Pain 740 ｜ Call Wall 755（+0.3%，弱）（OI 13.8k） ｜ Put Wall 736（-2.2%）（OI 25.6k）
量化解读： 存量 Put 重｜ATM IV 12.7%｜历史 Rank 77%（近端代理）｜IV/RV 0.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,024,651 股

📆 10-06 Forward Structure
存量OI: C 23.3k / P 59.6k，今日变化ΔOI: C +5.1k / P +17.8k，平值价格ATM: C $4.90 / P $4.53 ｜ ATM IV 14.4%，净 delta 敞口 184k shares
Top ΔOI: P 715 +3,482 ｜ P 736 +1,554 ｜ C 757 +1,267
仓位参考: Max Pain 739 ｜ Call Wall 770（+2.3%）（OI 2.6k） ｜ Put Wall 736（-2.2%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 14.4%｜历史 Rank 77%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 184,495 股

📆 10-07 Forward Structure
存量OI: C 28.0k / P 58.7k，今日变化ΔOI: C +8.6k / P +12.1k，平值价格ATM: C $5.68 / P $5.36 ｜ ATM IV 15.2%，净 delta 敞口 250k shares
Top ΔOI: C 763 +2,895 ｜ P 717 +1,254 ｜ C 770 +1,117
仓位参考: Max Pain 740 ｜ Call Wall 763（+1.4%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 15.2%｜历史 Rank 77%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 250,283 股

📆 10-08 Forward Structure
存量OI: C 15.8k / P 43.2k，今日变化ΔOI: C +5.9k / P +26.8k，平值价格ATM: C $6.50 / P $7.06 ｜ ATM IV 15.7%，净 delta 敞口 136k shares
仓位参考: Max Pain 740 ｜ Call Wall 740（-1.7%，弱）（OI 1.5k） ｜ Put Wall 770（+2.3%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 15.7%｜历史 Rank 77%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 135,626 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/QQQ_morning.json