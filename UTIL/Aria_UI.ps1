Add-Type -AssemblyName System.Windows.Forms
$f=New-Object Windows.Forms.Form;$f.Text='Aria Core';$f.Size='500,300';$f.BackColor='LightGray';$f.TopMost=$true;$f.StartPosition='CenterScreen'
$l=New-Object Windows.Forms.Label;$l.Text='aria activa';$l.ForeColor='DarkGreen';$l.Font='Segoe UI,25,Bold';$l.Dock='Fill';$l.TextAlign='MiddleCenter'
$f.Controls.Add($l);
# MINIMIZAR TODO AL MOSTRARSE
(New-Object -ComObject Shell.Application).MinimizeAll()
$f.ShowDialog()
