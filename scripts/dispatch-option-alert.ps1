# OPTION-ALERT 本地触发器（workflow_dispatch）
#
# 两种方式二选一（都不需要付费）：
#   A) 已安装 GitHub CLI：gh auth login 后直接可用
#   B) 未安装 gh：设置环境变量 GH_OPTION_ALERT_TOKEN（带 workflow 权限的 PAT）
#
# 用法：
#   powershell -NoProfile -ExecutionPolicy Bypass -File dispatch-option-alert.ps1 -Session morning
#   powershell -NoProfile -ExecutionPolicy Bypass -File dispatch-option-alert.ps1 -Session evening
#
# force_send=true + session=morning|evening：忽略时间、精确只发指定会话（不会重发另一份）。

param([string]$Session = "morning")

$ErrorActionPreference = "Stop"

if ($Session -notin @("morning", "evening")) {
    throw "Session 必须是 morning 或 evening"
}

$REPO = "KKOO245/OPTION-ALERT"
$WORKFLOW_FILE = "daily-options-report.yml"

if (Get-Command gh -ErrorAction SilentlyContinue) {
    # 方式 A：GitHub CLI
    & gh workflow run "每日期权报告" --repo $REPO --ref main `
        -f force_send=true -f session=$Session -f use_new_renderer=true
    if ($LASTEXITCODE -ne 0) {
        throw "gh workflow run 失败: $LASTEXITCODE"
    }
} elseif ($env:GH_OPTION_ALERT_TOKEN) {
    # 方式 B：PAT（REST API dispatch）
    $headers = @{
        Authorization = "Bearer $env:GH_OPTION_ALERT_TOKEN"
        Accept        = "application/vnd.github+json"
    }
    $body = '{"ref":"main","inputs":{"force_send":"true","session":"' + $Session + '","use_new_renderer":"true"}}'
    Invoke-RestMethod -Method Post `
        -Uri "https://api.github.com/repos/$REPO/actions/workflows/$WORKFLOW_FILE/dispatches" `
        -Headers $headers -Body $body -ContentType "application/json"
} else {
    throw "未找到 gh 且未设置 GH_OPTION_ALERT_TOKEN。请安装 GitHub CLI 并 gh auth login，或生成带 workflow 权限的 PAT 后执行: setx GH_OPTION_ALERT_TOKEN 你的token"
}

Write-Host "[OK] $(Get-Date -Format 'yyyy-MM-dd HH:mm') 已触发 $Session"
