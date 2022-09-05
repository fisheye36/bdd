import datetime

import requests
from behave import given, then, when
from behave.runner import Context

from config import settings
from schemas.public_api import ServerTimeResponseSchema, TradingPairResponseSchema


@given('the user knows the API endpoint to get the server time')
def step_impl(context: Context) -> None:
    context.endpoint = f'{settings.base_url}/0/public/Time'


@when('the user makes the request')
def step_impl(context: Context) -> None:
    context.response = requests.get(context.endpoint)


@then('the response conforms to the server time schema')
def step_impl(context: Context) -> None:
    response_json = context.response.json()
    context.validated_response = ServerTimeResponseSchema(**response_json)


@then("the reported Unix time is similar to the local machine's Unix time")
def step_impl(context: Context) -> None:
    server_timestamp = context.validated_response.result.unixtime
    local_timestamp = datetime.datetime.utcnow().timestamp()
    assert abs(server_timestamp - local_timestamp) < 5


@given('the user knows the API endpoint to get the trading pair')
def step_impl(context: Context) -> None:
    context.endpoint = f'{settings.base_url}/0/public/AssetPairs?pair=XBTUSD'


@then('the response conforms to the trading pair schema')
def step_impl(context: Context) -> None:
    response_json = context.response.json()
    context.validated_response = TradingPairResponseSchema(**response_json)


@then('the response contains the correct values')
def step_impl(context: Context) -> None:
    asset_pair = context.validated_response.result.XXBTZUSD
    for row in context.table:
        field = row['field']
        expected_value = row['value']
        actual_value = getattr(asset_pair, field)
        assert actual_value == expected_value
