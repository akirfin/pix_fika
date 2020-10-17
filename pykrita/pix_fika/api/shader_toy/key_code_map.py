"""

Happy world of n+ standards ...

"""

from Qt.QtCore import Qt


key_code_map = {
        Qt.Key_Any: None,
        Qt.Key_Exclam: 49,
        Qt.Key_QuoteDbl: 50,
        Qt.Key_NumberSign: 51,
        Qt.Key_Dollar: 52,
        Qt.Key_Percent: 53,
        Qt.Key_Ampersand: 54,
        Qt.Key_Apostrophe: None,
        Qt.Key_ParenLeft: 56,
        Qt.Key_ParenRight: 57,
        Qt.Key_Asterisk: None,
        Qt.Key_Plus: None,
        Qt.Key_Comma: 188,
        Qt.Key_Minus: None,
        Qt.Key_Period: 190,
        Qt.Key_Slash: None,
        Qt.Key_0: 48,
        Qt.Key_1: 49,
        Qt.Key_2: 50,
        Qt.Key_3: 51,
        Qt.Key_4: 52,
        Qt.Key_5: 53,
        Qt.Key_6: 54,
        Qt.Key_7: 55,
        Qt.Key_8: 56,
        Qt.Key_9: 57,
        Qt.Key_Colon: 190,
        Qt.Key_Semicolon: 188,
        Qt.Key_Less: None,
        Qt.Key_Equal: None,
        Qt.Key_Greater: None,
        Qt.Key_Question: None,
        Qt.Key_At: 64,
        Qt.Key_A: 65,
        Qt.Key_B: 66,
        Qt.Key_C: 67,
        Qt.Key_D: 68,
        Qt.Key_E: 69,
        Qt.Key_F: 70,
        Qt.Key_G: 71,
        Qt.Key_H: 72,
        Qt.Key_I: 73,
        Qt.Key_J: 74,
        Qt.Key_K: 75,
        Qt.Key_L: 76,
        Qt.Key_M: 77,
        Qt.Key_N: 78,
        Qt.Key_O: 79,
        Qt.Key_P: 80,
        Qt.Key_Q: 81,
        Qt.Key_R: 82,
        Qt.Key_S: 83,
        Qt.Key_T: 84,
        Qt.Key_U: 85,
        Qt.Key_V: 86,
        Qt.Key_W: 87,
        Qt.Key_X: 88,
        Qt.Key_Y: 89,
        Qt.Key_Z: 90,
        Qt.Key_BracketLeft: None,
        Qt.Key_Backslash: 220,
        Qt.Key_BracketRight: None,
        Qt.Key_AsciiCircum: None,
        Qt.Key_Underscore: None,
        Qt.Key_QuoteLeft: None,
        Qt.Key_BraceLeft: None,
        Qt.Key_Bar: None,
        Qt.Key_BraceRight: None,
        Qt.Key_AsciiTilde: None,
        Qt.Key_nobreakspace: None,
        Qt.Key_exclamdown: None,
        Qt.Key_cent: None,
        Qt.Key_sterling: None,
        Qt.Key_currency: None,
        Qt.Key_yen: None,
        Qt.Key_brokenbar: None,
        Qt.Key_section: None,
        Qt.Key_diaeresis: None,
        Qt.Key_copyright: None,
        Qt.Key_ordfeminine: None,
        Qt.Key_guillemotleft: None,
        Qt.Key_notsign: None,
        Qt.Key_hyphen: None,
        Qt.Key_registered: None,
        Qt.Key_macron: None,
        Qt.Key_degree: None,
        Qt.Key_plusminus: None,
        Qt.Key_twosuperior: None,
        Qt.Key_threesuperior: None,
        Qt.Key_acute: None,
        Qt.Key_mu: None,
        Qt.Key_paragraph: None,
        Qt.Key_periodcentered: None,
        Qt.Key_cedilla: None,
        Qt.Key_onesuperior: None,
        Qt.Key_masculine: None,
        Qt.Key_guillemotright: None,
        Qt.Key_onequarter: None,
        Qt.Key_onehalf: None,
        Qt.Key_threequarters: None,
        Qt.Key_questiondown: None,
        Qt.Key_Agrave: None,
        Qt.Key_Aacute: None,
        Qt.Key_Acircumflex: None,
        Qt.Key_Atilde: None,
        Qt.Key_Adiaeresis: None,
        Qt.Key_Aring: None,
        Qt.Key_AE: None,
        Qt.Key_Ccedilla: None,
        Qt.Key_Egrave: None,
        Qt.Key_Eacute: None,
        Qt.Key_Ecircumflex: None,
        Qt.Key_Ediaeresis: None,
        Qt.Key_Igrave: None,
        Qt.Key_Iacute: None,
        Qt.Key_Icircumflex: None,
        Qt.Key_Idiaeresis: None,
        Qt.Key_ETH: None,
        Qt.Key_Ntilde: None,
        Qt.Key_Ograve: None,
        Qt.Key_Oacute: None,
        Qt.Key_Ocircumflex: None,
        Qt.Key_Otilde: None,
        Qt.Key_Odiaeresis: None,
        Qt.Key_multiply: None,
        Qt.Key_Ooblique: None,
        Qt.Key_Ugrave: None,
        Qt.Key_Uacute: None,
        Qt.Key_Ucircumflex: None,
        Qt.Key_Udiaeresis: None,
        Qt.Key_Yacute: None,
        Qt.Key_THORN: None,
        Qt.Key_ssharp: None,
        Qt.Key_division: None,
        Qt.Key_ydiaeresis: None,
        Qt.Key_Escape: 27,
        Qt.Key_Tab: 9,
        Qt.Key_Backtab: None,
        Qt.Key_Backspace: 8,
        Qt.Key_Return: None,
        Qt.Key_Enter: 13,
        Qt.Key_Insert: 45,
        Qt.Key_Delete: 46,
        Qt.Key_Pause: 19,
        Qt.Key_Print: 42,
        Qt.Key_SysReq: None,
        Qt.Key_Clear: 12,
        Qt.Key_Home: 172,
        Qt.Key_End: 35,
        Qt.Key_Left: 37,
        Qt.Key_Up: 38,
        Qt.Key_Right: 39,
        Qt.Key_Down: 40,
        Qt.Key_PageUp: 33,
        Qt.Key_PageDown: 34,
        Qt.Key_Shift: 16,
        Qt.Key_Control: 17,
        Qt.Key_Meta: 91,
        Qt.Key_Alt: 18,
        Qt.Key_CapsLock: 20,
        Qt.Key_NumLock: 144,
        Qt.Key_ScrollLock: 145,
        Qt.Key_F1: 112,
        Qt.Key_F2: 113,
        Qt.Key_F3: 114,
        Qt.Key_F4: 115,
        Qt.Key_F5: 116,
        Qt.Key_F6: 117,
        Qt.Key_F7: 118,
        Qt.Key_F8: 119,
        Qt.Key_F9: 120,
        Qt.Key_F10: 121,
        Qt.Key_F11: 122,
        Qt.Key_F12: 123,
        Qt.Key_F13: 124,
        Qt.Key_F14: 125,
        Qt.Key_F15: 126,
        Qt.Key_F16: 127,
        Qt.Key_F17: 128,
        Qt.Key_F18: 129,
        Qt.Key_F19: 130,
        Qt.Key_F20: 131,
        Qt.Key_F21: 132,
        Qt.Key_F22: 133,
        Qt.Key_F23: 134,
        Qt.Key_F24: 135,
        Qt.Key_F25: None,
        Qt.Key_F26: None,
        Qt.Key_F27: None,
        Qt.Key_F28: None,
        Qt.Key_F29: None,
        Qt.Key_F30: None,
        Qt.Key_F31: None,
        Qt.Key_F32: None,
        Qt.Key_F33: None,
        Qt.Key_F34: None,
        Qt.Key_F35: None,
        Qt.Key_Super_L: None,
        Qt.Key_Super_R: None,
        Qt.Key_Menu: None,
        Qt.Key_Hyper_L: None,
        Qt.Key_Hyper_R: None,
        Qt.Key_Help: 47,
        Qt.Key_Direction_L: None,
        Qt.Key_Direction_R: None,
        Qt.Key_Back: None,
        Qt.Key_Forward: None,
        Qt.Key_Stop: 178,
        Qt.Key_Refresh: 168,
        Qt.Key_VolumeDown: None,
        Qt.Key_VolumeMute: None,
        Qt.Key_VolumeUp: None,
        Qt.Key_BassBoost: None,
        Qt.Key_BassUp: None,
        Qt.Key_BassDown: None,
        Qt.Key_TrebleUp: None,
        Qt.Key_TrebleDown: None,
        Qt.Key_MediaPlay: None,
        Qt.Key_MediaStop: None,
        Qt.Key_MediaPrevious: None,
        Qt.Key_MediaNext: None,
        Qt.Key_MediaRecord: None,
        Qt.Key_MediaPause: None,
        Qt.Key_MediaTogglePlayPause: None,
        Qt.Key_HomePage: None,
        Qt.Key_Favorites: None,
        Qt.Key_Search: None,
        Qt.Key_Standby: None,
        Qt.Key_OpenUrl: None,
        Qt.Key_LaunchMail: None,
        Qt.Key_LaunchMedia: None,
        Qt.Key_Launch0: None,
        Qt.Key_Launch1: None,
        Qt.Key_Launch2: None,
        Qt.Key_Launch3: None,
        Qt.Key_Launch4: None,
        Qt.Key_Launch5: None,
        Qt.Key_Launch6: None,
        Qt.Key_Launch7: None,
        Qt.Key_Launch8: None,
        Qt.Key_Launch9: None,
        Qt.Key_LaunchA: None,
        Qt.Key_LaunchB: None,
        Qt.Key_LaunchC: None,
        Qt.Key_LaunchD: None,
        Qt.Key_LaunchE: None,
        Qt.Key_LaunchF: None,
        Qt.Key_MonBrightnessUp: None,
        Qt.Key_MonBrightnessDown: None,
        Qt.Key_KeyboardLightOnOff: None,
        Qt.Key_KeyboardBrightnessUp: None,
        Qt.Key_KeyboardBrightnessDown: None,
        Qt.Key_PowerOff: None,
        Qt.Key_WakeUp: None,
        Qt.Key_Eject: None,
        Qt.Key_ScreenSaver: None,
        Qt.Key_WWW: None,
        Qt.Key_Memo: None,
        Qt.Key_LightBulb: None,
        Qt.Key_Shop: None,
        Qt.Key_History: None,
        Qt.Key_AddFavorite: None,
        Qt.Key_HotLinks: None,
        Qt.Key_BrightnessAdjust: None,
        Qt.Key_Finance: None,
        Qt.Key_Community: None,
        Qt.Key_AudioRewind: None,
        Qt.Key_BackForward: None,
        Qt.Key_ApplicationLeft: None,
        Qt.Key_ApplicationRight: None,
        Qt.Key_Book: None,
        Qt.Key_CD: None,
        Qt.Key_Calculator: None,
        Qt.Key_ToDoList: None,
        Qt.Key_ClearGrab: None,
        Qt.Key_Close: None,
        Qt.Key_Copy: None,
        Qt.Key_Cut: None,
        Qt.Key_Display: None,
        Qt.Key_DOS: None,
        Qt.Key_Documents: None,
        Qt.Key_Excel: None,
        Qt.Key_Explorer: None,
        Qt.Key_Game: None,
        Qt.Key_Go: None,
        Qt.Key_iTouch: None,
        Qt.Key_LogOff: None,
        Qt.Key_Market: None,
        Qt.Key_Meeting: None,
        Qt.Key_MenuKB: None,
        Qt.Key_MenuPB: None,
        Qt.Key_MySites: None,
        Qt.Key_News: None,
        Qt.Key_OfficeHome: None,
        Qt.Key_Option: None,
        Qt.Key_Paste: None,
        Qt.Key_Phone: None,
        Qt.Key_Calendar: None,
        Qt.Key_Reply: None,
        Qt.Key_Reload: None,
        Qt.Key_RotateWindows: None,
        Qt.Key_RotationPB: None,
        Qt.Key_RotationKB: None,
        Qt.Key_Save: None,
        Qt.Key_Send: None,
        Qt.Key_Spell: None,
        Qt.Key_SplitScreen: None,
        Qt.Key_Support: None,
        Qt.Key_TaskPane: None,
        Qt.Key_Terminal: None,
        Qt.Key_Tools: None,
        Qt.Key_Travel: None,
        Qt.Key_Video: None,
        Qt.Key_Word: None,
        Qt.Key_Xfer: None,
        Qt.Key_ZoomIn: None,
        Qt.Key_ZoomOut: None,
        Qt.Key_Away: None,
        Qt.Key_Messenger: None,
        Qt.Key_WebCam: None,
        Qt.Key_MailForward: None,
        Qt.Key_Pictures: None,
        Qt.Key_Music: None,
        Qt.Key_Battery: None,
        Qt.Key_Bluetooth: None,
        Qt.Key_WLAN: None,
        Qt.Key_UWB: None,
        Qt.Key_AudioForward: None,
        Qt.Key_AudioRepeat: None,
        Qt.Key_AudioRandomPlay: None,
        Qt.Key_Subtitle: None,
        Qt.Key_AudioCycleTrack: None,
        Qt.Key_Time: None,
        Qt.Key_Hibernate: None,
        Qt.Key_View: None,
        Qt.Key_TopMenu: None,
        Qt.Key_PowerDown: None,
        Qt.Key_Suspend: None,
        Qt.Key_ContrastAdjust: None,
        Qt.Key_LaunchG: None,
        Qt.Key_LaunchH: None,
        Qt.Key_TouchpadToggle: None,
        Qt.Key_TouchpadOn: None,
        Qt.Key_TouchpadOff: None,
        Qt.Key_MicMute: None,
        Qt.Key_Red: None,
        Qt.Key_Green: None,
        Qt.Key_Yellow: None,
        Qt.Key_Blue: None,
        Qt.Key_ChannelUp: None,
        Qt.Key_ChannelDown: None,
        Qt.Key_Guide: None,
        Qt.Key_Info: None,
        Qt.Key_Settings: None,
        Qt.Key_MicVolumeUp: None,
        Qt.Key_MicVolumeDown: None,
        Qt.Key_New: None,
        Qt.Key_Open: None,
        Qt.Key_Find: None,
        Qt.Key_Undo: None,
        Qt.Key_Redo: None,
        Qt.Key_AltGr: 225,
        Qt.Key_Multi_key: None,
        Qt.Key_Kanji: 244,
        Qt.Key_Muhenkan: None,
        Qt.Key_Henkan: None,
        Qt.Key_Romaji: None,
        Qt.Key_Hiragana: None,
        Qt.Key_Katakana: None,
        Qt.Key_Hiragana_Katakana: None,
        Qt.Key_Zenkaku: None,
        Qt.Key_Hankaku: None,
        Qt.Key_Zenkaku_Hankaku: None,
        Qt.Key_Touroku: None,
        Qt.Key_Massyo: None,
        Qt.Key_Kana_Lock: None,
        Qt.Key_Kana_Shift: None,
        Qt.Key_Eisu_Shift: None,
        Qt.Key_Eisu_toggle: None,
        Qt.Key_Hangul: 21,
        Qt.Key_Hangul_Start: None,
        Qt.Key_Hangul_End: None,
        Qt.Key_Hangul_Hanja: None,
        Qt.Key_Hangul_Jamo: None,
        Qt.Key_Hangul_Romaja: None,
        Qt.Key_Codeinput: None,
        Qt.Key_Hangul_Jeonja: None,
        Qt.Key_Hangul_Banja: None,
        Qt.Key_Hangul_PreHanja: None,
        Qt.Key_Hangul_PostHanja: None,
        Qt.Key_SingleCandidate: None,
        Qt.Key_MultipleCandidate: None,
        Qt.Key_PreviousCandidate: None,
        Qt.Key_Hangul_Special: None,
        Qt.Key_Mode_switch: None,
        Qt.Key_Dead_Grave: None,
        Qt.Key_Dead_Acute: None,
        Qt.Key_Dead_Circumflex: None,
        Qt.Key_Dead_Tilde: None,
        Qt.Key_Dead_Macron: None,
        Qt.Key_Dead_Breve: None,
        Qt.Key_Dead_Abovedot: None,
        Qt.Key_Dead_Diaeresis: None,
        Qt.Key_Dead_Abovering: None,
        Qt.Key_Dead_Doubleacute: None,
        Qt.Key_Dead_Caron: None,
        Qt.Key_Dead_Cedilla: None,
        Qt.Key_Dead_Ogonek: None,
        Qt.Key_Dead_Iota: None,
        Qt.Key_Dead_Voiced_Sound: None,
        Qt.Key_Dead_Semivoiced_Sound: None,
        Qt.Key_Dead_Belowdot: None,
        Qt.Key_Dead_Hook: None,
        Qt.Key_Dead_Horn: None,
        Qt.Key_Dead_Stroke: None,
        Qt.Key_Dead_Abovecomma: None,
        Qt.Key_Dead_Abovereversedcomma: None,
        Qt.Key_Dead_Doublegrave: None,
        Qt.Key_Dead_Belowring: None,
        Qt.Key_Dead_Belowmacron: None,
        Qt.Key_Dead_Belowcircumflex: None,
        Qt.Key_Dead_Belowtilde: None,
        Qt.Key_Dead_Belowbreve: None,
        Qt.Key_Dead_Belowdiaeresis: None,
        Qt.Key_Dead_Invertedbreve: None,
        Qt.Key_Dead_Belowcomma: None,
        Qt.Key_Dead_Currency: None,
        Qt.Key_Dead_a: None,
        Qt.Key_Dead_A: None,
        Qt.Key_Dead_e: None,
        Qt.Key_Dead_E: None,
        Qt.Key_Dead_i: None,
        Qt.Key_Dead_I: None,
        Qt.Key_Dead_o: None,
        Qt.Key_Dead_O: None,
        Qt.Key_Dead_u: None,
        Qt.Key_Dead_U: None,
        Qt.Key_Dead_Small_Schwa: None,
        Qt.Key_Dead_Capital_Schwa: None,
        Qt.Key_Dead_Greek: None,
        Qt.Key_Dead_Lowline: None,
        Qt.Key_Dead_Aboveverticalline: None,
        Qt.Key_Dead_Belowverticalline: None,
        Qt.Key_Dead_Longsolidusoverlay: None,
        Qt.Key_MediaLast: None,
        Qt.Key_Select: 41,
        Qt.Key_Yes: None,
        Qt.Key_No: None,
        Qt.Key_Cancel: None,
        Qt.Key_Printer: None,
        Qt.Key_Execute: 43,
        Qt.Key_Sleep: 95,
        Qt.Key_Play: 179,
        Qt.Key_Zoom: None,
        Qt.Key_Exit: None,
        Qt.Key_Context1: None,
        Qt.Key_Context2: None,
        Qt.Key_Context3: None,
        Qt.Key_Context4: None,
        Qt.Key_Call: None,
        Qt.Key_Hangup: None,
        Qt.Key_Flip: None,
        Qt.Key_ToggleCallHangup: None,
        Qt.Key_VoiceDial: None,
        Qt.Key_LastNumberRedial: None,
        Qt.Key_Camera: None,
        Qt.Key_CameraFocus: None,
        Qt.Key_unknown: None}


class VirtualKeyCodes(IntEnum):
    VK_LBUTTON      = 0x01
    VK_RBUTTON      = 0x02
    VK_CANCEL       = 0x03
    VK_MBUTTON      = 0x04  # NOT contiguous with L & RBUTTON

    VK_XBUTTON1     = 0x05  # NOT contiguous with L & RBUTTON
    VK_XBUTTON2     = 0x06  # NOT contiguous with L & RBUTTON

    # 0x07 : reserved

    VK_BACK         = 0x08
    VK_TAB          = 0x09

    # 0x0A - 0x0B : reserved

    VK_CLEAR        = 0x0C
    VK_RETURN       = 0x0D

    # 0x0E - 0x0F : unassigned

    VK_SHIFT        = 0x10
    VK_CONTROL      = 0x11
    VK_MENU         = 0x12
    VK_PAUSE        = 0x13
    VK_CAPITAL      = 0x14

    VK_KANA         = 0x15
    VK_HANGEUL      = 0x15  # old name - should be here for compatibility
    VK_HANGUL       = 0x15

    # 0x16 : unassigned

    VK_JUNJA        = 0x17
    VK_FINAL        = 0x18
    VK_HANJA        = 0x19
    VK_KANJI        = 0x19

    # 0x1A : unassigned

    VK_ESCAPE       = 0x1B

    VK_CONVERT      = 0x1C
    VK_NONCONVERT   = 0x1D
    VK_ACCEPT       = 0x1E
    VK_MODECHANGE   = 0x1F

    VK_SPACE        = 0x20
    VK_PRIOR        = 0x21
    VK_NEXT         = 0x22
    VK_END          = 0x23
    VK_HOME         = 0x24
    VK_LEFT         = 0x25
    VK_UP           = 0x26
    VK_RIGHT        = 0x27
    VK_DOWN         = 0x28
    VK_SELECT       = 0x29
    VK_PRINT        = 0x2A
    VK_EXECUTE      = 0x2B
    VK_SNAPSHOT     = 0x2C
    VK_INSERT       = 0x2D
    VK_DELETE       = 0x2E
    VK_HELP         = 0x2F

    # VK_0 - VK_9 are the same as ASCII '0' - '9' (0x30 - 0x39)
    # 0x3A - 0x40 : unassigned
    # VK_A - VK_Z are the same as ASCII 'A' - 'Z' (0x41 - 0x5A)

    VK_LWIN         = 0x5B
    VK_RWIN         = 0x5C
    VK_APPS         = 0x5D

    # 0x5E : reserved

    VK_SLEEP        = 0x5F

    VK_NUMPAD0      = 0x60
    VK_NUMPAD1      = 0x61
    VK_NUMPAD2      = 0x62
    VK_NUMPAD3      = 0x63
    VK_NUMPAD4      = 0x64
    VK_NUMPAD5      = 0x65
    VK_NUMPAD6      = 0x66
    VK_NUMPAD7      = 0x67
    VK_NUMPAD8      = 0x68
    VK_NUMPAD9      = 0x69
    VK_MULTIPLY     = 0x6A
    VK_ADD          = 0x6B
    VK_SEPARATOR    = 0x6C
    VK_SUBTRACT     = 0x6D
    VK_DECIMAL      = 0x6E
    VK_DIVIDE       = 0x6F
    VK_F1           = 0x70
    VK_F2           = 0x71
    VK_F3           = 0x72
    VK_F4           = 0x73
    VK_F5           = 0x74
    VK_F6           = 0x75
    VK_F7           = 0x76
    VK_F8           = 0x77
    VK_F9           = 0x78
    VK_F10          = 0x79
    VK_F11          = 0x7A
    VK_F12          = 0x7B
    VK_F13          = 0x7C
    VK_F14          = 0x7D
    VK_F15          = 0x7E
    VK_F16          = 0x7F
    VK_F17          = 0x80
    VK_F18          = 0x81
    VK_F19          = 0x82
    VK_F20          = 0x83
    VK_F21          = 0x84
    VK_F22          = 0x85
    VK_F23          = 0x86
    VK_F24          = 0x87

    VK_NAVIGATION_VIEW   = 0x88
    VK_NAVIGATION_MENU   = 0x89
    VK_NAVIGATION_UP     = 0x8A
    VK_NAVIGATION_DOWN   = 0x8B
    VK_NAVIGATION_LEFT   = 0x8C
    VK_NAVIGATION_RIGHT  = 0x8D
    VK_NAVIGATION_ACCEPT = 0x8E
    VK_NAVIGATION_CANCEL = 0x8F

    VK_NUMLOCK      = 0x90
    VK_SCROLL       = 0x91

    VK_OEM_NEC_EQUAL  0x92  # '=' key on numpad

    VK_OEM_FJ_JISHO = 0x92  # 'Dictionary' key
    VK_OEM_FJ_MASSHOU 0x93  # 'Unregister word' key
    VK_OEM_FJ_TOUROKU 0x94  # 'Register word' key
    VK_OEM_FJ_LOYA  = 0x95  # 'Left OYAYUBI' key
    VK_OEM_FJ_ROYA  = 0x96  # 'Right OYAYUBI' key

    # 0x97 - 0x9F : unassigned

    VK_LSHIFT       = 0xA0
    VK_RSHIFT       = 0xA1
    VK_LCONTROL     = 0xA2
    VK_RCONTROL     = 0xA3
    VK_LMENU        = 0xA4
    VK_RMENU        = 0xA5

    VK_BROWSER_BACK      = 0xA6
    VK_BROWSER_FORWARD   = 0xA7
    VK_BROWSER_REFRESH   = 0xA8
    VK_BROWSER_STOP      = 0xA9
    VK_BROWSER_SEARCH    = 0xAA
    VK_BROWSER_FAVORITES = 0xAB
    VK_BROWSER_HOME      = 0xAC

    VK_VOLUME_MUTE       = 0xAD
    VK_VOLUME_DOWN       = 0xAE
    VK_VOLUME_UP         = 0xAF
    VK_MEDIA_NEXT_TRACK  = 0xB0
    VK_MEDIA_PREV_TRACK  = 0xB1
    VK_MEDIA_STOP        = 0xB2
    VK_MEDIA_PLAY_PAUSE  = 0xB3
    VK_LAUNCH_MAIL       = 0xB4
    VK_LAUNCH_MEDIA_SELECT 0xB5
    VK_LAUNCH_APP1       = 0xB6
    VK_LAUNCH_APP2       = 0xB7

    # 0xB8 - 0xB9 : reserved

    VK_OEM_1        = 0xBA  # ';:' for US
    VK_OEM_PLUS     = 0xBB  # '+' any country
    VK_OEM_COMMA    = 0xBC  # ',' any country
    VK_OEM_MINUS    = 0xBD  # '-' any country
    VK_OEM_PERIOD   = 0xBE  # '.' any country
    VK_OEM_2        = 0xBF  # '/?' for US
    VK_OEM_3        = 0xC0  # '`~' for US

    # 0xC1 - 0xC2 : reserved

    VK_GAMEPAD_A                       = 0xC3
    VK_GAMEPAD_B                       = 0xC4
    VK_GAMEPAD_X                       = 0xC5
    VK_GAMEPAD_Y                       = 0xC6
    VK_GAMEPAD_RIGHT_SHOULDER          = 0xC7
    VK_GAMEPAD_LEFT_SHOULDER           = 0xC8
    VK_GAMEPAD_LEFT_TRIGGER            = 0xC9
    VK_GAMEPAD_RIGHT_TRIGGER           = 0xCA
    VK_GAMEPAD_DPAD_UP                 = 0xCB
    VK_GAMEPAD_DPAD_DOWN               = 0xCC
    VK_GAMEPAD_DPAD_LEFT               = 0xCD
    VK_GAMEPAD_DPAD_RIGHT              = 0xCE
    VK_GAMEPAD_MENU                    = 0xCF
    VK_GAMEPAD_VIEW                    = 0xD0
    VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON  = 0xD1
    VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON = 0xD2
    VK_GAMEPAD_LEFT_THUMBSTICK_UP      = 0xD3
    VK_GAMEPAD_LEFT_THUMBSTICK_DOWN    = 0xD4
    VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT   = 0xD5
    VK_GAMEPAD_LEFT_THUMBSTICK_LEFT    = 0xD6
    VK_GAMEPAD_RIGHT_THUMBSTICK_UP     = 0xD7
    VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN   = 0xD8
    VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT  = 0xD9
    VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT   = 0xDA

    VK_OEM_4        = 0xDB  # '[{' for US
    VK_OEM_5        = 0xDC  # '\|' for US
    VK_OEM_6        = 0xDD  # ']}' for US
    VK_OEM_7        = 0xDE  # ''"' for US
    VK_OEM_8        = 0xDF

    # 0xE0 : reserved

    VK_OEM_AX       = 0xE1  # 'AX' key on Japanese AX kbd
    VK_OEM_102      = 0xE2  # "<>" or "\|" on RT 102-key kbd.
    VK_ICO_HELP     = 0xE3  # Help key on ICO
    VK_ICO_00       = 0xE4  # 00 key on ICO

    VK_PROCESSKEY   = 0xE5

    VK_ICO_CLEAR    = 0xE6

    VK_PACKET       = 0xE7

    # 0xE8 : unassigned

    VK_OEM_RESET    = 0xE9
    VK_OEM_JUMP     = 0xEA
    VK_OEM_PA1      = 0xEB
    VK_OEM_PA2      = 0xEC
    VK_OEM_PA3      = 0xED
    VK_OEM_WSCTRL   = 0xEE
    VK_OEM_CUSEL    = 0xEF
    VK_OEM_ATTN     = 0xF0
    VK_OEM_FINISH   = 0xF1
    VK_OEM_COPY     = 0xF2
    VK_OEM_AUTO     = 0xF3
    VK_OEM_ENLW     = 0xF4
    VK_OEM_BACKTAB  = 0xF5

    VK_ATTN         = 0xF6
    VK_CRSEL        = 0xF7
    VK_EXSEL        = 0xF8
    VK_EREOF        = 0xF9
    VK_PLAY         = 0xFA
    VK_ZOOM         = 0xFB
    VK_NONAME       = 0xFC
    VK_PA1          = 0xFD
    VK_OEM_CLEAR    = 0xFE

    # 0xFF : reserved
