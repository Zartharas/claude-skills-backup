# Troubleshooting Method

## First-failure principle

Trace the path in order and stop at the earliest unsupported boundary.

Example:

1. source generated event;
2. export/API/syslog stream emitted it;
3. collector received it;
4. transport delivered it;
5. SIEM indexed it;
6. parser extracted fields;
7. normalization matched schema;
8. data model/search saw it;
9. detection matched it;
10. finding/notable was created;
11. SOAR received it;
12. response action executed.

A downstream symptom can originate upstream.

## Discriminating tests

Prefer a test whose outcomes route to different hypotheses.

Bad:
- collect all internal logs;
- run 40 unrelated searches.

Good:
- prove whether the raw event exists before investigating CIM;
- prove whether the API returned the record before tuning Splunk;
- prove whether the correlation search matched before debugging SOAR.

## Fix discipline

Fix the smallest evidenced cause.
Do not "improve" neighboring components during incident restoration unless required.

## Validation

Validate the repaired boundary and one downstream consumer.
Avoid declaring success from a configuration save alone.
