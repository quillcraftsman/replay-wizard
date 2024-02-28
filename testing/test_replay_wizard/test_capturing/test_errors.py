"""
Test errors module
"""
from replay_wizard.capturing.errors import UnknownKeyError


class TestUnknownKeyError:
    """
    Test UnknownKeyError
    """

    def test_str(self):
        """
        Test str method
        """
        e = UnknownKeyError()
        assert str(e) == 'Key was unknown (None value)'
