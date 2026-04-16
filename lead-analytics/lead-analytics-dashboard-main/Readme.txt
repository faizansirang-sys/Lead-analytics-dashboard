 Lead Analytics Dashboard

A full-stack lead management and analytics system built with **FastAPI (backend)** and **React (frontend)**.
The system automatically assigns incoming leads to agents, tracks lead status changes, and provides real-time analytics through a dashboard.

---

# Features

### Lead Assignment Engine

* Incoming leads are automatically assigned to the **agent with the fewest open leads**
* Each agent has a **maximum capacity of 10 open leads**
* Ensures fair workload distribution across agents

### Lead Status Management

Leads can be updated with statuses such as:

* New
* Converted
* Rejected
* Closed

Rejected leads can be reassigned automatically.

### Agent Workload Tracking

The system tracks how many open leads each agent currently manages.

Endpoint:

```
GET /api/agents/workload
```

---

### Analytics Dashboard

The React dashboard visualizes:

* Total leads
* Conversion rate
* Revenue generated
* Leads by source
* Agent performance

Charts included:

* Leads by Source (Bar Chart)
* Lead Source Distribution (Pie Chart)
* Revenue Trend by Agent
* Top Performing Agents Table

---

### CSV Data Import

Bulk lead data can be uploaded using CSV files.

Endpoint:

```
POST /api/upload-csv
```

This allows the system to ingest large datasets for analytics.

---

# System Architecture

```
React Frontend
      ↓
FastAPI Backend
      ↓
SQLite Database
```

Frontend runs on:

```
http://localhost:3000
```

Backend runs on:

```
http://127.0.0.1:8001
```

API documentation is available at:

```
http://127.0.0.1:8001/docs
```

---

# Installation

## 1. Clone the Repository

```
git clone <repository-url>
cd lead-analytics
```

---

# Backend Setup

Navigate to the backend directory:

```
cd backend
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the FastAPI server:

```
uvicorn main:app --reload --port 8001
```

Backend will start at:

```
http://127.0.0.1:8001
```

---

# Frontend Setup

Navigate to the frontend directory:

```
cd frontend
```

Install dependencies:

```
npm install
```

Start the React development server:

```
npm start
```

Open the dashboard:

```
http://localhost:3000
```

---

# Example API Usage

### Create Agent

```
POST /create-agent?name=Sarah Johnson
```

---

### Create Incoming Lead

```
POST /api/leads/incoming
```

Parameters:

```
source = Google Ads
revenue = 5000
```

---

### Update Lead Status

```
PATCH /api/leads/{lead_id}/status
```

Example:

```
lead_id = 1
status = Converted
```

---

### Agent Workload

```
GET /api/agents/workload
```

Returns current open lead counts for each agent.

---

# Scaling Considerations

If the system handled **10,000 leads per hour**, improvements would include:

* Database indexing for faster queries
* Background task queues (Celery / Redis)
* Caching analytics queries
* Horizontal scaling of the API layer

---

# Technologies Used

Backend:

* FastAPI
* SQLAlchemy
* SQLite

Frontend:

* React
* Chart.js
* Axios

---

# Author

Muhammad Musa Kakakhel


