# -*- mode: python -*-
a = Analysis(['Minok.py'],
             pathex=['C:\\Users\\Minok\\Desktop\\pthon\\exe\\pyinstaller'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'Minok.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='my.ico')
app = BUNDLE(exe,
             name=os.path.join('dist', 'Minok.exe.app'))
