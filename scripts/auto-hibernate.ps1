# ============================================================
# OPTION-ALERT  auto-hibernate.ps1
# ------------------------------------------------------------
# Puts this PC into hibernate (S4) after a long stretch with no
# real keyboard/mouse input, so the scheduled wake tasks can
# bring it back in time for the briefs.
#
# Why not use Windows' own "hibernate after idle"?
#   This is a Modern Standby (S0) machine with no S3. Its idle
#   hibernate timer only starts counting after the system has
#   entered standby, and standby must stay disabled here because
#   wake timers are not honored reliably from S0. Measured
#   2026-09-19: idle 5 min with hibernate timeout = 2 min -> no
#   hibernation. So we decide ourselves instead.
#
# Driven by task: OPTION-ALERT-AutoHibernate (every 10 minutes)
#
# Examples
#   inspect only : powershell -NoProfile -ExecutionPolicy Bypass -File auto-hibernate.ps1 -DryRun
#   live test    : powershell -NoProfile -ExecutionPolicy Bypass -File auto-hibernate.ps1 -IdleMinutes 0
# ============================================================
param(
    [int]$IdleMinutes = 90,
    [switch]$DryRun
)

$ErrorActionPreference = 'Continue'
$logPath = Join-Path $PSScriptRoot 'auto-hibernate.log'

# Local-time windows where hibernation is forbidden, so that
# wake (08:50 / 20:50) -> brief -> settle always completes.
$protected = @(
    @{ From = [TimeSpan]'08:40'; To = [TimeSpan]'10:20' },
    @{ From = [TimeSpan]'20:40'; To = [TimeSpan]'22:20' }
)

if (-not ('IdleProbe' -as [type])) {
    Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
public static class IdleProbe {
    [StructLayout(LayoutKind.Sequential)]
    private struct LASTINPUTINFO { public uint cbSize; public uint dwTime; }
    [DllImport("user32.dll")]
    private static extern bool GetLastInputInfo(ref LASTINPUTINFO plii);
    public static uint IdleMilliseconds() {
        LASTINPUTINFO li = new LASTINPUTINFO();
        li.cbSize = (uint)Marshal.SizeOf(li);
        if (!GetLastInputInfo(ref li)) { return 0; }
        return (uint)Environment.TickCount - li.dwTime;
    }
}
'@
}

$idleMin  = [IdleProbe]::IdleMilliseconds() / 60000.0
$tod      = (Get-Date).TimeOfDay
$inWindow = $false
foreach ($w in $protected) {
    if ($tod -ge $w.From -and $tod -lt $w.To) { $inWindow = $true; break }
}
$idleTxt = '{0:N1}' -f $idleMin
$stamp   = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'

if ($DryRun) {
    Write-Host ("DRYRUN idle={0} min  threshold={1} min  protectedWindow={2}" -f $idleTxt, $IdleMinutes, $inWindow)
    if ($idleMin -ge $IdleMinutes -and -not $inWindow) { Write-Host '  -> would hibernate' }
    else { Write-Host '  -> no action' }
    return
}

if ($idleMin -ge $IdleMinutes -and -not $inWindow) {
    "$stamp idle=$idleTxt min -> hibernating" | Add-Content -LiteralPath $logPath -Encoding UTF8
    shutdown.exe /h
} elseif ($idleMin -ge $IdleMinutes -and $inWindow) {
    "$stamp idle=$idleTxt min -> hold (protected window)" | Add-Content -LiteralPath $logPath -Encoding UTF8
}
