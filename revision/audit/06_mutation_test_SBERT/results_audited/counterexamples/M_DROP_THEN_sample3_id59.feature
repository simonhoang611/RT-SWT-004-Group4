# Two separate features for side-by-side inspection; do not parse this combined file.
# Original sample=3 id=59 domain=E-commerce
Feature: Returning from order summary page to one of previous steps
    Scenario: Going back to payment step
        Given I am a logged in customer
        And I have product "Stark Robe" in the cart
        And I addressed the cart
        And I proceed with "Free" shipping method and "Cash on Delivery" payment
        When I decide to change the payment method
        Then I should be redirected to the payment step
        And I should be able to go to the summary page again


# Perturbation M_DROP_THEN
Feature: Returning from order summary page to one of previous steps
    Scenario: Going back to payment step
        Given I am a logged in customer
        And I have product "Stark Robe" in the cart
        And I addressed the cart
        And I proceed with "Free" shipping method and "Cash on Delivery" payment
        When I decide to change the payment method
        Then I should be redirected to the payment step

