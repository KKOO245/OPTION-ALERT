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
🟡 **单日价格波动**: -2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 100P ΔOI +582（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 104.24 → 收盘 99.65（-4.4%） ｜ 今日高 104.74 ｜ 低 98.69
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.62 | OI比 0.64 | ATM IV 44.9% | Skew -1.3pp | Term 1.00 | ExpMove ±0.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±5.1% ｜ 09-11（14D）±6.6% ｜ 09-18（21D）±8.7% ｜ 09-25（28D）±9.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 97.16 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 523 / LOW 181 / INVALID 338
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈97（全链重定价，覆盖 79%，CONDITIONAL）
Put Wall 80（现价高于该位 24.6%） | Call Wall 104（现价低于该位 4.2%）
最近结构参考: Flip 97（现价高于该位 2.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall）；上方 104（Call Wall）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 108.0C — Vol 14,955 | 最新价 $0.17 | OI 12904→18191 (ΔOI +5287张) | ΔOI/Volume 35.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5287张（+41.0% vs前日OI），连续性待观察（方向未知）
09-18 99.0P — Vol 530 | 最新价 $2.41 | OI 1682→6051 (ΔOI +4369张) | ΔOI/Volume 824.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4369张（+259.8% vs前日OI），连续性待观察（方向未知）
09-04 100.0P — Vol 1,487 | 最新价 $1.25 | OI 2879→6745 (ΔOI +3866张) | ΔOI/Volume 260.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3866张（+134.3% vs前日OI），连续性待观察（方向未知）
09-18 85.0P — Vol 2,604 | 最新价 $0.22 | OI 29096→31509 (ΔOI +2413张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2413张（+8.3% vs前日OI），连续性待观察（方向未知）
09-18 89.0P — Vol 2,020 | 最新价 $0.44 | OI 3304→5635 (ΔOI +2331张) | ΔOI/Volume 115.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2331张（+70.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +2.2k / P +1.0k ｜ Activity MEDIUM △ ｜ 7D
09-11  C +0.1k / P +0.5k ｜ Activity MEDIUM △ ｜ 14D
09-18  C +3.5k / P +5.5k ｜ Activity HIGH ｜ 21D
09-25  C +89 / P +0.7k ｜ Activity HIGH ｜ 28D

   Top ΔOI: 110C +1,368 ｜ 100P +582

   Top ΔOI: 100P +266 ｜ 98P +85

📆 09-18 Forward Structure
OI:       C 251.4k / P 381.6k
ΔOI:      C +3.5k / P +5.5k
ATM:      C 4.30 / P 4.39
ATM IV:   44.9%
ΔOI Δ Exposure*: -194k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 104 ｜ +4,487 ｜ $6.60 ｜ 名义 $2.96M* ｜ +4.4%
C 100 ｜ +2,531 ｜ $4.30 ｜ 名义 $1.09M* ｜ +0.4%
P 85 ｜ -1,685 ｜ $0.35 ｜ 名义 $-59.0k* ｜ -14.7%
结构参考：104（+4.4%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 5.0k / P 5.4k
ΔOI:      C +89 / P +0.7k
ATM:      C 4.95 / P 4.97
ATM IV:   44.8%
ΔOI Δ Exposure*: -16k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 95 ｜ +340 ｜ $2.80 ｜ 名义 $95.2k* ｜ -4.7%
P 86 ｜ +174 ｜ $0.71 ｜ 名义 $12.4k* ｜ -13.7%
P 96 ｜ +76 ｜ $3.10 ｜ 名义 $23.6k* ｜ -3.7%
结构参考：95（-4.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/GDX_evening.json