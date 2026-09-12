# Evidence Method

## Evidence classes

- **Observed**: directly supported by supplied logs/configuration/query output/source.
- **Reported**: stated by a person/vendor/support case but not independently confirmed.
- **Documented**: supported by current authoritative documentation.
- **Inferred**: reasoned from evidence but not directly observed.
- **Hypothesis**: testable explanation.
- **Unknown**: not established.

Never collapse these categories.

## Minimum useful evidence

Collect only evidence that can change the next decision.

Examples:
- one event proving source generation;
- one transport/collector check proving delivery;
- one SIEM search proving ingestion;
- one field/CIM check proving normalization;
- one detection execution proving matching;
- one finding/SOAR check proving downstream action.

## Evidence packet

For complex work, maintain:

| Fact | Evidence | Class | Confidence | Implication |
|---|---|---|---|---|

Do not include secrets or unnecessary personal data.

## Contradictions

When sources conflict:
1. state the conflict;
2. rank source quality;
3. identify the test that can resolve it;
4. avoid choosing the convenient answer.
