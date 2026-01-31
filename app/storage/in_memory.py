from datetime import datetime
from app.models.route import Route
from app.models.bus import Bus

# --------------------
# ROUTES
# --------------------
routes = {
    "ROUTE-1": Route(
        id="ROUTE-1",
        name="Hostel to Academic Block",
        stops=["Hostel", "Main Gate", "Library", "Academic Block"]
    ),

    "ROUTE-2": Route(
        id="ROUTE-2",
        name="City Gate to Hostel",
        stops=["City Gate", "Sports Complex", "Main Gate", "Hostel"]
    ),

    "ROUTE-3": Route(
        id="ROUTE-3",
        name="Faculty Housing Loop",
        stops=["Faculty Housing", "Admin Block", "Library", "Faculty Housing"]
    )
}

# --------------------
# BUSES
# --------------------
buses = {
    "BUS-1": Bus(
        id="BUS-1",
        route_id="ROUTE-1",
        current_stop_index=0,
        last_updated_at=datetime.utcnow()
    ),

    "BUS-2": Bus(
        id="BUS-2",
        route_id="ROUTE-1",
        current_stop_index=2,
        last_updated_at=datetime.utcnow()
    ),

    "BUS-3": Bus(
        id="BUS-3",
        route_id="ROUTE-2",
        current_stop_index=1,
        last_updated_at=datetime.utcnow()
    ),

    "BUS-4": Bus(
        id="BUS-4",
        route_id="ROUTE-3",
        current_stop_index=0,
        last_updated_at=datetime.utcnow()
    )
}
