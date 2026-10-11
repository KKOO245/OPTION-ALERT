param([string]$Session = "morning")
$ErrorActionPreference = "Stop"

if ($Session -notin @("morning", "evening")) {
    throw "Session must be morning or evening"
}

$REPO = "KKOO245/OPTION-ALERT"
$WORKFLOW_FILE = "daily-brief.yml"
$logDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$logPath = Join-Path $logDir "dispatch-brief.log"

function Write-Log([string]$Message) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $Message"
    Add-Content -LiteralPath $logPath -Value $line -Encoding UTF8
    Write-Host $line
}

try {
    if (-not $env:GH_OPTION_ALERT_TOKEN) {
        $env:GH_OPTION_ALERT_TOKEN = [Environment]::GetEnvironmentVariable("GH_OPTION_ALERT_TOKEN", "User")
    }

    if (Get-Command gh -ErrorAction SilentlyContinue) {
        & gh workflow run $WORKFLOW_FILE --repo $REPO --ref main -f force_send=true -f session=$Session
        if ($LASTEXITCODE -ne 0) { throw "gh workflow run failed: $LASTEXITCODE" }
        Write-Log "[OK] dispatched $Session via gh"
    } elseif ($env:GH_OPTION_ALERT_TOKEN) {
        $headers = @{
            Authorization = "Bearer $($env:GH_OPTION_ALERT_TOKEN)"
            Accept        = "application/vnd.github+json"
        }
        $body = '{"ref":"main","inputs":{"force_send":"true","session":"' + $Session + '"}}'
        Invoke-RestMethod -Method Post `
            -Uri "https://api.github.com/repos/$REPO/actions/workflows/$WORKFLOW_FILE/dispatches" `
            -Headers $headers -Body $body -ContentType "application/json" | Out-Null
        Write-Log "[OK] dispatched $Session via PAT"
    } else {
        throw "No gh and no GH_OPTION_ALERT_TOKEN"
    }
    exit 0
} catch {
    Write-Log "[ERROR] $($_.Exception.Message)"
    exit 1
}
