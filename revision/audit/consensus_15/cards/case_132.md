# Case 132 — discussion evidence

Preparation only. No final labels are proposed here. Numbering below is specific to this evidence card. Original notes are quoted unchanged from the source label files and may say pending review; An recorded the confirmation of these labels on 2026-10-15.

## business_logic: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026; confidence of the comparison: high. AC1 is partially covered: there is no rejection/withdrawal/deletion, and modify does not yet check the new value; D_MISSING_AC is not counted because many operations of this AC are present. AC2 does not yet confirm equivalent behavior/returned data for all operations between internal/external ID. Chained success only counts transactions without checking types. In the case enclosingTransaction=false, add fee fail400 but transactionCount2 even though only one disbursement succeeded; the expected count needs to be fixed. This is an AI label for comparison; the API has not been run. Coverage: 1/5. Not yet reviewed by An/Hoàng.

### Hoang original note
AC1(wrong): UC1 and UC2 cover CREATE, MODIFY, APPROVE, DISBURSE, ADD_DISCOUNT_FEE, FETCH_DETAILS, FETCH_TRANSACTIONS. REJECT and WITHDRAW/DELETE have no scenario yet.|AC2(correct): UC2 and UC7 demonstrate equivalent behavior for external ID in CREATE, MODIFY, APPROVE, DISBURSE, FETCH.|AC3(correct): UC3 chains all 5 steps; the final result is Active with transactionCount 2 (DISBURSEMENT + DISCOUNT_FEE), consistent with UC7 (1 transaction, no fee yet) and UC8 (2 transactions).|AC4(correct): UC4 sets enclosingTransaction = true, the ADD_DISCOUNT_FEE step fails, returns 400 and rollback is checked (the loan no longer exists).|AC5(wrong): UC5 checks transactionCount = 2 while the ADD_DISCOUNT_FEE step using invalidLoanId has returned 400, so the loan has only 1 transaction.|Unsure: do not know whether the AC5 defect should be classed as D_NUM or as D_OUTCOME|CONVENTION: an AC that only states a state counts as checked if that state is present in Given/Background

## temporal_causal: initial An=Y; Hoang=Y

### An original note
AI draft 12/10/2026. AC1 is partially covered: there is no rejection/withdrawal/deletion, and modify does not yet check the new value; D_MISSING_AC is not counted because many operations of this AC are present. AC2 does not yet confirm equivalent behavior/returned data for all operations between internal/external ID. Chained success only counts transactions without checking types. In the case enclosingTransaction=false, add fee fail400 but transactionCount2 even though only one disbursement succeeded; the expected count needs to be fixed. This is an AI label for comparison; the API has not been run. PRE counts the business context, not only the position of the Given keyword. Not yet reviewed by An/Hoàng.

### Hoang original note
The enclosingTransaction configuration is the precondition of AC4 and AC5.|The scenarios all have a When that is a Batch API call, and create the loan themselves within the chain, so no Background is needed.|The results of REJECT and WITHDRAW/DELETE are not checked by any Then.|In UC5, Then checks the consequence of ADD_DISCOUNT_FEE (the 2nd transaction), but the When of that step has already failed, so it produces no consequence.|The chains are all in the correct business order (CREATE, MODIFY, APPROVE, DISBURSE, ADD_DISCOUNT_FEE, FETCH), with no fee before disburse. | ACS WITH PRECONDITION: AC4, AC5

## User story

```text
0001: As a system integrator managing loan operations,
0002: I want to perform Working Capital Loan operations (create, modify, approve, disburse, reject, withdraw, add discount fee, and fetch details/transactions) through a single Batch API, referencing loans by either internal ID or external ID, and optionally chaining multiple steps within one enclosing transaction,
0003: So that I can efficiently automate and orchestrate complete Working Capital Loan lifecycles in a single request while ensuring data consistency and proper rollback when any step fails.
0004: 
0005: Acceptance Criteria:
0006: - The Batch API must support individual operations on Working Capital Loans, including creation, modification, approval, disbursement, rejection, withdrawal/deletion, discount fee addition, and fetching loan details or transactions, all returning a 200OK response and correctly updated loan data upon success.
0007: - The Batch API must support referencing a Working Capital Loan by either its internal loan ID or its external ID for all supported operations, with equivalent behavior and correct data returned in both cases.
0008: - The Batch API must support executing multiple chained Working Capital Loan steps (e.g., create, approve, disburse, add discount fee, fetch details) within a single call, correctly reflecting the final loan status and all resulting transactions.
0009: - When enclosingTransaction is set to "true" and any step in the chain fails, all previously executed steps within that batch call must be rolled back, and the failing step must return an error with code 400.
0010: - When enclosingTransaction is set to "false", each step in the chain must be evaluated independently, allowing prior successful steps to persist even if a later step fails, with each step's individual result status (200 or error code) verifiable.
```

## Generated Gherkin C0

```text
0001: @WorkingCapital
0002: @WorkingCapitalLoanBatchApiFeature
0003: Feature: Working Capital Loan Batch API
0004: 
0005:   @TestRailId:C76707
0006:   Scenario: Verify Working Capital Loan Batch API single operation lifecycle by internal ID - UC1
0007:     Given Admin prepares a Working Capital Loan Batch request payload with the following values
0008:       | batchOperationType | referenceType | referenceValue | enclosingTransaction |
0009:       | CREATE             | INTERNAL_ID   | null           | true                 |
0010:     When Admin calls Working Capital Loan Batch API to create a Working Capital Loan
0011:     Then Admin receives a 200OK response for Working Capital Loan creation
0012:     And Check created Working Capital Loan has the following values
0013:       | loanProductType              | WORKING_CAPITAL |
0014:       | loanStatus                   | Submitted       |
0015:       | referenceType                | INTERNAL_ID     |
0016:       | referenceValue               | internalLoanId  |
0017:       | batchOperationResultStatus   | 200             |
0018: 
0019:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0020:       | batchOperationType | referenceType | referenceValue  | enclosingTransaction |
0021:       | MODIFY             | INTERNAL_ID   | internalLoanId  | true                 |
0022:     And Admin calls Working Capital Loan Batch API to modify a Working Capital Loan
0023:     Then Admin receives a 200OK response for Working Capital Loan modification
0024:     And Check modified Working Capital Loan has the following values
0025:       | loanStatus                 | Submitted       |
0026:       | referenceType              | INTERNAL_ID     |
0027:       | referenceValue             | internalLoanId  |
0028:       | batchOperationResultStatus | 200             |
0029: 
0030:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0031:       | batchOperationType | referenceType | referenceValue  | enclosingTransaction |
0032:       | APPROVE            | INTERNAL_ID   | internalLoanId  | true                 |
0033:     And Admin calls Working Capital Loan Batch API to approve a Working Capital Loan
0034:     Then Admin receives a 200OK response for Working Capital Loan approval
0035:     And Check approved Working Capital Loan has the following values
0036:       | loanStatus                 | Approved        |
0037:       | referenceType              | INTERNAL_ID     |
0038:       | referenceValue             | internalLoanId  |
0039:       | batchOperationResultStatus | 200             |
0040: 
0041:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0042:       | batchOperationType | referenceType | referenceValue  | enclosingTransaction |
0043:       | DISBURSE           | INTERNAL_ID   | internalLoanId  | true                 |
0044:     And Admin calls Working Capital Loan Batch API to disburse a Working Capital Loan
0045:     Then Admin receives a 200OK response for Working Capital Loan disbursement
0046:     And Check disbursed Working Capital Loan has the following values
0047:       | loanStatus                 | Active          |
0048:       | referenceType              | INTERNAL_ID     |
0049:       | referenceValue             | internalLoanId  |
0050:       | batchOperationResultStatus | 200             |
0051: 
0052:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0053:       | batchOperationType | referenceType | referenceValue  | enclosingTransaction |
0054:       | ADD_DISCOUNT_FEE  | INTERNAL_ID   | internalLoanId  | true                 |
0055:     And Admin calls Working Capital Loan Batch API to add a discount fee to a Working Capital Loan
0056:     Then Admin receives a 200OK response for Working Capital Loan discount fee addition
0057:     And Check Working Capital Loan discount fee transaction has the following values
0058:       | transactionType            | DISCOUNT_FEE    |
0059:       | referenceType              | INTERNAL_ID     |
0060:       | referenceValue             | internalLoanId  |
0061:       | batchOperationResultStatus | 200             |
0062: 
0063:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0064:       | batchOperationType | referenceType | referenceValue  | enclosingTransaction |
0065:       | FETCH_DETAILS      | INTERNAL_ID   | internalLoanId  | true                 |
0066:     And Admin calls Working Capital Loan Batch API to fetch Working Capital Loan details
0067:     Then Admin receives a 200OK response for Working Capital Loan details retrieval
0068:     And Check fetched Working Capital Loan details has the following values
0069:       | loanStatus                 | Active          |
0070:       | referenceType              | INTERNAL_ID     |
0071:       | referenceValue             | internalLoanId  |
0072:       | batchOperationResultStatus | 200             |
0073: 
0074:   @TestRailId:C76708
0075:   Scenario: Verify Working Capital Loan Batch API single operation lifecycle by external ID - UC2
0076:     Given Admin prepares a Working Capital Loan Batch request payload with the following values
0077:       | batchOperationType | referenceType | referenceValue   | enclosingTransaction |
0078:       | CREATE             | EXTERNAL_ID   | externalLoanId   | true                 |
0079:     When Admin calls Working Capital Loan Batch API to create a Working Capital Loan
0080:     Then Admin receives a 200OK response for Working Capital Loan creation
0081:     And Check created Working Capital Loan has the following values
0082:       | loanProductType              | WORKING_CAPITAL |
0083:       | loanStatus                   | Submitted       |
0084:       | referenceType                | EXTERNAL_ID     |
0085:       | referenceValue               | externalLoanId   |
0086:       | batchOperationResultStatus   | 200             |
0087: 
0088:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0089:       | batchOperationType | referenceType | referenceValue   | enclosingTransaction |
0090:       | APPROVE            | EXTERNAL_ID   | externalLoanId   | true                 |
0091:     And Admin calls Working Capital Loan Batch API to approve a Working Capital Loan
0092:     Then Admin receives a 200OK response for Working Capital Loan approval
0093:     And Check approved Working Capital Loan has the following values
0094:       | loanStatus                 | Approved        |
0095:       | referenceType              | EXTERNAL_ID     |
0096:       | referenceValue             | externalLoanId   |
0097:       | batchOperationResultStatus | 200             |
0098: 
0099:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0100:       | batchOperationType | referenceType | referenceValue   | enclosingTransaction |
0101:       | DISBURSE           | EXTERNAL_ID   | externalLoanId   | true                 |
0102:     And Admin calls Working Capital Loan Batch API to disburse a Working Capital Loan
0103:     Then Admin receives a 200OK response for Working Capital Loan disbursement
0104:     And Check disbursed Working Capital Loan has the following values
0105:       | loanStatus                 | Active          |
0106:       | referenceType              | EXTERNAL_ID     |
0107:       | referenceValue             | externalLoanId   |
0108:       | batchOperationResultStatus | 200             |
0109: 
0110:     When Admin prepares a Working Capital Loan Batch request payload with the following values
0111:       | batchOperationType | referenceType | referenceValue   | enclosingTransaction |
0112:       | FETCH_TRANSACTIONS | EXTERNAL_ID   | externalLoanId   | true                 |
0113:     And Admin calls Working Capital Loan Batch API to fetch Working Capital Loan transactions
0114:     Then Admin receives a 200OK response for Working Capital Loan transactions retrieval
0115:     And Check fetched Working Capital Loan transactions has the following values
0116:       | transactionType            | DISBURSEMENT    |
0117:       | referenceType              | EXTERNAL_ID     |
0118:       | referenceValue             | externalLoanId   |
0119:       | batchOperationResultStatus | 200             |
0120: 
0121:   @TestRailId:C76709
0122:   Scenario: Verify Working Capital Loan Batch API chained operations within a single call - UC3
0123:     Given Admin prepares a Working Capital Loan Batch request payload with the following values
0124:       | batchOperationType | referenceType | referenceValue | enclosingTransaction |
0125:       | CREATE             | INTERNAL_ID   | null           | true                 |
0126:       | APPROVE            | INTERNAL_ID   | loanId         | true                 |
0127:       | DISBURSE           | INTERNAL_ID   | loanId         | true                 |
0128:       | ADD_DISCOUNT_FEE   | INTERNAL_ID   | loanId         | true                 |
0129:       | FETCH_DETAILS      | INTERNAL_ID   | loanId         | true                 |
0130:     When Admin calls Working Capital Loan Batch API with chained operations
0131:     Then Admin receives a 200OK response for all Working Capital Loan chained operations
0132:     And Check chained Working Capital Loan final state has the following values
0133:       | loanStatus                 | Active          |
0134:       | transactionCount            | 2               |
0135:       | referenceType              | INTERNAL_ID     |
0136:       | batchOperationResultStatus | 200             |
0137: 
0138:   @TestRailId:C76710
0139:   Scenario: Verify Working Capital Loan Batch API chained operations with enclosing transaction true shall rollback on failure - UC4
0140:     Given Admin prepares a Working Capital Loan Batch request payload with the following values
0141:       | batchOperationType | referenceType | referenceValue | enclosingTransaction |
0142:       | CREATE             | INTERNAL_ID   | null           | true                 |
0143:       | APPROVE            | INTERNAL_ID   | loanId         | true                 |
0144:       | DISBURSE           | INTERNAL_ID   | loanId         | true                 |
0145:       | ADD_DISCOUNT_FEE   | INTERNAL_ID   | invalidLoanId   | true                 |
0146:       | FETCH_DETAILS      | INTERNAL_ID   | loanId         | true                 |
0147:     When Admin calls Working Capital Loan Batch API with chained operations
0148:     Then Admin receives a 400 error for the failing batch step
0149:     And Check previously executed Working Capital Loan batch steps are rolled back
0150:     And Check Working Capital Loan does not exist after rollback
0151: 
0152:   @TestRailId:C76711
0153:   Scenario: Verify Working Capital Loan Batch API chained operations with enclosing transaction false shall persist prior success on failure - UC5
0154:     Given Admin prepares a Working Capital Loan Batch request payload with the following values
0155:       | batchOperationType | referenceType | referenceValue | enclosingTransaction |
0156:       | CREATE             | INTERNAL_ID   | null           | false                |
0157:       | APPROVE            | INTERNAL_ID   | loanId         | false                |
0158:       | DISBURSE           | INTERNAL_ID   | loanId         | false                |
0159:       | ADD_DISCOUNT_FEE   | INTERNAL_ID   | invalidLoanId   | false                |
0160:       | FETCH_DETAILS      | INTERNAL_ID   | loanId         | false                |
0161:     When Admin calls Working Capital Loan Batch API with chained operations
0162:     Then Admin receives a 200OK response for successful batch steps and an error code 400 for the failing step
0163:     And Check previously executed Working Capital Loan batch steps are persisted
0164:     And Check Working Capital Loan final state has the following values
0165:       | loanStatus                 | Active          |
0166:       | transactionCount            | 2               |
0167:       | batchOperationResultStatus | 200             |
0168: 
0169:   @TestRailId:C76712
0170:   Scenario Outline: Verify Working Capital Loan Batch API operations by invalid reference identifier shall outcome with error - UC6
0171:     Then Admin failed to execute Working Capital Loan Batch operation "<wcl_batch_operation>" with reference type "<wcl_reference_type>" and reference value "<wcl_reference_value>" results with an error <wcl_error_message>
0172: 
0173:     Examples:
0174:       | wcl_batch_operation | wcl_reference_type | wcl_reference_value | wcl_error_message                                      |
0175:       | APPROVE             | INTERNAL_ID        | 0                   | The parameter `loanId` is invalid.                    |
0176:       | APPROVE             | INTERNAL_ID        | 999999              | The Working Capital Loan was not found.               |
0177:       | APPROVE             | EXTERNAL_ID        | ""                  | The parameter `externalId` is mandatory.              |
0178:       | DISBURSE            | EXTERNAL_ID        | invalidExternalId    | The Working Capital Loan was not found.               |
0179:       | FETCH_DETAILS       | INTERNAL_ID        | 0                   | The parameter `loanId` is invalid.                    |
0180:       | FETCH_TRANSACTIONS   | EXTERNAL_ID        | 0                   | The parameter `externalId` is invalid.                |
0181: 
0182:   @TestRailId:C76713
0183:   Scenario: Verify Working Capital Loan Batch API modify, approve, disburse and fetch details by external ID shall return equivalent data - UC7
0184:     Given Admin creates a Working Capital Loan using Batch API with external ID
0185:     When Admin modifies the Working Capital Loan using Batch API with external ID
0186:     And Admin approves the Working Capital Loan using Batch API with external ID
0187:     And Admin disburses the Working Capital Loan using Batch API with external ID
0188:     And Admin fetches the Working Capital Loan details using Batch API with external ID
0189:     Then Check Working Capital Loan data returned by external ID has the following values
0190:       | loanStatus                 | Active          |
0191:       | referenceType              | EXTERNAL_ID     |
0192:       | batchOperationResultStatus | 200             |
0193:       | transactionCount            | 1               |
0194: 
0195:   @TestRailId:C76714
0196:   Scenario: Verify Working Capital Loan Batch API fetch transactions after discount fee addition shall return correct transaction set - UC8
0197:     Given Admin creates and disburses a Working Capital Loan using Batch API
0198:     When Admin adds a discount fee to the Working Capital Loan using Batch API
0199:     And Admin fetches the Working Capital Loan transactions using Batch API
0200:     Then Check Working Capital Loan transactions has the following values
0201:       | transactionType            | DISBURSEMENT,DISCOUNT_FEE |
0202:       | transactionCount            | 2                         |
0203:       | batchOperationResultStatus | 200                       |
```

## Archived reference Gherkin

```text
0001: @WorkingCapitalBatchApi
0002: Feature: Working Capital Batch API
0003: 
0004:   # ============================================
0005:   # SECTION 1: Individual Operation Tests
0006:   # ============================================
0007: 
0008:   @TestRailId:C83089
0009:   Scenario: Verify Batch API - UC1: Create Working Capital Loan via Batch API
0010:     When Admin sets the business date to "01 January 2026"
0011:     And Admin creates a client with random data
0012:     When Batch API creates a working capital loan with the following data:
0013:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0014:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0015:     Then Admin checks that all steps result 200OK
0016:     And Working capital loan creation was successful
0017:     And Working capital loan account has the correct data:
0018:       | product.name | submittedOnDate | expectedDisbursementDate | status                         | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0019:       | WCLP         | 2026-01-01      | 2026-01-01               | Submitted and pending approval | 9000.0            | 100000.0           | 18.0              | null     |
0020: 
0021:   @TestRailId:C83090
0022:   Scenario: Verify Batch API - UC2: Modify Working Capital Loan via Batch API by ID
0023:     When Admin sets the business date to "01 January 2026"
0024:     And Admin creates a client with random data
0025:     And Admin creates a working capital loan with the following data:
0026:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0027:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0028:     When Batch API modifies the working capital loan principal to "8000" by loan ID
0029:     Then Admin checks that all steps result 200OK
0030:     And Working capital loan account has the correct data:
0031:       | product.name | submittedOnDate | expectedDisbursementDate | status                         | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0032:       | WCLP         | 2026-01-01      | 2026-01-01               | Submitted and pending approval | 8000.0            | 100000.0           | 18.0              | null     |
0033: 
0034:   @TestRailId:C83091
0035:   Scenario: Verify Batch API - UC3: Approve Working Capital Loan via Batch API
0036:     When Admin sets the business date to "01 January 2026"
0037:     And Admin creates a client with random data
0038:     And Admin creates a working capital loan with the following data:
0039:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0040:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0041:     When Batch API approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0042:     Then Admin checks that all steps result 200OK
0043:     And Working capital loan approval was successful
0044:     And Working capital loan account has the correct data:
0045:       | product.name | submittedOnDate | expectedDisbursementDate | status   | approvedPrincipal | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0046:       | WCLP         | 2026-01-01      | 2026-01-01               | Approved | 9000.0            | 9000.0            | 100000.0           | 18.0              | null     |
0047: 
0048:   @TestRailId:C83092
0049:   Scenario: Verify Batch API - UC4: Disburse Working Capital Loan via Batch API
0050:     When Admin sets the business date to "01 January 2026"
0051:     And Admin creates a client with random data
0052:     And Admin creates a working capital loan with the following data:
0053:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0054:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0055:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0056:     When Batch API disburses the working capital loan on "01 January 2026" with "9000" EUR transaction amount
0057:     Then Admin checks that all steps result 200OK
0058:     And Working capital loan account has the correct data:
0059:       | product.name | submittedOnDate | expectedDisbursementDate | status | principal | approvedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0060:       | WCLP         | 2026-01-01      | 2026-01-01               | Active | 9000.0    | 9000.0            | 100000.0           | 18.0              | null     |
0061: 
0062:   @TestRailId:C83093
0063:   Scenario: Verify Batch API - UC5: Reject Working Capital Loan via Batch API
0064:     When Admin sets the business date to "01 January 2026"
0065:     And Admin creates a client with random data
0066:     And Admin creates a working capital loan with the following data:
0067:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0068:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0069:     When Batch API rejects the working capital loan on "01 January 2026"
0070:     Then Admin checks that all steps result 200OK
0071:     And Working capital loan rejection was successful
0072:     And Working capital loan account has the correct data:
0073:       | product.name | submittedOnDate | expectedDisbursementDate | status   | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0074:       | WCLP         | 2026-01-01      | 2026-01-01               | Rejected | 9000.0            | 100000.0           | 18.0              | null     |
0075: 
0076:   @TestRailId:C83094
0077:   Scenario: Verify Batch API - UC6: Withdraw/Delete Working Capital Loan via Batch API by ID
0078:     When Admin sets the business date to "01 January 2026"
0079:     And Admin creates a client with random data
0080:     And Admin creates a working capital loan with the following data:
0081:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0082:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0083:     Then Working capital loan account has the correct data:
0084:       | product.name | submittedOnDate | expectedDisbursementDate | status                         | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0085:       | WCLP         | 2026-01-01      | 2026-01-01               | Submitted and pending approval | 9000.0            | 100000.0           | 18.0              | null     |
0086:     When Batch API deletes the working capital loan by loan ID
0087:     Then Admin checks that all steps result 200OK
0088:     And Working capital loan no longer exists
0089: 
0090:   @TestRailId:C83095
0091:   Scenario: Verify Batch API - UC7: Add Discount Fee via Batch API
0092:     When Admin sets the business date to "01 January 2026"
0093:     And Admin creates a client with random data
0094:     And Admin creates a working capital loan with the following data:
0095:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0096:       | WCLP_DISCOUNT | 01 January 2026 | 01 January 2026          | 100             | 100                | 1                 | 0        |
0097:     And Admin successfully approves the working capital loan on "01 January 2026" with "100" amount and expected disbursement date on "01 January 2026"
0098:     And Admin successfully disburse the Working Capital loan on "01 January 2026" with "100" EUR transaction amount
0099:     When Batch API adds discount fee with "12" amount on the working capital loan
0100:     Then Admin checks that all steps result 200OK
0101:     And Working Capital Loan has transactions:
0102:       | transactionDate | type         | transactionAmount | principalPortion | feeChargesPortion | penaltyChargesPortion | reversed |
0103:       | 01 January 2026 | Disbursement | 100.0             | 100.0            | 0.0               | 0.0                   | false    |
0104:       | 01 January 2026 | Discount Fee | 12.0              | 12.0             | 0.0               | 0.0                   | false    |
0105: 
0106:   @TestRailId:C83096
0107:   Scenario: Verify Batch API - UC8: Fetch Working Capital Loan Details via Batch API by ID
0108:     When Admin sets the business date to "01 January 2026"
0109:     And Admin creates a client with random data
0110:     And Admin creates a working capital loan with the following data:
0111:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0112:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0113:     When Batch API fetches working capital loan details by loan ID
0114:     Then Admin checks that all steps result 200OK
0115:     And Batch API response contains working capital loan with the correct data:
0116:       | product.name | submittedOnDate | expectedDisbursementDate | status                         | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0117:       | WCLP         | 2026-01-01      | 2026-01-01               | Submitted and pending approval | 9000.0            | 100000.0           | 18.0              | null     |
0118: 
0119:   @TestRailId:C83097
0120:   Scenario: Verify Batch API - UC9: Fetch Working Capital Loan Transactions via Batch API
0121:     When Admin sets the business date to "01 January 2026"
0122:     And Admin creates a client with random data
0123:     And Admin creates a working capital loan with the following data:
0124:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0125:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0126:     And Admin successfully approves the working capital loan on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0127:     And Admin successfully disburse the Working Capital loan on "01 January 2026" with "9000" EUR transaction amount
0128:     When Batch API fetches working capital loan disbursement transaction by loan ID
0129:     Then Admin checks that all steps result 200OK
0130:     And Batch API response contains working capital transaction with the correct data:
0131:       | transactionDate | type         | transactionAmount | principalPortion | feeChargesPortion | penaltyChargesPortion | reversed |
0132:       | 01 January 2026 | Disbursement | 9000.0            | 9000.0           | 0.0               | 0.0                   | false    |
0133: 
0134:   # ============================================
0135:   # SECTION 2: Combined Workflow Tests
0136:   # ============================================
0137: 
0138:   @TestRailId:C83098
0139:   Scenario: Verify Batch API - UC10: Full Working Capital Loan lifecycle via Batch API in single call
0140:     When Admin sets the business date to "01 January 2026"
0141:     And Admin creates a client with random data
0142:     When Batch API call with working capital steps: "createWCLoan, approveWCLoan, disburseWCLoan" runs with enclosingTransaction: "true" and loan data:
0143:       | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0144:       | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0145:     Then Admin checks that all steps result 200OK
0146:     And Working Capital loan status will be "ACTIVE"
0147:     And Working capital loan account has the correct data:
0148:       | product.name | submittedOnDate | expectedDisbursementDate | status | principal | approvedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0149:       | WCLP         | 2026-01-01      | 2026-01-01               | Active | 9000.0    | 9000.0            | 100000.0           | 18.0              | null     |
0150: 
0151:   @TestRailId:C83099
0152:   Scenario: Verify Batch API - UC11: Create, Approve, Disburse and Add Discount Fee in single Batch API call
0153:     When Admin sets the business date to "01 January 2026"
0154:     And Admin creates a client with random data
0155:     When Batch API call with working capital steps: "createWCLoan, approveWCLoan, disburseWCLoan, addDiscountFee" runs with enclosingTransaction: "true" and loan data:
0156:       | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0157:       | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0158:     Then Admin checks that all steps result 200OK
0159:     And Working Capital loan status will be "ACTIVE"
0160:     And Working Capital Loan has transactions:
0161:       | transactionDate | type         | transactionAmount | principalPortion | feeChargesPortion | penaltyChargesPortion | reversed |
0162:       | 01 January 2026 | Disbursement | 9000.0            | 9000.0           | 0.0               | 0.0                   | false    |
0163:       | 01 January 2026 | Discount Fee | 100.0             | 100.0            | 0.0               | 0.0                   | false    |
0164: 
0165:   @TestRailId:C83100
0166:   Scenario: Verify Batch API - UC12: Working Capital Batch API enclosing transaction FALSE with chained dependencies
0167:     When Admin sets the business date to "01 January 2026"
0168:     And Admin creates a client with random data
0169:     When Batch API call with working capital steps: "createWCLoan, approveWCLoan, disburseWCLoan" runs with enclosingTransaction: "false" and loan data:
0170:       | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0171:       | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0172:     Then Verify that WCL step 1 results 200
0173:     And Verify that WCL step 2 results 200
0174:     And Verify that WCL step 3 results 200
0175: 
0176:   @TestRailId:C83101
0177:   Scenario: Verify Batch API - UC13: Working Capital Batch API enclosing transaction FALSE with chained dependencies and failed last step
0178:     When Admin sets the business date to "01 January 2026"
0179:     And Admin creates a client with random data
0180:     When Batch API call with working capital steps: "createWCLoan, approveWCLoan, disburseWCLoan" runs with enclosingTransaction: "false", with failed disburse step and loan data:
0181:       | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0182:       | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0183:     Then Verify that WCL step 1 results 200
0184:     And Verify that WCL step 2 results 200
0185:     And Verify that WCL step 3 throws an error with error code 400
0186: 
0187:   @TestRailId:C83102
0188:   Scenario: Verify Batch API - UC14: Working Capital Batch API with failed step in enclosing transaction TRUE
0189:     When Admin sets the business date to "01 January 2026"
0190:     And Admin creates a client with random data
0191:     When Batch API call with working capital steps: "createWCLoan, approveWCLoan, disburseWCLoan" runs with enclosingTransaction: "true", with failed disburse step and loan data:
0192:       | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0193:       | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0194:     Then Verify that WCL step 3 throws an error with error code 400
0195:     And Nr. 1 Working capital loan creation was rolled back
0196: 
0197:   # ============================================
0198:   # SECTION 3: External ID Tests
0199:   # ============================================
0200: 
0201:   @TestRailId:C83103
0202:   Scenario: Verify Batch API - UC15: Working Capital Loan lifecycle via Batch API by External ID
0203:     When Admin sets the business date to "01 January 2026"
0204:     And Admin creates a client with random data
0205:     And Batch API creates a working capital loan with external ID and the following data:
0206:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0207:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0208:     Then Working capital loan account has the correct data:
0209:       | product.name | submittedOnDate | expectedDisbursementDate | status                         | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0210:       | WCLP         | 2026-01-01      | 2026-01-01               | Submitted and pending approval | 9000.0            | 100000.0           | 18.0              | null     |
0211:     When Batch API approves the working capital loan by external ID on "01 January 2026" with "9000" amount and expected disbursement date on "01 January 2026"
0212:     Then Working capital loan account has the correct data:
0213:       | product.name | submittedOnDate | expectedDisbursementDate | status   | approvedPrincipal | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0214:       | WCLP         | 2026-01-01      | 2026-01-01               | Approved | 9000.0            | 9000.0            | 100000.0           | 18.0              | null     |
0215:     And Batch API disburses the working capital loan by external ID on "01 January 2026" with "9000" EUR transaction amount
0216:     And Working capital loan account has the correct data:
0217:       | product.name | submittedOnDate | expectedDisbursementDate | status | principal | approvedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0218:       | WCLP         | 2026-01-01      | 2026-01-01               | Active | 9000.0    | 9000.0            | 100000.0           | 18.0              | null     |
0219:   When Batch API fetches working capital loan details by external ID
0220:     Then Admin checks that all steps result 200OK
0221:     And Batch API response contains working capital loan with the correct data:
0222:       | product.name | submittedOnDate | expectedDisbursementDate | status | principal | approvedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0223:       | WCLP         | 2026-01-01      | 2026-01-01               | Active | 9000.0    | 9000.0            | 100000.0           | 18.0              | null     |
0224:     When Batch API fetches working capital loan disbursement transaction by external ID
0225:     Then Admin checks that all steps result 200OK
0226:     And Batch API response contains working capital transaction with the correct data:
0227:       | transactionDate | type         | transactionAmount | principalPortion | feeChargesPortion | penaltyChargesPortion | reversed |
0228:       | 01 January 2026 | Disbursement | 9000.0            | 9000.0           | 0.0               | 0.0                   | false    |
0229: 
0230:   @TestRailId:C83104
0231:   Scenario: Verify Batch API - UC16: Modify Working Capital Loan via Batch API by External ID
0232:     When Admin sets the business date to "01 January 2026"
0233:     And Admin creates a client with random data
0234:     And Batch API creates a working capital loan with external ID and the following data:
0235:       | LoanProduct | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0236:       | WCLP        | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0237:     When Batch API modifies the working capital loan principal to "8000" by external ID
0238:     Then Admin checks that all steps result 200OK
0239:     And Working capital loan account has the correct data:
0240:       | product.name | submittedOnDate | expectedDisbursementDate | status                         | proposedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0241:       | WCLP         | 2026-01-01      | 2026-01-01               | Submitted and pending approval | 8000.0            | 100000.0           | 18.0              | null     |
0242: 
0243:   @TestRailId:C83105
0244:   Scenario: Verify Batch API - UC17: Working Capital Batch API with external IDs
0245:     When Admin sets the business date to "01 January 2026"
0246:     And Admin creates a client with random data
0247:     When Batch API call with working capital steps by external IDs: "createWCLoan, approveWCLoan, disburseWCLoan, getWCLoanDetails" runs with enclosingTransaction: "true" and loan data:
0248:       | submittedOnDate | expectedDisbursementDate | principalAmount | totalPaymentVolume | periodPaymentRate | discount |
0249:       | 01 January 2026 | 01 January 2026          | 9000            | 100000             | 18                | 0        |
0250:     Then Admin checks that all steps result 200OK
0251:     And Batch API response contains working capital loan details with the correct data:
0252:       | product.name | submittedOnDate | expectedDisbursementDate | status | principal | approvedPrincipal | totalPaymentVolume | periodPaymentRate | discount |
0253:       | WCLP         | 2026-01-01      | 2026-01-01               | Active | 9000.0    | 9000.0            | 100000.0           | 18.0              | null     |
0254:     And Working Capital loan status will be "ACTIVE"
0255:     And Working Capital Loan has transactions:
0256:       | transactionDate | type         | transactionAmount | principalPortion | feeChargesPortion | penaltyChargesPortion | reversed |
0257:       | 01 January 2026 | Disbursement | 9000.0            | 9000.0           | 0.0               | 0.0                   | false    |
```
