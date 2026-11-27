# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $641.80
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-30 262P ΔOI +9,690（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 268.87 → 今开 271.82（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 272.44 ｜ 低 270.68

Options: P/C成交量 2.04 | OI比 1.84 | ATM IV 32.4% | Skew 3.8pp | Term 0.72 | ExpMove ±1.4%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜当日成交偏 Put（P/C量 2.04）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.04×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.84×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±1.4% ｜ 12-01（4D）±1.7% ｜ 12-02（5D）±2.1% ｜ 12-03（6D）±2.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -603,022,310 | GEX Change vs 上次快照 201,948,649 | Flip: Primary Flip: 282.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 1245 / LOW 242 / INVALID 1263
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 282.06（全链重定价，覆盖 93%）
Put Wall 250（弱结构｜现价高于该位 8.4%）
最近结构参考: Flip 282（现价低于该位 3.9%）
量化视角： 负 Gamma（6.03亿，无历史分位）｜负 Gamma 缓解（+2.02亿）｜现价位于 Flip 下方 3.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（Put Wall，弱结构） / 270（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 256.0P — Vol 34,145 | 最新价 $3.08 | OI 31469→62722 (ΔOI +31253张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31253张（+99.3% vs前日OI），连续性待观察（方向未知）
12-18 253.0P — Vol 44,112 | 最新价 $2.47 | OI 27480→48184 (ΔOI +20704张) | ΔOI/Volume 46.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20704张（+75.3% vs前日OI），连续性待观察（方向未知）
11-27 264.0P — Vol 19,676 | 最新价 $0.42 | OI 3232→18463 (ΔOI +15231张) | ΔOI/Volume 77.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15231张（+471.3% vs前日OI），连续性待观察（方向未知）
12-18 250.0P — Vol 71,168 | 最新价 $2.13 | OI 79011→90759 (ΔOI +11748张) | ΔOI/Volume 16.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11748张（+14.9% vs前日OI），连续性待观察（方向未知）
11-30 262.0P — Vol 15,319 | 最新价 $0.73 | OI 1334→11024 (ΔOI +9690张) | ΔOI/Volume 63.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9690张（+726.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 88,626 张（Put 88,626 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $17M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 134.1k / P 246.4k，今日成交量: C 48.6k / P 98.9k，平值价格ATM: C $0.59 / P $0.79 ｜ ATM IV 32.4%，预期波动 ±0.5%，Max Pain 270
Top ΔOI: P 264 +15,231 ｜ P 254 +3,603 ｜ P 260 +2,854

📆 Forward Expiration Structure

11-30  C +6.6k / P +13.0k ｜ Activity HIGH ｜ 3D
12-01  C +1.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 4D
12-02  C +2.6k / P +1.5k ｜ Activity HIGH ｜ 5D
12-03  C +1.4k / P +3.5k ｜ Activity HIGH ｜ 6D

📆 11-30 Forward Structure
存量OI: C 32.0k / P 88.5k，今日变化ΔOI: C +6.6k / P +13.0k，平值价格ATM: C $1.92 / P $1.99 ｜ ATM IV 18.8%，净 delta 敞口 37k shares
Top ΔOI: P 262 +9,690 ｜ P 264 +2,795 ｜ P 255 +2,539
仓位参考: Max Pain 269 ｜ Call Wall 276（+1.8%，弱）（OI 4.1k） ｜ Put Wall 262（-3.3%，弱）（OI 11.0k）
量化解读： 存量 Put 重｜ATM IV 18.8%｜历史 Rank 67%（近端代理）｜IV/RV 0.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 37,192 股

12-01（MEDIUM △）Top ΔOI: 277C +516 ｜ 278C +420
12-01（MEDIUM △）仓位参考: Max Pain 265 ｜ Call Wall 277（+2.2%，弱）（OI 3.6k） ｜ Put Wall 260（-4.1%）（OI 6.2k）

📆 12-02 Forward Structure
存量OI: C 6.7k / P 12.2k，今日变化ΔOI: C +2.6k / P +1.5k，平值价格ATM: C $2.94 / P $2.76 ｜ ATM IV 21.9%，净 delta 敞口 70k shares
Top ΔOI: C 275 +1,472 ｜ P 252 +633 ｜ P 245 +299
仓位参考: Max Pain 265 ｜ Call Wall 275（+1.5%）（OI 1.6k） ｜ Put Wall 260（-4.1%）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.9%｜历史 Rank 67%（近端代理）｜IV/RV 0.72×（近似）｜净 delta 敞口 正 69,606 股

📆 12-03 Forward Structure
存量OI: C 4.9k / P 14.4k，今日变化ΔOI: C +1.4k / P +3.5k，平值价格ATM: C $3.25 / P $3.24 ｜ ATM IV 22.8%，净 delta 敞口 17k shares
Top ΔOI: P 262 +341
仓位参考: Max Pain 266 ｜ Call Wall 269（-0.8%，弱）（OI 0.9k） ｜ Put Wall 250（-7.8%）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 22.8%｜历史 Rank 67%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 正 17,360 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/IWM_morning.json