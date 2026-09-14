# 本机主检测包装：19:00-23:00 ET 建议每 10-15 分钟运行（Windows 任务计划）
# 需先设置环境变量 DISCORD_BRIEF_WEBHOOK_URL（新简报 server）。
param([string]$Repo = "D:\git\Option Alert-数据储存")
$ErrorActionPreference = "Stop"
Set-Location $Repo
git pull --rebase origin main
python scripts\oi_ready_watch.py --runner local
if ($LASTEXITCODE -ne 0) { throw "oi_ready_watch.py 失败: $LASTEXITCODE" }
git add data/history
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "OI 就绪状态 $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    git push
}
