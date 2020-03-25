"""Advanced calculator interpreter."""


def remove_spaces(expression: str) -> str:
    """Remove the additional spaces from a given expression."""
    return ''.join(expression.split())
