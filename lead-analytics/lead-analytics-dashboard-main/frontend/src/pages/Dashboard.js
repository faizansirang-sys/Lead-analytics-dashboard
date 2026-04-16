import React, { useState, useEffect } from "react";
import axios from "axios";
import Layout from "../components/Layout";

import StatsCards from "../components/StatsCards";
import SourceChart from "../components/SourceChart";
import TopAgents from "../components/TopAgents";
import CsvUpload from "../components/CsvUpload";

import RevenueTrend from "../components/RevenueTrend";
import SourcePieChart from "../components/SourcePieChart";
import AgentLeaderboard from "../components/AgentLeaderboard";

const API_BASE = "http://127.0.0.1:8001/api";

function Dashboard() {
  const [analytics, setAnalytics] = useState(null);
  const [sourceData, setSourceData] = useState(null);
  const [topAgents, setTopAgents] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchData = () => {
    setLoading(true);

    axios.get(`${API_BASE}/analytics`).then((res) => {
      setAnalytics(res.data);
    });

    axios.get(`${API_BASE}/analytics/leads-by-source`).then((res) => {
      setSourceData(res.data);
    });

    axios.get(`${API_BASE}/analytics/top-agents`).then((res) => {
      setTopAgents(res.data);
      setLoading(false);
    });
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleUploadSuccess = () => {
    fetchData();
  };

  if (loading) {
    return (
      <Layout>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            height: "60vh",
          }}
        >
          <h2>Loading dashboard...</h2>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <h1 style={{ marginBottom: "30px" }}>Lead Analytics Dashboard</h1>

      {/* CSV Upload */}
      <CsvUpload onSuccess={handleUploadSuccess} />

      {/* Stats */}
      {analytics && <StatsCards analytics={analytics} />}

      {/* First Row Charts */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        {sourceData && <SourceChart data={sourceData} />}
        <TopAgents agents={topAgents} />
      </div>

      {/* Second Row Charts */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        {sourceData && <SourcePieChart data={sourceData} />}
        <RevenueTrend agents={topAgents} />
      </div>

      {/* Leaderboard */}
      <div style={{ marginTop: "30px" }}>
        <AgentLeaderboard agents={topAgents} />
      </div>
    </Layout>
  );
}

export default Dashboard;