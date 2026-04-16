import React from "react";
import {
  AppBar,
  Toolbar,
  Typography,
  Container,
  Box,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import PeopleIcon from "@mui/icons-material/People";
import PersonIcon from "@mui/icons-material/Person";
import BarChartIcon from "@mui/icons-material/BarChart";
import SettingsIcon from "@mui/icons-material/Settings";

function Layout({ children }) {
  return (
    <Box sx={{ display: "flex", minHeight: "100vh", background: "#f5f6fa" }}>

      {/* Sidebar */}
      <Box
        sx={{
          width: 240,
          background: "#1e293b",
          color: "white",
          display: "flex",
          flexDirection: "column",
          paddingTop: "20px"
        }}
      >
        <Typography
          variant="h6"
          sx={{ paddingLeft: "20px", marginBottom: "30px" }}
        >
          Analytics
        </Typography>

        <List>

          <ListItemButton sx={{ color: "white" }}>
            <ListItemIcon sx={{ color: "white" }}>
              <DashboardIcon />
            </ListItemIcon>
            <ListItemText primary="Dashboard" />
          </ListItemButton>

          <ListItemButton sx={{ color: "white" }}>
            <ListItemIcon sx={{ color: "white" }}>
              <PeopleIcon />
            </ListItemIcon>
            <ListItemText primary="Leads" />
          </ListItemButton>

          <ListItemButton sx={{ color: "white" }}>
            <ListItemIcon sx={{ color: "white" }}>
              <PersonIcon />
            </ListItemIcon>
            <ListItemText primary="Agents" />
          </ListItemButton>

          <ListItemButton sx={{ color: "white" }}>
            <ListItemIcon sx={{ color: "white" }}>
              <BarChartIcon />
            </ListItemIcon>
            <ListItemText primary="Reports" />
          </ListItemButton>

          <ListItemButton sx={{ color: "white" }}>
            <ListItemIcon sx={{ color: "white" }}>
              <SettingsIcon />
            </ListItemIcon>
            <ListItemText primary="Settings" />
          </ListItemButton>

        </List>

      </Box>

      {/* Main Content */}
      <Box sx={{ flex: 1 }}>

        {/* Top Bar */}
        <AppBar position="static" elevation={1}>
          <Toolbar>
            <Typography variant="h6">
              Lead Analytics Dashboard
            </Typography>
          </Toolbar>
        </AppBar>

        {/* Page Content */}
        <Container maxWidth="lg" sx={{ marginTop: "30px" }}>
          {children}
        </Container>

      </Box>

    </Box>
  );
}

export default Layout;