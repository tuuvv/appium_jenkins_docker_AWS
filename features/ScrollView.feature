Feature: Scroll View


  Scenario Outline: Scrollview
    Given User is on 'main' page
    When User clicks on 'ScrollView' button at Main page
    Then Srollview and select '<label>'
    And click yes btn

    Examples:
      | label    |
      | BUTTON12 |


