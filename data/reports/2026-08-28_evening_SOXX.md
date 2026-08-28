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
🟡 **近现价集中开仓**: 09-04 490P ΔOI +257（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 521.31 → 收盘 508.62（-2.4%） ｜ 今日高 522.65 ｜ 低 506.82
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 7.01 | OI比 0.77 | ATM IV 45.3% | Skew 1.3pp | Term 0.84 | ExpMove ±0.7%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 7.01×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±3.9% ｜ 09-11（14D）±5.6% ｜ 09-18（21D）±8.0% ｜ 09-25（28D）±3.2%
   ⇒ IV–VIX Spread: +30.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 524.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 566 / LOW 313 / INVALID 743
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 524.63（全链重定价，覆盖 87%）
Put Wall 500（现价高于该位 1.7%） | Call Wall 575（现价低于该位 11.5%）
最近结构参考: Put Wall 500（现价高于该位 1.7%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall）；上方 575（Call Wall）。
• Gamma 区域：切换参考 525（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 580.0C — Vol 5 | 最新价 $5.31 | OI 41→1878 (ΔOI +1837张) | ΔOI/Volume 36740.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1837张（+4480.5% vs前日OI），连续性待观察（方向未知）
08-28 475.0P — Vol 5 | 最新价 $0.07 | OI 782→1786 (ΔOI +1004张) | ΔOI/Volume 20080.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1004张（+128.4% vs前日OI），连续性待观察（方向未知）
08-28 515.0P — Vol 142 | 最新价 $2.50 | OI 565→1533 (ΔOI +968张) | ΔOI/Volume 681.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增968张（+171.3% vs前日OI），连续性待观察（方向未知）
08-28 527.5C — Vol 750 | 最新价 $2.33 | OI 14→768 (ΔOI +754张) | ΔOI/Volume 100.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增754张（+5385.7% vs前日OI），连续性待观察（方向未知）
09-04 510.0P — Vol 362 | 最新价 $6.41 | OI 322→647 (ΔOI +325张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增325张（+100.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.7k / P +0.7k ｜ Activity HIGH ｜ 7D
09-11  C +45 / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
09-18  C +1.0k / P -0.3k ｜ Activity HIGH ｜ 21D
09-25  C +0.2k / P +37 ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 25.4k / P 18.3k
ΔOI:      C +0.7k / P +0.7k
ATM:      C 11.40 / P 8.60
ATM IV:   36.5%
ΔOI Δ Exposure*: -16k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 490 ｜ +257 ｜ $3.40 ｜ 名义 $87.4k* ｜ -3.7%
C 570 ｜ +255 ｜ $0.39 ｜ 名义 $9.9k* ｜ +12.1%
C 547 ｜ +240 ｜ $2.20 ｜ 名义 $52.8k* ｜ +7.6%
结构参考：570（+12.1%）上方 / 490（-3.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 435P +70 ｜ 430P +50

📆 09-18 Forward Structure
OI:       C 78.6k / P 75.6k
ΔOI:      C +1.0k / P -0.3k
ATM:      C 22.70 / P 17.89
ATM IV:   37.7%
ΔOI Δ Exposure*: 57k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 470 ｜ -403 ｜ $6.05 ｜ 名义 $-243.8k* ｜ -7.6%
P 495 ｜ +375 ｜ $11.78 ｜ 名义 $441.8k* ｜ -2.7%
C 540 ｜ +279 ｜ $7.55 ｜ 名义 $210.6k* ｜ +6.2%
结构参考：540（+6.2%）上方 / 495（-2.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 4.2k / P 4.1k
ΔOI:      C +0.2k / P +37
ATM:      C 0.00 / P 16.20
ATM IV:   37.9%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 630 ｜ +166 ｜ $0.99 ｜ 名义 $16.4k* ｜ +23.9%
P 410 ｜ +28 ｜ $1.16 ｜ 名义 $3.2k* ｜ -19.4%
C 575 ｜ +19 ｜ $5.30 ｜ 名义 $10.1k* ｜ +13.1%
结构参考：630（+23.9%）上方 / 410（-19.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SOXX_evening.json