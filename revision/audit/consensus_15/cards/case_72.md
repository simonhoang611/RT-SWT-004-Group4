# Case 72 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: high. Single-channel, Category and the main image are set up; when the taxon is opened, the name and image are checked. Coverage: 5/5. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Background has Given the store operates on a single channel in "United States", correct "single channel" and correct country United States.|AC2(correct): Background has And the store classifies products under a taxon named "Category", correct taxon name "Category".|AC3(correct): Background has And the taxon "Category" has an image with type "main", correct taxon "Category" and correct image type "main".|AC4(correct): Scenario has When I view the details of the "Category" taxon followed by Then I should see the taxon name "Category", correct detail page of taxon "Category" and correct result of seeing the taxon name.|AC5(correct): Scenario has And I should see the taxon main image, correct result of seeing the taxon's main image. Gherkin uses "the taxon main image" instead of "its main image", same meaning, does not change the test result.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026. Single-channel, Category and the main image are set up; when the taxon is opened, the name and image are checked. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1, AC2 and AC3 are all initial states (single-channel store in the US, taxon “Category”, the taxon's “main” image).|All three preconditions are in the Background, so they apply to the only scenario.|I view the details of the "Category" taxon matches the action in AC4 and AC5.|Both expected results (taxon name, main image) are verified by a Then.|Both Thens check the content displayed on the detail page that the When has just opened, and the main image is a consequence of the Given in the Background.|The order set up the store, create the taxon, assign the image, and only then view the details follows the correct business process. | ACS WITH PRECONDITION: AC1, AC2 and AC3

## User story

```text
0001: As a Visitor,
0002: I want to view an image on a taxon details page,
0003: So that I can visually identify the taxon and browse products more easily.
0004: 
0005: Acceptance Criteria:
0006: - The store operates on a single channel in the United States.
0007: - The store classifies products under a taxon named "Category".
0008: - The "Category" taxon can have an image assigned with type "main".
0009: - When I view the details of the "Category" taxon, I should see the taxon name.
0010: - When I view the details of the "Category" taxon, I should see its main image.
```

## Generated Gherkin C0

```text
0001: @viewing_taxons
0002: Feature: Viewing a taxon image on the taxon details page
0003: 
0004:     Background:
0005:         Given the store operates on a single channel in "United States"
0006:         And the store classifies products under a taxon named "Category"
0007:         And the taxon "Category" has an image with type "main"
0008: 
0009:     @ui
0010:     Scenario: Viewing the details of a taxon with its main image
0011:         When I view the details of the "Category" taxon
0012:         Then I should see the taxon name "Category"
0013:         And I should see the taxon main image
```

## Archived reference Gherkin

```text
0001: @viewing_products
0002: Feature: Viewing a taxon's image on a taxon details page
0003:     In order to see images of a taxon
0004:     As a Visitor
0005:     I want to be able to view an image of a taxon
0006: 
0007:     Background:
0008:         Given the store operates on a single channel in "United States"
0009:         And the store classifies its products as "Category"
0010:         And the "Category" taxon has an image "lamborghini.jpg" with "main" type
0011: 
0012:     @api @no-ui
0013:     Scenario: Viewing a taxon's image
0014:         When I check the "Category" taxon's details
0015:         Then I should see the taxon name "Category"
0016:         And I should see a main image
```
