import requests
from behave import given, then, when
from behave.runner import Context

import auth
from config import settings
from helpers import build_post_headers, get_uri_from_endpoint
from schemas.private_api import ErrorResponseSchema, OpenOrdersResponseSchema


@given('the user knows the API endpoint to get the open orders')
def step_impl(context: Context) -> None:
    context.endpoint = f'{settings.base_url}/0/private/OpenOrders'


@when('the user makes an authenticated request')
def step_impl(context: Context) -> None:
    form_data = {
        'nonce': auth.generate_nonce(),
        'otp': settings.auth.otp,
    }
    headers = build_post_headers(uri=get_uri_from_endpoint(context.endpoint), form_data=form_data)

    context.response = requests.post(context.endpoint, data=form_data, headers=headers)


@then('the response conforms to the open orders schema')
def step_impl(context: Context) -> None:
    response_json = context.response.json()
    context.validated_response = OpenOrdersResponseSchema(**response_json)


@when('the user makes an authenticated request with wrong OTP value')
def step_impl(context: Context) -> None:
    form_data = {
        'nonce': auth.generate_nonce(),
        'otp': 1337,
    }
    headers = build_post_headers(uri=get_uri_from_endpoint(context.endpoint), form_data=form_data)

    context.response = requests.post(context.endpoint, data=form_data, headers=headers)


@then('the response contains an error message')
def step_impl(context: Context) -> None:
    response_json = context.response.json()
    context.validated_response = ErrorResponseSchema(**response_json)


@then('the error message says "{message}"')
def step_impl(context: Context, message: str) -> None:
    print(context.validated_response.error)
    assert message in context.validated_response.error
