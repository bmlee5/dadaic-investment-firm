$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$media_dir = Join-Path (Split-Path -Parent $PSScriptRoot) "DecisionMemo\Media"
$s_en_html = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Slide-EN-261009.html"
$s_en_pdf = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Slide-EN-261009.pdf"

$s_kr_html = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Slide-KR-261009.html"
$s_kr_pdf = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Slide-KR-261009.pdf"

$i_en_html = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Infographic-EN-261009.html"
$i_en_png = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Infographic-EN-261009.png"

$i_kr_html = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Infographic-KR-261009.html"
$i_kr_png = Join-Path $media_dir "PLTR-Investment-Committee-Decision-Memo-Infographic-KR-261009.png"

Write-Host "Rendering Slide EN PDF..."
Start-Process -FilePath $chrome -ArgumentList @("--headless", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=$s_en_pdf", $s_en_html) -Wait

Write-Host "Rendering Slide KR PDF..."
Start-Process -FilePath $chrome -ArgumentList @("--headless", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=$s_kr_pdf", $s_kr_html) -Wait

Write-Host "Rendering Infographic EN PNG..."
Start-Process -FilePath $chrome -ArgumentList @("--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,2400", "--screenshot=$i_en_png", $i_en_html) -Wait

Write-Host "Rendering Infographic KR PNG..."
Start-Process -FilePath $chrome -ArgumentList @("--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,2400", "--screenshot=$i_kr_png", $i_kr_html) -Wait

Write-Host "Render Complete."
