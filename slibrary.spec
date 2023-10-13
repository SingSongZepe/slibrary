# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['event/close_event.py', 'event/drag/mouse_move_event.py', 'event/drag/mouse_press_event.py', 'event/drag/mouse_release_event.py', 'main.py', 'object/book.py', 'object/book_item.py', 'object/download.py', 'object/history_item.py', 'object/history_search.py', 'object/search.py', 'object/slibrary.py', 'object/time.py', 'pyspec.py', 'signal_/signal_append_book.py', 'signal_/signal_append_history.py', 'signal_/signal_append_recommend.py', 'slibrary.py', 'slibrary_functions/append_book.py', 'slibrary_functions/append_books.py', 'slibrary_functions/append_history.py', 'slibrary_functions/append_recommend.py', 'slibrary_functions/append_recommends.py', 'slibrary_functions/function/download.py', 'slibrary_functions/function/recommend.py', 'slibrary_functions/function/search.py', 'slibrary_functions/hover.py', 'slibrary_functions/launcher/append_history_launcher.py', 'slibrary_functions/launcher/download_launcher.py', 'slibrary_functions/launcher/recommend_launcher.py', 'slibrary_functions/launcher/search_launcher.py', 'slibrary_functions/other_init.py', 'slibrary_functions/toggle.py', 'slibrary_functions/toggle_history.py', 'slibrary_ui.py', 'sszp/SLineEdit.py', 'sszp/sszpThread.py', 'utils/common/circle.py', 'utils/common/collect_book_info.py', 'utils/common/dry.py', 'utils/common/encode_sha1.py', 'utils/common/gl_remove_wgt.py', 'utils/common/load_pic.py', 'utils/common/log_common.py', 'utils/common/num_length_info.py', 'utils/common/open_url.py', 'utils/common/retitle.py', 'utils/slibrary/clear_history.py', 'utils/slibrary/logger.py', 'utils/slibrary/read.py', 'utils/slibrary/save.py', 'utils/slibrary/setup.py', 'value/color.py', 'value/font.py', 'value/pic_path.py', 'value/strings.py', 'value/value.py', 'windows/wgt_book.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='slibrary',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='res/img/reSSZp.png',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='slibrary',
)
