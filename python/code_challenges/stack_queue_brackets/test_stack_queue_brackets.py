import pytest 
from stack_queue_brackets.stack_queue_brackets import checker

def test_validate_brackets_one():
  string = "{[]}"
  expected = True
  actual = checker(string)
  assert expected == actual

def test_validate_brackets_two():
  string = "[}"
  expected = False
  actual = checker(string)
  assert expected == actual

def test_validate_brackets_three():
  string = "[({}]"
  expected = False
  actual = checker(string)
  assert expected == actual


# if __name__=="__main__":
#
