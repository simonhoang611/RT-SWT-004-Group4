# Case 207 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. There is a user/public post; it opens the web+diaspora link and checks the correct text. The hard-coded link posts/1 needs confirmation that the fixture assigns the post the correct ID; there is no ID data to conclude that it points to the wrong post, so no defect is counted. Coverage: 3/3. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Background creates a user, signs in and publishes a public post. Scenario uses the link web+diaspora:// pointing to that post.|AC2(correct): the When step opens the external link, correct action as the AC describes.|AC3(correct): Then I should see "This is a public post" correctly checks the text content of the post.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026. There is a user/public post; it opens the web+diaspora link and checks the correct text. The hard-coded link posts/1 needs confirmation that the fixture assigns the post the correct ID; there is no ID data to conclude that it points to the wrong post, so no defect is counted. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
Only AC1 states the initial state clearly (user registered, has a public post). AC2 implicitly requires a post to exist but does not say so.|The Background has the user, the sign-in and the public post.|When I open the external link ... matches the action in AC2.|Each expected result is verified by a Then. AC2 is checked indirectly via the same Then step.|The order is the correct business order: create the user, sign in, publish the post, and only then open the link. | ACS WITH PRECONDITION: AC1

## User story

```text
0001: As a user,
0002: I want web+diaspora:// links to resolve directly to the corresponding post,
0003: So that I can access shared content through external links without extra navigation.
0004: 
0005: Acceptance Criteria:
0006: - A registered user with a public post can be referenced by an external web+diaspora:// link.
0007: - Opening an external link pointing to a specific user's post navigates to that post's content.
0008: - The resolved page correctly displays the text content of the linked post.
```

## Generated Gherkin C0

```text
0001: # We can create a separate cucumber profile that will run these tests with Selenium
0002: @javascript
0003: Feature: web+diaspora links
0004: 
0005:   Background:
0006:     Given following user exists:
0007:       | username    | email             |
0008:       | Alice Smith | alice@alice.alice |
0009:     And I sign in as "alice@alice.alice"
0010:     And I post a public message "This is a public post"
0011: 
0012:   Scenario: Open a web+diaspora link to a post
0013:     When I open the external link "web+diaspora://alice@alice.alice/posts/1"
0014:     Then I should see "This is a public post"
```

## Archived reference Gherkin

```text
0001: @javascript
0002: Feature: (web+)diaspora:// links resolve
0003: 
0004:   Background:
0005:     Given following user exists:
0006:       | username | email             |
0007:       | Alice    | alice@alice.alice |
0008:     And "alice@alice.alice" has a public post with text "This is a post accessed by an external link"
0009: 
0010:   Scenario: Resolving web+diaspora:// link
0011:     When I open an external link to the first post of "alice@alice.alice"
0012:     Then I should see "This is a post accessed by an external link"
```
