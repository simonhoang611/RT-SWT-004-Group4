# Case 76 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026; confidence of the comparison: high. AC4 has the outcome 73.80/13.80, corresponding to 2×30 remaining. The output removes only 1 unit of the 100 product from the cart 3×100+2×30, so 260 remains before tax; at 23% it should be total 319.80, tax 59.80. The action and the outcome contradict each other. Coverage: 4/5. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Scenario 1 has When I add product "Taxed Product" to the cart, Then my cart total should be "$123.00" and my cart taxes should be "$23.00", correct price $100.00, tax 23% (Background) and both amounts.|AC2(correct): Scenario 2 has When I add 3 units of product "Taxed Product" to the cart, Then total "$369.00" and taxes "$69.00", correct 3 units and both amounts correct (3 x 100 x 1.23 = 369).|AC3(correct): Scenario 3 adds 3 units "Taxed Product" and 2 units "Another Taxed Product" ($30.00), Then total "$442.80" and taxes "$82.80", correct quantities and amounts (360 x 1.23 = 442.80).|AC4(wrong): Scenario 4 uses When I remove one unit of product "Taxed Product" from the cart, but the AC is "remove one taxed product", i.e. removing the whole product line. The amount $73.80 is only correct when 2 x $30 remain (60 x 1.23 = 73.80). Removing one unit leaves the cart with 2 "Taxed Product" and 2 "Another Taxed Product" = $319.80, tax $59.80. Then matches the AC but When makes the test FAIL even on a correct system.|AC5 (correct): Scenario 5 has Given 3 units and 2 units, When I change the quantity of product "Taxed Product" to 1, Then total "$196.80" and taxes "$36.80", correct product changed (100 + 60 = 160, 160 x 1.23 = 196.80).|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026. AC4 has the outcome 73.80/13.80, corresponding to 2×30 remaining. The output removes only 1 unit of the 100 product from the cart 3×100+2×30, so 260 remains before tax; at 23% it should be total 319.80, tax 59.80. The action and the outcome contradict each other. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC4 and AC5 state the initial cart state clearly (“a cart containing 3 units ... and 2 units ...”).|The Background has all of: the US channel, two products priced $100.00 and $30.00, the tax category, tax rate 23% and the assignment of both products to “Standard Tax”. Scenarios 4 and 5 have a Given that builds the cart with 3 units and 2 units.|Scenario 4 uses I remove one unit of product "Taxed Product", whereas the AC describes removing one product from the cart. The result $73.80 only matches when all 3 units of “Taxed Product” are removed, not one unit.|All 5 ACs have two Thens checking total and taxes.|The order set up the store, build the cart, perform the action, then check the total follows the correct process. | ACS WITH PRECONDITION: AC4 and AC5

## User story

```text
0001: As a Customer,
0002: I want to have correct taxes applied to my cart for products in the same tax category,
0003: So that I can see and pay the proper total amount for my order.
0004: 
0005: Acceptance Criteria:
0006: - When I add one taxed product priced at $100.00 with a 23% tax rate, the cart total should be $123.00 and the cart taxes should be $23.00.
0007: - When I add 3 units of the same taxed product priced at $100.00 with a 23% tax rate, the cart total should be $369.00 and the cart taxes should be $69.00.
0008: - When I add 3 units of one taxed product priced at $100.00 and 2 units of another taxed product priced at $30.00, both with a 23% tax rate, the cart total should be $442.80 and the cart taxes should be $82.80.
0009: - When I remove one taxed product from a cart containing 3 units of one taxed product and 2 units of another taxed product, both with a 23% tax rate, the cart total should be $73.80 and the cart taxes should be $13.80.
0010: - When I change the quantity of a taxed product in a cart containing 3 units of one taxed product and 2 units of another taxed product, both with a 23% tax rate, to 1, the cart total should be $196.80 and the cart taxes should be $36.80.
```

## Generated Gherkin C0

```text
0001: @managing_cart
0002: Feature: Having correct taxes applied to products in the same tax category
0003: 
0004:     Background:
0005:         Given the store operates on a single channel in "United States"
0006:         And the store has a product "Taxed Product" priced at "$100.00"
0007:         And the store has a product "Another Taxed Product" priced at "$30.00"
0008:         And the store has a tax category "Standard Tax"
0009:         And the store has a tax rate "23%" for tax category "Standard Tax"
0010:         And the product "Taxed Product" belongs to tax category "Standard Tax"
0011:         And the product "Another Taxed Product" belongs to tax category "Standard Tax"
0012:         And I am logged in as a customer
0013: 
0014:     @ui
0015:     Scenario: Having correct taxes applied when adding one taxed product
0016:         When I add product "Taxed Product" to the cart
0017:         Then my cart total should be "$123.00"
0018:         And my cart taxes should be "$23.00"
0019: 
0020:     @ui
0021:     Scenario: Having correct taxes applied when adding multiple units of the same taxed product
0022:         When I add 3 units of product "Taxed Product" to the cart
0023:         Then my cart total should be "$369.00"
0024:         And my cart taxes should be "$69.00"
0025: 
0026:     @ui
0027:     Scenario: Having correct taxes applied when adding multiple taxed products in the same tax category
0028:         When I add 3 units of product "Taxed Product" to the cart
0029:         And I add 2 units of product "Another Taxed Product" to the cart
0030:         Then my cart total should be "$442.80"
0031:         And my cart taxes should be "$82.80"
0032: 
0033:     @ui
0034:     Scenario: Having correct taxes applied after removing one taxed product from the cart
0035:         Given I add 3 units of product "Taxed Product" to the cart
0036:         And I add 2 units of product "Another Taxed Product" to the cart
0037:         When I remove one unit of product "Taxed Product" from the cart
0038:         Then my cart total should be "$73.80"
0039:         And my cart taxes should be "$13.80"
0040: 
0041:     @ui
0042:     Scenario: Having correct taxes applied after changing the quantity of a taxed product in the cart
0043:         Given I add 3 units of product "Taxed Product" to the cart
0044:         And I add 2 units of product "Another Taxed Product" to the cart
0045:         When I change the quantity of product "Taxed Product" to 1
0046:         Then my cart total should be "$196.80"
0047:         And my cart taxes should be "$36.80"
```

## Archived reference Gherkin

```text
0001: @applying_taxes
0002: Feature: Apply correct taxes for items with the same tax rate
0003:     In order to pay proper amount when buying goods from the same tax category
0004:     As a Customer
0005:     I want to have correct taxes applied to my order
0006: 
0007:     Background:
0008:         Given the store operates on a single channel in "United States"
0009:         And default tax zone is "US"
0010:         And the store has "VAT" tax rate of 23% for "Clothes" within the "US" zone
0011:         And the store has a product "PHP T-Shirt" priced at "$100.00"
0012:         And it belongs to "Clothes" tax category
0013:         And the store has a product "Symfony Hat" priced at "$30.00"
0014:         And it belongs to "Clothes" tax category
0015:         And I am a logged in customer
0016: 
0017:     @api @ui
0018:     Scenario: Proper taxes for taxed product
0019:         Given I added product "PHP T-Shirt" to the cart
0020:         When I check the details of my cart
0021:         Then my cart total should be "$123.00"
0022:         And my cart taxes should be "$23.00"
0023: 
0024:     @api @ui
0025:     Scenario: Proper taxes for multiple same products with the same tax rate
0026:         Given I added 3 products "PHP T-Shirt" to the cart
0027:         When I check the details of my cart
0028:         Then my cart total should be "$369.00"
0029:         And my cart taxes should be "$69.00"
0030: 
0031:     @api @ui
0032:     Scenario: Proper taxes for multiple different products with the same tax rate
0033:         Given I added 3 products "PHP T-Shirt" to the cart
0034:         And I added 2 products "Symfony Hat" to the cart
0035:         When I check the details of my cart
0036:         Then my cart total should be "$442.80"
0037:         And my cart taxes should be "$82.80"
0038: 
0039:     @api @ui
0040:     Scenario: Proper taxes after removing one of the item
0041:         Given I added 3 products "PHP T-Shirt" to the cart
0042:         And I added 2 products "Symfony Hat" to the cart
0043:         And I removed product "PHP T-Shirt" from the cart
0044:         When I check the details of my cart
0045:         Then my cart total should be "$73.80"
0046:         And my cart taxes should be "$13.80"
0047: 
0048:     @api @ui
0049:     Scenario: Proper taxes after changing item quantity
0050:         Given I added 3 products "PHP T-Shirt" to the cart
0051:         And I added 2 products "Symfony Hat" to the cart
0052:         And I changed product "PHP T-Shirt" quantity to 1 in my cart
0053:         When I check the details of my cart
0054:         Then my cart total should be "$196.80"
0055:         And my cart taxes should be "$36.80"
```
