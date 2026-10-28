# Case 238 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: high. The two Bitcoin/Liberapay configurations have separate setups; Donate is in the info-bar and the content after the click is correct. Coverage: 4/4. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Scenario 1 has Given I have configured a Bitcoin address, When I go to the home page, Then I should see "Donate" within ".info-bar", correct condition, correct home page and correct .info-bar area.|AC2(correct): Scenario 1 has When I click on "Donate" followed by Then I should see the configured Bitcoin address, correct result of displaying the configured address. The Gherkin only writes click on "Donate" and does not explicitly say "navbar title", a minor deviation that does not change the test result.|AC3(correct): Scenario 2 has Given I have configured a Liberapay username, When I go to the home page, Then I should see "Donate" within ".info-bar" with Liberapay.|AC4(correct): Scenario 2 has When I click on "Donate" followed by Then I should see the Liberapay donate button, correct result of displaying the Liberapay donate button, not mixed up with the Bitcoin address. Only writes click on "Donate" instead of "navbar title". |CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026. The two Bitcoin/Liberapay configurations have separate setups; Donate is in the info-bar and the content after the click is correct. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1 and AC3 state the initial states clearly (“When I have configured a Bitcoin address / a Liberapay username”).|Both preconditions are in the Given of each scenario; each scenario configures exactly what it checks.|I go to the home page and I click on "Donate" match the actions in the AC.|All 4 results are verified by a Then.|The Then after the click checks the content shown because of the click, and that content is a consequence of the configuration in Given.|The order configure, go to home, see the link, click, see the content follows the correct business process. | ACS WITH PRECONDITION: AC1 and AC3

## User story

```text
0001: As a podmin,
0002: I want to display a donation box on the stream page,
0003: So that visitors can easily support the pod.
0004: 
0005: Acceptance Criteria:
0006: - When I have configured a Bitcoin address, the home page shows a “Donate” link in the `.info-bar`.
0007: - When I click the “Donate” navbar title, the configured Bitcoin address is displayed.
0008: - When I have configured a Liberapay username, the home page shows a “Donate” link in the `.info-bar`.
0009: - When I click the “Donate” navbar title, the Liberapay donate button is displayed.
```

## Generated Gherkin C0

```text
0001: # We can create a separate cucumber profile that will run these tests with Selenium
0002: @javascript
0003: Feature: donation box
0004: 
0005:   Background:
0006:     Given following user exists:
0007:       | username | email           |
0008:       | Podmin   | podmin@podmin.alice |
0009:     And I sign in as "podmin@podmin.alice"
0010: 
0011:   Scenario: Show a donate link when a Bitcoin address is configured
0012:     Given I have configured a Bitcoin address
0013:     When I go to the home page
0014:     Then I should see "Donate" within ".info-bar"
0015:     When I click on "Donate"
0016:     Then I should see the configured Bitcoin address
0017: 
0018:   Scenario: Show a donate link when a Liberapay username is configured
0019:     Given I have configured a Liberapay username
0020:     When I go to the home page
0021:     Then I should see "Donate" within ".info-bar"
0022:     When I click on "Donate"
0023:     Then I should see the Liberapay donate button
```

## Archived reference Gherkin

```text
0001: @javascript
0002: Feature: donations
0003:   In order to accept donation
0004:   As a podmin
0005:   I want a donation box shown on the stream page
0006: 
0007:   Background:
0008:     Given following user exists:
0009:       | username | email             |
0010:       | Alice    | alice@alice.alice |
0011:     And I sign in as "alice@alice.alice"
0012: 
0013:   Scenario: Bitcoin donations
0014:     Given I have configured a Bitcoin address
0015:     And I go to the home page
0016:     Then I should see "Donate" within ".info-bar"
0017:     And I click on "Donate" navbar title
0018:     Then I should see the Bitcoin address
0019: 
0020:   Scenario: Liberapay donations
0021:     Given I have configured a Liberapay username
0022:     And I go to the home page
0023:     Then I should see "Donate" within ".info-bar"
0024:     And I click on "Donate" navbar title
0025:     Then I should see the Liberapay donate button
```
