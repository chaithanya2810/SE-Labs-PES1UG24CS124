# Requirements Specification

## Digital Parking Reservation Gateway

**Primary Domain:** Campus and Academic Operations  
**Target Actors:** Student, Security Staff, Parking Administrator

---

## Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall allow authenticated students to search available parking bays by campus zone and reserve a specific bay for a time window up to 24 hours in advance. | High | **Pass:** A valid reservation is created with a unique parking token and assigned bay.  
**Fail:** The system permits double-booking or a reservation beyond 24 hours. | Digital reservation is the core function of the gateway and prevents conflicts in parking allocation. |
| FR-002 | Functional | The system shall validate the vehicle registration details associated with a student's reservation before confirming the reservation. | High | **Pass:** Reservation proceeds only when the vehicle registration is valid. **Fail:** An unregistered or invalid vehicle is accepted for reservation. | Prevents unauthorized vehicles from using campus parking facilities. |
| FR-003 | Functional | The system shall provide Security Staff with the ability to verify a vehicle's parking authorization and reservation status at a campus parking zone. | High | **Pass:** Security Staff can retrieve the vehicle's valid reservation and parking authorization. **Fail:** An unauthorized vehicle is incorrectly shown as authorized. | Enables security personnel to enforce controlled campus parking access. |
| FR-004 | Functional | The system shall detect parking-rule violations such as overstay or unauthorized zone access and generate a fine for the violation. | High | **Pass:** A detected violation generates a fine associated with the relevant vehicle or reservation. **Fail:** A confirmed violation produces no fine or an incorrect fine. | Automates enforcement of campus parking rules and reduces manual monitoring. |
| FR-005 | Functional | The system shall allow the Parking Administrator to manage parking zones, bays, availability, and parking-rule configurations. | Medium | **Pass:** An authorized administrator can add, update, or deactivate parking resources and rules. **Fail:** Unauthorized users can modify administrative parking data. | Allows parking capacity and rules to be maintained as campus requirements change. |

---

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Non-Functional – Performance & Security | The parking availability dashboard shall reflect bay status changes within 5 seconds of sensor or check-in updates and shall enforce role-based access for administrative override functions. | High | **Pass:** Bay status updates are reflected within 5 seconds and administrative functions are accessible only to authorized roles. **Fail:** Updates exceed 5 seconds or unauthorized users can perform administrative overrides. | Real-time availability is important for reliable reservation decisions, while role-based access prevents unauthorized changes. |
| NFR-002 | Non-Functional – Availability & Reliability | The system shall maintain reliable access to current parking availability and reservation information during normal campus operating hours. | High | **Pass:** Users can retrieve current availability and reservation information during the defined operating period without loss of confirmed reservations. **Fail:** Availability becomes inaccessible or confirmed reservations are lost during normal operation. | Students and Security Staff depend on accurate and accessible reservation information for parking operations. |
