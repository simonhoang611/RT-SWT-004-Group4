# Case 229 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=Y

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. Navigation, search user/tag, aspects, followed tags and the regular/moderator/admin permissions are all present. The 'on page' assertions are understood as reaching the correct page; the actual UI content/step definitions are not verified. A reviewer needs to confirm the mobile fixture. Coverage: 11/11. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): scenario 1 starts from the activity stream page, clicks the header title, then checks being on the stream page. Starting point, action and result are all as in the AC.|AC2(correct): scenario 2 clicks the notification badge and checks being on the notifications page.|AC3(correct): scenario 3 clicks the conversations badge and checks being on the conversations page.|AC4(correct): scenario 4 clicks the compose badge and checks being on the new status message page.|AC5(correct): scenario 5 searches for “Alice Smith” and checks that the user appears in the results. Scenario 6 searches for “#diaspora” and checks being redirected to the tag page. Both branches, username and hashtag, have their own test, and Alice Smith exists in the Background, so the search result has a basis.|AC6(correct): scenario 7 goes through all 7 items Stream, My activity, Mentions, Aspects, Profile, Contacts, Settings, each item with a step checking the destination page, and reopens the drawer before each click.|AC7(correct): scenario 8 creates two posts in two aspects; selecting Friends shows only the Friends post, selecting Family shows only the Family post. It covers both “only posts of the selected aspect are shown” and “changing the aspect changes the content”.|AC8(correct): scenario 9 follows a tag first, checks that the tag is in “Followed tags”, then goes to all three pages (tag page, followed tags stream, manage tag followings).|AC9 (correct): scenario 10 checks that a regular user does not see “Admin” and “Reports”. The negation is kept as is, not inverted.|AC10(correct): scenario 11 checks that a moderator sees “Reports”, does not see “Admin”, and that clicking “Reports” leads to the reports overview page.|AC11(wrong):  The AC describes Admin as an expandable item for accessing 7 subpages. The Gherkin clicks “Admin” only once and then clicks “Dashboard”. For the remaining 6 items, it does this: When I open the drawer\And I click "User search". After the page change and reopening the drawer, the Admin menu returns to the collapsed state, so “User search” is not yet shown to be clicked. The step I click "Admin" is missing in the 6 later times, so the sequence of actions is in the wrong business order.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=Y

### An original note
AI draft 12/10/2026. Navigation, search user/tag, aspects, followed tags and the regular/moderator/admin permissions are all present. The 'on page' assertions are understood as reaching the correct page; the actual UI content/step definitions are not verified. A reviewer needs to confirm the mobile fixture. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1 (starting from the activity stream page), AC7 (viewing aspects), AC9 to AC11 (by role) state the initial state.|The regular, moderator, admin roles are set up with the steps I am signed in as ... in each scenario.|Each When is the right kind of action the AC describes.|Each result of AC1 to AC11 has at least one Then.|After opening the drawer, the next step clicks a sub-item of Admin while the Admin menu has not been expanded; the step I click "Admin" in between is missing. | ACS WITH PRECONDITION: AC1, AC7, AC9, AC10, AC11

## User story

```text
0001: As a mobile website user,
0002: I want to navigate between different pages (stream, notifications, conversations, publisher, profile, contacts, settings, aspects, tags, and admin/moderation areas) using the header menu and the drawer navigation,
0003: So that I can quickly access the content and features relevant to my role and preferences without confusion.
0004: 
0005: Acceptance Criteria:
0006: - Clicking the header title from the activity stream page navigates the user to the stream page.
0007: - Clicking the notification badge navigates the user to the notifications page.
0008: - Clicking the conversations badge navigates the user to the conversations page.
0009: - Clicking the compose badge navigates the user to the new status message page.
0010: - Opening the drawer displays a search input, and searching for a username shows matching users while searching for a hashtag navigates to the corresponding tag page.
0011: - The drawer provides navigation links to the stream page, my activity page, mentions page, aspects pages, profile page, contacts page, and settings page, each leading to the correct destination.
0012: - When viewing aspects, only posts belonging to the selected aspect are displayed within the main stream, and switching aspects updates the visible content accordingly.
0013: - Following a tag adds it to the "Followed tags" section in the drawer, allowing navigation to its tag page, the followed tags stream page, and the manage tag followings page.
0014: - Regular users do not see "Admin" or "Reports" options in the drawer.
0015: - Moderators see a "Reports" option in the drawer (but not "Admin"), which leads to the reports overview page.
0016: - Admins see an "Admin" option in the drawer (but not "Reports" or "Dashboard" directly), which expands to provide access to Dashboard, User search, Weekly user stats, Pod stats, Reports, Pod network, and Sidekiq monitor pages, each displaying the correct corresponding content.
```

## Generated Gherkin C0

```text
0001: # We can create a separate cucumber profile that will run these tests with Selenium
0002: @javascript
0003: Feature: mobile navigation
0004: 
0005:   Background:
0006:     Given following user exists:
0007:       | username    | email             |
0008:       | Alice Smith | alice@alice.alice |
0009:       | Bob Jones   | bob@bob.bob       |
0010: 
0011:   Scenario: Navigate to the stream page from the header title
0012:     Given I am on the activity stream page
0013:     When I click the header title
0014:     Then I should be on the stream page
0015: 
0016:   Scenario: Navigate to the notifications page from the notification badge
0017:     Given I am on the activity stream page
0018:     When I click the notification badge
0019:     Then I should be on the notifications page
0020: 
0021:   Scenario: Navigate to the conversations page from the conversations badge
0022:     Given I am on the activity stream page
0023:     When I click the conversations badge
0024:     Then I should be on the conversations page
0025: 
0026:   Scenario: Navigate to the new status message page from the compose badge
0027:     Given I am on the activity stream page
0028:     When I click the compose badge
0029:     Then I should be on the new status message page
0030: 
0031:   Scenario: Search for a user from the drawer
0032:     Given I am on the activity stream page
0033:     When I open the drawer
0034:     And I search for "Alice Smith"
0035:     Then I should see "Alice Smith" in the search results
0036: 
0037:   Scenario: Search for a hashtag from the drawer
0038:     Given I am on the activity stream page
0039:     When I open the drawer
0040:     And I search for "#diaspora"
0041:     Then I should be on the tag page for "#diaspora"
0042: 
0043:   Scenario: Navigate to pages from the drawer
0044:     Given I am on the activity stream page
0045:     When I open the drawer
0046:     And I click "Stream"
0047:     Then I should be on the stream page
0048:     When I open the drawer
0049:     And I click "My activity"
0050:     Then I should be on the my activity page
0051:     When I open the drawer
0052:     And I click "Mentions"
0053:     Then I should be on the mentions page
0054:     When I open the drawer
0055:     And I click "Aspects"
0056:     Then I should be on the aspects page
0057:     When I open the drawer
0058:     And I click "Profile"
0059:     Then I should be on the profile page
0060:     When I open the drawer
0061:     And I click "Contacts"
0062:     Then I should be on the contacts page
0063:     When I open the drawer
0064:     And I click "Settings"
0065:     Then I should be on the settings page
0066: 
0067:   Scenario: Switch aspects from the drawer and see only posts from the selected aspect
0068:     Given I am on the activity stream page
0069:     And I have a post in my "Friends" aspect
0070:     And I have a post in my "Family" aspect
0071:     When I open the drawer
0072:     And I click "Friends"
0073:     Then I should see only posts from my "Friends" aspect in the main stream
0074:     When I open the drawer
0075:     And I click "Family"
0076:     Then I should see only posts from my "Family" aspect in the main stream
0077: 
0078:   Scenario: Follow a tag and navigate to followed tag pages from the drawer
0079:     Given I am on the activity stream page
0080:     When I follow the tag "#diaspora"
0081:     And I open the drawer
0082:     Then I should see "#diaspora" in the "Followed tags" section
0083:     When I click "#diaspora" in the "Followed tags" section
0084:     Then I should be on the tag page for "#diaspora"
0085:     When I open the drawer
0086:     And I click "Followed tags"
0087:     Then I should be on the followed tags stream page
0088:     When I open the drawer
0089:     And I click "Manage tag followings"
0090:     Then I should be on the manage tag followings page
0091: 
0092:   Scenario: Regular users do not see admin or reports options in the drawer
0093:     Given I am signed in as a regular user
0094:     When I open the drawer
0095:     Then I should not see "Admin"
0096:     And I should not see "Reports"
0097: 
0098:   Scenario: Moderators see reports in the drawer
0099:     Given I am signed in as a moderator
0100:     When I open the drawer
0101:     Then I should see "Reports"
0102:     And I should not see "Admin"
0103:     When I click "Reports"
0104:     Then I should be on the reports overview page
0105: 
0106:   Scenario: Admins see admin navigation in the drawer
0107:     Given I am signed in as an admin
0108:     When I open the drawer
0109:     Then I should see "Admin"
0110:     And I should not see "Reports"
0111:     And I should not see "Dashboard"
0112:     When I click "Admin"
0113:     Then I should see "Dashboard"
0114:     And I should see "User search"
0115:     And I should see "Weekly user stats"
0116:     And I should see "Pod stats"
0117:     And I should see "Reports"
0118:     And I should see "Pod network"
0119:     And I should see "Sidekiq monitor"
0120:     When I click "Dashboard"
0121:     Then I should be on the dashboard page
0122:     When I open the drawer
0123:     And I click "User search"
0124:     Then I should be on the user search page
0125:     When I open the drawer
0126:     And I click "Weekly user stats"
0127:     Then I should be on the weekly user stats page
0128:     When I open the drawer
0129:     And I click "Pod stats"
0130:     Then I should be on the pod stats page
0131:     When I open the drawer
0132:     And I click "Reports"
0133:     Then I should be on the reports page
0134:     When I open the drawer
0135:     And I click "Pod network"
0136:     Then I should be on the pod network page
0137:     When I open the drawer
0138:     And I click "Sidekiq monitor"
0139:     Then I should be on the sidekiq monitor page
```

## Archived reference Gherkin

```text
0001: @javascript @mobile
0002: Feature: Navigate between pages using the header menu and the drawer
0003: 
0004:   Background:
0005:     Given a user with email "alice@alice.alice"
0006:     And I sign in as "alice@alice.alice" on the mobile website
0007: 
0008:   Scenario: navigate to the stream page
0009:     When I go to the activity stream page
0010:     And I click on selector ".header-title"
0011:     Then I should be on the stream page
0012: 
0013:   Scenario: navigate to the notification page
0014:     When I click on selector "#notification-badge"
0015:     Then I should be on the notifications page
0016: 
0017:   Scenario: navigate to the conversation page
0018:     When I click on selector "#conversations-badge"
0019:     Then I should be on the conversations page
0020: 
0021:   Scenario: navigate to the publisher page
0022:     When I click on selector "#compose-badge"
0023:     Then I should be on the new status message page
0024: 
0025:   Scenario: search a user
0026:     When I open the drawer
0027:     Then I should see a "#q" within "#drawer"
0028:     When I search for "Bob"
0029:     Then I should see "Users matching Bob" within "#search_title"
0030: 
0031:   Scenario: search for a tag
0032:     When I open the drawer
0033:     Then I should see a "#q" within "#drawer"
0034:     When I search for "#bob"
0035:     Then I should be on the tag page for "bob"
0036: 
0037:   Scenario: navigate to the stream page
0038:     When I open the drawer
0039:     And I click on "Stream" in the drawer
0040:     Then I should be on the stream page
0041: 
0042:   Scenario: navigate to my activity page
0043:     When I open the drawer
0044:     And I click on "My activity" in the drawer
0045:     Then I should be on the activity stream page
0046: 
0047:   Scenario: navigate to my mentions page
0048:     When I open the drawer
0049:     And I click on "@Mentions" in the drawer
0050:     Then I should be on the mentioned stream page
0051: 
0052:   Scenario: navigate to aspects pages
0053:     Given I have a limited post with text "Hi you!" in the aspect "Besties"
0054:     When I open the drawer
0055:     Then I should not see "All aspects" within "#drawer"
0056:     And I click on "My aspects" in the drawer
0057:     And I click on "All aspects" in the drawer
0058:     Then I should be on the aspects page
0059:     And I should see "Hi you!" within "#main-stream"
0060:     When I open the drawer
0061:     And I click on "My aspects" in the drawer
0062:     And I click on "Unicorns" in the drawer
0063:     And I should not see "Hi you!" within "#main-stream"
0064: 
0065:   Scenario: navigate to the followed tags page
0066:     When I follow the "boss" tag
0067:     And I go to the stream page
0068:     And I open the drawer
0069:     Then I should not see "All tags" within "#drawer"
0070:     And I click on "#Followed tags" in the drawer
0071:     And I click on "All tags" in the drawer
0072:     Then I should be on the followed tags stream page
0073: 
0074:   Scenario: navigate to the boss tag page
0075:     When I follow the "boss" tag
0076:     And I go to the stream page
0077:     And I open the drawer
0078:     And I click on "#Followed tags" in the drawer
0079:     And I click on "#boss" in the drawer
0080:     Then I should be on the tag page for "boss"
0081: 
0082:     When I open the drawer
0083:     And I click on "#Followed tags" in the drawer
0084:     And I click on "Manage followed tags" in the drawer
0085:     Then I should be on the manage tag followings page
0086: 
0087:   Scenario: navigate to the public stream page
0088:     When I open the drawer
0089:     And I click on "Public activity" in the drawer
0090:     Then I should be on the public stream page
0091: 
0092:   Scenario: navigate to my profile page
0093:     When I open the drawer
0094:     And I click on "Profile" in the drawer
0095:     Then I should be on my profile page
0096: 
0097:   Scenario: navigate to my contacts page
0098:     When I open the drawer
0099:     And I click on "Contacts" in the drawer
0100:     Then I should be on the contacts page
0101: 
0102:   Scenario: navigate to my settings page
0103:     When I open the drawer
0104:     And I click on "Settings" in the drawer
0105:     Then I should be on my account settings page
0106: 
0107:   Scenario: navigate to the moderation page
0108:     Given a moderator with email "bob@bob.bob"
0109:     And I sign in as "bob@bob.bob" on the mobile website
0110:     When I open the drawer
0111:     Then I should not see "Admin" within "#drawer"
0112:     And I should see "Reports" within "#drawer"
0113:     When I click on "Reports" in the drawer
0114:     Then I should see "Reports overview" within "#main h1"
0115: 
0116:   Scenario: navigate to the admin pages
0117:     Given an admin with email "bob@bob.bob"
0118:     And I sign in as "bob@bob.bob" on the mobile website
0119:     When I open the drawer
0120:     Then I should not see "Reports" within "#drawer"
0121:     Then I should not see "Dashboard" within "#drawer"
0122:     When I click on "Admin" in the drawer
0123:     And I click on "Dashboard" in the drawer
0124:     Then I should see "Pod status" within "#main h2"
0125:     When I click on "Admin" in the drawer
0126:     And I click on "User search" in the drawer
0127:     Then I should see "User search" within "#main h3"
0128:     When I click on "Admin" in the drawer
0129:     And I click on "Weekly user stats" in the drawer
0130:     Then I should see "Current server date is " within "#main h2"
0131:     When I click on "Admin" in the drawer
0132:     And I click on "Pod stats" in the drawer
0133:     Then I should see "Usage statistics" within "#main h1"
0134:     When I click on "Admin" in the drawer
0135:     And I click on "Reports" in the drawer
0136:     Then I should see "Reports overview" within "#main h1"
0137:     When I click on "Admin" in the drawer
0138:     And I click on "Pod network" in the drawer
0139:     Then I should see "Pod network" within "#main h2"
0140:     When I click on "Admin" in the drawer
0141:     Then I should see "Sidekiq monitor" within "#drawer"
0142: 
0143:   Scenario: users doesn't have access to the admin pages
0144:     When I open the drawer
0145:     Then I should not see "Admin" within "#drawer"
0146:     Then I should not see "Reports" within "#drawer"
```
