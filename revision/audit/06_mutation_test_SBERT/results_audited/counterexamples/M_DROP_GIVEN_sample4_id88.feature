# Two separate features for side-by-side inspection; do not parse this combined file.
# Original sample=4 id=88 domain=E-commerce
Feature: Displaying themed channel website
    Scenario: Displaying default shop homepage
        Given channel "United States" does not use any theme
        When I visit this channel's homepage
        Then I should not see a homepage from "maverick/meerkat" theme


# Perturbation M_DROP_GIVEN
Feature: Displaying themed channel website
    Scenario: Displaying default shop homepage
        When I visit this channel's homepage
        Then I should not see a homepage from "maverick/meerkat" theme

