# Runs the offline checks for NT3. Usage, from this folder in PowerShell:
#   powershell -ExecutionPolicy Bypass -File .\RUN_CHECKS.ps1
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$venvPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $venvPython)) {
    Write-Host 'Step 1/3: creating a separate Python environment (.venv)...'
    py -3 -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw 'Could not create .venv. See "Common errors" in GUIDE.md.' }
}
Write-Host 'Step 2/3: installing the libraries from requirements.txt...'
& $venvPython -m pip install --disable-pip-version-check -q -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'Installing the libraries failed. See "Common errors" in GUIDE.md.' }

$name = Read-Host 'Full name of the person running this (e.g. Nguyen Hieu An)'
if ([string]::IsNullOrWhiteSpace($name)) { throw 'The name of the person running this must be entered.' }
Write-Host 'Step 3/3: running the 10 scripts and comparing the 15 result tables...'
& $venvPython -X utf8 run_checks.py --executed-by $name
if ($LASTEXITCODE -ne 0) { Write-Host 'A step did not pass. Read KET_QUA.json and execution_logs in the ket_qua folder.' -ForegroundColor Red; exit 1 }
Write-Host 'Done. Read KET_QUA.json and execution_logs in the ket_qua folder before confirming NT3.' -ForegroundColor Green
