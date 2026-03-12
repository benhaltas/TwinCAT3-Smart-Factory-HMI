import pyads
import time

plc = pyads.Connection('127.0.0.1.1.1', 851) 

try:
    plc.open()
    print("🚀 PLC Connection Established!")
    print("-" * 30)

    while True:
        
        total_bottles = plc.read_by_name('GVL_Process.nTotalBottles', pyads.PLCTYPE_INT)
        current_temp = plc.read_by_name('GVL_Process.fCurrentTemp', pyads.PLCTYPE_REAL)
        status = plc.read_by_name('GVL_Process.sStatusMessage', pyads.PLCTYPE_STRING)

        print(f"Status: {status}")
        print(f"Total Produced: {total_bottles} | Temp: {current_temp:.2f}°C")
        print("-" * 30)
        
        time.sleep(1) 

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    plc.close()