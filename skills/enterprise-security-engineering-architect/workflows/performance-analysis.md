# Performance Analysis

Separate:
- query/analytic cost;
- data volume/cardinality;
- scheduling/concurrency;
- platform capacity;
- upstream polling/export behavior;
- network/API latency;
- downstream fan-out.

Measure before optimizing.
Preserve functional semantics unless the user authorizes a behavior change.
