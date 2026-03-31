from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import threading
import speech_recognition as sr
import requests
import time
import os

# --- НАСТРОЙКИ ---
TOKEN = "8243802558:AAE13_ZisQLxRkyqlCoYYIAkNY7XdEsrMag"
CHAT_ID = "-1003173600734" 
TRIGGER_PHRASE = "игра"

class SecurityApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.status_label = Label(text="Система готова", font_size='20sp')
        self.start_btn = Button(text="ЗАПУСТИТЬ ЗАЩИТУ", background_color=(1, 0, 0, 1))
        self.start_btn.bind(on_press=self.start_system)
        
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.start_btn)
        return self.layout

    def start_system(self, instance):
        self.status_label.text = "🔴 МОНИТОРИНГ АКТИВЕН"
        self.start_btn.disabled = True
        threading.Thread(target=self.run_logic, daemon=True).start()

    def send_sos(self, text, filename):
        # Координаты (заглушка)
        lat, lon = "50.4501", "30.5234" 
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        caption = f"🚨 ТРЕВОГА!\nСлово: {text}\nЛокация: {maps_link}"
        
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
            with open(filename, "rb") as f:
                requests.post(url, data={"chat_id": CHAT_ID, "caption": caption}, files={"document": f})
        except:
            pass

    def run_logic(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
        
        def callback(recognizer, audio):
            try:
                text = recognizer.recognize_google(audio, language="ru-RU").lower()
                # Сохраняем временный файл
                fname = f"rec_{int(time.time())}.wav"
                with open(fname, "wb") as f:
                    f.write(audio.get_wav_data())
                
                if TRIGGER_PHRASE in text:
                    self.send_sos(text, fname)
            except:
                pass

        r.listen_in_background(m, callback, phrase_time_limit=15)

if __name__ == "__main__":
    SecurityApp().run()