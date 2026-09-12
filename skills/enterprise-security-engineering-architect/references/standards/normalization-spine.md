# Normalization Spine

Use common concepts before vendor-specific fields.

## OCSF
Use as a vendor-neutral security event vocabulary when useful for cross-product reasoning.

Official:
- https://schema.ocsf.io/
- https://github.com/ocsf/ocsf-schema

## Sigma
Use as portable detection semantics and rule logic, not as proof that every backend translation is semantically identical.

Official:
- https://sigmahq.io/
- https://github.com/SigmaHQ/sigma

## OpenTelemetry
Use for general traces, metrics, logs, resources, attributes, and telemetry architecture.

Official:
- https://opentelemetry.io/docs/

## STIX / TAXII
Use for structured cyber-threat intelligence and exchange.

Official:
- https://oasis-open.github.io/cti-documentation/
- https://www.oasis-open.org/standard/stix-version-2-1/
- https://www.oasis-open.org/standard/taxii-version-2-1/

## Splunk CIM
Use for Splunk data-model normalization.
Verify current CIM documentation for exact fields/models.

Official:
- https://help.splunk.com/en/splunk-enterprise-security-8/common-information-model/

## Microsoft ASIM
Use for Microsoft Sentinel source-independent normalized analytics.

Official:
- https://learn.microsoft.com/azure/sentinel/normalization
- https://github.com/Azure/Azure-Sentinel/tree/master/ASIM
