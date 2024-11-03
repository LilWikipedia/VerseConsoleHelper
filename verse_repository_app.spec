
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['verse_repository_app.py'],
             pathex=[],
             binaries=[],
             datas=[
                 ('verse', 'verse'),
                 ('verse/docs', 'verse/docs'),
                 ('verse/snippets', 'verse/snippets'),
                 ('verse/snippets/Game', 'verse/snippets/Game'),
                 ('verse/snippets/Helper Scripts', 'verse/snippets/Helper Scripts'),
                 ('verse/snippets/Object', 'verse/snippets/Object'),
                 ('verse/snippets/Player', 'verse/snippets/Player'),
                 ('verse/snippets/UI', 'verse/snippets/UI'),
                 ('verse/snippets/Game/Sets', 'verse/snippets/Game/Sets'),
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='VerseConsoleHelper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='VerseConsoleHelper')