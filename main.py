from pyboy import PyBoy
from pathlib import Path
import time
import keyboard
from engine.fight import do_fight

BASE_DIR = Path(__file__).resolve().parent
state_save_path = BASE_DIR / "red.gb.state"

class PyBoy_Web(PyBoy):
    run_data = {
        "status_msg": "Manual Operation",
        "action_msg": "There not Action now.",
        "reason_msg": "There not Reason now.",
    }

pyboy = PyBoy_Web("red.gb")

if state_save_path.exists():
    with open(state_save_path, "rb") as f:
        pyboy.load_state(f)

def pyboy_thread():
    while True:
        # pyboy.memory[0xD023] = 0
        # pyboy.memory[0xD024] = 0 # revise enemy's max hp into 0 so that skip the discussion
        pyboy.tick()
        if keyboard.is_pressed("\\"):
            print("Saving state...")
            with open(state_save_path, "wb") as f:
                pyboy.save_state(f)
            print("State Saved!")
        if bool(pyboy.memory[0xD057]):
            do_fight(pyboy)
        
        time.sleep(0.01)

if __name__ == "__main__":
    pyboy_thread()