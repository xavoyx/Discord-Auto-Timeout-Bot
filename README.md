# Discord Auto Timeout Bot

Ein Discord-Bot, der Benutzer automatisch in Timeout setzt, wenn sie beleidigende Wörter verwenden. Zusätzlich wird eine Embed-Nachricht im Chat gepostet, um die Maßnahme zu dokumentieren.

## 🚀 Funktionen
- Erkennt vordefinierte beleidigende Wörter in Nachrichten.
- Setzt den Verfasser automatisch für eine bestimmte Zeit in Timeout.
- Sendet eine Embed-Nachricht in den Chat mit Details zur Strafe.

## 🛠️ Installation
### 1. Voraussetzungen
- [Python 3.8+](https://www.python.org/downloads/)
- [discord.py](https://github.com/Rapptz/discord.py) Bibliothek

### 2. Bot-Token erstellen
1. Gehe zu [Discord Developer Portal](https://discord.com/developers/applications).
2. Erstelle eine neue Anwendung.
3. Navigiere zu "Bot" und erstelle einen Bot.
4. Kopiere das Token und setze es in `bot.py` ein.

### 3. Benötigte Pakete installieren
```sh
pip install discord.py
```

## ⚙️ Konfiguration
Bearbeite die Datei `bot.py`, um eigene beleidigende Wörter in `BAD_WORDS` hinzuzufügen:
```python
BAD_WORDS = ["schimpfwort1", "schimpfwort2", "schimpfwort3"]
```
Du kannst auch die Timeout-Dauer anpassen:
```python
TIMEOUT_DURATION = 300  # Sekunden (5 Minuten)
```

## ▶️ Starten des Bots
```sh
python bot.py
```

## 📜 Lizenz
Dieses Projekt steht unter der MIT-Lizenz.
