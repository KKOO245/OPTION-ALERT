# 期权晨报 2026-08-24

市场背景： SPY $765.09 ｜ VIX 15.68 ｜ CNN 恐惧贪婪 56.4（greed）

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 519.52 → 今晨 508.32（-2.2%） | 较昨收变动（含盘初走势）


## SOXX

Options: P/C量 2.07 | OI比 0.73 | ATM IV 49.0% | Skew 3.5pp | Term 0.86 | ExpMove ±4.3% | Rank — (历史不足)
   ⇒ Put/Call Volume: 2.07×（Put 成交显著高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构不一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: NEGATIVE | GEX(存量) N/A | GEX Change N/A | Flip: N/A
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: N/A（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 500: +1.7% | 距 Call Wall 670: -24.1%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall）；上方 670（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 430.0P — Vol N/A | OI 883→4712 (ΔOI +3829张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增3829张（+433.6% vs前日OI），连续性待观察（方向未知）
09-18 485.0P — Vol N/A | OI 2064→4068 (ΔOI +2004张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2004张（+97.1% vs前日OI），连续性待观察（方向未知）
08-28 480.0P — Vol N/A | OI 189→1582 (ΔOI +1393张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1393张（+737.0% vs前日OI），连续性待观察（方向未知）
09-18 590.0C — Vol N/A | OI 4726→5883 (ΔOI +1157张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1157张（+24.5% vs前日OI），连续性待观察（方向未知）
09-18 350.0P — Vol N/A | OI 791→1790 (ΔOI +999张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增999张（+126.3% vs前日OI），连续性待观察（方向未知）
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-24/SOXX_morning.json