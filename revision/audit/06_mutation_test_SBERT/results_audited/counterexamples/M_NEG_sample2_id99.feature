# Two separate features for side-by-side inspection; do not parse this combined file.
# Original sample=2 id=99 domain=E-commerce
Feature: Applying catalog promotions only in proper channels
    Scenario: Applying catalog promotion
        When I change my current channel to "Web-US"
        And I view product "T-Shirt"
        Then I should see the product price "$14.00"
        And I should see the product original price "$20.00"


# Perturbation M_NEG
Feature: Applying catalog promotions only in proper channels
    Scenario: Applying catalog promotion
        When I change my current channel to "Web-US"
        And I view product "T-Shirt"
        Then I should not see the product price "$14.00"
        And I should see the product original price "$20.00"

