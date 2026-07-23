from datetime import datetime

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>NSE Daily Report</title>
</head>
<body style="font-family: Arial; max-width: 800px; margin: 40px auto;">
    <h1>📈 NSE Daily Report</h1>

    <p>This page was generated automatically by GitHub Actions.</p>

    <h2>Current Time (UTC)</h2>
    <p>{datetime.utcnow()}</p>

    <hr>

    <h2>Today's Summary</h2>

    <ul>
        <li>FII: ₹2,315 Cr</li>
        <li>DII: ₹980 Cr</li>
        <li>Market Mood: Bullish 🚀</li>
    </ul>

</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)

print("Generated index.html")
