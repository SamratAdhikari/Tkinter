# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/SAMRAT FILE/Documents/Programing/Programming/Python/Practice and Programs/Tkinter Module/Digital Clock/Digital Clock.py'],
             pathex=['D:\\SAMRAT FILE\\Documents\\Programing\\Programming\\Python\\Practice and Programs\\Tkinter Module\\Digital Clock'],
             binaries=[],
             datas=[('D:/SAMRAT FILE/Documents/Programing/Programming/Python/Practice and Programs/Tkinter Module/Digital Clock/icon.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Digital Clock',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\SAMRAT FILE\\Documents\\Programing\\Programming\\Python\\Practice and Programs\\Tkinter Module\\Digital Clock\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Digital Clock')
