# Change Request — HMI Screen Update

## Change Identification

**Change ID:** CR-2026-027-HMI  
**Title:** HMI Screen Update for Improved Operator Clarity  
**Requestor:** Jane Doe  
**Role:** SCADA Engineer  
**Date:** 2026-08-21  
**Priority:** Medium  
**Change Type:** Normal Change  
**Affected Component:** HMI


---

## Change Description

Update selected HMI screens to improve operator visibility, readability, and navigation.

The proposed change includes:

- Improving screen layout.
- Making important process information easier to identify.
- Standardizing labels.
- Improving navigation between HMI screens.
- Maintaining existing control functionality.

No PLC logic changes are included in this request.


---

## Reason for Change

The change is intended to:

- Improve operator efficiency.
- Reduce potential operator confusion.
- Improve information visibility.
- Standardize the HMI user interface.


---

## Impact Analysis

### Expected Impact

The expected operational impact is low because the proposed change is limited to the HMI presentation layer.

### Potential Risks

- Incorrect screen configuration.
- Display or navigation errors.
- Operator confusion if changes are not properly tested.
- Unexpected HMI application behavior.

### Risk Level

**Medium**


---

## Testing Plan

Testing will be performed in the simulated laboratory environment.

Testing will verify:

1. HMI configuration can be loaded.
2. Updated screens display correctly.
3. Navigation works correctly.
4. Labels are correct.
5. Existing simulated control functionality remains unchanged.
6. No unexpected configuration errors occur.


---

## Backup Plan

Before implementation, the existing HMI configuration will be backed up.

Example:

```bash
cp hmi/config.ini backup/hmi/config.ini
```

### Rollback Plan

If the change fails validation:

Stop implementation.
Restore the previous HMI configuration.
Verify configuration integrity.
Record the rollback.
Reopen the change request for investigation.

---

## Approval Status
### Pending Approval

- Required reviewers:
  - HMI Design Team Lead
  - Operations Manager

## Change Decision

**Status:** Pending Approval

No production implementation is authorized by this laboratory exercise.
 
