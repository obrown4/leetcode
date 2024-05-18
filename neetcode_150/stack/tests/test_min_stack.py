from ..src.min_stack import MinStack
import pytest

def test1():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2

def test2():
    stack = MinStack()

    stack.push(-1)
    assert stack.getMin() == -1
    stack.push(-2)
    assert stack.getMin() == -2
    stack.push(-3)
    assert stack.getMin() == -3
    stack.push(5)
    stack.pop()
    assert stack.getMin() == -3
    stack.push(-3)
    assert stack.getMin() == -3

def test3():
    stack = MinStack()

    stack.push(0)
    stack.push(1)
    stack.push(0)
    assert stack.getMin() == 0
    stack.pop()
    assert stack.getMin() == 0
