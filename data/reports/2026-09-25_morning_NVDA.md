# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.58
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-28 230C ΔOI +4,352（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 224.58 → 今开 225.15（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 226.94 ｜ 低 223.45

Options: P/C成交量 0.40 | OI比 0.64 | ATM IV 35.1% | Skew 1.9pp | Term 0.87 | ExpMove ±1.7%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-28（3D）±1.7% ｜ 09-30（5D）±2.7% ｜ 10-02（7D）±3.3% ｜ 10-05（10D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 731,979,552 | GEX Change vs 上次快照 165,205,115 | Flip: Primary Flip: 215.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 672 / LOW 210 / INVALID 470
结构观察区: Primary Flip 215.63（全链重定价，覆盖 95%）
Call Wall 230（弱结构｜现价低于该位 2.3%）
最近结构参考: Call Wall 230（现价低于该位 2.3%）
量化视角： 正 Gamma（7.32亿，无历史分位）｜正 Gamma 增强（+1.65亿）｜现价位于 Flip 上方 4.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 225.0C — Vol 260,174 | 最新价 $1.35 | OI 38416→87943 (ΔOI +49527张) | ΔOI/Volume 19.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增49527张（+128.9% vs前日OI），连续性待观察（方向未知）
09-25 230.0C — Vol 112,116 | 最新价 $0.17 | OI 81391→90075 (ΔOI +8684张) | ΔOI/Volume 7.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8684张（+10.7% vs前日OI），连续性待观察（方向未知）
09-25 227.5C — Vol 88,189 | 最新价 $0.50 | OI 50081→58388 (ΔOI +8307张) | ΔOI/Volume 9.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8307张（+16.6% vs前日OI），连续性待观察（方向未知）
10-09 115.0P — Vol 8,272 | 最新价 $0.03 | OI 10004→18026 (ΔOI +8022张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8022张（+80.2% vs前日OI），连续性待观察（方向未知）
09-25 222.5P — Vol 70,205 | 最新价 $0.74 | OI 7216→13033 (ΔOI +5817张) | ΔOI/Volume 8.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5817张（+80.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 80,357 张（Put 13,839 / Call 66,518），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 587.4k / P 373.0k，今日成交量: C 260.1k / P 104.4k，平值价格ATM: C $0.53 / P $1.30 ｜ ATM IV 35.1%，预期波动 ±0.8%，Max Pain 220
Top ΔOI: C 225 +49,527 ｜ C 230 +8,684 ｜ C 227 +8,307

📆 Forward Expiration Structure

09-28  C +15.2k / P +13.7k ｜ Activity HIGH ｜ 3D
09-30  C +7.1k / P +5.0k ｜ Activity HIGH ｜ 5D
10-02  C +11.2k / P +18.7k ｜ Activity HIGH ｜ 7D
10-05  C +4.6k / P +1.4k ｜ Activity HIGH ｜ 10D

📆 09-28 Forward Structure
存量OI: C 68.0k / P 52.5k，今日变化ΔOI: C +15.2k / P +13.7k，平值价格ATM: C $1.49 / P $2.30 ｜ ATM IV 22.0%，净 delta 敞口 177k shares
Top ΔOI: C 230 +4,352 ｜ C 237 +3,750 ｜ C 225 +3,717
仓位参考: Max Pain 222 ｜ Call Wall 230（+2.3%，弱）（OI 12.7k） ｜ Put Wall 220（-2.1%，弱）（OI 6.0k）
量化解读： 存量 Call 重｜ATM IV 22.0%｜历史 Rank 20%（近端代理）｜IV/RV 0.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 177,295 股

📆 09-30 Forward Structure
存量OI: C 37.3k / P 25.2k，今日变化ΔOI: C +7.1k / P +5.0k，平值价格ATM: C $2.66 / P $3.33 ｜ ATM IV 27.7%，净 delta 敞口 134k shares
Top ΔOI: P 212 +1,905 ｜ C 225 +1,852 ｜ C 230 +1,180
仓位参考: Max Pain 222 ｜ Call Wall 230（+2.3%）（OI 9.6k） ｜ Put Wall 212.5（-5.5%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 27.7%｜历史 Rank 20%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 133,603 股

📆 10-02 Forward Structure
存量OI: C 219.7k / P 249.0k，今日变化ΔOI: C +11.2k / P +18.7k，平值价格ATM: C $3.45 / P $4.05 ｜ ATM IV 29.4%，净 delta 敞口 -167k shares
Top ΔOI: P 215 +4,420 ｜ P 225 +3,267
仓位参考: Max Pain 220 ｜ Call Wall 235（+4.6%，弱）（OI 26.9k） ｜ Put Wall 220（-2.1%，弱）（OI 13.6k）
量化解读： 存量两侧均衡｜ATM IV 29.4%｜历史 Rank 20%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 166,992 股

📆 10-05 Forward Structure
存量OI: C 15.1k / P 5.8k，今日变化ΔOI: C +4.6k / P +1.4k，平值价格ATM: C $3.88 / P $4.40 ｜ ATM IV 27.7%，净 delta 敞口 142k shares
Top ΔOI: C 225 +970 ｜ C 230 +790 ｜ C 235 +687
仓位参考: Max Pain 222 ｜ Call Wall 230（+2.3%）（OI 3.9k） ｜ Put Wall 222.5（-1.0%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 27.7%｜历史 Rank 20%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 142,457 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NVDA_morning.json