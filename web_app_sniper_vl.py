import pyautogui
import pyperclip
import time
import pandas as pd
import csv
from datetime import datetime
from pathlib import Path

def save_prices_to_csv(players_data, players, filename="player_prices.csv"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = Path(filename).exists()
    
    with open(filename, "a", newline='') as f:
        writer = csv.writer(f)
        # Write headers if new file
        if not file_exists:
            headers = ["Timestamp"] + players
            writer.writerow(headers)
        # Write data row
        writer.writerow([timestamp] + players_data)

def futbin_pricing(name):
    time.sleep(1)
    pyautogui.moveTo(500, 130) 
    pyautogui.leftClick()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    pyautogui.typewrite(name)
    time.sleep(3)
    pyautogui.moveTo(500, 170) 
    pyautogui.leftClick()
    time.sleep(3)
    pyautogui.moveTo(950, 450) 
    pyautogui.doubleClick()
    pyautogui.hotkey("ctrl", "c")

    price_text = pyperclip.paste()
    try:
        price = int(price_text.replace(",", "")) * 0.95
        return price
    except:
        return 0

def get_price_from_excel(name):
    file_path = 'player_prices.csv'  # Changed to CSV since we're saving in CSV
    
    try:
        # Read CSV file
        df = pd.read_csv(file_path)
        
        # Convert Timestamp column to datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        
        # Get today's date
        today = datetime.now().date()
        
        # Filter for today's data
        today_df = df[df['Timestamp'].dt.date == today]
        
        if name in today_df.columns:
            # Get minimum price for the player today
            min_price = today_df[name].min()
            print(f"Found minimum price for {name}: {min_price}")  # Debug print
            return int(min_price) if not pd.isna(min_price) else None
            
    except FileNotFoundError:
        print(f"CSV file not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return None

def auto_snipe_specjalna(name):
    # Pobierz cenę zawodnika z pliku Excel
    price = get_price_from_excel(name)
    if price is None:
        # Jeśli cena nie istnieje w Excelu, pobierz ją za pomocą funkcji futbin_pricing i zapisz
        price = futbin_pricing(name)

    # Reszta automatyzacji za pomocą pyautogui
    time.sleep(1)
    pyautogui.moveTo(800, 360)
    pyautogui.leftClick()
    pyautogui.typewrite(name)
    time.sleep(2)
    pyautogui.moveTo(800, 440)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(800, 440)
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(800, 650)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(1400, 850)
    pyautogui.leftClick()
    pyautogui.typewrite(str(price))

    # Petla
    i = 0
    while i <= 5:
        time.sleep(0.5)
        pyautogui.moveTo(1000, 740)  # zwiększenie ceny min licytacji 
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.moveTo(1400, 950)  # search
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(1500, 750)  # kliknięcie na kup teraz
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.moveTo(980, 560)  # zaakceptowanie kup teraz
        pyautogui.leftClick() 
        time.sleep(0.5)
        pyautogui.moveTo(170, 150)  # powrót
        pyautogui.leftClick() 
        i += 1

if __name__ == "__main__":
    players = ["Paulo Futre", "Wesley Snejider", "Fikayo Tomori", "Alejandro Garnacho", "Emmanuel Petit"]
    
    while True:
        time.sleep(1)
        pyautogui.moveTo(450, 30)
        pyautogui.leftClick()
        
        prices = []
        for player in players:
            price = futbin_pricing(player)
            prices.append(price)
        
        save_prices_to_csv(prices, players)

        time.sleep(1)
        pyautogui.moveTo(200, 30) 
        pyautogui.leftClick()
        time.sleep(4)
        pyautogui.moveTo(1400, 600) 
        pyautogui.leftClick()
        time.sleep(4)
        pyautogui.moveTo(100, 400)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(800, 400) 
        pyautogui.leftClick()
        temp=0
        while temp < 5:
            auto_snipe_specjalna("Paulo Futre")
            auto_snipe_specjalna("Wesley Snejider")
            auto_snipe_specjalna("Fikayo Tomori")
            auto_snipe_specjalna("Alejandro Garnacho")
            auto_snipe_specjalna("Emmanuel Petit")
            temp +=1

        pyautogui.moveTo(140, 60)
        pyautogui.leftClick()
        time.sleep(15)