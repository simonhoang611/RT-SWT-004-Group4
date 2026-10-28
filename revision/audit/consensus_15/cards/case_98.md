# Case 98 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=Y; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. AC2-7 have complete concrete examples. AC1 requires the taxon set to be filtered by locale; with a fixture containing PL/FR/DE/UA, negating only UA does not verify that FR/DE do not appear in PL (likewise for the other locales). The reviewer should confirm the required level of checking exclusivity. Coverage: 6/7. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): All three scenarios have When I choose the main taxon and then check the set of selectable taxons according to the currently selected locale.|AC2(correct): Scenario 1 has I am in the "Polish" panel locale, Then I should be able to select taxon "Men-T-Shirts_PL" and I should be able to select taxon "Woman-T-Shirts_PL", correct locale and both taxons correct.|AC3(correct): Scenario 1 has Then I should not be able to select taxon "Woman-T-Shirts_UA", correct taxon of another locale and correctly keeps the negation "cannot".|AC4(correct): Scenario 2 has I am in the "French" panel locale, Then be able to select "Men-T-Shirts_FR" and "Woman-T-Shirts_FR", correct locale and both taxons correct.|AC5(correct): Scenario 2 has Then I should not be able to select taxon "Woman-T-Shirts_UA", correct taxon of another locale and correct negation.|AC6(correct): Scenario 3 has I am in the "German" panel locale, Then be able to select "Men-T-Shirts_DE" and "Woman-T-Shirts_DE", correct locale and both taxons correct. | AC7 (correct): Scenario 3 has Then I should not be able to select taxon "Woman-T-Shirts_UA", correct taxon of another locale and correct negation.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026. AC2-7 have complete concrete examples. AC1 requires the taxon set to be filtered by locale; with a fixture containing PL/FR/DE/UA, negating only UA does not verify that FR/DE do not appear in PL (likewise for the other locales). The reviewer should confirm the required level of checking exclusivity. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1 is general about the filtering and states no specific initial state. The product “PHP T-Shirt” was never created.|The Background only creates the channel, the taxons and the admin, but each scenario has Given I am editing product "PHP T-Shirt", so there is no product whose edit page could be opened.|All 6 expected results (two taxons selectable, the UA taxon not selectable, for three locales) are verified by a Then.|The Thens all check the list of taxons shown when the When opens the main taxon selector. | ACS WITH PRECONDITION: AC2 to AC7

## User story

```text
0001: As an Administrator,
0002: I want to select a product’s main taxon only from taxons available in the current panel locale,
0003: So that product categorization stays consistent with the locale I am managing.
0004: 
0005: Acceptance Criteria:
0006: - When I choose the main taxon for a product, the available taxons are filtered by the currently selected panel locale.
0007: - In the Polish locale, I can select Polish taxons such as `Men-T-Shirts_PL` and `Woman-T-Shirts_PL`.
0008: - In the Polish locale, I cannot select taxons from other locales such as `Woman-T-Shirts_UA`.
0009: - In the French locale, I can select French taxons such as `Men-T-Shirts_FR` and `Woman-T-Shirts_FR`.
0010: - In the French locale, I cannot select taxons from other locales such as `Woman-T-Shirts_UA`.
0011: - In the German locale, I can select German taxons such as `Men-T-Shirts_DE` and `Woman-T-Shirts_DE`.
0012: - In the German locale, I cannot select taxons from other locales such as `Woman-T-Shirts_UA`.
```

## Generated Gherkin C0

```text
0001: @managing_products
0002: Feature: Selecting a product main taxon only from taxons available in the current panel locale
0003: 
0004:     Background:
0005:         Given the store operates on a single channel in "United States"
0006:         And the store has taxons "Men-T-Shirts_PL", "Woman-T-Shirts_PL", "Men-T-Shirts_FR", "Woman-T-Shirts_FR", "Men-T-Shirts_DE", "Woman-T-Shirts_DE", "Woman-T-Shirts_UA"
0007:         And I am logged in as an administrator
0008: 
0009:     @ui
0010:     Scenario: Selecting a main taxon in the Polish locale
0011:         Given I am editing product "PHP T-Shirt"
0012:         And I am in the "Polish" panel locale
0013:         When I choose the main taxon
0014:         Then I should be able to select taxon "Men-T-Shirts_PL"
0015:         And I should be able to select taxon "Woman-T-Shirts_PL"
0016:         And I should not be able to select taxon "Woman-T-Shirts_UA"
0017: 
0018:     @ui
0019:     Scenario: Selecting a main taxon in the French locale
0020:         Given I am editing product "PHP T-Shirt"
0021:         And I am in the "French" panel locale
0022:         When I choose the main taxon
0023:         Then I should be able to select taxon "Men-T-Shirts_FR"
0024:         And I should be able to select taxon "Woman-T-Shirts_FR"
0025:         And I should not be able to select taxon "Woman-T-Shirts_UA"
0026: 
0027:     @ui
0028:     Scenario: Selecting a main taxon in the German locale
0029:         Given I am editing product "PHP T-Shirt"
0030:         And I am in the "German" panel locale
0031:         When I choose the main taxon
0032:         Then I should be able to select taxon "Men-T-Shirts_DE"
0033:         And I should be able to select taxon "Woman-T-Shirts_DE"
0034:         And I should not be able to select taxon "Woman-T-Shirts_UA"
```

## Archived reference Gherkin

```text
0001: @managing_products
0002: Feature: Selecting main taxon for product in different locales
0003:     In order to be consistent with the store's chosen locale
0004:     As an Administrator
0005:     I want to be able to choose only taxons from the current locale
0006: 
0007:     Background:
0008:         Given the store operates on a channel named "Web"
0009:         And the store has many locales
0010:         And the store has "Category" taxonomy
0011:         And the "Category" taxon has child taxon "T-Shirts" in many locales
0012:         And the "T-Shirts" taxon has child taxon "Men-T-Shirts" in many locales
0013:         And the "T-Shirts" taxon has child taxon "Woman-T-Shirts" in many locales
0014:         And the "Category" taxon has child taxon "Jeans" in many locales
0015:         And the "Jeans" taxon has child taxon "Men-Jeans" in many locales
0016:         And the "Jeans" taxon has child taxon "Woman-Jeans" in many locales
0017:         And the store has a product "T-Shirt Batman"
0018:         And I am logged in as an administrator
0019: 
0020:     @ui @mink:chromedriver @no-api
0021:     Scenario: Choosing only taxons from the Polish locale
0022:         Given I am using "Polish (Poland)" locale for my panel
0023:         When I want to choose main taxon for product "T-Shirt Batman"
0024:         Then I should be able to choose taxon "Men-T-Shirts_PL" from the list
0025:         And I should be able to choose taxon "Woman-T-Shirts_PL" from the list
0026:         And I should not be able to choose taxon "Woman-T-Shirts_UA" from the list
0027: 
0028:     @ui @mink:chromedriver @no-api
0029:     Scenario: Choosing only taxons from the French locale
0030:         Given I am using "French (France)" locale for my panel
0031:         When I want to choose main taxon for product "T-Shirt Batman"
0032:         Then I should be able to choose taxon "Men-T-Shirts_FR" from the list
0033:         And I should be able to choose taxon "Woman-T-Shirts_FR" from the list
0034:         And I should not be able to choose taxon "Woman-T-Shirts_UA" from the list
0035: 
0036:     @ui @mink:chromedriver @no-api
0037:     Scenario: Choosing only taxons from the German locale
0038:         Given I am using "German (Germany)" locale for my panel
0039:         When I want to choose main taxon for product "T-Shirt Batman"
0040:         Then I should be able to choose taxon "Men-T-Shirts_DE" from the list
0041:         And I should be able to choose taxon "Woman-T-Shirts_DE" from the list
0042:         And I should not be able to choose taxon "Woman-T-Shirts_UA" from the list
```
