import datetime

import requests
from behave import given, then, when
from behave.runner import Context

from config import settings
from schemas.public_api import ServerTimeResponseSchema


@given('the user knows the API endpoint to get the server time')
def step_impl(context: Context) -> None:
    context.endpoint = f'{settings.base_url}/0/public/Time'


@when('the user makes the request')
def step_impl(context: Context) -> None:
    context.response = requests.get(context.endpoint)


@then('the response conforms to the schema')
def step_impl(context: Context) -> None:
    response_json = context.response.json()
    context.validated_response = ServerTimeResponseSchema(**response_json)


@then("the reported Unix time is similar to the local machine's Unix time")
def step_impl(context: Context) -> None:
    server_timestamp = context.validated_response.result.unixtime
    local_timestamp = datetime.datetime.utcnow().timestamp()
    assert abs(server_timestamp - local_timestamp) < 5
