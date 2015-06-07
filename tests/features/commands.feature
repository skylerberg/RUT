Feature: Commands

  Scenario Outline: User enters a command
    Given I open a new file
     When I enter <command>
     Then <result>

    Examples: Commands
      | command   | name    | result                    |
      | :q        | quits   | the program ends          |
      | :s        | save    | the file is saved         |
      | :s PATH   | save as | the file is saved as PATH |
