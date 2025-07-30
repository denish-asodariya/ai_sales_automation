# AI Sales Automation Dashboard

This project demonstrates an **AI-powered sales automation system** that helps sales teams save hours weekly.  
It provides a Flask-based dashboard to:

- Generate personalized follow-up emails with GPT-4o  
- Classify leads into **Hot / Warm / Cold** priority  
- Store interactions in a **SQLite database**  
- Sync data to **Airtable**  
- Trigger **Zapier webhooks** for Hot leads (e.g. Slack, Email, Google Sheets)  

---

## 🚀 Features

- **Lead Entry Form**: Add leads with name, email, and product interest.  
- **AI Email Generation**: Auto-creates professional follow-up emails.  
- **AI Lead Scoring**: Classifies leads into Hot, Warm, or Cold.  
- **Local Storage**: Persists leads in SQLite.  
- **Airtable Sync**: Automatically pushes each lead into your Airtable base.  
- **Zapier Notifications**: Instantly alerts sales reps when a Hot lead is added.  

---

## 🛠️ Tech Stack

- **Backend**: Python 3.9+, Flask  
- **Database**: SQLite (via SQLAlchemy)  
- **AI**: OpenAI GPT-4o-mini  
- **Integrations**: Airtable API, Zapier Webhooks  
- **Env Management**: python-dotenv  

---

## 📂 Project Structure

```

ai\_sales\_automation/
│
├── README.md
├── requirements.txt
├── .env                # (You must create this)
├── data/
│   └── leads.csv
├── db/
│   └── schema.sql
└── src/
├── app.py
├── email\_generator.py
├── lead\_classifier.py
├── db\_utils.py
├── airtable\_integration.py
├── zapier\_integration.py
├── test\_airtable.py
├── test\_zapier.py
└── static/
└── style.css

````

---

## ⚙️ Setup Instructions

### 1. Clone the Project
```bash
git clone <your-repo-url>
cd ai_sales_automation
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root:

```env
OPENAI_API_KEY=your_openai_key_here
DATABASE_URL=sqlite:///db/automation.db

# Airtable configuration
AIRTABLE_API_KEY=your_airtable_pat_here
AIRTABLE_BASE_ID=appPWRCua1iCMd7vh
AIRTABLE_TABLE_NAME=Leads

# Zapier Webhook
ZAPIER_WEBHOOK_URL=https://hooks.zapier.com/hooks/catch/24003062/uuvqq0h/
```

> ⚠️ Airtable field names must match exactly:
>
> * Name
> * E-mail
> * Product
> * Priority
> * Generated Email

---

### 5. Initialize the Database

```bash
python src/db_utils.py
```

---

### 6. Run the App

```bash
python src/app.py
```

Open in your browser:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔍 Testing Integrations

### ✅ Test Airtable

```bash
python src/test_airtable.py
```

Expected:

```
Lead Test User synced to Airtable.
```

Record will appear in your Airtable `Leads` table.

---

### ✅ Test Zapier

```bash
python src/test_zapier.py
```

Expected:

```
Zapier notified for Zapier Test.
```

Check your Zapier task → Slack/Email notification should appear.

---

## 📊 Demo Flow (For Loom Recording)

1. Open the Flask dashboard.
2. Add a new lead:

   * Name: *John Smith*
   * Email: *[john@example.com](mailto:john@example.com)*
   * Product: *SUV*
3. Show the **Priority classification** and **Generated Email** in the table.
4. Switch to Airtable → refresh → record appears.
5. If Priority = Hot → show Slack/Email notification from Zapier.
6. Conclude:

   > “This system saves our sales reps hours weekly by automatically generating follow-ups, prioritizing leads, syncing to Airtable, and notifying our team in real-time.”

---

## 📈 Impact

* Saves **5+ hours per sales rep weekly**
* Provides instant visibility across platforms
* Scales easily as new leads flow in
* Reduces manual CRM data entry

---

## 🧑‍💻 Author

Denish Asodariya
Master’s in Computer Science | AI & Automation Enthusiast


