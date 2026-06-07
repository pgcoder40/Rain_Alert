# 🌧️ Rain Alert

- Rain Alert is a Python project that fetches real-time weather data using the OpenWeather API and notifies the user when rain is expected.  
- It helps you prepare in advance by sending an umbrella alert whenever rainfall conditions are detected.

## 📂 Project Structure
rain_alert/

│── main.py (Core script)

│── requirements.txt  (Dependencies)

│── README.md         (Documentation)

---

## ⚙️ How It Works
1. **Fetch weather forecast** from OpenWeather API (based on latitude/longitude).  
2. **Check rain conditions** using weather codes (<700).  
3. **Trigger SMS alert** via Twilio if rain is expected.  
4. **Send notification** to your mobile number.  
5. **Run daily** via GitHub Actions (cron schedule).  

---

## 📑 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rain_alert.git
cd rain_alert

2. Add Dependencies
Create a requirements.txt file:
requests
twilio

3. Configure GitHub Secrets
Go to Settings → Secrets → Actions in your repository and add:

OWM_API_KEY → OpenWeather API key

ACCOUNT_SID → Twilio Account SID

AUTH_TOKEN → Twilio Auth Token

4. Prepare Files
main.py → contains the rain alert logic

requirements.txt → lists dependencies

🚀 GitHub Actions Workflow
Example .github/workflows/rain_alert.yml:

yaml
name: Rain Alert

on:
  schedule:
    - cron: "0 23 * * *"   # Runs daily at 4:30 AM IST (11:00 PM UTC)
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run rain alert script
        env:
          OWM_API_KEY: ${{ secrets.OWM_API_KEY }}
          ACCOUNT_SID: ${{ secrets.ACCOUNT_SID }}
          AUTH_TOKEN: ${{ secrets.AUTH_TOKEN }}
        run: python main.py

🎉 Example Output:

When rain is expected:
🌧️ SMS sent: It's going to rain today. Remember to bring an umbrella☔
Weather IDs: [500, 801, 802, 803]

When no rain is forecasted:
☀️ No rain is expected today. You can step out without an umbrella!
Weather IDs: [800, 801, 802, 803]
