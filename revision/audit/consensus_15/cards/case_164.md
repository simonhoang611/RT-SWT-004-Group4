# Case 164 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026; confidence of the comparison: high. UC8 runs COB on 31/01 first and then runs it again on 28/29/30/01 to describe remaining days after repayment: the date sequence is not increasing; the timeline needs to be fixed, or it must be explained clearly that backdated COB is supported. The two daily interest ACs only have 'following values' without an expected table. The 6 periods and the transaction types/flags have other complete assertions. Coverage: 10/12. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): UC1 and UC2 create product, client, loan, approve, disburse with valid attributes(declining balance, equal installments, daily, advanced payment allocation, 6 months).|AC2(correct): UC2 checks 6 periods with principal, interest, due, outstanding.|AC3(correct): UC1 and UC3 check that the tab has only disbursement.|AC4 (correct): UC4 runs COB on 02, 03, 04 January and checks daily accrual up to the COB date.|AC5 (correct): UC5 checks the allocation of the repayment between principal and interest.|AC6(correct): UC6 checks that the schedule marks paid and updates total paid, outstanding.|AC7(correct): UC7 checks that there is a repayment without accrual and that there is accrual activity for the interest portion of the period.|AC8(wrong): UC8 runs COB on 31 January first, then the repayment, and only then runs COB on 28, 29, 30 January, so the business date goes backwards, and therefore the Then that accrual continues for the remaining days of January cannot be a consequence of the When.|AC9(correct): UC9 checks accrual activity per period and daily accrual for the past days. The second Then step checks that accrual activity shows the total interest of the completed period.|AC10(correct): UC10 and UC1 check that the history distinguishes repayment, accrual, accrual activity.|AC11(correct): merged with AC10 above; those two scenarios also cover AC11.|AC12(correct): UC11 and UC1 check that the replayed/reverted flags are false for all four transaction types (disbursement, repayment, accrual, accrual activity).|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026. UC8 runs COB on 31/01 first and then runs it again on 28/29/30/01 to describe remaining days after repayment: the date sequence is not increasing; the timeline needs to be fixed, or it must be explained clearly that backdated COB is supported. The two daily interest ACs only have 'following values' without an expected table. The 6 periods and the transaction types/flags have other complete assertions. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
the ACs state the initial states clearly (after disbursement, after repayment, after COB).|The scenarios all build product, client, loan in the initial chain of steps and have no separate Given/Background, the same as how the UCs of the Batch API part were scored.|The When of each scenario matches the action the AC describes (COB, repayment, creating and disbursing the loan).|Each expected result of AC1 to AC12 has at least one Then.|COB on 31 January runs first, after which COB runs on 28, 29, 30 January, i.e. the business date goes backwards. The row 31 January 2027 in the Examples also duplicates the COB date already run. This is a state sequence in the wrong business order. | ACS WITH PRECONDITION: AC2, AC3, AC4, AC6, AC7, AC8, AC9

## User story

```text
0001: As a loan operations administrator,
0002: I want loan accruals and accrual activity to be generated correctly for re-aged equal-amortization loans with advanced payment allocation,
0003: So that interest is recognized accurately over time and repayment schedules and transaction history remain correct after payments and COB processing.
0004: 
0005: Acceptance Criteria:
0006: - A fully customized declining-balance loan with equal installments, daily interest calculation, advanced payment allocation, and a 6-month term can be created, approved, and disbursed successfully.
0007: - After disbursement, the repayment schedule is generated with 6 periods and the expected principal, interest, due, and outstanding amounts for each installment.
0008: - The loan transaction tab initially shows only the disbursement transaction after loan disbursement.
0009: - When COB is run shortly after disbursement, daily accrual transactions are posted for each business day up to the COB date with the expected interest amounts.
0010: - When the first scheduled repayment is made on the due date, the repayment is allocated correctly between principal and interest according to the schedule.
0011: - After repayment, the repayment schedule reflects the installment as paid and updates the total paid and outstanding amounts correctly.
0012: - After repayment and COB processing, the transaction tab shows the repayment transaction without accruals and includes the corresponding accrual activity entry for the installment interest.
0013: - Daily accrual transactions continue to be generated correctly for the remaining days in January after the first repayment, with the expected daily interest amounts.
0014: - When COB is run on a later date, the transaction tab includes accrual activity entries for the relevant installment periods and the corresponding daily accrual transactions for the elapsed days.
0015: - The accrual activity entries reflect the total accrued interest for each completed installment period.
0016: - The transaction history distinguishes between repayment transactions, accrual transactions, and accrual activity transactions correctly.
0017: - Replayed/reverted flags remain false for the generated disbursement, repayment, accrual, and accrual activity transactions.
```

## Generated Gherkin C0

```text
0001: @Loans
0002: @LoanAccruals
0003: @ReagedEqualAmortizationAdvancedPaymentAllocationFeature
0004: Feature: Loan Accruals and Accrual Activity for Re-aged Equal-Amortization Loans with Advanced Payment Allocation
0005: 
0006:   @TestRailId:C76707
0007:   Scenario: Verify re-aged equal-amortization loan accrual generation, repayment allocation, and transaction history - UC1
0008:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0009:     And Admin creates a client with random data
0010:     And Admin creates and approves a re-aged equal-amortization loan with advanced payment allocation
0011:     And Admin disburses the loan
0012:     Then Check loan repayment schedule has the following values
0013:     Then Check loan transaction tab contains only disbursement transaction
0014:     When Admin runs COB on "02 January 2027"
0015:     Then Check daily accrual transactions are posted for each business day up to COB date with the following values
0016:     When Admin makes the first scheduled repayment on due date
0017:     Then Check repayment is allocated correctly between principal and interest
0018:     Then Check loan repayment schedule reflects installment as paid with updated total paid and outstanding amounts
0019:     When Admin runs COB on "31 January 2027"
0020:     Then Check loan transaction tab contains repayment transaction without accruals and accrual activity entry for installment interest
0021:     Then Check daily accrual transactions continue for remaining days in January with the following values
0022:     When Admin runs COB on "15 February 2027"
0023:     Then Check loan transaction history contains repayment transactions, accrual transactions, and accrual activity transactions correctly
0024:     Then Check replayed and reverted flags are false for disbursement, repayment, accrual, and accrual activity transactions
0025: 
0026:   @TestRailId:C76708
0027:   Scenario: Verify loan creation, approval, and disbursement for re-aged equal-amortization loan with advanced payment allocation - UC2
0028:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0029:     And Admin creates a client with random data
0030:     Then Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation successfully
0031:     Then Check loan repayment schedule has 6 periods with expected principal, interest, due, and outstanding amounts
0032: 
0033:   @TestRailId:C76709
0034:   Scenario: Verify loan transaction tab after disbursement contains only disbursement transaction - UC3
0035:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0036:     And Admin creates a client with random data
0037:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0038:     Then Check loan transaction tab initially shows only the disbursement transaction
0039: 
0040:   @TestRailId:C76710
0041:   Scenario Outline: Verify daily accrual transactions are generated correctly by COB after disbursement - UC4
0042:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0043:     And Admin creates a client with random data
0044:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0045:     When Admin runs COB on "<cob_date>"
0046:     Then Check daily accrual transactions are posted for each business day up to COB date with the following values
0047: 
0048:     Examples:
0049:       | cob_date        |
0050:       | 02 January 2027 |
0051:       | 03 January 2027 |
0052:       | 04 January 2027 |
0053: 
0054:   @TestRailId:C76711
0055:   Scenario: Verify first scheduled repayment allocation between principal and interest on due date - UC5
0056:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0057:     And Admin creates a client with random data
0058:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0059:     And Admin runs COB on "31 January 2027"
0060:     When Admin makes the first scheduled repayment on due date
0061:     Then Check repayment is allocated correctly between principal and interest according to the schedule
0062: 
0063:   @TestRailId:C76712
0064:   Scenario: Verify repayment schedule updates after first repayment - UC6
0065:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0066:     And Admin creates a client with random data
0067:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0068:     And Admin runs COB on "31 January 2027"
0069:     And Admin makes the first scheduled repayment on due date
0070:     Then Check loan repayment schedule reflects installment as paid and updates total paid and outstanding amounts correctly
0071: 
0072:   @TestRailId:C76713
0073:   Scenario: Verify transaction tab after repayment and COB includes repayment transaction and accrual activity entry - UC7
0074:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0075:     And Admin creates a client with random data
0076:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0077:     And Admin runs COB on "31 January 2027"
0078:     And Admin makes the first scheduled repayment on due date
0079:     And Admin runs COB on "31 January 2027"
0080:     Then Check loan transaction tab contains repayment transaction without accruals and accrual activity entry for installment interest
0081: 
0082:   @TestRailId:C76714
0083:   Scenario Outline: Verify daily accrual transactions continue for remaining days in January after first repayment - UC8
0084:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0085:     And Admin creates a client with random data
0086:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0087:     And Admin runs COB on "31 January 2027"
0088:     And Admin makes the first scheduled repayment on due date
0089:     When Admin runs COB on "<cob_date>"
0090:     Then Check daily accrual transactions continue for remaining days in January with the following values
0091: 
0092:     Examples:
0093:       | cob_date        |
0094:       | 28 January 2027 |
0095:       | 29 January 2027 |
0096:       | 30 January 2027 |
0097:       | 31 January 2027 |
0098: 
0099:   @TestRailId:C76715
0100:   Scenario: Verify later COB includes accrual activity entries for relevant installment periods and elapsed daily accruals - UC9
0101:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0102:     And Admin creates a client with random data
0103:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0104:     And Admin runs COB on "31 January 2027"
0105:     And Admin makes the first scheduled repayment on due date
0106:     When Admin runs COB on "15 February 2027"
0107:     Then Check loan transaction tab includes accrual activity entries for the relevant installment periods and corresponding daily accrual transactions for elapsed days
0108:     Then Check accrual activity entries reflect the total accrued interest for each completed installment period
0109: 
0110:   @TestRailId:C76716
0111:   Scenario: Verify transaction history distinguishes repayment, accrual, and accrual activity transactions correctly - UC10
0112:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0113:     And Admin creates a client with random data
0114:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0115:     And Admin runs COB on "31 January 2027"
0116:     And Admin makes the first scheduled repayment on due date
0117:     And Admin runs COB on "15 February 2027"
0118:     Then Check loan transaction history contains repayment transactions, accrual transactions, and accrual activity transactions correctly
0119: 
0120:   @TestRailId:C76717
0121:   Scenario: Verify replayed and reverted flags remain false for generated loan transactions - UC11
0122:     When Admin creates a fully customized declining-balance loan product with equal installments, daily interest calculation, advanced payment allocation, and 6 month term
0123:     And Admin creates a client with random data
0124:     And Admin creates, approves, and disburses a re-aged equal-amortization loan with advanced payment allocation
0125:     And Admin runs COB on "31 January 2027"
0126:     And Admin makes the first scheduled repayment on due date
0127:     And Admin runs COB on "15 February 2027"
0128:     Then Check replayed and reverted flags are false for disbursement, repayment, accrual, and accrual activity transactions
```

## Archived reference Gherkin

```text
0001: @LoanReAgingAccrualsEqualAmortizationFeature
0002: Feature: LoanReAgingAccrualsEqualAmortization
0003: 
0004:   @TestRailId:C4440 @AdvancedPaymentAllocation
0005:   Scenario: Verify Accrual Posting and Accrual Activity Posting on re-aged loan - interest bearing loan with equal amortization; outstanding payable interest - UC1
0006:     When Admin sets the business date to "01 January 2024"
0007:     When Admin creates a client with random data
0008:     When Admin creates a fully customized loan with the following data:
0009:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
0010:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_REFUND_INTEREST_RECALC_ACCRUAL_ACTIVITY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
0011:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
0012:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
0013:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0014:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
0015:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
0016:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0017:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0018:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0019:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0020:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0021:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
0022:     Then Loan Repayment schedule has the following data in Total row:
0023:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
0024:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
0025:     Then Loan Transactions tab has the following data:
0026:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0027:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0028: 
0029:     When Admin sets the business date to "03 January 2024"
0030:     When Admin runs inline COB job for Loan
0031:     Then Loan Transactions tab has the following data:
0032:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0033:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0034:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0035: 
0036:     When Admin sets the business date to "01 February 2024"
0037:     When Admin runs inline COB job for Loan
0038:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
0039:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0040:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0041:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0042:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0043:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0044:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0045:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0046:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0047:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
0048:     Then Loan Repayment schedule has the following data in Total row:
0049:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0050:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
0051:     Then Loan Transactions tab has the following data without accruals:
0052:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0053:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0054:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0055: 
0056:     Then Loan Transactions tab has the following new accrual data:
0057:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0058:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0059:       | 03 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0060:       | 04 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0061:       | 05 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0062:       | 06 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0063:       | 07 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0064:       | 08 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0065:       | 09 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0066:       | 10 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0067:       | 11 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0068:       | 12 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0069:       | 13 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0070:       | 14 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0071:       | 15 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0072:       | 16 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0073:       | 17 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0074:       | 18 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0075:       | 19 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0076:       | 20 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0077:       | 21 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0078:       | 22 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0079:       | 23 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0080:       | 24 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0081:       | 25 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0082:       | 26 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0083:       | 27 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0084:       | 28 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0085:       | 29 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0086:       | 30 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0087:       | 31 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0088: 
0089:     When Admin sets the business date to "15 March 2024"
0090:     When Admin runs inline COB job for Loan
0091:     Then Loan Transactions tab has the following data without accruals:
0092:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0093:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0094:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0095:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0096:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
0097: 
0098:     Then Loan Transactions tab has the following new accrual data:
0099:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0100:       | 01 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0101:       | 02 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0102:       | 03 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0103:       | 04 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0104:       | 05 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0105:       | 06 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0106:       | 07 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0107:       | 08 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0108:       | 09 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0109:       | 10 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0110:       | 11 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0111:       | 12 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0112:       | 13 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0113:       | 14 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0114:       | 15 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0115:       | 16 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0116:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0117:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0118:       | 19 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0119:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0120:       | 21 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0121:       | 22 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0122:       | 23 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0123:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0124:       | 25 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0125:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0126:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0127:       | 28 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0128:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0129:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0130:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0131:       | 03 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0132:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0133:       | 05 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0134:       | 06 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0135:       | 07 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0136:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0137:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0138:       | 10 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0139:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0140:       | 12 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0141:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0142:       | 14 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0143: 
0144:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
0145:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
0146:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
0147:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
0148:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0149:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0150:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0151:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0152:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0153:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0154:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0155:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0156:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0157:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0158:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
0159:     Then Loan Repayment schedule has the following data in Total row:
0160:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0161:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
0162:     Then Loan Transactions tab has the following data without accruals:
0163:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0164:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0165:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0166:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0167:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
0168:     Then Loan Transactions tab has the following new accrual data:
0169:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0170: 
0171:     When Admin sets the business date to "16 March 2024"
0172:     When Admin runs inline COB job for Loan
0173:     Then Loan Transactions tab has the following data without accruals:
0174:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0175:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0176:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0177:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0178:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
0179:     Then Loan Transactions tab has the following new accrual data:
0180:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0181:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
0182: 
0183:     When Admin sets the business date to "01 May 2024"
0184:     When Admin runs inline COB job for Loan
0185: 
0186:     When Admin sets the business date to "02 September 2024"
0187:     When Admin runs inline COB job for Loan
0188: 
0189:   @TestRailId:C4441 @AdvancedPaymentAllocation
0190:   Scenario: Verify Accrual Posting and Accrual Activity Posting on re-aged loan - interest bearing loan with equal amortization; outstanding full interest - UC2
0191:     When Admin sets the business date to "01 January 2024"
0192:     When Admin creates a client with random data
0193:     When Admin creates a fully customized loan with the following data:
0194:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
0195:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_REFUND_INTEREST_RECALC_ACCRUAL_ACTIVITY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
0196:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
0197:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
0198:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0199:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
0200:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
0201:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0202:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0203:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0204:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0205:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0206:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
0207:     Then Loan Repayment schedule has the following data in Total row:
0208:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
0209:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
0210:     Then Loan Transactions tab has the following data:
0211:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0212:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0213: 
0214:     When Admin sets the business date to "03 January 2024"
0215:     When Admin runs inline COB job for Loan
0216:     Then Loan Transactions tab has the following data:
0217:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0218:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0219:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0220: 
0221:     When Admin sets the business date to "01 February 2024"
0222:     When Admin runs inline COB job for Loan
0223:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
0224:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0225:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0226:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0227:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0228:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0229:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0230:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0231:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0232:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
0233:     Then Loan Repayment schedule has the following data in Total row:
0234:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0235:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
0236:     Then Loan Transactions tab has the following data without accruals:
0237:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0238:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0239:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0240: 
0241:     Then Loan Transactions tab has the following new accrual data:
0242:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0243:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0244:       | 03 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0245:       | 04 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0246:       | 05 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0247:       | 06 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0248:       | 07 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0249:       | 08 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0250:       | 09 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0251:       | 10 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0252:       | 11 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0253:       | 12 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0254:       | 13 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0255:       | 14 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0256:       | 15 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0257:       | 16 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0258:       | 17 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0259:       | 18 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0260:       | 19 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0261:       | 20 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0262:       | 21 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0263:       | 22 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0264:       | 23 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0265:       | 24 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0266:       | 25 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0267:       | 26 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0268:       | 27 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0269:       | 28 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0270:       | 29 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0271:       | 30 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0272:       | 31 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0273: 
0274:     When Admin sets the business date to "15 March 2024"
0275:     When Admin runs inline COB job for Loan
0276:     Then Loan Transactions tab has the following data without accruals:
0277:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0278:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0279:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0280:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0281:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
0282: 
0283:     Then Loan Transactions tab has the following new accrual data:
0284:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0285:       | 01 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0286:       | 02 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0287:       | 03 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0288:       | 04 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0289:       | 05 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0290:       | 06 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0291:       | 07 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0292:       | 08 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0293:       | 09 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0294:       | 10 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0295:       | 11 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0296:       | 12 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0297:       | 13 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0298:       | 14 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0299:       | 15 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0300:       | 16 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0301:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0302:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0303:       | 19 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0304:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0305:       | 21 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0306:       | 22 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0307:       | 23 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0308:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0309:       | 25 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0310:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0311:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0312:       | 28 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0313:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0314:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0315:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0316:       | 03 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0317:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0318:       | 05 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0319:       | 06 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0320:       | 07 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0321:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0322:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0323:       | 10 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0324:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0325:       | 12 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0326:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0327:       | 14 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0328:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
0329:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
0330:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
0331:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
0332:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0333:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0334:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0335:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0336:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0337:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0338:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0339:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0340:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0341:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0342:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0343:     Then Loan Repayment schedule has the following data in Total row:
0344:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0345:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
0346:     Then Loan Transactions tab has the following data without accruals:
0347:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0348:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0349:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0350:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0351:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
0352:     Then Loan Transactions tab has the following new accrual data:
0353:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0354: 
0355:     When Admin sets the business date to "16 March 2024"
0356:     When Admin runs inline COB job for Loan
0357:     Then Loan Transactions tab has the following new accrual data:
0358:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0359:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
0360: 
0361:   @TestRailId:C4442 @AdvancedPaymentAllocation
0362:   Scenario: Verify Accrual Posting and Accrual Activity Posting on re-aged loan - outstanding payable interest + outstanding principal, backdated re-age with dueDate change
0363:     When Admin sets the business date to "01 January 2024"
0364:     When Admin creates a client with random data
0365:     When Admin creates a fully customized loan with the following data:
0366:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
0367:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_REFUND_INTEREST_RECALC_ACCRUAL_ACTIVITY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
0368:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
0369:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
0370:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0371:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
0372:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
0373:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0374:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0375:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0376:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0377:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0378:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
0379:     Then Loan Repayment schedule has the following data in Total row:
0380:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
0381:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
0382:     Then Loan Transactions tab has the following data:
0383:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0384:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0385: 
0386:     When Admin sets the business date to "03 January 2024"
0387:     When Admin runs inline COB job for Loan
0388:     Then Loan Transactions tab has the following data:
0389:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0390:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0391:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0392: 
0393:     When Admin sets the business date to "01 February 2024"
0394:     When Admin runs inline COB job for Loan
0395:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
0396:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0397:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0398:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0399:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0400:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0401:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0402:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0403:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0404:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
0405:     Then Loan Repayment schedule has the following data in Total row:
0406:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0407:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
0408:     Then Loan Transactions tab has the following data without accruals:
0409:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0410:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0411:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0412: 
0413:     Then Loan Transactions tab has the following new accrual data:
0414:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0415:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0416:       | 03 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0417:       | 04 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0418:       | 05 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0419:       | 06 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0420:       | 07 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0421:       | 08 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0422:       | 09 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0423:       | 10 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0424:       | 11 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0425:       | 12 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0426:       | 13 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0427:       | 14 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0428:       | 15 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0429:       | 16 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0430:       | 17 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0431:       | 18 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0432:       | 19 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0433:       | 20 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0434:       | 21 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0435:       | 22 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0436:       | 23 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0437:       | 24 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0438:       | 25 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0439:       | 26 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0440:       | 27 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0441:       | 28 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0442:       | 29 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0443:       | 30 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0444:       | 31 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0445: 
0446:     When Admin sets the business date to "01 May 2024"
0447:     When Admin runs inline COB job for Loan
0448:     Then Loan Transactions tab has the following data without accruals:
0449:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0450:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0451:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0452:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0453:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
0454:       | 01 April 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
0455:     Then Loan Transactions tab has the following new accrual data:
0456:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0457:       | 01 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0458:       | 02 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0459:       | 03 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0460:       | 04 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0461:       | 05 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0462:       | 06 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0463:       | 07 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0464:       | 08 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0465:       | 09 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0466:       | 10 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0467:       | 11 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0468:       | 12 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0469:       | 13 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0470:       | 14 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0471:       | 15 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0472:       | 16 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0473:       | 17 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0474:       | 18 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0475:       | 19 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0476:       | 20 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0477:       | 21 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0478:       | 22 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0479:       | 23 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0480:       | 24 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0481:       | 25 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0482:       | 26 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0483:       | 27 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0484:       | 28 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0485:       | 29 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0486:       | 01 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0487:       | 02 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0488:       | 03 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0489:       | 04 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0490:       | 05 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0491:       | 06 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0492:       | 07 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0493:       | 08 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0494:       | 09 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0495:       | 10 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0496:       | 11 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0497:       | 12 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0498:       | 13 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0499:       | 14 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0500:       | 15 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0501:       | 16 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0502:       | 17 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0503:       | 18 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0504:       | 19 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0505:       | 20 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0506:       | 21 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0507:       | 22 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0508:       | 23 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0509:       | 24 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0510:       | 25 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0511:       | 26 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0512:       | 27 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0513:       | 28 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0514:       | 29 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0515:       | 30 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0516:       | 31 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0517:       | 01 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0518:       | 02 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0519:       | 03 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0520:       | 04 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0521:       | 05 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0522:       | 06 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0523:       | 07 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0524:       | 08 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0525:       | 09 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0526:       | 10 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0527:       | 11 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0528:       | 12 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0529:       | 13 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0530:       | 14 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0531:       | 15 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0532:       | 16 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0533:       | 17 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0534:       | 18 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0535:       | 19 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0536:       | 20 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0537:       | 21 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0538:       | 22 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0539:       | 23 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0540:       | 24 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0541:       | 25 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0542:       | 26 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0543:       | 27 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0544:       | 28 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0545:       | 29 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0546:       | 30 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0547: 
0548:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
0549:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
0550:       | 1               | MONTHS        | 15 March 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
0551:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
0552:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0553:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0554:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0555:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0556:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0557:       | 4  | 0    | 15 March 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0558:       | 5  | 31   | 15 April 2024     |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0559:       | 6  | 30   | 15 May 2024       |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0560:       | 7  | 31   | 15 June 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0561:       | 8  | 30   | 15 July 2024      |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
0562:       | 9  | 31   | 15 August 2024    |                  |  0.0            | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
0563:     Then Loan Repayment schedule has the following data in Total row:
0564:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0565:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
0566:     Then Loan Transactions tab has the following data without accruals:
0567:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0568:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0569:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0570:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0571:       | 15 March 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | true     |
0572:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
0573:       | 15 April 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false     |
0574:     Then Loan Transactions tab has the following new accrual data:
0575:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0576: 
0577:     When Admin sets the business date to "02 May 2024"
0578:     When Admin runs inline COB job for Loan
0579:     Then Loan Transactions tab has the following data without accruals:
0580:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0581:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0582:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0583:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0584:       | 15 March 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
0585:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
0586:       | 15 April 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false     |
0587:     Then Loan Transactions tab has the following new accrual data:
0588:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0589:       | 01 May 2024      | Accrual Adjustment | 1.15   | 0.0       | 1.15     | 0.0  | 0.0       | 0.0          | false    | false    |
0590: 
0591:     When Admin sets the business date to "02 September 2024"
0592:     When Admin runs inline COB job for Loan
0593:     Then Loan Transactions tab has the following data without accruals:
0594:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0595:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0596:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0597:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0598:       | 15 March 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
0599:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
0600:       | 15 April 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false     |
0601:       | 15 May 2024      | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
0602:       | 15 June 2024     | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
0603:       | 15 July 2024     | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
0604:       | 15 August 2024   | Accrual Activity | 0.11   | 0.0       | 0.11     | 0.0  | 0.0       | 0.0          | false    | false    |
0605:     Then Loan Transactions tab has the following new accrual data:
0606:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0607:       | 02 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0608:       | 04 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0609:       | 07 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0610:       | 09 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0611:       | 12 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0612:       | 14 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0613:       | 17 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0614:       | 19 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0615:       | 22 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0616:       | 25 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0617:       | 27 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0618:       | 30 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0619:       | 01 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0620:       | 04 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0621:       | 06 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0622:       | 09 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0623:       | 12 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0624:       | 14 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0625:       | 17 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0626:       | 19 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0627:       | 22 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0628:       | 24 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0629:       | 27 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0630:       | 29 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0631:       | 02 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0632:       | 04 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0633:       | 07 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0634:       | 09 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0635:       | 12 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0636:       | 14 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0637:       | 17 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0638:       | 20 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0639:       | 23 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0640:       | 25 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0641:       | 28 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0642:       | 31 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0643:       | 03 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0644:       | 06 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0645:       | 08 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0646:       | 11 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0647:       | 14 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0648: 
0649:   @TestRailId:C4443 @AdvancedPaymentAllocation
0650:   Scenario: Verify Accrual Posting and Accrual Activity Posting on re-aged loan - outstanding FULL interest + outstanding principal, backdated re-age with dueDate change
0651:     When Admin sets the business date to "01 January 2024"
0652:     When Admin creates a client with random data
0653:     When Admin creates a fully customized loan with the following data:
0654:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
0655:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_REFUND_INTEREST_RECALC_ACCRUAL_ACTIVITY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
0656:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
0657:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
0658:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0659:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
0660:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
0661:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0662:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0663:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0664:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0665:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0666:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
0667:     Then Loan Repayment schedule has the following data in Total row:
0668:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
0669:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
0670:     Then Loan Transactions tab has the following data:
0671:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0672:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0673: 
0674:     When Admin sets the business date to "03 January 2024"
0675:     When Admin runs inline COB job for Loan
0676:     Then Loan Transactions tab has the following data:
0677:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0678:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0679:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0680: 
0681:     When Admin sets the business date to "01 February 2024"
0682:     When Admin runs inline COB job for Loan
0683:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
0684:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0685:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0686:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0687:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0688:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0689:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0690:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0691:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
0692:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
0693:     Then Loan Repayment schedule has the following data in Total row:
0694:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0695:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
0696:     Then Loan Transactions tab has the following data without accruals:
0697:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0698:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0699:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0700: 
0701:     Then Loan Transactions tab has the following new accrual data:
0702:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0703:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0704:       | 03 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0705:       | 04 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0706:       | 05 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0707:       | 06 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0708:       | 07 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0709:       | 08 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0710:       | 09 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0711:       | 10 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0712:       | 11 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0713:       | 12 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0714:       | 13 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0715:       | 14 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0716:       | 15 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0717:       | 16 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0718:       | 17 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0719:       | 18 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0720:       | 19 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0721:       | 20 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0722:       | 21 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0723:       | 22 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0724:       | 23 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0725:       | 24 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0726:       | 25 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0727:       | 26 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0728:       | 27 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0729:       | 28 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0730:       | 29 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0731:       | 30 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0732:       | 31 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0733: 
0734:     When Admin sets the business date to "01 May 2024"
0735:     When Admin runs inline COB job for Loan
0736:     Then Loan Transactions tab has the following data without accruals:
0737:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0738:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0739:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0740:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0741:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
0742:       | 01 April 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
0743:     Then Loan Transactions tab has the following new accrual data:
0744:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0745:       | 01 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0746:       | 02 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0747:       | 03 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0748:       | 04 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0749:       | 05 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0750:       | 06 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0751:       | 07 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0752:       | 08 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0753:       | 09 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0754:       | 10 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0755:       | 11 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0756:       | 12 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0757:       | 13 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0758:       | 14 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0759:       | 15 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0760:       | 16 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0761:       | 17 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0762:       | 18 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0763:       | 19 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0764:       | 20 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0765:       | 21 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0766:       | 22 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0767:       | 23 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0768:       | 24 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0769:       | 25 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0770:       | 26 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0771:       | 27 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0772:       | 28 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0773:       | 29 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0774:       | 01 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0775:       | 02 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0776:       | 03 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0777:       | 04 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0778:       | 05 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0779:       | 06 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0780:       | 07 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0781:       | 08 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0782:       | 09 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0783:       | 10 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0784:       | 11 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0785:       | 12 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0786:       | 13 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0787:       | 14 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0788:       | 15 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0789:       | 16 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0790:       | 17 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0791:       | 18 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0792:       | 19 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0793:       | 20 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0794:       | 21 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0795:       | 22 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0796:       | 23 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0797:       | 24 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0798:       | 25 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0799:       | 26 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0800:       | 27 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0801:       | 28 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0802:       | 29 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0803:       | 30 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0804:       | 31 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0805:       | 01 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0806:       | 02 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0807:       | 03 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0808:       | 04 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0809:       | 05 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0810:       | 06 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0811:       | 07 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0812:       | 08 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0813:       | 09 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0814:       | 10 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0815:       | 11 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0816:       | 12 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0817:       | 13 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0818:       | 14 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0819:       | 15 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0820:       | 16 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0821:       | 17 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0822:       | 18 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0823:       | 19 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0824:       | 20 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0825:       | 21 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0826:       | 22 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0827:       | 23 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0828:       | 24 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0829:       | 25 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0830:       | 26 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0831:       | 27 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0832:       | 28 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0833:       | 29 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0834:       | 30 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
0835: 
0836:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
0837:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
0838:       | 1               | MONTHS        | 15 March 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
0839:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
0840:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
0841:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
0842:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
0843:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0844:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
0845:       | 4  | 0    | 15 March 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0846:       | 5  | 31   | 15 April 2024     |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0847:       | 6  | 30   | 15 May 2024       |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0848:       | 7  | 31   | 15 June 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0849:       | 8  | 30   | 15 July 2024      |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0850:       | 9  | 31   | 15 August 2024    |                  |  0.0            | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
0851:     Then Loan Repayment schedule has the following data in Total row:
0852:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
0853:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
0854:     Then Loan Transactions tab has the following data without accruals:
0855:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0856:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0857:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0858:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0859:       | 15 March 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | true     |
0860:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
0861:       | 15 April 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false     |
0862:     Then Loan Transactions tab has the following new accrual data:
0863:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0864: 
0865:     When Admin sets the business date to "02 May 2024"
0866:     When Admin runs inline COB job for Loan
0867:     Then Loan Transactions tab has the following data without accruals:
0868:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0869:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0870:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0871:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0872:       | 15 March 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
0873:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
0874:       | 15 April 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false     |
0875:     Then Loan Transactions tab has the following new accrual data:
0876:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0877:       | 01 May 2024      | Accrual Adjustment | 0.82   | 0.0       | 0.82     | 0.0  | 0.0       | 0.0          | false    | false    |
0878: 
0879:     When Admin sets the business date to "02 September 2024"
0880:     When Admin runs inline COB job for Loan
0881:     Then Loan Transactions tab has the following data without accruals:
0882:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0883:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
0884:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
0885:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
0886:       | 15 March 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
0887:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
0888:       | 15 April 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false     |
0889:       | 15 May 2024      | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
0890:       | 15 June 2024     | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
0891:       | 15 July 2024     | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
0892:       | 15 August 2024   | Accrual Activity | 0.26   | 0.0       | 0.26     | 0.0  | 0.0       | 0.0          | false    | false    |
0893:     Then Loan Transactions tab has the following new accrual data:
0894:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
0895:       | 02 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0896:       | 03 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0897:       | 04 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0898:       | 05 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0899:       | 06 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0900:       | 08 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0901:       | 09 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0902:       | 10 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0903:       | 11 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0904:       | 13 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0905:       | 14 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0906:       | 15 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0907:       | 16 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0908:       | 17 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0909:       | 19 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0910:       | 20 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0911:       | 21 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0912:       | 22 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0913:       | 24 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0914:       | 25 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0915:       | 26 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0916:       | 27 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0917:       | 29 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0918:       | 30 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0919:       | 31 May 2024      | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0920:       | 01 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0921:       | 02 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0922:       | 04 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0923:       | 05 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0924:       | 06 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0925:       | 07 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0926:       | 09 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0927:       | 10 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0928:       | 11 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0929:       | 12 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0930:       | 14 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0931:       | 15 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0932:       | 16 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0933:       | 17 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0934:       | 19 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0935:       | 20 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0936:       | 21 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0937:       | 22 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0938:       | 23 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0939:       | 24 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0940:       | 26 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0941:       | 27 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0942:       | 28 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0943:       | 29 June 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0944:       | 01 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0945:       | 02 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0946:       | 03 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0947:       | 04 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0948:       | 05 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0949:       | 06 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0950:       | 08 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0951:       | 09 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0952:       | 10 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0953:       | 11 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0954:       | 13 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0955:       | 14 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0956:       | 15 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0957:       | 16 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0958:       | 17 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0959:       | 18 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0960:       | 20 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0961:       | 21 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0962:       | 22 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0963:       | 23 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0964:       | 24 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0965:       | 26 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0966:       | 27 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0967:       | 28 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0968:       | 29 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0969:       | 30 July 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0970:       | 01 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0971:       | 02 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0972:       | 03 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0973:       | 04 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0974:       | 05 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0975:       | 07 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0976:       | 08 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0977:       | 09 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0978:       | 10 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0979:       | 11 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0980:       | 13 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0981:       | 14 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0982:       | 15 August 2024   | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
0983: 
0984:   @TestRailId:C4444 @AdvancedPaymentAllocation
0985:   Scenario: Verify Loan re-aging trn with repayment - interest bearing loan with equal amortization; outstanding payable interest + outstanding principal - UC1
0986:     When Admin sets the business date to "01 January 2024"
0987:     When Admin creates a client with random data
0988:     When Admin creates a fully customized loan with the following data:
0989:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
0990:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
0991:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
0992:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
0993:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
0994:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
0995:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
0996:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0997:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0998:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
0999:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1000:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1001:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
1002:     Then Loan Repayment schedule has the following data in Total row:
1003:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
1004:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
1005:     Then Loan Transactions tab has the following data:
1006:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1007:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1008: 
1009:     When Admin sets the business date to "01 February 2024"
1010:     When Admin runs inline COB job for Loan
1011:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
1012:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1013:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1014:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1015:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1016:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1017:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1018:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1019:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1020:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
1021:     Then Loan Repayment schedule has the following data in Total row:
1022:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1023:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
1024:     Then Loan Transactions tab has the following data:
1025:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1026:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1027:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
1028:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1029: 
1030:     When Admin sets the business date to "15 March 2024"
1031:     When Admin runs inline COB job for Loan
1032:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
1033:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
1034:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
1035:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1036:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1037:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1038:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1039:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1040:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1041:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1042:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1043:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1044:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1045:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1046:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
1047:     Then Loan Repayment schedule has the following data in Total row:
1048:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1049:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
1050: 
1051:     When Admin sets the business date to "16 March 2024"
1052:     When Admin runs inline COB job for Loan
1053:     Then Loan Transactions tab has the following data without accruals:
1054:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1055:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1056:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1057:       | 15 March 2024    | Re-age             | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
1058:     Then Loan Transactions tab has the following new accrual data:
1059:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1060:       | 31 January 2024  | Accrual            | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
1061:       | 01 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1062:       | 02 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1063:       | 03 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1064:       | 04 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1065:       | 05 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1066:       | 06 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1067:       | 07 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1068:       | 08 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1069:       | 09 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1070:       | 10 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1071:       | 11 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1072:       | 12 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1073:       | 13 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1074:       | 14 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1075:       | 15 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1076:       | 16 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1077:       | 17 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1078:       | 18 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1079:       | 19 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1080:       | 20 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1081:       | 21 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1082:       | 22 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1083:       | 23 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1084:       | 24 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1085:       | 25 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1086:       | 26 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1087:       | 27 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1088:       | 28 February 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1089:       | 29 February 2024 | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1090: 
1091:       | 01 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1092:       | 02 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1093:       | 03 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1094:       | 04 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1095:       | 05 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1096:       | 06 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1097:       | 07 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1098:       | 08 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1099:       | 09 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1100:       | 10 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1101:       | 11 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1102:       | 12 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1103:       | 13 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1104:       | 14 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1105:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
1106: 
1107:     When Admin sets the business date to "01 May 2024"
1108:     When Admin runs inline COB job for Loan
1109:     Then Loan Transactions tab has the following data without accruals:
1110:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1111:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1112:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1113:       | 15 March 2024    | Re-age             | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
1114:     Then Loan Transactions tab has the following new accrual data:
1115:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1116:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1117:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1118:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1119:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1120:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1121:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1122:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1123:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1124:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1125:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1126:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1127:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1128:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1129:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1130:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1131:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1132:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1133:       | 15 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1134:       | 18 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1135:       | 20 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1136:       | 23 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1137:       | 25 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1138:       | 28 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1139:       | 30 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1140: 
1141:     When Loan Pay-off is made on "01 May 2024"
1142:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
1143: 
1144:   @TestRailId:C4445 @AdvancedPaymentAllocation
1145:   Scenario: Verify Loan re-aging trn with MIR trn before re-age - interest bearing multidisb loan with equal amortization; outstanding payable interest - UC1.3
1146:     When Admin sets the business date to "01 January 2024"
1147:     When Admin creates a client with random data
1148:     When Admin creates a fully customized loan with the following data:
1149:       | LoanProduct                                                                                       | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
1150:       | LP2_ADV_PYMNT_INTEREST_DAILY_RECALC_EMI_360_30_MULTIDISB_APPROVED_OVER_APPLIED_CAPITALIZED_INCOME | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
1151:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
1152:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
1153:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1154:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
1155:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
1156:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1157:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1158:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1159:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1160:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1161:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
1162:     Then Loan Repayment schedule has the following data in Total row:
1163:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
1164:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
1165:     Then Loan Transactions tab has the following data:
1166:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1167:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1168: 
1169:     When Admin sets the business date to "01 February 2024"
1170:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
1171:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1172:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1173:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1174:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1175:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1176:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1177:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1178:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1179:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
1180:     Then Loan Repayment schedule has the following data in Total row:
1181:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1182:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
1183:     Then Loan Transactions tab has the following data:
1184:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1185:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1186:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1187: 
1188:     When Admin sets the business date to "01 March 2024"
1189:     When Admin runs inline COB job for Loan
1190:     When Admin makes "MERCHANT_ISSUED_REFUND" transaction with "AUTOPAY" payment type on "01 March 2024" with 34.02 EUR transaction amount
1191:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1192:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1193:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1194:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1195:       | 2  | 29   | 01 March 2024    | 01 March 2024    | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1196:       | 3  | 31   | 01 April 2024    |                  | 50.33           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 4.25  | 4.25       | 0.0  | 12.76      |
1197:       | 4  | 30   | 01 May 2024      |                  | 33.54           | 16.79         | 0.22     | 0.0  | 0.0       | 17.01 | 4.25  | 4.25       | 0.0  | 12.76       |
1198:       | 5  | 31   | 01 June 2024     |                  | 16.68           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 4.25  | 4.25       | 0.0  | 12.76       |
1199:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.68         | 0.07     | 0.0  | 0.0       | 16.75 | 4.26  | 4.26       | 0.0  | 12.49       |
1200:     Then Loan Repayment schedule has the following data in Total row:
1201:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1202:       | 100.0         | 1.8      | 0.0  | 0.0       | 101.8  | 51.03 | 17.01      | 0.0  | 50.77       |
1203:     Then Loan Transactions tab has the following data:
1204:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1205:       | 01 January 2024  | Disbursement           | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1206:       | 01 February 2024 | Repayment              | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1207:       | 29 February 2024 | Accrual                | 1.05   | 0.0       | 1.05     | 0.0  | 0.0       | 0.0          | false    | false    |
1208:       | 01 March 2024    | Merchant Issued Refund | 34.02  | 33.53     | 0.49     | 0.0  | 0.0       | 50.04        | false    | false    |
1209: 
1210:     When Admin sets the business date to "15 March 2024"
1211:     When Admin runs inline COB job for Loan
1212:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1213:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1214:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1215:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1216:       | 2  | 29   | 01 March 2024    | 01 March 2024    | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1217:       | 3  | 31   | 01 April 2024    |                  | 50.33           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 4.25  | 4.25       | 0.0  | 12.76      |
1218:       | 4  | 30   | 01 May 2024      |                  | 33.54           | 16.79         | 0.22     | 0.0  | 0.0       | 17.01 | 4.25  | 4.25       | 0.0  | 12.76       |
1219:       | 5  | 31   | 01 June 2024     |                  | 16.68           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 4.25  | 4.25       | 0.0  | 12.76       |
1220:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.68         | 0.07     | 0.0  | 0.0       | 16.75 | 4.26  | 4.26       | 0.0  | 12.49       |
1221:     Then Loan Repayment schedule has the following data in Total row:
1222:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1223:       | 100.0         | 1.8      | 0.0  | 0.0       | 101.8  | 51.03 | 17.01      | 0.0  | 50.77       |
1224:     Then Loan Transactions tab has the following data without accruals:
1225:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1226:       | 01 January 2024  | Disbursement           | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1227:       | 01 February 2024 | Repayment              | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1228:       | 01 March 2024    | Merchant Issued Refund | 34.02  | 33.53     | 0.49     | 0.0  | 0.0       | 50.04        | false    | false    |
1229: 
1230:     Then Loan Transactions tab has the following new accrual data:
1231:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1232:       | 29 February 2024 | Accrual            | 1.05   | 0.0       | 1.05     | 0.0  | 0.0       | 0.0          | false    | false    |
1233:       | 01 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1234:       | 02 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1235:       | 03 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1236:       | 04 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1237:       | 05 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1238:       | 06 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1239:       | 07 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1240:       | 08 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1241:       | 09 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1242:       | 11 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1243:       | 12 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1244:       | 13 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1245:       | 14 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1246: 
1247:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
1248:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
1249:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
1250:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1251:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1252:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1253:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1254:       | 2  | 29   | 01 March 2024     | 01 March 2024    | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1255:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 50.04           | 17.01         | 0.0      | 0.0  | 0.0       | 17.01 | 17.01 | 17.01      | 0.0  | 0.0          |
1256:       | 4  | 17   | 01 April 2024     |                  | 41.7            | 8.34          | 0.02     | 0.0  | 0.0       | 8.36  | 0.0   | 0.0        | 0.0  | 8.36        |
1257:       | 5  | 30   | 01 May 2024       |                  | 33.36           | 8.34          | 0.02     | 0.0  | 0.0       | 8.36  | 0.0   | 0.0        | 0.0  | 8.36        |
1258:       | 6  | 31   | 01 June 2024      |                  | 25.02           | 8.34          | 0.02     | 0.0  | 0.0       | 8.36  | 0.0   | 0.0        | 0.0  | 8.36        |
1259:       | 7  | 30   | 01 July 2024      |                  | 16.68           | 8.34          | 0.02     | 0.0  | 0.0       | 8.36  | 0.0   | 0.0        | 0.0  | 8.36        |
1260:       | 8  | 31   | 01 August 2024    |                  |  8.34           | 8.34          | 0.02     | 0.0  | 0.0       | 8.36  | 0.0   | 0.0        | 0.0  | 8.36        |
1261:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 8.34          | 0.03     | 0.0  | 0.0       | 8.37  | 0.0   | 0.0        | 0.0  | 8.37        |
1262:     Then Loan Repayment schedule has the following data in Total row:
1263:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1264:       | 100.0         | 1.2      | 0.0  | 0.0       | 101.2  | 51.03 | 17.01      | 0.0  | 50.17       |
1265:     Then Loan Transactions tab has the following data without accruals:
1266:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1267:       | 01 January 2024  | Disbursement           | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1268:       | 01 February 2024 | Repayment              | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1269:       | 01 March 2024    | Merchant Issued Refund | 34.02  | 33.53     | 0.49     | 0.0  | 0.0       | 50.04        | false    | false    |
1270:       | 15 March 2024    | Re-age                 | 50.17  | 50.04     | 0.13     | 0.0  | 0.0       | 0.0          | false    | false    |
1271:     Then Loan Transactions tab has no new accrual data
1272: 
1273:     When Admin sets the business date to "01 May 2024"
1274:     When Admin runs inline COB job for Loan
1275:     Then Loan Transactions tab has the following data without accruals:
1276:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1277:       | 01 January 2024  | Disbursement           | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1278:       | 01 February 2024 | Repayment              | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1279:       | 01 March 2024    | Merchant Issued Refund | 34.02  | 33.53     | 0.49     | 0.0  | 0.0       | 50.04        | false    | false    |
1280:       | 15 March 2024    | Re-age                 | 50.17  | 50.04     | 0.13     | 0.0  | 0.0       | 0.0          | false    | false    |
1281:     Then Loan Transactions tab has the following new accrual data:
1282:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1283:       | 15 March 2024    | Accrual Adjustment | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
1284:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1285:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1286:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1287:       | 24 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1288: 
1289:     When Loan Pay-off is made on "01 May 2024"
1290:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
1291: 
1292:   @TestRailId:C4446 @AdvancedPaymentAllocation
1293:   Scenario: Verify Loan re-aging trn with repayment and charge - interest bearing loan with equal amortization; outstanding payable interest - UC2
1294:     When Admin sets the business date to "01 January 2024"
1295:     When Admin creates a client with random data
1296:     When Admin creates a fully customized loan with the following data:
1297:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
1298:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
1299:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
1300:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
1301:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1302:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
1303:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
1304:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1305:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1306:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1307:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1308:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1309:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
1310:     Then Loan Repayment schedule has the following data in Total row:
1311:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
1312:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
1313:     Then Loan Transactions tab has the following data:
1314:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1315:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1316: 
1317:     When Admin sets the business date to "01 February 2024"
1318:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
1319:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1320:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1321:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1322:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1323:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1324:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1325:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1326:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1327:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
1328:     Then Loan Repayment schedule has the following data in Total row:
1329:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1330:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
1331:     Then Loan Transactions tab has the following data:
1332:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1333:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1334:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1335: 
1336:     When Admin sets the business date to "15 February 2024"
1337:     When Admin runs inline COB job for Loan
1338:     And Admin adds "LOAN_SNOOZE_FEE" due date charge with "15 February 2024" due date and 10 EUR transaction amount
1339:     Then Loan Charges tab has the following data:
1340:       | Name       | isPenalty | Payment due at     | Due as of        | Calculation type | Due  | Paid | Waived | Outstanding |
1341:       | Snooze fee | false     | Specified due date | 15 February 2024 | Flat             | 10.0 | 0.0  | 0.0    | 10.0        |
1342: 
1343:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1344:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1345:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1346:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1347:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 10.0 | 0.0       | 27.01 | 0.0   | 0.0        | 0.0  | 27.01       |
1348:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1349:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1350:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1351:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
1352:     Then Loan Repayment schedule has the following data in Total row:
1353:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1354:       | 100.0         | 2.05     | 10.0 | 0.0       | 112.05 | 17.01 | 0.0        | 0.0  | 95.04       |
1355:     Then Loan Transactions tab has the following data:
1356:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1357:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1358:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1359:       | 14 February 2024 | Accrual          | 0.8    | 0.0       | 0.8      | 0.0  | 0.0       | 0.0          | false    | false    |
1360: 
1361:     When Admin sets the business date to "15 March 2024"
1362:     When Admin runs inline COB job for Loan
1363:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
1364:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
1365:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
1366:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1367:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1368:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1369:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1370:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1371:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1372:       | 4  | 17   | 01 April 2024     |                  | 69.65           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1373:       | 5  | 30   | 01 May 2024       |                  | 55.73           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1374:       | 6  | 31   | 01 June 2024      |                  | 41.81           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1375:       | 7  | 30   | 01 July 2024      |                  | 27.89           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1376:       | 8  | 31   | 01 August 2024    |                  | 13.97           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1377:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.97         | 0.11     | 1.65 | 0.0       | 15.73 | 0.0   | 0.0        | 0.0  | 15.73       |
1378:     Then Loan Repayment schedule has the following data in Total row:
1379:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1380:       | 100.0         | 1.29     | 10.0 | 0.0       | 111.29 | 17.01 | 0.0        | 0.0  | 94.28       |
1381:     Then Loan Transactions tab has the following data without accruals:
1382:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1383:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1384:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1385:       | 15 March 2024    | Re-age           | 94.28  | 83.57     | 0.71     | 10.0 | 0.0       | 0.0          | false    | false    |
1386:     Then Loan Transactions tab has the following new accrual data:
1387:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1388:       | 14 February 2024 | Accrual          | 0.8    | 0.0       | 0.8      | 0.0  | 0.0       | 0.0          | false    | false    |
1389:       | 15 February 2024 | Accrual          | 10.02  | 0.0       | 0.02     | 10.0 | 0.0       | 0.0          | false    | false    |
1390:       | 16 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1391:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1392:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1393:       | 19 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1394:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1395:       | 21 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1396:       | 22 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1397:       | 23 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1398:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1399:       | 25 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1400:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1401:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1402:       | 28 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1403:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1404: 
1405:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1406:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1407:       | 03 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1408:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1409:       | 05 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1410:       | 06 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1411:       | 07 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1412:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1413:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1414:       | 10 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1415:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1416:       | 12 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1417:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1418:       | 14 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1419: 
1420:     When Admin sets the business date to "15 April 2024"
1421:     When Admin runs inline COB job for Loan
1422:     Then Loan Transactions tab has the following data without accruals:
1423:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1424:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1425:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1426:       | 15 March 2024    | Re-age           | 94.28  | 83.57     | 0.71     | 10.0 | 0.0       | 0.0          | false    | false    |
1427:     Then Loan Transactions tab has the following new accrual data:
1428:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1429:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
1430:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1431:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1432:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1433:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1434:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1435:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1436:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1437:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1438:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1439:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1440:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1441:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1442:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1443:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1444:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1445:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1446:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1447:     When Loan Pay-off is made on "15 April 2024"
1448:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
1449: 
1450:   @TestRailId:C4447 @AdvancedPaymentAllocation
1451:   Scenario: Verify Loan re-aging transaction with repayment and chargeback - interest bearing loan with equal amortization; outstanding payable interest - UC3
1452:     When Admin sets the business date to "01 January 2024"
1453:     When Admin creates a client with random data
1454:     When Admin creates a fully customized loan with the following data:
1455:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
1456:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
1457:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
1458:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
1459:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1460:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
1461:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
1462:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1463:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1464:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1465:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1466:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1467:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
1468:     Then Loan Repayment schedule has the following data in Total row:
1469:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
1470:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
1471:     Then Loan Transactions tab has the following data:
1472:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1473:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1474: 
1475:     When Admin sets the business date to "01 February 2024"
1476:     When Admin runs inline COB job for Loan
1477:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
1478:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
1479:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1480:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1481:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1482:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1483:       | 2  | 29   | 01 March 2024    |                  | 67.15           | 33.43         | 0.59     | 0.0  | 0.0       | 34.02 | 0.0   | 0.0        | 0.0  | 34.02       |
1484:       | 3  | 31   | 01 April 2024    |                  | 50.53           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1485:       | 4  | 30   | 01 May 2024      |                  | 33.81           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1486:       | 5  | 31   | 01 June 2024     |                  | 17.0            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1487:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 17.0          | 0.1      | 0.0  | 0.0       | 17.1  | 0.0   | 0.0        | 0.0  | 17.1        |
1488:     Then Loan Repayment schedule has the following data in Total row:
1489:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1490:       | 117.01        | 2.15     | 0.0  | 0.0       | 119.16 | 17.01 | 0.0        | 0.0  | 102.15      |
1491:     Then Loan Transactions tab has the following data:
1492:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1493:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1494:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
1495:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1496:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 100.58       | false    | false    |
1497: 
1498:     When Admin sets the business date to "15 March 2024"
1499:     When Admin runs inline COB job for Loan
1500:     Then Loan Transactions tab has the following data without accruals:
1501:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1502:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1503:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1504:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 100.58       | false    | false    |
1505:     Then Loan Transactions tab has the following new accrual data:
1506:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1507:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
1508:       | 01 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1509:       | 02 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1510:       | 03 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1511:       | 04 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1512:       | 05 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1513:       | 06 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1514:       | 07 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1515:       | 08 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1516:       | 09 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1517:       | 10 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1518:       | 11 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1519:       | 12 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1520:       | 13 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1521:       | 14 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1522:       | 15 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1523:       | 16 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1524:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1525:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1526:       | 19 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1527:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1528:       | 21 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1529:       | 22 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1530:       | 23 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
1531:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1532:       | 25 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1533:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1534:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1535:       | 28 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1536:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1537: 
1538:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1539:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1540:       | 03 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1541:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1542:       | 05 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1543:       | 06 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1544:       | 07 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1545:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1546:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1547:       | 10 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1548:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1549:       | 12 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1550:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1551:       | 14 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1552: 
1553:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
1554:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
1555:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
1556:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1557:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1558:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1559:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1560:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 100.58          | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1561:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 100.58          | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1562:       | 4  | 17   | 01 April 2024     |                  | 83.82           | 16.76         | 0.14     | 0.0  | 0.0       | 16.9  | 0.0   | 0.0        | 0.0  | 16.9        |
1563:       | 5  | 30   | 01 May 2024       |                  | 67.06           | 16.76         | 0.14     | 0.0  | 0.0       | 16.9  | 0.0   | 0.0        | 0.0  | 16.9        |
1564:       | 6  | 31   | 01 June 2024      |                  | 50.3            | 16.76         | 0.14     | 0.0  | 0.0       | 16.9  | 0.0   | 0.0        | 0.0  | 16.9        |
1565:       | 7  | 30   | 01 July 2024      |                  | 33.54           | 16.76         | 0.14     | 0.0  | 0.0       | 16.9  | 0.0   | 0.0        | 0.0  | 16.9        |
1566:       | 8  | 31   | 01 August 2024    |                  | 16.78           | 16.76         | 0.14     | 0.0  | 0.0       | 16.9  | 0.0   | 0.0        | 0.0  | 16.9        |
1567:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 16.78         | 0.15     | 0.0  | 0.0       | 16.93 | 0.0   | 0.0        | 0.0  | 16.93       |
1568:     Then Loan Repayment schedule has the following data in Total row:
1569:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1570:       | 117.01        | 1.43     | 0.0  | 0.0       | 118.44 | 17.01 | 0.0        | 0.0  | 101.43      |
1571:     Then Loan Transactions tab has the following data without accruals:
1572:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1573:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1574:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1575:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 100.58       | false    | false    |
1576:       | 15 March 2024    | Re-age           | 101.43 | 100.58    | 0.85     | 0.0  | 0.0       | 0.0          | false    | false    |
1577:     Then Loan Transactions tab has no new accrual data
1578: 
1579:     When Admin sets the business date to "15 April 2024"
1580:     When Admin runs inline COB job for Loan
1581:     Then Loan Transactions tab has the following data without accruals:
1582:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1583:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1584:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1585:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 100.58       | false    | false    |
1586:       | 15 March 2024    | Re-age           | 101.43 | 100.58    | 0.85     | 0.0  | 0.0       | 0.0          | false    | false    |
1587:     Then Loan Transactions tab has the following new accrual data:
1588:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1589:       | 15 March 2024    | Accrual Adjustment | 0.84   | 0.0       | 0.84     | 0.0  | 0.0       | 0.0          | false    | false    |
1590:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1591:       | 17 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1592:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1593:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1594:       | 21 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1595:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1596:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1597:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1598:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1599:       | 27 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1600:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1601:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1602:       | 31 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1603:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1604:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1605:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1606:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1607:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1608:       | 11 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1609:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1610: 
1611:     When Loan Pay-off is made on "15 April 2024"
1612:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
1613: 
1614:   @TestRailId:C4448 @AdvancedPaymentAllocation
1615:   Scenario: Verify Loan re-aging trn with repayment and partial chargeback with payment alloc - interest bearing loan with equal amortization; outstanding payable interest - UC3.2
1616:     When Admin sets the business date to "01 January 2024"
1617:     When Admin creates a client with random data
1618:     When Admin creates a fully customized loan with the following data:
1619:       | LoanProduct                                                                                       | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
1620:       | LP2_ADV_PYMNT_INTEREST_DAILY_INTEREST_RECALC_EMI_360_30_CHARGEBACK_INTEREST_PENALTY_FEE_PRINCIPAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
1621:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
1622:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
1623:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1624:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
1625:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
1626:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1627:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1628:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1629:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1630:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1631:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
1632:     Then Loan Repayment schedule has the following data in Total row:
1633:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
1634:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
1635:     Then Loan Transactions tab has the following data:
1636:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1637:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1638: 
1639:     When Admin sets the business date to "01 February 2024"
1640:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
1641:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 10 EUR transaction amount
1642:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1643:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1644:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1645:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1646:       | 2  | 29   | 01 March 2024    |                  | 67.1            | 25.89         | 1.12     | 0.0  | 0.0       | 27.01 | 0.0   | 0.0        | 0.0  | 27.01       |
1647:       | 3  | 31   | 01 April 2024    |                  | 50.48           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1648:       | 4  | 30   | 01 May 2024      |                  | 33.76           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1649:       | 5  | 31   | 01 June 2024     |                  | 16.95           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1650:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.95         | 0.1      | 0.0  | 0.0       | 17.05 | 0.0   | 0.0        | 0.0  | 17.05       |
1651:     Then Loan Repayment schedule has the following data in Total row:
1652:       | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1653:       | 109.42        | 2.68     | 0.0  | 0.0       | 112.1 | 17.01 | 0.0        | 0.0  | 95.09       |
1654:     Then Loan Transactions tab has the following data:
1655:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1656:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1657:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1658:       | 01 February 2024 | Chargeback       | 10.0   | 9.42      | 0.58     | 0.0  | 0.0       | 92.99        | false    | false    |
1659: 
1660:     When Admin sets the business date to "15 March 2024"
1661:     When Admin runs inline COB job for Loan
1662:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1663:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1664:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1665:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1666:       | 2  | 29   | 01 March 2024    |                  | 67.1            | 25.89         | 1.12     | 0.0  | 0.0       | 27.01 | 0.0   | 0.0        | 0.0  | 27.01       |
1667:       | 3  | 31   | 01 April 2024    |                  | 50.55           | 16.55         | 0.46     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1668:       | 4  | 30   | 01 May 2024      |                  | 33.83           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1669:       | 5  | 31   | 01 June 2024     |                  | 17.02           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1670:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 17.02         | 0.1      | 0.0  | 0.0       | 17.12 | 0.0   | 0.0        | 0.0  | 17.12       |
1671:     Then Loan Repayment schedule has the following data in Total row:
1672:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1673:       | 109.42        | 2.75     | 0.0  | 0.0       | 112.17 | 17.01 | 0.0        | 0.0  | 95.16       |
1674:     Then Loan Transactions tab has the following data:
1675:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1676:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1677:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1678:       | 01 February 2024 | Chargeback       | 10.0   | 9.42      | 0.58     | 0.0  | 0.0       | 92.99        | false    | false    |
1679:       | 14 March 2024    | Accrual          | 1.35   | 0.0       | 1.35     | 0.0  | 0.0       | 0.0          | false    | false    |
1680: 
1681:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
1682:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
1683:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
1684:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1685:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1686:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1687:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1688:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 92.99           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1689:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 92.99           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1690:       | 4  | 17   | 01 April 2024     |                  | 77.5            | 15.49         | 0.23     | 0.0  | 0.0       | 15.72 | 0.0   | 0.0        | 0.0  | 15.72       |
1691:       | 5  | 30   | 01 May 2024       |                  | 62.01           | 15.49         | 0.23     | 0.0  | 0.0       | 15.72 | 0.0   | 0.0        | 0.0  | 15.72       |
1692:       | 6  | 31   | 01 June 2024      |                  | 46.52           | 15.49         | 0.23     | 0.0  | 0.0       | 15.72 | 0.0   | 0.0        | 0.0  | 15.72       |
1693:       | 7  | 30   | 01 July 2024      |                  | 31.03           | 15.49         | 0.23     | 0.0  | 0.0       | 15.72 | 0.0   | 0.0        | 0.0  | 15.72       |
1694:       | 8  | 31   | 01 August 2024    |                  | 15.54           | 15.49         | 0.23     | 0.0  | 0.0       | 15.72 | 0.0   | 0.0        | 0.0  | 15.72       |
1695:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 15.54         | 0.21     | 0.0  | 0.0       | 15.75 | 0.0   | 0.0        | 0.0  | 15.75       |
1696:     Then Loan Repayment schedule has the following data in Total row:
1697:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1698:       | 109.42        | 1.94     | 0.0  | 0.0       | 111.36 | 17.01 | 0.0        | 0.0  | 94.35       |
1699:     Then Loan Transactions tab has the following data:
1700:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1701:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1702:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1703:       | 01 February 2024 | Chargeback       | 10.0   | 9.42      | 0.58     | 0.0  | 0.0       | 92.99        | false    | false    |
1704:       | 14 March 2024    | Accrual          | 1.35   | 0.0       | 1.35     | 0.0  | 0.0       | 0.0          | false    | false    |
1705:       | 15 March 2024    | Re-age           | 94.35  | 92.99     | 1.36     | 0.0  | 0.0       | 0.0          | false    | false    |
1706: 
1707:     When Admin sets the business date to "15 April 2024"
1708:     When Admin runs inline COB job for Loan
1709:     Then Loan Transactions tab has the following data without accruals:
1710:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1711:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1712:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1713:       | 01 February 2024 | Chargeback       | 10.0   | 9.42      | 0.58     | 0.0  | 0.0       | 92.99        | false    | false    |
1714:       | 15 March 2024    | Re-age           | 94.35  | 92.99     | 1.36     | 0.0  | 0.0       | 0.0          | false    | false    |
1715:     Then Loan Transactions tab has the following new accrual data:
1716:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1717:       | 14 March 2024    | Accrual            | 1.35   | 0.0       | 1.35     | 0.0  | 0.0       | 0.0          | false    | false    |
1718:       | 15 March 2024    | Accrual Adjustment | 0.77   | 0.0       | 0.77     | 0.0  | 0.0       | 0.0          | false    | false    |
1719:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1720:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1721:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1722:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1723:       | 20 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1724:       | 21 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1725:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1726:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1727:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1728:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1729:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1730:       | 27 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1731:       | 28 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1732:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1733:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1734:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
1735:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1736:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1737:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1738:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1739:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1740:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1741:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1742:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1743:       | 11 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1744:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1745:       | 14 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1746: 
1747:     When Loan Pay-off is made on "15 April 2024"
1748:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
1749: 
1750:   @TestRailId:C4449 @AdvancedPaymentAllocation
1751:   Scenario: Verify Loan re-aging transaction with repayment and charge - interest bearing loan with equal amortization; outstanding payable interest - UC4
1752:     When Admin sets the business date to "01 January 2024"
1753:     When Admin creates a client with random data
1754:     When Admin creates a fully customized loan with the following data:
1755:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
1756:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
1757:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
1758:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
1759:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1760:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
1761:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
1762:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1763:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1764:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1765:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1766:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1767:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
1768:     Then Loan Repayment schedule has the following data in Total row:
1769:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
1770:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
1771:     Then Loan Transactions tab has the following data:
1772:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1773:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1774: 
1775:     When Admin sets the business date to "01 February 2024"
1776:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
1777:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1778:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1779:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1780:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1781:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1782:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1783:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1784:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1785:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
1786:     Then Loan Repayment schedule has the following data in Total row:
1787:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1788:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
1789:     Then Loan Transactions tab has the following data:
1790:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1791:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1792:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1793: 
1794:     And Admin adds "LOAN_SNOOZE_FEE" due date charge with "15 July 2024" due date and 10 EUR transaction amount
1795:     Then Loan Charges tab has the following data:
1796:       | Name       | isPenalty | Payment due at     | Due as of    | Calculation type | Due  | Paid | Waived | Outstanding |
1797:       | Snooze fee | false     | Specified due date | 15 July 2024 | Flat             | 10.0 | 0.0  | 0.0    | 10.0        |
1798: 
1799:     When Admin sets the business date to "15 March 2024"
1800:     When Admin runs inline COB job for Loan
1801:     Then Loan Repayment schedule has 7 periods, with the following data for periods:
1802:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1803:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1804:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1805:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1806:       | 3  | 31   | 01 April 2024    |                  | 50.47           | 16.58         | 0.43     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1807:       | 4  | 30   | 01 May 2024      |                  | 33.75           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1808:       | 5  | 31   | 01 June 2024     |                  | 16.94           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1809:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.94         | 0.1      | 0.0  | 0.0       | 17.04 | 0.0   | 0.0        | 0.0  | 17.04       |
1810:       | 7  | 14   | 15 July 2024     |                  | 0.0             | 0.0           | 0.0      | 10.0 | 0.0       | 10.0  | 0.0   | 0.0        | 0.0  | 10.0        |
1811:     Then Loan Repayment schedule has the following data in Total row:
1812:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1813:       | 100.0         | 2.09     | 10.0 | 0.0       | 112.09 | 17.01 | 0.0        | 0.0  | 95.08       |
1814:     Then Loan Transactions tab has the following data:
1815:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1816:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1817:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1818:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
1819: 
1820:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
1821:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
1822:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
1823:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1824:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1825:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1826:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1827:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1828:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1829:       | 4  | 17   | 01 April 2024     |                  | 69.65           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1830:       | 5  | 30   | 01 May 2024       |                  | 55.73           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1831:       | 6  | 31   | 01 June 2024      |                  | 41.81           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1832:       | 7  | 30   | 01 July 2024      |                  | 27.89           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1833:       | 8  | 31   | 01 August 2024    |                  | 13.97           | 13.92         | 0.12     | 1.67 | 0.0       | 15.71 | 0.0   | 0.0        | 0.0  | 15.71       |
1834:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.97         | 0.11     | 1.65 | 0.0       | 15.73 | 0.0   | 0.0        | 0.0  | 15.73       |
1835:     Then Loan Repayment schedule has the following data in Total row:
1836:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1837:       | 100.0         | 1.29     | 10.0 | 0.0       | 111.29 | 17.01 | 0.0        | 0.0  | 94.28       |
1838:     Then Loan Transactions tab has the following data:
1839:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1840:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1841:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1842:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
1843:       | 15 March 2024    | Re-age           | 94.28  | 83.57     | 0.71     | 10.0 | 0.0       | 0.0          | false    | false    |
1844: 
1845:     When Admin sets the business date to "17 July 2024"
1846:     When Admin runs inline COB job for Loan
1847:     Then Loan Transactions tab has the following data without accruals:
1848:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1849:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1850:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1851:       | 15 March 2024    | Re-age           | 94.28  | 83.57     | 0.71     | 10.0 | 0.0       | 0.0          | false    | false    |
1852:     Then Loan Transactions tab has the following new accrual data:
1853:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1854:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
1855:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
1856:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1857:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1858:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1859:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1860:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1861:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1862:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1863:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1864:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1865:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1866:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1867:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1868:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1869:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1870:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1871:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1872:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1873:       | 15 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1874:       | 18 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1875:       | 20 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1876:       | 23 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1877:       | 25 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1878:       | 28 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1879:       | 30 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1880:       | 03 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1881:       | 05 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1882:       | 08 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1883:       | 11 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1884:       | 13 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1885:       | 16 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1886:       | 18 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1887:       | 21 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1888:       | 13 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1889:       | 26 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1890:       | 29 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1891:       | 31 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1892:       | 03 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1893:       | 05 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1894:       | 08 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1895:       | 10 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1896:       | 13 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1897:       | 15 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1898:       | 18 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1899:       | 20 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1900:       | 23 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1901:       | 25 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1902:       | 28 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1903:       | 30 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1904:       | 03 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1905:       | 05 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1906:       | 08 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1907:       | 11 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1908:       | 13 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1909:       | 15 July 2024     | Accrual            | 10.0   | 0.0       | 0.0      | 10.0 | 0.0       | 0.0          | false    | false    |
1910:       | 16 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
1911: 
1912:     When Loan Pay-off is made on "17 July 2024"
1913:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
1914: 
1915:   @TestRailId:C4450 @AdvancedPaymentAllocation
1916:   Scenario: Verify Loan re-aging transaction with chargeback after re-age - interest bearing loan with equal amortization; outstanding payable interest - UC6
1917:     When Admin sets the business date to "01 January 2024"
1918:     When Admin creates a client with random data
1919:     When Admin creates a fully customized loan with the following data:
1920:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
1921:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
1922:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
1923:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
1924:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1925:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
1926:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
1927:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1928:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1929:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1930:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1931:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
1932:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
1933:     Then Loan Repayment schedule has the following data in Total row:
1934:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
1935:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
1936:     Then Loan Transactions tab has the following data:
1937:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1938:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1939: 
1940:     When Admin sets the business date to "01 February 2024"
1941:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
1942:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
1943:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1944:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1945:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1946:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1947:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1948:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1949:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
1950:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
1951:     Then Loan Repayment schedule has the following data in Total row:
1952:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1953:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
1954:     Then Loan Transactions tab has the following data:
1955:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1956:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1957:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1958: 
1959:     When Admin sets the business date to "15 March 2024"
1960:     When Admin runs inline COB job for Loan
1961:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
1962:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
1963:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
1964:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1965:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1966:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1967:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1968:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1969:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1970:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1971:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1972:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1973:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1974:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1975:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
1976:     Then Loan Repayment schedule has the following data in Total row:
1977:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
1978:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
1979:     Then Loan Transactions tab has the following data:
1980:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
1981:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
1982:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
1983:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
1984:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
1985: 
1986:     When Admin sets the business date to "01 April 2024"
1987:     When Admin runs inline COB job for Loan
1988:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
1989:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
1990:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
1991:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
1992:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
1993:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1994:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
1995:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1996:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 30.94         | 0.12     | 0.0  | 0.0       | 31.06 | 0.0   | 0.0        | 0.0  | 31.06       |
1997:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1998:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
1999:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
2000:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
2001:     Then Loan Repayment schedule has the following data in Total row:
2002:       | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2003:       | 117.01        | 1.29     | 0.0  | 0.0       | 118.3 | 17.01 | 0.0        | 0.0  | 101.29      |
2004:     Then Loan Transactions tab has the following data without accruals:
2005:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2006:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2007:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2008:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
2009:       | 01 April 2024    | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 100.58       | false    | false    |
2010:     Then Loan Transactions tab has the following new accrual data:
2011:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2012:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
2013:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
2014:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2015:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2016:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2017:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2018:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2019:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2020:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2021:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2022:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2023:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2024:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2025: 
2026:     When Admin sets the business date to "02 April 2024"
2027:     When Admin runs inline COB job for Loan
2028:     Then Loan Transactions tab has the following data without accruals:
2029:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2030:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2031:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2032:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
2033:       | 01 April 2024    | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 100.58       | false    | false    |
2034:     Then Loan Transactions tab has the following new accrual data:
2035:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2036:       | 01 April 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2037: 
2038:   @TestRailId:C4451 @AdvancedPaymentAllocation
2039:   Scenario: Verify Loan re-aging transaction with MIR after re-age - interest bearing loan with equal amortization; outstanding payable interest - UC6.3
2040:     When Admin sets the business date to "01 January 2024"
2041:     When Admin creates a client with random data
2042:     When Admin creates a fully customized loan with the following data:
2043:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
2044:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
2045:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
2046:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
2047:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2048:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
2049:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
2050:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2051:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2052:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2053:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2054:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2055:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
2056:     Then Loan Repayment schedule has the following data in Total row:
2057:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
2058:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
2059:     Then Loan Transactions tab has the following data:
2060:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2061:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2062: 
2063:     When Admin sets the business date to "01 February 2024"
2064:     When Admin runs inline COB job for Loan
2065:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
2066:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2067:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2068:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2069:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2070:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2071:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2072:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2073:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2074:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
2075:     Then Loan Repayment schedule has the following data in Total row:
2076:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2077:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
2078:     Then Loan Transactions tab has the following data:
2079:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2080:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2081:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
2082:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2083: 
2084:     When Admin sets the business date to "15 March 2024"
2085:     When Admin runs inline COB job for Loan
2086:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
2087:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
2088:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
2089:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
2090:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2091:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2092:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2093:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2094:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2095:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
2096:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
2097:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
2098:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
2099:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
2100:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
2101:     Then Loan Repayment schedule has the following data in Total row:
2102:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2103:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
2104:     Then Loan Transactions tab has the following data without accruals:
2105:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2106:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2107:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2108:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
2109:     Then Loan Transactions tab has the following new accrual data:
2110:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2111:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
2112:       | 01 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2113:       | 02 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2114:       | 03 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2115:       | 04 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2116:       | 05 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2117:       | 06 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2118:       | 07 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2119:       | 08 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2120:       | 09 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2121:       | 10 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2122:       | 11 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2123:       | 12 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2124:       | 13 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2125:       | 14 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2126:       | 15 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2127:       | 16 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2128:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2129:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2130:       | 19 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2131:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2132:       | 21 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2133:       | 22 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2134:       | 23 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2135:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2136:       | 25 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2137:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2138:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2139:       | 28 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2140:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2141:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2142:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2143:       | 03 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2144:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2145:       | 05 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2146:       | 06 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2147:       | 07 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2148:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2149:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2150:       | 10 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2151:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2152:       | 12 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2153:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2154:       | 14 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2155: 
2156:     When Admin sets the business date to "01 April 2024"
2157:     When Admin runs inline COB job for Loan
2158:     When Admin makes "MERCHANT_ISSUED_REFUND" transaction with "AUTOPAY" payment type on "01 April 2024" with 34.02 EUR transaction amount
2159:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
2160:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2161:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2162:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2163:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2164:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2165:       | 4  | 17   | 01 April 2024     | 01 April 2024    | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 14.05 | 0.0        | 0.0  | 0.0         |
2166:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 3.99  | 3.99       | 0.0  | 10.06       |
2167:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 3.99  | 3.99       | 0.0  | 10.06       |
2168:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 3.99  | 3.99       | 0.0  | 10.06       |
2169:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 3.99  | 3.99       | 0.0  | 10.06       |
2170:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 4.01  | 4.01       | 0.0  | 10.02       |
2171:     Then Loan Repayment schedule has the following data in Total row:
2172:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2173:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 51.03 | 19.97      | 0.0  | 50.26       |
2174:     Then Loan Transactions tab has the following data without accruals:
2175:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2176:       | 01 January 2024  | Disbursement           | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2177:       | 01 February 2024 | Repayment              | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2178:       | 15 March 2024    | Re-age                 | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
2179:       | 01 April 2024    | Merchant Issued Refund | 34.02  | 33.9      | 0.12     | 0.0  | 0.0       | 49.67        | false    | false    |
2180:     Then Loan Transactions tab has the following new accrual data:
2181:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2182:       | 15 March 2024    | Accrual Adjustment     | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
2183:       | 16 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2184:       | 18 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2185:       | 19 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2186:       | 20 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2187:       | 22 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2188:       | 23 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2189:       | 25 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2190:       | 26 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2191:       | 28 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2192:       | 29 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2193:       | 30 March 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2194: 
2195:     When Admin sets the business date to "02 April 2024"
2196:     When Admin runs inline COB job for Loan
2197:     Then Loan Transactions tab has the following data without accruals:
2198:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2199:       | 01 January 2024  | Disbursement           | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2200:       | 01 February 2024 | Repayment              | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2201:       | 15 March 2024    | Re-age                 | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
2202:       | 01 April 2024    | Merchant Issued Refund | 34.02  | 33.9      | 0.12     | 0.0  | 0.0       | 49.67        | false    | false    |
2203:     Then Loan Transactions tab has the following new accrual data:
2204:       | Transaction date | Transaction Type       | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2205:       | 01 April 2024    | Accrual                | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2206: 
2207:     When Loan Pay-off is made on "02 April 2024"
2208:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
2209: 
2210:   @TestRailId:C4452 @AdvancedPaymentAllocation
2211:   Scenario: Verify Loan re-aging trn with repayment and 2nd disb before re-age - interest bearing multidisb loan with equal amortization; outstanding FULL interest - UC1.1
2212:     When Admin sets the business date to "01 January 2024"
2213:     When Admin creates a client with random data
2214:     When Admin creates a fully customized loan with the following data:
2215:       | LoanProduct                                                                 | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
2216:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALC_DAILY_MULTIDISBURSE | 01 January 2024   | 150            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
2217:     And Admin successfully approves the loan on "01 January 2024" with "150" amount and expected disbursement date on "01 January 2024"
2218:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
2219:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2220:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
2221:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
2222:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2223:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2224:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2225:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2226:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2227:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
2228:     Then Loan Repayment schedule has the following data in Total row:
2229:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
2230:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
2231:     Then Loan Transactions tab has the following data:
2232:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2233:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2234: 
2235:     When Admin sets the business date to "01 February 2024"
2236:     When Admin runs inline COB job for Loan
2237:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
2238:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2239:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2240:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2241:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2242:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2243:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2244:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2245:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2246:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
2247:     Then Loan Repayment schedule has the following data in Total row:
2248:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2249:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
2250:     Then Loan Transactions tab has the following data:
2251:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2252:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2253:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
2254:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2255: 
2256:     When Admin successfully disburse the loan on "01 February 2024" with "50" EUR transaction amount
2257:     When Admin runs inline COB job for Loan
2258:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2259:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2260:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2261:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2262:       |    |      | 01 February 2024 |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2263:       | 2  | 29   | 01 March 2024    |                  | 107.17          | 26.4          | 0.78     | 0.0  | 0.0       | 27.18 | 0.0   | 0.0        | 0.0  | 27.18       |
2264:       | 3  | 31   | 01 April 2024    |                  | 80.62           | 26.55         | 0.63     | 0.0  | 0.0       | 27.18 | 0.0   | 0.0        | 0.0  | 27.18       |
2265:       | 4  | 30   | 01 May 2024      |                  | 53.91           | 26.71         | 0.47     | 0.0  | 0.0       | 27.18 | 0.0   | 0.0        | 0.0  | 27.18       |
2266:       | 5  | 31   | 01 June 2024     |                  | 27.04           | 26.87         | 0.31     | 0.0  | 0.0       | 27.18 | 0.0   | 0.0        | 0.0  | 27.18       |
2267:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 27.04         | 0.16     | 0.0  | 0.0       | 27.2  | 0.0   | 0.0        | 0.0  | 27.2        |
2268:     Then Loan Repayment schedule has the following data in Total row:
2269:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2270:       | 150.0         | 2.93     | 0.0  | 0.0       | 152.93 | 17.01 | 0.0        | 0.0  | 135.92      |
2271:     Then Loan Transactions tab has the following data:
2272:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2273:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2274:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
2275:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2276:       | 01 February 2024 | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
2277: 
2278:     When Admin sets the business date to "15 March 2024"
2279:     When Admin runs inline COB job for Loan
2280:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
2281:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
2282:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
2283:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
2284:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2285:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2286:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2287:       |    |      | 01 February 2024  |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2288:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 133.57          | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2289:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 133.57          | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2290:       | 4  | 17   | 01 April 2024     |                  | 111.31          | 22.26         | 0.4      | 0.0  | 0.0       | 22.66 | 0.0   | 0.0        | 0.0  | 22.66       |
2291:       | 5  | 30   | 01 May 2024       |                  | 89.05           | 22.26         | 0.4      | 0.0  | 0.0       | 22.66 | 0.0   | 0.0        | 0.0  | 22.66       |
2292:       | 6  | 31   | 01 June 2024      |                  | 66.79           | 22.26         | 0.4      | 0.0  | 0.0       | 22.66 | 0.0   | 0.0        | 0.0  | 22.66       |
2293:       | 7  | 30   | 01 July 2024      |                  | 44.53           | 22.26         | 0.4      | 0.0  | 0.0       | 22.66 | 0.0   | 0.0        | 0.0  | 22.66       |
2294:       | 8  | 31   | 01 August 2024    |                  | 22.27           | 22.26         | 0.4      | 0.0  | 0.0       | 22.66 | 0.0   | 0.0        | 0.0  | 22.66       |
2295:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 22.27         | 0.41     | 0.0  | 0.0       | 22.68 | 0.0   | 0.0        | 0.0  | 22.68       |
2296:     Then Loan Repayment schedule has the following data in Total row:
2297:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2298:       | 150.0         | 2.99     | 0.0  | 0.0       | 152.99 | 17.01 | 0.0        | 0.0  | 135.98      |
2299:     Then Loan Transactions tab has the following data without accruals:
2300:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2301:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2302:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2303:       | 01 February 2024 | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
2304:       | 15 March 2024    | Re-age           | 135.98 | 133.57    | 2.41     | 0.0  | 0.0       | 0.0          | false    | false    |
2305:     Then Loan Transactions tab has the following new accrual data:
2306:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2307:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
2308:       | 01 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2309:       | 02 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2310:       | 03 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2311:       | 04 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2312:       | 05 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2313:       | 06 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2314:       | 07 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2315:       | 08 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2316:       | 09 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2317:       | 10 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2318:       | 11 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2319:       | 12 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2320:       | 13 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2321:       | 14 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2322:       | 15 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2323:       | 16 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2324:       | 17 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2325:       | 18 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2326:       | 19 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2327:       | 20 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2328:       | 21 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2329:       | 22 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2330:       | 23 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2331:       | 24 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2332:       | 25 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2333:       | 26 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2334:       | 27 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2335:       | 28 February 2024 | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2336:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2337: 
2338:       | 01 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2339:       | 02 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2340:       | 03 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2341:       | 04 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2342:       | 05 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2343:       | 06 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2344:       | 07 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2345:       | 08 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2346:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2347:       | 10 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2348:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2349:       | 12 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2350:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2351:       | 14 March 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2352: 
2353:     When Admin sets the business date to "15 April 2024"
2354:     When Admin runs inline COB job for Loan
2355:     Then Loan Transactions tab has the following data without accruals:
2356:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2357:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2358:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2359:       | 01 February 2024 | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
2360:       | 15 March 2024    | Re-age           | 135.98 | 133.57    | 2.41     | 0.0  | 0.0       | 0.0          | false    | false    |
2361:     Then Loan Transactions tab has the following new accrual data:
2362:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2363:       | 15 March 2024    | Accrual Adjustment | 1.11   | 0.0       | 1.11     | 0.0  | 0.0       | 0.0          | false    | false    |
2364:       | 16 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2365:       | 17 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2366:       | 18 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2367:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2368:       | 20 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2369:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2370:       | 22 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2371:       | 23 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2372:       | 24 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2373:       | 25 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2374:       | 26 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2375:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2376:       | 28 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2377:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2378:       | 30 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2379:       | 31 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2380:       | 01 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2381:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2382:       | 03 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2383:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2384:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2385:       | 06 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2386:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2387:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2388:       | 09 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2389:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2390:       | 11 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2391:       | 12 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2392:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2393:       | 14 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2394: 
2395:     When Loan Pay-off is made on "15 April 2024"
2396:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
2397: 
2398:   @TestRailId:C4453 @AdvancedPaymentAllocation
2399:   Scenario: Verify Loan re-aging transaction with charge and repayment - interest bearing loan with equal amortization; outstanding FULL interest - UC2.1
2400:     When Admin sets the business date to "01 January 2024"
2401:     When Admin creates a client with random data
2402:     When Admin creates a fully customized loan with the following data:
2403:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
2404:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
2405:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
2406:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
2407:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2408:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
2409:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
2410:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2411:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2412:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2413:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2414:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2415:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
2416:     Then Loan Repayment schedule has the following data in Total row:
2417:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
2418:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
2419:     Then Loan Transactions tab has the following data:
2420:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2421:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2422: 
2423:     When Admin sets the business date to "01 February 2024"
2424:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
2425:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2426:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2427:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2428:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2429:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2430:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2431:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2432:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2433:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
2434:     Then Loan Repayment schedule has the following data in Total row:
2435:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2436:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
2437:     Then Loan Transactions tab has the following data:
2438:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2439:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2440:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2441: 
2442:     When Admin sets the business date to "15 February 2024"
2443:     And Admin adds "LOAN_SNOOZE_FEE" due date charge with "15 February 2024" due date and 10 EUR transaction amount
2444:     Then Loan Charges tab has the following data:
2445:       | Name       | isPenalty | Payment due at     | Due as of        | Calculation type | Due  | Paid | Waived | Outstanding |
2446:       | Snooze fee | false     | Specified due date | 15 February 2024 | Flat             | 10.0 | 0.0  | 0.0    | 10.0        |
2447:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2448:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2449:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2450:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2451:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 10.0 | 0.0       | 27.01 | 0.0   | 0.0        | 0.0  | 27.01       |
2452:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2453:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2454:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2455:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
2456:     Then Loan Repayment schedule has the following data in Total row:
2457:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2458:       | 100.0         | 2.05     | 10.0 | 0.0       | 112.05 | 17.01 | 0.0        | 0.0  | 95.04       |
2459:     Then Loan Transactions tab has the following data:
2460:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2461:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2462:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2463: 
2464:     When Admin sets the business date to "16 February 2024"
2465:     When Admin runs inline COB job for Loan
2466:     And Customer makes "AUTOPAY" repayment on "16 February 2024" with 10 EUR transaction amount
2467:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2468:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2469:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2470:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2471:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 10.0 | 0.0       | 27.01 | 10.0  | 10.0       | 0.0  | 17.01       |
2472:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2473:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2474:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2475:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
2476:     Then Loan Repayment schedule has the following data in Total row:
2477:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2478:       | 100.0         | 2.05     | 10.0 | 0.0       | 112.05 | 27.01 | 10.0       | 0.0  | 85.04       |
2479:     Then Loan Transactions tab has the following data:
2480:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2481:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2482:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2483:       | 15 February 2024 | Accrual          | 10.82  | 0.0       | 0.82     | 10.0 | 0.0       | 0.0          | false    | false    |
2484:       | 16 February 2024 | Repayment        | 10.0   | 0.0       | 0.0      | 10.0 | 0.0       | 83.57        | false    | false    |
2485: 
2486:     When Admin sets the business date to "15 March 2024"
2487:     When Admin runs inline COB job for Loan
2488:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
2489:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
2490:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
2491:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
2492:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2493:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2494:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2495:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 10.0 | 0.0       | 10.0  | 10.0  | 10.0       | 0.0  | 0.0         |
2496:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2497:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
2498:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
2499:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
2500:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
2501:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
2502:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
2503:     Then Loan Repayment schedule has the following data in Total row:
2504:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2505:       | 100.0         | 2.09     | 10.0 | 0.0       | 112.09 | 27.01 | 10.0       | 0.0  | 85.08       |
2506:     Then Loan Transactions tab has the following data without accruals:
2507:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2508:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2509:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2510:       | 16 February 2024 | Repayment        | 10.0   | 0.0       | 0.0      | 10.0 | 0.0       | 83.57        | false    | false    |
2511:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
2512:     Then Loan Transactions tab has the following new accrual data:
2513:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2514:       | 15 February 2024 | Accrual          | 10.82  | 0.0       | 0.82     | 10.0 | 0.0       | 0.0          | false    | false    |
2515:       | 16 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2516:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2517:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2518:       | 19 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2519:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2520:       | 21 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2521:       | 22 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2522:       | 23 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2523:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2524:       | 25 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2525:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2526:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2527:       | 28 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2528:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2529:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2530:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2531:       | 03 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2532:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2533:       | 05 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2534:       | 06 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2535:       | 07 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2536:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2537:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2538:       | 10 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2539:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2540:       | 12 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2541:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2542:       | 14 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2543: 
2544:     When Admin sets the business date to "05 April 2024"
2545:     When Admin runs inline COB job for Loan
2546:     Then Loan Transactions tab has the following data without accruals:
2547:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2548:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2549:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
2550:       | 16 February 2024 | Repayment        | 10.0   | 0.0       | 0.0      | 10.0 | 0.0       | 83.57        | false    | false    |
2551:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
2552:     Then Loan Transactions tab has the following new accrual data:
2553:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2554:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
2555:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2556:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2557:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2558:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2559:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2560:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2561:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2562:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2563:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2564:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2565:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2566:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2567:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2568:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2569:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2570:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2571:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2572:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2573:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2574: 
2575:     When Loan Pay-off is made on "05 April 2024"
2576:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
2577: 
2578:   @TestRailId:C4454 @AdvancedPaymentAllocation
2579:   Scenario: Verify Loan re-aging trn with repayment, charge and partial chargeback with payment alloc - interest bearing loan with equal amortization; outstanding FULL interest - UC3.3
2580:     When Admin sets the business date to "01 January 2024"
2581:     When Admin creates a client with random data
2582:     When Admin creates a fully customized loan with the following data:
2583:       | LoanProduct                                                                                       | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
2584:       | LP2_ADV_PYMNT_INTEREST_DAILY_INTEREST_RECALC_EMI_360_30_CHARGEBACK_INTEREST_PENALTY_FEE_PRINCIPAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
2585:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
2586:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
2587:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2588:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
2589:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
2590:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2591:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2592:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2593:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2594:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2595:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
2596:     Then Loan Repayment schedule has the following data in Total row:
2597:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
2598:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
2599:     Then Loan Transactions tab has the following data:
2600:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2601:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2602: 
2603:     When Admin sets the business date to "01 February 2024"
2604:     When Admin runs inline COB job for Loan
2605:     And Admin adds "LOAN_SNOOZE_FEE" due date charge with "01 February 2024" due date and 8 EUR transaction amount
2606:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
2607:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 10 EUR transaction amount
2608:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2609:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2610:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2611:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 8.0  | 0.0       | 25.01 | 17.01 | 0.0        | 0.0  | 8.0         |
2612:       | 2  | 29   | 01 March 2024    |           | 67.06           | 18.51         | 0.5      | 8.0  | 0.0       | 27.01 | 0.0   | 0.0        | 0.0  | 27.01       |
2613:       | 3  | 31   | 01 April 2024    |           | 50.44           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2614:       | 4  | 30   | 01 May 2024      |           | 33.72           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2615:       | 5  | 31   | 01 June 2024     |           | 16.91           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2616:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.91         | 0.1      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
2617:     Then Loan Repayment schedule has the following data in Total row:
2618:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2619:       | 102.0         | 2.06     | 16.0 | 0.0       | 120.06 | 17.01 | 0.0        | 0.0  | 103.05      |
2620:     Then Loan Transactions tab has the following data:
2621:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2622:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2623:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
2624:       | 01 February 2024 | Repayment        | 17.01  | 9.01      | 0.0      | 8.0  | 0.0       | 90.99        | false    | false    |
2625:       | 01 February 2024 | Chargeback       | 10.0   | 2.0       | 0.0      | 8.0  | 0.0       | 92.99        | false    | false    |
2626: 
2627:     When Admin sets the business date to "15 March 2024"
2628:     When Admin runs inline COB job for Loan
2629:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
2630:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
2631:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
2632:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
2633:       | Nr | Days | Date              | Paid date     | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
2634:       |    |      | 01 January 2024   |               | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
2635:       | 1  | 31   | 01 February 2024  | 15 March 2024 | 90.99           | 9.01          | 0.0      | 8.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
2636:       | 2  | 29   | 01 March 2024     | 15 March 2024 | 92.99           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2637:       | 3  | 14   | 15 March 2024     | 15 March 2024 | 92.99           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2638:       | 4  | 17   | 01 April 2024     |               | 77.49           | 15.5          | 0.36     | 1.33 | 0.0       | 17.19 | 0.0   | 0.0        | 0.0  | 17.19       |
2639:       | 5  | 30   | 01 May 2024       |               | 61.99           | 15.5          | 0.36     | 1.33 | 0.0       | 17.19 | 0.0   | 0.0        | 0.0  | 17.19       |
2640:       | 6  | 31   | 01 June 2024      |               | 46.49           | 15.5          | 0.36     | 1.33 | 0.0       | 17.19 | 0.0   | 0.0        | 0.0  | 17.19       |
2641:       | 7  | 30   | 01 July 2024      |               | 30.99           | 15.5          | 0.36     | 1.33 | 0.0       | 17.19 | 0.0   | 0.0        | 0.0  | 17.19       |
2642:       | 8  | 31   | 01 August 2024    |               | 15.49           | 15.5          | 0.36     | 1.33 | 0.0       | 17.19 | 0.0   | 0.0        | 0.0  | 17.19       |
2643:       | 9  | 31   | 01 September 2024 |               | 0.0             | 15.49         | 0.37     | 1.35 | 0.0       | 17.21 | 0.0   | 0.0        | 0.0  | 17.21       |
2644:     Then Loan Repayment schedule has the following data in Total row:
2645:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
2646:       | 102.0         | 2.17     | 16.0 | 0.0       | 120.17 | 17.01 | 0.0        | 0.0  | 103.16      |
2647:     Then Loan Transactions tab has the following data without accruals:
2648:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2649:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2650:       | 01 February 2024 | Repayment        | 17.01  | 9.01      | 0.0      | 8.0  | 0.0       | 90.99        | false    | false    |
2651:       | 01 February 2024 | Chargeback       | 10.0   | 2.0       | 0.0      | 8.0  | 0.0       | 92.99        | false    | false    |
2652:       | 15 March 2024    | Re-age           | 103.16 | 92.99     | 2.17     | 8.0  | 0.0       | 0.0          | false    | false    |
2653:     Then Loan Transactions tab has the following new accrual data:
2654:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2655:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
2656:       | 01 February 2024 | Accrual          | 8.02   | 0.0       | 0.02     | 8.0  | 0.0       | 0.0          | false    | false    |
2657:       | 02 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2658:       | 03 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2659:       | 04 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2660:       | 05 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2661:       | 06 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2662:       | 07 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2663:       | 08 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2664:       | 09 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2665:       | 10 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2666:       | 11 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2667:       | 12 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2668:       | 13 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2669:       | 14 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2670:       | 15 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2671:       | 16 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2672:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2673:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2674:       | 19 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2675:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2676:       | 21 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2677:       | 22 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2678:       | 23 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2679:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2680:       | 25 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2681:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2682:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2683:       | 28 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2684:       | 29 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2685: 
2686:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2687:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2688:       | 03 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2689:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2690:       | 05 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2691:       | 06 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2692:       | 07 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2693:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2694:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2695:       | 10 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2696:       | 11 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2697:       | 12 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2698:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2699:       | 14 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2700: 
2701:     When Admin sets the business date to "05 April 2024"
2702:     When Admin runs inline COB job for Loan
2703:     Then Loan Transactions tab has the following data without accruals:
2704:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2705:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2706:       | 01 February 2024 | Repayment        | 17.01  | 9.01      | 0.0      | 8.0  | 0.0       | 90.99        | false    | false    |
2707:       | 01 February 2024 | Chargeback       | 10.0   | 2.0       | 0.0      | 8.0  | 0.0       | 92.99        | false    | false    |
2708:       | 15 March 2024    | Re-age           | 103.16 | 92.99     | 2.17     | 8.0  | 0.0       | 0.0          | false    | false    |
2709:     Then Loan Transactions tab has the following new accrual data:
2710:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2711:       | 15 March 2024    | Accrual Adjustment | 1.35   | 0.0       | 1.35     | 0.0  | 0.0       | 0.0          | false    | false    |
2712:       | 16 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2713:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2714:       | 18 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2715:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2716:       | 20 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2717:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2718:       | 22 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2719:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2720:       | 24 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2721:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2722:       | 26 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2723:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2724:       | 28 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2725:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2726:       | 30 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2727:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2728:       | 01 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2729:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2730:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2731:       | 04 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2732: 
2733:     When Loan Pay-off is made on "05 April 2024"
2734:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
2735: 
2736:   @TestRailId:C4455 @AdvancedPaymentAllocation
2737:   Scenario: Verify Loan re-aging trn with repayment and charges(fee and penalty) with due date after re-age - interest bearing loan with equal amortization; outstanding FULL interest - UC3.5
2738:     When Admin sets the business date to "01 January 2024"
2739:     When Admin creates a client with random data
2740:     When Admin creates a fully customized loan with the following data:
2741:       | LoanProduct                                                                        | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
2742:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALCULATION_DAILY_TILL_PRECLOSE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
2743:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
2744:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
2745:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2746:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
2747:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
2748:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2749:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2750:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2751:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2752:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2753:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
2754:     Then Loan Repayment schedule has the following data in Total row:
2755:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
2756:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
2757:     Then Loan Transactions tab has the following data:
2758:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2759:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2760: 
2761:     When Admin sets the business date to "01 February 2024"
2762:     And Admin adds "LOAN_SNOOZE_FEE" due date charge with "01 April 2024" due date and 8 EUR transaction amount
2763:     When Admin adds "LOAN_NSF_FEE" due date charge with "01 April 2024" due date and 10 EUR transaction amount
2764:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
2765:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
2766:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
2767:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2768:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2769:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 8.0  | 10.0      | 35.01 | 0.0  | 0.0        | 0.0  | 35.01       |
2770:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2771:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
2772:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
2773:     Then Loan Repayment schedule has the following data in Total row:
2774:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
2775:       | 100.0         | 2.05     | 8.0  | 10.0      | 120.05 | 0.0  | 0.0        | 0.0  | 120.05      |
2776:     Then Loan Transactions tab has the following data:
2777:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2778:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2779: 
2780:     When Admin sets the business date to "15 March 2024"
2781:     When Admin runs inline COB job for Loan
2782:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
2783:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
2784:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
2785:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
2786:       | Nr | Days | Date              | Paid date     | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
2787:       |    |      | 01 January 2024   |               | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
2788:       | 1  | 31   | 01 February 2024  | 15 March 2024 | 100.0           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0  | 0.0        | 0.0  | 0.0         |
2789:       | 2  | 29   | 01 March 2024     | 15 March 2024 | 100.0           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0  | 0.0        | 0.0  | 0.0         |
2790:       | 3  | 14   | 15 March 2024     | 15 March 2024 | 100.0           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
2791:       | 4  | 17   | 01 April 2024     |               | 83.33           | 16.67         | 0.37     | 1.33 | 1.67      | 20.04 | 0.0  | 0.0        | 0.0  | 20.04       |
2792:       | 5  | 30   | 01 May 2024       |               | 66.66           | 16.67         | 0.37     | 1.33 | 1.67      | 20.04 | 0.0  | 0.0        | 0.0  | 20.04       |
2793:       | 6  | 31   | 01 June 2024      |               | 49.99           | 16.67         | 0.37     | 1.33 | 1.67      | 20.04 | 0.0  | 0.0        | 0.0  | 20.04       |
2794:       | 7  | 30   | 01 July 2024      |               | 33.32           | 16.67         | 0.37     | 1.33 | 1.67      | 20.04 | 0.0  | 0.0        | 0.0  | 20.04       |
2795:       | 8  | 31   | 01 August 2024    |               | 16.65           | 16.67         | 0.37     | 1.33 | 1.67      | 20.04 | 0.0  | 0.0        | 0.0  | 20.04       |
2796:       | 9  | 31   | 01 September 2024 |               | 0.0             | 16.65         | 0.39     | 1.35 | 1.65      | 20.04 | 0.0  | 0.0        | 0.0  | 20.04       |
2797:     Then Loan Repayment schedule has the following data in Total row:
2798:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
2799:       | 100.0         | 2.24     | 8.0  | 10.0      | 120.24 | 0.0  | 0.0        | 0.0  | 120.24      |
2800:     Then Loan Transactions tab has the following data:
2801:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2802:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2803:       | 14 March 2024    | Accrual          | 1.31   | 0.0       | 1.31     | 0.0  | 0.0       | 0.0          | false    | false    |
2804:       | 15 March 2024    | Re-age           | 120.24 | 100.0     | 2.24     | 8.0  | 10.0      | 0.0          | false    | false    |
2805: 
2806:     When Admin sets the business date to "01 April 2024"
2807:     When Admin runs inline COB job for Loan
2808:     And Customer makes "AUTOPAY" repayment on "01 April 2024" with 20.04 EUR transaction amount
2809:     Then Loan has 100.2 outstanding amount
2810:     Then Loan Transactions tab has the following data without accruals:
2811:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2812:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2813:       | 15 March 2024    | Re-age           | 120.24 | 100.0     | 2.24     | 8.0  | 10.0      | 0.0          | false    | false    |
2814:       | 01 April 2024    | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 83.33        | false    | false    |
2815:     Then Loan Transactions tab has the following new accrual data:
2816:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2817:       | 14 March 2024    | Accrual            | 1.31   | 0.0       | 1.31     | 0.0  | 0.0       | 0.0          | false    | false    |
2818:       | 15 March 2024    | Accrual Adjustment | 1.31   | 0.0       | 1.31     | 0.0  | 0.0       | 0.0          | false    | false    |
2819:       | 16 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2820:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2821:       | 18 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2822:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2823:       | 20 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2824:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2825:       | 22 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2826:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2827:       | 24 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2828:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2829:       | 26 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2830:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2831:       | 28 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2832:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2833:       | 30 March 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
2834:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2835: 
2836:     When Admin sets the business date to "01 May 2024"
2837:     When Admin runs inline COB job for Loan
2838:     And Customer makes "AUTOPAY" repayment on "01 May 2024" with 20.04 EUR transaction amount
2839:     Then Loan has 80.16 outstanding amount
2840:     Then Loan Transactions tab has the following data without accruals:
2841:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2842:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2843:       | 15 March 2024    | Re-age           | 120.24 | 100.0     | 2.24     | 8.0  | 10.0      | 0.0          | false    | false    |
2844:       | 01 April 2024    | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 83.33        | false    | false    |
2845:       | 01 May 2024      | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 66.66        | false    | false    |
2846:     Then Loan Transactions tab has the following new accrual data:
2847:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2848:       | 01 April 2024    | Accrual            | 18.02  | 0.0       | 0.02     | 8.0  | 10.0      | 0.0          | false    | false    |
2849:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2850:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2851:       | 04 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2852:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2853:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2854:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2855:       | 08 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2856:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2857:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2858:       | 11 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2859:       | 12 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2860:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2861:       | 14 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2862:       | 15 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2863:       | 16 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2864:       | 17 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2865:       | 18 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2866:       | 19 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2867:       | 20 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2868:       | 21 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2869:       | 22 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2870:       | 23 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2871:       | 24 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2872:       | 25 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2873:       | 26 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2874:       | 27 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2875:       | 28 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2876:       | 29 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2877:       | 30 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2878: 
2879:     When Admin sets the business date to "01 June 2024"
2880:     When Admin runs inline COB job for Loan
2881:     And Customer makes "AUTOPAY" repayment on "01 June 2024" with 20.04 EUR transaction amount
2882:     Then Loan has 60.12 outstanding amount
2883:     Then Loan Transactions tab has the following data without accruals:
2884:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2885:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2886:       | 15 March 2024    | Re-age           | 120.24 | 100.0     | 2.24     | 8.0  | 10.0      | 0.0          | false    | false    |
2887:       | 01 April 2024    | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 83.33        | false    | false    |
2888:       | 01 May 2024      | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 66.66        | false    | false    |
2889:       | 01 June 2024     | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 49.99        | false    | false    |
2890:     Then Loan Transactions tab has the following new accrual data:
2891:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2892:       | 01 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2893:       | 02 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2894:       | 03 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2895:       | 04 May 2024      | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2896:       | 05 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2897:       | 06 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2898:       | 07 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2899:       | 08 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2900:       | 09 May 2024      | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2901:       | 10 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2902:       | 11 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2903:       | 12 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2904:       | 13 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2905:       | 14 May 2024      | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2906:       | 15 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2907:       | 16 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2908:       | 17 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2909:       | 18 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2910:       | 19 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2911:       | 20 May 2024      | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2912:       | 21 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2913:       | 22 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2914:       | 23 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2915:       | 24 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2916:       | 25 May 2024      | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2917:       | 26 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2918:       | 27 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2919:       | 28 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2920:       | 29 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2921:       | 30 May 2024      | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2922:       | 31 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2923: 
2924:     When Admin sets the business date to "01 July 2024"
2925:     When Admin runs inline COB job for Loan
2926:     And Customer makes "AUTOPAY" repayment on "01 July 2024" with 20.04 EUR transaction amount
2927:     Then Loan has 40.08 outstanding amount
2928:     Then Loan Transactions tab has the following data without accruals:
2929:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2930:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2931:       | 15 March 2024    | Re-age           | 120.24 | 100.0     | 2.24     | 8.0  | 10.0      | 0.0          | false    | false    |
2932:       | 01 April 2024    | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 83.33        | false    | false    |
2933:       | 01 May 2024      | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 66.66        | false    | false    |
2934:       | 01 June 2024     | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 49.99        | false    | false    |
2935:       | 01 July 2024     | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 33.32        | false    | false    |
2936:     Then Loan Transactions tab has the following new accrual data:
2937:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2938:       | 01 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2939:       | 02 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2940:       | 03 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2941:       | 04 June 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2942:       | 05 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2943:       | 06 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2944:       | 07 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2945:       | 08 June 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2946:       | 09 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2947:       | 10 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2948:       | 11 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2949:       | 12 June 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2950:       | 13 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2951:       | 14 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2952:       | 15 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2953:       | 16 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2954:       | 17 June 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2955:       | 18 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2956:       | 19 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2957:       | 20 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2958:       | 21 June 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2959:       | 22 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2960:       | 23 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2961:       | 24 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2962:       | 25 June 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2963:       | 26 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2964:       | 27 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2965:       | 28 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2966:       | 29 June 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2967:       | 30 June 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2968: 
2969:     When Admin sets the business date to "01 August 2024"
2970:     When Admin runs inline COB job for Loan
2971:     And Customer makes "AUTOPAY" repayment on "01 August 2024" with 20.04 EUR transaction amount
2972:     Then Loan has 20.04 outstanding amount
2973:     Then Loan Transactions tab has the following data without accruals:
2974:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2975:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
2976:       | 15 March 2024    | Re-age           | 120.24 | 100.0     | 2.24     | 8.0  | 10.0      | 0.0          | false    | false    |
2977:       | 01 April 2024    | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 83.33        | false    | false    |
2978:       | 01 May 2024      | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 66.66        | false    | false    |
2979:       | 01 June 2024     | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 49.99        | false    | false    |
2980:       | 01 July 2024     | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 33.32        | false    | false    |
2981:       | 01 August 2024   | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 16.65        | false    | false    |
2982:     Then Loan Transactions tab has the following new accrual data:
2983:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
2984:       | 01 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2985:       | 02 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2986:       | 03 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2987:       | 04 July 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2988:       | 05 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2989:       | 06 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2990:       | 07 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2991:       | 08 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2992:       | 09 July 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2993:       | 10 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2994:       | 11 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2995:       | 12 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2996:       | 13 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2997:       | 14 July 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
2998:       | 15 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
2999:       | 16 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3000:       | 17 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3001:       | 18 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3002:       | 19 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3003:       | 20 July 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3004:       | 21 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3005:       | 22 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3006:       | 23 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3007:       | 24 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3008:       | 25 July 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3009:       | 26 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3010:       | 27 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3011:       | 28 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3012:       | 29 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3013:       | 30 July 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3014:       | 31 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3015: 
3016:     When Admin sets the business date to "01 September 2024"
3017:     When Admin runs inline COB job for Loan
3018:     And Customer makes "AUTOPAY" repayment on "01 September 2024" with 20.04 EUR transaction amount
3019:     Then Loan Transactions tab has the following data without accruals:
3020:       | Transaction date  | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3021:       | 01 January 2024   | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3022:       | 15 March 2024     | Re-age           | 120.24 | 100.0     | 2.24     | 8.0  | 10.0      | 0.0          | false    | false    |
3023:       | 01 April 2024     | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 83.33        | false    | false    |
3024:       | 01 May 2024       | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 66.66        | false    | false    |
3025:       | 01 June 2024      | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 49.99        | false    | false    |
3026:       | 01 July 2024      | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 33.32        | false    | false    |
3027:       | 01 August 2024    | Repayment        | 20.04  | 16.67     | 0.37     | 1.33 | 1.67      | 16.65        | false    | false    |
3028:       | 01 September 2024 | Repayment        | 20.04  | 16.65     | 0.39     | 1.35 | 1.65      | 0.0          | false    | false    |
3029:     Then Loan Transactions tab has the following new accrual data:
3030:       | Transaction date  | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3031:       | 01 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3032:       | 02 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3033:       | 03 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3034:       | 04 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3035:       | 05 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3036:       | 06 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3037:       | 07 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3038:       | 08 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3039:       | 09 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3040:       | 10 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3041:       | 11 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3042:       | 12 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3043:       | 13 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3044:       | 14 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3045:       | 15 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3046:       | 16 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3047:       | 17 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3048:       | 18 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3049:       | 19 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3050:       | 20 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3051:       | 21 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3052:       | 22 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3053:       | 23 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3054:       | 24 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3055:       | 25 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3056:       | 26 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3057:       | 27 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3058:       | 28 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3059:       | 29 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3060:       | 30 August 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3061:       | 31 August 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3062:       | 01 September 2024 | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3063:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
3064: 
3065:   @TestRailId:C4456 @AdvancedPaymentAllocation
3066:   Scenario: Verify Loan re-aging transaction with partially paid installment; adjust to last - interest bearing loan with equal amortization; outstanding full interest - UC5.1
3067:     When Admin sets the business date to "01 January 2024"
3068:     When Admin creates a client with random data
3069:     When Admin creates a fully customized loan with the following data:
3070:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
3071:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_IR_DAILY_TILL_PRECLOSE_LAST_INSTALLMENT_STRATEGY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
3072:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
3073:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
3074:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3075:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
3076:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
3077:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3078:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3079:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3080:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3081:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3082:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
3083:     Then Loan Repayment schedule has the following data in Total row:
3084:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3085:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
3086:     Then Loan Transactions tab has the following data:
3087:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3088:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3089: 
3090:     When Admin sets the business date to "01 February 2024"
3091:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 25 EUR transaction amount
3092:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3093:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3094:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3095:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3096:       | 2  | 29   | 01 March 2024    |                  | 67.0            | 16.57         | 0.44     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3097:       | 3  | 31   | 01 April 2024    |                  | 50.33           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3098:       | 4  | 30   | 01 May 2024      |                  | 33.57           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3099:       | 5  | 31   | 01 June 2024     |                  | 16.71           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3100:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.71         | 0.05     | 0.0  | 0.0       | 16.76 | 7.99  | 7.99       | 0.0  | 8.77        |
3101:     Then Loan Repayment schedule has the following data in Total row:
3102:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3103:       | 100.0         | 1.81     | 0.0  | 0.0       | 101.81 | 25.0 | 7.99       | 0.0  | 76.81       |
3104:     Then Loan Transactions tab has the following data:
3105:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3106:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3107:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
3108: 
3109:     When Admin sets the business date to "15 March 2024"
3110:     When Admin runs inline COB job for Loan
3111:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3112:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3113:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3114:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3115:       | 2  | 29   | 01 March 2024    |                  | 67.0            | 16.57         | 0.44     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3116:       | 3  | 31   | 01 April 2024    |                  | 50.38           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3117:       | 4  | 30   | 01 May 2024      |                  | 33.62           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3118:       | 5  | 31   | 01 June 2024     |                  | 16.76           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3119:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.76         | 0.05     | 0.0  | 0.0       | 16.81 | 7.99  | 7.99       | 0.0  | 8.82        |
3120:     Then Loan Repayment schedule has the following data in Total row:
3121:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3122:       | 100.0         | 1.86     | 0.0  | 0.0       | 101.86 | 25.0 | 7.99       | 0.0  | 76.86       |
3123:     Then Loan Transactions tab has the following data:
3124:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3125:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3126:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
3127:       | 14 March 2024    | Accrual          | 1.2    | 0.0       | 1.2      | 0.0  | 0.0       | 0.0          | false    | false    |
3128: 
3129:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
3130:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
3131:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
3132:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3133:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3134:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3135:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3136:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3137:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 75.58           | 7.99          | 0.0      | 0.0  | 0.0       | 7.99  | 7.99  | 7.99       | 0.0  | 0.0         |
3138:       | 4  | 17   | 01 April 2024     |                  | 62.98           | 12.6          | 0.21     | 0.0  | 0.0       | 12.81 | 0.0   | 0.0        | 0.0  | 12.81       |
3139:       | 5  | 30   | 01 May 2024       |                  | 50.38           | 12.6          | 0.21     | 0.0  | 0.0       | 12.81 | 0.0   | 0.0        | 0.0  | 12.81       |
3140:       | 6  | 31   | 01 June 2024      |                  | 37.78           | 12.6          | 0.21     | 0.0  | 0.0       | 12.81 | 0.0   | 0.0        | 0.0  | 12.81       |
3141:       | 7  | 30   | 01 July 2024      |                  | 25.18           | 12.6          | 0.21     | 0.0  | 0.0       | 12.81 | 0.0   | 0.0        | 0.0  | 12.81       |
3142:       | 8  | 31   | 01 August 2024    |                  | 12.58           | 12.6          | 0.21     | 0.0  | 0.0       | 12.81 | 0.0   | 0.0        | 0.0  | 12.81       |
3143:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 12.58         | 0.23     | 0.0  | 0.0       | 12.81 | 0.0   | 0.0        | 0.0  | 12.81       |
3144:     Then Loan Repayment schedule has the following data in Total row:
3145:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3146:       | 100.0         | 1.86     | 0.0  | 0.0       | 101.86 | 25.0 | 7.99       | 0.0  | 76.86       |
3147:     Then Loan Transactions tab has the following data:
3148:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3149:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3150:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
3151:       | 14 March 2024    | Accrual          | 1.2    | 0.0       | 1.2      | 0.0  | 0.0       | 0.0          | false    | false    |
3152:       | 15 March 2024    | Re-age           | 76.86  | 75.58     | 1.28     | 0.0  | 0.0       | 0.0          | false    | false    |
3153: 
3154:     When Admin sets the business date to "05 April 2024"
3155:     When Admin runs inline COB job for Loan
3156:     Then Loan Transactions tab has the following data without accruals:
3157:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3158:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3159:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
3160:       | 15 March 2024    | Re-age           | 76.86  | 75.58     | 1.28     | 0.0  | 0.0       | 0.0          | false    | false    |
3161:     Then Loan Transactions tab has the following new accrual data:
3162:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3163:       | 14 March 2024    | Accrual            | 1.2    | 0.0       | 1.2      | 0.0  | 0.0       | 0.0          | false    | false    |
3164:       | 15 March 2024    | Accrual Adjustment | 0.62   | 0.0       | 0.62     | 0.0  | 0.0       | 0.0          | false    | false    |
3165:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3166:       | 17 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3167:       | 18 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3168:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3169:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3170:       | 21 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3171:       | 22 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3172:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3173:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3174:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3175:       | 26 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3176:       | 27 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3177:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3178:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3179:       | 30 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3180:       | 31 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3181:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3182:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3183:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3184: 
3185:     When Loan Pay-off is made on "05 April 2024"
3186:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
3187: 
3188:   @TestRailId:C4457 @AdvancedPaymentAllocation
3189:   Scenario: Verify Loan re-aging trn with partial chargeback with custom payment alloc after re-age - interest bearing loan with equal amortization; outstanding FULL interest - UC6.2
3190:     When Admin sets the business date to "01 January 2024"
3191:     When Admin creates a client with random data
3192:     When Admin creates a fully customized loan with the following data:
3193:       | LoanProduct                                                                                       | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
3194:       | LP2_ADV_PYMNT_INTEREST_DAILY_INTEREST_RECALC_EMI_360_30_CHARGEBACK_INTEREST_PENALTY_FEE_PRINCIPAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
3195:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
3196:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
3197:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3198:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
3199:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
3200:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3201:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3202:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3203:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3204:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3205:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
3206:     Then Loan Repayment schedule has the following data in Total row:
3207:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3208:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
3209:     Then Loan Transactions tab has the following data:
3210:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3211:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3212: 
3213:     When Admin sets the business date to "01 February 2024"
3214:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
3215:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3216:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3217:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3218:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3219:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3220:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3221:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3222:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3223:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
3224:     Then Loan Repayment schedule has the following data in Total row:
3225:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3226:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
3227:     Then Loan Transactions tab has the following data:
3228:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3229:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3230:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3231: 
3232:     When Admin sets the business date to "15 March 2024"
3233:     When Admin runs inline COB job for Loan
3234:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
3235:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
3236:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
3237:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3238:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3239:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3240:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3241:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3242:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3243:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3244:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3245:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3246:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3247:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3248:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3249:     Then Loan Repayment schedule has the following data in Total row:
3250:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3251:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
3252:     Then Loan Transactions tab has the following data:
3253:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3254:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3255:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3256:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3257:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
3258: 
3259:     When Admin sets the business date to "01 April 2024"
3260:     When Admin runs inline COB job for Loan
3261:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 10 EUR transaction amount
3262:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3263:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3264:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3265:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3266:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3267:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3268:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3269:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 23.35         | 0.83     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
3270:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3271:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3272:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3273:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3274:     Then Loan Repayment schedule has the following data in Total row:
3275:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3276:       | 109.42        | 2.67     | 0.0  | 0.0       | 112.09 | 17.01 | 0.0        | 0.0  | 95.08       |
3277:     Then Loan Transactions tab has the following data without accruals:
3278:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3279:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3280:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3281:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
3282:       | 01 April 2024    | Chargeback       | 10.0   | 9.42      | 0.58     | 0.0  | 0.0       | 92.99        | false    | false    |
3283:     Then Loan Transactions tab has the following new accrual data:
3284:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3285:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3286:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
3287:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3288:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3289:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3290:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3291:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3292:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3293:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3294:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3295:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3296:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3297:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3298:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3299:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3300:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3301:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3302:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3303: 
3304:     When Admin sets the business date to "10 April 2024"
3305:     When Admin runs inline COB job for Loan
3306:     Then Loan Transactions tab has the following data without accruals:
3307:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3308:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3309:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3310:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
3311:       | 01 April 2024    | Chargeback       | 10.0   | 9.42      | 0.58     | 0.0  | 0.0       | 92.99        | false    | false    |
3312:     Then Loan Transactions tab has the following new accrual data:
3313:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3314:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3315:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3316:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3317:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3318:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3319:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3320:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3321:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3322: 
3323:     When Loan Pay-off is made on "10 April 2024"
3324:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
3325: 
3326:   @TestRailId:C4458 @AdvancedPaymentAllocation
3327:   Scenario: Verify Loan re-aging transaction with downpayment - interest bearing loan with equal amortization; outstanding FULL interest - UC7
3328:     When Admin sets the business date to "01 January 2024"
3329:     When Admin creates a client with random data
3330:     When Admin creates a fully customized loan with the following data:
3331:       | LoanProduct                                                                          | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
3332:       | LP2_ADV_PYMNT_INTEREST_RECALCULATION_DAILY_EMI_360_30_MULTIDISBURSE_AUTO_DOWNPAYMENT | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
3333:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
3334:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
3335:     Then Loan Repayment schedule has 7 periods, with the following data for periods:
3336:       | Nr | Days | Date             | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
3337:       |    |      | 01 January 2024  |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
3338:       | 1  | 0    | 01 January 2024  | 01 January 2024 | 75.0            | 25.0          | 0.0      | 0.0  | 0.0       | 25.0  | 25.0 | 0.0        | 0.0  | 0.0         |
3339:       | 2  | 31   | 01 February 2024 |                 | 62.68           | 12.32         | 0.44     | 0.0  | 0.0       | 12.76 | 0.0  | 0.0        | 0.0  | 12.76       |
3340:       | 3  | 29   | 01 March 2024    |                 | 50.29           | 12.39         | 0.37     | 0.0  | 0.0       | 12.76 | 0.0  | 0.0        | 0.0  | 12.76       |
3341:       | 4  | 31   | 01 April 2024    |                 | 37.82           | 12.47         | 0.29     | 0.0  | 0.0       | 12.76 | 0.0  | 0.0        | 0.0  | 12.76       |
3342:       | 5  | 30   | 01 May 2024      |                 | 25.28           | 12.54         | 0.22     | 0.0  | 0.0       | 12.76 | 0.0  | 0.0        | 0.0  | 12.76       |
3343:       | 6  | 31   | 01 June 2024     |                 | 12.67           | 12.61         | 0.15     | 0.0  | 0.0       | 12.76 | 0.0  | 0.0        | 0.0  | 12.76       |
3344:       | 7  | 30   | 01 July 2024     |                 | 0.0             | 12.67         | 0.07     | 0.0  | 0.0       | 12.74 | 0.0  | 0.0        | 0.0  | 12.74       |
3345:     Then Loan Repayment schedule has the following data in Total row:
3346:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3347:       | 100.0         | 1.54     | 0.0  | 0.0       | 101.54 | 25.0 | 0.0        | 0.0  | 76.54       |
3348:     Then Loan Transactions tab has the following data:
3349:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3350:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3351:       | 01 January 2024  | Down Payment     | 25.0   | 25.0      | 0.0      | 0.0  | 0.0       | 75.0         | false    | false    |
3352: 
3353:     When Admin sets the business date to "01 February 2024"
3354:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 12.76 EUR transaction amount
3355:     Then Loan Repayment schedule has 7 periods, with the following data for periods:
3356:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3357:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3358:       | 1  | 0    | 01 January 2024  | 01 January 2024  | 75.0            | 25.0          | 0.0      | 0.0  | 0.0       | 25.0  | 25.0  | 0.0        | 0.0  | 0.0         |
3359:       | 2  | 31   | 01 February 2024 | 01 February 2024 | 62.68           | 12.32         | 0.44     | 0.0  | 0.0       | 12.76 | 12.76 | 0.0        | 0.0  | 0.0         |
3360:       | 3  | 29   | 01 March 2024    |                  | 50.29           | 12.39         | 0.37     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3361:       | 4  | 31   | 01 April 2024    |                  | 37.82           | 12.47         | 0.29     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3362:       | 5  | 30   | 01 May 2024      |                  | 25.28           | 12.54         | 0.22     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3363:       | 6  | 31   | 01 June 2024     |                  | 12.67           | 12.61         | 0.15     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3364:       | 7  | 30   | 01 July 2024     |                  | 0.0             | 12.67         | 0.07     | 0.0  | 0.0       | 12.74 | 0.0   | 0.0        | 0.0  | 12.74       |
3365:     Then Loan Repayment schedule has the following data in Total row:
3366:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3367:       | 100.0         | 1.54     | 0.0  | 0.0       | 101.54 | 37.76 | 0.0        | 0.0  | 63.78       |
3368:     Then Loan Transactions tab has the following data:
3369:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3370:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3371:       | 01 January 2024  | Down Payment     | 25.0   | 25.0      | 0.0      | 0.0  | 0.0       | 75.0         | false    | false    |
3372:       | 01 February 2024 | Repayment        | 12.76  | 12.32     | 0.44     | 0.0  | 0.0       | 62.68        | false    | false    |
3373: 
3374:     When Admin sets the business date to "15 March 2024"
3375:     When Admin runs inline COB job for Loan
3376:     Then Loan Repayment schedule has 7 periods, with the following data for periods:
3377:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3378:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3379:       | 1  | 0    | 01 January 2024  | 01 January 2024  | 75.0            | 25.0          | 0.0      | 0.0  | 0.0       | 25.0  | 25.0  | 0.0        | 0.0  | 0.0         |
3380:       | 2  | 31   | 01 February 2024 | 01 February 2024 | 62.68           | 12.32         | 0.44     | 0.0  | 0.0       | 12.76 | 12.76 | 0.0        | 0.0  | 0.0         |
3381:       | 3  | 29   | 01 March 2024    |                  | 50.29           | 12.39         | 0.37     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3382:       | 4  | 31   | 01 April 2024    |                  | 37.86           | 12.43         | 0.33     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3383:       | 5  | 30   | 01 May 2024      |                  | 25.32           | 12.54         | 0.22     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3384:       | 6  | 31   | 01 June 2024     |                  | 12.71           | 12.61         | 0.15     | 0.0  | 0.0       | 12.76 | 0.0   | 0.0        | 0.0  | 12.76       |
3385:       | 7  | 30   | 01 July 2024     |                  | 0.0             | 12.71         | 0.07     | 0.0  | 0.0       | 12.78 | 0.0   | 0.0        | 0.0  | 12.78       |
3386:     Then Loan Repayment schedule has the following data in Total row:
3387:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3388:       | 100.0         | 1.58     | 0.0  | 0.0       | 101.58 | 37.76 | 0.0        | 0.0  | 63.82       |
3389:     Then Loan Transactions tab has the following data:
3390:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3391:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3392:       | 01 January 2024  | Down Payment     | 25.0   | 25.0      | 0.0      | 0.0  | 0.0       | 75.0         | false    | false    |
3393:       | 01 February 2024 | Repayment        | 12.76  | 12.32     | 0.44     | 0.0  | 0.0       | 62.68        | false    | false    |
3394:       | 14 March 2024    | Accrual          | 0.96   | 0.0       | 0.96     | 0.0  | 0.0       | 0.0          | false    | false    |
3395: 
3396:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
3397:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
3398:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
3399:     Then Loan Repayment schedule has 10 periods, with the following data for periods:
3400:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3401:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3402:       | 1  | 0    | 01 January 2024   | 01 January 2024  | 75.0            | 25.0          | 0.0      | 0.0  | 0.0       | 25.0  | 25.0  | 0.0        | 0.0  | 0.0         |
3403:       | 2  | 31   | 01 February 2024  | 01 February 2024 | 62.68           | 12.32         | 0.44     | 0.0  | 0.0       | 12.76 | 12.76 | 0.0        | 0.0  | 0.0         |
3404:       | 3  | 29   | 01 March 2024     | 15 March 2024    | 62.68           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3405:       | 4  | 14   | 15 March 2024     | 15 March 2024    | 62.68           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3406:       | 5  | 17   | 01 April 2024     |                  | 52.23           | 10.45         | 0.19     | 0.0  | 0.0       | 10.64 | 0.0   | 0.0        | 0.0  | 10.64       |
3407:       | 6  | 30   | 01 May 2024       |                  | 41.78           | 10.45         | 0.19     | 0.0  | 0.0       | 10.64 | 0.0   | 0.0        | 0.0  | 10.64       |
3408:       | 7  | 31   | 01 June 2024      |                  | 31.33           | 10.45         | 0.19     | 0.0  | 0.0       | 10.64 | 0.0   | 0.0        | 0.0  | 10.64       |
3409:       | 8  | 30   | 01 July 2024      |                  | 20.88           | 10.45         | 0.19     | 0.0  | 0.0       | 10.64 | 0.0   | 0.0        | 0.0  | 10.64       |
3410:       | 9  | 31   | 01 August 2024    |                  | 10.43           | 10.45         | 0.19     | 0.0  | 0.0       | 10.64 | 0.0   | 0.0        | 0.0  | 10.64       |
3411:       | 10 | 31   | 01 September 2024 |                  | 0.0             | 10.43         | 0.19     | 0.0  | 0.0       | 10.62 | 0.0   | 0.0        | 0.0  | 10.62       |
3412:     Then Loan Repayment schedule has the following data in Total row:
3413:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3414:       | 100.0         | 1.58     | 0.0  | 0.0       | 101.58 | 37.76 | 0.0        | 0.0  | 63.82       |
3415:     Then Loan Transactions tab has the following data:
3416:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3417:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3418:       | 01 January 2024  | Down Payment     | 25.0   | 25.0      | 0.0      | 0.0  | 0.0       | 75.0         | false    | false    |
3419:       | 01 February 2024 | Repayment        | 12.76  | 12.32     | 0.44     | 0.0  | 0.0       | 62.68        | false    | false    |
3420:       | 14 March 2024    | Accrual          | 0.96   | 0.0       | 0.96     | 0.0  | 0.0       | 0.0          | false    | false    |
3421:       | 15 March 2024    | Re-age           | 63.82  | 62.68     | 1.14     | 0.0  | 0.0       | 0.0          | false    | false    |
3422: 
3423:     When Admin sets the business date to "15 April 2024"
3424:     When Admin runs inline COB job for Loan
3425:     Then Loan Transactions tab has the following data without accruals:
3426:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3427:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3428:       | 01 January 2024  | Down Payment     | 25.0   | 25.0      | 0.0      | 0.0  | 0.0       | 75.0         | false    | false    |
3429:       | 01 February 2024 | Repayment        | 12.76  | 12.32     | 0.44     | 0.0  | 0.0       | 62.68        | false    | false    |
3430:       | 15 March 2024    | Re-age           | 63.82  | 62.68     | 1.14     | 0.0  | 0.0       | 0.0          | false    | false    |
3431:     Then Loan Transactions tab has the following new accrual data:
3432:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3433:       | 14 March 2024    | Accrual            | 0.96   | 0.0       | 0.96     | 0.0  | 0.0       | 0.0          | false    | false    |
3434:       | 15 March 2024    | Accrual Adjustment | 0.52   | 0.0       | 0.52     | 0.0  | 0.0       | 0.0          | false    | false    |
3435:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3436:       | 17 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3437:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3438:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3439:       | 20 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3440:       | 21 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3441:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3442:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3443:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3444:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3445:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3446:       | 27 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3447:       | 28 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3448:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3449:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3450:       | 31 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3451:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3452:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3453:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3454:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3455:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3456:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3457:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3458:       | 12 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3459:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3460:     When Loan Pay-off is made on "15 April 2024"
3461:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
3462: 
3463:   @TestRailId:C4459 @AdvancedPaymentAllocation
3464:   Scenario: Verify Re-aging reversal on interest bearing loan - UC3: Interest handling: EQUAL_AMORTIZATION_PAYABLE_INTEREST
3465:     When Admin sets the business date to "01 January 2024"
3466:     And Admin creates a client with random data
3467:     And Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
3468:     And Admin creates a fully customized loan with the following data:
3469:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
3470:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
3471:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
3472:     And Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
3473:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3474:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
3475:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
3476:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3477:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3478:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3479:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3480:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3481:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
3482:     And Loan Repayment schedule has the following data in Total row:
3483:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3484:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
3485:     And Loan Transactions tab has the following data:
3486:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted |
3487:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |
3488:     When Admin sets the business date to "01 February 2024"
3489:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
3490:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3491:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3492:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3493:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3494:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3495:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3496:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3497:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3498:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
3499:     And Loan Repayment schedule has the following data in Total row:
3500:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3501:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
3502:     And Loan Transactions tab has the following data:
3503:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted |
3504:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |
3505:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    |
3506:     When Admin sets the business date to "15 March 2024"
3507:     When Admin runs inline COB job for Loan
3508:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3509:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3510:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3511:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3512:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3513:       | 3  | 31   | 01 April 2024    |                  | 50.47           | 16.58         | 0.43     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3514:       | 4  | 30   | 01 May 2024      |                  | 33.75           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3515:       | 5  | 31   | 01 June 2024     |                  | 16.94           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3516:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.94         | 0.1      | 0.0  | 0.0       | 17.04 | 0.0   | 0.0        | 0.0  | 17.04       |
3517:     And Loan Repayment schedule has the following data in Total row:
3518:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3519:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
3520:     And Loan Transactions tab has the following data:
3521:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3522:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3523:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3524:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3525:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3526:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3527: #   --- Re-age transaction ---
3528:     When Admin creates a Loan re-aging transaction with the following data:
3529:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
3530:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
3531:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3532:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3533:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3534:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3535:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3536:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3537:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3538:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3539:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3540:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3541:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3542:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
3543:     And Loan Repayment schedule has the following data in Total row:
3544:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3545:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
3546:     And Loan Transactions tab has the following data:
3547:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3548:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3549:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3550:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3551:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3552:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
3553: #   --- Reversal of re-age transaction ---
3554:     When Admin sets the business date to "01 April 2024"
3555:     When Admin runs inline COB job for Loan
3556:     And Admin successfully undo Loan re-aging transaction
3557:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3558:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3559:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3560:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3561:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3562:       | 3  | 31   | 01 April 2024    |                  | 50.53           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3563:       | 4  | 30   | 01 May 2024      |                  | 33.81           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3564:       | 5  | 31   | 01 June 2024     |                  | 17.0            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3565:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 17.0          | 0.1      | 0.0  | 0.0       | 17.1  | 0.0   | 0.0        | 0.0  | 17.1        |
3566:     And Loan Repayment schedule has the following data in Total row:
3567:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3568:       | 100.0         | 2.15     | 0.0  | 0.0       | 102.15 | 17.01 | 0.0        | 0.0  | 85.14       |
3569:     And Loan Transactions tab has the following data without accruals:
3570:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3571:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3572:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3573:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3574:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3575:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | true     | false    |
3576:     Then Loan Transactions tab has the following new accrual data:
3577:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3578:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3579:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
3580:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3581:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3582:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3583:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3584:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3585:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3586:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3587:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3588:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3589:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3590:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3591: 
3592:     When Admin sets the business date to "10 April 2024"
3593:     When Admin runs inline COB job for Loan
3594:     Then Loan Transactions tab has the following data without accruals:
3595:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3596:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3597:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3598:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3599:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3600:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | true     | false    |
3601:       | 01 April 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3602:     Then Loan Transactions tab has the following new accrual data:
3603:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3604:       | 01 April 2024    | Accrual            | 0.87   | 0.0       | 0.87     | 0.0  | 0.0       | 0.0          | false    | false    |
3605:       | 02 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3606:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3607:       | 04 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3608:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3609:       | 06 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3610:       | 07 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3611:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3612:       | 09 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3613:     When Loan Pay-off is made on "10 April 2024"
3614:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
3615: 
3616:   @TestRailId:C4460
3617:   Scenario: Verify Re-aging reversal on interest bearing loan - UC4.1: Interest handling: EQUAL_AMORTIZATION_FULL_INTEREST, re-aging is NOT the latest transaction on loan
3618:     When Admin sets the business date to "01 January 2024"
3619:     And Admin creates a client with random data
3620:     And Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
3621:     And Admin creates a fully customized loan with the following data:
3622:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
3623:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
3624:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
3625:     And Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
3626:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3627:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
3628:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
3629:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3630:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3631:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3632:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3633:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3634:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
3635:     And Loan Repayment schedule has the following data in Total row:
3636:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3637:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
3638:     And Loan Transactions tab has the following data:
3639:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3640:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |false    |
3641:     When Admin sets the business date to "01 February 2024"
3642:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
3643:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3644:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3645:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3646:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3647:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3648:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3649:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3650:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3651:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
3652:     And Loan Repayment schedule has the following data in Total row:
3653:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3654:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
3655:     And Loan Transactions tab has the following data:
3656:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3657:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |false    |
3658:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    |false    |
3659:     When Admin sets the business date to "15 March 2024"
3660:     When Admin runs inline COB job for Loan
3661:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3662:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3663:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3664:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3665:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3666:       | 3  | 31   | 01 April 2024    |                  | 50.47           | 16.58         | 0.43     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3667:       | 4  | 30   | 01 May 2024      |                  | 33.75           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3668:       | 5  | 31   | 01 June 2024     |                  | 16.94           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3669:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.94         | 0.1      | 0.0  | 0.0       | 17.04 | 0.0   | 0.0        | 0.0  | 17.04       |
3670:     And Loan Repayment schedule has the following data in Total row:
3671:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3672:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
3673:     And Loan Transactions tab has the following data:
3674:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3675:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3676:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3677:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3678:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3679:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3680: #   --- Re-age transaction ---
3681:     When Admin creates a Loan re-aging transaction with the following data:
3682:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
3683:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
3684:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3685:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3686:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3687:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3688:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3689:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3690:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3691:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3692:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3693:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3694:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3695:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3696:     And Loan Repayment schedule has the following data in Total row:
3697:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3698:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
3699:     And Loan Transactions tab has the following data:
3700:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3701:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3702:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3703:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3704:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3705:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
3706: #  --- Transaction after re-aging ---
3707:     When Admin sets the business date to "16 March 2024"
3708:     When Admin runs inline COB job for Loan
3709:     And Customer makes "AUTOPAY" repayment on "16 March 2024" with 14.18 EUR transaction amount
3710:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3711:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3712:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3713:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3714:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3715:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3716:       | 4  | 17   | 01 April 2024     | 16 March 2024    | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 14.18 | 14.18      | 0.0  | 0.0         |
3717:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3718:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3719:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3720:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3721:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3722:     And Loan Repayment schedule has the following data in Total row:
3723:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3724:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 31.19 | 14.18      | 0.0  | 70.9        |
3725:     And Loan Transactions tab has the following data:
3726:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3727:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3728:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3729:       | 01 February 2024 | Accrual Activity   | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3730:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3731:       | 15 March 2024    | Re-age             | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
3732:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
3733:       | 16 March 2024    | Repayment          | 14.18  | 13.93     | 0.25     | 0.0  | 0.0       | 69.64        | false    | false    |
3734: #   --- Reversal of re-age transaction ---
3735:     When Admin sets the business date to "01 April 2024"
3736:     When Admin runs inline COB job for Loan
3737:     And Admin successfully undo Loan re-aging transaction
3738:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3739:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late  | Outstanding |
3740:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |       |             |
3741:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0   | 0.0         |
3742:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 14.18 | 0.0        | 14.18 | 2.83        |
3743:       | 3  | 31   | 01 April 2024    |                  | 50.49           | 16.56         | 0.45     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0   | 17.01       |
3744:       | 4  | 30   | 01 May 2024      |                  | 33.77           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0   | 17.01       |
3745:       | 5  | 31   | 01 June 2024     |                  | 16.96           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0   | 17.01       |
3746:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.96         | 0.1      | 0.0  | 0.0       | 17.06 | 0.0   | 0.0        | 0.0   | 17.06       |
3747:     And Loan Repayment schedule has the following data in Total row:
3748:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late  | Outstanding |
3749:       | 100.0         | 2.11     | 0.0  | 0.0       | 102.11 | 31.19 | 0.0        | 14.18 | 70.92       |
3750:     And Loan Transactions tab has the following data without accruals:
3751:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3752:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3753:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3754:       | 01 February 2024 | Accrual Activity   | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3755:       | 01 March 2024    | Accrual Activity   | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3756:       | 15 March 2024    | Re-age             | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | true     | false    |
3757:       | 16 March 2024    | Repayment          | 14.18  | 13.69     | 0.49     | 0.0  | 0.0       | 69.88        | false    | true     |
3758:     Then Loan Transactions tab has the following new accrual data:
3759:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3760:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3761:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
3762:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3763:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3764:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3765:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3766:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3767:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3768:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3769:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3770:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3771:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3772:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3773:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3774:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3775:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3776:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3777:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3778: 
3779:     When Admin sets the business date to "15 April 2024"
3780:     When Admin runs inline COB job for Loan
3781:     And Loan Transactions tab has the following data without accruals:
3782:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3783:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3784:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3785:       | 01 February 2024 | Accrual Activity   | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3786:       | 01 March 2024    | Accrual Activity   | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3787:       | 15 March 2024    | Re-age             | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | true     | false    |
3788:       | 16 March 2024    | Repayment          | 14.18  | 13.69     | 0.49     | 0.0  | 0.0       | 69.88        | false    | true     |
3789:       | 01 April 2024    | Accrual Activity   | 0.45   | 0.0       | 0.45     | 0.0  | 0.0       | 0.0          | false    | false    |
3790:     Then Loan Transactions tab has the following new accrual data:
3791:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3792:       | 01 April 2024    | Accrual            | 0.7    | 0.0       | 0.7      | 0.0  | 0.0       | 0.0          | false    | false    |
3793:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3794:       | 03 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3795:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3796:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3797:       | 06 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3798:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3799:       | 08 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3800:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3801:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3802:       | 11 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3803:       | 12 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3804:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3805:       | 14 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
3806:     When Loan Pay-off is made on "15 April 2024"
3807:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
3808: 
3809:   @TestRailId:C4461 @AdvancedPaymentAllocation
3810:   Scenario: Verify Re-aging on interest bearing loan - equal amortization + payable outstanding interest - reverse-repay, backdated repayment - UC8
3811:     When Admin sets the business date to "01 January 2024"
3812:     When Admin creates a client with random data
3813:     When Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
3814:     When Admin creates a fully customized loan with the following data:
3815:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
3816:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                       | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
3817:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
3818:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
3819:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3820:       | Nr | Days | Date            | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
3821:       |    |      | 01 January 2024 |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
3822:       | 1  | 31   | 01 February 2024|           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3823:       | 2  | 29   | 01 March 2024   |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3824:       | 3  | 31   | 01 April 2024   |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3825:       | 4  | 30   | 01 May 2024     |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3826:       | 5  | 31   | 01 June 2024    |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3827:       | 6  | 30   | 01 July 2024    |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
3828:     Then Loan Repayment schedule has the following data in Total row:
3829:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3830:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
3831:     Then Loan Transactions tab has the following data:
3832:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted |
3833:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |
3834:     When Admin sets the business date to "01 February 2024"
3835:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
3836:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3837:       | Nr | Days | Date            | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3838:       |    |      | 01 January 2024 |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3839:       | 1  | 31   | 01 February 2024| 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3840:       | 2  | 29   | 01 March 2024   |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3841:       | 3  | 31   | 01 April 2024   |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3842:       | 4  | 30   | 01 May 2024     |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3843:       | 5  | 31   | 01 June 2024    |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3844:       | 6  | 30   | 01 July 2024    |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
3845:     Then Loan Repayment schedule has the following data in Total row:
3846:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3847:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
3848:     Then Loan Transactions tab has the following data:
3849:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted |
3850:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |
3851:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    |
3852:     When Admin sets the business date to "15 March 2024"
3853:     When Admin runs inline COB job for Loan
3854:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
3855:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
3856:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
3857:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3858:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3859:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3860:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3861:       | 2  | 29   | 01 March 2024    | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3862:       | 3  | 14   | 15 March 2024    | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3863:       | 4  | 17   | 01 April 2024    |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3864:       | 5  | 30   | 01 May 2024      |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3865:       | 6  | 31   | 01 June 2024     |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3866:       | 7  | 30   | 01 July 2024     |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3867:       | 8  | 31   | 01 August 2024   |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
3868:       | 9  | 31   | 01 September 2024|                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
3869:     Then Loan Repayment schedule has the following data in Total row:
3870:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3871:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
3872:     Then Loan Transactions tab has the following data:
3873:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3874:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3875:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3876:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3877:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3878:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
3879:     When Admin sets the business date to "01 April 2024"
3880:     When Admin runs inline COB job for Loan
3881:     And Customer makes "AUTOPAY" repayment on "01 March 2024" with 17.01 EUR transaction amount
3882:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3883:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3884:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3885:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3886:       | 2  | 29   | 01 March 2024    | 01 March 2024    | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3887:       | 3  | 14   | 15 March 2024    | 15 March 2024    | 67.05           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3888:       | 4  | 17   | 01 April 2024    |                  | 55.88           | 11.17         | 0.03     | 0.0  | 0.0       | 11.2  | 0.0   | 0.0        | 0.0  | 11.2        |
3889:       | 5  | 30   | 01 May 2024      |                  | 44.71           | 11.17         | 0.03     | 0.0  | 0.0       | 11.2  | 0.0   | 0.0        | 0.0  | 11.2        |
3890:       | 6  | 31   | 01 June 2024     |                  | 33.54           | 11.17         | 0.03     | 0.0  | 0.0       | 11.2  | 0.0   | 0.0        | 0.0  | 11.2        |
3891:       | 7  | 30   | 01 July 2024     |                  | 22.37           | 11.17         | 0.03     | 0.0  | 0.0       | 11.2  | 0.0   | 0.0        | 0.0  | 11.2        |
3892:       | 8  | 31   | 01 August 2024   |                  | 11.2            | 11.17         | 0.03     | 0.0  | 0.0       | 11.2  | 0.0   | 0.0        | 0.0  | 11.2        |
3893:       | 9  | 31   | 01 September 2024|                  | 0.0             | 11.2          | 0.03     | 0.0  | 0.0       | 11.23 | 0.0   | 0.0        | 0.0  | 11.23       |
3894:     Then Loan Repayment schedule has the following data in Total row:
3895:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3896:       | 100.0         | 1.25     | 0.0  | 0.0       | 101.25 | 34.02 | 0.0        | 0.0  | 67.23       |
3897:     Then Loan Transactions tab has the following data without accruals:
3898:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3899:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3900:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3901:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3902:       | 01 March 2024    | Repayment        | 17.01  | 16.52     | 0.49     | 0.0  | 0.0       | 67.05        | false    | false    |
3903:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3904:       | 15 March 2024    | Re-age           | 67.23  | 67.05     | 0.18     | 0.0  | 0.0       | 0.0          | false    | true     |
3905:     Then Loan Transactions tab has the following new accrual data:
3906:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3907:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
3908:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
3909:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3910:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3911:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3912:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3913:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3914:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3915:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3916:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3917:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3918:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3919:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3920: 
3921:     When Admin sets the business date to "15 April 2024"
3922:     When Admin runs inline COB job for Loan
3923:     And Loan Transactions tab has the following data without accruals:
3924:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3925:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
3926:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
3927:       | 01 February 2024 | Accrual Activity   | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
3928:       | 01 March 2024    | Repayment          | 17.01  | 16.52     | 0.49     | 0.0  | 0.0       | 67.05        | false    | false    |
3929:       | 01 March 2024    | Accrual Activity   | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
3930:       | 15 March 2024    | Re-age             | 67.23  | 67.05     | 0.18     | 0.0  | 0.0       | 0.0          | false    | true     |
3931:       | 01 April 2024    | Accrual Activity   | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
3932:     Then Loan Transactions tab has the following new accrual data:
3933:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
3934:       | 01 April 2024    | Accrual            | 0.41   | 0.0       | 0.41     | 0.0  | 0.0       | 0.0          | false    | false    |
3935:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
3936:     When Loan Pay-off is made on "15 April 2024"
3937:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
3938: 
3939:   @TestRailId:C4462 @AdvancedPaymentAllocation
3940:   Scenario: Verify Re-aging on interest bearing loan - equal amortization + full outstanding interest - reverse-repay, reversal of backdated repayment - UC8.1
3941:     When Admin sets the business date to "01 January 2024"
3942:     When Admin creates a client with random data
3943:     When Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
3944:     When Admin creates a fully customized loan with the following data:
3945:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
3946:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                       | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
3947:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
3948:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
3949:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3950:       | Nr | Days | Date            | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
3951:       |    |      | 01 January 2024 |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
3952:       | 1  | 31   | 01 February 2024|           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3953:       | 2  | 29   | 01 March 2024   |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3954:       | 3  | 31   | 01 April 2024   |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3955:       | 4  | 30   | 01 May 2024     |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3956:       | 5  | 31   | 01 June 2024    |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
3957:       | 6  | 30   | 01 July 2024    |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
3958:     Then Loan Repayment schedule has the following data in Total row:
3959:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
3960:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
3961:     Then Loan Transactions tab has the following data:
3962:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted |
3963:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |
3964:     When Admin sets the business date to "01 February 2024"
3965:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
3966:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
3967:       | Nr | Days | Date            | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3968:       |    |      | 01 January 2024 |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3969:       | 1  | 31   | 01 February 2024| 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3970:       | 2  | 29   | 01 March 2024   |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3971:       | 3  | 31   | 01 April 2024   |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3972:       | 4  | 30   | 01 May 2024     |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3973:       | 5  | 31   | 01 June 2024    |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
3974:       | 6  | 30   | 01 July 2024    |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
3975:     Then Loan Repayment schedule has the following data in Total row:
3976:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
3977:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
3978:     Then Loan Transactions tab has the following data:
3979:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted |
3980:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    |
3981:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    |
3982:     When Admin sets the business date to "15 March 2024"
3983:     When Admin runs inline COB job for Loan
3984:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
3985:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
3986:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
3987:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
3988:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
3989:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
3990:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
3991:       | 2  | 29   | 01 March 2024    | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3992:       | 3  | 14   | 15 March 2024    | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
3993:       | 4  | 17   | 01 April 2024    |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3994:       | 5  | 30   | 01 May 2024      |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3995:       | 6  | 31   | 01 June 2024     |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3996:       | 7  | 30   | 01 July 2024     |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3997:       | 8  | 31   | 01 August 2024   |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3998:       | 9  | 31   | 01 September 2024|                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
3999:     Then Loan Repayment schedule has the following data in Total row:
4000:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4001:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
4002:     Then Loan Transactions tab has the following data:
4003:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4004:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4005:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4006:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
4007:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4008:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4009:     When Admin sets the business date to "01 April 2024"
4010:     When Admin runs inline COB job for Loan
4011:     And Customer makes "AUTOPAY" repayment on "01 March 2024" with 17.01 EUR transaction amount
4012:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4013:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4014:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4015:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4016:       | 2  | 29   | 01 March 2024    | 01 March 2024    | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4017:       | 3  | 14   | 15 March 2024    | 15 March 2024    | 67.05           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4018:       | 4  | 17   | 01 April 2024    |                  | 55.87           | 11.18         | 0.16     | 0.0  | 0.0       | 11.34  | 0.0  | 0.0        | 0.0  | 11.34       |
4019:       | 5  | 30   | 01 May 2024      |                  | 44.69           | 11.18         | 0.16     | 0.0  | 0.0       | 11.34  | 0.0  | 0.0        | 0.0  | 11.34       |
4020:       | 6  | 31   | 01 June 2024     |                  | 33.51           | 11.18         | 0.16     | 0.0  | 0.0       | 11.34  | 0.0  | 0.0        | 0.0  | 11.34       |
4021:       | 7  | 30   | 01 July 2024     |                  | 22.33           | 11.18         | 0.16     | 0.0  | 0.0       | 11.34  | 0.0  | 0.0        | 0.0  | 11.34       |
4022:       | 8  | 31   | 01 August 2024   |                  | 11.15           | 11.18         | 0.16     | 0.0  | 0.0       | 11.34  | 0.0  | 0.0        | 0.0  | 11.34       |
4023:       | 9  | 31   | 01 September 2024|                  | 0.0             | 11.15         | 0.18     | 0.0  | 0.0       | 11.33  | 0.0  | 0.0        | 0.0  | 11.33       |
4024:     Then Loan Repayment schedule has the following data in Total row:
4025:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4026:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 34.02 | 0.0        | 0.0  | 68.03       |
4027:     Then Loan Transactions tab has the following data without accruals:
4028:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4029:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4030:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4031:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
4032:       | 01 March 2024    | Repayment        | 17.01  | 16.52     | 0.49     | 0.0  | 0.0       | 67.05        | false    | false    |
4033:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
4034:       | 15 March 2024    | Re-age           | 68.03  | 67.05     | 0.98     | 0.0  | 0.0       | 0.0          | false    | true     |
4035:     Then Loan Transactions tab has the following new accrual data:
4036:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4037:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4038:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
4039:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4040:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4041:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4042:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4043:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4044:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4045:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4046:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4047:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4048:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4049:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4050:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4051:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4052:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4053:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4054:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4055: 
4056:     When Customer undo "2"th transaction made on "01 March 2024"
4057:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4058:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4059:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4060:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4061:       | 2  | 29   | 01 March 2024    | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4062:       | 3  | 14   | 15 March 2024    | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4063:       | 4  | 17   | 01 April 2024    |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4064:       | 5  | 30   | 01 May 2024      |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4065:       | 6  | 31   | 01 June 2024     |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4066:       | 7  | 30   | 01 July 2024     |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4067:       | 8  | 31   | 01 August 2024   |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4068:       | 9  | 31   | 01 September 2024|                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4069:     Then Loan Repayment schedule has the following data in Total row:
4070:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4071:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
4072:     Then Loan Transactions tab has the following data without accruals:
4073:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4074:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4075:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4076:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
4077:       | 01 March 2024    | Repayment        | 17.01  | 16.52     | 0.49     | 0.0  | 0.0       | 67.05        | true     | false    |
4078:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | true     |
4079:     Then Loan Transactions tab has no new accrual data
4080: 
4081:     When Admin sets the business date to "15 April 2024"
4082:     When Admin runs inline COB job for Loan
4083:     And Loan Transactions tab has the following data without accruals:
4084:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4085:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4086:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4087:       | 01 February 2024 | Accrual Activity   | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
4088:       | 01 March 2024    | Repayment          | 17.01  | 16.52     | 0.49     | 0.0  | 0.0       | 67.05        | true     | false    |
4089:       | 15 March 2024    | Re-age             | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | true     |
4090:       | 01 April 2024    | Accrual Activity   | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
4091:     Then Loan Transactions tab has the following new accrual data:
4092:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4093:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4094:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4095:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4096:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4097:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4098:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4099:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4100:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4101:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4102:       | 12 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4103:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4104:       | 14 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4105:     When Loan Pay-off is made on "15 April 2024"
4106:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
4107: 
4108:   @TestRailId:C4463 @AdvancedPaymentAllocation
4109:   Scenario: Verify Loan re-aging trn with 2nd disb and partial chargeback(with custom pmnt alloc) after re-age - interest bearing multidisb loan with equal amortization; outstanding payable interest - UC2
4110:     When Admin sets the business date to "01 January 2024"
4111:     When Admin creates a client with random data
4112:     When Admin creates a fully customized loan with the following data:
4113:       | LoanProduct                                                                            | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
4114:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALC_DAILY_MULTIDISBURSE_CHARGEBACK | 01 January 2024   | 150            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
4115:     And Admin successfully approves the loan on "01 January 2024" with "150" amount and expected disbursement date on "01 January 2024"
4116:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
4117:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4118:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
4119:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
4120:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4121:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4122:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4123:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4124:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4125:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
4126:     Then Loan Repayment schedule has the following data in Total row:
4127:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
4128:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
4129:     Then Loan Transactions tab has the following data:
4130:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4131:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4132: 
4133:     When Admin sets the business date to "01 February 2024"
4134:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
4135:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4136:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4137:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4138:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4139:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4140:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4141:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4142:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4143:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
4144:     Then Loan Repayment schedule has the following data in Total row:
4145:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4146:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
4147:     Then Loan Transactions tab has the following data:
4148:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4149:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4150:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4151: 
4152:     When Admin sets the business date to "15 March 2024"
4153:     When Admin runs inline COB job for Loan
4154:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
4155:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
4156:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
4157:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4158:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4159:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4160:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4161:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4162:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4163:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4164:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4165:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4166:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4167:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4168:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
4169:     Then Loan Repayment schedule has the following data in Total row:
4170:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4171:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
4172:     Then Loan Transactions tab has the following data:
4173:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4174:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4175:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4176:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4177:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
4178: 
4179:     When Admin sets the business date to "01 April 2024"
4180:     When Admin runs inline COB job for Loan
4181:     When Admin successfully disburse the loan on "01 April 2024" with "50" EUR transaction amount
4182:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4183:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4184:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4185:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4186:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4187:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4188:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4189:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4190:       | 5  | 30   | 01 May 2024       |                  | 95.71           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4191:       | 6  | 31   | 01 June 2024      |                  | 71.78           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4192:       | 7  | 30   | 01 July 2024      |                  | 47.85           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4193:       | 8  | 31   | 01 August 2024    |                  | 23.92           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4194:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 23.92         | 0.11     | 0.0  | 0.0       | 24.03 | 0.0   | 0.0        | 0.0  | 24.03       |
4195:     Then Loan Repayment schedule has the following data in Total row:
4196:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4197:       | 150.0        | 1.29     | 0.0  | 0.0       | 151.29  | 17.01 | 0.0        | 0.0  | 134.28      |
4198:     Then Loan Transactions tab has the following data without accruals:
4199:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4200:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4201:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4202:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
4203:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4204:     Then Loan Transactions tab has the following new accrual data:
4205:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4206:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4207:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
4208:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4209:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4210:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4211:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4212:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4213:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4214:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4215:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4216:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4217:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4218:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4219: 
4220:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
4221:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4222:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4223:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4224:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4225:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4226:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4227:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4228:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4229:       | 5  | 30   | 01 May 2024       |                  | 95.71           | 40.36         | 0.7      | 0.0  | 0.0       | 41.06 | 0.0   | 0.0        | 0.0  | 41.06       |
4230:       | 6  | 31   | 01 June 2024      |                  | 71.78           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4231:       | 7  | 30   | 01 July 2024      |                  | 47.85           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4232:       | 8  | 31   | 01 August 2024    |                  | 23.92           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4233:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 23.92         | 0.11     | 0.0  | 0.0       | 24.03 | 0.0   | 0.0        | 0.0  | 24.03       |
4234:     Then Loan Repayment schedule has the following data in Total row:
4235:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4236:       | 166.43        | 1.87     | 0.0  | 0.0       | 168.3  | 17.01 | 0.0        | 0.0  | 151.29      |
4237:     Then Loan Transactions tab has the following data without accruals:
4238:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4239:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4240:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4241:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
4242:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4243:       | 01 April 2024    | Chargeback       | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 150.0        | false    | false    |
4244:     Then Loan Transactions tab has no new accrual data
4245: 
4246: # --- undo re-age --- #
4247:     When Admin successfully undo Loan re-aging transaction
4248:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4249:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4250:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4251:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4252:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4253:       | 3  | 31   | 01 April 2024    |                  | 50.53           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4254:       |    |      | 01 April 2024    |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4255:       | 4  | 30   | 01 May 2024      |                  | 67.34           | 49.62         | 1.26     | 0.0  | 0.0       | 50.88 | 0.0   | 0.0        | 0.0  | 50.88       |
4256:       | 5  | 31   | 01 June 2024     |                  | 33.86           | 33.48         | 0.39     | 0.0  | 0.0       | 33.87 | 0.0   | 0.0        | 0.0  | 33.87       |
4257:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 33.86         | 0.2      | 0.0  | 0.0       | 34.06 | 0.0   | 0.0        | 0.0  | 34.06       |
4258:     Then Loan Repayment schedule has the following data in Total row:
4259:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4260:       | 166.43        | 3.41     | 0.0  | 0.0       | 169.84 | 17.01 | 0.0        | 0.0  | 152.83     |
4261:     Then Loan Transactions tab has the following data without accruals:
4262:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4263:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4264:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4265:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | true     | false    |
4266:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4267:       | 01 April 2024    | Chargeback       | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 150.0        | false    | false    |
4268:     Then Loan Transactions tab has no new accrual data
4269: 
4270:     When Admin sets the business date to "15 April 2024"
4271:     When Admin runs inline COB job for Loan
4272:     And Loan Transactions tab has the following data without accruals:
4273:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4274:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4275:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4276:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | true     | false    |
4277:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4278:       | 01 April 2024    | Chargeback       | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 150.0        | false    | false    |
4279:     Then Loan Transactions tab has the following new accrual data:
4280:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4281:       | 01 April 2024    | Accrual            | 0.87   | 0.0       | 0.87     | 0.0  | 0.0       | 0.0          | false    | false    |
4282:       | 02 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4283:       | 03 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4284:       | 04 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4285:       | 05 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4286:       | 06 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4287:       | 07 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4288:       | 08 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4289:       | 09 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4290:       | 10 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4291:       | 11 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4292:       | 12 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4293:       | 13 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4294:       | 14 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4295:     When Loan Pay-off is made on "15 April 2024"
4296:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
4297: 
4298:   @TestRailId:C4464 @AdvancedPaymentAllocation
4299:   Scenario: Verify Loan re-aging trn with 2nd disb and charge after re-age and undo re-age - interest bearing multidisb loan with equal amortization; outstanding FULL interest - UC3
4300:     When Admin sets the business date to "01 January 2024"
4301:     When Admin creates a client with random data
4302:     When Admin creates a fully customized loan with the following data:
4303:       | LoanProduct                                                                                       | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
4304:       | LP2_ADV_PYMNT_INTEREST_DAILY_RECALC_EMI_360_30_MULTIDISB_APPROVED_OVER_APPLIED_CAPITALIZED_INCOME | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
4305:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
4306:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
4307:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4308:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
4309:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
4310:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4311:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4312:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4313:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4314:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4315:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
4316:     Then Loan Repayment schedule has the following data in Total row:
4317:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
4318:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
4319:     Then Loan Transactions tab has the following data:
4320:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4321:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4322: 
4323:     When Admin sets the business date to "01 February 2024"
4324:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
4325:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4326:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4327:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4328:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4329:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4330:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4331:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4332:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4333:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
4334:     Then Loan Repayment schedule has the following data in Total row:
4335:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4336:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
4337:     Then Loan Transactions tab has the following data:
4338:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4339:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4340:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4341: 
4342:     When Admin sets the business date to "15 March 2024"
4343:     When Admin runs inline COB job for Loan
4344:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
4345:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
4346:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
4347:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4348:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4349:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4350:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4351:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4352:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4353:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4354:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4355:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4356:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4357:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4358:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4359:     Then Loan Repayment schedule has the following data in Total row:
4360:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4361:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
4362:     Then Loan Transactions tab has the following data:
4363:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4364:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4365:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4366:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4367:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4368: 
4369:     When Admin sets the business date to "01 April 2024"
4370:     When Admin runs inline COB job for Loan
4371:     When Admin successfully disburse the loan on "01 April 2024" with "50" EUR transaction amount
4372:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4373:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4374:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4375:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4376:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4377:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4378:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4379:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4380:       | 5  | 30   | 01 May 2024       |                  | 95.71           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4381:       | 6  | 31   | 01 June 2024      |                  | 71.78           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4382:       | 7  | 30   | 01 July 2024      |                  | 47.85           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4383:       | 8  | 31   | 01 August 2024    |                  | 23.92           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4384:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 23.92         | 0.26     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4385:     Then Loan Repayment schedule has the following data in Total row:
4386:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4387:       | 150.0         | 2.09     | 0.0  | 0.0       | 152.09 | 17.01 | 0.0        | 0.0  | 135.08      |
4388:     Then Loan Transactions tab has the following data without accruals:
4389:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4390:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4391:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4392:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4393:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4394:     Then Loan Transactions tab has the following new accrual data:
4395:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4396:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4397:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
4398:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4399:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4400:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4401:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4402:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4403:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4404:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4405:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4406:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4407:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4408:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4409:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4410:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4411:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4412:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4413:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4414: 
4415:     When Admin adds "LOAN_NSF_FEE" due date charge with "05 October 2024" due date and 10 EUR transaction amount
4416:     Then Loan Repayment schedule has 10 periods, with the following data for periods:
4417:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4418:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4419:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4420:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4421:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4422:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4423:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4424:       | 5  | 30   | 01 May 2024       |                  | 95.71           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4425:       | 6  | 31   | 01 June 2024      |                  | 71.78           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4426:       | 7  | 30   | 01 July 2024      |                  | 47.85           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4427:       | 8  | 31   | 01 August 2024    |                  | 23.92           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4428:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 23.92         | 0.26     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4429:       | 10 | 34   | 05 October 2024   |                  |  0.0            | 0.0           | 0.0      | 0.0  | 10.0      | 10.0  | 0.0   | 0.0        | 0.0  | 10.0        |
4430:     Then Loan Repayment schedule has the following data in Total row:
4431:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4432:       | 150.0         | 2.09     | 0.0  | 10.0      | 162.09 | 17.01 | 0.0        | 0.0  | 145.08      |
4433:     Then Loan Transactions tab has the following data without accruals:
4434:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4435:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4436:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4437:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4438:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4439:     Then Loan Transactions tab has no new accrual data
4440:     Then Loan Charges tab has the following data:
4441:       | Name    | isPenalty | Payment due at       | Due as of       | Calculation type | Due  | Paid | Waived | Outstanding |
4442:       | NSF fee | true      | Specified due date   | 05 October 2024 | Flat             | 10.0 | 0.0  | 0.0    | 10.0        |
4443: 
4444:     When Admin sets the business date to "15 April 2024"
4445:     When Admin runs inline COB job for Loan
4446:     And Loan Transactions tab has the following data without accruals:
4447:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4448:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4449:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4450:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4451:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4452:     Then Loan Transactions tab has the following new accrual data:
4453:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4454:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4455:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4456:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4457:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4458:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4459:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4460:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4461:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4462:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4463:       | 12 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4464:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4465:       | 14 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4466:     When Loan Pay-off is made on "15 April 2024"
4467:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
4468: 
4469:   @TestRailId:C4465 @AdvancedPaymentAllocation
4470:   Scenario: Verify Loan re-aging trn with backdated re-aging before 2nd disb - interest bearing multidisb loan with equal amortization; outstanding FULL interest - UC6
4471:     When Admin sets the business date to "01 January 2024"
4472:     When Admin creates a client with random data
4473:     When Admin creates a fully customized loan with the following data:
4474:       | LoanProduct                                                                            | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
4475:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALC_DAILY_MULTIDISBURSE_CHARGEBACK | 01 January 2024   | 150            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
4476:     And Admin successfully approves the loan on "01 January 2024" with "150" amount and expected disbursement date on "01 January 2024"
4477:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
4478:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4479:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
4480:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
4481:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4482:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4483:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4484:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4485:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4486:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
4487:     Then Loan Repayment schedule has the following data in Total row:
4488:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
4489:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
4490:     Then Loan Transactions tab has the following data:
4491:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4492:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4493: 
4494:     When Admin sets the business date to "01 February 2024"
4495:     When Admin runs inline COB job for Loan
4496:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
4497:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4498:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4499:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4500:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4501:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4502:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4503:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4504:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4505:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
4506:     Then Loan Repayment schedule has the following data in Total row:
4507:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4508:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
4509:     Then Loan Transactions tab has the following data:
4510:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4511:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4512:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
4513:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4514: 
4515:     When Admin sets the business date to "01 April 2024"
4516:     When Admin runs inline COB job for Loan
4517:     When Admin successfully disburse the loan on "01 April 2024" with "50" EUR transaction amount
4518:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4519:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4520:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4521:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4522:       | 2  | 29   | 01 March 2024     |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4523:       | 3  | 31   | 01 April 2024     |                  | 50.53           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4524:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4525:       | 4  | 30   | 01 May 2024       |                  | 67.25           | 33.28         | 0.59     | 0.0  | 0.0       | 33.87 | 0.0   | 0.0        | 0.0  | 33.87       |
4526:       | 5  | 31   | 01 June 2024      |                  | 33.77           | 33.48         | 0.39     | 0.0  | 0.0       | 33.87 | 0.0   | 0.0        | 0.0  | 33.87       |
4527:       | 6  | 30   | 01 July 2024      |                  |  0.0            | 33.77         | 0.2      | 0.0  | 0.0       | 33.97 | 0.0   | 0.0        | 0.0  | 33.97       |
4528:     Then Loan Repayment schedule has the following data in Total row:
4529:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4530:       | 150.0         | 2.74     | 0.0  | 0.0       | 152.74 | 17.01 | 0.0        | 0.0  | 135.73      |
4531:     Then Loan Transactions tab has the following data without accruals:
4532:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4533:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4534:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4535:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4536:     Then Loan Transactions tab has the following new accrual data:
4537:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4538:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
4539:       | 01 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4540:       | 02 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4541:       | 03 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4542:       | 04 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4543:       | 05 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4544:       | 06 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4545:       | 07 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4546:       | 08 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4547:       | 09 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4548:       | 10 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4549:       | 11 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4550:       | 12 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4551:       | 13 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4552:       | 14 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4553:       | 15 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4554:       | 16 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4555:       | 17 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4556:       | 18 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4557:       | 19 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4558:       | 20 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4559:       | 21 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4560:       | 22 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4561:       | 23 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4562:       | 24 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4563:       | 25 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4564:       | 26 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4565:       | 27 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4566:       | 28 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4567:       | 29 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4568:       | 01 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4569:       | 02 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4570:       | 03 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4571:       | 04 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4572:       | 05 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4573:       | 06 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4574:       | 07 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4575:       | 08 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4576:       | 09 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4577:       | 10 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4578:       | 11 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4579:       | 12 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4580:       | 13 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4581:       | 14 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4582:       | 15 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4583:       | 16 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4584:       | 17 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4585:       | 18 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4586:       | 19 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4587:       | 20 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4588:       | 21 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4589:       | 22 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4590:       | 23 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4591:       | 24 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4592:       | 25 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4593:       | 26 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4594:       | 27 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4595:       | 28 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4596:       | 29 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4597:       | 30 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4598:       | 31 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4599: 
4600: # --- backdated re-aging ---#
4601:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
4602:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
4603:       | 1               | MONTHS        | 15 March 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
4604:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4605:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4606:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4607:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4608:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4609:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4610:       | 4  | 0    | 15 March 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4611:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4612:       | 5  | 31   | 15 April 2024     |                  | 95.71           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4613:       | 6  | 30   | 15 May 2024       |                  | 71.78           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4614:       | 7  | 31   | 15 June 2024      |                  | 47.85           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4615:       | 8  | 30   | 15 July 2024      |                  | 23.92           | 23.93         | 0.25     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4616:       | 9  | 31   | 15 August 2024    |                  |  0.0            | 23.92         | 0.26     | 0.0  | 0.0       | 24.18 | 0.0   | 0.0        | 0.0  | 24.18       |
4617:     Then Loan Repayment schedule has the following data in Total row:
4618:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4619:       | 150.0         | 2.09     | 0.0  | 0.0       | 152.09 | 17.01 | 0.0        | 0.0  | 135.08     |
4620:     Then Loan Transactions tab has the following data without accruals:
4621:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4622:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4623:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4624:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4625:       | 01 April 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4626:     Then Loan Transactions tab has no new accrual data
4627: 
4628: # --- undo last disbursement --- #
4629:     When Admin successfully undo last disbursal
4630:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4631:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4632:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4633:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4634:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4635:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4636:       | 4  | 0    | 15 March 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4637:       | 5  | 31   | 15 April 2024     |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4638:       | 6  | 30   | 15 May 2024       |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4639:       | 7  | 31   | 15 June 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4640:       | 8  | 30   | 15 July 2024      |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4641:       | 9  | 31   | 15 August 2024    |                  |  0.0            | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
4642:     Then Loan Repayment schedule has the following data in Total row:
4643:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4644:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08      |
4645:     Then Loan Transactions tab has the following data without accruals:
4646:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4647:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4648:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4649:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4650:     Then Loan Transactions tab has no new accrual data
4651: 
4652:     When Admin sets the business date to "15 April 2024"
4653:     When Admin runs inline COB job for Loan
4654:     Then Loan Transactions tab has the following data without accruals:
4655:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4656:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4657:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4658:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4659:     Then Loan Transactions tab has the following new accrual data:
4660:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4661:       | 01 April 2024    | Accrual Adjustment | 0.57   | 0.0       | 0.57     | 0.0  | 0.0       | 0.0          | false    | false    |
4662:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4663:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4664:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4665:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4666:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4667:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4668:       | 10 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4669:       | 11 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4670:       | 12 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4671:       | 14 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4672:     When Loan Pay-off is made on "15 April 2024"
4673:     Then Loan Transactions tab has the following data without accruals:
4674:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4675:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4676:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4677:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4678:       | 15 April 2024    | Repayment        | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
4679:     Then Loan Transactions tab has the following new accrual data:
4680:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4681:       | 15 April 2024    | Accrual            | 1.02   | 0.0       | 1.02     | 0.0  | 0.0       | 0.0          | false    | false    |
4682:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
4683: 
4684:   @TestRailId:C4466 @AdvancedPaymentAllocation
4685:   Scenario: Verify Loan re-aging trn with backdated 2nd disb and charge after re-age - interest bearing multidisb loan with equal amortization; outstanding payable interest - UC8
4686:     When Admin sets the business date to "01 January 2024"
4687:     When Admin creates a client with random data
4688:     When Admin creates a fully customized loan with the following data:
4689:       | LoanProduct                                                                            | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
4690:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALC_DAILY_MULTIDISBURSE_CHARGEBACK | 01 January 2024   | 150            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
4691:     And Admin successfully approves the loan on "01 January 2024" with "150" amount and expected disbursement date on "01 January 2024"
4692:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
4693:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4694:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
4695:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
4696:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4697:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4698:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4699:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4700:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4701:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
4702:     Then Loan Repayment schedule has the following data in Total row:
4703:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
4704:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
4705:     Then Loan Transactions tab has the following data:
4706:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4707:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4708: 
4709:     When Admin sets the business date to "01 February 2024"
4710:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
4711:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4712:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4713:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4714:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4715:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4716:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4717:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4718:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4719:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
4720:     Then Loan Repayment schedule has the following data in Total row:
4721:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4722:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
4723:     Then Loan Transactions tab has the following data:
4724:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4725:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4726:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4727: 
4728:     When Admin sets the business date to "15 March 2024"
4729:     When Admin runs inline COB job for Loan
4730:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
4731:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
4732:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
4733:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4734:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4735:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4736:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4737:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4738:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4739:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4740:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4741:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4742:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4743:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4744:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
4745:     Then Loan Repayment schedule has the following data in Total row:
4746:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4747:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
4748:     Then Loan Transactions tab has the following data:
4749:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4750:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4751:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4752:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4753:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
4754: 
4755:     When Admin sets the business date to "01 April 2024"
4756:     When Admin runs inline COB job for Loan
4757:     When Admin successfully disburse the loan on "01 March 2024" with "50" EUR transaction amount
4758:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4759:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4760:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4761:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4762:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4763:       |    |      | 01 March 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4764:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 133.57          |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4765:       | 4  | 17   | 01 April 2024     |                  | 111.31          | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4766:       | 5  | 30   | 01 May 2024       |                  | 89.05           | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4767:       | 6  | 31   | 01 June 2024      |                  | 66.79           | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4768:       | 7  | 30   | 01 July 2024      |                  | 44.53           | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4769:       | 8  | 31   | 01 August 2024    |                  | 22.27           | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4770:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 22.27         | 0.14     | 0.0  | 0.0       | 22.41 | 0.0   | 0.0        | 0.0  | 22.41       |
4771:     Then Loan Repayment schedule has the following data in Total row:
4772:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4773:       | 150.0         | 1.42     | 0.0  | 0.0       | 151.42 | 17.01 | 0.0        | 0.0  | 134.41      |
4774:     Then Loan Transactions tab has the following data without accruals:
4775:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4776:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4777:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4778:       | 01 March 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4779:       | 15 March 2024    | Re-age           | 134.41 | 133.57    | 0.84     | 0.0  | 0.0       | 0.0          | false    | true     |
4780:     Then Loan Transactions tab has the following new accrual data:
4781:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4782:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4783:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
4784:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4785:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4786:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4787:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4788:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4789:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4790:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4791:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4792:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4793:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4794:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4795: 
4796:     When Admin adds "LOAN_NSF_FEE" due date charge with "05 May 2024" due date and 10 EUR transaction amount
4797:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4798:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4799:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4800:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4801:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4802:       |    |      | 01 March 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4803:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 133.57          |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4804:       | 4  | 17   | 01 April 2024     |                  | 111.31          | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4805:       | 5  | 30   | 01 May 2024       |                  | 89.05           | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4806:       | 6  | 31   | 01 June 2024      |                  | 66.79           | 22.26         | 0.14     | 0.0  | 10.0      | 32.4  | 0.0   | 0.0        | 0.0  | 32.4        |
4807:       | 7  | 30   | 01 July 2024      |                  | 44.53           | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4808:       | 8  | 31   | 01 August 2024    |                  | 22.27           | 22.26         | 0.14     | 0.0  | 0.0       | 22.4  | 0.0   | 0.0        | 0.0  | 22.4        |
4809:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 22.27         | 0.14     | 0.0  | 0.0       | 22.41 | 0.0   | 0.0        | 0.0  | 22.41       |
4810:     Then Loan Repayment schedule has the following data in Total row:
4811:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4812:       | 150.0         | 1.42     | 0.0  | 10.0      | 161.42 | 17.01 | 0.0        | 0.0  | 144.41      |
4813:     Then Loan Transactions tab has the following data without accruals:
4814:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4815:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4816:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4817:       | 01 March 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4818:       | 15 March 2024    | Re-age           | 134.41 | 133.57    | 0.84     | 0.0  | 0.0       | 0.0          | false    | true     |
4819:     Then Loan Transactions tab has no new accrual data
4820: 
4821:     When Admin sets the business date to "15 April 2024"
4822:     When Admin runs inline COB job for Loan
4823:     Then Loan Transactions tab has the following data without accruals:
4824:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4825:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4826:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4827:       | 01 March 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4828:       | 15 March 2024    | Re-age           | 134.41 | 133.57    | 0.84     | 0.0  | 0.0       | 0.0          | false    | true     |
4829:     Then Loan Transactions tab has the following new accrual data:
4830:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4831:       | 01 April 2024    | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
4832:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4833:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4834:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4835:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4836:       | 11 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4837:       | 13 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4838:     When Loan Pay-off is made on "15 April 2024"
4839:     Then Loan Transactions tab has the following data without accruals:
4840:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4841:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4842:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4843:       | 01 March 2024    | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4844:       | 15 March 2024    | Re-age           | 134.41 | 133.57    | 0.84     | 0.0  | 0.0       | 0.0          | false    | true     |
4845:       | 15 April 2024    | Repayment        | 144.41 | 133.57    | 0.84     | 0.0  | 10.0      | 0.0          | false    | false    |
4846:     Then Loan Transactions tab has the following new accrual data:
4847:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4848:       | 15 April 2024    | Accrual            | 10.64  | 0.0       | 0.64     | 0.0  | 10.0      | 0.0          | false    | false    |
4849:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
4850: 
4851:   @TestRailId:C4467 @AdvancedPaymentAllocation
4852:   Scenario: Verify Loan re-aging trn with CI after re-age - interest bearing multidisb loan with equal amortization; outstanding payable interest - UC11
4853:     When Admin sets the business date to "01 January 2024"
4854:     When Admin creates a client with random data
4855:     When Admin creates a fully customized loan with the following data:
4856:       | LoanProduct                                                                                       | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
4857:       | LP2_ADV_PYMNT_INTEREST_DAILY_RECALC_EMI_360_30_MULTIDISB_APPROVED_OVER_APPLIED_CAPITALIZED_INCOME | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
4858:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
4859:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
4860:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4861:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
4862:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
4863:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4864:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4865:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4866:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4867:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
4868:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
4869:     Then Loan Repayment schedule has the following data in Total row:
4870:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
4871:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
4872:     Then Loan Transactions tab has the following data:
4873:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4874:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4875: 
4876:     When Admin sets the business date to "01 February 2024"
4877:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
4878:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4879:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4880:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4881:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4882:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4883:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4884:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4885:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4886:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
4887:     Then Loan Repayment schedule has the following data in Total row:
4888:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4889:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
4890:     Then Loan Transactions tab has the following data:
4891:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4892:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4893:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4894: 
4895:     When Admin sets the business date to "15 March 2024"
4896:     When Admin runs inline COB job for Loan
4897:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
4898:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
4899:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
4900:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4901:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4902:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4903:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4904:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4905:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4906:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4907:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4908:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4909:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4910:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4911:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
4912:     Then Loan Repayment schedule has the following data in Total row:
4913:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4914:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
4915:     Then Loan Transactions tab has the following data:
4916:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4917:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4918:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4919:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4920:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
4921: 
4922:     When Admin sets the business date to "01 April 2024"
4923:     When Admin runs inline COB job for Loan
4924:     And Admin adds capitalized income with "AUTOPAY" payment type to the loan on "01 April 2024" with "50" EUR transaction amount
4925:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
4926:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4927:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4928:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4929:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4930:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
4931:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
4932:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4933:       | 5  | 30   | 01 May 2024       |                  | 95.71           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4934:       | 6  | 31   | 01 June 2024      |                  | 71.78           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4935:       | 7  | 30   | 01 July 2024      |                  | 47.85           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4936:       | 8  | 31   | 01 August 2024    |                  | 23.92           | 23.93         | 0.12     | 0.0  | 0.0       | 24.05 | 0.0   | 0.0        | 0.0  | 24.05       |
4937:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 23.92         | 0.11     | 0.0  | 0.0       | 24.03 | 0.0   | 0.0        | 0.0  | 24.03       |
4938:     Then Loan Repayment schedule has the following data in Total row:
4939:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4940:       | 150.0         | 1.29     | 0.0  | 0.0       | 151.29 | 17.01 | 0.0        | 0.0  | 134.28      |
4941:     Then Loan Transactions tab has the following data without accruals:
4942:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4943:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4944:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4945:       | 15 March 2024    | Re-age             | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
4946:       | 01 April 2024    | Capitalized Income | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4947:     Then Loan Transactions tab has the following new accrual data:
4948:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4949:       | 14 March 2024    | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
4950:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
4951:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4952:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4953:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4954:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4955:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4956:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4957:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4958:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4959:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4960:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4961:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
4962: 
4963:     When Admin successfully undo Loan re-aging transaction
4964:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
4965:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
4966:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4967:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
4968:       | 2  | 29   | 01 March 2024     |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4969:       | 3  | 31   | 01 April 2024     |                  | 50.53           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
4970:       |    |      | 01 April 2024     |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
4971:       | 4  | 30   | 01 May 2024       |                  | 67.25           | 33.28         | 0.59     | 0.0  | 0.0       | 33.87 | 0.0   | 0.0        | 0.0  | 33.87       |
4972:       | 5  | 31   | 01 June 2024      |                  | 33.77           | 33.48         | 0.39     | 0.0  | 0.0       | 33.87 | 0.0   | 0.0        | 0.0  | 33.87       |
4973:       | 6  | 30   | 01 July 2024      |                  |  0.0            | 33.77         | 0.2      | 0.0  | 0.0       | 33.97 | 0.0   | 0.0        | 0.0  | 33.97       |
4974:     Then Loan Repayment schedule has the following data in Total row:
4975:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
4976:       | 150.0         | 2.74     | 0.0  | 0.0       | 152.74 | 17.01 | 0.0        | 0.0  | 135.73      |
4977:     Then Loan Transactions tab has the following data without accruals:
4978:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4979:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4980:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4981:       | 15 March 2024    | Re-age             | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | true     | false    |
4982:       | 01 April 2024    | Capitalized Income | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4983:     Then Loan Transactions tab has no new accrual data
4984: 
4985:     When Admin sets the business date to "10 April 2024"
4986:     When Admin runs inline COB job for Loan
4987:     Then Loan Transactions tab has the following data without accruals:
4988:       | Transaction date | Transaction Type                | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
4989:       | 01 January 2024  | Disbursement                    | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
4990:       | 01 February 2024 | Repayment                       | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
4991:       | 15 March 2024    | Re-age                          | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | true     | false    |
4992:       | 01 April 2024    | Capitalized Income              | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
4993:       | 01 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
4994:       | 02 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
4995:       | 03 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
4996:       | 04 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
4997:       | 05 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
4998:       | 06 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
4999:       | 07 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5000:       | 08 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5001:       | 09 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5002:     Then Loan Transactions tab has the following new accrual data:
5003:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5004:       | 01 April 2024    | Accrual          | 0.87   | 0.0       | 0.87     | 0.0  | 0.0       | 0.0          | false    | false    |
5005:       | 02 April 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
5006:       | 03 April 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5007:       | 04 April 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
5008:       | 05 April 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5009:       | 06 April 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
5010:       | 07 April 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
5011:       | 08 April 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5012:       | 09 April 2024    | Accrual          | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
5013: 
5014:     When Loan Pay-off is made on "10 April 2024"
5015:     Then Loan Transactions tab has the following data without accruals:
5016:       | Transaction date | Transaction Type                | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5017:       | 01 January 2024  | Disbursement                    | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5018:       | 01 February 2024 | Repayment                       | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5019:       | 15 March 2024    | Re-age                          | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | true     | false    |
5020:       | 01 April 2024    | Capitalized Income              | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
5021:       | 01 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5022:       | 02 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5023:       | 03 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5024:       | 04 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5025:       | 05 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5026:       | 06 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5027:       | 07 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5028:       | 08 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5029:       | 09 April 2024    | Capitalized Income Amortization | 0.55   | 0.0       | 0.55     | 0.0  | 0.0       | 0.0          | false    | false    |
5030:       | 10 April 2024    | Repayment                       | 134.78 | 133.57    | 1.21     | 0.0  | 0.0       | 0.0          | false    | false    |
5031:       | 10 April 2024    | Capitalized Income Amortization | 45.05  | 0.0       | 45.05    | 0.0  | 0.0       | 0.0          | false    | false    |
5032:     Then Loan Transactions tab has the following new accrual data:
5033:       | Transaction date | Transaction Type                | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5034:       | 10 April 2024    | Accrual                         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5035:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
5036: 
5037:   @TestRailId:C4468 @AdvancedPaymentAllocation
5038:   Scenario: Verify Loan re-aging trn with backdated re-aging after CI with CI undo afterwards - interest bearing multidisb loan with equal amortization; outstanding FULL interest - UC15
5039:     When Admin sets the business date to "01 January 2024"
5040:     When Admin creates a client with random data
5041:     When Admin creates a fully customized loan with the following data:
5042:       | LoanProduct                                                                                       | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
5043:       | LP2_ADV_PYMNT_INTEREST_DAILY_RECALC_EMI_360_30_MULTIDISB_APPROVED_OVER_APPLIED_CAPITALIZED_INCOME | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
5044:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
5045:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
5046:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5047:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
5048:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
5049:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5050:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5051:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5052:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5053:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5054:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
5055:     Then Loan Repayment schedule has the following data in Total row:
5056:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
5057:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
5058:     Then Loan Transactions tab has the following data:
5059:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5060:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5061: 
5062:     When Admin sets the business date to "01 February 2024"
5063:     When Admin runs inline COB job for Loan
5064:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
5065:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5066:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5067:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5068:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5069:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5070:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5071:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5072:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5073:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
5074:     Then Loan Repayment schedule has the following data in Total row:
5075:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5076:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
5077:     Then Loan Transactions tab has the following data:
5078:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5079:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5080:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
5081:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5082: 
5083:     When Admin sets the business date to "01 May 2024"
5084:     When Admin runs inline COB job for Loan
5085:     And Admin adds capitalized income with "AUTOPAY" payment type to the loan on "01 May 2024" with "50" EUR transaction amount
5086:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5087:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5088:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5089:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5090:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5091:       | 3  | 31   | 01 April 2024    |                  | 50.53           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5092:       | 4  | 30   | 01 May 2024      |                  | 34.01           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5093:       |    |      | 01 May 2024      |                  | 50.0            |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5094:       | 5  | 31   | 01 June 2024     |                  | 42.28           | 41.73         | 0.49     | 0.0  | 0.0       | 42.22 | 0.0   | 0.0        | 0.0  | 42.22       |
5095:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 42.28         | 0.25     | 0.0  | 0.0       | 42.53 | 0.0   | 0.0        | 0.0  | 42.53       |
5096:     Then Loan Repayment schedule has the following data in Total row:
5097:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5098:       | 150.0         | 2.79     | 0.0  | 0.0       | 152.79 | 17.01 | 0.0        | 0.0  | 135.78      |
5099:     Then Loan Transactions tab has the following data without accruals:
5100:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5101:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5102:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5103:       | 01 May 2024      | Capitalized Income | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
5104:     Then Loan Transactions tab has the following new accrual data:
5105:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5106:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
5107:       | 01 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5108:       | 02 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5109:       | 03 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5110:       | 04 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5111:       | 05 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5112:       | 06 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5113:       | 07 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5114:       | 08 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5115:       | 09 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5116:       | 10 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5117:       | 11 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5118:       | 12 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5119:       | 13 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5120:       | 14 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5121:       | 15 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5122:       | 16 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5123:       | 17 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5124:       | 18 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5125:       | 19 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5126:       | 20 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5127:       | 21 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5128:       | 22 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5129:       | 23 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5130:       | 24 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5131:       | 25 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5132:       | 26 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5133:       | 27 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5134:       | 28 February 2024  | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5135:       | 29 February 2024  | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5136:       | 01 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5137:       | 02 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5138:       | 03 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5139:       | 04 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5140:       | 05 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5141:       | 06 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5142:       | 07 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5143:       | 08 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5144:       | 09 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5145:       | 10 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5146:       | 11 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5147:       | 12 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5148:       | 13 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5149:       | 14 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5150:       | 15 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5151:       | 16 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5152:       | 17 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5153:       | 18 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5154:       | 19 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5155:       | 20 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5156:       | 21 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5157:       | 22 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5158:       | 23 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5159:       | 24 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5160:       | 25 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5161:       | 26 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5162:       | 27 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5163:       | 28 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5164:       | 29 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5165:       | 30 March 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5166:       | 31 March 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5167:       | 01 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5168:       | 02 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5169:       | 03 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5170:       | 04 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5171:       | 05 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5172:       | 06 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5173:       | 07 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5174:       | 08 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5175:       | 09 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5176:       | 10 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5177:       | 11 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5178:       | 12 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5179:       | 13 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5180:       | 14 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5181:       | 15 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5182:       | 16 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5183:       | 17 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5184:       | 18 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5185:       | 19 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5186:       | 20 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5187:       | 21 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5188:       | 22 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5189:       | 23 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5190:       | 24 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5191:       | 25 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5192:       | 26 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5193:       | 27 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5194:       | 28 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5195:       | 29 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5196:       | 30 April 2024     | Accrual         | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5197: 
5198:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
5199:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
5200:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
5201:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5202:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5203:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5204:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5205:       | 2  | 29   | 01 March 2024     | 01 April 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       |  0.0  | 0.0   | 0.0        | 0.0  | 0.0         |
5206:       | 3  | 31   | 01 April 2024     | 01 April 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       |  0.0  | 0.0   | 0.0        | 0.0  | 0.0         |
5207:       | 4  |  0   | 01 April 2024     |                  | 69.64           | 13.93         | 0.26     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5208:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.26     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5209:       |    |      | 01 May 2024       |                  |  50.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5210:       | 6  | 31   | 01 June 2024      |                  | 79.28           | 26.43         | 0.26     | 0.0  | 0.0       | 26.69 | 0.0   | 0.0        | 0.0  | 26.69       |
5211:       | 7  | 30   | 01 July 2024      |                  | 52.85           | 26.43         | 0.26     | 0.0  | 0.0       | 26.69 | 0.0   | 0.0        | 0.0  | 26.69       |
5212:       | 8  | 31   | 01 August 2024    |                  | 26.42           | 26.43         | 0.26     | 0.0  | 0.0       | 26.69 | 0.0   | 0.0        | 0.0  | 26.69       |
5213:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 26.42         | 0.27     | 0.0  | 0.0       | 26.69 | 0.0   | 0.0        | 0.0  | 26.69       |
5214:     Then Loan Repayment schedule has the following data in Total row:
5215:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5216:       | 150.0         | 2.15     | 0.0  | 0.0       | 152.15 | 17.01 | 0.0        | 0.0  | 135.14      |
5217:     Then Loan Transactions tab has the following data without accruals:
5218:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5219:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5220:       | 01 February 2024 | Repayment          | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5221:       | 01 April 2024    | Re-age             | 85.14  | 83.57     | 1.57     | 0.0  | 0.0       | 0.0          | false    | false    |
5222:       | 01 May 2024      | Capitalized Income | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | false    | false    |
5223:     Then Loan Transactions tab has no new accrual data
5224: 
5225:     When Admin sets the business date to "02 May 2024"
5226:     When Admin runs inline COB job for Loan
5227:     When Customer undo "1"th "Capitalized Income" transaction made on "01 May 2024"
5228:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5229:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5230:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5231:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5232:       | 2  | 29   | 01 March 2024     | 01 April 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5233:       | 3  | 31   | 01 April 2024     | 01 April 2024    | 83.57           |  0.0          | 0.0      | 0.0  | 0.0       |  0.0  | 0.0   | 0.0        | 0.0  | 0.0         |
5234:       | 4  |  0   | 01 April 2024     |                  | 69.64           | 13.93         | 0.26     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5235:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.26     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5236:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.26     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5237:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.26     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5238:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.26     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5239:       | 9  | 31   | 01 September 2024 |                  |  0.0            | 13.92         | 0.27     | 0.0  | 0.0       | 14.19 | 0.0   | 0.0        | 0.0  | 14.19       |
5240:     Then Loan Repayment schedule has the following data in Total row:
5241:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5242:       | 100.0         | 2.15     | 0.0  | 0.0       | 102.15 | 17.01 | 0.0        | 0.0  | 85.14      |
5243:     Then Loan Transactions tab has the following data without accruals:
5244:       | Transaction date | Transaction Type                | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5245:       | 01 January 2024  | Disbursement                    | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5246:       | 01 February 2024 | Repayment                       | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5247:       | 01 April 2024    | Re-age                          | 85.14  | 83.57     | 1.57     | 0.0  | 0.0       | 0.0          | false    | false    |
5248:       | 01 May 2024      | Capitalized Income              | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | true     | false    |
5249:       | 01 May 2024      | Capitalized Income Amortization | 0.41   | 0.0       | 0.41     | 0.0  | 0.0       | 0.0          | false    | false    |
5250:     Then Loan Transactions tab has the following new accrual data:
5251:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5252:       | 01 May 2024      | Accrual Adjustment | 0.93   | 0.0       | 0.93     | 0.0  | 0.0       | 0.0          | false    | false    |
5253: 
5254:     When Admin sets the business date to "10 May 2024"
5255:     When Admin runs inline COB job for Loan
5256:     When Loan Pay-off is made on "10 May 2024"
5257:     Then Loan Transactions tab has the following data without accruals:
5258:       | Transaction date | Transaction Type                | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5259:       | 01 January 2024  | Disbursement                    | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5260:       | 01 February 2024 | Repayment                       | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5261:       | 01 April 2024    | Re-age                          | 85.14  | 83.57     | 1.57     | 0.0  | 0.0       | 0.0          | false    | false    |
5262:       | 01 May 2024      | Capitalized Income              | 50.0   | 50.0      | 0.0      | 0.0  | 0.0       | 133.57       | true     | false    |
5263:       | 01 May 2024      | Capitalized Income Amortization | 0.41   | 0.0       | 0.41     | 0.0  | 0.0       | 0.0          | false    | false    |
5264:       | 02 May 2024      | Capitalized Income Amortization Adjustment | 0.41   | 0.0       | 0.41     | 0.0  | 0.0       | 0.0          | false    | false    |
5265:       | 10 May 2024      | Repayment                       | 85.14  | 83.57     | 1.57     | 0.0  | 0.0       | 0.0          | false    | false    |
5266:     Then Loan Transactions tab has the following new accrual data:
5267:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5268:       | 02 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5269:       | 03 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5270:       | 04 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5271:       | 06 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5272:       | 07 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5273:       | 08 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5274:       | 09 May 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5275:       | 10 May 2024      | Accrual            | 0.98   | 0.0       | 0.98     | 0.0  | 0.0       | 0.0          | false    | false    |
5276:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
5277: 
5278:   @TestRailId:C4469
5279:   Scenario: Verify Re-aging with interest pause: UC7: Interest handling: EQUAL_AMORTIZATION_PAYABLE_INTEREST, multiple pauses, early repayment, mid-pause repayment
5280:     When Admin sets the business date to "01 January 2024"
5281:     And Admin creates a client with random data
5282:     And Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
5283:     And Admin creates a fully customized loan with the following data:
5284:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
5285:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
5286:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
5287:     And Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
5288:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5289:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
5290:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
5291:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5292:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5293:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5294:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5295:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5296:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
5297:     And Loan Repayment schedule has the following data in Total row:
5298:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
5299:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
5300:     And Loan Transactions tab has the following data:
5301:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5302:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5303: #    --- First installment paid - early repayment---
5304:     When Admin sets the business date to "14 January 2024"
5305:     When Admin runs inline COB job for Loan
5306:     And Customer makes "AUTOPAY" repayment on "14 January 2024" with 17.01 EUR transaction amount
5307:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5308:       | Nr | Days | Date             | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5309:       |    |      | 01 January 2024  |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5310:       | 1  | 31   | 01 February 2024 | 14 January 2024 | 83.23           | 16.77         | 0.24     | 0.0  | 0.0       | 17.01 | 17.01 | 17.01      | 0.0  | 0.0         |
5311:       | 2  | 29   | 01 March 2024    |                 | 67.0            | 16.23         | 0.78     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5312:       | 3  | 31   | 01 April 2024    |                 | 50.38           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5313:       | 4  | 30   | 01 May 2024      |                 | 33.66           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5314:       | 5  | 31   | 01 June 2024     |                 | 16.85           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5315:       | 6  | 30   | 01 July 2024     |                 | 0.0             | 16.85         | 0.1      | 0.0  | 0.0       | 16.95 | 0.0   | 0.0        | 0.0  | 16.95       |
5316:     And Loan Repayment schedule has the following data in Total row:
5317:       | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5318:       | 100.0         | 2.0      | 0.0  | 0.0       | 102.0 | 17.01 | 17.01      | 0.0  | 84.99       |
5319:     And Loan Transactions tab has the following data:
5320:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5321:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5322:       | 13 January 2024  | Accrual          | 0.23   | 0.0       | 0.23     | 0.0  | 0.0       | 0.0          | false    | false    |
5323:       | 14 January 2024  | Repayment        | 17.01  | 16.77     | 0.24     | 0.0  | 0.0       | 83.23        | false    | false    |
5324:       #    --- Interest pause ---
5325:     And Create an interest pause period with start date "15 January 2024" and end date "10 March 2024"
5326:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5327:       | Nr | Days | Date             | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5328:       |    |      | 01 January 2024  |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5329:       | 1  | 31   | 01 February 2024 | 14 January 2024 | 83.23           | 16.77         | 0.24     | 0.0  | 0.0       | 17.01 | 17.01 | 17.01      | 0.0  | 0.0         |
5330:       | 2  | 29   | 01 March 2024    |                 | 66.22           | 17.01         | 0.0      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5331:       | 3  | 31   | 01 April 2024    |                 | 49.48           | 16.74         | 0.27     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5332:       | 4  | 30   | 01 May 2024      |                 | 32.76           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5333:       | 5  | 31   | 01 June 2024     |                 | 15.94           | 16.82         | 0.19     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5334:       | 6  | 30   | 01 July 2024     |                 | 0.0             | 15.94         | 0.09     | 0.0  | 0.0       | 16.03 | 0.0   | 0.0        | 0.0  | 16.03       |
5335:     And Loan Repayment schedule has the following data in Total row:
5336:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5337:       | 100.0         | 1.08     | 0.0  | 0.0       | 101.08 | 17.01 | 17.01      | 0.0  | 84.07       |
5338:     And Loan Transactions tab has the following data:
5339:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5340:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5341:       | 13 January 2024  | Accrual          | 0.23   | 0.0       | 0.23     | 0.0  | 0.0       | 0.0          | false    | false    |
5342:       | 14 January 2024  | Repayment        | 17.01  | 16.77     | 0.24     | 0.0  | 0.0       | 83.23        | false    | false    |
5343: #    --- Check before re-age ---
5344:     When Admin sets the business date to "15 March 2024"
5345:     When Admin runs inline COB job for Loan
5346:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5347:       | Nr | Days | Date             | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5348:       |    |      | 01 January 2024  |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5349:       | 1  | 31   | 01 February 2024 | 14 January 2024 | 83.23           | 16.77         | 0.24     | 0.0  | 0.0       | 17.01 | 17.01 | 17.01      | 0.0  | 0.0         |
5350:       | 2  | 29   | 01 March 2024    |                 | 66.22           | 17.01         | 0.0      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5351:       | 3  | 31   | 01 April 2024    |                 | 49.5            | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5352:       | 4  | 30   | 01 May 2024      |                 | 32.78           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5353:       | 5  | 31   | 01 June 2024     |                 | 15.96           | 16.82         | 0.19     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5354:       | 6  | 30   | 01 July 2024     |                 | 0.0             | 15.96         | 0.09     | 0.0  | 0.0       | 16.05 | 0.0   | 0.0        | 0.0  | 16.05       |
5355:     And Loan Repayment schedule has the following data in Total row:
5356:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5357:       | 100.0         | 1.1      | 0.0  | 0.0       | 101.1  | 17.01 | 17.01      | 0.0  | 84.09       |
5358:     And Loan Transactions tab has the following data without accruals:
5359:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5360:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5361:       | 14 January 2024  | Repayment        | 17.01  | 16.77     | 0.24     | 0.0  | 0.0       | 83.23        | false    | false    |
5362:       | 01 February 2024 | Accrual Activity | 0.24   | 0.0       | 0.24     | 0.0  | 0.0       | 0.0          | false    | false    |
5363:     Then Loan Transactions tab has the following new accrual data:
5364:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5365:       | 13 January 2024  | Accrual          | 0.23   | 0.0       | 0.23     | 0.0  | 0.0       | 0.0          | false    | false    |
5366:       | 14 January 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5367:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5368:       | 12 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5369:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5370:       | 14 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5371: #   --- Re-age transaction ---
5372:     When Admin creates a Loan re-aging transaction with the following data:
5373:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
5374:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
5375:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5376:       | Nr | Days | Date              | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5377:       |    |      | 01 January 2024   |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5378:       | 1  | 31   | 01 February 2024  | 14 January 2024 | 83.23           | 16.77         | 0.24     | 0.0  | 0.0       | 17.01 | 17.01 | 17.01      | 0.0  | 0.0         |
5379:       | 2  | 29   | 01 March 2024     | 15 March 2024   | 83.23           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5380:       | 3  | 14   | 15 March 2024     | 15 March 2024   | 83.23           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5381:       | 4  | 17   | 01 April 2024     |                 | 69.36           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5382:       | 5  | 30   | 01 May 2024       |                 | 55.49           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5383:       | 6  | 31   | 01 June 2024      |                 | 41.62           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5384:       | 7  | 30   | 01 July 2024      |                 | 27.75           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5385:       | 8  | 31   | 01 August 2024    |                 | 13.88           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5386:       | 9  | 31   | 01 September 2024 |                 | 0.0             | 13.88         | 0.03     | 0.0  | 0.0       | 13.91 | 0.0   | 0.0        | 0.0  | 13.91       |
5387:     And Loan Repayment schedule has the following data in Total row:
5388:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5389:       | 100.0         | 0.32     | 0.0  | 0.0       | 100.32 | 17.01 | 17.01      | 0.0  | 83.31       |
5390:     And Loan Transactions tab has the following data without accruals:
5391:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5392:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5393:       | 14 January 2024  | Repayment        | 17.01  | 16.77     | 0.24     | 0.0  | 0.0       | 83.23        | false    | false    |
5394:       | 01 February 2024 | Accrual Activity | 0.24   | 0.0       | 0.24     | 0.0  | 0.0       | 0.0          | false    | false    |
5395:       | 15 March 2024    | Re-age           | 83.31  | 83.23     | 0.08     | 0.0  | 0.0       | 0.0          | false    | false    |
5396:     Then Loan Transactions tab has no new accrual data
5397:   #    --- 2nd Interest pause ---
5398:     When Admin sets the business date to "02 April 2024"
5399:     When Admin runs inline COB job for Loan
5400:     And Create an interest pause period with start date "10 April 2024" and end date "10 June 2024"
5401:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5402:       | Nr | Days | Date              | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5403:       |    |      | 01 January 2024   |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5404:       | 1  | 31   | 01 February 2024  | 14 January 2024 | 83.23           | 16.77         | 0.24     | 0.0  | 0.0       | 17.01 | 17.01 | 17.01      | 0.0  | 0.0         |
5405:       | 2  | 29   | 01 March 2024     | 15 March 2024   | 83.23           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5406:       | 3  | 14   | 15 March 2024     | 15 March 2024   | 83.23           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5407:       | 4  | 17   | 01 April 2024     |                 | 69.36           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5408:       | 5  | 30   | 01 May 2024       |                 | 55.49           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5409:       | 6  | 31   | 01 June 2024      |                 | 41.62           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5410:       | 7  | 30   | 01 July 2024      |                 | 27.75           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5411:       | 8  | 31   | 01 August 2024    |                 | 13.88           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5412:       | 9  | 31   | 01 September 2024 |                 | 0.0             | 13.88         | 0.03     | 0.0  | 0.0       | 13.91 | 0.0   | 0.0        | 0.0  | 13.91       |
5413:     And Loan Repayment schedule has the following data in Total row:
5414:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5415:       | 100.0         | 0.32     | 0.0  | 0.0       | 100.32 | 17.01 | 17.01      | 0.0  | 83.31       |
5416:     And Loan Transactions tab has the following data without accruals:
5417:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5418:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5419:       | 14 January 2024  | Repayment        | 17.01  | 16.77     | 0.24     | 0.0  | 0.0       | 83.23        | false    | false    |
5420:       | 01 February 2024 | Accrual Activity | 0.24   | 0.0       | 0.24     | 0.0  | 0.0       | 0.0          | false    | false    |
5421:       | 15 March 2024    | Re-age           | 83.31  | 83.23     | 0.08     | 0.0  | 0.0       | 0.0          | false    | false    |
5422:       | 01 April 2024    | Accrual Activity | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5423:     Then Loan Transactions tab has the following new accrual data:
5424:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5425:       | 15 March 2024    | Accrual Adjustment | 0.06   | 0.0       | 0.06     | 0.0  | 0.0       | 0.0          | false    | false    |
5426:       | 24 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5427: #    --- Mid-pause repayment ---
5428:     When Admin sets the business date to "01 May 2024"
5429:     When Admin runs inline COB job for Loan
5430:     And Customer makes "AUTOPAY" repayment on "01 May 2024" with 17.01 EUR transaction amount
5431:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5432:       | Nr | Days | Date              | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5433:       |    |      | 01 January 2024   |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5434:       | 1  | 31   | 01 February 2024  | 14 January 2024 | 83.23           | 16.77         | 0.24     | 0.0  | 0.0       | 17.01 | 17.01 | 17.01      | 0.0  | 0.0         |
5435:       | 2  | 29   | 01 March 2024     | 15 March 2024   | 83.23           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5436:       | 3  | 14   | 15 March 2024     | 15 March 2024   | 83.23           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5437:       | 4  | 17   | 01 April 2024     | 01 May 2024     | 69.36           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 13.88 | 0.0        | 13.88| 0.0         |
5438:       | 5  | 30   | 01 May 2024       |                 | 55.49           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 3.13  | 0.0        | 0.0  | 10.75       |
5439:       | 6  | 31   | 01 June 2024      |                 | 41.62           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5440:       | 7  | 30   | 01 July 2024      |                 | 27.75           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5441:       | 8  | 31   | 01 August 2024    |                 | 13.88           | 13.87         | 0.01     | 0.0  | 0.0       | 13.88 | 0.0   | 0.0        | 0.0  | 13.88       |
5442:       | 9  | 31   | 01 September 2024 |                 | 0.0             | 13.88         | 0.03     | 0.0  | 0.0       | 13.91 | 0.0   | 0.0        | 0.0  | 13.91       |
5443:     And Loan Repayment schedule has the following data in Total row:
5444:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late  | Outstanding |
5445:       | 100.0         | 0.32     | 0.0  | 0.0       | 100.32 | 34.02 | 17.01      | 13.88 | 66.3        |
5446:     And Loan Transactions tab has the following data without accruals:
5447:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5448:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5449:       | 14 January 2024  | Repayment        | 17.01  | 16.77     | 0.24     | 0.0  | 0.0       | 83.23        | false    | false    |
5450:       | 01 February 2024 | Accrual Activity | 0.24   | 0.0       | 0.24     | 0.0  | 0.0       | 0.0          | false    | false    |
5451:       | 15 March 2024    | Re-age           | 83.31  | 83.23     | 0.08     | 0.0  | 0.0       | 0.0          | false    | false    |
5452:       | 01 April 2024    | Accrual Activity | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5453:       | 01 May 2024      | Repayment        | 17.01  | 16.99     | 0.02     | 0.0  | 0.0       | 66.24        | false    | false    |
5454:     Then Loan Transactions tab has the following new accrual data:
5455:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5456:       | 17 April 2024     | Accrual         | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5457: #   --- Close loan ---
5458:     When Admin sets the business date to "05 May 2024"
5459:     When Admin runs inline COB job for Loan
5460:     When Loan Pay-off is made on "05 May 2024"
5461:     And Loan Transactions tab has the following data without accruals:
5462:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5463:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5464:       | 14 January 2024  | Repayment        | 17.01  | 16.77     | 0.24     | 0.0  | 0.0       | 83.23        | false    | false    |
5465:       | 01 February 2024 | Accrual Activity | 0.24   | 0.0       | 0.24     | 0.0  | 0.0       | 0.0          | false    | false    |
5466:       | 15 March 2024    | Re-age           | 83.31  | 83.23     | 0.08     | 0.0  | 0.0       | 0.0          | false    | false    |
5467:       | 01 April 2024    | Accrual Activity | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5468:       | 01 May 2024      | Repayment        | 17.01  | 16.99     | 0.02     | 0.0  | 0.0       | 66.24        | false    | false    |
5469:       | 01 May 2024      | Accrual Activity | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5470:       | 05 May 2024      | Repayment        | 66.3   | 66.24     | 0.06     | 0.0  | 0.0       | 0.0          | false    | false    |
5471:       | 05 May 2024      | Accrual Activity | 0.06   | 0.0       | 0.06     | 0.0  | 0.0       | 0.0          | false    | false    |
5472:     Then Loan Transactions tab has the following new accrual data:
5473:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5474:       | 05 May 2024      | Accrual          | 0.06   | 0.0       | 0.06     | 0.0  | 0.0       | 0.0          | false    | false    |
5475:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
5476: 
5477:   @TestRailId:C4470
5478:   Scenario: Verify Re-aging with interest pause: UC5: Interest handling: equal amortization + outstanding full interest, backdated interest pause to re-aging, starts after re-aging
5479:     When Admin sets the business date to "01 January 2024"
5480:     And Admin creates a client with random data
5481:     And Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
5482:     And Admin creates a fully customized loan with the following data:
5483:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
5484:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
5485:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
5486:     And Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
5487:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5488:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
5489:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
5490:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5491:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5492:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5493:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5494:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5495:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
5496:     And Loan Repayment schedule has the following data in Total row:
5497:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
5498:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
5499:     And Loan Transactions tab has the following data:
5500:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5501:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5502: #    --- First installment paid ---
5503:     When Admin sets the business date to "01 February 2024"
5504:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
5505:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5506:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5507:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5508:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5509:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5510:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5511:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5512:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5513:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
5514:     And Loan Repayment schedule has the following data in Total row:
5515:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5516:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
5517:     And Loan Transactions tab has the following data:
5518:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5519:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5520:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5521: #    --- Check before re-age ---
5522:     When Admin sets the business date to "15 March 2024"
5523:     When Admin runs inline COB job for Loan
5524:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5525:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5526:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5527:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5528:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5529:       | 3  | 31   | 01 April 2024    |                  | 50.47           | 16.58         | 0.43     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5530:       | 4  | 30   | 01 May 2024      |                  | 33.75           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5531:       | 5  | 31   | 01 June 2024     |                  | 16.94           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5532:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.94         | 0.1      | 0.0  | 0.0       | 17.04 | 0.0   | 0.0        | 0.0  | 17.04       |
5533:     Then Loan Repayment schedule has the following data in Total row:
5534:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5535:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
5536:     And Loan Transactions tab has the following data:
5537:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5538:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5539:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5540:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5541:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
5542:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
5543: #   --- Re-age transaction ---
5544:     When Admin creates a Loan re-aging transaction with the following data:
5545:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
5546:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
5547:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5548:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5549:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5550:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5551:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5552:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5553:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5554:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5555:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5556:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5557:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5558:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5559:     And Loan Repayment schedule has the following data in Total row:
5560:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5561:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
5562:     And Loan Transactions tab has the following data:
5563:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5564:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5565:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5566:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5567:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
5568:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
5569:   #    --- Interest pause ---
5570:     When Admin sets the business date to "01 July 2024"
5571:     When Admin runs inline COB job for Loan
5572:     And Create an interest pause period with start date "10 April 2024" and end date "10 June 2024"
5573:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5574:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5575:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5576:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5577:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5578:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5579:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5580:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5581:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5582:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5583:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5584:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5585:     And Loan Repayment schedule has the following data in Total row:
5586:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5587:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
5588:     And Loan Transactions tab has the following data without accruals:
5589:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5590:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5591:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5592:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5593:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
5594:       | 01 April 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
5595:       | 01 May 2024      | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
5596:       | 01 June 2024     | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
5597:     Then Loan Transactions tab has the following new accrual data:
5598:       | Transaction date | Transaction Type    | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5599:       | 14 March 2024     | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
5600:       | 15 March 2024     | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
5601:       | 16 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5602:       | 17 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5603:       | 18 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5604:       | 19 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5605:       | 20 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5606:       | 21 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5607:       | 22 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5608:       | 23 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5609:       | 24 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5610:       | 25 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5611:       | 26 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5612:       | 27 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5613:       | 28 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5614:       | 29 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5615:       | 30 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5616:       | 31 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5617:       | 01 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5618:       | 02 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5619:       | 03 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5620:       | 05 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5621:       | 06 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5622:       | 07 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5623:       | 08 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5624:       | 09 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5625:       | 10 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5626:       | 12 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5627:       | 13 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5628:       | 14 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5629:       | 15 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5630:       | 17 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5631:       | 18 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5632:       | 19 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5633:       | 20 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5634:       | 21 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5635:       | 22 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5636:       | 24 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5637:       | 25 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5638:       | 26 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5639:       | 27 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5640:       | 29 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5641:       | 30 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5642:       | 01 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5643:       | 02 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5644:       | 03 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5645:       | 05 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5646:       | 06 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5647:       | 07 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5648:       | 08 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5649:       | 10 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5650:       | 11 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5651:       | 12 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5652:       | 13 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5653:       | 15 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5654:       | 16 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5655:       | 17 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5656:       | 18 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5657:       | 19 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5658:       | 21 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5659:       | 22 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5660:       | 23 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5661:       | 24 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5662:       | 26 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5663:       | 27 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5664:       | 28 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5665:       | 29 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5666:       | 31 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5667:       | 01 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5668:       | 02 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5669:       | 03 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5670:       | 05 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5671:       | 06 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5672:       | 07 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5673:       | 08 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5674:       | 09 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5675:       | 10 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5676:       | 12 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5677:       | 13 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5678:       | 14 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5679:       | 15 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5680:       | 17 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5681:       | 18 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5682:       | 19 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5683:       | 20 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5684:       | 21 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5685:       | 22 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5686:       | 24 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5687:       | 25 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5688:       | 26 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5689:       | 27 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5690:       | 29 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5691:       | 30 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5692: #   --- Close loan ---
5693:     When Admin sets the business date to "05 July 2024"
5694:     When Admin runs inline COB job for Loan
5695:     When Loan Pay-off is made on "05 July 2024"
5696:     And Loan Transactions tab has the following data without accruals:
5697:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5698:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5699:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5700:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5701:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
5702:       | 01 April 2024    | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
5703:       | 01 May 2024      | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
5704:       | 01 June 2024     | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
5705:       | 01 July 2024     | Accrual Activity | 0.25   | 0.0       | 0.25     | 0.0  | 0.0       | 0.0          | false    | false    |
5706:       | 05 July 2024     | Repayment        | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
5707:       | 05 July 2024     | Accrual Activity | 0.51   | 0.0       | 0.51     | 0.0  | 0.0       | 0.0          | false    | false    |
5708:     Then Loan Transactions tab has the following new accrual data:
5709:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5710:       | 01 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5711:       | 02 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5712:       | 03 July 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5713:       | 05 July 2024     | Accrual            | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
5714:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
5715: 
5716:   @TestRailId:C4471
5717:   Scenario: Verify Re-aging with interest pause: UC6: Interest handling: equal amortization + outstanding full interest, backdated interest pause after re-aging, overlapping re-aging partially
5718:     When Admin sets the business date to "01 January 2024"
5719:     And Admin creates a client with random data
5720:     And Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
5721:     And Admin creates a fully customized loan with the following data:
5722:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
5723:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
5724:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
5725:     And Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
5726:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5727:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
5728:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
5729:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5730:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5731:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5732:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5733:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5734:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
5735:     And Loan Repayment schedule has the following data in Total row:
5736:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
5737:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
5738:     And Loan Transactions tab has the following data:
5739:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5740:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5741: #    --- First installment paid ---
5742:     When Admin sets the business date to "01 February 2024"
5743:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
5744:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5745:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5746:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5747:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5748:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5749:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5750:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5751:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5752:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
5753:     And Loan Repayment schedule has the following data in Total row:
5754:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5755:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
5756:     And Loan Transactions tab has the following data:
5757:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5758:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5759:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5760: #    --- Check before re-age ---
5761:     When Admin sets the business date to "15 March 2024"
5762:     When Admin runs inline COB job for Loan
5763:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5764:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5765:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5766:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5767:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5768:       | 3  | 31   | 01 April 2024    |                  | 50.47           | 16.58         | 0.43     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5769:       | 4  | 30   | 01 May 2024      |                  | 33.75           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5770:       | 5  | 31   | 01 June 2024     |                  | 16.94           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5771:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.94         | 0.1      | 0.0  | 0.0       | 17.04 | 0.0   | 0.0        | 0.0  | 17.04       |
5772:     Then Loan Repayment schedule has the following data in Total row:
5773:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5774:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
5775:     And Loan Transactions tab has the following data:
5776:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5777:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5778:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5779:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5780:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
5781:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
5782: #   --- Re-age transaction ---
5783:     When Admin creates a Loan re-aging transaction with the following data:
5784:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
5785:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
5786:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5787:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5788:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5789:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5790:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5791:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5792:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5793:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5794:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5795:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5796:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.25     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5797:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.26     | 0.0  | 0.0       | 14.18 | 0.0   | 0.0        | 0.0  | 14.18       |
5798:     And Loan Repayment schedule has the following data in Total row:
5799:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5800:       | 100.0         | 2.09     | 0.0  | 0.0       | 102.09 | 17.01 | 0.0        | 0.0  | 85.08       |
5801:     And Loan Transactions tab has the following data:
5802:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5803:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5804:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5805:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5806:       | 14 March 2024    | Accrual          | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
5807:       | 15 March 2024    | Re-age           | 85.08  | 83.57     | 1.51     | 0.0  | 0.0       | 0.0          | false    | false    |
5808:   #    --- Interest pause ---
5809:     When Admin sets the business date to "01 July 2024"
5810:     When Admin runs inline COB job for Loan
5811:     And Create an interest pause period with start date "10 February 2024" and end date "10 June 2024"
5812:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
5813:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5814:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5815:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5816:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5817:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
5818:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.03     | 0.0  | 0.0       | 13.96 | 0.0   | 0.0        | 0.0  | 13.96       |
5819:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.03     | 0.0  | 0.0       | 13.96 | 0.0   | 0.0        | 0.0  | 13.96       |
5820:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.03     | 0.0  | 0.0       | 13.96 | 0.0   | 0.0        | 0.0  | 13.96       |
5821:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.03     | 0.0  | 0.0       | 13.96 | 0.0   | 0.0        | 0.0  | 13.96       |
5822:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.03     | 0.0  | 0.0       | 13.96 | 0.0   | 0.0        | 0.0  | 13.96       |
5823:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.04     | 0.0  | 0.0       | 13.96 | 0.0   | 0.0        | 0.0  | 13.96       |
5824:     And Loan Repayment schedule has the following data in Total row:
5825:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5826:       | 100.0         | 0.77     | 0.0  | 0.0       | 100.77 | 17.01 | 0.0        | 0.0  | 83.76       |
5827:     And Loan Transactions tab has the following data without accruals:
5828:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5829:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5830:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5831:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5832:       | 15 March 2024    | Re-age           | 83.76  | 83.57     | 0.19     | 0.0  | 0.0       | 0.0          | false    | true     |
5833:       | 01 April 2024    | Accrual Activity | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | true     |
5834:       | 01 May 2024      | Accrual Activity | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | true     |
5835:       | 01 June 2024     | Accrual Activity | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | true     |
5836:     Then Loan Transactions tab has the following new accrual data:
5837:       | Transaction date | Transaction Type    | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5838:       | 14 March 2024     | Accrual            | 1.27   | 0.0       | 1.27     | 0.0  | 0.0       | 0.0          | false    | false    |
5839:       | 15 March 2024     | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
5840:       | 16 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5841:       | 17 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5842:       | 18 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5843:       | 19 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5844:       | 20 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5845:       | 21 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5846:       | 22 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5847:       | 23 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5848:       | 24 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5849:       | 25 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5850:       | 26 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5851:       | 27 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5852:       | 28 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5853:       | 29 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5854:       | 30 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5855:       | 31 March 2024     | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
5856:       | 01 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5857:       | 02 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5858:       | 03 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5859:       | 05 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5860:       | 06 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5861:       | 07 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5862:       | 08 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5863:       | 09 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5864:       | 10 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5865:       | 12 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5866:       | 13 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5867:       | 14 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5868:       | 15 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5869:       | 17 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5870:       | 18 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5871:       | 19 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5872:       | 20 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5873:       | 21 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5874:       | 22 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5875:       | 24 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5876:       | 25 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5877:       | 26 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5878:       | 27 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5879:       | 29 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5880:       | 30 April 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5881:       | 01 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5882:       | 02 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5883:       | 03 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5884:       | 05 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5885:       | 06 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5886:       | 07 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5887:       | 08 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5888:       | 10 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5889:       | 11 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5890:       | 12 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5891:       | 13 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5892:       | 15 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5893:       | 16 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5894:       | 17 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5895:       | 18 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5896:       | 19 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5897:       | 21 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5898:       | 22 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5899:       | 23 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5900:       | 24 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5901:       | 26 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5902:       | 27 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5903:       | 28 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5904:       | 29 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5905:       | 31 May 2024       | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5906:       | 01 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5907:       | 02 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5908:       | 03 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5909:       | 05 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5910:       | 06 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5911:       | 07 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5912:       | 08 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5913:       | 09 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5914:       | 10 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5915:       | 12 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5916:       | 13 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5917:       | 14 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5918:       | 15 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5919:       | 17 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5920:       | 18 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5921:       | 19 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5922:       | 20 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5923:       | 21 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5924:       | 22 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5925:       | 24 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5926:       | 25 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5927:       | 26 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5928:       | 27 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5929:       | 29 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5930:       | 30 June 2024      | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
5931: #   --- Close loan ---
5932:     When Admin sets the business date to "05 July 2024"
5933:     When Admin runs inline COB job for Loan
5934:     When Loan Pay-off is made on "05 July 2024"
5935:     And Loan Transactions tab has the following data without accruals:
5936:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5937:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5938:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5939:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
5940:       | 15 March 2024    | Re-age           | 83.76  | 83.57     | 0.19     | 0.0  | 0.0       | 0.0          | false    | true     |
5941:       | 01 April 2024    | Accrual Activity | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | true     |
5942:       | 01 May 2024      | Accrual Activity | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | true     |
5943:       | 01 June 2024     | Accrual Activity | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | true     |
5944:       | 01 July 2024     | Accrual Activity | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
5945:       | 05 July 2024     | Repayment        | 83.76  | 83.57     | 0.19     | 0.0  | 0.0       | 0.0          | false    | false    |
5946:       | 05 July 2024     | Accrual Activity | 0.07   | 0.0       | 0.07     | 0.0  | 0.0       | 0.0          | false    | false    |
5947:     Then Loan Transactions tab has the following new accrual data:
5948:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5949:       | 01 July 2024     | Accrual Adjustment | 0.87   | 0.0       | 0.87     | 0.0  | 0.0       | 0.0          | false    | false    |
5950:       | 05 July 2024     | Accrual            | 0.07   | 0.0       | 0.07     | 0.0  | 0.0       | 0.0          | false    | false    |
5951:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
5952: 
5953:   @TestRailId:C4472
5954:   Scenario: Verify Re-aging with loan reschedule: UC1.3: Interest handling: equal amortization + outstanding payable interest, reschedule - extra terms
5955:     When Admin sets the business date to "01 January 2024"
5956:     And Admin creates a client with random data
5957:     And Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
5958:     And Admin creates a fully customized loan with the following data:
5959:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
5960:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
5961:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
5962:     And Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
5963:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5964:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
5965:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
5966:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5967:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5968:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5969:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5970:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
5971:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
5972:     And Loan Repayment schedule has the following data in Total row:
5973:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
5974:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
5975:     And Loan Transactions tab has the following data:
5976:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5977:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5978: #    --- First installment paid ---
5979:     When Admin sets the business date to "01 February 2024"
5980:     When Admin runs inline COB job for Loan
5981:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
5982:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
5983:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
5984:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
5985:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
5986:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5987:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5988:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5989:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
5990:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
5991:     And Loan Repayment schedule has the following data in Total row:
5992:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
5993:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
5994:     And Loan Transactions tab has the following data:
5995:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
5996:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
5997:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
5998:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
5999: #    --- Reschedule ---
6000:     When Admin sets the business date to "02 February 2024"
6001:     When Admin runs inline COB job for Loan
6002:     When Admin creates and approves Loan reschedule with the following data:
6003:       | rescheduleFromDate | submittedOnDate  | adjustedDueDate | graceOnPrincipal | graceOnInterest | extraTerms | newInterestRate |
6004:       | 01 March 2024      | 02 February 2024 |                 |                  |                 | 2          |                 |
6005:     Then Loan Repayment schedule has 8 periods, with the following data for periods:
6006:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6007:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6008:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6009:       | 2  | 29   | 01 March 2024     |                  | 71.84           | 11.73         | 0.49     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6010:       | 3  | 31   | 01 April 2024     |                  | 60.04           | 11.8          | 0.42     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6011:       | 4  | 30   | 01 May 2024       |                  | 48.17           | 11.87         | 0.35     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6012:       | 5  | 31   | 01 June 2024      |                  | 36.23           | 11.94         | 0.28     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6013:       | 6  | 30   | 01 July 2024      |                  | 24.22           | 12.01         | 0.21     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6014:       | 7  | 31   | 01 August 2024    |                  | 12.14           | 12.08         | 0.14     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6015:       | 8  | 31   | 01 September 2024 |                  | 0.0             | 12.14         | 0.07     | 0.0  | 0.0       | 12.21 | 0.0   | 0.0        | 0.0  | 12.21       |
6016:     And Loan Repayment schedule has the following data in Total row:
6017:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6018:       | 100.0         | 2.54     | 0.0  | 0.0       | 102.54 | 17.01 | 0.0        | 0.0  | 85.53       |
6019:     And Loan Transactions tab has the following data:
6020:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6021:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6022:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6023:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6024:       | 01 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6025:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6026: #    --- Check before re-age ---
6027:     When Admin sets the business date to "15 March 2024"
6028:     When Admin runs inline COB job for Loan
6029:     Then Loan Repayment schedule has 8 periods, with the following data for periods:
6030:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6031:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6032:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6033:       | 2  | 29   | 01 March 2024     |                  | 71.84           | 11.73         | 0.49     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6034:       | 3  | 31   | 01 April 2024     |                  | 60.07           | 11.77         | 0.45     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6035:       | 4  | 30   | 01 May 2024       |                  | 48.2            | 11.87         | 0.35     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6036:       | 5  | 31   | 01 June 2024      |                  | 36.26           | 11.94         | 0.28     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6037:       | 6  | 30   | 01 July 2024      |                  | 24.25           | 12.01         | 0.21     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6038:       | 7  | 31   | 01 August 2024    |                  | 12.17           | 12.08         | 0.14     | 0.0  | 0.0       | 12.22 | 0.0   | 0.0        | 0.0  | 12.22       |
6039:       | 8  | 31   | 01 September 2024 |                  | 0.0             | 12.17         | 0.07     | 0.0  | 0.0       | 12.24 | 0.0   | 0.0        | 0.0  | 12.24       |
6040:     And Loan Repayment schedule has the following data in Total row:
6041:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6042:       | 100.0         | 2.57     | 0.0  | 0.0       | 102.57 | 17.01 | 0.0        | 0.0  | 85.56       |
6043:     And Loan Transactions tab has the following data without accruals:
6044:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6045:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6046:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6047:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6048:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
6049:     Then Loan Transactions tab has the following new accrual data:
6050:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6051:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6052:       | 01 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6053:       | 02 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6054:       | 03 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6055:       | 04 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6056:       | 05 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6057:       | 06 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6058:       | 07 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6059:       | 08 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6060:       | 09 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6061:       | 10 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6062:       | 11 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6063:       | 12 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6064:       | 13 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6065:       | 14 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6066:       | 15 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6067:       | 16 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6068:       | 17 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6069:       | 18 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6070:       | 19 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6071:       | 20 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6072:       | 21 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6073:       | 22 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6074:       | 23 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6075:       | 24 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6076:       | 25 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6077:       | 26 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6078:       | 27 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6079:       | 28 February 2024 | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6080:       | 29 February 2024 | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6081:       | 01 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6082:       | 02 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6083:       | 03 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6084:       | 04 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6085:       | 05 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6086:       | 06 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6087:       | 07 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6088:       | 08 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6089:       | 09 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6090:       | 10 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6091:       | 11 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6092:       | 12 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6093:       | 13 March 2024    | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6094:       | 14 March 2024    | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6095: 
6096: #   --- Re-age transaction ---
6097:     When Admin creates a Loan re-aging transaction with the following data:
6098:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
6099:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
6100:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
6101:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6102:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6103:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6104:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6105:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6106:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6107:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6108:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6109:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6110:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6111:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.11     | 0.0  | 0.0       | 14.03 | 0.0   | 0.0        | 0.0  | 14.03       |
6112:     And Loan Repayment schedule has the following data in Total row:
6113:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6114:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
6115:     And Loan Transactions tab has the following data without accruals:
6116:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6117:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6118:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6119:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6120:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
6121:     Then Loan Transactions tab has no new accrual data
6122: #  --- Reschedule after re-age ---
6123:     When Admin sets the business date to "02 April 2024"
6124:     When Admin runs inline COB job for Loan
6125:     When Admin creates and approves Loan reschedule with the following data:
6126:       | rescheduleFromDate | submittedOnDate | adjustedDueDate | graceOnPrincipal | graceOnInterest | extraTerms | newInterestRate |
6127:       | 01 July 2024       | 02 April 2024   |                 |                  |                 | 2          |                 |
6128:     Then Loan Repayment schedule has 11 periods, with the following data for periods:
6129:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6130:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6131:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6132:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6133:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6134:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6135:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6136:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.12     | 0.0  | 0.0       | 14.05 | 0.0   | 0.0        | 0.0  | 14.05       |
6137:       | 7  | 30   | 01 July 2024      |                  | 33.47           | 8.31          | 0.12     | 0.0  | 0.0       | 8.43  | 0.0   | 0.0        | 0.0  | 8.43        |
6138:       | 8  | 31   | 01 August 2024    |                  | 25.16           | 8.31          | 0.12     | 0.0  | 0.0       | 8.43  | 0.0   | 0.0        | 0.0  | 8.43        |
6139:       | 9  | 31   | 01 September 2024 |                  | 16.84           | 8.32          | 0.11     | 0.0  | 0.0       | 8.43  | 0.0   | 0.0        | 0.0  | 8.43        |
6140:       | 10 | 30   | 01 October 2024   |                  | 8.41            | 8.43          | 0.0      | 0.0  | 0.0       | 8.43  | 0.0   | 0.0        | 0.0  | 8.43        |
6141:       | 11 | 31   | 01 November 2024  |                  | 0.0             | 8.41          | 0.0      | 0.0  | 0.0       | 8.41  | 0.0   | 0.0        | 0.0  | 8.41        |
6142:     And Loan Repayment schedule has the following data in Total row:
6143:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6144:       | 100.0         | 1.29     | 0.0  | 0.0       | 101.29 | 17.01 | 0.0        | 0.0  | 84.28       |
6145:     And Loan Transactions tab has the following data without accruals:
6146:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6147:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6148:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6149:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6150:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
6151:       | 01 April 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
6152:     Then Loan Transactions tab has the following new accrual data:
6153:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6154:       | 15 March 2024    | Accrual Adjustment | 0.69   | 0.0       | 0.69     | 0.0  | 0.0       | 0.0          | false    | false    |
6155:       | 16 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6156:       | 18 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6157:       | 19 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6158:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6159:       | 22 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6160:       | 23 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6161:       | 25 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6162:       | 26 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6163:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6164:       | 29 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6165:       | 30 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6166:       | 01 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6167: #   --- Close loan ---
6168:     When Admin sets the business date to "10 April 2024"
6169:     When Admin runs inline COB job for Loan
6170:     When Loan Pay-off is made on "10 April 2024"
6171:     And Loan Transactions tab has the following data without accruals:
6172:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6173:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6174:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6175:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6176:       | 15 March 2024    | Re-age           | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
6177:       | 01 April 2024    | Accrual Activity | 0.12   | 0.0       | 0.12     | 0.0  | 0.0       | 0.0          | false    | false    |
6178:       | 10 April 2024    | Repayment        | 84.28  | 83.57     | 0.71     | 0.0  | 0.0       | 0.0          | false    | false    |
6179:       | 10 April 2024    | Accrual Activity | 0.59   | 0.0       | 0.59     | 0.0  | 0.0       | 0.0          | false    | false    |
6180:     Then Loan Transactions tab has the following new accrual data:
6181:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6182:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6183:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6184:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6185:       | 10 April 2024    | Accrual            | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6186:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
6187: 
6188:   @TestRailId:C4473
6189:   Scenario: Verify Re-aging with loan reschedule: UC3.2: Interest handling: equal amortization + outstanding full interest, reschedule - newInterestRate
6190:     When Admin sets the business date to "01 January 2024"
6191:     And Admin creates a client with random data
6192:     And Admin set "LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL" loan product "DEFAULT" transaction type to "NEXT_INSTALLMENT" future installment allocation rule
6193:     And Admin creates a fully customized loan with the following data:
6194:       | LoanProduct                                                   | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
6195:       | LP2_ADV_CUSTOM_PMT_ALLOC_PROGRESSIVE_LOAN_SCHEDULE_HORIZONTAL | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
6196:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
6197:     And Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
6198:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6199:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
6200:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
6201:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6202:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6203:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6204:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6205:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6206:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
6207:     And Loan Repayment schedule has the following data in Total row:
6208:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6209:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
6210:     And Loan Transactions tab has the following data:
6211:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6212:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6213: #    --- First installment paid ---
6214:     When Admin sets the business date to "01 February 2024"
6215:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 17.01 EUR transaction amount
6216:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6217:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6218:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6219:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6220:       | 2  | 29   | 01 March 2024    |                  | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6221:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6222:       | 4  | 30   | 01 May 2024      |                  | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6223:       | 5  | 31   | 01 June 2024     |                  | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6224:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0   | 0.0        | 0.0  | 17.0        |
6225:     And Loan Repayment schedule has the following data in Total row:
6226:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6227:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 17.01 | 0.0        | 0.0  | 85.04       |
6228:     And Loan Transactions tab has the following data:
6229:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6230:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6231:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6232: #    --- Reschedule before re-age ---
6233:     When Admin sets the business date to "02 February 2024"
6234:     When Admin creates and approves Loan reschedule with the following data:
6235:       | rescheduleFromDate | submittedOnDate  | adjustedDueDate | graceOnPrincipal | graceOnInterest | extraTerms | newInterestRate |
6236:       | 01 March 2024      | 02 February 2024 |                 |                  |                 |            | 10              |
6237:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6238:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6239:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6240:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6241:       | 2  | 29   | 01 March 2024    |                  | 66.97           | 16.6          | 0.49     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6242:       | 3  | 31   | 01 April 2024    |                  | 50.44           | 16.53         | 0.56     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6243:       | 4  | 30   | 01 May 2024      |                  | 33.77           | 16.67         | 0.42     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6244:       | 5  | 31   | 01 June 2024     |                  | 16.96           | 16.81         | 0.28     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6245:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.96         | 0.14     | 0.0  | 0.0       | 17.1  | 0.0   | 0.0        | 0.0  | 17.1        |
6246:     And Loan Repayment schedule has the following data in Total row:
6247:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6248:       | 100.0         | 2.47     | 0.0  | 0.0       | 102.47 | 17.01 | 0.0        | 0.0  | 85.46       |
6249:     And Loan Transactions tab has the following data:
6250:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6251:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6252:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6253: #    --- Check before re-age ---
6254:     When Admin sets the business date to "15 March 2024"
6255:     When Admin runs inline COB job for Loan
6256:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6257:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6258:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6259:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6260:       | 2  | 29   | 01 March 2024    |                  | 66.97           | 16.6          | 0.49     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6261:       | 3  | 31   | 01 April 2024    |                  | 50.5            | 16.47         | 0.62     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6262:       | 4  | 30   | 01 May 2024      |                  | 33.83           | 16.67         | 0.42     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6263:       | 5  | 31   | 01 June 2024     |                  | 17.02           | 16.81         | 0.28     | 0.0  | 0.0       | 17.09 | 0.0   | 0.0        | 0.0  | 17.09       |
6264:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 17.02         | 0.14     | 0.0  | 0.0       | 17.16 | 0.0   | 0.0        | 0.0  | 17.16       |
6265:     And Loan Repayment schedule has the following data in Total row:
6266:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6267:       | 100.0         | 2.53     | 0.0  | 0.0       | 102.53 | 17.01 | 0.0        | 0.0  | 85.52       |
6268:     And Loan Transactions tab has the following data:
6269:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6270:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6271:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6272:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6273:       | 01 March 2024    | Accrual Activity | 0.49   | 0.0       | 0.49     | 0.0  | 0.0       | 0.0          | false    | false    |
6274:       | 14 March 2024    | Accrual          | 1.36   | 0.0       | 1.36    | 0.0  | 0.0       | 0.0          | false    | false    |
6275: 
6276: #   --- Re-age transaction ---
6277:     When Admin creates a Loan re-aging transaction with the following data:
6278:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling            |
6279:       | 1               | MONTHS        | 01 April 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
6280:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
6281:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6282:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6283:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6284:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6285:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6286:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6287:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6288:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6289:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6290:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6291:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.35     | 0.0  | 0.0       | 14.27 | 0.0   | 0.0        | 0.0  | 14.27       |
6292:     And Loan Repayment schedule has the following data in Total row:
6293:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6294:       | 100.0         | 2.53     | 0.0  | 0.0       | 102.53 | 17.01 | 0.0        | 0.0  | 85.52       |
6295:     And Loan Transactions tab has the following data:
6296:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6297:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6298:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6299:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6300:       | 14 March 2024    | Accrual          | 1.36   | 0.0       | 1.36    | 0.0  | 0.0       | 0.0          | false    | false    |
6301:       | 15 March 2024    | Re-age           | 85.52  | 83.57     | 1.95     | 0.0  | 0.0       | 0.0          | false    | false    |
6302:     #    --- Reschedule after re-age ---
6303:     When Admin sets the business date to "02 April 2024"
6304:     When Admin runs inline COB job for Loan
6305:     When Admin creates and approves Loan reschedule with the following data:
6306:       | rescheduleFromDate | submittedOnDate | adjustedDueDate | graceOnPrincipal | graceOnInterest | extraTerms | newInterestRate |
6307:       | 01 May 2024        | 02 April 2024   |                 |                  |                 |            | 12              |
6308:     Then Loan Repayment schedule has 9 periods, with the following data for periods:
6309:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6310:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6311:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6312:       | 2  | 29   | 01 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6313:       | 3  | 14   | 15 March 2024     | 15 March 2024    | 83.57           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0   | 0.0        | 0.0  | 0.0         |
6314:       | 4  | 17   | 01 April 2024     |                  | 69.64           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6315:       | 5  | 30   | 01 May 2024       |                  | 55.71           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6316:       | 6  | 31   | 01 June 2024      |                  | 41.78           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6317:       | 7  | 30   | 01 July 2024      |                  | 27.85           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6318:       | 8  | 31   | 01 August 2024    |                  | 13.92           | 13.93         | 0.32     | 0.0  | 0.0       | 14.25 | 0.0   | 0.0        | 0.0  | 14.25       |
6319:       | 9  | 31   | 01 September 2024 |                  | 0.0             | 13.92         | 0.35     | 0.0  | 0.0       | 14.27 | 0.0   | 0.0        | 0.0  | 14.27       |
6320:     And Loan Repayment schedule has the following data in Total row:
6321:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6322:       | 100.0         | 2.53     | 0.0  | 0.0       | 102.53 | 17.01 | 0.0        | 0.0  | 85.52       |
6323:     And Loan Transactions tab has the following data without accruals:
6324:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6325:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6326:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6327:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6328:       | 15 March 2024    | Re-age           | 85.52  | 83.57     | 1.95     | 0.0  | 0.0       | 0.0          | false    | false    |
6329:       | 01 April 2024    | Accrual Activity | 0.32   | 0.0       | 0.32     | 0.0  | 0.0       | 0.0          | false    | false    |
6330:     Then Loan Transactions tab has the following new accrual data:
6331:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6332:       | 14 March 2024    | Accrual            | 1.36   | 0.0       | 1.36     | 0.0  | 0.0       | 0.0          | false    | false    |
6333:       | 15 March 2024    | Accrual Adjustment | 0.78   | 0.0       | 0.78     | 0.0  | 0.0       | 0.0          | false    | false    |
6334:       | 16 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6335:       | 17 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6336:       | 18 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6337:       | 19 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6338:       | 20 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6339:       | 21 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6340:       | 22 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6341:       | 23 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6342:       | 24 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6343:       | 25 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6344:       | 26 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6345:       | 27 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6346:       | 28 March 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6347:       | 29 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6348:       | 30 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6349:       | 31 March 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6350:       | 01 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6351: 
6352:     When Admin sets the business date to "10 April 2024"
6353:     When Admin runs inline COB job for Loan
6354:     When Loan Pay-off is made on "10 April 2024"
6355:     And Loan Transactions tab has the following data without accruals:
6356:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6357:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6358:       | 01 February 2024 | Repayment        | 17.01  | 16.43     | 0.58     | 0.0  | 0.0       | 83.57        | false    | false    |
6359:       | 01 February 2024 | Accrual Activity | 0.58   | 0.0       | 0.58     | 0.0  | 0.0       | 0.0          | false    | false    |
6360:       | 15 March 2024    | Re-age           | 85.52  | 83.57     | 1.95     | 0.0  | 0.0       | 0.0          | false    | false    |
6361:       | 01 April 2024    | Accrual Activity | 0.32   | 0.0       | 0.32     | 0.0  | 0.0       | 0.0          | false    | false    |
6362:       | 10 April 2024    | Repayment        | 85.52  | 83.57     | 1.95     | 0.0  | 0.0       | 0.0          | false    | false    |
6363:       | 10 April 2024    | Accrual Activity | 1.63   | 0.0       | 1.63     | 0.0  | 0.0       | 0.0          | false    | false    |
6364:     Then Loan Transactions tab has the following new accrual data:
6365:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6366:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6367:       | 03 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6368:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6369:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6370:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6371:       | 07 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6372:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6373:       | 09 April 2024    | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6374:       | 10 April 2024    | Accrual            | 1.54   | 0.0       | 1.54     | 0.0  | 0.0       | 0.0          | false    | false    |
6375:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
6376: 
6377:   @TestRailId:C4474 @AdvancedPaymentAllocation
6378:   Scenario: Verify Loan backdated re-aging during 2nd installment after chargeback on reage start date on a closed period transaction with partially paid installment; adjust to last - interest bearing loan with equal amortization; payable interest - UC1
6379:     When Admin sets the business date to "01 January 2024"
6380:     When Admin creates a client with random data
6381:     When Admin creates a fully customized loan with the following data:
6382:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
6383:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_IR_DAILY_TILL_PRECLOSE_LAST_INSTALLMENT_STRATEGY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
6384:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
6385:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
6386:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6387:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
6388:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
6389:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6390:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6391:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6392:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6393:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6394:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
6395:     Then Loan Repayment schedule has the following data in Total row:
6396:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6397:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
6398:     Then Loan Transactions tab has the following data:
6399:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6400:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6401: 
6402:     When Admin sets the business date to "1 February 2024"
6403:     When Admin runs inline COB job for Loan
6404:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 25 EUR transaction amount
6405:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6406:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6407:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6408:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6409:       | 2  | 29   | 01 March 2024    |                  | 67.0            | 16.57         | 0.44     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6410:       | 3  | 31   | 01 April 2024    |                  | 50.33           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6411:       | 4  | 30   | 01 May 2024      |                  | 33.57           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6412:       | 5  | 31   | 01 June 2024     |                  | 16.71           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6413:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.71         | 0.05     | 0.0  | 0.0       | 16.76 | 7.99  | 7.99       | 0.0  | 8.77        |
6414:     Then Loan Repayment schedule has the following data in Total row:
6415:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6416:       | 100.0         | 1.81     | 0.0  | 0.0       | 101.81 | 25.0 | 7.99       | 0.0  | 76.81       |
6417:     Then Loan Transactions tab has the following data:
6418:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6419:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6420:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6421:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6422: 
6423:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
6424:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6425:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6426:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6427:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6428:       | 2  | 29   | 01 March 2024    |                  | 67.1            | 33.48         | 0.54     | 0.0  | 0.0       | 34.02 | 0.0   | 0.0        | 0.0  | 34.02       |
6429:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6430:       | 4  | 30   | 01 May 2024      |                  | 33.67           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6431:       | 5  | 31   | 01 June 2024     |                  | 16.81           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6432:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.81         | 0.05     | 0.0  | 0.0       | 16.86 | 7.99  | 7.99       | 0.0  | 8.87        |
6433:     Then Loan Repayment schedule has the following data in Total row:
6434:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6435:       | 117.01        | 1.91     | 0.0  | 0.0       | 118.92 | 25.0 | 7.99       | 0.0  | 93.92       |
6436:     Then Loan Transactions tab has the following data:
6437:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6438:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6439:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6440:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6441:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6442: 
6443:     When Admin sets the business date to "1 April 2024"
6444:     When Admin runs inline COB job for Loan
6445:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
6446:       | frequencyNumber | frequencyType | startDate        | numberOfInstallments | reAgeInterestHandling               |
6447:       | 1               | MONTHS        | 15 February 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
6448:     Then Loan Repayment schedule has 8 periods, with the following data for periods:
6449:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6450:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6451:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6452:       | 2  | 14   | 15 February 2024 | 15 February 2024 | 92.59           |  7.99         | 0.0      | 0.0  | 0.0       | 7.99  | 7.99  | 7.99       | 0.0  | 0.0         |
6453:       | 3  |  0   | 15 February 2024 |                  | 77.15           | 15.44         | 0.04     | 0.0  | 0.0       | 15.48 | 0.0   | 0.0        | 0.0  | 15.48       |
6454:       | 4  | 29   | 15 March 2024    |                  | 61.71           | 15.44         | 0.04     | 0.0  | 0.0       | 15.48 | 0.0   | 0.0        | 0.0  | 15.48       |
6455:       | 5  | 31   | 15 April 2024    |                  | 46.27           | 15.44         | 0.04     | 0.0  | 0.0       | 15.48 | 0.0   | 0.0        | 0.0  | 15.48       |
6456:       | 6  | 30   | 15 May 2024      |                  | 30.83           | 15.44         | 0.04     | 0.0  | 0.0       | 15.48 | 0.0   | 0.0        | 0.0  | 15.48       |
6457:       | 7  | 31   | 15 June 2024     |                  | 15.39           | 15.44         | 0.04     | 0.0  | 0.0       | 15.48 | 0.0   | 0.0        | 0.0  | 15.48       |
6458:       | 8  | 30   | 15 July 2024     |                  | 0.0             | 15.39         | 0.06     | 0.0  | 0.0       | 15.45 | 0.0   | 0.0        | 0.0  | 15.45       |
6459:     Then Loan Repayment schedule has the following data in Total row:
6460:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6461:       | 117.01        | 0.84     | 0.0  | 0.0       | 117.85 | 25.0  | 7.99       | 0.0  | 92.85       |
6462:     Then Loan Transactions tab has the following data without accruals:
6463:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6464:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6465:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6466:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6467:       | 15 February 2024 | Re-age           | 92.85  | 92.59     | 0.26     | 0.0  | 0.0       | 0.0          | false    | false    |
6468: 
6469:     Then Loan Transactions tab has the following new accrual data:
6470:       | Transaction date  | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6471:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6472:       | 01 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6473:       | 02 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6474:       | 03 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6475:       | 04 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6476:       | 05 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6477:       | 06 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6478:       | 07 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6479:       | 08 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6480:       | 09 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6481:       | 10 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6482:       | 11 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6483:       | 12 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6484:       | 13 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6485:       | 14 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6486:       | 15 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6487:       | 16 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6488:       | 17 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6489:       | 18 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6490:       | 19 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6491:       | 20 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6492:       | 21 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6493:       | 22 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6494:       | 23 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6495:       | 24 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6496:       | 25 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6497:       | 26 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6498:       | 27 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6499:       | 28 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6500:       | 29 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6501:       | 01 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6502:       | 02 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6503:       | 03 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6504:       | 04 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6505:       | 05 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6506:       | 06 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6507:       | 07 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6508:       | 08 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6509:       | 09 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6510:       | 10 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6511:       | 11 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6512:       | 12 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6513:       | 13 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6514:       | 14 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6515:       | 15 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6516:       | 16 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6517:       | 17 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6518:       | 18 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6519:       | 19 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6520:       | 20 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6521:       | 21 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6522:       | 22 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6523:       | 23 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6524:       | 24 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6525:       | 25 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6526:       | 26 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6527:       | 27 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6528:       | 28 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6529:       | 29 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6530:       | 30 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6531:       | 31 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6532: 
6533:     When Admin sets the business date to "10 April 2024"
6534:     When Admin runs inline COB job for Loan
6535:     When Loan Pay-off is made on "10 April 2024"
6536:     And Loan Transactions tab has the following data without accruals:
6537:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6538:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6539:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6540:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6541:       | 15 February 2024 | Re-age           | 92.85  | 92.59     | 0.26     | 0.0  | 0.0       | 0.0          | false    | false    |
6542:       | 10 April 2024    | Repayment        | 92.85  | 92.59     | 0.26     | 0.0  | 0.0       | 0.0          | false    | false    |
6543:     Then Loan Transactions tab has the following new accrual data:
6544:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6545:       | 01 April 2024    | Accrual Adjustment | 0.96   | 0.0       | 0.96     | 0.0  | 0.0       | 0.0          | false    | false    |
6546:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6547:       | 10 April 2024    | Accrual            | 0.15   | 0.0       | 0.15     | 0.0  | 0.0       | 0.0          | false    | false    |
6548:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
6549: 
6550:   @TestRailId:C4475 @AdvancedPaymentAllocation
6551:   Scenario: Verify Loan backdated re-aging on 2nd due after repay and chargeback on 1st due with partially paid installment; adjust to last - interest bearing loan with equal amortization; full interest - UC2
6552:     When Admin sets the business date to "01 January 2024"
6553:     When Admin creates a client with random data
6554:     When Admin creates a fully customized loan with the following data:
6555:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
6556:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_IR_DAILY_TILL_PRECLOSE_LAST_INSTALLMENT_STRATEGY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
6557:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
6558:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
6559:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6560:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
6561:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
6562:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6563:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6564:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6565:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6566:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6567:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
6568:     Then Loan Repayment schedule has the following data in Total row:
6569:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6570:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
6571:     Then Loan Transactions tab has the following data:
6572:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6573:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6574: 
6575:     When Admin sets the business date to "01 February 2024"
6576:     When Admin runs inline COB job for Loan
6577:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 25 EUR transaction amount
6578:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6579:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6580:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6581:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6582:       | 2  | 29   | 01 March 2024    |                  | 67.0            | 16.57         | 0.44     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6583:       | 3  | 31   | 01 April 2024    |                  | 50.33           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6584:       | 4  | 30   | 01 May 2024      |                  | 33.57           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6585:       | 5  | 31   | 01 June 2024     |                  | 16.71           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6586:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.71         | 0.05     | 0.0  | 0.0       | 16.76 | 7.99  | 7.99       | 0.0  | 8.77        |
6587:     Then Loan Repayment schedule has the following data in Total row:
6588:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6589:       | 100.0         | 1.81     | 0.0  | 0.0       | 101.81 | 25.0 | 7.99       | 0.0  | 76.81       |
6590:     Then Loan Transactions tab has the following data:
6591:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6592:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6593:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6594:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6595: 
6596:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
6597:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6598:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6599:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6600:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6601:       | 2  | 29   | 01 March 2024    |                  | 67.1            | 33.48         | 0.54     | 0.0  | 0.0       | 34.02 | 0.0   | 0.0        | 0.0  | 34.02       |
6602:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6603:       | 4  | 30   | 01 May 2024      |                  | 33.67           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6604:       | 5  | 31   | 01 June 2024     |                  | 16.81           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6605:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.81         | 0.05     | 0.0  | 0.0       | 16.86 | 7.99  | 7.99       | 0.0  | 8.87        |
6606:     Then Loan Repayment schedule has the following data in Total row:
6607:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6608:       | 117.01        | 1.91     | 0.0  | 0.0       | 118.92 | 25.0 | 7.99       | 0.0  | 93.92       |
6609:     Then Loan Transactions tab has the following data:
6610:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6611:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6612:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6613:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6614:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6615: 
6616:     When Admin sets the business date to "1 April 2024"
6617:     When Admin runs inline COB job for Loan
6618:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
6619:       | frequencyNumber | frequencyType | startDate    | numberOfInstallments | reAgeInterestHandling            |
6620:       | 1               | MONTHS        | 1 March 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
6621:     Then Loan Repayment schedule has 8 periods, with the following data for periods:
6622:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6623:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6624:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6625:       | 2  | 29   | 01 March 2024    | 01 March 2024    | 92.59           |  7.99         | 0.0      | 0.0  | 0.0       | 7.99  | 7.99  | 7.99       | 0.0  | 0.0         |
6626:       | 3  |  0   | 01 March 2024    |                  | 77.16           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6627:       | 4  | 31   | 01 April 2024    |                  | 61.73           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6628:       | 5  | 30   | 01 May 2024      |                  | 46.3            | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6629:       | 6  | 31   | 01 June 2024     |                  | 30.87           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6630:       | 7  | 30   | 01 July 2024     |                  | 15.44           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6631:       | 8  | 31   | 01 August 2024   |                  | 0.0             | 15.44         | 0.23     | 0.0  | 0.0       | 15.67 | 0.0   | 0.0        | 0.0  | 15.67       |
6632:     Then Loan Repayment schedule has the following data in Total row:
6633:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6634:       | 117.01        | 1.91     | 0.0  | 0.0       | 118.92 | 25.0  | 7.99       | 0.0  | 93.92       |
6635:     Then Loan Transactions tab has the following data without accruals:
6636:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6637:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6638:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6639:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6640:       | 01 March 2024    | Re-age           | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
6641:     Then Loan Transactions tab has the following new accrual data:
6642:       | Transaction date  | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6643:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6644:       | 01 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6645:       | 02 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6646:       | 03 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6647:       | 04 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6648:       | 05 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6649:       | 06 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6650:       | 07 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6651:       | 08 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6652:       | 09 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6653:       | 10 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6654:       | 11 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6655:       | 12 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6656:       | 13 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6657:       | 14 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6658:       | 15 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6659:       | 16 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6660:       | 17 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6661:       | 18 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6662:       | 19 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6663:       | 20 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6664:       | 21 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6665:       | 22 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6666:       | 23 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6667:       | 24 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6668:       | 25 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6669:       | 26 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6670:       | 27 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6671:       | 28 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6672:       | 29 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6673:       | 01 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6674:       | 02 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6675:       | 03 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6676:       | 04 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6677:       | 05 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6678:       | 06 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6679:       | 07 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6680:       | 08 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6681:       | 09 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6682:       | 10 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6683:       | 11 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6684:       | 12 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6685:       | 13 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6686:       | 14 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6687:       | 15 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6688:       | 16 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6689:       | 17 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6690:       | 18 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6691:       | 19 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6692:       | 20 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6693:       | 21 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6694:       | 22 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6695:       | 23 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6696:       | 24 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6697:       | 25 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6698:       | 26 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6699:       | 27 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6700:       | 28 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6701:       | 29 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6702:       | 30 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6703:       | 31 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6704: 
6705:     When Admin sets the business date to "10 April 2024"
6706:     When Admin runs inline COB job for Loan
6707:     When Loan Pay-off is made on "10 April 2024"
6708:     And Loan Transactions tab has the following data without accruals:
6709:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6710:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6711:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6712:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6713:       | 01 March 2024    | Re-age           | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
6714:       | 10 April 2024    | Repayment        | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
6715:     Then Loan Transactions tab has the following new accrual data:
6716:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6717:       | 01 April 2024    | Accrual Adjustment | 0.62   | 0.0       | 0.62     | 0.0  | 0.0       | 0.0          | false    | false    |
6718:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6719:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6720:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6721:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6722:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6723:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6724:       | 10 April 2024    | Accrual            | 0.83   | 0.0       | 0.83     | 0.0  | 0.0       | 0.0          | false    | false    |
6725:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
6726: 
6727:   @TestRailId:C4476 @AdvancedPaymentAllocation
6728:   Scenario: Verify Loan backdated re-aging on 1st installment after repay and chargeback on 1st due with partially paid installment; adjust to last - interest bearing loan with equal amortization; full interest - UC3
6729:     When Admin sets the business date to "01 January 2024"
6730:     When Admin creates a client with random data
6731:     When Admin creates a fully customized loan with the following data:
6732:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
6733:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_IR_DAILY_TILL_PRECLOSE_LAST_INSTALLMENT_STRATEGY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
6734:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
6735:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
6736:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6737:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
6738:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
6739:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6740:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6741:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6742:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6743:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6744:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
6745:     Then Loan Repayment schedule has the following data in Total row:
6746:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6747:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
6748:     Then Loan Transactions tab has the following data:
6749:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6750:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6751: 
6752:     When Admin sets the business date to "01 February 2024"
6753:     When Admin runs inline COB job for Loan
6754:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 25 EUR transaction amount
6755:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6756:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6757:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6758:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6759:       | 2  | 29   | 01 March 2024    |                  | 67.0            | 16.57         | 0.44     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6760:       | 3  | 31   | 01 April 2024    |                  | 50.33           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6761:       | 4  | 30   | 01 May 2024      |                  | 33.57           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6762:       | 5  | 31   | 01 June 2024     |                  | 16.71           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6763:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.71         | 0.05     | 0.0  | 0.0       | 16.76 | 7.99  | 7.99       | 0.0  | 8.77        |
6764:     Then Loan Repayment schedule has the following data in Total row:
6765:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6766:       | 100.0         | 1.81     | 0.0  | 0.0       | 101.81 | 25.0 | 7.99       | 0.0  | 76.81       |
6767:     Then Loan Transactions tab has the following data:
6768:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6769:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6770:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6771:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6772: 
6773:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
6774:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6775:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6776:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6777:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
6778:       | 2  | 29   | 01 March 2024    |                  | 67.1            | 33.48         | 0.54     | 0.0  | 0.0       | 34.02 | 0.0   | 0.0        | 0.0  | 34.02       |
6779:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6780:       | 4  | 30   | 01 May 2024      |                  | 33.67           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6781:       | 5  | 31   | 01 June 2024     |                  | 16.81           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
6782:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.81         | 0.05     | 0.0  | 0.0       | 16.86 | 7.99  | 7.99       | 0.0  | 8.87        |
6783:     Then Loan Repayment schedule has the following data in Total row:
6784:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6785:       | 117.01        | 1.91     | 0.0  | 0.0       | 118.92 | 25.0 | 7.99       | 0.0  | 93.92       |
6786:     Then Loan Transactions tab has the following data:
6787:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6788:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6789:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6790:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6791:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6792: 
6793:     When Admin sets the business date to "1 April 2024"
6794:     When Admin runs inline COB job for Loan
6795:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
6796:       | frequencyNumber | frequencyType | startDate        | numberOfInstallments | reAgeInterestHandling            |
6797:       | 1               | MONTHS        | 01 February 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
6798:     Then Loan Repayment schedule has 7 periods, with the following data for periods:
6799:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6800:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6801:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 92.59           | 24.42         | 0.58     | 0.0  | 0.0       | 25.0  | 25.0  | 7.99       | 0.0  | 0.0         |
6802:       | 2  |  0   | 01 February 2024 |                  | 77.16           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6803:       | 3  | 29   | 01 March 2024    |                  | 61.73           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6804:       | 4  | 31   | 01 April 2024    |                  | 46.3            | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6805:       | 5  | 30   | 01 May 2024      |                  | 30.87           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6806:       | 6  | 31   | 01 June 2024     |                  | 15.44           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
6807:       | 7  | 30   | 01 July 2024     |                  |  0.0            | 15.44         | 0.23     | 0.0  | 0.0       | 15.67 | 0.0   | 0.0        | 0.0  | 15.67       |
6808:     Then Loan Repayment schedule has the following data in Total row:
6809:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6810:       | 117.01        | 1.91     | 0.0  | 0.0       | 118.92 | 25.0  | 7.99       | 0.0  | 93.92       |
6811:     Then Loan Transactions tab has the following data without accruals:
6812:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6813:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6814:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6815:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6816:       | 01 February 2024 | Re-age           | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
6817: 
6818:     Then Loan Transactions tab has the following new accrual data:
6819:       | Transaction date  | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6820:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
6821:       | 01 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6822:       | 02 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6823:       | 03 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6824:       | 04 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6825:       | 05 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6826:       | 06 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6827:       | 07 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6828:       | 08 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6829:       | 09 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6830:       | 10 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6831:       | 11 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6832:       | 12 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6833:       | 13 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6834:       | 14 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6835:       | 15 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6836:       | 16 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6837:       | 17 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6838:       | 18 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6839:       | 19 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6840:       | 20 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6841:       | 21 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6842:       | 22 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6843:       | 23 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6844:       | 24 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6845:       | 25 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6846:       | 26 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6847:       | 27 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6848:       | 28 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6849:       | 29 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6850:       | 01 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6851:       | 02 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6852:       | 03 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6853:       | 04 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6854:       | 05 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6855:       | 06 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6856:       | 07 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6857:       | 08 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6858:       | 09 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6859:       | 10 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6860:       | 11 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6861:       | 12 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6862:       | 13 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6863:       | 14 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6864:       | 15 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6865:       | 16 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6866:       | 17 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6867:       | 18 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6868:       | 19 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6869:       | 20 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6870:       | 21 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6871:       | 22 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6872:       | 23 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6873:       | 24 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6874:       | 25 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6875:       | 26 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6876:       | 27 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6877:       | 28 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6878:       | 29 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6879:       | 30 March 2024     | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6880:       | 31 March 2024     | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6881: 
6882:     When Admin sets the business date to "10 April 2024"
6883:     When Admin runs inline COB job for Loan
6884:     When Loan Pay-off is made on "10 April 2024"
6885:     And Loan Transactions tab has the following data without accruals:
6886:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6887:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6888:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
6889:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
6890:       | 01 February 2024 | Re-age           | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
6891:       | 10 April 2024    | Repayment        | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
6892:     Then Loan Transactions tab has the following new accrual data:
6893:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6894:       | 01 April 2024    | Accrual Adjustment | 0.4    | 0.0       | 0.4      | 0.0  | 0.0       | 0.0          | false    | false    |
6895:       | 02 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6896:       | 04 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6897:       | 05 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6898:       | 06 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6899:       | 08 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6900:       | 09 April 2024    | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6901:       | 10 April 2024    | Accrual            | 0.61   | 0.0       | 0.61     | 0.0  | 0.0       | 0.0          | false    | false    |
6902:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
6903: 
6904:   @TestRailId:C4477 @AdvancedPaymentAllocation
6905:   Scenario: Verify Loan re-aging trn with repayment and 2nd disb before re-age at the same date - interest bearing multidisb loan with equal amortization; outstanding payable interest - UC1
6906:     When Admin sets the business date to "01 January 2024"
6907:     When Admin creates a client with random data
6908:     When Admin creates a fully customized loan with the following data:
6909:       | LoanProduct                                                                 | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
6910:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_INTEREST_RECALC_DAILY_MULTIDISBURSE | 01 January 2024   | 150            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
6911:     And Admin successfully approves the loan on "01 January 2024" with "150" amount and expected disbursement date on "01 January 2024"
6912:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
6913:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6914:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
6915:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
6916:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6917:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6918:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6919:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6920:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
6921:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
6922:     Then Loan Repayment schedule has the following data in Total row:
6923:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6924:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
6925:     Then Loan Transactions tab has the following data:
6926:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6927:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6928: 
6929:     When Admin sets the business date to "03 January 2024"
6930:     When Admin runs inline COB job for Loan
6931:     When Admin successfully disburse the loan on "03 January 2024" with "50" EUR transaction amount
6932:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
6933:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
6934:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6935:       |    |      | 03 January 2024  |                  |  50.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
6936:       | 1  | 31   | 01 February 2024 |                  | 125.35          | 24.65         | 0.86     | 0.0  | 0.0       | 25.51 | 0.0   | 0.0        | 0.0  | 25.51       |
6937:       | 2  | 29   | 01 March 2024    |                  | 100.57          | 24.78         | 0.73     | 0.0  | 0.0       | 25.51 | 0.0   | 0.0        | 0.0  | 25.51       |
6938:       | 3  | 31   | 01 April 2024    |                  | 75.65           | 24.92         | 0.59     | 0.0  | 0.0       | 25.51 | 0.0   | 0.0        | 0.0  | 25.51       |
6939:       | 4  | 30   | 01 May 2024      |                  | 50.58           | 25.07         | 0.44     | 0.0  | 0.0       | 25.51 | 0.0   | 0.0        | 0.0  | 25.51       |
6940:       | 5  | 31   | 01 June 2024     |                  | 25.37           | 25.21         | 0.3      | 0.0  | 0.0       | 25.51 | 0.0   | 0.0        | 0.0  | 25.51       |
6941:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 25.37         | 0.15     | 0.0  | 0.0       | 25.52 | 0.0   | 0.0        | 0.0  | 25.52       |
6942:     Then Loan Repayment schedule has the following data in Total row:
6943:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
6944:       | 150.0         | 3.07     | 0.0  | 0.0       | 153.07 | 0.0   | 0.0        | 0.0  | 153.07      |
6945:     Then Loan Transactions tab has the following data:
6946:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6947:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6948:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6949:       | 03 January 2024  | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 150.0        | false    | false    |
6950: 
6951:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
6952:       | frequencyNumber | frequencyType | startDate       | numberOfInstallments | reAgeInterestHandling               |
6953:       | 1               | MONTHS        | 04 January 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
6954:     Then Loan Repayment schedule has 7 periods, with the following data for periods:
6955:       | Nr | Days | Date             | Paid date       | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
6956:       |    |      | 01 January 2024  |                 | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
6957:       | 1  | 2    | 03 January 2024  | 03 January 2024 | 100.0           | 0.0           | 0.0      | 0.0  | 0.0       | 0.0   | 0.0  | 0.0        | 0.0  | 0.0         |
6958:       |    |      | 03 January 2024  |                 | 50.0            |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
6959:       | 2  | 1    | 04 January 2024  |                 | 125.0           | 25.0          | 0.01     | 0.0  | 0.0       | 25.01 | 0.0  | 0.0        | 0.0  | 25.01       |
6960:       | 3  | 31   | 04 February 2024 |                 | 100.0           | 25.0          | 0.01     | 0.0  | 0.0       | 25.01 | 0.0  | 0.0        | 0.0  | 25.01       |
6961:       | 4  | 29   | 04 March 2024    |                 | 75.0            | 25.0          | 0.01     | 0.0  | 0.0       | 25.01 | 0.0  | 0.0        | 0.0  | 25.01       |
6962:       | 5  | 31   | 04 April 2024    |                 | 50.0            | 25.0          | 0.01     | 0.0  | 0.0       | 25.01 | 0.0  | 0.0        | 0.0  | 25.01       |
6963:       | 6  | 30   | 04 May 2024      |                 | 24.99           | 25.01         | 0.0      | 0.0  | 0.0       | 25.01 | 0.0  | 0.0        | 0.0  | 25.01       |
6964:       | 7  | 31   | 04 June 2024     |                 | 0.0             | 24.99         | 0.0      | 0.0  | 0.0       | 24.99 | 0.0  | 0.0        | 0.0  | 24.99       |
6965:     Then Loan Repayment schedule has the following data in Total row:
6966:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
6967:       | 150.0         | 0.04     | 0.0  | 0.0       | 150.04 | 0.0  | 0.0        | 0.0  | 150.04      |
6968:     Then Loan Transactions tab has the following data:
6969:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6970:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6971:       | 02 January 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6972:       | 03 January 2024  | Disbursement     | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 150.0        | false    | false    |
6973:       | 03 January 2024  | Re-age           | 150.04 | 150.0     | 0.04     | 0.0  | 0.0       | 0.0          | false    | false    |
6974: 
6975:     When Admin sets the business date to "10 January 2024"
6976:     When Admin runs inline COB job for Loan
6977:     When Loan Pay-off is made on "10 January 2024"
6978:     Then Loan Transactions tab has the following data:
6979:       | Transaction date | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
6980:       | 01 January 2024  | Disbursement       | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
6981:       | 02 January 2024  | Accrual            | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6982:       | 03 January 2024  | Disbursement       | 50.0   | 0.0       | 0.0      | 0.0  | 0.0       | 150.0        | false    | false    |
6983:       | 03 January 2024  | Re-age             | 150.04 | 150.0     | 0.04     | 0.0  | 0.0       | 0.0          | false    | false    |
6984:       | 03 January 2024  | Accrual Adjustment | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
6985:       | 04 January 2024  | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
6986:       | 10 January 2024  | Repayment          | 150.04 | 150.0     | 0.04     | 0.0  | 0.0       | 0.0          | false    | false    |
6987:       | 10 January 2024  | Accrual            | 0.03   | 0.0       | 0.03     | 0.0  | 0.0       | 0.0          | false    | false    |
6988:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
6989: 
6990:   @TestRailId:C4478 @AdvancedPaymentAllocation
6991:   Scenario: Verify Loan re-aging on 1st installment after repay and chargeback on 1st due with partially paid installment; adjust to last - interest bearing loan with equal amortization; outstanding payable interest - UC4.1
6992:     When Admin sets the business date to "01 January 2024"
6993:     When Admin creates a client with random data
6994:     When Admin creates a fully customized loan with the following data:
6995:       | LoanProduct                                                                               | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
6996:       | LP2_ADV_PYMNT_INTEREST_DAILY_INTEREST_RECALC_EMI_360_30_CHARGEBACK_PRINCIPAL_INTEREST_FEE | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
6997:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
6998:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
6999:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
7000:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
7001:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
7002:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7003:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7004:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7005:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7006:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7007:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
7008:     Then Loan Repayment schedule has the following data in Total row:
7009:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
7010:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
7011:     Then Loan Transactions tab has the following data:
7012:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7013:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7014: 
7015:     When Admin sets the business date to "01 February 2024"
7016:     When Admin runs inline COB job for Loan
7017:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 25 EUR transaction amount
7018:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
7019:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
7020:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
7021:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
7022:       | 2  | 29   | 01 March 2024    |                  | 67.0            | 16.57         | 0.44     | 0.0  | 0.0       | 17.01 | 7.99  | 7.99       | 0.0  | 9.02       |
7023:       | 3  | 31   | 01 April 2024    |                  | 50.38           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7024:       | 4  | 30   | 01 May 2024      |                  | 33.66           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7025:       | 5  | 31   | 01 June 2024     |                  | 16.85           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7026:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.85         | 0.1      | 0.0  | 0.0       | 16.95 | 0.0   | 0.0        | 0.0  | 16.95       |
7027:     Then Loan Repayment schedule has the following data in Total row:
7028:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
7029:       | 100.0         | 2.0      | 0.0  | 0.0       | 102.0  | 25.0 | 7.99       | 0.0  | 77.0        |
7030:     Then Loan Transactions tab has the following data:
7031:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7032:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7033:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
7034:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7035: 
7036:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
7037:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
7038:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
7039:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
7040:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
7041:       | 2  | 29   | 01 March 2024    |                  | 67.1            | 33.48         | 0.54     | 0.0  | 0.0       | 34.02 | 7.99  | 7.99       | 0.0  | 26.03      |
7042:       | 3  | 31   | 01 April 2024    |                  | 50.48           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7043:       | 4  | 30   | 01 May 2024      |                  | 33.76           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7044:       | 5  | 31   | 01 June 2024     |                  | 16.95           | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7045:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.95         | 0.1      | 0.0  | 0.0       | 17.05 | 0.0   | 0.0        | 0.0  | 17.05       |
7046:     Then Loan Repayment schedule has the following data in Total row:
7047:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
7048:       | 117.01        | 2.1      | 0.0  | 0.0       | 119.11 | 25.0 | 7.99       | 0.0  | 94.11       |
7049:     Then Loan Transactions tab has the following data:
7050:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7051:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7052:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
7053:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7054:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
7055: 
7056:     When Admin sets the business date to "21 February 2024"
7057:     When Admin runs inline COB job for Loan
7058:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
7059:       | frequencyNumber | frequencyType | startDate     | numberOfInstallments | reAgeInterestHandling               |
7060:       | 1               | MONTHS        | 01 March 2024 | 6                    | EQUAL_AMORTIZATION_PAYABLE_INTEREST |
7061:     Then Loan Repayment schedule has 8 periods, with the following data for periods:
7062:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
7063:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
7064:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
7065:       | 2  | 20   | 21 February 2024 | 21 February 2024 | 92.59           |  7.99         | 0.0      | 0.0  | 0.0       | 7.99  | 7.99  | 7.99       | 0.0  | 0.0         |
7066:       | 3  |  9   | 01 March 2024    |                  | 77.16           | 15.43         | 0.06     | 0.0  | 0.0       | 15.49 | 0.0   | 0.0        | 0.0  | 15.49       |
7067:       | 4  | 31   | 01 April 2024    |                  | 61.73           | 15.43         | 0.06     | 0.0  | 0.0       | 15.49 | 0.0   | 0.0        | 0.0  | 15.49       |
7068:       | 5  | 30   | 01 May 2024      |                  | 46.3            | 15.43         | 0.06     | 0.0  | 0.0       | 15.49 | 0.0   | 0.0        | 0.0  | 15.49       |
7069:       | 6  | 31   | 01 June 2024     |                  | 30.87           | 15.43         | 0.06     | 0.0  | 0.0       | 15.49 | 0.0   | 0.0        | 0.0  | 15.49       |
7070:       | 7  | 30   | 01 July 2024     |                  | 15.44           | 15.43         | 0.06     | 0.0  | 0.0       | 15.49 | 0.0   | 0.0        | 0.0  | 15.49       |
7071:       | 8  | 31   | 01 August 2024   |                  | 0.0             | 15.44         | 0.07     | 0.0  | 0.0       | 15.51 | 0.0   | 0.0        | 0.0  | 15.51       |
7072:     Then Loan Repayment schedule has the following data in Total row:
7073:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
7074:       | 117.01        | 0.95     | 0.0  | 0.0       | 117.96 | 25.0  | 7.99       | 0.0  | 92.96       |
7075:     Then Loan Transactions tab has the following data without accruals:
7076:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7077:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7078:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7079:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
7080:       | 21 February 2024 | Re-age           | 92.96  | 92.59     | 0.37     | 0.0  | 0.0       | 0.0          | false    | false    |
7081:     Then Loan Transactions tab has the following new accrual data:
7082:       | Transaction date  | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7083:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
7084:       | 01 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7085:       | 02 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7086:       | 03 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7087:       | 04 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7088:       | 05 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7089:       | 06 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7090:       | 07 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7091:       | 08 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7092:       | 09 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7093:       | 10 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7094:       | 11 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7095:       | 12 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7096:       | 13 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7097:       | 14 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7098:       | 15 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7099:       | 16 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7100:       | 17 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7101:       | 18 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7102:       | 19 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7103:       | 20 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7104: 
7105:     When Admin sets the business date to "02 March 2024"
7106:     When Admin runs inline COB job for Loan
7107:     When Loan Pay-off is made on "02 March 2024"
7108:     And Loan Transactions tab has the following data without accruals:
7109:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7110:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7111:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7112:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
7113:       | 21 February 2024 | Re-age           | 92.96  | 92.59     | 0.37     | 0.0  | 0.0       | 0.0          | false    | false    |
7114:       | 02 March 2024    | Repayment        | 92.96  | 92.59     | 0.37     | 0.0  | 0.0       | 0.0          | false    | false    |
7115:     Then Loan Transactions tab has the following new accrual data:
7116:       | Transaction date | Transaction Type    | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7117:       | 21 February 2024  | Accrual Adjustment | 0.35   | 0.0       | 0.35     | 0.0  | 0.0       | 0.0          | false    | false    |
7118:       | 22 February 2024  | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7119:       | 24 February 2024  | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7120:       | 25 February 2024  | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7121:       | 27 February 2024  | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7122:       | 28 February 2024  | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7123:       | 01 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7124:       | 02 March 2024     | Accrual            | 0.31   | 0.0       | 0.31     | 0.0  | 0.0       | 0.0          | false    | false    |
7125:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
7126: 
7127:   @TestRailId:C4479 @AdvancedPaymentAllocation
7128:   Scenario: Verify Loan re-aging on date after maturity date after repay and chargeback on 1st due with partially paid installment; adjust to last - interest bearing loan with equal amortization; outstanding full interest - UC4.3
7129:     When Admin sets the business date to "01 January 2024"
7130:     When Admin creates a client with random data
7131:     When Admin creates a fully customized loan with the following data:
7132:       | LoanProduct                                                                              | submitted on date | with Principal | ANNUAL interest rate % | interest type     | interest calculation period | amortization type  | loanTermFrequency | loanTermFrequencyType | repaymentEvery | repaymentFrequencyType | numberOfRepayments | graceOnPrincipalPayment | graceOnInterestPayment | interest free period | Payment strategy            |
7133:       | LP2_ADV_PYMNT_INTEREST_DAILY_EMI_360_30_IR_DAILY_TILL_PRECLOSE_LAST_INSTALLMENT_STRATEGY | 01 January 2024   | 100            | 7                      | DECLINING_BALANCE | DAILY                       | EQUAL_INSTALLMENTS | 6                 | MONTHS                | 1              | MONTHS                 | 6                  | 0                       | 0                      | 0                    | ADVANCED_PAYMENT_ALLOCATION |
7134:     And Admin successfully approves the loan on "01 January 2024" with "100" amount and expected disbursement date on "01 January 2024"
7135:     When Admin successfully disburse the loan on "01 January 2024" with "100" EUR transaction amount
7136:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
7137:       | Nr | Days | Date             | Paid date | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid | In advance | Late | Outstanding |
7138:       |    |      | 01 January 2024  |           | 100.0           |               |          | 0.0  |           | 0.0   | 0.0  |            |      |             |
7139:       | 1  | 31   | 01 February 2024 |           | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7140:       | 2  | 29   | 01 March 2024    |           | 67.05           | 16.52         | 0.49     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7141:       | 3  | 31   | 01 April 2024    |           | 50.43           | 16.62         | 0.39     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7142:       | 4  | 30   | 01 May 2024      |           | 33.71           | 16.72         | 0.29     | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7143:       | 5  | 31   | 01 June 2024     |           | 16.9            | 16.81         | 0.2      | 0.0  | 0.0       | 17.01 | 0.0  | 0.0        | 0.0  | 17.01       |
7144:       | 6  | 30   | 01 July 2024     |           | 0.0             | 16.9          | 0.1      | 0.0  | 0.0       | 17.0  | 0.0  | 0.0        | 0.0  | 17.0        |
7145:     Then Loan Repayment schedule has the following data in Total row:
7146:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
7147:       | 100.0         | 2.05     | 0.0  | 0.0       | 102.05 | 0.0  | 0.0        | 0.0  | 102.05      |
7148:     Then Loan Transactions tab has the following data:
7149:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7150:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7151: 
7152:     When Admin sets the business date to "01 February 2024"
7153:     When Admin runs inline COB job for Loan
7154:     And Customer makes "AUTOPAY" repayment on "01 February 2024" with 25 EUR transaction amount
7155:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
7156:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
7157:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
7158:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
7159:       | 2  | 29   | 01 March 2024    |                  | 67.0            | 16.57         | 0.44     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7160:       | 3  | 31   | 01 April 2024    |                  | 50.33           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7161:       | 4  | 30   | 01 May 2024      |                  | 33.57           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7162:       | 5  | 31   | 01 June 2024     |                  | 16.71           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7163:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.71         | 0.05     | 0.0  | 0.0       | 16.76 | 7.99  | 7.99       | 0.0  | 8.77        |
7164:     Then Loan Repayment schedule has the following data in Total row:
7165:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
7166:       | 100.0         | 1.81     | 0.0  | 0.0       | 101.81 | 25.0 | 7.99       | 0.0  | 76.81       |
7167:     Then Loan Transactions tab has the following data:
7168:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7169:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7170:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
7171:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7172: 
7173:     When Admin makes "REPAYMENT_ADJUSTMENT_CHARGEBACK" chargeback with 17.01 EUR transaction amount
7174:     Then Loan Repayment schedule has 6 periods, with the following data for periods:
7175:       | Nr | Days | Date             | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
7176:       |    |      | 01 January 2024  |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
7177:       | 1  | 31   | 01 February 2024 | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
7178:       | 2  | 29   | 01 March 2024    |                  | 67.1            | 33.48         | 0.54     | 0.0  | 0.0       | 34.02 | 0.0   | 0.0        | 0.0  | 34.02       |
7179:       | 3  | 31   | 01 April 2024    |                  | 50.43           | 16.67         | 0.34     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7180:       | 4  | 30   | 01 May 2024      |                  | 33.67           | 16.76         | 0.25     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7181:       | 5  | 31   | 01 June 2024     |                  | 16.81           | 16.86         | 0.15     | 0.0  | 0.0       | 17.01 | 0.0   | 0.0        | 0.0  | 17.01       |
7182:       | 6  | 30   | 01 July 2024     |                  | 0.0             | 16.81         | 0.05     | 0.0  | 0.0       | 16.86 | 7.99  | 7.99       | 0.0  | 8.87        |
7183:     Then Loan Repayment schedule has the following data in Total row:
7184:       | Principal due | Interest | Fees | Penalties | Due    | Paid | In advance | Late | Outstanding |
7185:       | 117.01        | 1.91     | 0.0  | 0.0       | 118.92 | 25.0 | 7.99       | 0.0  | 93.92       |
7186:     Then Loan Transactions tab has the following data:
7187:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7188:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7189:       | 31 January 2024  | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
7190:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7191:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
7192: 
7193:     When Admin sets the business date to "01 March 2024"
7194:     When Admin runs inline COB job for Loan
7195:     When Admin creates a Loan re-aging transaction by Loan external ID with the following data:
7196:       | frequencyNumber | frequencyType | startDate      | numberOfInstallments | reAgeInterestHandling             |
7197:       | 1               | MONTHS        | 01 August 2024 | 6                    | EQUAL_AMORTIZATION_FULL_INTEREST |
7198:     Then Loan Repayment schedule has 8 periods, with the following data for periods:
7199:       | Nr | Days | Date              | Paid date        | Balance of loan | Principal due | Interest | Fees | Penalties | Due   | Paid  | In advance | Late | Outstanding |
7200:       |    |      | 01 January 2024   |                  | 100.0           |               |          | 0.0  |           | 0.0   | 0.0   |            |      |             |
7201:       | 1  | 31   | 01 February 2024  | 01 February 2024 | 83.57           | 16.43         | 0.58     | 0.0  | 0.0       | 17.01 | 17.01 | 0.0        | 0.0  | 0.0         |
7202:       | 2  | 29   | 01 March 2024     | 01 March 2024    | 92.59           |  7.99         | 0.0      | 0.0  | 0.0       | 7.99  | 7.99  | 7.99       | 0.0  | 0.0         |
7203:       | 3  | 153  | 01 August 2024    |                  | 77.16           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
7204:       | 4  | 31   | 01 September 2024 |                  | 61.73           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
7205:       | 5  | 30   | 01 October 2024   |                  | 46.3            | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
7206:       | 6  | 31   | 01 November 2024  |                  | 30.87           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
7207:       | 7  | 30   | 01 December 2024  |                  | 15.44           | 15.43         | 0.22     | 0.0  | 0.0       | 15.65 | 0.0   | 0.0        | 0.0  | 15.65       |
7208:       | 8  | 31   | 01 January 2025   |                  |  0.0            | 15.44         | 0.23     | 0.0  | 0.0       | 15.67 | 0.0   | 0.0        | 0.0  | 15.67       |
7209:     Then Loan Repayment schedule has the following data in Total row:
7210:       | Principal due | Interest | Fees | Penalties | Due    | Paid  | In advance | Late | Outstanding |
7211:       | 117.01        | 1.91     | 0.0  | 0.0       | 118.92 | 25.0  | 7.99       | 0.0  | 93.92       |
7212:     Then Loan Transactions tab has the following data without accruals:
7213:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7214:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7215:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7216:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
7217:       | 01 March 2024    | Re-age           | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
7218:     Then Loan Transactions tab has the following new accrual data:
7219:       | Transaction date  | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7220:       | 31 January 2024   | Accrual          | 0.56   | 0.0       | 0.56     | 0.0  | 0.0       | 0.0          | false    | false    |
7221:       | 01 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7222:       | 02 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7223:       | 03 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7224:       | 04 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7225:       | 05 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7226:       | 06 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7227:       | 07 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7228:       | 08 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7229:       | 09 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7230:       | 10 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7231:       | 11 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7232:       | 12 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7233:       | 13 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7234:       | 14 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7235:       | 15 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7236:       | 16 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7237:       | 17 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7238:       | 18 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7239:       | 19 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7240:       | 20 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7241:       | 21 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7242:       | 22 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7243:       | 23 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7244:       | 24 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7245:       | 25 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7246:       | 26 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7247:       | 27 February 2024  | Accrual          | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7248:       | 28 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7249:       | 29 February 2024  | Accrual          | 0.02   | 0.0       | 0.02     | 0.0  | 0.0       | 0.0          | false    | false    |
7250: 
7251:     When Admin sets the business date to "10 March 2024"
7252:     When Admin runs inline COB job for Loan
7253:     When Loan Pay-off is made on "10 March 2024"
7254:     Then Loan Transactions tab has the following data without accruals:
7255:       | Transaction date | Transaction Type | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7256:       | 01 January 2024  | Disbursement     | 100.0  | 0.0       | 0.0      | 0.0  | 0.0       | 100.0        | false    | false    |
7257:       | 01 February 2024 | Repayment        | 25.0   | 24.42     | 0.58     | 0.0  | 0.0       | 75.58        | false    | false    |
7258:       | 01 February 2024 | Chargeback       | 17.01  | 17.01     | 0.0      | 0.0  | 0.0       | 92.59        | false    | false    |
7259:       | 01 March 2024    | Re-age           | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
7260:       | 10 March 2024    | Repayment        | 93.92  | 92.59     | 1.33     | 0.0  | 0.0       | 0.0          | false    | false    |
7261:     Then Loan Transactions tab has the following new accrual data:
7262:       | Transaction date  | Transaction Type   | Amount | Principal | Interest | Fees | Penalties | Loan Balance | Reverted | Replayed |
7263:       | 01 March 2024     | Accrual Adjustment | 0.52   | 0.0       | 0.52     | 0.0  | 0.0       | 0.0          | false    | false    |
7264:       | 05 March 2024     | Accrual            | 0.01   | 0.0       | 0.01     | 0.0  | 0.0       | 0.0          | false    | false    |
7265:       | 10 March 2024     | Accrual            | 1.32   | 0.0       | 1.32     | 0.0  | 0.0       | 0.0          | false    | false    |
7266:     Then Loan is closed with zero outstanding balance and it's all installments have obligations met
```
