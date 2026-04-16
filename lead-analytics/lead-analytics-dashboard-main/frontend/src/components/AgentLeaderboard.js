import React from "react";

function AgentLeaderboard({ agents }) {

  const medals = ["🥇", "🥈", "🥉"];

  return (
    <div style={{
      background: "white",
      borderRadius: "8px",
      padding: "20px",
      boxShadow: "0 2px 4px rgba(0,0,0,0.1)"
    }}>
      <h3>Agent Leaderboard</h3>

      {agents.slice(0, 5).map((agent, index) => (
        <div
          key={index}
          style={{
            display: "flex",
            justifyContent: "space-between",
            padding: "10px 0",
            borderBottom: "1px solid #eee"
          }}
        >
          <div>
            {medals[index] || "🏅"} {agent.agent_name}
          </div>

          <div>
            ${agent.revenue.toLocaleString()}
          </div>
        </div>
      ))}

    </div>
  );
}

export default AgentLeaderboard;