[app]
# Название приложения на экране телефона
title = SafeGuard Ukraine
# Внутреннее имя (маленькими буквами, без пробелов)
package.name = safeguardua
# Твой уникальный домен
package.domain = org.security.ua

# Где лежит код (точка означает текущую папку)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# СПИСОК БИБЛИОТЕК (Самое важное!)
# Мы используем kivy для интерфейса, requests для Telegram, plyer для GPS
requirements = python3,kivy==2.2.1,requests,urllib3,charset-normalizer,idna,certifi,plyer

orientation = portrait

# РАЗРЕШЕНИЯ (Без них Android заблокирует микрофон и интернет)
android.permissions = INTERNET, RECORD_AUDIO, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, FOREGROUND_SERVICE

# Настройки для современных Android 12-14
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Архитектуры процессоров (поддерживаем все современные телефоны)
android.archs = armeabi-v7a, arm64-v8a

# Позволяет приложению работать в фоне
android.foreground_service = true

[buildozer]
log_level = 2
warn_on_root = 1