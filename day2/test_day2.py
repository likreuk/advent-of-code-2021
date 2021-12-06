import pathlib
import pytest
import day2_2021 as d2

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = PUZZLE_DIR / 'example1.txt'
    return d2.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

def test_part1_example1(example1):
    assert d2.part1(example1) == 150

def test_part2_example1(example1):
    assert d2.part2(example1) == 900