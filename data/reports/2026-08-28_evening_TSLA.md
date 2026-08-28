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
🟡 **近现价集中开仓**: 08-31 355C ΔOI +1,403（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 357.10 → 收盘 348.75（-2.3%） ｜ 今日高 358.80 ｜ 低 345.20
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.69 | OI比 0.84 | ATM IV 25.6% | Skew 0.2pp | Term 1.46 | ExpMove ±0.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-31（3D）±1.8% ｜ 09-02（5D）±3.0% ｜ 09-04（7D）±4.0% ｜ 09-09（12D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 339.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 1151 / LOW 211 / INVALID 850
结构观察区: Primary Flip 339.67（全链重定价，覆盖 84%）
Put Wall 340（现价高于该位 2.6%） | Call Wall 400（现价低于该位 12.8%）
最近结构参考: Put Wall 340（现价高于该位 2.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall）；上方 400（Call Wall）。
• Gamma 区域：切换参考 340（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 345.0P — Vol 53,720 | 最新价 $0.45 | OI 3637→8456 (ΔOI +4819张) | ΔOI/Volume 9.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4819张（+132.5% vs前日OI），连续性待观察（方向未知）
09-18 400.0C — Vol 9,219 | 最新价 $2.35 | OI 21314→24948 (ΔOI +3634张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3634张（+17.1% vs前日OI），连续性待观察（方向未知）
08-28 350.0C — Vol 75,659 | 最新价 $6.00 | OI 6894→10383 (ΔOI +3489张) | ΔOI/Volume 4.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3489张（+50.6% vs前日OI），连续性待观察（方向未知）
08-28 355.0C — Vol 119,389 | 最新价 $3.09 | OI 6393→9842 (ΔOI +3449张) | ΔOI/Volume 2.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3449张（+54.0% vs前日OI），连续性待观察（方向未知）
08-28 360.0C — Vol 114,755 | 最新价 $1.36 | OI 10154→13582 (ΔOI +3428张) | ΔOI/Volume 3.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3428张（+33.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +8.8k / P +8.2k ｜ Activity HIGH ｜ 3D
09-02  C +1.6k / P +2.3k ｜ Activity HIGH ｜ 5D
09-04  C +27.1k / P +13.9k ｜ Activity HIGH ｜ 7D
09-09  C +2.4k / P +0.6k ｜ Activity HIGH ｜ 12D

📆 08-31 Forward Structure
OI:       C 55.8k / P 26.3k
ΔOI:      C +8.8k / P +8.2k
ATM:      C 3.85 / P 2.57
ATM IV:   24.8%
ΔOI Δ Exposure*: -23k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 315 ｜ +5,009 ｜ $0.05 ｜ 名义 $25.0k* ｜ -9.7%
C 355 ｜ +1,403 ｜ $1.06 ｜ 名义 $148.7k* ｜ +1.8%
C 370 ｜ +862 ｜ $0.06 ｜ 名义 $5.2k* ｜ +6.1%
结构参考：355（+1.8%）上方 / 315（-9.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 20.2k / P 12.4k
ΔOI:      C +1.6k / P +2.3k
ATM:      C 5.95 / P 4.65
ATM IV:   32.9%
ΔOI Δ Exposure*: -79k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 355 ｜ -681 ｜ $2.90 ｜ 名义 $-197.5k* ｜ +1.8%
C 380 ｜ +415 ｜ $0.17 ｜ 名义 $7.1k* ｜ +9.0%
P 335 ｜ +326 ｜ $1.14 ｜ 名义 $37.2k* ｜ -3.9%
结构参考：380（+9.0%）上方 / 335（-3.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 101.8k / P 77.7k
ΔOI:      C +27.1k / P +13.9k
ATM:      C 7.84 / P 6.30
ATM IV:   36.6%
ΔOI Δ Exposure*: 202k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 372 ｜ +5,450 ｜ $0.98 ｜ 名义 $534.1k* ｜ +6.8%
C 360 ｜ +3,348 ｜ $3.00 ｜ 名义 $1.00M* ｜ +3.2%
C 375 ｜ +2,595 ｜ $0.79 ｜ 名义 $205.0k* ｜ +7.5%
结构参考：372（+6.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 5.3k / P 1.9k
ΔOI:      C +2.4k / P +0.6k
ATM:      C 9.25 / P 8.47
ATM IV:   34.2%
ΔOI Δ Exposure*: 7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 375 ｜ +407 ｜ $1.51 ｜ 名义 $61.5k* ｜ +7.5%
C 400 ｜ +354 ｜ $0.32 ｜ 名义 $11.3k* ｜ +14.7%
C 420 ｜ +327 ｜ $0.15 ｜ 名义 $4.9k* ｜ +20.4%
结构参考：375（+7.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/TSLA_evening.json