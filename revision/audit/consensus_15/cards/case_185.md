# Case 185 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026; confidence of the comparison: high. The business date stays at 01/01/2027; the pause starting 15/01 is not yet active, but Then already checks PAUSED; resume on 01/02 (other cases 20/01,25/01) is still expected to succeed although AC4 requires resumeStartDate = current business date. There is no advance-date step. This is the same timeline defect repeated across many scenarios; each repetition is not counted. Fix the business date per case before the resume; do not change the requirement to legitimize the output. Coverage: 4/15. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(correct): UC1 and the other scenarios create a pause with start/end date.|AC2, 3(correct): UC1 checks that the history has PAUSE with startDate and endDate.|AC4(wrong): the system date is always 01/01/2027 but the resume date is 01/02, 20/01 or 25/01, which does not match the current date as AC4 requires.|AC5(correct): UC1 and UC7 check that the history has RESUME and startDate.|AC6, AC7(correct): UC1, UC7, UC8 check that pauseEndDate is shortened to the resume date (01 Feb, 20 Jan, 25 Jan, all earlier than 15 Feb).|AC8(correct): all resume steps are “by loan id”.|AC9 (correct): UC3 creates no pause and then the resume fails.|AC10(correct): UC4 and UC2 row 31 December 2026 (before the business date) are rejected.|AC11 (correct): the business date is 01/01/2027 but the test resumes on 15/01 (the pause start date). Since today is not yet 15/01, it is not certain that the rejection error is due to coinciding with the pause start.|AC12(correct): UC6 a second resume for the same pause is rejected.|AC13, AC14(correct): UC7 checks that the schedule is updated immediately after the resume and reflects updated period boundaries and delinquent day calculations.|AC15(correct): UC1 has fully repays and closes the working capital loan account.|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026. The business date stays at 01/01/2027; the pause starting 15/01 is not yet active, but Then already checks PAUSED; resume on 01/02 (other cases 20/01,25/01) is still expected to succeed although AC4 requires resumeStartDate = current business date. There is no advance-date step. This is the same timeline defect repeated across many scenarios; each repetition is not counted. Fix the business date per case before the resume; do not change the requirement to legitimize the output. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
The ACs state the initial states clearly (pause active, no pause yet, already resumed, after pause/resume).|The Given already has the business date and a product with delinquency tracking; the loan data is fully built.|The When is the right kind of action (create pause, resume by loan id).|Each expected result has at least one Then.|The business date stays at 01 January 2027, before even the pause start (15 January). The pause is created for the future and then resumed (and checked as “active”) before its start date is reached, similar to “repayment before disbursement”. | ACS WITH PRECONDITION: AC2, AC3, AC4, AC6, AC9, AC12, AC15

## User story

```text
0001: As a loan administrator,
0002: I want to pause and resume delinquency tracking on working capital loans,
0003: So that delinquency schedules reflect temporary pauses accurately and prevent invalid resume actions.
0004: 
0005: Acceptance Criteria:
0006: - A delinquency pause can be created for a working capital loan with a start date and end date.
0007: - When a pause is active, the delinquency action history records the PAUSE action with its start and end dates.
0008: - When a pause is active, the delinquency range schedule is generated and reflects the paused delinquency period.
0009: - Resuming delinquency during an active pause is allowed when the resume start date is the current business date.
0010: - A valid resume action is recorded in the delinquency action history with action RESUME and the resume start date.
0011: - Resuming during an active pause shortens the delinquency range schedule end date based on the resume date.
0012: - If the resume date is earlier than the planned pause end date, the delinquency range schedule is shortened accordingly.
0013: - A resume can be initiated by loan ID.
0014: - A resume cannot be created if there is no active pause.
0015: - A resume cannot be backdated before the current business date.
0016: - A resume cannot occur on the same date as the pause start date.
0017: - A second resume cannot be created for the same pause once the pause has already been resumed.
0018: - When delinquency is resumed, delinquency recalculation happens immediately and updates the delinquency range schedule.
0019: - The delinquency range schedule after resume must reflect updated period boundaries and delinquent day calculations.
0020: - The working capital loan can be fully repaid and closed after pause/resume processing.
```

## Generated Gherkin C0

```text
0001: @WorkingCapital
0002: @WorkingCapitalDelinquencyPauseResumeFeature
0003: Feature: Working Capital Delinquency Pause and Resume Management
0004: 
0005:   @TestRailId:C76707
0006:   Scenario: Verify Working Capital Delinquency Pause creation, history recording, schedule generation, and loan closure after pause/resume processing - UC1
0007:     Given Admin sets the business date to "01 January 2027"
0008:     And Admin creates a client with random data
0009:     And Admin creates a working capital loan product with delinquency tracking enabled
0010:     And Admin creates a working capital loan account for the client with the following values
0011:       | loan_field_name                         | loan_field_value        |
0012:       | principal                               | 100000                  |
0013:       | numberOfRepayments                      | 12                      |
0014:       | repaymentEvery                          | 1                       |
0015:       | repaymentFrequencyType                  | MONTHS                  |
0016:       | interestRatePerPeriod                   | 2.5                     |
0017:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0018:       | interestType                            | FLAT                    |
0019:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0020:       | expectedDisbursementDate                | 01 January 2027         |
0021:       | submittedOnDate                         | 01 January 2027         |
0022:       | disbursementDate                        | 01 January 2027         |
0023:       | delinquencyPauseStartDate                | 15 January 2027         |
0024:       | delinquencyPauseEndDate                  | 15 February 2027        |
0025:     When Admin creates a delinquency pause for the working capital loan
0026:     Then Check delinquency action history contains the following values
0027:       | delinquency_action_field_name | delinquency_action_field_value |
0028:       | action                        | PAUSE                          |
0029:       | startDate                     | 15 January 2027                |
0030:       | endDate                       | 15 February 2027               |
0031:     Then Check delinquency range schedule contains the following values
0032:       | delinquency_schedule_field_name | delinquency_schedule_field_value |
0033:       | pauseStartDate                  | 15 January 2027                  |
0034:       | pauseEndDate                    | 15 February 2027                 |
0035:       | scheduleStatus                  | PAUSED                           |
0036:     When Admin resumes delinquency for the working capital loan by loan id with resume start date "01 February 2027"
0037:     Then Check delinquency action history contains the following values
0038:       | delinquency_action_field_name | delinquency_action_field_value |
0039:       | action                        | RESUME                         |
0040:       | startDate                     | 01 February 2027               |
0041:     Then Check delinquency range schedule contains the following values
0042:       | delinquency_schedule_field_name | delinquency_schedule_field_value |
0043:       | pauseStartDate                  | 15 January 2027                  |
0044:       | pauseEndDate                    | 01 February 2027                 |
0045:       | scheduleStatus                  | RESUMED                          |
0046:     When Admin fully repays the working capital loan
0047:     Then Admin closes the working capital loan account
0048: 
0049:   @TestRailId:C76708
0050:   Scenario Outline: Verify Working Capital Delinquency Resume validation with invalid data shall outcome with error - UC2
0051:     Given Admin sets the business date to "01 January 2027"
0052:     And Admin creates a client with random data
0053:     And Admin creates a working capital loan product with delinquency tracking enabled
0054:     And Admin creates a working capital loan account for the client with the following values
0055:       | loan_field_name                         | loan_field_value        |
0056:       | principal                               | 100000                  |
0057:       | numberOfRepayments                      | 12                      |
0058:       | repaymentEvery                          | 1                       |
0059:       | repaymentFrequencyType                  | MONTHS                  |
0060:       | interestRatePerPeriod                   | 2.5                     |
0061:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0062:       | interestType                            | FLAT                    |
0063:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0064:       | expectedDisbursementDate                | 01 January 2027         |
0065:       | submittedOnDate                         | 01 January 2027         |
0066:       | disbursementDate                        | 01 January 2027         |
0067:       | delinquencyPauseStartDate                | 15 January 2027         |
0068:       | delinquencyPauseEndDate                  | 15 February 2027        |
0069:     When Admin creates a delinquency pause for the working capital loan
0070:     Then Admin failed to resume delinquency for field "<delinquency_resume_field_name_invalid>" with invalid data <delinquency_resume_field_value_invalid> results with an error <delinquency_resume_error_message>
0071: 
0072:     Examples:
0073:       | delinquency_resume_field_name_invalid | delinquency_resume_field_value_invalid | delinquency_resume_error_message                                                                 |
0074:       | resumeStartDate                      | "null"                                | The parameter `resumeStartDate` is mandatory.                                                   |
0075:       | resumeStartDate                      | ""                                    | The parameter `resumeStartDate` is mandatory.                                                   |
0076:       | resumeStartDate                      | "31 December 2026"                    | The parameter `resumeStartDate` cannot be before the current business date.                    |
0077:       | resumeStartDate                      | "15 January 2027"                    | The parameter `resumeStartDate` cannot be the same as the pause start date.                    |
0078: 
0079:   @TestRailId:C76709
0080:   Scenario: Verify Working Capital Delinquency Resume creation with no active pause outcomes with error - UC3
0081:     Given Admin sets the business date to "01 January 2027"
0082:     And Admin creates a client with random data
0083:     And Admin creates a working capital loan product with delinquency tracking enabled
0084:     And Admin creates a working capital loan account for the client with the following values
0085:       | loan_field_name                         | loan_field_value        |
0086:       | principal                               | 100000                  |
0087:       | numberOfRepayments                      | 12                      |
0088:       | repaymentEvery                          | 1                       |
0089:       | repaymentFrequencyType                  | MONTHS                  |
0090:       | interestRatePerPeriod                   | 2.5                     |
0091:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0092:       | interestType                            | FLAT                    |
0093:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0094:       | expectedDisbursementDate                | 01 January 2027         |
0095:       | submittedOnDate                         | 01 January 2027         |
0096:       | disbursementDate                        | 01 January 2027         |
0097:     Then Admin failed to resume delinquency for working capital loan by loan id with no active pause
0098: 
0099:   @TestRailId:C76710
0100:   Scenario: Verify Working Capital Delinquency Resume cannot be backdated before current business date - UC4
0101:     Given Admin sets the business date to "01 January 2027"
0102:     And Admin creates a client with random data
0103:     And Admin creates a working capital loan product with delinquency tracking enabled
0104:     And Admin creates a working capital loan account for the client with the following values
0105:       | loan_field_name                         | loan_field_value        |
0106:       | principal                               | 100000                  |
0107:       | numberOfRepayments                      | 12                      |
0108:       | repaymentEvery                          | 1                       |
0109:       | repaymentFrequencyType                  | MONTHS                  |
0110:       | interestRatePerPeriod                   | 2.5                     |
0111:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0112:       | interestType                            | FLAT                    |
0113:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0114:       | expectedDisbursementDate                | 01 January 2027         |
0115:       | submittedOnDate                         | 01 January 2027         |
0116:       | disbursementDate                        | 01 January 2027         |
0117:       | delinquencyPauseStartDate                | 15 January 2027         |
0118:       | delinquencyPauseEndDate                  | 15 February 2027        |
0119:     When Admin creates a delinquency pause for the working capital loan
0120:     Then Admin failed to resume delinquency for working capital loan by loan id with resume start date "31 December 2026" because it is before the current business date
0121: 
0122:   @TestRailId:C76711
0123:   Scenario: Verify Working Capital Delinquency Resume cannot occur on the same date as pause start date - UC5
0124:     Given Admin sets the business date to "01 January 2027"
0125:     And Admin creates a client with random data
0126:     And Admin creates a working capital loan product with delinquency tracking enabled
0127:     And Admin creates a working capital loan account for the client with the following values
0128:       | loan_field_name                         | loan_field_value        |
0129:       | principal                               | 100000                  |
0130:       | numberOfRepayments                      | 12                      |
0131:       | repaymentEvery                          | 1                       |
0132:       | repaymentFrequencyType                  | MONTHS                  |
0133:       | interestRatePerPeriod                   | 2.5                     |
0134:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0135:       | interestType                            | FLAT                    |
0136:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0137:       | expectedDisbursementDate                | 01 January 2027         |
0138:       | submittedOnDate                         | 01 January 2027         |
0139:       | disbursementDate                        | 01 January 2027         |
0140:       | delinquencyPauseStartDate                | 15 January 2027         |
0141:       | delinquencyPauseEndDate                  | 15 February 2027        |
0142:     When Admin creates a delinquency pause for the working capital loan
0143:     Then Admin failed to resume delinquency for working capital loan by loan id with resume start date "15 January 2027" because it matches the pause start date
0144: 
0145:   @TestRailId:C76712
0146:   Scenario: Verify second resume cannot be created for the same pause once already resumed - UC6
0147:     Given Admin sets the business date to "01 January 2027"
0148:     And Admin creates a client with random data
0149:     And Admin creates a working capital loan product with delinquency tracking enabled
0150:     And Admin creates a working capital loan account for the client with the following values
0151:       | loan_field_name                         | loan_field_value        |
0152:       | principal                               | 100000                  |
0153:       | numberOfRepayments                      | 12                      |
0154:       | repaymentEvery                          | 1                       |
0155:       | repaymentFrequencyType                  | MONTHS                  |
0156:       | interestRatePerPeriod                   | 2.5                     |
0157:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0158:       | interestType                            | FLAT                    |
0159:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0160:       | expectedDisbursementDate                | 01 January 2027         |
0161:       | submittedOnDate                         | 01 January 2027         |
0162:       | disbursementDate                        | 01 January 2027         |
0163:       | delinquencyPauseStartDate                | 15 January 2027         |
0164:       | delinquencyPauseEndDate                  | 15 February 2027        |
0165:     When Admin creates a delinquency pause for the working capital loan
0166:     When Admin resumes delinquency for the working capital loan by loan id with resume start date "01 February 2027"
0167:     Then Admin failed to resume delinquency for working capital loan by loan id because the pause has already been resumed
0168: 
0169:   @TestRailId:C76713
0170:   Scenario: Verify delinquency recalculation happens immediately after resume and updates delinquency range schedule - UC7
0171:     Given Admin sets the business date to "01 January 2027"
0172:     And Admin creates a client with random data
0173:     And Admin creates a working capital loan product with delinquency tracking enabled
0174:     And Admin creates a working capital loan account for the client with the following values
0175:       | loan_field_name                         | loan_field_value        |
0176:       | principal                               | 100000                  |
0177:       | numberOfRepayments                      | 12                      |
0178:       | repaymentEvery                          | 1                       |
0179:       | repaymentFrequencyType                  | MONTHS                  |
0180:       | interestRatePerPeriod                   | 2.5                     |
0181:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0182:       | interestType                            | FLAT                    |
0183:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0184:       | expectedDisbursementDate                | 01 January 2027         |
0185:       | submittedOnDate                         | 01 January 2027         |
0186:       | disbursementDate                        | 01 January 2027         |
0187:       | delinquencyPauseStartDate                | 15 January 2027         |
0188:       | delinquencyPauseEndDate                  | 15 February 2027        |
0189:     When Admin creates a delinquency pause for the working capital loan
0190:     When Admin resumes delinquency for the working capital loan by loan id with resume start date "20 January 2027"
0191:     Then Check delinquency range schedule contains the following values
0192:       | delinquency_schedule_field_name | delinquency_schedule_field_value |
0193:       | pauseStartDate                  | 15 January 2027                  |
0194:       | pauseEndDate                    | 20 January 2027                  |
0195:       | scheduleStatus                  | RESUMED                          |
0196:     Then Check delinquency range schedule reflects updated period boundaries and delinquent day calculations
0197:     Then Check delinquency action history contains the following values
0198:       | delinquency_action_field_name | delinquency_action_field_value |
0199:       | action                        | RESUME                         |
0200:       | startDate                     | 20 January 2027                |
0201: 
0202:   @TestRailId:C76714
0203:   Scenario: Verify resume shortens delinquency range schedule end date when resume date is earlier than planned pause end date - UC8
0204:     Given Admin sets the business date to "01 January 2027"
0205:     And Admin creates a client with random data
0206:     And Admin creates a working capital loan product with delinquency tracking enabled
0207:     And Admin creates a working capital loan account for the client with the following values
0208:       | loan_field_name                         | loan_field_value        |
0209:       | principal                               | 100000                  |
0210:       | numberOfRepayments                      | 12                      |
0211:       | repaymentEvery                          | 1                       |
0212:       | repaymentFrequencyType                  | MONTHS                  |
0213:       | interestRatePerPeriod                   | 2.5                     |
0214:       | amortizationType                        | EQUAL_INSTALLMENTS      |
0215:       | interestType                            | FLAT                    |
0216:       | transactionProcessingStrategyCode       | mifos-standard-strategy |
0217:       | expectedDisbursementDate                | 01 January 2027         |
0218:       | submittedOnDate                         | 01 January 2027         |
0219:       | disbursementDate                        | 01 January 2027         |
0220:       | delinquencyPauseStartDate                | 15 January 2027         |
0221:       | delinquencyPauseEndDate                  | 15 February 2027        |
0222:     When Admin creates a delinquency pause for the working capital loan
0223:     When Admin resumes delinquency for the working capital loan by loan id with resume start date "25 January 2027"
0224:     Then Check delinquency range schedule contains the following values
0225:       | delinquency_schedule_field_name | delinquency_schedule_field_value |
0226:       | pauseStartDate                  | 15 January 2027                  |
0227:       | pauseEndDate                    | 25 January 2027                  |
0228:       | scheduleStatus                  | RESUMED                          |
0229:     Then Check delinquency range schedule is shortened accordingly based on the resume date
```

## Archived reference Gherkin

```text
0001: @WorkingCapital
0002: @WorkingCapitalDelinquencyResumeFeature
0003: Feature: Working Capital Delinquency Resume
0004: 
0005:   @TestRailId:C85172
0006:   Scenario: Verify working capital loan delinquency resume - UC1: resume shortens active pause and delinquency range schedule
0007:     When Admin sets the business date to "01 January 2026"
0008:     And Admin creates a client with random data
0009:     And Admin creates a working capital loan with the following data:
0010:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0011:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0012:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0013:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0014:     When Admin runs inline COB job for Working Capital Loan by loanId
0015:     And Admin initiate a Working Capital loan delinquency pause with startDate "01 January 2026" and endDate "16 January 2026"
0016:     Then Working Capital loan delinquency action has the following data:
0017:       | action | startDate  | endDate    |
0018:       | PAUSE  | 2026-01-01 | 2026-01-16 |
0019:     And Working Capital loan delinquency range schedule has the following data:
0020:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0021:       | 1            | 2026-01-01 | 2026-02-15 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0022:     When Admin sets the business date to "10 January 2026"
0023:     And Admin runs inline COB job for Working Capital Loan by loanId
0024:     And Admin initiate a Working Capital loan delinquency resume with startDate "10 January 2026"
0025:     Then Working Capital loan delinquency action has the following data:
0026:       | action | startDate  | endDate    |
0027:       | PAUSE  | 2026-01-01 | 2026-01-16 |
0028:       | RESUME | 2026-01-10 |            |
0029:     And Working Capital loan delinquency range schedule has the following data:
0030:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0031:       | 1            | 2026-01-01 | 2026-02-09 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0032:     Then Admin closes the Working Capital loan with a full repayment on "10 January 2026"
0033: 
0034:   @TestRailId:C85173
0035:   Scenario: Verify working capital loan delinquency resume - UC2: resume on the day before planned pause end shortens schedule by one day
0036:     When Admin sets the business date to "01 January 2026"
0037:     And Admin creates a client with random data
0038:     And Admin creates a working capital loan with the following data:
0039:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0040:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000       | 18                | 0        |
0041:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0042:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0043:     When Admin runs inline COB job for Working Capital Loan by loanId
0044:     And Admin initiate a Working Capital loan delinquency pause with startDate "01 January 2026" and endDate "16 January 2026"
0045:     And Working Capital loan delinquency range schedule has the following data:
0046:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0047:       | 1            | 2026-01-01 | 2026-02-15 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0048:     When Admin sets the business date to "15 January 2026"
0049:     And Admin runs inline COB job for Working Capital Loan by loanId
0050:     And Admin initiate a Working Capital loan delinquency resume with startDate "15 January 2026"
0051:     Then Working Capital loan delinquency action has the following data:
0052:       | action | startDate  | endDate    |
0053:       | PAUSE  | 2026-01-01 | 2026-01-16 |
0054:       | RESUME | 2026-01-15 |            |
0055:     And Working Capital loan delinquency range schedule has the following data:
0056:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0057:       | 1            | 2026-01-01 | 2026-02-14 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0058:     Then Admin closes the Working Capital loan with a full repayment on "15 January 2026"
0059: 
0060:   @TestRailId:C85174
0061:   Scenario: Verify working capital loan delinquency resume - UC3: resume by external ID
0062:     When Admin sets the business date to "01 January 2026"
0063:     And Admin creates a client with random data
0064:     And Admin creates a working capital loan with the following data:
0065:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0066:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000       | 18                | 0        |
0067:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0068:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0069:     When Admin runs inline COB job for Working Capital Loan by loanId
0070:     And Admin initiate a Working Capital loan delinquency pause by external ID with startDate "01 January 2026" and endDate "16 January 2026"
0071:     When Admin sets the business date to "10 January 2026"
0072:     And Admin runs inline COB job for Working Capital Loan by loanId
0073:     And Admin initiate a Working Capital loan delinquency resume by external ID with startDate "10 January 2026"
0074:     Then Working Capital loan delinquency action by external ID has the following data:
0075:       | action | startDate  | endDate    |
0076:       | PAUSE  | 2026-01-01 | 2026-01-16 |
0077:       | RESUME | 2026-01-10 |            |
0078:     Then Admin closes the Working Capital loan with a full repayment on "10 January 2026"
0079: 
0080:   @TestRailId:C85175
0081:   Scenario: Verify working capital loan delinquency resume - UC4: resume without an active pause results an error (Negative)
0082:     When Admin sets the business date to "01 January 2026"
0083:     And Admin creates a client with random data
0084:     And Admin creates a working capital loan with the following data:
0085:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0086:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0087:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0088:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0089:     When Admin runs inline COB job for Working Capital Loan by loanId
0090:     When Admin sets the business date to "10 January 2026"
0091:     And Admin runs inline COB job for Working Capital Loan by loanId
0092:     Then Initiating a Working Capital loan delinquency resume with startDate "10 January 2026" results an error with the following data:
0093:       | httpCode | errorMessage                                                         |
0094:       | 400      | Resume Delinquency Action can only be created during an active pause |
0095:     Then Admin closes the Working Capital loan with a full repayment on "10 January 2026"
0096: 
0097:   @TestRailId:C85176
0098:   Scenario: Verify working capital loan delinquency resume - UC5: backdated resume results an error (Negative)
0099:     When Admin sets the business date to "01 January 2026"
0100:     And Admin creates a client with random data
0101:     And Admin creates a working capital loan with the following data:
0102:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0103:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0104:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0105:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0106:     When Admin runs inline COB job for Working Capital Loan by loanId
0107:     And Admin initiate a Working Capital loan delinquency pause with startDate "01 January 2026" and endDate "16 January 2026"
0108:     When Admin sets the business date to "10 January 2026"
0109:     And Admin runs inline COB job for Working Capital Loan by loanId
0110:     Then Initiating a Working Capital loan delinquency resume with startDate "09 January 2026" results an error with the following data:
0111:       | httpCode | errorMessage                                                                  |
0112:       | 400      | Start date of the Resume Delinquency action must be the current business date |
0113:     Then Admin closes the Working Capital loan with a full repayment on "10 January 2026"
0114: 
0115:   @TestRailId:C85177
0116:   Scenario: Verify working capital loan delinquency resume - UC6: resume on pause start date results an error (Negative)
0117:     When Admin sets the business date to "01 January 2026"
0118:     And Admin creates a client with random data
0119:     And Admin creates a working capital loan with the following data:
0120:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0121:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0122:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0123:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0124:     When Admin runs inline COB job for Working Capital Loan by loanId
0125:     And Admin initiate a Working Capital loan delinquency pause with startDate "01 January 2026" and endDate "16 January 2026"
0126:     Then Initiating a Working Capital loan delinquency resume with startDate "01 January 2026" results an error with the following data:
0127:       | httpCode | errorMessage                                          |
0128:       | 400      | Resume date must be after the active pause start date |
0129:     Then Admin closes the Working Capital loan with a full repayment on "01 January 2026"
0130: 
0131:   @TestRailId:C85178
0132:   Scenario: Verify working capital loan delinquency resume - UC7: multiple resumes on the same pause results an error (Negative)
0133:     When Admin sets the business date to "01 January 2026"
0134:     And Admin creates a client with random data
0135:     And Admin creates a working capital loan with the following data:
0136:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0137:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0138:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0139:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0140:     When Admin runs inline COB job for Working Capital Loan by loanId
0141:     And Admin initiate a Working Capital loan delinquency pause with startDate "01 January 2026" and endDate "16 January 2026"
0142:     When Admin sets the business date to "10 January 2026"
0143:     And Admin runs inline COB job for Working Capital Loan by loanId
0144:     And Admin initiate a Working Capital loan delinquency resume with startDate "10 January 2026"
0145:     Then Initiating a Working Capital loan delinquency resume with startDate "10 January 2026" results an error with the following data:
0146:       | httpCode | errorMessage                                                         |
0147:       | 400      | Resume Delinquency Action can only be created during an active pause |
0148:     Then Admin closes the Working Capital loan with a full repayment on "10 January 2026"
0149: 
0150:   @TestRailId:C85179
0151:   Scenario: Verify working capital loan delinquency resume - UC8: resume recalculates delinquency immediately
0152:     When Admin sets the business date to "01 January 2026"
0153:     And Admin creates a client with random data
0154:     And Admin creates a working capital loan with the following data:
0155:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0156:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0157:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0158:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0159:     When Admin runs inline COB job for Working Capital Loan by loanId
0160:     When Admin sets the business date to "15 February 2026"
0161:     And Admin runs inline COB job for Working Capital Loan by loanId
0162:     Then Working Capital loan delinquency range schedule has the following data:
0163:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0164:       | 1            | 2026-01-01 | 2026-01-30 | 270.0          | 0.0        | 270.0             | false                 | 270.0            | 16             |
0165:       | 2            | 2026-01-31 | 2026-03-01 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0166:     And Admin initiate a Working Capital loan delinquency pause with startDate "15 February 2026" and endDate "15 March 2026"
0167:     Then Working Capital loan delinquency range schedule has the following data:
0168:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0169:       | 1            | 2026-01-01 | 2026-01-30 | 270.0          | 0.0        | 270.0             | false                 | 270.0            | 16             |
0170:       | 2            | 2026-01-31 | 2026-03-30 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0171:     When Admin sets the business date to "20 February 2026"
0172:     And Admin initiate a Working Capital loan delinquency resume with startDate "20 February 2026"
0173:     Then Working Capital loan delinquency range schedule has the following data:
0174:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0175:       | 1            | 2026-01-01 | 2026-01-30 | 270.0          | 0.0        | 270.0             | false                 | 270.0            | 21             |
0176:       | 2            | 2026-01-31 | 2026-03-07 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0177:     Then Admin closes the Working Capital loan with a full repayment on "20 February 2026"
0178: 
0179:   @TestRailId:C85219
0180:   Scenario: Verify resume keeps the PAUSE action dates unchanged and only shortens the delinquency period extension
0181:     When Admin sets the business date to "01 January 2026"
0182:     And Admin creates a client with random data
0183:     And Admin creates a working capital loan with the following data:
0184:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0185:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0186:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0187:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0188:     When Admin runs inline COB job for Working Capital Loan by loanId
0189:     When Admin sets the business date to "28 January 2026"
0190:     And Admin initiate a Working Capital loan delinquency pause with startDate "28 January 2026" and endDate "20 February 2026"
0191:     When Admin sets the business date to "29 January 2026"
0192:     And Admin initiate a Working Capital loan delinquency resume with startDate "29 January 2026"
0193:     Then Working Capital loan delinquency action has the following data:
0194:       | action | startDate  | endDate    |
0195:       | PAUSE  | 2026-01-28 | 2026-02-20 |
0196:       | RESUME | 2026-01-29 |            |
0197:     And Working Capital loan delinquency range schedule has the following data:
0198:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0199:       | 1            | 2026-01-01 | 2026-02-01 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0200:     Then Admin closes the Working Capital loan with a full repayment on "29 January 2026"
0201: 
0202:   @TestRailId:C85220
0203:   Scenario: Verify that COB-generated period after resume must honour the shortened (resumed) pause
0204:     When Admin sets the business date to "01 January 2026"
0205:     And Admin creates a client with random data
0206:     And Admin creates a working capital loan with the following data:
0207:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0208:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0209:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0210:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0211:     When Admin runs inline COB job for Working Capital Loan by loanId
0212:     When Admin sets the business date to "28 January 2026"
0213:     And Admin initiate a Working Capital loan delinquency pause with startDate "28 January 2026" and endDate "20 February 2026"
0214:     When Admin sets the business date to "29 January 2026"
0215:     And Admin initiate a Working Capital loan delinquency resume with startDate "29 January 2026"
0216:     When Admin sets the business date to "02 February 2026"
0217:     And Admin runs inline COB job for Working Capital Loan by loanId
0218:     Then Working Capital loan delinquency range schedule has the following data:
0219:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount |
0220:       | 1            | 2026-01-01 | 2026-02-01 | 270.0          | 0.0        | 270.0             |
0221:       | 2            | 2026-02-02 | 2026-03-03 | 270.0          | 0.0        | 270.0             |
0222:     Then Admin closes the Working Capital loan with a full repayment on "02 February 2026"
0223: 
0224:   @TestRailId:C85314
0225:   Scenario: Verify new pause is allowed after resumed pause when outside effective pause window
0226:     When Admin sets the business date to "01 January 2026"
0227:     And Admin creates a client with random data
0228:     And Admin creates a working capital loan with the following data:
0229:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0230:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0231:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0232:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0233:     When Admin runs inline COB job for Working Capital Loan by loanId
0234:     When Admin sets the business date to "28 January 2026"
0235:     And Admin initiate a Working Capital loan delinquency pause with startDate "28 January 2026" and endDate "20 February 2026"
0236:     And Working Capital loan delinquency range schedule has the following data:
0237:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0238:       | 1            | 2026-01-01 | 2026-02-23 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0239:     When Admin sets the business date to "29 January 2026"
0240:     And Admin initiate a Working Capital loan delinquency resume with startDate "29 January 2026"
0241:     And Working Capital loan delinquency range schedule has the following data:
0242:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0243:       | 1            | 2026-01-01 | 2026-02-01 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0244:     When Admin sets the business date to "05 February 2026"
0245:     And Admin runs inline COB job for Working Capital Loan by loanId
0246:     And Admin initiate a Working Capital loan delinquency pause with startDate "05 February 2026" and endDate "10 February 2026"
0247:     Then Working Capital loan delinquency action has the following data:
0248:       | action | startDate  | endDate    |
0249:       | PAUSE  | 2026-01-28 | 2026-02-20 |
0250:       | RESUME | 2026-01-29 |            |
0251:       | PAUSE  | 2026-02-05 | 2026-02-10 |
0252:     And Working Capital loan delinquency range schedule has the following data:
0253:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0254:       | 1            | 2026-01-01 | 2026-02-01 | 270.0          | 0.0        | 270.0             | false                 | 270.0            | 4              |
0255:       | 2            | 2026-02-02 | 2026-03-09 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0256:     Then Admin closes the Working Capital loan with a full repayment on "05 February 2026"
0257: 
0258:   @TestRailId:C85330
0259:   Scenario: Verify working capital loan delinquency pause - G1: a one-day pause (startDate == endDate) is accepted and extends the schedule by one day
0260:   # both pause dates are INCLUSIVE, so startDate == endDate is a valid 1-day pause
0261:     When Admin sets the business date to "01 January 2026"
0262:     And Admin creates a client with random data
0263:     And Admin creates a working capital loan with the following data:
0264:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0265:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0266:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0267:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0268:     When Admin runs inline COB job for Working Capital Loan by loanId
0269:     And Admin initiate a Working Capital loan delinquency pause with startDate "10 January 2026" and endDate "10 January 2026"
0270:     Then Working Capital loan delinquency action has the following data:
0271:       | action | startDate  | endDate    |
0272:       | PAUSE  | 2026-01-10 | 2026-01-10 |
0273:     And Working Capital loan delinquency range schedule has the following data:
0274:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0275:       | 1            | 2026-01-01 | 2026-01-31 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0276:     Then Admin closes the Working Capital loan with a full repayment on "01 January 2026"
0277: 
0278:   @TestRailId:C85328
0279:   Scenario: Verify working capital loan delinquency pause - G2: an active pause suppresses delinquency on the first overdue day
0280:   # Period 1 is due 30-Jan. A pause 30-Jan -> 10-Feb shifts its toDate to 11-Feb (+12 inclusive).
0281:   # On 31-Jan, the first day AFTER the original due date, the loan would normally be delinquentDays = 1;
0282:   # while paused it must stay non-delinquent (null) - i.e. delinquency does not grow across the paused period's start/due boundary.
0283:     When Admin sets the business date to "01 January 2026"
0284:     And Admin creates a client with random data
0285:     And Admin creates a working capital loan with the following data:
0286:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0287:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0288:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0289:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0290:     When Admin runs inline COB job for Working Capital Loan by loanId
0291:     When Admin sets the business date to "30 January 2026"
0292:     And Admin initiate a Working Capital loan delinquency pause with startDate "30 January 2026" and endDate "10 February 2026"
0293:     Then Working Capital loan delinquency range schedule has the following data:
0294:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0295:       | 1            | 2026-01-01 | 2026-02-11 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0296:     When Admin sets the business date to "31 January 2026"
0297:     And Admin runs inline COB job for Working Capital Loan by loanId
0298:     Then Working Capital loan delinquency range schedule has the following data:
0299:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0300:       | 1            | 2026-01-01 | 2026-02-11 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0301:     Then Admin closes the Working Capital loan with a full repayment on "31 January 2026"
0302: 
0303:   @TestRailId:C85329
0304:   Scenario: Verify working capital loan delinquency resume - G3: the resume date counts as paused and delinquency resumes only the next day
0305:   # Pause 10-Jan -> 20-Feb (+42 inclusive) is resumed on 15-Jan. The resume date is STILL a paused day, so the
0306:   # effective pause is 10..15-Jan = 6 days (inclusive of the 15th), shifting period 1 toDate to 05-Feb (due 30-Jan + 6).
0307:   # On 05-Feb (the shifted toDate) the period is still open (null); delinquency only resumes on 06-Feb (= 1).
0308:     When Admin sets the business date to "01 January 2026"
0309:     And Admin creates a client with random data
0310:     And Admin creates a working capital loan with the following data:
0311:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0312:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0313:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0314:     When Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0315:     When Admin runs inline COB job for Working Capital Loan by loanId
0316:     When Admin sets the business date to "10 January 2026"
0317:     And Admin initiate a Working Capital loan delinquency pause with startDate "10 January 2026" and endDate "20 February 2026"
0318:     When Admin sets the business date to "15 January 2026"
0319:     And Admin initiate a Working Capital loan delinquency resume with startDate "15 January 2026"
0320:     Then Working Capital loan delinquency range schedule has the following data:
0321:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0322:       | 1            | 2026-01-01 | 2026-02-05 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0323:     When Admin sets the business date to "05 February 2026"
0324:     And Admin runs inline COB job for Working Capital Loan by loanId
0325:     Then Working Capital loan delinquency range schedule has the following data:
0326:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0327:       | 1            | 2026-01-01 | 2026-02-05 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0328:     When Admin sets the business date to "06 February 2026"
0329:     And Admin runs inline COB job for Working Capital Loan by loanId
0330:     Then Working Capital loan delinquency range schedule has the following data:
0331:       | periodNumber | fromDate   | toDate     | expectedAmount | paidAmount | outstandingAmount | minPaymentCriteriaMet | delinquentAmount | delinquentDays |
0332:       | 1            | 2026-01-01 | 2026-02-05 | 270.0          | 0.0        | 270.0             | false                 | 270.0            | 1              |
0333:       | 2            | 2026-02-06 | 2026-03-07 | 270.0          | 0.0        | 270.0             | null                  | null             | null           |
0334:     Then Admin closes the Working Capital loan with a full repayment on "06 February 2026"
```
