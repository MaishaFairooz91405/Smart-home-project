def get_filters(**kwargs):
    """Build filter dict from provided keyword arguments."""
    return {k: v for k, v in kwargs.items() if v is not None}