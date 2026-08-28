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
🟡 **近现价集中开仓**: 08-31 700P ΔOI +5,503（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-01 495P ΔOI +13,081 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 719.75 → 收盘 716.43（-0.5%） ｜ 今日高 724.12 ｜ 低 715.09
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.92 | OI比 1.03 | ATM IV 12.8% | Skew 3.2pp | Term 1.32 | ExpMove ±0.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-31（3D）±0.7% ｜ 09-01（4D）±1.0% ｜ 09-02（5D）±1.2% ｜ 09-03（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 713.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 2892 / LOW 661 / INVALID 2129
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 713.87（全链重定价，覆盖 89%）
Put Wall 700（现价高于该位 2.3%） | Call Wall 730（现价低于该位 1.9%）
最近结构参考: Flip 714（现价高于该位 0.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall）；上方 730（Call Wall）。
• Gamma 区域：切换参考 714（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 425.0P — Vol 610 | 最新价 $0.01 | OI 39→18641 (ΔOI +18602张) | ΔOI/Volume 3049.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18602张（+47697.4% vs前日OI），连续性待观察（方向未知）
08-28 625.0P — Vol 319 | 最新价 $0.01 | OI 942→17225 (ΔOI +16283张) | ΔOI/Volume 5104.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16283张（+1728.6% vs前日OI），连续性待观察（方向未知）
09-30 715.0C — Vol 315 | 最新价 $20.00 | OI 544→10403 (ΔOI +9859张) | ΔOI/Volume 3129.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9859张（+1812.3% vs前日OI），连续性待观察（方向未知）
09-30 730.0C — Vol 1,507 | 最新价 $11.75 | OI 4744→12936 (ΔOI +8192张) | ΔOI/Volume 543.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8192张（+172.7% vs前日OI），连续性待观察（方向未知）
09-01 675.0P — Vol 128 | 最新价 $0.13 | OI 255→8089 (ΔOI +7834张) | ΔOI/Volume 6120.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7834张（+3072.2% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C -6.8k / P +35.9k ｜ Activity HIGH ｜ 3D
09-01  C +3.6k / P +37.5k ｜ Activity HIGH ｜ 4D
09-02  C +2.6k / P +27.9k ｜ Activity HIGH ｜ 5D
09-03  C +6.1k / P +8.7k ｜ Activity HIGH ｜ 6D

📆 08-31 Forward Structure
OI:       C 381.2k / P 288.5k
ΔOI:      C -6.8k / P +35.9k
ATM:      C 2.60 / P 2.23
ATM IV:   9.3%
ΔOI Δ Exposure*: -884k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 525 ｜ +9,529 ｜ $0.01 ｜ 名义 $9.5k* ｜ -26.7%
P 700 ｜ +5,503 ｜ $0.12 ｜ 名义 $66.0k* ｜ -2.3%
P 650 ｜ +4,667 ｜ $0.01 ｜ 名义 $4.7k* ｜ -9.3%
结构参考：525（-26.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-01 Forward Structure
OI:       C 32.8k / P 88.5k
ΔOI:      C +3.6k / P +37.5k
ATM:      C 3.67 / P 3.18
ATM IV:   11.4%
ΔOI Δ Exposure*: -90k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 495 ｜ +13,081 ｜ $0.01 ｜ 名义 $13.1k* ｜ -30.9%
P 500 ｜ +12,256 ｜ $0.01 ｜ 名义 $12.3k* ｜ -30.2%
P 505 ｜ +3,840 ｜ $0.01 ｜ 名义 $3.8k* ｜ -29.5%
结构参考：495（-30.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 15.9k / P 50.3k
ΔOI:      C +2.6k / P +27.9k
ATM:      C 4.52 / P 4.02
ATM IV:   12.7%
ΔOI Δ Exposure*: -200k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 655 ｜ +9,395 ｜ $0.04 ｜ 名义 $37.6k* ｜ -8.6%
P 691 ｜ +7,681 ｜ $0.26 ｜ 名义 $199.7k* ｜ -3.5%
P 650 ｜ +5,892 ｜ $0.04 ｜ 名义 $23.6k* ｜ -9.3%
结构参考：655（-8.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-03 Forward Structure
OI:       C 15.3k / P 26.5k
ΔOI:      C +6.1k / P +8.7k
ATM:      C 5.25 / P 4.76
ATM IV:   13.6%
ΔOI Δ Exposure*: -94k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 733 ｜ +1,443 ｜ $0.28 ｜ 名义 $40.4k* ｜ +2.3%
P 703 ｜ +1,141 ｜ $1.37 ｜ 名义 $156.3k* ｜ -1.9%
P 710 ｜ +697 ｜ $2.71 ｜ 名义 $188.9k* ｜ -0.9%
结构参考：733（+2.3%）上方 / 703（-1.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/QQQ_evening.json