import pyautogui
import pyperclip
import time
import pandas as pd

def futbin_pricing(name):
    time.sleep(1)
    pyautogui.moveTo(300, 20)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(500, 100) 
    pyautogui.leftClick()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    pyautogui.typewrite(name)
    time.sleep(3)
    pyautogui.moveTo(500, 150) 
    pyautogui.leftClick()
    time.sleep(3)
    pyautogui.moveTo(950, 450) 
    pyautogui.doubleClick()
    pyautogui.hotkey("ctrl", "c")

    # Pobranie ceny ze schowka
    price_text = pyperclip.paste()
    price = int(price_text.replace(",", "")) * 0.9  # Usunięcie przecinków i pomnożenie
    print("Cena karty:", price)

    # Zapisanie wyniku do pliku Excel
    file_path = 'web_sniper\\futbin_prices.xlsx'
    
    try:
        # Wczytaj istniejący plik Excel lub stwórz nowy DataFrame, jeśli plik nie istnieje
        df = pd.read_excel(file_path, index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame()

    # Zaktualizuj cenę dla danego zawodnika, wpisując ją w pierwszy wiersz odpowiedniej kolumny
    df.loc[0, name] = price

    # Zapisz dane do pliku Excel
    df.to_excel(file_path)

    return price


def get_price_from_excel(name):
    file_path = 'web_sniper\\futbin_prices.xlsx'
    
    try:
        # Wczytaj plik Excel i sprawdź, czy zawodnik istnieje w danych
        df = pd.read_excel(file_path, index_col=0)
        if name in df.columns:
            return df[name][0]  # Zwraca cenę z pierwszego wiersza dla kolumny o nazwie zawodnika
    except FileNotFoundError:
        print("Plik Excel nie istnieje.")
    
    return None  # Zwróć None, jeśli cena nie została znaleziona

def auto_snipe_specjalna(name):
    # Pobierz cenę zawodnika z pliku Excel
    price = get_price_from_excel(name)
    if price is None:
        # Jeśli cena nie istnieje w Excelu, pobierz ją za pomocą funkcji futbin_pricing i zapisz
        price = futbin_pricing(name)

    # Reszta automatyzacji za pomocą pyautogui
    time.sleep(1)
    pyautogui.moveTo(800, 360) #pole tekstowe
    pyautogui.leftClick()
    pyautogui.typewrite(name)
    time.sleep(2)
    pyautogui.moveTo(800, 440) #klikniecie na nazwisko zawodnika
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(800, 440) #klikniecie na jakosc karty
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(800, 600) #wybranie specjalnej
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(120, 10) 
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(1400, 850)
    pyautogui.leftClick()
    pyautogui.typewrite(str(price))

    # Petla
    i = 0
    while i <= 1:
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
    while True:
        futbin_pricing("Federico Dimarco")
        futbin_pricing("Christian Pulisic")
        futbin_pricing("Grace Geyoro")
        futbin_pricing("Marcos Llorente")
        futbin_pricing("Claudia Pina")
        futbin_pricing("Alessandro Bastoni")


        time.sleep(1)
        pyautogui.moveTo(120, 10) 
        pyautogui.leftClick()
        time.sleep(4)
        pyautogui.moveTo(1400, 600) 
        pyautogui.leftClick()
        time.sleep(4)
        pyautogui.moveTo(100, 400)
        pyautogui.leftClick()
        time.sleep(4)
        pyautogui.moveTo(800, 400) 
        pyautogui.leftClick()
        temp=0
        while temp < 10:
            auto_snipe_specjalna("Federico Dimarco")
            auto_snipe_specjalna("Christian Pulisic")
            auto_snipe_specjalna("Grace Geyoro")
            auto_snipe_specjalna("Marcos Llorente")
            auto_snipe_specjalna("Claudia Pina")
            auto_snipe_specjalna("Alessandro Bastoni")
            temp +=1

        pyautogui.moveTo(140, 50)
        pyautogui.leftClick()
        time.sleep(10)