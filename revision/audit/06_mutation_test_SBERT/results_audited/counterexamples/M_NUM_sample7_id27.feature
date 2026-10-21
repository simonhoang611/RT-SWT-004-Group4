# Two separate features for side-by-side inspection; do not parse this combined file.
# Original sample=7 id=27 domain=E-commerce
Feature: Seeing the product's lowest price before the discount
    Scenario: Seeing the lowest price information on a product with catalog promotion
        Given the store has a product "Wyborowa Vodka" priced at "$37.00"
        And there is a catalog promotion "Winter Sale" with priority 100 that reduces price by "$10.00" and applies on "Wyborowa Vodka" product
        When I check this product's details
        Then I should see "$37.00" as its lowest price before the discount


# Perturbation M_NUM
Feature: Seeing the product's lowest price before the discount
    Scenario: Seeing the lowest price information on a product with catalog promotion
        Given the store has a product "Wyborowa Vodka" priced at "$371"
        And there is a catalog promotion "Winter Sale" with priority 1001 that reduces price by "$101" and applies on "Wyborowa Vodka" product
        When I check this product's details
        Then I should see "$371" as its lowest price before the discount

