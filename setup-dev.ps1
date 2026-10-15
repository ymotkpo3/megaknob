$ErrorActionPreference = "Stop"

Push-Location $PSScriptRoot

try {
    if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
        throw "Python Launcher (py) is not installed."
    }

    & py -3.13 --version

    if ($LASTEXITCODE -ne 0) {
        throw "Python 3.13 is required."
    }

    if (-not (Test-Path ".venv")) {
        Write-Host "Creating virtual environment..."
        & py -3.13 -m venv .venv

        if ($LASTEXITCODE -ne 0) {
            throw "Failed to create virtual environment."
        }
    }

    $python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

    $version = & $python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null

    if ($LASTEXITCODE -ne 0 -or $version -ne "3.13") {
        throw "Existing .venv is invalid or uses another Python version. Rename or remove it and retry."
    }

    Write-Host "Installing Megaknob and development dependencies..."
    & $python -m pip install -e ".[dev]"

    if ($LASTEXITCODE -ne 0) {
        throw "Dependency installation failed."
    }

    Write-Host "Megaknob development environment is ready."
}
finally {
    Pop-Location
}