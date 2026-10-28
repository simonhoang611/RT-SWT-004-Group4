# Case 255 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=Y

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. Scored conservatively under section 8 of the guidelines: NOT YET COUNTED AS A DEFECT because there is no step definition/fixture yet to rule out implicit setup. Point to check: The regenerate recovery codes scenario lacks a Given 2FA enabled. The scenarios run independently, so activation cannot be inherited from a previous scenario. The login/deactivate cases have a complete enabled setup. Coverage: 13/13. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Scenario 1 has both "navigate" and "start activation" for a logged-in user.| AC2(correct): Scenario 1  correct "confirmation step with a QR code".|AC3(correct): Scenario 2 has I enter a valid TOTP token, correct valid token as the AC requires.|AC4(correct): Scenario 2 has Then I should see that two-factor authentication is activated and I should see recovery codes, both results present.|AC5(correct): Scenario 3 repeats the activation flow and then checks activated and the Deactivate option. The Gherkin has no separate "confirm" step (entering the token already includes the confirmation) and does not explicitly say "settings page", a minor deviation that does not change the test result.|AC6(correct): Scenario 4 has Given enabled, sign out, sign in with my username and password, sees the prompt, enters the valid TOTP token and only then Then I should be on the stream page, correct order "token after login, before stream".|AC7(correct): Scenario 5 enters an invalid TOTP token, Then I should still see the two-factor authentication prompt and I should not be on the stream page, covering both parts "access not granted" and "prompt still present".|AC8 (correct): Scenario 6 has When I enter a valid recovery code followed by Then I should be on the stream page, correct recovery code and correct destination, the stream page. AC9(wrong): Scenario 7 only has When I go to the two-factor authentication page and I regenerate recovery codes, missing Given I have two-factor authentication enabled, whereas the AC clearly states "A user with two-factor authentication enabled". The test runs in a state where 2FA is not yet enabled, not the condition the AC requires.|AC10(correct): Scenario 7 has Then I should see the new list of recovery codes, matching "shown the new list". Then does not compare with the old list, but the AC does not require that either.|AC11(correct): Scenario 8 has Given enabled and I deactivate two-factor authentication with the correct password, correct "correct password" from the 2FA page.|AC12(correct): Scenario 8 has Then I should see that two-factor authentication is not activated, correct result after disabling.|AC13(correct): Scenario 9 has Given enabled, deactivate with an incorrect password, Then activated and I should see a Deactivate option, covering both parts "still enabled" and "Deactivate still present".|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=Y

### An original note
AI draft 12/10/2026. Scored conservatively under section 8 of the guidelines: NOT YET COUNTED AS A DEFECT because there is no step definition/fixture yet to rule out implicit setup. Point to check: The regenerate recovery codes scenario lacks a Given 2FA enabled. The scenarios run independently, so activation cannot be inherited from a previous scenario. The login/deactivate cases have a complete enabled setup. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1, AC6, AC8 and AC9 state the initial states clearly.|Scenario 7 lacks Given I have two-factor authentication enabled, both in the Given and in the Background.|the Whens match the actions in the AC (go to the 2FA page, start activation, enter the token, sign in, enter the recovery code, regenerate recovery codes, disable 2FA).|Every expected result is verified by a Then (QR and confirmation step, activated, recovery codes, Deactivate option, prompt, stream page, new list, not activated).|The order configure, sign out, sign in, enter the token (or recovery code), go to the stream follows the correct business process. | ACS WITH PRECONDITION: AC1, AC6, AC8 and AC9

## User story

```text
0001: As a user,
0002: I want to enable, use, regenerate, and disable two-factor authentication,
0003: So that my account is better protected while still allowing secure access and account recovery.
0004: 
0005: Acceptance Criteria:
0006: - A signed-in user can navigate to the two-factor authentication page and start activation.
0007: - When activation is started, the user is shown a confirmation step with a QR code to scan.
0008: - A valid TOTP token confirms activation successfully.
0009: - After successful activation, the user sees that two-factor authentication is activated and is shown recovery codes.
0010: - After confirming activation, the two-factor authentication settings page shows the feature as activated and offers a Deactivate option.
0011: - A user with two-factor authentication enabled must enter a valid TOTP token after username/password login before accessing the stream page.
0012: - If the user enters an invalid TOTP token, access is not granted and the two-factor authentication prompt remains.
0013: - A user with two-factor authentication enabled can sign in using a valid recovery code and reach the stream page.
0014: - A user with two-factor authentication enabled can generate new recovery codes from the two-factor authentication page.
0015: - When recovery codes are regenerated, the user is shown the new list of recovery codes.
0016: - A user can deactivate two-factor authentication from the two-factor authentication page by entering the correct password.
0017: - After successful deactivation, the user sees that two-factor authentication is not activated.
0018: - If the user enters an incorrect password when attempting to deactivate, two-factor authentication remains activated and the Deactivate option is still available.
```

## Generated Gherkin C0

```text
0001: # We can create a separate cucumber profile that will run these tests with Selenium
0002: @javascript
0003: Feature: two-factor authentication
0004: 
0005:   Background:
0006:     Given following user exists:
0007:       | username    | email             |
0008:       | Alice Smith | alice@alice.alice |
0009:     And I sign in as "alice@alice.alice"
0010: 
0011:   Scenario: Start two-factor authentication activation
0012:     When I go to the two-factor authentication page
0013:     And I start two-factor authentication activation
0014:     Then I should see a QR code to scan
0015:     And I should see a confirmation step
0016: 
0017:   Scenario: Confirm two-factor authentication activation with a valid token
0018:     When I go to the two-factor authentication page
0019:     And I start two-factor authentication activation
0020:     And I enter a valid TOTP token
0021:     Then I should see that two-factor authentication is activated
0022:     And I should see recovery codes
0023: 
0024:   Scenario: See two-factor authentication as activated on the settings page
0025:     When I go to the two-factor authentication page
0026:     And I start two-factor authentication activation
0027:     And I enter a valid TOTP token
0028:     Then I should see that two-factor authentication is activated
0029:     And I should see a Deactivate option
0030: 
0031:   Scenario: Require a valid TOTP token after username and password login
0032:     Given I have two-factor authentication enabled
0033:     When I sign out
0034:     And I sign in with my username and password
0035:     Then I should see the two-factor authentication prompt
0036:     When I enter a valid TOTP token
0037:     Then I should be on the stream page
0038: 
0039:   Scenario: Reject an invalid TOTP token after username and password login
0040:     Given I have two-factor authentication enabled
0041:     When I sign out
0042:     And I sign in with my username and password
0043:     Then I should see the two-factor authentication prompt
0044:     When I enter an invalid TOTP token
0045:     Then I should still see the two-factor authentication prompt
0046:     And I should not be on the stream page
0047: 
0048:   Scenario: Sign in with a valid recovery code
0049:     Given I have two-factor authentication enabled
0050:     When I sign out
0051:     And I sign in with my username and password
0052:     Then I should see the two-factor authentication prompt
0053:     When I enter a valid recovery code
0054:     Then I should be on the stream page
0055: 
0056:   Scenario: Regenerate recovery codes
0057:     When I go to the two-factor authentication page
0058:     And I regenerate recovery codes
0059:     Then I should see the new list of recovery codes
0060: 
0061:   Scenario: Deactivate two-factor authentication with the correct password
0062:     Given I have two-factor authentication enabled
0063:     When I go to the two-factor authentication page
0064:     And I deactivate two-factor authentication with the correct password
0065:     Then I should see that two-factor authentication is not activated
0066: 
0067:   Scenario: Keep two-factor authentication activated when deactivation password is incorrect
0068:     Given I have two-factor authentication enabled
0069:     When I go to the two-factor authentication page
0070:     And I deactivate two-factor authentication with an incorrect password
0071:     Then I should see that two-factor authentication is activated
0072:     And I should see a Deactivate option
```

## Archived reference Gherkin

```text
0001: # frozen_string_literal: true
0002: @javascript
0003: Feature: Two-factor autentication
0004: 
0005:   Scenario: Activate 2fa
0006:     Given a user with email "alice@test.com"
0007:     When I sign in as "alice@test.com"
0008:     When I go to the two-factor authentication page
0009:     And I press "Activate"
0010:     Then I should see "Confirm activation"
0011:     When I scan the QR code and fill in a valid TOTP token for "alice@test.com"
0012:     And I press "Confirm and activate"
0013:     Then I should see "Two-factor authentication activated"
0014:     And I should see "Recovery codes"
0015:     When I confirm activation
0016:     Then I should see "Two-factor authentication activated"
0017:     And I should see "Deactivate"
0018: 
0019:   Scenario: Signing in with 2fa activated and correct token
0020:     Given a user with username "alice" and password "secret"
0021:     And 2fa is activated for "alice"
0022:     When I go to the login page
0023:     And I fill in username "alice" and password "secret"
0024:     And press "Sign in"
0025:     Then I should see "Two-factor authentication"
0026:     When I fill in a valid TOTP token for "alice"
0027:     And I press "Sign in"
0028:     Then I should be on the stream page
0029: 
0030:   Scenario: Trying to sign in with 2fa activated and incorrect token
0031:     Given a user with username "alice" and password "secret"
0032:     And 2fa is activated for "alice"
0033:     When I go to the login page
0034:     And I fill in username "alice" and password "secret"
0035:     And press "Sign in"
0036:     Then I should see "Two-factor authentication"
0037:     When I fill in an invalid TOTP token
0038:     And I press "Sign in"
0039:     Then I should see "Two-factor authentication"
0040: 
0041:   Scenario: Signing in with 2fa activated and a recovery code
0042:     Given a user with username "alice" and password "secret"
0043:     And 2fa is activated for "alice"
0044:     When I go to the login page
0045:     And I fill in username "alice" and password "secret"
0046:     And press "Sign in"
0047:     Then I should see "Two-factor authentication"
0048:     When I fill in a recovery code from "alice"
0049:     And I press "Sign in"
0050:     Then I should be on the stream page
0051: 
0052:   Scenario: Regenerating recovery codes
0053:     Given a user with email "alice@test.com"
0054:     And 2fa is activated for "alice@test.com"
0055:     When I sign in as "alice@test.com"
0056:     When I go to the two-factor authentication page
0057:     Then I should see "Generate new recovery codes"
0058:     When I press the recovery code generate button
0059:     Then I should see a list of recovery codes
0060: 
0061:   Scenario: Deactivating 2fa with correct password
0062:     Given a user with email "alice@test.com"
0063:     And 2fa is activated for "alice@test.com"
0064:     When I sign in as "alice@test.com"
0065:     When I go to the two-factor authentication page
0066:     Then I should see "Deactivate"
0067:     When I put in my password in "two_factor_authentication_password"
0068:     And I press "Deactivate"
0069:     Then I should see "Two-factor authentication not activated"
0070: 
0071:   Scenario: Trying to deactivate with incorrect password
0072:     Given a user with email "alice@test.com"
0073:     And 2fa is activated for "alice@test.com"
0074:     When I sign in as "alice@test.com"
0075:     When I go to the two-factor authentication page
0076:     Then I should see "Deactivate"
0077:     When I fill in "two_factor_authentication_password" with "incorrect"
0078:     And I press "Deactivate"
0079:     Then I should see "Two-factor authentication activated"
0080:     And I should see "Deactivate"
```
