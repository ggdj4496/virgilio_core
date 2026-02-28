$s = New-Object -ComObject Shell.Application
$b = "C:\Zbrain\Core\bridge_cmd.txt"
while($true) {
    if (Test-Path $b) {
        $cmd = Get-Content $b -Raw
        if ($cmd -and $cmd.Trim() -ne "") {
            switch ($cmd.Trim()) {
                "FULL"  { $s.MinimizeAll(); explorer "C:\Zbrain" }
                "LAB"   { explorer "C:\Zbrain\CamasotsLab" }
                "CLEAN" { $s.MinimizeAll() }
            }
            Clear-Content $b
        }
    }
    Start-Sleep -Seconds 1
}
