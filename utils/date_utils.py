from datetime import datetime


def format_epoch_to_str(epoch_time: int) -> str:
    """Converts a Unix epoch timestamp to a 'YYYY-MM-DD' string format."""
    return datetime.fromtimestamp(epoch_time).strftime("%Y-%m-%d")
