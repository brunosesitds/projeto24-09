# Empacotar projeto em ZIP - Powershell
$src = Split-Path -Parent $MyInvocation.MyCommand.Path
$zip = Join-Path $src 'entrega_projeto_tkinter.zip'
if (Test-Path $zip) { Remove-Item $zip }
Compress-Archive -Path (Join-Path $src '*') -DestinationPath $zip -Force
Write-Output "Arquivo gerado: $zip"
