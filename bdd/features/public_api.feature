Feature: test public API

  Scenario: retrieve server time and validate the response
    Given the user knows the API endpoint to get the server time
     When the user makes the request
     Then the response conforms to the server time schema
      And the reported Unix time is similar to the local machine's Unix time

  Scenario: retrieve XBT/USD trading pair and validate the response
    Given the user knows the API endpoint to get the trading pair
     When the user makes the request
     Then the response conforms to the trading pair schema
      And the response contains the correct values
        | field   | value   |
        | altname | XBTUSD  |
        | wsname  | XBT/USD |
        | base    | XXBT    |
        | quote   | ZUSD    |
