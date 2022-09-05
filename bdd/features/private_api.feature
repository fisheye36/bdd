Feature: test private API that requires authentication

  @auth
  Scenario: retrieve open orders on the account and validate the response
    Given the user knows the API endpoint to get the open orders
     When the user makes an authenticated request
     Then the response conforms to the open orders schema

  @auth
  Scenario: invalid OTP value results in an error
    Given the user knows the API endpoint to get the open orders
     When the user makes an authenticated request with wrong OTP value
     Then the response contains an error message
      And the error message says "EAPI:Invalid signature"
