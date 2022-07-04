#imita um cliente utilizando o nosso programa

from unittest import result
from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()

def test_add_beer():
    result = runner.invoke(main,
                    ["add","Skol","Pilsen",
                    "--flavor=2","--image=2",
                    "--cost=4"]
                    )
    assert result.exit_code == 0
    assert "beer added" in result.stdout
    