Feature: Validate About Us page

    Scenario Outline: Find Out Values elements to validate quantity and content
        Given user chooses browser "<browser>"
        # TODO: add 'user open "{page_name}"' to make it flexible
        And user open "Home Page"
        When find link contains text "About Us" and click it
        # TODO: find page title by page_name in first scenario
        Then on opened page Title will be as expected
        And on opened page quantity of located Our Values elements equal 3
        And all expected values "Accountable, Reliable, Ethical" present in

        Examples:
            | browser |
            | chrome  |
#            | firefox |
#            | mobile  |