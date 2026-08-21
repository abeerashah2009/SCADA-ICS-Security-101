# ICS/SCADA Change Management Procedure

## 1. Purpose

This procedure defines a controlled process for managing changes to ICS/SCADA systems.

The objective is to reduce operational risk, maintain system integrity, and ensure that changes are properly documented, reviewed, tested, approved, implemented, and verified.

## 2. Scope

This procedure applies to simulated ICS/SCADA components including:

- HMI configurations
- PLC programs
- SCADA configurations
- Alarm configurations
- Network configurations
- Engineering workstation configurations

This laboratory uses simulated systems only.

## 3. Change Management Lifecycle

Every change should follow this lifecycle:

1. Change identification
2. Change request creation
3. Impact and risk assessment
4. Approval
5. Testing
6. Implementation
7. Post-implementation verification
8. Documentation and closure

## 4. Change Request

The requestor must document:

- Change title
- Requestor
- Date
- Reason for change
- Description
- Affected component
- Expected impact
- Risk
- Testing plan
- Rollback plan

## 5. Approval

Changes should be reviewed by appropriate personnel.

Example approval levels:

| Change Risk | Example | Approval |
|---|---|---|
| Low | HMI display text | SCADA/HMI Lead |
| Medium | HMI configuration | SCADA Lead + Operations |
| High | PLC logic change | Engineering + Operations + Change Manager |
| Critical | Safety/control architecture | Management + Engineering + Safety |

No change should be implemented before required approval is obtained.

## 6. Testing

Changes should first be tested in a controlled or simulated environment.

Testing should verify:

- Configuration validity
- Expected functionality
- Operator usability
- System stability
- No unexpected side effects
- Rollback procedure

## 7. Implementation

After approval and successful testing:

1. Schedule the change.
2. Notify affected personnel.
3. Back up the existing configuration.
4. Implement the approved change.
5. Verify functionality.
6. Monitor the system.

## 8. Rollback

A rollback plan must be available before implementation.

If the change causes unexpected behavior:

1. Stop the change.
2. Restore the previous configuration.
3. Verify system functionality.
4. Document the incident.
5. Escalate if required.

## 9. Post-Implementation Review

After implementation:

- Verify the expected result.
- Confirm that no unexpected effects occurred.
- Record test results.
- Update documentation.
- Close the change request.

## 10. Change Closure

A change can be closed when:

- Approval is documented.
- Testing is successful.
- Implementation is verified.
- Rollback information is recorded.
- Post-implementation review is complete.

## 11. Security Principles

ICS/SCADA change management should follow:

- Least privilege
- Separation of duties
- Defense in depth
- Backup before change
- Controlled testing
- Audit logging
- Configuration integrity
- Formal approval
- Documented rollback
