# Two separate features for side-by-side inspection; do not parse this combined file.
# Original sample=0 id=59 domain=E-commerce
Feature: Returning from order summary page to one of previous steps
    Scenario: Going back to shipping step with steps panel when order total is zero
        Given I am a logged in customer
        And I added product "Stark Robe" to the cart
        And I added product "Paganini T-Shirt" to the cart
        And I addressed the cart
        When I proceed with "Free" shipping method
        And I go to the shipping step
        Then I should be redirected to the shipping step
        And I should be able to go to the complete step again


# Perturbation M_DROP_THEN
Feature: Returning from order summary page to one of previous steps
    Scenario: Going back to shipping step with steps panel when order total is zero
        Given I am a logged in customer
        And I added product "Stark Robe" to the cart
        And I added product "Paganini T-Shirt" to the cart
        And I addressed the cart
        When I proceed with "Free" shipping method
        And I go to the shipping step
        Then I should be redirected to the shipping step

