from toolkit.exceptions import InvalidUserError


def validate_user(user: dict) -> bool:
    if not user.get("name"):
        raise InvalidUserError("User name is required")

    if not user.get("email"):
        raise InvalidUserError("User email is required")

    age = int(user.get("age", 0))

    if age < 18:
        raise InvalidUserError("User must be at least 18 years old")

    return True