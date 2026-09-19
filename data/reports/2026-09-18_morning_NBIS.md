# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.85 ｜ QQQ $nan
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 215C ΔOI +1,578（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 217.99 → 今开 218.15（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 220.20 ｜ 低 210.30

Options: P/C成交量 0.54 | OI比 1.21 | ATM IV 108.0% | Skew 4.9pp | Term 0.72 | ExpMove ±8.4%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 4.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±8.4% ｜ 10-02（14D）±12.5% ｜ 10-09（21D）±15.6% ｜ 10-16（28D）±17.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,085,985 | GEX Change vs 上次快照 3,400,166 | Flip: Primary Flip: 217.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 491 / LOW 71 / INVALID 240
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 217.48（全链重定价，覆盖 97%）
Put Wall 200（弱结构｜现价高于该位 6.7%）
最近结构参考: Flip 217（现价低于该位 1.9%）
量化视角： 负 Gamma（709万，无历史分位）｜负 Gamma 缓解（+340万）｜现价位于 Flip 下方 1.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 217（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 75.0P — Vol 5,401（Yahoo补） | 最新价 $0.05 | OI 272→5481 (ΔOI +5209张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5209张（+1915.1% vs前日OI），连续性待观察（方向未知）
09-18 220.0C — Vol 1,363 | 最新价 $2.53 | OI 3054→5142 (ΔOI +2088张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2088张（+68.4% vs前日OI），连续性待观察（方向未知）
09-25 250.0C — Vol 128 | 最新价 $1.76 | OI 1248→3332 (ΔOI +2084张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2084张（+167.0% vs前日OI），连续性待观察（方向未知）
09-18 267.5C — Vol 4 | 最新价 $0.04 | OI 117→1762 (ΔOI +1645张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1645张（+1406.0% vs前日OI），连续性待观察（方向未知）
09-25 230.0C — Vol 190 | 最新价 $5.28 | OI 683→2326 (ΔOI +1643张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1643张（+240.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,669 张（Put 5,209 / Call 7,460），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 153.5k / P 186.3k，今日成交量: C 28.8k / P 15.6k，平值价格ATM: C $3.08 / P $1.84 ｜ ATM IV 108.0%，预期波动 ±2.3%，Max Pain 215
Top ΔOI: C 220 +2,088 ｜ C 267 +1,645 ｜ C 230 +1,412

📆 Forward Expiration Structure

09-25  C +10.4k / P +5.1k ｜ Activity HIGH ｜ 7D
10-02  C +1.9k / P +0.9k ｜ Activity MEDIUM △ ｜ 14D
10-09  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 21D
10-16  C +3.2k / P +6.7k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 35.6k / P 32.9k，今日变化ΔOI: C +10.4k / P +5.1k，平值价格ATM: C $9.55 / P $8.29 ｜ ATM IV 73.6%，净 delta 敞口 177k shares
Top ΔOI: C 250 +2,084 ｜ C 230 +1,643 ｜ C 215 +1,578
仓位参考: Max Pain 212 ｜ Call Wall 227.5（+6.6%，弱）（OI 3.3k） ｜ Put Wall 200（-6.3%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜ATM IV 73.6%｜历史 Rank 55%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 176,576 股

10-02（MEDIUM △）仓位参考: Max Pain 215 ｜ Call Wall 230（+7.8%，弱）（OI 0.4k） ｜ Put Wall 200（-6.3%，弱）（OI 0.8k）

📆 10-09 Forward Structure
存量OI: C 8.0k / P 8.0k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $15.49 / P $17.74 ｜ ATM IV 77.2%，净 delta 敞口 16k shares
Top ΔOI: P 170 +526
仓位参考: Max Pain 215 ｜ Call Wall 215（+0.7%，弱）（OI 0.5k） ｜ Put Wall 200（-6.3%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.2%｜历史 Rank 55%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 15,762 股

📆 10-16 Forward Structure
存量OI: C 42.7k / P 66.9k，今日变化ΔOI: C +3.2k / P +6.7k，平值价格ATM: C $20.30 / P $16.07 ｜ ATM IV 77.8%，净 delta 敞口 68k shares
Top ΔOI: C 240 +709 ｜ C 250 +644
仓位参考: Max Pain 210 ｜ Call Wall 200（-6.3%，弱）（OI 2.9k） ｜ Put Wall 210（-1.6%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 77.8%｜历史 Rank 55%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 正 67,812 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NBIS_morning.json