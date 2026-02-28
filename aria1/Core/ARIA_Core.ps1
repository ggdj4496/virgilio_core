while($true) {
    if (Test-Path 'C:\Zbrain\Core\bridge_cmd.txt') {
        $cmd = Get-Content 'C:\Zbrain\Core\bridge_cmd.txt' -Raw
        if ($cmd -match 'CREA') {
            'HOLA' | Out-File 'C:\Zbrain\ZBRAIN_AUTO.txt' -Force
            '[' + (Get-Date -Format 'HH:mm:ss') + '] ARIA: Archivo ZBRAIN_AUTO creado. Sincronía OK.' | Out-File 'C:\Zbrain\Core\bridge_cmd.txt' -Append
        }
        # Limpiar puente para nueva orden cada 2 segundos
        Start-Sleep -Seconds 2
        Clear-Content 'C:\Zbrain\Core\bridge_cmd.txt' -ErrorAction SilentlyContinue
    }
    Start-Sleep -Seconds 1
}
