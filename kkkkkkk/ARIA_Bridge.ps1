function Abrir-Cerebro { Invoke-Item "C:\Zbrain\Core" }
function Abrir-Cajon { Invoke-Item "C:\Zbrain\cajon\proyectos" }
function Limpiar-Chimenea { 
    Remove-Item "C:\Zbrain\*.tmp" -ErrorAction SilentlyContinue
    Write-Host "Chimenea limpia, Guille." -ForegroundColor Cyan
}
