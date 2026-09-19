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
🟡 **近现价集中开仓**: 09-25 150P ΔOI -1,912（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 150P ΔOI +254 占该期限总 OI 15.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 162.9）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 158.25 → 今开 158.21（-0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 159.19 ｜ 低 156.66

Options: P/C成交量 4.73 | OI比 1.42 | ATM IV 37.1% | Skew 0.2pp | Term 0.84 | ExpMove ±3.8%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜当日成交偏 Put（P/C量 4.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.73×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.42×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±3.8% ｜ 10-02（14D）±4.2% ｜ 10-09（21D）±6.3% ｜ 10-16（28D）±8.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -77,961,891 | GEX Change vs 上次快照 -29,544,760 | Flip: Candidates 162.94 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 375 / LOW 143 / INVALID 336
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈163（全链重定价，覆盖 79%，CONDITIONAL）
Put Wall 150（现价高于该位 4.7%） | Call Wall 170（弱结构｜现价低于该位 7.6%）
最近结构参考: Flip 163（现价低于该位 3.6%）
量化视角： 负 Gamma（7796万，无历史分位）｜负 Gamma 加深（2954万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 156（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 156.0P — Vol 15,332 | 最新价 $0.59 | OI 3201→9373 (ΔOI +6172张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6172张（+192.8% vs前日OI），连续性待观察（方向未知）
10-16 153.0P — Vol 4,020 | 最新价 $3.15 | OI 2551→6377 (ΔOI +3826张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3826张（+150.0% vs前日OI），连续性待观察（方向未知）
10-16 170.0C — Vol 2,132 | 最新价 $1.58 | OI 984→3038 (ΔOI +2054张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2054张（+208.7% vs前日OI），连续性待观察（方向未知）
10-16 150.0P — Vol 2,291 | 最新价 $2.30 | OI 16257→17682 (ΔOI +1425张) | ΔOI/Volume 62.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1425张（+8.8% vs前日OI），连续性待观察（方向未知）
09-18 158.0P — Vol 12,985 | 最新价 $1.21 | OI 11324→12536 (ΔOI +1212张) | ΔOI/Volume 9.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1212张（+10.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,689 张（Put 12,635 / Call 2,054），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 78.9k / P 112.0k，今日成交量: C 7.2k / P 33.9k，平值价格ATM: C $2.05 / P $0.64 ｜ ATM IV 37.1%，预期波动 ±1.7%，Max Pain 156
Top ΔOI: P 156 +6,172 ｜ P 158 +1,212 ｜ C 157 -858

📆 Forward Expiration Structure

09-25  C +0.3k / P -1.0k ｜ Activity MEDIUM △ ｜ 7D
10-02  C +73 / P +0.2k ｜ Activity HIGH ｜ 14D
10-09  C +8 / P +0.5k ｜ Activity HIGH ｜ 21D
10-16  C +3.4k / P +6.8k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 7.2k / P 32.3k，今日变化ΔOI: C +0.3k / P -1.0k，平值价格ATM: C $3.66 / P $2.34 ｜ ATM IV 30.2%，净 delta 敞口 -11k shares
Top ΔOI: P 150 -1,912 ｜ P 157 +597 ｜ P 158 +339
仓位参考: Max Pain 158 ｜ Call Wall 160（+1.9%，弱）（OI 2.4k） ｜ Put Wall 145（-7.7%）（OI 15.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 30.2%｜历史 Rank 72%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 负 11,379 股

📆 10-02 Forward Structure
存量OI: C 1.7k / P 1.6k，今日变化ΔOI: C +73 / P +0.2k，平值价格ATM: C $3.20 / P $3.32 ｜ ATM IV 30.3%，净 delta 敞口 -8k shares
Top ΔOI: P 158 +77 ｜ P 164 +60 ｜ P 149 +46
仓位参考: Max Pain 160 ｜ Call Wall 165（+5.1%）（OI 0.7k） ｜ Put Wall 157（-0.0%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.3%｜历史 Rank 72%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 负 8,174 股

📆 10-09 Forward Structure
存量OI: C 0.3k / P 1.3k，今日变化ΔOI: C +8 / P +0.5k，平值价格ATM: C $3.37 / P $6.46 ｜ ATM IV 30.5%，净 delta 敞口 -7k shares
Top ΔOI: P 150 +254 ｜ C 158 +5
仓位参考: Max Pain 160 ｜ Call Wall 172（+9.5%，弱）（OI 38） ｜ Put Wall 150（-4.5%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 30.5%｜历史 Rank 72%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 负 7,119 股

📆 10-16 Forward Structure
存量OI: C 33.3k / P 53.6k，今日变化ΔOI: C +3.4k / P +6.8k，平值价格ATM: C $6.19 / P $6.79 ｜ ATM IV 31.1%，净 delta 敞口 -62k shares
Top ΔOI: P 153 +3,826 ｜ C 170 +2,054 ｜ P 150 +1,425
仓位参考: Max Pain 165 ｜ Call Wall 170（+8.3%，弱）（OI 3.0k） ｜ Put Wall 150（-4.5%）（OI 17.7k）
量化解读： 存量 Put 重｜ATM IV 31.1%｜历史 Rank 72%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 负 61,585 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/XBI_morning.json