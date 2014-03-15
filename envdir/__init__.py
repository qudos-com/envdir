from .__main__ import runner, go
from .env import Env  # noqa
from .version import __version__  # noqa

open = runner.open


# for backward compatibility
def read(path=None, no_clobber=None):
    return open(path, stacklevel=2, no_clobber=no_clobber)


def run(*args):
    go(runner.run, *args)


def shell(*args):
    go(runner.shell, *args)
