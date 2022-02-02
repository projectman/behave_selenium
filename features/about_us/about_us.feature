Feature: Validate About Us page

    Chose browser, open Home page, navigate to About Us page
    Find Our Values with expected quantity and 
    validate all our Values names

    Scenario: Open About Us page
        # TODO: update scenario to examles browsers... 
        Given user choses browser "chrome"
        And user open Home Page
        When find link contains text "About Us" and click it
        # Then on opened page Title will be as expected
        # Then on opened page quantity of located Our Values elements eqal 3
        # And all expected values "Accountable, Realiable, Ethical" present in  
