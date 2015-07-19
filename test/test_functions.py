import pytest
from src.functions import multiply, add

def test_multiply():
	assert multiply(1,2) == 2
	assert multiply(0,1) == 0

def test_add():
	assert add(1,1) == 2

def test_python3():
	with pytest.raises(SyntaxError):
		print("a")