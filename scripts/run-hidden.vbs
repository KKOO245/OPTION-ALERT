' run-hidden.vbs
' Launches auto-hibernate.ps1 with NO visible console window.
'
' Why: the scheduled task used to run powershell.exe directly, which lets
' conhost create a console window before -WindowStyle Hidden takes effect,
' so the window flashed on screen every 10 minutes.
'
' Use this file as the scheduled-task action instead:
'   wscript.exe //B "C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\run-hidden.vbs"
'
' Created 2026-09-19.

Dim sh, ps1
ps1 = "C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\auto-hibernate.ps1"

Set sh = CreateObject("WScript.Shell")
sh.Run "powershell.exe -NoProfile -ExecutionPolicy Bypass -File """ & ps1 & """", 0, True
