Feature: test public API

  Scenario: retrieve server time and validate the response
    Given the user knows the API endpoint to get the server time
     When the user makes the request
     Then the response conforms to the schema
      And the reported Unix time is similar to the local machine's Unix time
