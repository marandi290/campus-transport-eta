# Campus Transport ETA System

## Overview

Campus transport systems often rely on fixed schedules, but real-world issues like delays, breakdowns, or route changes make these schedules unreliable. Students and staff are left uncertain about when a bus will arrive, while transport staff are overwhelmed with repeated status queries.

This project addresses that gap by building a **lightweight backend service** that improves transparency and trust using **manual checkpoint-based updates** instead of GPS tracking.

---

## Problem Chosen

**Lack of real-time visibility into campus bus movement**.

Specifically:

* Users don’t know the current position of their bus
* Transport staff are repeatedly contacted for updates
* GPS-based tracking is unavailable or unreliable

---

## Solution Overview

The system provides **approximate ETA and bus status** using predefined routes and stops.

Instead of GPS:

* Each route has an ordered list of checkpoints (stops)
* Transport staff manually update when a bus reaches a checkpoint
* The system computes ETA based on remaining stops and an average time per stop

This approach is:

* Simple to operate
* Resilient to GPS failures
* Easy to deploy incrementally

---

## How the System Works

1. **Routes & Stops** are predefined in the system
2. **Buses** are assigned to routes
3. **Staff** update a bus’s current checkpoint via an API
4. **Users** query route status to see:

   * Current stop
   * Next stop
   * Estimated time of arrival (ETA)

The backend acts as a **single source of truth** for bus movement.

---

## Assumptions

* Routes and stops are predefined and ordered
* Buses move sequentially through stops
* Checkpoint updates are made manually by staff
* ETA is approximate and based on average travel time per stop
* Data is stored in-memory (no persistent database)

---

## What This System Does

* Provides APIs for staff to update bus checkpoints
* Provides APIs for users to fetch bus status and ETA
* Supports multiple routes and multiple buses per route
* Improves transparency without complex infrastructure

---

## What This System Does NOT Do

* GPS or live location tracking
* Push notifications or alerts
* Authentication or authorization
* Frontend / mobile UI
* Historical data storage or analytics

These are intentional trade-offs to keep the system focused and simple.

---

## Tech Stack

* **Python 3.11+**
* **FastAPI** for API development
* **Pydantic** for data validation
* **Uvicorn** as ASGI server
* In-memory data structures (no database)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd campus-transport-eta-system
```

### 2. Create Python virtual environment.

```bash
python -m venv venv
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

* **Swagger UI (interactive testing):**

  ```
  http://127.0.0.1:8000/docs
  ```

* **ReDoc (clean documentation):**

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## Example API Usage

### Update Bus Checkpoint (Staff)

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/staff/buses/BUS-1/checkpoint' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "stop_name": "Main Gate"
}'
```

### Get Route Bus Status (Users)

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/routes/ROUTE-1/bus-status' \
  -H 'accept: application/json'
```

---

