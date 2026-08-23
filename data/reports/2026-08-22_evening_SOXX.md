# 期权晚报 2026-08-22

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SOXX: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SOXX

Options: P/C量 4.24 | OI比 N/A | ATM IV N/A | Skew N/A | Term N/A | ExpMove N/A | Rank — (历史不足)
   ⇒ Put/Call Volume: 4.24×（Put 成交显著高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 数据不足
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: NEGATIVE | GEX(存量) N/A | GEX Change N/A | Flip: N/A
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: N/A（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 500: +3.9% | 距 Call Wall 670: -22.5%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall）；上方 670（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 575.0C — Vol N/A | OI 337→7685 (ΔOI +7348张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增7348张（+2180.4%），连续性待观察（方向未知）
08-28 565.0C — Vol N/A | OI 1059→2752 (ΔOI +1693张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1693张（+159.9%），连续性待观察（方向未知）
09-18 540.0P — Vol N/A | OI 780→2085 (ΔOI +1305张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1305张（+167.3%），连续性待观察（方向未知）
09-04 570.0C — Vol N/A | OI 200→1468 (ΔOI +1268张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1268张（+634.0%），连续性待观察（方向未知）
09-18 450.0P — Vol N/A | OI 5741→6435 (ΔOI +694张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增694张（+12.1% vs前日OI），值得跟踪（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-22/SOXX_evening.json