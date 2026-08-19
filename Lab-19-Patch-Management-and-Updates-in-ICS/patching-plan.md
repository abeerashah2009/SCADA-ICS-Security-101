# Task 3: ICS Patching Plan

## Objective

Develop a safe patching strategy that reduces security risk while
minimizing disruption to ICS operations.

## 1. Asset Prioritization

| Priority | Asset Type | Patching Approach |
|----------|------------|-------------------|
| Critical | Safety/control systems | Test extensively before deployment |
| High | Engineering/HMI systems | Patch during approved maintenance window |
| Medium | Monitoring/support systems | Schedule regular updates |
| Low | Non-critical systems | Patch during normal maintenance |

## 2. Pre-Patching Activities

Before applying any update:

1. Identify the affected system.
2. Record the current software and OS versions.
3. Review the vendor security advisory.
4. Check whether the patch addresses a security vulnerability.
5. Check compatibility with ICS applications.
6. Back up important configurations and data.
7. Test the update in a non-production environment.
8. Prepare a rollback/recovery procedure.
9. Obtain operational approval.

## 3. Maintenance Window

Patches should be scheduled during planned maintenance windows.

Consider:

- Production requirements
- System criticality
- Expected downtime
- Network traffic
- Availability of operators
- Backup and recovery requirements

Avoid applying patches during critical production operations.

## 4. Patch Deployment

The patch should first be deployed to a test system.

If testing is successful:

1. Schedule production deployment.
2. Notify affected personnel.
3. Apply the patch.
4. Verify system functionality.
5. Monitor logs and services.
6. Confirm normal ICS operation.

Automation tools such as Ansible can be used for controlled deployment
after testing and approval.

Example:

    ansible-playbook update_ics.yml -i inventory

## 5. Rollback Plan

If the patch causes problems:

1. Stop the deployment.
2. Restore the previous configuration or software version.
3. Verify system operation.
4. Document the problem.
5. Investigate compatibility issues.
6. Reschedule deployment after remediation.

## 6. Suggested Schedule

### Emergency Security Updates

Review immediately and deploy according to the ICS emergency change
procedure after appropriate testing.

### High-Priority Updates

Deploy during the next approved maintenance window after testing.

### Normal Updates

Include them in the regular maintenance cycle.

### Low-Priority Updates

Schedule them when operational impact is minimal.

## 7. Post-Patching Verification

After patching:

- Check system availability.
- Verify important services.
- Check network connectivity.
- Review system logs.
- Verify application functionality.
- Confirm that expected ports/services are available.
- Record the final software version.

## 8. Lab Environment

This lab uses an Ubuntu 24.04.3 LTS test environment.

The inventory identified:

- 476 upgradable packages
- SSH on TCP/22
- NICE DCV on TCP/8443
- Containerd installed
- Amazon CloudWatch Agent installed

Because this is a test environment, patching can be evaluated without
impacting a production ICS process.

## Conclusion

A safe ICS patching process requires more than simply installing
available updates. Patches should be reviewed, tested, approved,
scheduled, deployed, verified, and documented. A rollback plan should
always be available in case the update affects operational stability.
