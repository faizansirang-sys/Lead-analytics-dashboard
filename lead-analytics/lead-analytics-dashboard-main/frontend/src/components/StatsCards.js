import React from "react";
import { Grid, Paper, Typography } from "@mui/material";
import PeopleIcon from "@mui/icons-material/People";
import AttachMoneyIcon from "@mui/icons-material/AttachMoney";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";

function StatsCards({ analytics }) {

  const cardStyle = {
    padding: "25px",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    borderRadius: "10px",
    transition: "0.2s",
  };

  const formatNumber = (num) => {
    return num.toLocaleString();
  };

  const formatMoney = (num) => {
    return "$" + num.toLocaleString();
  };

  return (
    <Grid container spacing={3}>

      {/* Total Leads */}
      <Grid item xs={12} md={4}>
        <Paper sx={cardStyle} elevation={3}>
          <div>
            <Typography variant="subtitle2" color="text.secondary">
              Total Leads
            </Typography>

            <Typography variant="h4" fontWeight="bold">
              {formatNumber(analytics.total_leads)}
            </Typography>
          </div>

          <PeopleIcon sx={{ fontSize: 45, color: "#1976d2" }} />
        </Paper>
      </Grid>


      {/* Revenue */}
      <Grid item xs={12} md={4}>
        <Paper sx={cardStyle} elevation={3}>
          <div>
            <Typography variant="subtitle2" color="text.secondary">
              Revenue
            </Typography>

            <Typography variant="h4" fontWeight="bold">
              {formatMoney(analytics.total_revenue)}
            </Typography>
          </div>

          <AttachMoneyIcon sx={{ fontSize: 45, color: "#2e7d32" }} />
        </Paper>
      </Grid>


      {/* Conversion Rate */}
      <Grid item xs={12} md={4}>
        <Paper sx={cardStyle} elevation={3}>
          <div>
            <Typography variant="subtitle2" color="text.secondary">
              Conversion Rate
            </Typography>

            <Typography variant="h4" fontWeight="bold">
              {analytics.conversion_rate}%
            </Typography>
          </div>

          <TrendingUpIcon sx={{ fontSize: 45, color: "#ed6c02" }} />
        </Paper>
      </Grid>

    </Grid>
  );
}

export default StatsCards;