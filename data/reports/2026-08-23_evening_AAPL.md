# 期权晚报 2026-08-23

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
AAPL: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## AAPL

Options: P/C量 0.67 | OI比 0.52 | ATM IV 15.6% | Skew 0.6pp | Term 1.55 | ExpMove ±1.2% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.67×（Call 成交高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: POSITIVE | GEX(存量) N/A | GEX Change N/A | Flip: ≈170.00 / ≈177.50 / ≈315.54
结构观察区: 170–178（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 300: +3.2% | 距 Call Wall 320: -3.2%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 300（Put Wall）；上方 320（Call Wall）。
• Gamma 区域：切换参考 170（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-26 320.0C — Vol N/A | OI 1796→8903 (ΔOI +7107张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增7107张（+395.7%），连续性待观察（方向未知）
08-24 320.0C — Vol N/A | OI 3095→6826 (ΔOI +3731张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增3731张（+120.5%），连续性待观察（方向未知）
08-24 302.5P — Vol N/A | OI 211→3180 (ΔOI +2969张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2969张（+1407.1%），连续性待观察（方向未知）
08-28 322.5C — Vol N/A | OI 1401→3736 (ΔOI +2335张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2335张（+166.7%），连续性待观察（方向未知）
08-28 320.0C — Vol N/A | OI 5110→7142 (ΔOI +2032张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2032张（+39.8%），连续性待观察（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-23/AAPL_evening.json