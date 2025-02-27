
---
product: GAIA-AIR-CSDB
applicability: AMPEL Hydraulic System
ata: 29
dmc: GPAM-AMPEL-0201-29-001-A
issueDate: 2024-01-26
status: final
security: public
type: maintenance procedure
title: Hydraulic System Leak Check and Component Inspection
---

# GPAM-AMPEL-0201-29-001-A: Hydraulic System Leak Check and Component Inspection

## Table of Contents

1.  [Applicability](#applicability)
2.  [Purpose](#purpose)
3.  [Safety Precautions](#safety-precautions)
4.  [Prerequisites](#prerequisites)
5.  [Resources](#resources)
    *   5.1 [Tools and Equipment](#tools-and-equipment)
    *   5.2 [Consumables](#consumables)
    *   5.3 [Personnel](#personnel)
    *   5.4 [References](#references)
6.  [Procedure](#procedure)
    *   6.1 [Preparation](#preparation)
    *   6.2 [Leak Check](#leak-check)
    *   6.3 [Component Inspection](#component-inspection)
        *   6.3.1 [Hydraulic Pump (AMPEL-HYD-PUMP-100)](#hydraulic-pump-ampel-hyd-pump-100)
        *   6.3.2 [Hydraulic Actuators (AMPEL-ACT-FLAP-100)](#hydraulic-actuators-ampel-act-flap-100)
        *   6.3.3 [Hydraulic Reservoir (AMPEL-HYD-RES-100)](#hydraulic-reservoir-ampel-hyd-res-100)
    *   6.4 [Post-Inspection](#post-inspection)
7.  [Acceptance Criteria](#acceptance-criteria)
8.  [Close-Up](#close-up)

## 1. Applicability <a name="applicability"></a>

This procedure applies to the AMPEL hydraulic system (Part No. AMPEL-HYD-SYS-100) on GAIA-AIR-CSDB aircraft with serial numbers CSDB-1001 through CSDB-1050.

## 2. Purpose <a name="purpose"></a>

To provide instructions for performing a visual leak check and detailed component inspection of the AMPEL hydraulic system to ensure integrity and prevent failures.

## 3. Safety Precautions <a name="safety-precautions"></a>

**WARNING:** Hydraulic fluid operates at **3000 PSI** and can cause serious injection injuries. Always relieve system pressure before disassembly to prevent fluid injection. Refer to [GPAM-AMPEL-0002-01-001-A](#cross-reference-to-GPAM-AMPEL-0002-01-001-A) for depressurization procedures.

**CAUTION:** Wear **ANSI Z87.1 goggles and nitrile gloves** when handling Skydrol LD-4 hydraulic fluid to prevent skin and eye irritation. Refer to the Skydrol LD-4 Material Safety Data Sheet (MSDS) for detailed safety information.

Refer to [AMM-ATA12-24-001](#cross-reference-to-AMM-ATA12-24-001) for aircraft safety guidelines.

## 4. Prerequisites <a name="prerequisites"></a>

*   Aircraft parked on a level surface and chocked. Verify chocks are properly installed per [AMM-ATA10-11-001](#cross-reference-to-AMM-ATA10-11-001).
*   Hydraulic system **depressurized** (refer to [GPAM-GEN-0001-01-001-A](#cross-reference-to-GPAM-GEN-0001-01-001-A)). Verify pressure is 0 PSI using a calibrated pressure gauge.
*   Work area clean and well-lit (min **50 foot-candles** illumination).

## 5. Resources <a name="resources"></a>

### 5.1 Tools and Equipment <a name="tools-and-equipment"></a>

*   Hydraulic pressure gauge (0-5000 psi, ±1% accuracy)
*   Torque wrench (10-50 ft-lbs, ±2%)
*   Multimeter (Fluke 87V or equivalent)
*   Hydraulic fluid drain pan (5-gallon capacity)

### 5.2 Consumables <a name="consumables"></a>

*   Hydraulic fluid (Skydrol LD-4)
*   Cleaning solvent (Isopropyl Alcohol, 99%)
*   Safety wire (0.032-inch stainless steel)

### 5.3 Personnel <a name="personnel"></a>

*   One (1) qualified aircraft mechanic trained on AMPEL hydraulic systems.

### 5.4 References <a name="references"></a>

*   Aircraft Maintenance Manual (AMM), ATA Chapter 29
*   System Schematic Diagram: GAIA-AIR-CSDB-29-HYD-001
*   Component Maintenance Manuals (CMM):
    *   AMPEL-HYD-PUMP-100 (Hydraulic Pump)
    *   AMPEL-HSCU-200 (Hydraulic System Control Unit)
    *   AMPEL-ACT-FLAP-100 (Flap Actuator)

## 6. Procedure <a name="procedure"></a>

### 6.1 Preparation <a name="preparation"></a>

1.  Gather tools and PPE.
2.  Ensure aircraft configuration meets prerequisites.
3.  Open access panels 29-1A, 29-2B, and 29-3C.

### 6.2 Leak Check <a name="leak-check"></a>

1.  Inspect hydraulic lines, fittings, and components for leaks.
2.  Use an **inspection mirror and flashlight** for hidden areas.
3.  Categorize leaks as **minor, moderate, or severe** (see [TSM-ATA29-00-001](#cross-reference-to-TSM-ATA29-00-001)).
4.  Document findings in the maintenance log.

### 6.3 Component Inspection <a name="component-inspection"></a>

#### 6.3.1 Hydraulic Pump (AMPEL-HYD-PUMP-100) <a name="hydraulic-pump-ampel-hyd-pump-100"></a>

*   Inspect for cracks, dents, and loose fittings. Refer to [CMM-AMPEL-HYD-PUMP-100, Section 3.2](#cross-reference-to-CMM-AMPEL-HYD-PUMP-100).
*   Verify pressure output is between 2900-3100 PSI using the hydraulic test stand per [CMM-AMPEL-HYD-PUMP-100, Section 4.1](#cross-reference-to-CMM-AMPEL-HYD-PUMP-100).

    ```svg
## Diagrammatic Recap of GPAM Documentation Suite

This Markdown provides a diagrammatic recap of the different types of diagrams developed for the GPAM (Ground Procedure and Maintenance Manual) documentation suite. This visual index helps users understand the structure of the visual aids and quickly locate the appropriate diagram for their needs.

```mermaid
flowchart TB
    root("GPAM Diagram Types Overview")
    root --> workflow(Overall Maintenance Workflow Diagrams)
    root --> inspection(Component Inspection Diagrams)
    root --> repair(Repair Procedure Diagrams)
    root --> troubleshoot(Troubleshooting Guides)

    subgraph workflow_cluster [Overall Workflow Diagrams]
        direction TB
        workflow --> workflow_main["Main Maintenance Workflow <br/> (Diagram 1)"]
    end

    subgraph inspection_cluster [Component Inspection Diagrams]
        direction TB
        inspection --> inspect_actuator["Actuator Inspection <br/> (Diagram 3)"]
        inspection --> inspect_reservoir["Reservoir Inspection <br/> (Diagram 4)"]
        inspection --> inspect_pump["Pump Inspection <br/> (Diagram - Textual Section 6.3)"]
    end

    subgraph repair_cluster [Repair Procedure Diagrams]
        direction TB
        repair --> repair_line["Line Replacement <br/> (Diagram 5)"]
        repair --> repair_actuator_seal["Actuator Seal Replacement <br/> (Diagram 6)"]
        repair --> repair_pump_seal["Pump Seal Replacement <br/> (Diagram 7)"]
        repair --> repair_valve_overhaul["Valve Overhaul <br/> (Diagram 8)"]
    end

    subgraph troubleshoot_cluster [Troubleshooting Guides]
        direction TB
        troubleshoot --> troubleshoot_hydraulic["Hydraulic System Troubleshooting <br/> (Diagram 2)"]
    end

    style root fill:#f9f9f9,stroke:#333,stroke-width:2px
    style workflow_cluster fill:#e0f7fa,stroke:#333,stroke-width:1px
    style inspection_cluster fill:#e0f7fa,stroke:#333,stroke-width:1px
    style repair_cluster fill:#f0f4c3,stroke:#333,stroke-width:1px
    style troubleshoot_cluster fill:#ffe0b2,stroke:#333,stroke-width:1px

    linkStyle default stroke:#999,stroke-width:1px,color:#555
```

**Diagrammatic Recap - Explanation:**

This Mermaid diagram provides a high-level visual index of the GPAM diagrammatic documentation:

*   **"GPAM Diagram Types Overview" (Central Node):**  Represents the entry point to the visual index.
*   **Main Diagram Categories (Branches):**
    *   **Overall Maintenance Workflow Diagrams:**  Diagrams showing the general maintenance process flow.
    *   **Component Inspection Diagrams:** Diagrams detailing inspection procedures for specific components.
    *   **Repair Procedure Diagrams:** Diagrams outlining step-by-step repair tasks.
    *   **Troubleshooting Guides:** Diagrams providing decision trees for diagnosing system issues.
*   **Subgraphs for Each Category:** Each category is visually grouped within a subgraph, making the diagram more organized and readable.
*   **Diagram Labels and Numbers:** Each specific diagram is labeled with its name and assigned Diagram number for easy reference within the GPAM documentation.
*   **Consistent Styling:**  Color coding and consistent link styles are used to enhance visual clarity and organization.

**How to Use this Diagram:**

1.  **Understand Diagram Types:**  Quickly grasp the different categories of visual documentation available.
2.  **Navigate to Specific Diagrams:** Use the diagram as a visual index to locate the diagram needed for a particular task (e.g., "I need the diagram for Actuator Seal Replacement... Ah, it's Diagram 6 under 'Repair Procedure Diagrams'").
3.  **See the Big Picture:** Understand how the different types of diagrams fit together to create a comprehensive visual documentation suite for Hydraulic System Maintenance.

This Markdown provides the Mermaid code for the diagrammatic recap, along with a textual explanation of its structure and usage. You can copy and paste this Markdown directly into your GPAM documentation.
#### 6.3.1 Hydraulic Pump (AMPEL-HYD-PUMP-100) `<a name="hydraulic-pump-ampel-hyd-pump-100">``</a>`

**1. Visual Inspection Requirements:**

- Inspect for cracks, dents, and loose fittings per [CMM-AMPEL-HYD-PUMP-100, Section 3.2](#cross-reference-to-CMM-AMPEL-HYD-PUMP-100)

- Surface inspection criteria:

- No cracks permitted in any surface
- Maximum dent depth: 0.010 inches
- Document location of any damage



- Torque specifications:

- Input port fitting: 65 ft-lbs
- Output port fitting: 55 ft-lbs
- Case drain fitting: 25 ft-lbs








**2. Disassembly and Test Preparation:**

- Follow disassembly sequence:

1. Remove all connectors and fittings
2. Clean and inspect internal components
3. Install test gears per specifications
4. Verify all seals are properly seated





**3. Test Stand Setup Requirements:**

- Configure per [CMM-AMPEL-HYD-PUMP-100, Section 4.1](#cross-reference-to-CMM-AMPEL-HYD-PUMP-100)

- System parameters:

- Minimum inlet pressure: 30 PSI
- Return line: unrestricted flow
- Case drain: properly connected
- Oil temperature: 120°F ±10°F
- Warm-up time: 5 minutes minimum








**4. Pressure Test Procedure:**

- Test specifications:

- Target pressure range: 2900-3100 PSI
- Hold time: 2 minutes minimum
- Operating speed: 1800 ±50 RPM
- Maximum case drain flow: 2 GPM





**5. Troubleshooting Guide:**

- If pressure is out of range:

1. Check all external seals
2. Verify connection torques
3. Monitor case drain flow
4. Confirm oil temperature
5. Verify operating speed
6. Document all findings





**6. Documentation Requirements:**

- Record all test results:

- Final pressure reading
- Operating temperature
- Case drain flow rate
- Any repairs or adjustments made
- Inspector name and date

``

#### 6.3.2 Hydraulic Actuators (AMPEL-ACT-FLAP-100) <a name="hydraulic-actuators-ampel-act-flap-100"></a>

*   Check for smooth movement and no binding throughout the full range of travel.
*   Inspect actuator rods for pitting or corrosion. Refer to [CMM-AMPEL-ACT-FLAP-100, Section 2.5](#cross-reference-to-CMM-AMPEL-ACT-FLAP-100) for corrosion limits.

    ```svg
    <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiPgogIDwhLS0gQmFja2dyb3VuZCAtLT4KICA8cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iI0YwRjBGMCUiIC8+CgogIDwhLS0gUmVjdGFuZ2xlIC0tPgogIDxyZWN0IHg9IjIwIiB5PSIyMCIgd2lkdGg9IjYwIiBoZWlnaHQ9IjYwIiBzdHlsZT0iZmlsbDojMkRBNzQ4OyIvPgogIDxsaW5lIHgxPSIyMCIgeTE9IjIwIiB4Mj0iODAiIHkyPSI4MCIgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyIiAvPgogIDxsaW5lIHgxPSI4MCIgeTE9IjIwIiB4Mj0iMjAiIHkyPSI4MCIgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyIiAvPgogIDx0ZXh0IHg9IjUwJSIgeT0iNTUlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgc3R5bGU9ImZvbnQtc2l6ZToxMHB4O2ZvbnQtZmFtaWx5OkFyaWFsLHNhbnMtc2VyaWY7ZmlsbDojRkZGRkZGOyI+QWN0dWF0b3I8L3RleHQ+Cjwvc3ZnPg==" alt="Hydraulic Actuator Diagram">
    ```

#### 6.3.3 Hydraulic Reservoir (AMPEL-HYD-RES-100) <a name="hydraulic-reservoir-ampel-hyd-res-100"></a>

*   Verify fluid level between MIN and MAX marks.
*   Inspect vent lines for kinks, cracks, or obstructions that could prevent proper venting.

    ```svg
    <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiPgogIDwhLS0gQmFja2dyb3VuZCAtLT4KICA8cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iI0YwRjBGMCUiIC8+CgogIDwhLS0gRWxsaXBzZSAtLT4KICA8ZWxsaXBzZSBjeD0iNTAlIiBjeT0iNTAlIiByeD0iNDUiIHJ5PSIzMCIgc3R5bGU9ImZpbGw6I0E2NEQ3OTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MiIvPgogIDx0ZXh0IHg9IjUwJSIgeT0iNTUlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgc3R5bGU9ImZvbnQtc2l6ZToxMHB4O2ZvbnQtZmFtaWx5OkFyaWFsLHNhbnMtc2VyaWY7ZmlsbDojRkZGRkZGOyI+UmVzZXJ2b2lyPC90ZXh0Pgo8L3N2Zz4K" alt="Hydraulic Reservoir Diagram">
    ```

### 6.4 Post-Inspection <a name="post-inspection"></a>

1.  Clean any spilled fluid.
2.  Secure all access panels.
3.  Remove Lockout/Tagout devices.
4.  Document findings and corrective actions in the maintenance log, including the date, mechanic's signature, and any work order numbers created.
5.  Create maintenance work orders in [Maintenance Tracking System Name], if needed, and ensure they include a detailed description of the discrepancy, the corrective action taken, and any parts replaced.

## 7. Acceptance Criteria <a name="acceptance-criteria"></a>

*   No hydraulic leaks (within AMM limits).
*   Fluid level within acceptable range.
*   No visible damage or excessive corrosion.
*   Properly torqued and secured components.

## 8. Close-Up <a name="close-up"></a>

*Figure 1: AMPEL Hydraulic Pump Inspection Points*
<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiPgogIDwhLS0gQmFja2dyb3VuZCAtLT4KICA8cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iI0YwRjBGMCUiIC8+CgogIDwhLS0gQ2lyY2xlIC0tPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjQwIiBzdHlsZT0iZmlsbDojMDA3OGZmOyIgLz4KCiAgPHRleHQgeD0iNTAlIiB5PSI1NSUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiBzdHlsZT0iZm9udC1zaXplOjIwcHg7Zm9udC1mYW1pbHk6QXJpYWwsc2Fucy1zZXJpZjtmaWxsOiNGRkZGRkY7Ij5QdW1wPC90ZXh0Pgo8L3N2Zz4K" alt="Hydraulic Pump Diagram">

_Figure 1: Shows the hydraulic pump and key inspection points._

*Figure 2: AMPEL Flap Actuator Leak Check Points*
<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiPgogIDwhLS0gQmFja2dyb3VuZCAtLT4KICA8cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iI0YwRjBGMCUiIC8+CgogIDwhLS0gUmVjdGFuZ2xlIC0tPgogIDxyZWN0IHg9IjIwIiB5PSIyMCIgd2lkdGg9IjYwIiBoZWlnaHQ9IjYwIiBzdHlsZT0iZmlsbDojMkRBNzQ4OyIvPgogIDxsaW5lIHgxPSIyMCIgeTE9IjIwIiB4Mj0iODAiIHkyPSI4MCIgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyIiAvPgogIDxsaW5lIHgxPSI4MCIgeTE9IjIwIiB4Mj0iMjAiIHkyPSI4MCIgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyIiAvPgogIDx0ZXh0IHg9IjUwJSIgeT0iNTUlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgc3R5bGU9ImZvbnQtc2l6ZToxMHB4O2ZvbnQtZmFtaWx5OkFyaWFsLHNhbnMtc2VyaWY7ZmlsbDojRkZGRkZGOyI+QWN0dWF0b3I8L3RleHQ+Cjwvc3ZnPg==" alt="Hydraulic Actuator Diagram">

_Figure 2: Identifies potential leak points in the actuator._

*Figure 3: AMPEL Directional Control Valve Assembly*
<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiPgogIDwhLS0gQmFja2dyb3VuZCAtLT4KICA8cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iI0YwRjBGMCUiIC8+CgogIDwhLS0gRWxsaXBzZSAtLT4KICA8ZWxsaXBzZSBjeD0iNTAlIiBjeT0iNTAlIiByeD0iNDUiIHJ5PSIzMCIgc3R5bGU9ImZpbGw6I0E2NEQ3OTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MiIvPgogIDx0ZXh0IHg9IjUwJSIgeT0iNTUlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgc3R5bGU9ImZvbnQtc2l6ZToxMHB4O2ZvbnQtZmFtaWx5OkFyaWFsLHNhbnMtc2VyaWY7ZmlsbDojRkZGRkZGOyI+UmVzZXJ2b2lyPC90ZXh0Pgo8L3N2Zz4K" alt="Hydraulic Reservoir Diagram">

_Figure 3: Highlights the valve body and key components._

---
### **Next Steps:**

1.  **Replace Placeholder SVGs:**  *This is the most important step!* Create accurate, detailed SVG diagrams of the AMPEL hydraulic system components.  Use labels, callouts, and arrows to highlight key areas.  **To replace, you need to:**
    *   Create your SVG diagrams using a vector editor.
    *   Encode your SVG files to Base64 strings.
    *   Replace the `data:image/svg+xml;base64,...` part in the `<img>` tags with your new Base64 encoded SVG strings.
2.  **Validate all data** against official technical documentation (AMM, CMM, etc.).
3.  **Implement all cross-references** within your publishing system to create a hyperlinked document.
4.  **Conduct a technical review** by a qualified aircraft mechanic familiar with the AMPEL hydraulic system.
5.  **Test Rendering:** Verify that the Markdown document renders correctly in your chosen Markdown viewer and publishing system.  Pay close attention to the SVG images.
6.  **Publish to S1000D-compliant formats (HTML, PDF, XML).**

This provides a complete, self-contained Markdown document with embedded SVG images.  Remember to focus on replacing the placeholder SVGs with your actual diagrams for a truly professional and accurate S1000D data module.

5.  **Implement Cross-References:**  Use your S1000D publishing system to create working hyperlinks between data modules.  This is where the real power of S1000D comes in.
6.  **Validate Content:**  Ensure the content is accurate, complete, and complies with S1000D standards and your organization's style guide.
7.  **Publish:**  Use your S1000D publishing system to generate the deployable output format (HTML, PDF, etc.).

This improved structure should give you a much better starting point for creating your S1000D data module. Remember to adapt it to the specific requirements of your project and organization. Let me know if you have any more questions.
