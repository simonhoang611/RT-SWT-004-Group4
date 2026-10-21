# Two separate features for side-by-side inspection; do not parse this combined file.
# Original sample=1 id=69 domain=E-commerce
Feature: Redirecting on login page
    Scenario: Redirecting on login page after being logout
        When I try to open administration dashboard
        Then I should be on login page


# Perturbation M_THEN_FIRST
Feature: Redirecting on login page
    Scenario: Redirecting on login page after being logout
        Then I should be on login page
        When I try to open administration dashboard

