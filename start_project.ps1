$projectRoot = "C:\Users\mohit\Desktop\AI Material Management System"
$backendDir = Join-Path $projectRoot "backend"

Set-Location $backendDir
Write-Host "Starting AI Material Management System backend..." -ForegroundColor Green
Start-Process -FilePath "C:\Python313\python.exe" -ArgumentList "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000" -WorkingDirectory $backendDir

Start-Sleep -Seconds 3
Write-Host "Opening frontend..." -ForegroundColor Cyan
Start-Process "file:///C:/Users/mohit/Desktop/AI%20Material%20Management%20System/frontend/index.html"
