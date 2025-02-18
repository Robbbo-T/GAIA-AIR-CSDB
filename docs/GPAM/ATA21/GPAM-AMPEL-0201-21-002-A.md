---
dmc: DMC-GAIAPULSE-AMPEL-0201-21-002-A-020-00_EN-US
ident:
  dmCode: GPAM-AMPEL-0201-21-002-A
  modelIdentCode: AMPEL360
  systemDiffCode: A
  systemCode: 21
  subSystemCode: 02
  subSubSystemCode: 00
  assyCode: 00
  disassyCode: 00
  disassyCodeVariant: A
  infoCode: 020
  infoCodeVariant: A
  itemLocationCode: 00
  language: EN-US
applicability: AMPEL360XWLRGA
status: draft
security: proprietary - GAIA AIR Internal Use Only
responsiblePartnerCompany: GAIAPULSE
originator: Amedeo Pelliccia & AI Collaboration
date: 2025-02-17
---

# Cabin Temperature Control System (CTCS) - System Description

## 1. Applicability

This data module provides a detailed description of the Cabin Temperature Control System (CTCS) installed on the AMPEL360XWLRGA aircraft. It applies to all configurations unless otherwise specified.

---

## 2. References

The following documents are referenced within this data module:

| Document Code               | Title                                                                 | Version/Revision | Purpose                                                                 |
|-----------------------------|---------------------------------------------------------------------------|-------------------|-----------------------------------------------------------------------------|
| GPAM-AMPEL-0201-24-001-A        | Primary Power Generation System (S1000D)                                 | Rev A             | Provides power supply details for CTCS components.                         |
| GPAM-AMPEL-0201-28-Q2-001       | AEHCS System Overview and Architecture (S1000D)                          | Rev B             | Describes the source of conditioned air for the CTCS.                      |
| GPAM-AMPEL-0201-31-002-A        | Instrument Panel Layout Diagrams (S1000D)                                | Rev A             | Shows the location of temperature controls and displays.                   |
| GPAM-AMPEL-0201-45-001          | Central Maintenance Computer (CMC) Specifications (S1000D)               | Rev C             | Details the interface with the CMC for monitoring and diagnostics.         |
| GPAM-AMPEL-0201-46-001-A        | Data Network Architecture (S1000D)                                       | Rev A             | Describes the network communication protocols used by the CTCS.            |
| [Honeywell HPT-7500-T Manual] | Honeywell HPT-7500-T Temperature Sensor Technical Manual                  | Rev 1.2           | Provides detailed specifications and maintenance information for the cabin temperature sensors. |
| [Parker Hannifin Valve Manual] | Parker Hannifin Control Valve Technical Manual                           | Rev 2.0           | Provides detailed specifications and maintenance information for the control valves. |
| DO-178C                         | Software Considerations in Airborne Systems and Equipment Certification  | N/A               | Governs the software development process for the CTCS ECU.                 |
| DO-160G                         | Environmental Conditions and Test Procedures for Airborne Equipment      | N/A               | Specifies the environmental testing requirements for CTCS components.      |

---

## 3. System Overview

The Cabin Temperature Control System (CTCS) is an integrated, fully automatic system designed to maintain a comfortable and consistent cabin temperature for passengers and crew on the AMPEL360XWLRGA aircraft. It utilizes feedback from multiple temperature sensors to regulate the flow of conditioned air into the cabin, minimizing reliance on traditional bleed air systems by primarily using the **Atmospheric Energy Harvesting and Conversion System (AEHCS)** as the source of conditioned air. The CTCS is controlled by a dedicated **Electronic Control Unit (ECU)** and interfaces with the aircraft's **Central Maintenance Computer (CMC)** for monitoring, diagnostics, and fault reporting.

---

## 4. Functional Description

The CTCS operates as a closed-loop control system. Here's a breakdown of its operation:

1.  **Temperature Sensing:** Temperature sensors, strategically located throughout the cabin and in the air distribution ducts, provide real-time temperature readings to the ECU.
2.  **Setpoint Comparison:** The ECU compares these readings to the desired temperature setpoint, which is selected by the pilot on the instrument panel (refer to `GPAM-AMPEL-0201-31-002-A`).
3.  **Control Signal Calculation:** The ECU calculates the necessary adjustments to the **Hot Air Control Valve** (`GPAM-AMPEL-0201-21-CTV-001-P`) and **Cold Air Control Valve** (`GPAM-AMPEL-0201-21-CTV-002-P`) to achieve the desired supply air temperature.
4.  **Valve Actuation:** The ECU sends control signals to the valves, modulating the flow of hot and cold air from the AEHCS.
5.  **Air Mixing:** The Hot and Cold Air Control Valves feed into the **Air Mix Valve** (`GPAM-AMPEL-0201-21-AMV-001-P`), which blends the air streams to achieve the precise temperature required.
6.  **Air Distribution:** The conditioned air is then distributed throughout the cabin via the **Air Distribution System**, consisting of ducts and diffusers.
7.  **Recirculation:** Recirculation fans enhance air circulation and ensure even temperature distribution throughout the cabin.
8. **Fault Management:** The ECU performs continuous fault detection, and logs any detected faults to the CMC.

---

## 5. System Diagram

```mermaid
graph LR
    subgraph CTCS
        A[Temperature Sensors Multiple Locations] --> B(ECU - Electronic Control Unit);
        B --> C[Hot Air Control Valve GPAM-AMPEL-0201-21-CTV-001-P];
        B --> D[Cold Air Control Valve GPAM-AMPEL-0201-21-CTV-002-P];
        C --> E[Air Mix Valve GPAM-AMPEL-0201-21-AMV-001-P];
        D --> E;
        E --> F[Air Distribution System];
        F --> G[Cabin];
        G --> A;
    end
    subgraph AEHCS
        H[AEHCS] --> C;
        H --> D;
        style H fill:#98FB98,stroke:#228B22,stroke-width:2px,color:black
    end
    style A fill:#ccf,stroke:#333,stroke-width:1px,color:black
    style B fill:#f9f,stroke:#333,stroke-width:2px,color:black
    style C fill:#cce0ff,stroke:#3366cc,stroke-width:1px,color:black
    style D fill:#cce0ff,stroke:#3366cc,stroke-width:1px,color:black
    style E fill:#cce0ff,stroke:#3366cc,stroke-width:1px,color:black
    style F fill:#cce0ff,stroke:#3366cc,stroke-width:1px,color:black
    style G fill:#cce0ff,stroke:#3366cc,stroke-width:1px,color:black
```

*Figure 1: CTCS System Schematic Diagram*

---

## 6. Main Components

The CTCS comprises the following main components:

| Component               | Part Number                      | Description                              | Manufacturer     | Quantity |
|-----------------------------|--------------------------------------|----------------------------------------------|------------------|----------|
| Temperature Sensor (Cabin)  | GPAM-AMPEL-0201-21-TS-001-P         | Measures cabin air temperature              | Honeywell        | 4        |
| Temperature Sensor (Duct)   | GPAM-AMPEL-0201-21-TS-002-P         | Measures air temperature in ducts           | Honeywell        | 2        |
| Hot Air Control Valve       | GPAM-AMPEL-0201-21-CTV-001-P        | Modulates hot air flow from AEHCS           | Parker Hannifin  | 1        |
| Cold Air Control Valve      | GPAM-AMPEL-0201-21-CTV-002-P        | Modulates cold air flow from AEHCS          | Parker Hannifin  | 1        |
| Air Mix Valve               | GPAM-AMPEL-0201-21-AMV-001-P        | Mixes hot and cold air                      | Parker Hannifin  | 1        |
| Electronic Control Unit     | GPAM-AMPEL-0201-21-ECU-001-P        | Controls CTCS based on sensor inputs        | GAIAPULSE        | 1        |
| Recirculation Fan           | GPAM-AMPEL-0201-21-FAN-001-P        | Circulates air within the cabin             | EBM-Papst        | 2        |
| Air Distribution Ducts      | GPAM-AMPEL-0201-21-DUCT-001-P       | Distributes conditioned air                 | GAIAPULSE        | Varies   |
| Air Diffusers               | GPAM-AMPEL-0201-21-DIFF-001-P       | Distributes air into the cabin              | GAIAPULSE        | Varies   |

---

## 7. Control Logic

The ECU utilizes a **Proportional-Integral-Derivative (PID)** control algorithm to regulate the valve positions and maintain the desired cabin temperature. The algorithm considers:

- **Cabin Temperature**: Readings from multiple temperature sensors are processed to determine the representative cabin temperature.
- **Duct Temperature**: Duct temperature sensors provide feedback on the hot and cold air stream temperatures.
- **Setpoint Temperature**: The desired temperature selected by the pilot.
- **PID Parameters**: The PID parameters (`Kp`, `Ki`, `Kd`) are configurable via the CMC (refer to `GPAM-AMPEL-0201-45-001`).

---

## 8. Next Steps

1.  **Convert to S1000D XML**: Use an XML editor (e.g., Oxygen XML) to transform this Markdown into S1000D-compliant XML, adhering to **S1000D Issue 4.2** and the project Business Rules defined in **DMC-BREX-SAMPLE-0000-0000-00A-00Z-00_EN-US**.
2.  **Validate Schema**: Ensure the XML adheres to the S1000D Issue 4.2 schema.
3.  **Integrate into CSDB**: Upload the XML to the Common Source Database (CSDB) for version control and traceability.
4.  **Peer Review**: Conduct a review with systems engineers, maintainers, and S1000D specialists.

---

## 9. Roles and Responsibilities

Clear roles and responsibilities are crucial for the successful creation, maintenance, and evolution of the ECS documentation. Assigning ownership for each Data Module ensures accountability and streamlines the workflow. The following table outlines the proposed roles responsible for the development and upkeep of each Data Module. These roles are indicative and may need to be adjusted based on the specific organizational structure and project team.

| DMC                                | Title                                        | Primary Responsibility Role(s)                | Supporting Role(s)                                |
|------------------------------------|----------------------------------------------|-------------------------------------------------|---------------------------------------------------|
| DM-FTC_21-00-00-00-000-AGI-D        | ECS Abstract (AGI)                             | Systems Engineering, Project Management          | Lead Design Engineer, Technical Publications Lead      |
| DM-FTC_21-00-00-00-000-CON-D        | ECS Concept (Preliminary Design)             | Lead Design Engineer, Systems Engineering         | Design Engineering Team, Aerodynamics Team          |
| DM-FTC_21-00-00-00-000-DES-SYS-DESC | ECS Design - System Description              | Design Engineering Team                          | Systems Engineering, Technical Specialist (ECS)      |
| DM-FTC_21-00-00-00-010-DES-SYS-STD  | ECS Design - System Standard Practices        | Design Engineering Team, Reliability Engineering | Systems Engineering, Certification Engineer        |
| DM-FTC_21-00-00-00-030-DES-COMP-LST | ECS Design - Components List                 | Component Engineering, Procurement              | Design Engineering Team, Supply Chain Management      |
| DM-FTC_21-00-00-00-040-DES-PBS      | ECS Design - Components Breakdown (PBS)       | Systems Engineering, Design Engineering Team      | Configuration Management, Integration Engineering    |
| DM-FTC_21-00-00-00-050-DES-BOM      | ECS Design - Bill of Materials (BoM)          | Procurement, Component Engineering              | Supply Chain Management, Configuration Management      |
| DM-FTC_21-00-00-00-051-DES-SYS-STR  | ECS Design - System Standard Practices & Structures | Structural Engineering, Design Engineering Team  | Materials Engineering, Certification Engineer        |
| DM-FTC_21-00-00-00-053-DES-TRB      | ECS Design - Troubleshooting                  | Maintenance Engineering, Technical Support        | Field Service Engineers, Reliability Engineering     |
| DM-FTC_21-00-00-00-060-DES-PROP     | ECS Design - Propellant Interaction           | Fuel Systems Engineering, Safety Engineering     | Chemical Engineering (if applicable), Ground Operations |
| DM-FTC_21-00-00-00-070-DES-ENG-INT  | ECS Design - Engine Integration               | Propulsion Engineering, Design Engineering Team    | Engine OEM Liaison, Flight Controls Engineering      |
| DM-FTC_21-00-00-00-080-DES-SAF-MOD  | ECS Design - Safety and Failure Modes         | Safety Engineering, Reliability Engineering       | Design Engineering Team, Certification Engineer        |
| DM-FTC_21-00-00-00-090-DES-ENV-IMP  | ECS Design - Environmental Impact             | Environmental Engineering, Sustainability Team    | Design Engineering Team, Regulatory Compliance     |
| DM-FTC_21-00-00-00-100-DES-MNT-PRO  | ECS Design - Maintenance Procedures           | Maintenance Engineering, Technical Publications   | Field Service Engineers, Reliability Engineering     |
| DM-FTC_21-00-00-00-103-DES-HMI      | Human-Machine Interface (HMI) Design          | Human Factors Engineering, Avionics Engineering   | Flight Operations, Maintenance Engineering         |
| DM-FTC_21-00-00-00-110-DES-EVO-UPG | ECS Design - System Evolution and Upgrades      | Systems Engineering, Product Development        | Design Engineering Team, Certification Engineer        |
| DM-FTC_21-00-00-00-120-DES-TRN-DOC  | ECS Design - Training and Documentation       | Technical Publications, Training Department       | Subject Matter Experts (from relevant engineering teams) |
| DM-FTC_21-00-00-00-130-DES-PER-MET  | ECS Design - Performance Metrics              | Performance Analysis, Systems Engineering        | Flight Test Engineering, Data Analytics Team         |
| DM-FTC_21-00-00-00-140-DES-CFG-MGT  | ECS Design - Configuration Management         | Configuration Management, Quality Assurance     | All DM Owners (for content inputs and approvals)      |
| DM-FTC_21-00-00-00-150-DES-INN-CON  | ECS Design - Innovative Considerations        | Innovation Team, R&D Department                 | Systems Engineering, Future Product Strategy        |
| DM-FTC_21-00-00-00-170-DES-ACR      | ECS Design - Acronyms                         | Technical Publications, Configuration Management  | All DM Owners (for acronym contribution and review) |

**Note:** "Primary Responsibility Role(s)" indicates the team or role primarily accountable for the content and updates of the DM. "Supporting Role(s)" indicates teams or roles that contribute to or review the DM content. These assignments are preliminary and should be formally validated and adjusted within the project's organizational context.

---

## 10. Revision History

| Version | Date       | Author(s)                | Description of Changes                                  |
| :------ | :--------- | :----------------------- | :-------------------------------------------------------- |
| 1.0     | 2025-02-14 | AI Assistant & Amedeo Pelliccia     | Initial Draft Document                                  |
| 1.1     | 2025-10-27 | Amedeo Pelliccia         | Added "Roles and Responsibilities" section              |

---
**Document Code:** GPAM-AMPEL-0201-21-002-A
