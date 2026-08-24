# VIX / Volatility Environment v1.1（FROZEN 2026-08-24）

## 一、定位

VIX 是系统的**上层波动率环境锚（Volatility Regime Anchor）**，不是普通标的，不是方向信号。

它只回答一个问题：**当前市场处于什么波动环境？**
它永远不回答：市场会涨还是会跌。

## 二、数据层（后台保存，全部要求真实数据）

| 字段 | 来源 | 状态 |
|---|---|---|
| VIX Level（现货价） | yfinance `^VIX` | 现在可用 |
| VIX 1D Δ% | VIX 历史收盘 | 现在可用 |
| VIX 5D Δ% | VIX 历史收盘 | 现在可用 |
| VIX 20D/60D 百分位 | 历史积累 | 待积累（≥20期） |
| VIX 期限结构（VIX3M/VIX6M） | 待验证数据源 | 抓不到则标 N/A |
| VIX Shock | 由 1D Δ% 派生 | 后台记录，v1 不显示 |

规则：抓不到的字段一律标 null / N/A / 待积累，**不估算、不编造**。

## 三、Vol Regime 计算规则（冻结 v1）

```yaml
vol_regime:
  version: vol_regime_v1
  rule_freeze_date: "2026-08-24"
  classification_type: descriptive      # 专家经验分桶，非统计校准
  calibration_status: uncalibrated      # 15/20/25 不是证明出的临界点
  required_input: vix_level             # 缺失 → label = INSUFFICIENT_DATA
  buckets:                              # 半开区间 [min, max)
    LOW:      [null, 15)
    NORMAL:   [15,   20)
    ELEVATED: [20,   25)
    STRESS:   [25,   null)
  optional_evidence: [vix_1d_pct, vix_5d_pct, vix_percentile_20d, vix_term_structure]
  calibration_note: "v1 为经验默认阈值，待历史数据校准"
  not_direction: true
  gate_effect: none_in_v1
```

规则（不可破坏）：

- 标签只由 `vix_level` 决定，动量/百分位/期限结构**只存 evidence、不改标签**；
- 辅助数据缺失 → `evidence_completeness = partial`，标签不受影响；
- `vix_level` 缺失 → 标签 = INSUFFICIENT_DATA，不猜数；
- "辅助数据不全" ≠ "regime 无法判定"，两个概念分开。

## 四、VIX Shock（冻结 v1，预提交）

```yaml
vix_shock:
  version: vix_shock_v1
  metric: vix_1d_pct
  thresholds: {elevated: 10, extreme: 20}   # |1D Δ%|，经验默认，待历史校准
  display: false
  affects_regime: false
  affects_direction: false
  affects_gate: false
```

1D 数据缺失 → N/A，不推断。v1 不显示、不影响任何计分。

## 五、时间口径（写死）

- 按**实际美东时间**判定：≥16:00 → `basis = close`；<16:00 → `basis = intraday`；
  - 晨报（10:15）天然 intraday；晚报（16:30）天然 close；
  - FORCE 手动运行即使盘中按"晚报"生成，也诚实标 intraday（不许谎报 close）；
- 1D/5D 变化统一相对**前收盘 / 5 个交易日前的收盘**，按交易日对齐（跳过周末/假日）；
- 快照日当天的收盘不得当作"前收盘"。

## 六、存储结构（快照 context + Event）

```json
"vol_environment": {
  "vix": {
    "value": 15.67,
    "timestamp": "2026-08-24T10:15:00-04:00",
    "basis": "intraday",
    "prior_close": 15.48,
    "change_1d_pct": 1.2,
    "change_5d_pct": 8.4
  },
  "regime": {
    "label": "NORMAL",
    "rule_version": "vol_regime_v1",
    "classification_type": "descriptive",
    "calibration_status": "uncalibrated",
    "inputs": {
      "vix_level": 15.67,
      "vix_1d_pct": 1.2,
      "vix_5d_pct": 8.4,
      "vix_percentile_20d": null,
      "vix_term_structure": null
    },
    "evidence_completeness": "partial",
    "transition": { "from": "NORMAL", "to": "NORMAL", "changed": false }
  },
  "shock": {
    "version": "vix_shock_v1",
    "level": "NONE",
    "value": 0,
    "display": false
  }
}
```

事件保存**完整对象**（label + rule_version + 原始 inputs），不存字符串。未来 vol_regime_v2 上线后，旧 Event 仍能证明"当时为什么标 NORMAL"。

## 七、分析消费点

1. **Direction Edge —— 禁止进入（红线）**：VIX ↑ ≠ Bearish，Direction 只由 Trend / RS / Price Structure 决定。
2. **Volatility Edge —— v1 不进**：保持现有公式；未来只作为条件变量，需分环境历史验证。
3. **Gate —— v1 不参与**：数据验证前不影响资格与决策。
4. **Setup 触发条件 —— 禁止**：Setup 只由 Gamma + Price + Confirmation 触发，VIX 永远不是触发条件。
5. **Setup 环境标签**：每个 Setup 记录所在 vol_regime，未来输出分环境胜率。
6. **IV–VIX Spread**：每标的的相对波动率 Proxy（见下）。

## 八、IV–VIX Spread（每标的）

公式：`SOXX ATM IV − VIX`

- **P1（现在）**：近月 ATM IV − VIX，输出 raw 值，**标注 Proxy**；只在 Setup 触发时显示；不设绝对"异常"阈值。
- **P2（数据积累后）**：SOXX 30D IV − VIX(30D)，期限对齐后算 5D/20D/60D 百分位，输出"是否历史极端"。

措辞纪律：**不直接说"半导体风险溢价、越大越贵"**——差值可能来自 realized vol、行业结构、期限错配、指数构成、skew/smile；只作相对波动率 Proxy，不直接代表期权定价贵/便宜。

## 九、报告呈现

### 9.1 顶部市场环境块（每份报告一次）

```
📊 市场环境
SPY $764.19 ｜ QQQ $701.40
VIX 15.67 ↑1.2%（5D +8.4%）｜ Vol Regime: NORMAL
CNN 恐惧贪婪 56（Greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。
```

### 9.2 每标的（只在 Setup 触发时出现，不重复 VIX 数字）

```
   ⇒ IV–VIX Spread: +23.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
...
Setup: Setup A 触发（Core 2/3 满足）
环境: Vol NORMAL（仅环境标签，不参与计票）
```

无 Setup 时，每标的**不出现**任何 VIX 相关行。

## 十、红线纪律

1. VIX ↑ 只等于"SPX 期权隐含的近 30 日预期波动率上升"，不等于看跌；
2. VIX 不进 Direction Edge、不参与 Gate、**不是 Setup 触发条件**（v1 及以后默认）；
3. 期限未对齐一律标 Proxy；
4. 抓不到的数据标 N/A / 待积累，不估算；
5. 阈值版本化、待校准，不硬编码成真理；
6. 不重复进每个 ticker（顶部一次）；
7. 历史不足时不设绝对"异常"阈值；
8. v1 不新增 VIX9D / VVIX / SKEW 等指标（冻结）。

## 十一、数据积累后的升级路径（P2）

1. VIX 20D/60D 百分位 → 输出"当前 VIX 处于历史什么位置"；
2. SOXX 30D IV − VIX(30D) → 精确 IV–VIX Spread + 历史百分位；
3. Setup 分环境胜率统计（N + regime coverage + OOS lift + CI）；
4. 若证明增量信息稳定，Vol Regime 升级为条件变量（进 Volatility Edge / 环境分层验证）；
5. 每次升级都换版本号（vol_regime_v2...），旧 Episode 不重算。
