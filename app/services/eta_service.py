from app.config import AVG_TIME_PER_STOP_MINUTES

def calculate_eta(remaining_stops: int) -> str:
    min_eta = remaining_stops * AVG_TIME_PER_STOP_MINUTES
    max_eta = min_eta + 5
    return f"{min_eta}–{max_eta} minutes"
