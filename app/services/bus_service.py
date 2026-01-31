from datetime import datetime
from app.storage.in_memory import buses, routes
from app.services.eta_service import calculate_eta

def update_checkpoint(bus_id: str, stop_name: str):
    bus = buses.get(bus_id)
    route = routes.get(bus.route_id)

    if stop_name not in route.stops:
        raise ValueError("Invalid stop for this route")

    bus.current_stop_index = route.stops.index(stop_name)
    bus.last_updated_at = datetime.utcnow()

def get_bus_status(route_id: str):
    route = routes.get(route_id)
    bus = next(b for b in buses.values() if b.route_id == route_id)

    remaining_stops = len(route.stops) - bus.current_stop_index - 1
    eta = calculate_eta(remaining_stops)

    return {
        "route": route.name,
        "bus_id": bus.id,
        "last_checkpoint": route.stops[bus.current_stop_index],
        "last_updated_at": bus.last_updated_at,
        "next_stop": (
            route.stops[bus.current_stop_index + 1]
            if remaining_stops > 0 else None
        ),
        "estimated_arrival": eta
    }
