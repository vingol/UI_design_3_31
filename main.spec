# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

SETUP_DIR = 'C:\\Users\\Camille\\Desktop\\UI_design_test_2\\'

a = Analysis(['main.py'],
             pathex=['C:\\Program Files\\Python37\\Lib\\site-packages\\matlab', 'C:\\Users\\Camille\\Desktop\\UI_design_test_2'],
             binaries=[],
             datas=[(SETUP_DIR+'extra_data','extra_data'),(SETUP_DIR+'images','images'),(SETUP_DIR+'Power','Power'),(SETUP_DIR+'NWP','NWP')],
             hiddenimports=['mlarray'],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
