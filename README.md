project/
│
├── backend/          ← Python code (the brain)
│   ├── main.py       ← Starting point of the app
│   ├── models.py     ← defines Lead, Agent, History tables
│   ├── database.py   ← connects to database
│   └── routes/       ← different features
│       ├── analytics.py    ← dashboard numbers
│       ├── csv_import.py   ← upload CSV files
│       └── assignment.py   ← assign leads to agents
│
└── frontend/         ← React website (what you see)
    └── components/
        ├── StatsCards.js      ← total leads, revenue boxes
        ├── SourceChart.js     ← bar chart
        ├── SourcePieChart.js  ← pie chart
        ├── AgentLeaderboard.js← agent rankings
        └── RevenueTrend.js    ← revenue graph
