"""
Pytest fixtures
"""
from pytest import fixture


@fixture
def mock_argument_parser():
    """
    Mock class for argparse.ArgumentParser
    """

    class MockArgs:
        """
        Mock ArgumentParser args
        """

        def __init__(self):
            self.sequence = 'test'
            self.delay = 0
            self.timedelta = True
            self.keyboard = True
            self.mouse = True
            self.monitoring = True

    class MockArgumentParser:
        """
        Mock for ArgumentParser
        """

        def __init__(self, *args, **kwargs):
            pass

        def add_argument(self, *args, **kwargs):
            """
            Mock add argument method
            """

        def parse_args(self):
            """
            Mock parse args method
            """
            return MockArgs()

    return MockArgumentParser


@fixture
def mock_combine_argument_parser():
    """
    Mock class for argparse.ArgumentParser
    """

    class MockArgs:
        """
        Mock ArgumentParser args
        """

        def __init__(self):
            self.sequence = 'test'
            self.timedelta = False
            self.sequences = ['test', 'test']

    class MockArgumentParser:
        """
        Mock for ArgumentParser
        """

        def __init__(self, *args, **kwargs):
            pass

        def add_argument(self, *args, **kwargs):
            """
            Mock add argument method
            """

        def parse_args(self):
            """
            Mock parse args method
            """
            return MockArgs()

    return MockArgumentParser


@fixture
def mock_list_argument_parser():
    """
    Mock class for argparse.ArgumentParser
    """

    class MockArgs:
        """
        Mock ArgumentParser args
        """

        def __init__(self):
            self.extension = 's'

    class MockArgumentParser:
        """
        Mock for ArgumentParser
        """

        def __init__(self, *args, **kwargs):
            pass

        def add_argument(self, *args, **kwargs):
            """
            Mock add argument method
            """

        def parse_args(self):
            """
            Mock parse args method
            """
            return MockArgs()


    return MockArgumentParser
