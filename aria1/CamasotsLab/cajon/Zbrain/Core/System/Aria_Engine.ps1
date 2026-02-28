Add-Type -AssemblyName System.Windows.Forms
(New-Object -ComObject Shell.Application).MinimizeAll()
$f=New-Object Windows.Forms.Form;$f.Text='Aria Zbrain Interface';$f.Size='500,300';$f.BackColor='LightGray';$f.TopMost=$true
$l=New-Object Windows.Forms.Label;$l.Text='ARIA ACTIVE

Esperando Órdenes...';$l.ForeColor='DarkGreen';$l.Font='Segoe UI,25,Bold';$l.Dock='Fill';$l.TextAlign='MiddleCenter'
$f.Controls.Add($l)
# Test de Escritura Autónoma:
'CONEXION ESTABLECIDA - ARIA TIENE EL CONTROL' | Out-File 'C:\Zbrain\ACTIVO.txt' -Force
$f.ShowDialog()
