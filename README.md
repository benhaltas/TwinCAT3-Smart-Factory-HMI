# Smart Factory Process Control Simulation (TwinCAT 3)

A professional industrial automation project developed using **Beckhoff TwinCAT 3**. This project simulates a continuous production line for a smart factory, integrating PLC logic, HMI visualization, and IIoT connectivity.

##  Project Demo
[Click here to watch the operation video](https://youtu.be/J6CA5q3nxms)

---


https://github.com/user-attachments/assets/2a1c6a20-d754-4be7-b594-4c21fe66e749


---

##  System Architecture & Features

This project is built on a robust **State Machine** architecture and utilizes industrial best practices for structured programming (IEC 61131-3).

### 1. Advanced State Machine Control
The core logic is managed via a non-blocking `CASE` structure, ensuring deterministic behavior.
* **States:** IDLE ➔ INIT ➔ FILLING ➔ HEATING ➔ MIXING ➔ BOTTLING ➔ COMPLETE.
* **Continuous Loop:** The system is designed to run in a continuous production cycle until stopped by the operator or a safety interrupt.

### 2. Dynamic Recipe Management
Utilizes custom **Data Structures (DUTs)** to handle multi-product production.
* Operator can switch between products (e.g., **Cola** vs. **Juice**) via HMI.
* Targets for filling volume, temperature, and mixing duration are updated dynamically in real-time.

### 3. Predictive Maintenance (Industry 4.0)
Integrated a vibration and temperature monitoring simulation to prevent machine failure.
* **Cycle Monitoring:** Tracks valve actuations and component stress.
* **Intelligent Shutdown:** Automatically halts production and locks the system when a maintenance threshold is reached (e.g., simulated heat or vibration anomaly).
* **Maintenance Mode:** Requires a dedicated technician reset to re-calibrate and restart the process.

### 4. Machine Safety & HMI
* **Emergency Stop:** A high-priority safety interrupt that instantly kills all actuators and locks the UI.
* **Live SCADA Dashboard:** Real-time visualization of tank levels, temperatures, production counters (OEE), and system status strings.

### 5. OT-IT Connectivity & Data Logging (IIoT Bridge)
To demonstrate Industry 4.0 integration, I developed a high-level monitoring script using **Python** to act as a bridge between the PLC (OT) and Data Analytics (IT).
* **Live Telemetry:** Using the **ADS (Automation Device Specification)** protocol, Python extracts real-time variables directly from the TwinCAT runtime.
* **Historian / Data Archiving:** The system automatically logs production data (Timestamps, Status, Production Counts, and Temperature) into a `.csv` format, creating a historical record for OEE analysis.
* **Scalability:** This setup serves as the foundation for further integrations like MQTT cloud publishing or predictive AI modeling.

---

##  Technical Stack
* **Logic:** Structured Text (ST) - IEC 61131-3
* **Platform:** Beckhoff TwinCAT 3 (XAE / XAR)
* **Connectivity:** Python (pyads library)
* **Visualization:** TwinCAT HMI (Integrated Visualization)
* **Data Persistence:** CSV Data Logging (Historian)
* **Design Patterns:** State Machine, Dynamic Recipe Handling, Rising Edge Triggers.

---

##  About the Author
**Ahmed Haltas**
* **M.Eng. Industry 4.0 Student** @ Hochschule Albstadt-Sigmaringen
* **B.Sc.Mechanical Engineering**
* **Specialization:** Integrating Mechanical Design (CAD/CAE) with Industrial Automation, System Integration, and IIoT.

 **Connect with me:** [LinkedIn](https://www.linkedin.com/in/ahmedhaltas/)
