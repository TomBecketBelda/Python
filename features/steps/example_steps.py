from behave import given, when, then, step
from features.pages.page1 import page1

@given('we have behave installed')
def step_impl(context):
    print("hello world")
    pass


@when('we implement {number:d} tests')
def step_impl(context,number):  # --
    page1.test(number)

