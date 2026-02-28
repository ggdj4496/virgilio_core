# ARIA REMOTE CONTROL AGENT (Base en t?cnica TeamViewer)
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   ARIA REMOTE CONTROL - CAMASOTS HOST    " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
$signalFile = "C:\Zbrain\Core\remote_signal.txt"

if (!(Test-Path $signalFile)) { New-Item $signalFile -Force }

Write-Host "[SISTEMA] Esperando se?al de ARIA..." -ForegroundColor Gray

while ($true) {
    $order = Get-Content $signalFile | Select-Object -First 1
    if ($order) {
        Write-Host "[ARIA_REMOTE] Ejecutando: $order" -ForegroundColor Yellow
        try {
            if ($order -match "^http") { Start-Process $order }
            else { iex $order } # Ejecuci?n directa de comandos
            Clear-Content $signalFile
            Write-Host "[OK] Orden procesada con ?xito." -ForegroundColor Green
        } catch {
            Write-Host "[ERROR] No se pudo ejecutar la acci?n." -ForegroundColor Red
            Clear-Content $signalFile
        }
    }
    Start-Sleep -Milliseconds 500
}
