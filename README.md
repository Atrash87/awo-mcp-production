# AWO MCP Server

MCP (Model Context Protocol) server that exposes processed AWO facility data to AI assistants like Claude Desktop.

## Overview

This MCP server provides a standardized interface between AI assistants and AWO organizational data. It enables natural language queries about AWO facilities, services, and statistics.

**Data Source:** Processed AWO datasets (facilities, addresses, services, providers)

**Status:** ✅ Production-ready

---

## Architecture
User
│
Claude Desktop
│
MCP Server (this repo)
│
Processed AWO Data (CSV)


---

## Features

### Available Tools

| Tool | Description | Example |
|------|-------------|---------|
| `count_facilities(city)` | Count facilities in a city | "How many AWO facilities are in Berlin?" |
| `search_facilities(city)` | List all facilities in a city | "Show me all AWO facilities in Berlin" |
| `get_facility_details(name)` | Get detailed info about a facility | "Tell me about AWO Sozialstation Wedding" |
| `search_services(query)` | Search for services by keyword | "Find addiction services" |
| `generate_statistics()` | Get data statistics | "Show me statistics about AWO facilities" |
| `check_completeness()` | Check data quality | "Check data completeness for AWO records" |
| `detect_duplicates()` | Find duplicate records | "Are there duplicates in the AWO data?" |
| `compare_facilities(f1, f2)` | Compare two facilities | "Compare AWO Mitte and AWO Spree-Wuhle" |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/awo-mcp-production.git
cd awo-mcp-production
``

### 2. Create and Activate Conda Environment

``bash
conda create -n awo-mcp python=3.11
conda activate awo-mcp
``

