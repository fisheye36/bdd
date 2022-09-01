from behave import given, then, when
from behave.runner import Context


@given('we have behave installed')
def we_have_behave_installed(context: Context) -> None:
    pass


@given('we are in a Docker container')
def step_impl(context: Context) -> None:
    pass


@when('we run behave')
def step_impl(context: Context) -> None:
    assert True is not False


@then('this scenario should pass')
def step_impl(context: Context) -> None:
    assert context.failed is False
