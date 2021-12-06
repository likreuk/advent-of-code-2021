import pathlib
import pytest
import day3_2021 as d3

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = PUZZLE_DIR / 'example1.txt'
    return d3.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def test_part1_example1(example1):
    assert d3.part1(example1) == 198

def test_part2_example1(example1):
    assert d3.part2(example1) == 230
