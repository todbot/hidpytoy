# -*- mode: python ; coding: utf-8 -*-
import sys

if sys.platform == 'darwin':
    icon = 'src/main/icons/Icon.icns'
elif sys.platform == 'win32':
    icon = 'src/main/icons/Icon.ico'
else:
    icon = None

a = Analysis(
    ['src/main/python/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HIDPyToy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    icon=icon,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='HIDPyToy',
)

app = BUNDLE(
    coll,
    name='HIDPyToy.app',
    icon=icon,
    bundle_identifier='com.todbot.hidpytoy',
    version='0.1.0',
    info_plist={
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '11.0',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'NSHumanReadableCopyright': 'Copyright 2024 todbot',
    },
)
