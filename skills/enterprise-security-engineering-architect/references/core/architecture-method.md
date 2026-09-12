# Architecture Method

For L4/L5 work, model the system in layers:

1. actors/users/devices;
2. control plane;
3. data plane;
4. security enforcement;
5. telemetry/collection;
6. analytics/detection;
7. orchestration/response;
8. storage/retention;
9. identity/authorization;
10. management/ownership.

For each important flow capture:
- source;
- destination;
- protocol/mechanism;
- authentication/authorization;
- data type;
- sensitivity;
- buffering/replay behavior;
- expected latency;
- failure behavior;
- owner;
- validation method.

Evaluate alternatives on:
- security;
- reliability;
- performance;
- complexity;
- operational burden;
- cost;
- vendor dependency;
- observability;
- migration risk;
- recovery/rollback.
