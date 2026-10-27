---
name: claims-decoded
description: Explain insurance claims, Explanation of Benefits (EOB) statements, medical bills and denial letters in plain language, and tell the person what to do next. Use whenever someone shares or describes an EOB, a medical bill, a claim denial, a prior-authorization refusal, or asks what a claim code (CARC, RARC, CPT, HCPCS, ICD-10, revenue code), "patient responsibility", "allowed amount", deductible, coinsurance or out-of-pocket maximum means. Also use when they want to check whether they were billed correctly or want help appealing a denied claim.
---

# Claims Decoded

Turn confusing insurance paperwork into a clear answer to three questions:

1. **What happened?** What was billed, what the plan paid, and why.
2. **What do I owe?** And whether that number looks right.
3. **What should I do next?** Pay, wait, call, dispute or appeal.

Write for a policyholder, not a billing specialist. Every code or term you
mention gets a plain-language explanation the first time it appears.

## Workflow

### 1. Gather the document

Work from what the person shares: a photo, PDF, pasted text or a description.
If key fields are missing, ask for them, but do not block on them; decode what
is there and list what is missing.

Fields to look for on each claim line:

| Field | Where it usually appears |
| --- | --- |
| Date of service | EOB line, bill line |
| Provider / facility | Header, line description |
| Service codes (CPT, HCPCS, revenue code) | "Service", "Procedure", "Code" column |
| Diagnosis codes (ICD-10-CM) | Bill, claim form; rarely on EOBs |
| Billed / charged amount | "Amount billed", "Charges" |
| Allowed amount | "Allowed", "Plan discount" is billed minus allowed |
| Plan paid | "Plan paid", "Paid to provider" |
| Deductible, copay, coinsurance | Separate columns or a "Your share" breakdown |
| Not covered amount | "Not covered", "Non-covered" |
| Adjustment / remark codes (CARC, RARC) | Footnotes, "Remark", "Reason code" |
| Network status | "In-network" / "Out-of-network" |
| Claim number, member ID | Header |

Remind the person to redact their member ID, SSN and date of birth if they
are sharing an image, and never repeat those identifiers back in full.

### 2. Decode each line

For every claim line, produce:

- **Service:** the code and what it means ("99214: an established-patient
  office visit of moderate complexity").
- **The money:** billed → allowed → plan paid → your share, and the split of
  your share into deductible, copay, coinsurance and not covered.
- **Why:** translate every adjustment or remark code (see
  [Common codes](#common-codes)). If a code is not in that list, explain it
  from your own knowledge and say that the person should confirm the exact
  wording with their insurer, since plans sometimes use proprietary codes.

Check the arithmetic: `allowed = plan paid + deductible + copay + coinsurance`
(plus any not-covered amount, which sits outside the allowed amount), and
`billed − allowed` should be a contractual write-off for in-network care. Call
out any line where the numbers do not reconcile.

### 3. Flag problems

Look for these and name each one you find, with the line it applies to:

- **Balance billing:** an in-network provider billing more than the "your
  share" on the EOB, or an out-of-network bill for emergency care or for
  services at an in-network facility (likely protected under the No Surprises
  Act for US plans from 2022 onward).
- **Bill before EOB:** a provider bill that arrived before the insurer
  processed the claim. Advise waiting for the EOB before paying.
- **Duplicate charges:** same code, same date, same provider more than once
  without a modifier (for example 59, 76, 77, XS) that explains it.
- **Coding mismatches:** a diagnosis that does not support the procedure, an
  office-visit level that seems high for what the person describes, or
  "unbundled" services that are normally billed as one code.
- **Preventive care charged as diagnostic:** a screening (annual physical,
  screening colonoscopy, recommended vaccines) that produced cost sharing.
  ACA-compliant plans usually cover these at no cost in network.
- **Coordination of benefits:** denials saying another plan is primary
  (CARC 22) when the person has only one plan, or has told the insurer.
- **Fixable denials:** missing information, missing prior authorization,
  timely filing or eligibility errors. Many of these are fixed by a phone
  call from the provider's billing office, not an appeal.

Only flag what the documents support. Say "possible" or "worth asking about"
when you are inferring, and never accuse a provider of fraud.

### 4. Recommend next steps

Pick the action that matches what you found and make it concrete:

| Situation | Next step |
| --- | --- |
| Everything reconciles | Pay the "your share" amount; ask about a payment plan or financial assistance if it is large |
| Bill arrived before EOB | Wait for the EOB, then compare |
| Bill exceeds EOB "your share" | Call the provider's billing office with the EOB in hand |
| Denied for missing info, auth or coding | Ask the provider to correct and resubmit the claim |
| Denied as not covered / not medically necessary | Internal appeal (see below) |
| Possible surprise bill | Cite the No Surprises Act; contact the plan and the No Surprises Help Desk (1-800-985-3059) |
| Internal appeal already lost | External review through the state or federal process |

Include a short call script when a phone call is the next step: who to call,
the claim number to reference, what to ask for, and what to write down (date,
representative's name, reference number).

### 5. Appeals

When the person wants to appeal, draft the letter for them:

- Addressed to the appeals address on the denial letter or EOB.
- Member name, member ID placeholder, claim number, date of service, provider.
- What was denied and the stated reason, quoted with its code.
- Why the denial is wrong, tied to the plan's own terms, medical necessity
  and any supporting documents (letter of medical necessity from the doctor,
  records, prior authorization number).
- A specific request: reprocess and pay the claim.
- A list of enclosures.

Leave `[placeholders]` for anything you do not know rather than inventing it.
Remind them of deadlines: for most US plans an internal appeal must be filed
within 180 days of the denial notice, and urgent-care appeals can be
expedited. Tell them to check the denial letter for their plan's exact
deadline.

## Output format

Use this structure, and keep it scannable:

```markdown
## Summary
One to three sentences: what this is, what you owe, whether anything looks wrong.

## Line by line
| Date | Service | Billed | Allowed | Plan paid | You owe | Why |
| ...  | ...     | ...    | ...     | ...       | ...     | ... |

## Codes explained
- **CO-45:** ...

## Things to check
- ...

## What to do next
1. ...
```

Omit sections that would be empty. For a simple question ("what does PR-1
mean?") answer in a few sentences instead of the full structure.

## Common codes

Claim Adjustment Reason Codes (CARC) are prefixed with a group code:

- **CO** (contractual obligation): the provider must write this off; you do
  not owe it.
- **PR** (patient responsibility): you may owe this.
- **OA** (other adjustment) and **PI** (payer-initiated reduction): usually
  not billed to you; ask if it shows up on a bill.

| CARC | Meaning |
| --- | --- |
| 1 | Deductible amount |
| 2 | Coinsurance amount |
| 3 | Copay amount |
| 4 | Procedure code inconsistent with the modifier, or modifier missing |
| 11 | Diagnosis inconsistent with the procedure |
| 16 | Claim lacks information needed to process it (see the RARC) |
| 18 | Duplicate claim or service |
| 22 | May be covered by another payer (coordination of benefits) |
| 23 | Impact of prior payer's adjudication |
| 27 | Expenses incurred after coverage ended |
| 29 | Time limit for filing has expired |
| 31 | Patient cannot be identified as the insured |
| 45 | Charge exceeds the fee schedule or contracted amount (network discount) |
| 50 | Not deemed a medical necessity by the payer |
| 96 | Non-covered charge |
| 97 | Payment included in another service already paid (bundling) |
| 109 | Not covered by this payer; submit to the correct payer |
| 119 | Benefit maximum for this period has been reached |
| 151 | Payer deems the information does not support this many services |
| 197 | Precertification / authorization absent |
| 204 | Service not covered under the patient's current benefit plan |
| 242 | Services not provided by network or primary care providers |

Common Remittance Advice Remark Codes (RARC) that add detail:

| RARC | Meaning |
| --- | --- |
| M15 | Separately billed services were bundled |
| M51 | Missing, incomplete or invalid procedure code |
| M76 | Missing, incomplete or invalid diagnosis code |
| MA04 | Secondary payment cannot be considered without the primary payer's info |
| MA130 | Claim has missing or invalid information; resubmit as a new claim |
| N130 | Consult plan benefit documents for coverage restrictions |
| N290 | Missing, incomplete or invalid rendering provider identifier |
| N362 | Number of days or units exceeds the acceptable maximum |
| N386 | Decision based on a National Coverage Determination |

## Glossary

Use these definitions when you explain terms:

- **Billed amount:** the provider's list price. Rarely what anyone pays.
- **Allowed amount:** the most the plan recognizes for the service; for
  in-network care this is the negotiated rate.
- **Deductible:** what you pay each plan year before the plan starts sharing
  costs (preventive care is often exempt).
- **Copay:** a fixed fee per service, such as $30 per visit.
- **Coinsurance:** your percentage of the allowed amount after the deductible,
  such as 20%.
- **Out-of-pocket maximum:** the cap on your deductible, copays and
  coinsurance for the year; after it, the plan pays 100% of covered in-network
  care.
- **EOB:** a statement from the insurer explaining how a claim was processed.
  It is not a bill.
- **Prior authorization:** plan approval required before certain services.
- **Balance billing:** a provider billing you for the difference between their
  charge and the allowed amount.

## Boundaries

- This is general information, not legal, medical or financial advice. Say so
  once, briefly, when you recommend a dispute or appeal, not in every reply.
- Plan documents (the Summary of Benefits and Coverage, the Evidence of
  Coverage) override general rules. When the answer depends on the specific
  plan, say which document to check.
- Rules above are US-centric. If the claim is from another country, or is a
  property, auto or life claim, apply the same workflow (what happened, what
  is owed, what to do next) but do not cite US codes or laws.
- Do not guess dollar amounts, deadlines or policy terms that are not in the
  documents. Mark them as unknown and tell the person where to find them.
