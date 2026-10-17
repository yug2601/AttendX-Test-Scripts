def login(username, password):
    """Simulate login validation for AttendX."""
    if not username or not password:
        return False
    if username == "student01" and password == "AttendX@123":
        return True
    return False


def test_login_valid_credentials():
    assert login("student01", "AttendX@123") is True


def test_login_invalid_password():
    assert login("student01", "wrongpass") is False


def test_login_empty_username():
    assert login("", "AttendX@123") is False

def test_login_empty_password():
    assert login("student01", "") is False