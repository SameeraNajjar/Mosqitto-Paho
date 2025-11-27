# Mosqitto-Paho

**Student ID:** 12114875  
**Author:** Sameera Najjar  

---

## **1. Project Description**

This lab demonstrates a simple **MQTT system** using:

- **Mosquitto broker** (running locally on Windows)
- **Paho MQTT Python library**
- **Multiple publishers**:
  - Temperature
  - Humidity
  - People Counter
- **Multiple subscribers**, each receiving only its topic.
- **Student ID included** in every message for identification.

The lab simulates **real-time sensor data** and demonstrates how publishers and subscribers communicate via MQTT topics.

---

## **2. Folder Structure**

mqtt_lab/
├─ temp_publisher.py
├─ humidity_publisher.py
├─ people_publisher.py
├─ temp_subscriber.py
├─ humidity_subscriber.py
├─ people_subscriber.py
└─ screenshots/ # save your screenshots here

yaml
Copy code

---

## **3. How to Run**

### Step 1 — Open VS Code or PowerShell
Navigate to project folder:

```powershell```
cd C:\Users\USER-Q\Documents\mqtt_lab

### Step 2 — Run Subscribers (one per terminal)
powershell
Copy code
python temp_subscriber.py
python humidity_subscriber.py
python people_subscriber.py

### Step 3 — Run Publishers (one per terminal)
powershell
Copy code
python temp_publisher.py
python humidity_publisher.py
python people_publisher.py
Subscribers will start receiving messages from the corresponding publishers in real-time.

## **4. Example Output**
Publisher (Temperature)
makefile
Copy code
Publishing: ID=12114875, Temperature=32
Publishing: ID=12114875, Temperature=21
Publishing: ID=12114875, Temperature=30
Subscriber (Temperature)
makefile
Copy code
Received: ID=12114875, Temperature=32
Received: ID=12114875, Temperature=21
Received: ID=12114875, Temperature=30
The same behavior occurs for Humidity and People Counter.

## **5. Screenshots**
Add screenshots of each script running in the screenshots/ folder. Example:

Script	Screenshot
temp_publisher.py	
humidity_publisher.py	
people_publisher.py	
temp_subscriber.py	
humidity_subscriber.py	
people_subscriber.py	

Replace the image filenames with the actual screenshots you take.

## **6. Notes**
Messages include Student ID (12114875) for tracking.

Random values simulate sensor data.

Paho DeprecationWarning is normal and does not affect functionality.

Mosquitto must be running before starting any publishers or subscribers.

Each script must run in its own terminal because publishers continuously send messages and subscribers continuously listen.

