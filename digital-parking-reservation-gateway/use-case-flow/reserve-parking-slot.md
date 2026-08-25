# Use-Case Flow Specification

## UC-02: Reserve Parking Slot

**Primary Actor:** Student

### Goal

The student wants to reserve an available parking bay for a specific time period.

---

## Preconditions

1. The student is authenticated.
2. The student has a valid registered vehicle.
3. Parking zones and bays are available in the system.
4. The requested reservation time is within the allowed booking window.

---

## Postconditions

### Success

1. A parking bay is reserved for the student.
2. A unique parking token is generated.
3. The reservation is associated with the student's registered vehicle.
4. The selected bay is no longer available for conflicting reservations.

### Failure

1. No reservation is created.
2. The selected bay remains available for other valid users.

---

## Main Success Scenario

1. The student selects **Reserve Parking**.
2. The system displays available campus zones and parking bays.
3. The student selects a parking zone, available bay, and desired time window.
4. The system validates the student's vehicle registration.
5. The system verifies that the selected bay is available for the requested time window.
6. The system creates the parking reservation.
7. The system generates a unique parking token and confirms the assigned bay.
8. The system displays the reservation details to the student.

---

## Alternate Flow — Invalid Vehicle Registration

**At Step 4:**

4a. The system determines that the vehicle registration is invalid or not registered to the student.

4b. The system displays an appropriate error message.

4c. The system does not create the reservation.

4d. The student may select a valid registered vehicle and retry the reservation.
