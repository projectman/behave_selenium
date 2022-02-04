Feature: Validate About Us page

    Scenario: Find Out Values elements to validate quantity and content
        with preselected in command line browser name

        Given user open "Home Page"
        When find link contains text "About Us" and click it
        # TODO: find page title by page_name in first scenario
        Then on opened page "About Us title" should be as expected
        And on opened page quantity of located Our Values elements equal 3
        And all expected values "Accountable, Reliable, Ethical" present in
