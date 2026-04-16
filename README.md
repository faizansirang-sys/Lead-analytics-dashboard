Lead Analytics Dashboard & Management System
A high-performance full-stack application designed to streamline call center operations through automated lead distribution and real-time data visualization.

📌 Project Overview
This project solves the challenge of manual lead management by providing a centralized system for data ingestion, automated assignment logic, and executive-level analytics. Built with a focus on speed (FastAPI) and interactivity (React), it ensures that sales teams operate at peak efficiency.

🏗️ System Architecture
The application is built using a modern, decoupled architecture:

Frontend: A responsive React SPA (Single Page Application) utilizing Chart.js for data visualization.

Backend: High-performance FastAPI (Python) server handling RESTful API requests and business logic.

Database: SQLite for lightweight, persistent relational data storage.

Data Layer: Custom CSV Processing Engine for bulk data ingestion and validation.

✨ Key Features
1. Automated Lead Assignment Engine
At the heart of the system is a custom distribution algorithm that ensures a fair workload:

Constraint-Based Logic: Automatically assigns leads to available agents.

Load Balancing: Strictly enforces a maximum of 10 leads per agent to prevent burnout and ensure lead quality.

Real-time Updates: Instantly updates agent status upon assignment.

2. Interactive Analytics Dashboard
Transformed raw operational data into actionable insights:

Revenue Trends: Time-series line graphs showing performance over time.

Distribution Analysis: Pie charts visualizing lead sources and agent status.

Performance Metrics: Bar charts comparing agent conversion rates.

3. Bulk Data Processing
Integrated a robust CSV import feature.

Handles large datasets by validating data types before committing to the SQLite database, preventing data corruption.

🛠️ Tech Stack
Language: Python 3.x, JavaScript (ES6+)

Backend: FastAPI, Pydantic (Data Validation), SQLAlchemy (ORM)

Frontend: React.js, Chart.js, Axios

Database: SQLite

Styling: CSS3 / Tailwind CSS

🚀 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/your-repo-name.git
Backend Setup:

Bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend Setup:

Bash
cd frontend
npm install
npm start
📈 Future Roadmap (AI Integration)
As I prepare for further studies at MBZUAI, I plan to expand this project by:

Lead Scoring: Implementing a Machine Learning model (Scikit-Learn) to predict the "probability of conversion" for each lead based on historical CSV data.

NLP: Adding sentiment analysis for call logs to automatically categorize lead quality.
