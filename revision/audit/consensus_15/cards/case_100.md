# Case 100 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. default/name-desc/code-asc/code-desc and first/last are all present. Name and code have the same order, so the fixture does not strongly distinguish the name/code sort algorithms; recorded as a design limitation, not counted as an AC defect on its own. Coverage: 9/9. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Background creates three products with "tracked inventory" and Scenario 1 has When I browse tracked product variants on the inventory list, correct "displayed on the inventory list".|AC2(correct): Scenario 1 only has browse, without any sort step, followed by Then I should see tracked product variants sorted by name in ascending order, correct "by default".|AC3(correct): Scenario 2 has When I sort tracked product variants by name in descending order and Then sorted by name in descending order, correct name and correct descending direction.|AC4(correct): Scenario 3 has When I sort ... by code in ascending order and Then sorted by code in ascending order, correct code and correct ascending direction.|AC5(correct): Scenario 4 has When I sort ... by code in descending order and Then sorted by code in descending order, correct code and correct descending direction.|AC6(correct): Scenario 1 has first "Alpha T-Shirt" and last "Gamma T-Shirt", correct alphabetical order Alpha < Beta < Gamma.|AC7(correct): Scenario 2 has first "Gamma T-Shirt" and last "Alpha T-Shirt", correctly reversed relative to AC6.|AC8(correct): Scenario 3 has first "Alpha T-Shirt" (code ALPHA) and last "Gamma T-Shirt" (code GAMMA). Then refers to the product name, not the code, but ALPHA, BETA, GAMMA are in the same order as the names, so the values are still correct with respect to the AC.|AC9(correct): Scenario 4 has first "Gamma T-Shirt" (code GAMMA) and last "Alpha T-Shirt" (code ALPHA), correct reversed order of AC8.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026. default/name-desc/code-asc/code-desc and first/last are all present. Name and code have the same order, so the fixture does not strongly distinguish the name/code sort algorithms; recorded as a design limitation, not counted as an AC defect on its own. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
No AC states an initial state. AC1 only says the variants are displayed, AC2 states the default state of the list, the remaining ACs are sort actions and results.|The Whens match the actions in the ACs (browse the list, sort by name or code, ascending or descending direction).|All 9 results are verified by a Then. Each scenario has a Then on the sort direction and two Thens on the first and last elements.|The order open the product, switch the locale, open the taxon selector, then check the list follows the correct business process.

## User story

```text
0001: As an Administrator,
0002: I want to sort tracked product variants on the inventory list by name or code in ascending or descending order,
0003: So that I can quickly find and review inventory items in the order I need.
0004: 
0005: Acceptance Criteria:
0006: - Tracked product variants are displayed on the inventory list.
0007: - By default, tracked product variants are sorted by name in ascending order.
0008: - I can sort tracked product variants by name in descending order.
0009: - I can sort tracked product variants by code in ascending order.
0010: - I can sort tracked product variants by code in descending order.
0011: - When sorting by name ascending, the first item is the alphabetically earliest product name and the last item is the latest.
0012: - When sorting by name descending, the first item is the alphabetically latest product name and the last item is the earliest.
0013: - When sorting by code ascending, the first item is the alphabetically earliest product code and the last item is the latest.
0014: - When sorting by code descending, the first item is the alphabetically latest product code and the last item is the earliest.
```

## Generated Gherkin C0

```text
0001: @managing_inventory
0002: Feature: Sorting tracked product variants on the inventory list
0003: 
0004:     Background:
0005:         Given the store operates on a single channel in "United States"
0006:         And the store has a product "Alpha T-Shirt" with code "ALPHA" and tracked inventory
0007:         And the store has a product "Beta T-Shirt" with code "BETA" and tracked inventory
0008:         And the store has a product "Gamma T-Shirt" with code "GAMMA" and tracked inventory
0009:         And I am logged in as an administrator
0010: 
0011:     @ui
0012:     Scenario: Seeing tracked product variants sorted by name in ascending order by default
0013:         When I browse tracked product variants on the inventory list
0014:         Then I should see tracked product variants sorted by name in ascending order
0015:         And the first tracked product variant should be "Alpha T-Shirt"
0016:         And the last tracked product variant should be "Gamma T-Shirt"
0017: 
0018:     @ui
0019:     Scenario: Sorting tracked product variants by name in descending order
0020:         When I sort tracked product variants by name in descending order
0021:         Then I should see tracked product variants sorted by name in descending order
0022:         And the first tracked product variant should be "Gamma T-Shirt"
0023:         And the last tracked product variant should be "Alpha T-Shirt"
0024: 
0025:     @ui
0026:     Scenario: Sorting tracked product variants by code in ascending order
0027:         When I sort tracked product variants by code in ascending order
0028:         Then I should see tracked product variants sorted by code in ascending order
0029:         And the first tracked product variant should be "Alpha T-Shirt"
0030:         And the last tracked product variant should be "Gamma T-Shirt"
0031: 
0032:     @ui
0033:     Scenario: Sorting tracked product variants by code in descending order
0034:         When I sort tracked product variants by code in descending order
0035:         Then I should see tracked product variants sorted by code in descending order
0036:         And the first tracked product variant should be "Gamma T-Shirt"
0037:         And the last tracked product variant should be "Alpha T-Shirt"
```

## Archived reference Gherkin

```text
0001: @managing_inventory
0002: Feature: Sorting inventory
0003:     In order to change the order by which tracked product variants are displayed
0004:     As an Administrator
0005:     I want to be able to sort tracked product variants on the list
0006: 
0007:     Background:
0008:         Given the store operates on a single channel in "United States"
0009:         And the store has a product "Iron Maiden T-Shirt"
0010:         And "Iron Maiden T-Shirt" product is tracked by the inventory
0011:         And there are 5 units of product "Iron Maiden T-Shirt" available in the inventory
0012:         And the store has a product "RHCP T-Shirt"
0013:         And "RHCP T-Shirt" product is tracked by the inventory
0014:         And there are 25 units of product "RHCP T-Shirt" available in the inventory
0015:         And I am logged in as an administrator
0016:         And I am browsing inventory
0017: 
0018:     @ui @no-api
0019:     Scenario: Displaying tracked product variants sorted by name in ascending order by default
0020:         Then I should see 2 tracked variants in the list
0021:         And the first variant on the list should have name "Iron Maiden T-Shirt"
0022:         And the last variant on the list should have name "RHCP T-Shirt"
0023: 
0024:     @ui @no-api
0025:     Scenario: Sorting tracked product variants descending by name
0026:         When I sort the tracked variants descending by name
0027:         Then I should see 2 tracked variants in the list
0028:         And the first variant on the list should have name "RHCP T-Shirt"
0029:         And the last variant on the list should have name "Iron Maiden T-Shirt"
0030: 
0031:     @ui @no-api
0032:     Scenario: Sorting tracked product variants ascending by code
0033:         When I sort the tracked variants ascending by code
0034:         Then I should see 2 tracked variants in the list
0035:         And the first variant on the list should have code "IRON_MAIDEN_T_SHIRT"
0036:         And the last variant on the list should have code "RHCP_T_SHIRT"
0037: 
0038:     @ui @no-api
0039:     Scenario: Sorting tracked product variants descending by code
0040:         When I sort the tracked variants descending by code
0041:         Then I should see 2 tracked variants in the list
0042:         And the first variant on the list should have code "RHCP_T_SHIRT"
0043:         And the last variant on the list should have code "IRON_MAIDEN_T_SHIRT"
```
