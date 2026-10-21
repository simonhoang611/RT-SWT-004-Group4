# Two separate features for side-by-side inspection; do not parse this combined file.
# Original sample=5 id=27 domain=E-commerce
Feature: Seeing the product's lowest price before the discount
    Scenario: Seeing the lowest price information on a product that has a discount, and then seeing the discount change
        Given the store has a product "Wyborowa Vodka" priced at "$37.00"
        And this product's price changed to "$21.00" and original price changed to "$37.00"
        And this product's price changed to "$30.00"
        When I check this product's details
        Then I should see "$21.00" as its lowest price before the discount


# Perturbation M_NUM
Feature: Seeing the product's lowest price before the discount
    Scenario: Seeing the lowest price information on a product that has a discount, and then seeing the discount change
        Given the store has a product "Wyborowa Vodka" priced at "$371"
        And this product's price changed to "$211" and original price changed to "$371"
        And this product's price changed to "$301"
        When I check this product's details
        Then I should see "$211" as its lowest price before the discount

