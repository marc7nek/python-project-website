from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst", 
    "location": "Bengaluru, India",
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Bangalore, India",
  },
  { 
    "id": 3,
    "title": "Data Engineer",
    "location": "Mumbai, India"  
  },
  {
    "id": 4,
    "title": "Data Architect",
    "location": "Hyderabad, India",
    "salary": 'Rs. 75,00,000'
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)