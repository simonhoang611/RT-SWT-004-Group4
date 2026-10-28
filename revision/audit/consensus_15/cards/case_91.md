# Case 91 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026; confidence of the comparison: medium. The Background prepares checkout and admin; confirm happens before opening the summary; Then checks the customer's IP. The api/ui tags indicate the intended scope; they do not prove execution in both environments. Coverage: 3/3. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): Scenario has When the customer confirms their order, correct action "confirms and places an order". Gherkin has no Then that directly checks "order stores the IP"; it only checks indirectly via the admin's summary screen, and since the IP can only be shown once it has been stored, it is still satisfied.|AC2(correct): Scenario has And I view the summary of the placed order followed by Then I should see the customer's IP address on the order summary, correct administrator role (Background has I am logged in as an administrator), correct summary screen and correct result of seeing the IP.|AC3(correct): Scenario is tagged @api @ui, i.e. the same scenario runs in both the API and UI contexts, correct "both API and UI contexts" and correct "newly placed orders" because the order is placed within the scenario itself.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=N; Hoang=N

### An original note
AI draft 12/10/2026. The Background prepares checkout and admin; confirm happens before opening the summary; Then checks the customer's IP. The api/ui tags indicate the intended scope; they do not prove execution in both environments. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
Only AC2 states an initial state (“a placed order” exists for the admin to view). AC1 is the action of placing the order, AC3 is a requirement about scope (API and UI).|The Background builds everything needed for the customer to place an order (single-channel store in the US, product “PHP T-Shirt”, cart containing the product, address, shipping method, payment method) and the admin is logged in. The “Placed order” of AC2 is created by the When within the scenario, so no precondition is missing.|the customer confirms their order and I view the summary of the placed order match the actions in AC1 and AC2.|The expected result is verified by a Then. The “storing the IP” of AC1 is checked indirectly via this Then.|The IP shown on the summary is a consequence of the customer confirming the order in the preceding When.|The admin login step comes after the customer's steps in the Background, but it only needs to occur before viewing the summary, so the order is not reversed. | ACS WITH PRECONDITION: AC2

## User story

```text
0001: As a Administrator,
0002: I want to see the customer’s IP address on placed orders,
0003: So that I can know from which IP address a new order was placed.
0004: 
0005: Acceptance Criteria:
0006: - When a customer confirms and places an order, the order stores the customer’s IP address.
0007: - As an administrator, when I view the summary of a placed order, I can see the customer’s IP address.
0008: - The customer’s IP address is available for newly placed orders in both API and UI contexts.
```

## Generated Gherkin C0

```text
0001: @managing_orders
0002: Feature: Seeing the customer's IP address on placed orders
0003: 
0004:     Background:
0005:         Given the store operates on a single channel in "United States"
0006:         And the store has a product "PHP T-Shirt" priced at "$12.00"
0007:         And the customer added product "PHP T-Shirt" to the cart
0008:         And the customer addressed the order
0009:         And the customer selected "United States" as their country
0010:         And the customer chose "United States" as their shipping country
0011:         And the customer chose "United States" as their billing country
0012:         And the customer selected a shipping method
0013:         And the customer selected a payment method
0014:         And I am logged in as an administrator
0015: 
0016:     @api @ui
0017:     Scenario: Seeing the customer's IP address on a placed order
0018:         When the customer confirms their order
0019:         And I view the summary of the placed order
0020:         Then I should see the customer's IP address on the order summary
```

## Archived reference Gherkin

```text
0001: @managing_orders
0002: Feature: Assigning customer's IP address to a placed order
0003:     In order to know from which IP address a new order has been placed
0004:     As an Administrator
0005:     I want to have customer's IP address assigned to their orders
0006: 
0007:     Background:
0008:         Given the store operates on a single channel in "United States"
0009:         And the store has a product "PHP T-Shirt" priced at "$19.99"
0010:         And the store ships everywhere for Free
0011:         And the store allows paying Offline
0012:         And there is a customer account "customer@example.com"
0013:         And there is a customer "customer@example.com" that placed order with "PHP T-Shirt" product to "United States" based billing address with "Free" shipping method and "Offline" payment method without completing it
0014:         And the customer logged in as "customer@example.com"
0015:         And the customer confirmed the order
0016: 
0017:     @api @ui
0018:     Scenario: Verifying the customer's IP address for a newly placed order
0019:         Given I am logged in as an administrator
0020:         When I view the summary of the order placed by "customer@example.com"
0021:         Then I should see this customer's IP address
```
