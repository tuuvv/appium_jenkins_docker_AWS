Feature: Enter some value


  Scenario Outline: Enter some value
    Given User is on 'main' page
    When User clicks on 'Enter some value' button at Main page
    Then send '<value>' to input field

    Examples:
      | value      |
      | Skill2Lead |


