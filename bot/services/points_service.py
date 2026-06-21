from bot.core.config import POINT_SYSTEM

def generate_points(quantity: int) -> list[int]:
    """Return the points list sized to the given number of drivers."""
    points = POINT_SYSTEM

    if quantity <= len(points):
        return points[:quantity]
    
    return [0] * (quantity - len(points)) + points