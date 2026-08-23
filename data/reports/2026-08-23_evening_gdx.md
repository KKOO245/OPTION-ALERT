# 期权晚报 2026-08-23

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
GDX: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## GDX

Options: P/C量 0.31 | OI比 0.80 | ATM IV 49.9% | Skew -2.0pp | Term 0.99 | ExpMove ±5.5% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.31×（Call 成交高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: POSITIVE | GEX(存量) N/A | GEX Change N/A | Flip: ≈33.29 / ≈57.83 / ≈65.15
结构观察区: 33–58（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 70: +46.9% | 距 Call Wall 100: +2.8%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 70（Put Wall）；上方 100（Call Wall）。
• Gamma 区域：切换参考 33（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 104.0C — Vol N/A | OI 246→13766 (ΔOI +13520张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增13520张（+5495.9%），连续性待观察（方向未知）
08-28 100.0C — Vol N/A | OI 3670→10387 (ΔOI +6717张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增6717张（+183.0%），连续性待观察（方向未知）
08-28 101.0C — Vol N/A | OI 146→6710 (ΔOI +6564张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增6564张（+4495.9%），连续性待观察（方向未知）
08-28 92.0P — Vol N/A | OI 656→6842 (ΔOI +6186张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增6186张（+943.0%），连续性待观察（方向未知）
09-11 92.0P — Vol N/A | OI 11→5049 (ΔOI +5038张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增5038张（+45800.0%），连续性待观察（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-23/GDX_evening.json