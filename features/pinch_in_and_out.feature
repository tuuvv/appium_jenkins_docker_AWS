Feature: Pinch in and Pinch out


  Scenario Outline: Pinch
    Given User is on 'main' page
    When Scroll to '<label>' button and click
    Then User pinch out
    And User pinch in

    Examples:
      | label        |
      | PINCH IN OUT |
