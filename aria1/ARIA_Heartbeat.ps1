$fecha = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$status = "ARIA Activa en Camasotz"
$cpu = (Get-CimInstance Win32_Processor).LoadPercentage
$memoria = (Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB
$log = "[$fecha] Status: $status | CPU: $cpu% | RAM Libre: $("{0:N2}" -f $memoria) MB"
$log | Out-File -FilePath "C:\Zbrain\Core\Reportes\ultimo_pulso.txt" -Append
Write-Host "[ARIA] Pulso registrado en Reportes." -ForegroundColor Magenta
