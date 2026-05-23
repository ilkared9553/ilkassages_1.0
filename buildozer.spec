[app]
title = Ilkassages
package.name = ilkassages
package.domain = org.ilya

# Путь к исходникам
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

# Версия приложения
version = 0.1

# Библиотеки, которые нужны для работы (requirements)
requirements = python3,kivy,kivymd,pillow,sqlite3

# Ориентация экрана
orientation = portrait

# Разрешения для Android (если мессенджеру нужен интернет)
android.permissions = INTERNET

# (Костыль для стабильной сборки KivyMD)
osx.kivy_version = 2.1.0
