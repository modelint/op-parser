""" test_parse.py -- Test successful parsing of *.op files """

import pytest
from pathlib import Path
from op2_parser.op_parser import OpParser

operations = [
    "arrived-at-floor",
]

@pytest.mark.parametrize("op", operations)
def test_scenarios_pdf(op):

    result = OpParser.parse_file(file_input=Path(f"operations/{op}.op"), debug=False)
    assert result
