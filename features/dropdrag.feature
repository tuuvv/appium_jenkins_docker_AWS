Feature: Drop and Drag


  Scenario Outline: DropDrag
    Given User is on 'main' page
    When Scroll to '<label>' button and click
    Then Drop and drag picture to midle part
    And Drop and drag text to last part
    And Drop and drag button to last part

    Examples:
      | label       |
      | DRAGANDDROP |
