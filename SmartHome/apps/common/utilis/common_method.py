def parse_is_generic(value):
    if value is None:
        return None
    if isinstance(value, bool):
        return value

    value = str(value).lower()

    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError("is_generic must be 'true' or 'false'")


def parse_is_deleted(value):
    if value is None:
        return None
    if isinstance(value, bool):
        return value

    value = str(value).lower()

    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError("is_generic must be 'true' or 'false'")

def get_filters(**kwargs):
    """Build filter dict from provided keyword arguments."""
    return {k: v for k, v in kwargs.items() if v is not None}
