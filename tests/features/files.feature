Feature: Files

  Scenario Outline: Open a file
    Given I have a file called <name>
     When I open it
     Then its contents will be available

    Examples: Files
      | name    |
      | fox.txt |

  Scenario Outline: Save as
    Given I have a pane with "<text>"
     When I save it to a new file
     Then the file will contain "<text>"

    Examples: Text
      | text                 |
      | This is a test sting |

  Scenario: Save file
    Given I open a new file
     When I modify the file
      And I save the file
     Then the modifications are saved
