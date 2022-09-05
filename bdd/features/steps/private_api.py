import requests
from behave import given, then, when
from behave.runner import Context

import auth
from config import settings
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

    headers = {
        'API-Key': settings.auth.api_key,
        'API-Sign': auth.generate_api_key_signature(
            uri=context.endpoint.removeprefix(settings.base_url),
            data=form_data,
            secret=settings.auth.api_secret,
        ),
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }

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

    headers = {
        'API-Key': settings.auth.api_key,
        'API-Sign': auth.generate_api_key_signature(
            uri=context.endpoint.removeprefix(settings.base_url),
            data=form_data,
            secret=settings.auth.api_secret,
        ),
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }

    context.response = requests.post(context.endpoint, data=form_data, headers=headers)


@then('the response contains an error message')
def step_impl(context: Context) -> None:
    response_json = context.response.json()
    context.validated_response = ErrorResponseSchema(**response_json)


@then('the error message says "{message}"')
def step_impl(context: Context, message: str) -> None:
    print(context.validated_response.error)
    assert message in context.validated_response.error
