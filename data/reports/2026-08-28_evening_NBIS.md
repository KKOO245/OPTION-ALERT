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
🟡 **近现价集中开仓**: 09-04 200P ΔOI +2,770（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 211.97 → 收盘 209.18（-1.3%） ｜ 今日高 214.28 ｜ 低 205.48
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.57 | OI比 0.79 | ATM IV 95.9% | Skew -3.0pp | Term 0.82 | ExpMove ±0.7%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±8.3% ｜ 09-11（14D）±11.8% ｜ 09-18（21D）±14.8% ｜ 09-25（28D）±17.3%
   ⇒ IV–VIX Spread: +81.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 220.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 576 / LOW 71 / INVALID 247
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 220.52（全链重定价，覆盖 88%）
Put Wall 200（现价高于该位 4.6%） | Call Wall 250（现价低于该位 16.3%）
最近结构参考: Put Wall 200（现价高于该位 4.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 221（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 180.0P — Vol 413 | 最新价 $0.03 | OI 2063→2679 (ΔOI +616张) | ΔOI/Volume 149.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增616张（+29.9% vs前日OI），连续性待观察（方向未知）
08-28 235.0C — Vol 3,258 | 最新价 $0.55 | OI 1687→2244 (ΔOI +557张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增557张（+33.0% vs前日OI），连续性待观察（方向未知）
08-28 300.0C — Vol 754 | 最新价 $0.01 | OI 3394→3914 (ΔOI +520张) | ΔOI/Volume 69.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增520张（+15.3% vs前日OI），连续性待观察（方向未知）
08-28 245.0C — Vol 2,828 | 最新价 $0.13 | OI 1792→2288 (ΔOI +496张) | ΔOI/Volume 17.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增496张（+27.7% vs前日OI），连续性待观察（方向未知）
08-28 155.0P — Vol 342 | 最新价 $0.01 | OI 2000→2429 (ΔOI +429张) | ΔOI/Volume 125.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增429张（+21.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +7.1k / P +7.3k ｜ Activity HIGH ｜ 7D
09-11  C +2.9k / P +0.5k ｜ Activity HIGH ｜ 14D
09-18  C +0.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
09-25  C +0.8k / P +0.7k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 39.1k / P 29.9k
ΔOI:      C +7.1k / P +7.3k
ATM:      C 8.35 / P 8.92
ATM IV:   74.1%
ΔOI Δ Exposure*: -152k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 200 ｜ +2,770 ｜ $4.65 ｜ 名义 $1.29M* ｜ -4.4%
C 300 ｜ +1,062 ｜ $0.10 ｜ 名义 $10.6k* ｜ +43.4%
P 210 ｜ +985 ｜ $8.92 ｜ 名义 $878.6k* ｜ +0.4%
结构参考：300（+43.4%）上方 / 200（-4.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 10.5k / P 12.2k
ΔOI:      C +2.9k / P +0.5k
ATM:      C 12.01 / P 12.60
ATM IV:   75.3%
ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 260 ｜ +539 ｜ $1.50 ｜ 名义 $80.8k* ｜ +24.3%
C 300 ｜ +478 ｜ $0.40 ｜ 名义 $19.1k* ｜ +43.4%
C 280 ｜ +402 ｜ $0.74 ｜ 名义 $29.7k* ｜ +33.9%
结构参考：260（+24.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 310C +574 ｜ 210P +457

📆 09-25 Forward Structure
OI:       C 6.8k / P 9.6k
ΔOI:      C +0.8k / P +0.7k
ATM:      C 17.96 / P 18.20
ATM IV:   78.9%
ΔOI Δ Exposure*: 926 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 110 ｜ +199 ｜ $0.23 ｜ 名义 $4.6k* ｜ -47.4%
C 350 ｜ +157 ｜ $0.62 ｜ 名义 $9.7k* ｜ +67.3%
C 300 ｜ +143 ｜ $1.90 ｜ 名义 $27.2k* ｜ +43.4%
结构参考：350（+67.3%）上方 / 110（-47.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/NBIS_evening.json