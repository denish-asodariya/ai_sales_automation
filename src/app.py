from flask import Flask, render_template_string, request, redirect
from sqlalchemy import create_engine, text
from email_generator import generate_email
from lead_classifier import classify_lead
from airtable_integration import push_to_airtable
from zapier_integration import notify_zapier
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db/automation.db")
engine = create_engine(DATABASE_URL)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>AI Sales Automation Dashboard</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <h1>AI Sales Automation</h1>
  <form method="post">
    Name: <input type="text" name="name"><br>
    Email: <input type="text" name="email"><br>
    Product: <input type="text" name="product"><br>
    <button type="submit">Generate</button>
  </form>
  <hr>
  <h2>Leads</h2>
  <table border="1">
    <tr><th>Name</th><th>Email</th><th>Product</th><th>Priority</th><th>Generated Email</th></tr>
    {% for lead in leads %}
      <tr>
        <td>{{lead[1]}}</td>
        <td>{{lead[2]}}</td>
        <td>{{lead[3]}}</td>
        <td>{{lead[4]}}</td>
        <td>{{lead[5]}}</td>
      </tr>
    {% endfor %}
  </table>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        product = request.form["product"]
        priority = classify_lead(name, product)
        gen_email = generate_email(name, product)
        
        # Save to local DB
        with engine.begin() as conn:
            conn.execute(
                text("INSERT INTO leads (name, email, product, priority, generated_email) VALUES (:n, :e, :p, :pr, :ge)"),
                {"n": name, "e": email, "p": product, "pr": priority, "ge": gen_email}
            )
        
        # Push to Airtable
        push_to_airtable(name, email, product, priority, gen_email)
        
        # Trigger Zapier if HOT lead
        if "Hot" in priority:
            notify_zapier(name, email, product, priority)
        
        return redirect("/")
    
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM leads")).fetchall()
    return render_template_string(HTML_TEMPLATE, leads=rows)

if __name__ == "__main__":
    app.run(debug=True)
