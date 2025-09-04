[app]
# App ka naam
title = AgeProcessor

# Package ka naam (sirf chhoti letters allowed)
package.name = ageprocessor

# App ka domain (random de sakte ho)
package.domain = org.amaan

# Jaha se code load hoga
source.dir = .

# Ye extensions include honge
source.include_exts = py,png,jpg,kv,atlas

# App ka version
version = 1.0

# Libraries jo chahiye
requirements = python3,kivy,kivymd

# App sirf portrait mode me chale
orientation = portrait

# Android API versions (ye change mat karna)
android.api = 35
android.minapi = 24

# Android architectures
android.archs = arm64-v8a, armeabi-v7a

# Icon (optional)
icon.filename = %(source.dir)s/icon.png