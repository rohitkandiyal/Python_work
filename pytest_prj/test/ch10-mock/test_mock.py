import shlex

import pytest
from typer.testing import CliRunner
from cards.cli import app
import cards

from unittest import mock

runner = CliRunner()


# We have cli which calls api to do things.
# Now we will mock api so that we can test cli independently.

# this is jst a helper function to make calls to cli
def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_cards_cli_version_without_mock():
    result = cards_cli("version")
    print()
    print(f"version: {result}")
    assert result == "1.0.0"
    # assert result == "1.0.1"          #this fails

    result = cards_cli("list -o brian")
    print(f"list:\n{result}")


@mock.patch.object(cards, "__version__", "1.2.3")  # actual is 1.0.0
def test_cards_cli_version_with_mock():
    result = cards_cli("version")
    assert result == "1.2.3"


########################################################################################################################
#
# now we will mock a class and then the method inside it
# mocking path method in CardsDB class in api.py
@mock.patch.object(cards, "CardsDB")
def test_mock_cards_db_path(MockCardsDB):
    MockCardsDB.return_value.path.return_value = "/foo/"

    result = runner.invoke(app, ["config"])
    assert result.stdout.rstrip() == "/foo/"


# In above we mocked CardsDB class and it will be mocked many times so here we can use fixture
@pytest.fixture()
def mock_cardsdb_as_fixture():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        yield CardsDB.return_value


# Refactoring test_mock_cards_db_path()
def test_mock_cards_db_path_one(mock_cardsdb_as_fixture):
    mock_cardsdb_as_fixture.path.return_value = "/foo/"

    result = runner.invoke(app, ["config"])
    assert result.stdout.rstrip() == "/foo/"


########################################################################################################################
# NOTE
# USE OF AUTOSPEC
#
# Mock objects are typically intended to be objects that are used in place of the real implementation.
# if the real object allows .start(index), we want our mock objects to allow .start(index) as well. There’s a problem,
# however. Mock objects are too flexible by default. They will also accept star() happily, any misspelled methods, any
# additional parameters, really anything.
#
#
########################################################################################################################
# NOTE
# USE OF variations of assert_called methods
# When we do not have a return value which we can assert then we jst check if the correct method is called called
# correctly. Hence we use assert_called methods.

def test_add_with_owner(mock_cardsdb_as_fixture):
    cards_cli("add some task -o brian")
    expected = cards.Card("some task", owner="brian", state="todo")

    mock_cardsdb_as_fixture.add_card.assert_called_with(expected)


########################################################################################################################
# NOTE
# side_effect is mocking exceptions of the actual method or class.
#