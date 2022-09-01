Feature: hello world

  Scenario: run a hello world scenario to test environment setup
    Given we have behave installed
    And we are in a Docker container
    When we run behave
    Then this scenario should pass
