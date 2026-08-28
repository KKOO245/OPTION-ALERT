# 期权晚报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.51 ↓4.6%（5D -9.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🟡 **近现价集中开仓**: 08-28 167P ΔOI +3,969（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 08-28 167P ΔOI +3,969 占该期限总 OI 13.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
XBI: 今晨 168.56 → 收盘 168.23（-0.2%） ｜ 今日高 169.27 ｜ 低 166.88
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 5.92 | OI比 1.35 | ATM IV 34.3% | Skew -0.4pp | Term 0.92 | ExpMove ±1.5%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 5.92×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.35×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±1.4% ｜ 09-04（8D）±3.8% ｜ 09-11（15D）±2.6% ｜ 09-18（22D）±6.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 167.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 437 / LOW 164 / INVALID 299
结构观察区: ≈168（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 155: +8.5% | 距 Call Wall 170: -1.0%
最近结构参考: Flip 168（距现价 +0.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（Put Wall）；上方 170（Call Wall）。
• Gamma 区域：切换参考 168（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 167.0P — Vol 20 | 最新价 $0.59 | OI 32→4001 (ΔOI +3969张) | ΔOI/Volume 19845.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3969张（+12403.1% vs前日OI），连续性待观察（方向未知）
08-28 170.0C — Vol 180 | 最新价 $0.60 | OI 778→3800 (ΔOI +3022张) | ΔOI/Volume 1678.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3022张（+388.4% vs前日OI），连续性待观察（方向未知）
08-28 172.5C — Vol 1 | 最新价 $0.45 | OI 14→1471 (ΔOI +1457张) | ΔOI/Volume 145700.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1457张（+10407.1% vs前日OI），连续性待观察（方向未知）
09-18 155.0P — Vol 3,026 | 最新价 $0.91 | OI 14486→15485 (ΔOI +999张) | ΔOI/Volume 33.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+6.9% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 727 | 最新价 $2.50 | OI 7891→8772 (ΔOI +881张) | ΔOI/Volume 121.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增881张（+11.2% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +4.9k / P +5.3k ｜ Activity HIGH ｜ 1D
09-04  C +73 / P +0.4k ｜ Activity HIGH ｜ 8D
09-11  C +51 / P +36 ｜ Activity HIGH ｜ 15D
09-18  C +0.9k / P +1.0k ｜ Activity HIGH ｜ 22D

📆 08-28 Forward Structure
OI:       C 12.3k / P 16.6k
ΔOI:      C +4.9k / P +5.3k
ATM:      C 1.40 / P 0.87
ATM IV:   34.3%
ΔOI Δ Exposure*: -36k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 167 ｜ +3,969 ｜ $0.59 ｜ 名义 $234.2k* ｜ -0.7%
C 170 ｜ +3,022 ｜ $0.60 ｜ 名义 $181.3k* ｜ +1.1%
C 172 ｜ +1,457 ｜ $0.45 ｜ 名义 $65.6k* ｜ +2.5%
结构参考：170（+1.1%）上方 / 167（-0.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 2.4k / P 4.1k
ΔOI:      C +73 / P +0.4k
ATM:      C 3.55 / P 2.83
ATM IV:   31.3%
ΔOI Δ Exposure*: -13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 167 ｜ +329 ｜ $2.65 ｜ 名义 $87.2k* ｜ -0.4%
C 167 ｜ +23 ｜ $3.90 ｜ 名义 $9.0k* ｜ -0.4%
P 157 ｜ +16 ｜ $0.26 ｜ 名义 $416* ｜ -6.7%
结构参考：167（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 1.1k / P 1.4k
ΔOI:      C +51 / P +36
ATM:      C 4.34 / P 0.00
ATM IV:   30.3%
ΔOI Δ Exposure*: 2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 156 ｜ +20 ｜ $1.01 ｜ 名义 $2.0k* ｜ -7.3%
C 154 ｜ +15 ｜ $15.40 ｜ 名义 $23.1k* ｜ -8.5%
C 180 ｜ +14 ｜ $0.96 ｜ 名义 $1.3k* ｜ +7.0%
结构参考：180（+7.0%）上方 / 156（-7.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 70.9k / P 102.5k
ΔOI:      C +0.9k / P +1.0k
ATM:      C 5.75 / P 4.65
ATM IV:   32.0%
ΔOI Δ Exposure*: -48k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ -1,277 ｜ $10.60 ｜ 名义 $-1.35M* ｜ -4.9%
P 155 ｜ +999 ｜ $0.91 ｜ 名义 $90.9k* ｜ -7.9%
C 175 ｜ +881 ｜ $2.50 ｜ 名义 $220.2k* ｜ +4.0%
结构参考：175（+4.0%）上方 / 155（-7.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/XBI_evening.json