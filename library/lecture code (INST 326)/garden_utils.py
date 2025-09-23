
"""
garden_utils.py
Utility functions for the Garden Management System (Week 3).
Students can expand this module with more functions as the semester progresses.
"""

from datetime import date, timedelta

# Example frost date (College Park, MD). Update as needed.
FROST_DATE = date(2026, 4, 15)

def weeks_before_last_frost(crop: str) -> int:
    """Return recommended weeks to start indoors before last frost."""
    table = {
        "tomato": 6,
        "pepper": 8,
        "basil": 4,
        "eggplant": 8,
        "cucumber": 3,
    }
    return table.get(crop.lower(), 4)

def seed_start_date(crop: str, frost_date: date = FROST_DATE) -> date:
    """Calculate recommended seed start date based on crop and frost date."""
    weeks = weeks_before_last_frost(crop)
    return frost_date - timedelta(weeks=weeks)

def make_label(crop: str, variety: str, start: date) -> str:
    """Return a formatted label for seed starting trays."""
    return f"{crop.title()} — {variety} | Start: {start.isoformat()}"
