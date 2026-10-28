 # We can create a separate cucumber profile that will run these tests with Selenium
@javascript
Feature: oembed

  Background:
    Given following user exists:
      | username    | email             |
      | Alice Smith | alice@alice.alice |
    And I sign in as "alice@alice.alice"

  Scenario: Post a video link
    When I click the publisher and post "[title](https://example.com/file.ogv)"
    Then I should see a HTML5 video player

  Scenario: Post an audio link
    When I click the publisher and post "[title](https://example.com/file.ogg)"
    Then I should see a HTML5 audio player

