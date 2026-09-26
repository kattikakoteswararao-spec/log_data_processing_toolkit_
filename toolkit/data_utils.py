def get_names(users: list[dict]) -> list[str]:
    """Return all user names."""
    return [user["name"] for user in users]


def get_adult_users(users: list[dict]) -> list[dict]:
    """Return users whose age is 30 or above."""
    return [user for user in users if int(user["age"]) >= 30]


def create_user_lookup(users: list[dict]) -> dict[int, dict]:
    """Create a dictionary using user ID as the key."""
    return {int(user["id"]): user for user in users}


def user_generator(users: list[dict]):
    """Generate users one at a time."""
    for user in users:
        yield user
        