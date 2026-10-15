$ErrorActionPreference = "Stop"

Push-Location $PSScriptRoot

try {
    & ".\.venv\Scripts\python.exe" -m python_app.main
}
finally {
    Pop-Location
}