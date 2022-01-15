from app.main import is_google_available, is_github_available


def test_is_google_available():
    assert is_google_available()


def test_is_github_available():
    assert is_github_available()
