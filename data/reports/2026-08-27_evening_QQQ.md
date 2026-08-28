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
🟡 **近现价集中开仓**: 08-28 730C ΔOI +5,931（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
QQQ: 今晨 719.09 → 收盘 718.75（-0.0%） ｜ 今日高 721.35 ｜ 低 714.53
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 1.07 | OI比 0.93 | ATM IV 18.0% | Skew 3.5pp | Term 0.99 | ExpMove ±0.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-28（1D）±0.8% ｜ 08-31（4D）±1.1% ｜ 09-01（5D）±1.4% ｜ 09-02（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 711.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2871 / LOW 614 / INVALID 1923
结构观察区: ≈712（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 700: +2.7% | 距 Call Wall 750: -4.2%
最近结构参考: Flip 712（距现价 +1.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall）；上方 750（Call Wall）。
• Gamma 区域：切换参考 712（Top-3 近似，需全链重定价验证）。
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

08-28  C +18.7k / P +24.8k ｜ Activity MEDIUM △ ｜ 1D
08-31  C +22.6k / P +8.9k ｜ Activity HIGH ｜ 4D
09-01  C +4.2k / P +14.9k ｜ Activity HIGH ｜ 5D
09-02  C +5.1k / P +9.3k ｜ Activity HIGH ｜ 6D

   Top ΔOI: 625P +16,283 ｜ 730C +5,931

📆 08-31 Forward Structure
OI:       C 388.0k / P 252.6k
ΔOI:      C +22.6k / P +8.9k
ATM:      C 4.89 / P 3.39
ATM IV:   13.6%
ΔOI Δ Exposure*: 736k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 740 ｜ +6,511 ｜ $0.05 ｜ 名义 $32.6k* ｜ +3.0%
C 725 ｜ +5,856 ｜ $1.84 ｜ 名义 $1.08M* ｜ +0.9%
C 716 ｜ +5,128 ｜ $7.35 ｜ 名义 $3.77M* ｜ -0.4%
结构参考：740（+3.0%）上方 / 716（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-01 Forward Structure
OI:       C 29.2k / P 51.0k
ΔOI:      C +4.2k / P +14.9k
ATM:      C 5.66 / P 4.20
ATM IV:   14.4%
ΔOI Δ Exposure*: 194k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 675 ｜ +7,834 ｜ $0.13 ｜ 名义 $101.8k* ｜ -6.1%
P 676 ｜ +2,344 ｜ $0.16 ｜ 名义 $37.5k* ｜ -5.9%
C 710 ｜ +1,722 ｜ $12.80 ｜ 名义 $2.20M* ｜ -1.2%
结构参考：675（-6.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 13.3k / P 22.4k
ΔOI:      C +5.1k / P +9.3k
ATM:      C 6.98 / P 4.82
ATM IV:   15.4%
ΔOI Δ Exposure*: 130k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 685 ｜ +2,076 ｜ $0.34 ｜ 名义 $70.6k* ｜ -4.7%
P 693 ｜ +1,152 ｜ $0.54 ｜ 名义 $62.2k* ｜ -3.6%
C 728 ｜ +1,082 ｜ $2.57 ｜ 名义 $278.1k* ｜ +1.3%
结构参考：728（+1.3%）上方 / 685（-4.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/QQQ_evening.json