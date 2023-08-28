# Countdown de 10 a 0 com atraso de 1s.
import time

for i in range(10, 1 - 1, -1):
    print(f"{i}...")
    time.sleep(1)
print("🎆🎆🎆 Feliz ano novo!!! 🎆🎆🎆")