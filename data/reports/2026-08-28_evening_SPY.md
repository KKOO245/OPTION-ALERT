# 期权晚报 2026-08-28

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↓0.6%（5D -4.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 08-31 745P ΔOI -10,053（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 771.76 → 收盘 769.35（-0.3%） ｜ 今日高 775.29 ｜ 低 768.31
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.99 | OI比 1.52 | ATM IV 11.2% | Skew 2.8pp | Term 1.01 | ExpMove ±0.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.52×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-31（3D）±0.5% ｜ 09-01（4D）±0.6% ｜ 09-02（5D）±0.8% ｜ 09-03（6D）±0.9%
   ⇒ IV–VIX Spread: -3.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 771.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 3291 / LOW 600 / INVALID 1877
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 771.01（全链重定价，覆盖 91%）
Put Wall 535（现价高于该位 43.8%） | Call Wall 800（现价低于该位 3.8%）
最近结构参考: Flip 771（现价低于该位 0.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 535（Put Wall）；上方 800（Call Wall）。
• Gamma 区域：切换参考 771（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 800.0C — Vol 4,150 | 最新价 $1.54 | OI 50235→64519 (ΔOI +14284张) | ΔOI/Volume 344.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14284张（+28.4% vs前日OI），连续性待观察（方向未知）
09-04 760.0P — Vol 51,184 | 最新价 $1.70 | OI 44755→57595 (ΔOI +12840张) | ΔOI/Volume 25.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12840张（+28.7% vs前日OI），连续性待观察（方向未知）
08-31 745.0P — Vol 15,289 | 最新价 $0.07 | OI 10095→22058 (ΔOI +11963张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11963张（+118.5% vs前日OI），连续性待观察（方向未知）
09-04 747.0P — Vol 17,061 | 最新价 $0.56 | OI 785→11075 (ΔOI +10290张) | ΔOI/Volume 60.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10290张（+1310.8% vs前日OI），连续性待观察（方向未知）
10-02 795.0C — Vol 132 | 最新价 $2.63 | OI 321→7649 (ΔOI +7328张) | ΔOI/Volume 5551.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7328张（+2282.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +14.9k / P +14.2k ｜ Activity MEDIUM △ ｜ 3D
09-01  C +8.0k / P +8.2k ｜ Activity HIGH ｜ 4D
09-02  C +10.9k / P +30.9k ｜ Activity HIGH ｜ 5D
09-03  C +8.5k / P +9.5k ｜ Activity HIGH ｜ 6D

   Top ΔOI: 745P -10,053 ｜ 780C +3,966

📆 09-01 Forward Structure
OI:       C 53.9k / P 48.6k
ΔOI:      C +8.0k / P +8.2k
ATM:      C 2.62 / P 2.25
ATM IV:   7.5%
ΔOI Δ Exposure*: -47k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 777 ｜ +1,629 ｜ $0.18 ｜ 名义 $29.3k* ｜ +1.0%
C 775 ｜ +1,019 ｜ $0.40 ｜ 名义 $40.8k* ｜ +0.7%
P 761 ｜ +1,001 ｜ $0.47 ｜ 名义 $47.0k* ｜ -1.1%
结构参考：777（+1.0%）上方 / 761（-1.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 35.5k / P 62.8k
ΔOI:      C +10.9k / P +30.9k
ATM:      C 3.16 / P 2.81
ATM IV:   8.3%
ΔOI Δ Exposure*: -308k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 766 ｜ +9,776 ｜ $1.72 ｜ 名义 $1.68M* ｜ -0.4%
P 690 ｜ +7,999 ｜ $0.01 ｜ 名义 $8.0k* ｜ -10.3%
P 700 ｜ +5,214 ｜ $0.02 ｜ 名义 $10.4k* ｜ -9.0%
结构参考：766（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-03 Forward Structure
OI:       C 27.6k / P 28.6k
ΔOI:      C +8.5k / P +9.5k
ATM:      C 3.80 / P 3.26
ATM IV:   8.8%
ΔOI Δ Exposure*: -46k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 775 ｜ +2,498 ｜ $1.16 ｜ 名义 $289.8k* ｜ +0.7%
P 769 ｜ +1,245 ｜ $3.26 ｜ 名义 $405.9k* ｜ -0.0%
P 718 ｜ +1,000 ｜ $0.05 ｜ 名义 $5.0k* ｜ -6.7%
结构参考：775（+0.7%）上方 / 718（-6.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SPY_evening.json