# Case 88 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. Scored conservatively under section 8 of the guidelines: NOT YET COUNTED AS A DEFECT because there is no step definition/fixture yet to rule out implicit setup. Point to check: The no-theme case has only the scenario name, with no Given confirming that the channel uses no theme. A reviewer needs to check whether the single-channel fixture guarantees no-theme by default; if it does, there is no defect. Coverage: 3/3. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Scenario 1 has When I visit the homepage followed by Then I should not see "Onions and bananas", correct action "visiting its homepage" and correctly keeps "should not display".|AC2(correct): Scenario 2 has Given the channel uses the "maverick/meerkat" theme, When I visit the homepage, Then I should see "Onions and bananas", correct theme name "maverick/meerkat" and correct result of seeing the theme's homepage.|AC3(correct): Then in Scenario 2 correctly checks the content "Onions and bananas" that the AC uses as an example of the theme changing the homepage template content. Scenario 1 is the control (without the theme this text is absent), so the two scenarios together show that the theme is the cause of the content change.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026. Scored conservatively under section 8 of the guidelines: NOT YET COUNTED AS A DEFECT because there is no step definition/fixture yet to rule out implicit setup. Point to check: The no-theme case has only the scenario name, with no Given confirming that the channel uses no theme. A reviewer needs to check whether the single-channel fixture guarantees no-theme by default; if it does, there is no defect. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1 and AC2 both state the initial state of the channel. AC3 only describes a capability of the theme and states no initial state.|AC2 has an explicit Given. AC1 has no Given “channel does not use a theme”, but this is the default state of a channel.|I visit the homepage matches the action “visiting its homepage” in AC1 and AC2.|All three expected results are verified by a Then (the text not seen in Scenario 1, the text seen in Scenario 2, and that text is exactly the example of AC3).|The homepage content in Then is the result of whether the channel has a theme or not in Given, and When only opens the page to see the interface.|The order set up the channel, assign the theme (Scenario 2), and only then go to the homepage follows the correct business process. | ACS WITH PRECONDITION: AC1 and AC2

## User story

```text
0001: As a Visitor,
0002: I want to see a themed user interface on each channel website,
0003: So that I can easily distinguish stores.
0004: 
0005: Acceptance Criteria:
0006: - When a channel does not use any theme, visiting its homepage should not display the homepage from the theme.
0007: - When a channel uses the "maverick/meerkat" theme, visiting its homepage should display the themed homepage.
0008: - The theme should be able to change the homepage template contents, such as showing "Onions and bananas".
```

## Generated Gherkin C0

```text
0001: @theme_management
0002: Feature: Seeing a themed user interface on a channel website
0003: 
0004:     Background:
0005:         Given the store operates on a single channel in "United States"
0006: 
0007:     @ui
0008:     Scenario: Not displaying a themed homepage when the channel does not use any theme
0009:         When I visit the homepage
0010:         Then I should not see "Onions and bananas"
0011: 
0012:     @ui
0013:     Scenario: Displaying the themed homepage when the channel uses the "maverick/meerkat" theme
0014:         Given the channel uses the "maverick/meerkat" theme
0015:         When I visit the homepage
0016:         Then I should see "Onions and bananas"
```

## Archived reference Gherkin

```text
0001: @theming
0002: Feature: Displaying themed channel website
0003:     In order to easily distinguish stores
0004:     As an Visitor
0005:     I want to see a different user interface on each one
0006: 
0007:     Background:
0008:         Given the store operates on a single channel in "United States"
0009:         And the store has "maverick/meerkat" theme
0010:         And this theme changes homepage template contents to "Onions and bananas"
0011: 
0012:     @no-api @ui
0013:     Scenario: Displaying default shop homepage
0014:         Given channel "United States" does not use any theme
0015:         When I visit this channel's homepage
0016:         Then I should not see a homepage from "maverick/meerkat" theme
0017: 
0018:     @no-api @ui
0019:     Scenario: Displaying themed shop homepage
0020:         Given channel "United States" uses "maverick/meerkat" theme
0021:         When I visit this channel's homepage
0022:         Then I should see a homepage from that theme
```
