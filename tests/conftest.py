from pytest import fixture
from tasks.i9_list_functions.list_functions import *


@fixture
def list_functions():
    return MyList()
