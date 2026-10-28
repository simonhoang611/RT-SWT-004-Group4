# Case 236 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. Scored conservatively under section 8 of the guidelines: NOT YET COUNTED AS A DEFECT because there is no step definition/fixture yet to rule out implicit setup. Point to check: AC5 needs an already existing public post to check that it is still visible on the profile after the block; the Background only creates users and does not create a public post. Need to confirm whether the user fixture generates a public post by itself before keeping this label. Coverage: 6/6. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Scenario 1 has the step I click the block button followed by I confirm the block action, covering both parts "click block button" and "confirming the action".|AC2(correct): Scenario 1 has two Thens: no posts from Bob Jones in my home stream and no related posts from Bob Jones in my home stream, matching "no posts from that user or related posts".|AC3(correct): Scenario 2 has I click the profile block button followed by I confirm the block action, correct block button on the profile page and has the confirmation step.|AC4(correct): Scenario 2 has Then I should see "Stop ignoring" in the unblock area, correct string "Stop ignoring" and correct unblock area as in the AC.|AC5 (correct): Scenario 2 has And I should see Bob Jones's public post on their profile page, correct "public post" and correct profile page of the blocked person.|AC6(correct): Scenario 2 has When I go to the home page followed by Then I should see no posts in my stream, correct order: block on the profile, go back home, check the stream.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background.

## temporal_causal: initial An=N; Hoang=Y

### An original note
AI draft 12/10/2026. Scored conservatively under section 8 of the guidelines: NOT YET COUNTED AS A DEFECT because there is no step definition/fixture yet to rule out implicit setup. Point to check: AC5 needs an already existing public post to check that it is still visible on the profile after the block; the Background only creates users and does not create a public post. Need to confirm whether the user fixture generates a public post by itself before keeping this label. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
No AC states an initial state.|Scenario 1 and AC6 need Bob to have a post that appears in Alice's stream, i.e. Alice and Bob must be connected (sharing or following) and Bob must publish a post. Currently the Background only creates 2 users, with no posts.Scenario 2 needs Bob to have a public post. Without a post, Then see Bob Jones's public post will FAIL.|The Whens match the actions in the AC.|All 6 expected results are verified by a Then.|The sequence visit, click, confirm, then check is in the correct business order.

## User story

```text
0001: As a user,
0002: I want to block another user from my stream or profile,
0003: So that I can stop seeing their posts and mentions in my feed.
0004: 
0005: Acceptance Criteria:
0006: - I can block a user by clicking the block button from the stream and confirming the action.
0007: - After blocking a user from the stream, my home stream shows no posts from that user or related posts.
0008: - I can block a user from their profile page by clicking the profile block button and confirming the action.
0009: - After blocking a user from their profile page, the button changes to “Stop ignoring” in the unblock area.
0010: - After blocking a user from their profile page, I can still see the blocked user’s public post on their profile page.
0011: - After blocking a user from their profile page, returning to the home page shows no posts in my stream.
```

## Generated Gherkin C0

```text
0001: @javascript
0002: Feature: block users
0003: 
0004:   Background:
0005:     Given following users exist:
0006:       | username    | email             |
0007:       | Alice Smith | alice@alice.alice |
0008:       | Bob Jones   | bob@bob.bob       |
0009:     And I sign in as "alice@alice.alice"
0010: 
0011:   Scenario: Block a user from the stream
0012:     When I visit Bob Jones's stream
0013:     And I click the block button
0014:     And I confirm the block action
0015:     Then I should see no posts from Bob Jones in my home stream
0016:     And I should see no related posts from Bob Jones in my home stream
0017: 
0018:   Scenario: Block a user from their profile page
0019:     When I visit Bob Jones's profile page
0020:     And I click the profile block button
0021:     And I confirm the block action
0022:     Then I should see "Stop ignoring" in the unblock area
0023:     And I should see Bob Jones's public post on their profile page
0024:     When I go to the home page
0025:     Then I should see no posts in my stream
```

## Archived reference Gherkin

```text
0001: @javascript
0002: Feature: Blocking a user from the stream
0003:   Background:
0004:     Given following users exist:
0005:       | username    | email             |
0006:       | Bob Jones   | bob@bob.bob       |
0007:       | Alice Smith | alice@alice.alice |
0008:     And a user with email "bob@bob.bob" is connected with "alice@alice.alice"
0009:     And Alice has a post mentioning Bob
0010:     And "alice@alice.alice" has a public post with text "All your base are belong to us!"
0011:     And I sign in as "bob@bob.bob"
0012: 
0013:   Scenario: Blocking a user
0014:     When I confirm the alert after I click on the first block button
0015:     And I go to the home page
0016:     Then I should not see any posts in my stream
0017: 
0018:   Scenario: Blocking a user from the profile page
0019:     When I am on "alice@alice.alice"'s page
0020:     And I confirm the alert after I click on the profile block button
0021:     Then I should see "Stop ignoring" within "#unblock_user_button"
0022:     And "All your base are belong to us!" should be post 1
0023:     When I go to the home page
0024:     Then I should not see any posts in my stream
```
