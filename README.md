# Smart Factory Process Control Simulation (TwinCAT 3)

A professional industrial automation project developed using **Beckhoff TwinCAT 3**. This project simulates a continuous production line for a smart factory, integrating PLC logic, HMI visualization, and Predictive Maintenance concepts.

## Project Demo
To watch the full operation video: https://youtu.be/J6CA5q3nxms

https://github.com/user-attachments/assets/a9459346-ef92-409f-98cb-9ce65f870b9c

---

## System Architecture & Features

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
* **Intelligent Shutdown:** Automatically halts production and locks the system when a maintenance threshold is reached.
* **Maintenance Mode:** Requires a dedicated technician reset to re-calibrate and restart the process.

### 4. Machine Safety & HMI
* **Emergency Stop:** A high-priority safety interrupt that instantly kills all actuators and locks the UI.
* **Live SCADA Dashboard:** Real-time visualization of tank levels, temperatures, production counters (OEE), and system status strings.

---

##  Technical Stack
* **Logic:** Structured Text (ST) - IEC 61131-3
* **Platform:** Beckhoff TwinCAT 3 (XAE / XAR)
* **Visualization:** TwinCAT HMI (Integrated Visualization)
* **Design Patterns:** State Machine, Dynamic Recipe Handling, Rising Edge Triggers.

---

## About the Author
**Ahmed Haltas**
* **M.Eng. Industry 4.0** Student @ Hochschule Albstadt-Sigmaringen
* **B.Sc. Mechanical Engineering**
* Specializing in the integration of Mechanical Design (CAD/CAE) with Industrial Automation.

📫 **Connect with me:** [LinkedIn](https://www.linkedin.com/in/ahmedhaltas/)







