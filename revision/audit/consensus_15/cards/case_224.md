# Case 224 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: high. There are 3 users, so at least two is satisfied; connections/public/mention/hashtag are all present. Both reference/comparison run logged-out then logged-in and have the correct directory. OP_MISSING is a false positive. Coverage: 4/4. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Background creates the data the AC requires: two users “B Robertson” and “A Aronsdottir”, the are connected step, a public post by each of them, one post with a mention and one post with a hashtag. The Gherkin has three users (adding Alice Smith), still satisfying “at least two”.|AC2(correct): Scenario 1 takes screenshots while not logged in, Then checks that the screenshots are in the reference directory. Scenario 2 does the same with the comparison directory.|AC3(correct): Both scenarios have I sign in as "alice@alice.alice" followed by taking screenshots while logged in, correct user as in the AC.|AC4(correct): The two scenarios are two different modes (reference and comparison), with the same order: screenshot logged out, sign in, screenshot logged in.

## temporal_causal: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026. There are 3 users, so at least two is satisfied; connections/public/mention/hashtag are all present. Both reference/comparison run logged-out then logged-in and have the correct directory. OP_MISSING is a false positive. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC2 states the state “being logged out” and AC3 states “after signing in”.|The Background already has the users, the connection, the public posts, the mention post and the hashtag post.|The When taking screenshots (reference or comparison) is the action the AC describes.|Each scenario has one Then checking that the screenshots were saved in the correct directory.|The Then checking the directory is a direct consequence of the screenshot steps.|The order is correct: create the users and posts, take screenshots while logged out, sign in, and only then take screenshots while logged in. | ACS WITH PRECONDITION: AC2, AC3

## User story

```text
0001: As a QA Engineer,
0002: I want to capture reference and comparison screenshots of the application layout in both logged-out and logged-in states,
0003: So that I can detect unintended visual regressions across different user scenarios and content types.
0004: 
0005: Acceptance Criteria:
0006: - Test data includes at least two users (e.g., "B Robertson" and "A Aronsdottir") who are connected to each other, along with sample public posts, a post that mentions another user, and a post containing a hashtag.
0007: - Screenshots can be captured while the user is logged out, saving them into a designated reference or comparison directory depending on the test run type.
0008: - Screenshots can also be captured after signing in as a specific user (e.g., "alice@alice.alice"), reflecting the logged-in view of the layout.
0009: - The system supports two distinct screenshot-taking modes: one for generating reference screenshots and another for generating comparison screenshots, both following the same logged-out and logged-in capture sequence.
```

## Generated Gherkin C0

```text
0001: # We can create a separate cucumber profile that will run these tests with Selenium
0002: @javascript
0003: Feature: layout screenshots
0004: 
0005:   Background:
0006:     Given following user exists:
0007:       | username      | email                 |
0008:       | B Robertson   | b.robertson@diaspora |
0009:       | A Aronsdottir | a.aronsdottir@diaspora |
0010:       | Alice Smith   | alice@alice.alice     |
0011:     And "B Robertson" and "A Aronsdottir" are connected
0012:     And "B Robertson" has a public post "Public post from B Robertson"
0013:     And "A Aronsdottir" has a public post "Public post from A Aronsdottir"
0014:     And "B Robertson" has a public post mentioning "A Aronsdottir"
0015:     And "A Aronsdottir" has a public post with hashtag "#diaspora"
0016: 
0017:   Scenario: Capture reference screenshots while logged out and logged in
0018:     When I capture reference screenshots of the layout while logged out
0019:     And I sign in as "alice@alice.alice"
0020:     And I capture reference screenshots of the layout while logged in
0021:     Then I should have reference screenshots in the reference directory
0022: 
0023:   Scenario: Capture comparison screenshots while logged out and logged in
0024:     When I capture comparison screenshots of the layout while logged out
0025:     And I sign in as "alice@alice.alice"
0026:     And I capture comparison screenshots of the layout while logged in
0027:     Then I should have comparison screenshots in the comparison directory
```

## Archived reference Gherkin

```text
0001: @screenshots @javascript
0002: Feature: layout reference screenshots
0003: 
0004:   Background:
0005:     Given following users exist:
0006:       | username       | email             |
0007:       | B Robertson   | bob@bob.bob       |
0008:       | A Aronsdottir | alice@alice.alice |
0009:     And a user with email "bob@bob.bob" is connected with "alice@alice.alice"
0010:     And "bob@bob.bob" has a public post with text "this is a test post!"
0011:     And Alice has a post mentioning Bob
0012:     And "alice@alice.alice" has a public post with text "i am using a #tag"
0013: 
0014:   @reference-screenshots
0015:   Scenario: take the reference screenshots
0016:     Given the reference screenshot directory is used
0017:     When I take the screenshots while logged out
0018: 
0019:     And I sign in as "alice@alice.alice"
0020:     Then I take the screenshots while logged in
0021: 
0022:   @comparison-screenshots
0023:   Scenario: take the comparison screenshots
0024:     Given the comparison screenshot directory is used
0025:     When I take the screenshots while logged out
0026: 
0027:     And I sign in as "alice@alice.alice"
0028:     Then I take the screenshots while logged in
```
