.traytip, Compiled-Aimbot-.[censored].net%version%, Running in background!, 5, 1
Menu, tray, NoStandard
Menu, tray, Tip, Sharpshooter %version%
Menu, tray, Add, Sharpshooter %version%, return
Menu, tray, Add
Menu, tray, Add, Help, info
Menu, tray, Add, Exit, exit
SetKeyDelay,-1, 1
SetControlDelay, -1
SetMouseDelay, -1
SetWinDelay,-1
SendMode, InputThenPlay
SetBatchLines,-1
ListLines, Off
CoordMode, Pixel, Screen, RGB
CoordMode, Mouse, Screen
PID := DllCall("GetCurrentProcessId")
Process, Priority, %PID%, High
 
EMCol := 0xD82A22,0xDD5879,0x322F2D,0x0DF317,0xABB3C0,0xD82A22,0x240E11,0x955647,0x5D024F,0x1599A5,0x61145C,0xEEE679,0xD0723E,0xEAE6DB,0x915612,0x424649,0x7F5103,0x54697E,0xD68E44,0xB80A0V,0xD0B56A,0x813D2B,0xaC351A,0xE9D795,0xB5AF9B,0xE94F58,0x612B37,0x2ADD31,0x612B37
ColVn := 65
AntiShakeX := (A_ScreenHeight // 160)
AntiShakeY := (A_ScreenHeight // 128)
ZeroX := (A_ScreenWidth // 2)
ZeroY := (A_ScreenHeight // 2)
CFovX := (A_ScreenWidth // 8)
CFovY := (A_ScreenHeight // 64)
ScanL := ZeroX - CFovX
ScanT := ZeroY
ScanR := ZeroX + CFovX
ScanB := ZeroY + CFovY
NearAimScanL := ZeroX - AntiShakeX
NearAimScanT := ZeroY - AntiShakeY
NearAimScanR := ZeroX + AntiShakeX
NearAimScanB := ZeroY + AntiShakeY
 
Loop, {
    KeyWait, RButton, D
    PixelSearch, AimPixelX, AimPixelY, NearAimScanL, NearAimScanT, NearAimScanR, NearAimScanB, EMCol, ColVn, Fast RGB
    if (!ErrorLevel=0) {
        loop, 10 {
            PixelSearch, AimPixelX, AimPixelY, ScanL, ScanT, ScanR, ScanB, EMCol, ColVn, Fast RGB
            AimX := AimPixelX - ZeroX
            AimY := AimPixelY - ZeroY
            DirX := -1
            DirY := -1
            If ( AimX > 0 ) {
                DirX := 1
            }
            If ( AimY > 0 ) {
                DirY := 1
            }
            AimOffsetX := AimX * DirX
            AimOffsetY := AimY * DirY
            MoveX := Floor(( AimOffsetX ** ( 1 / 2 ))) * DirX
            MoveY := Floor(( AimOffsetY ** ( 1 / 2 ))) * DirY
            DllCall("mouse_event", uint, 1, int, MoveX * 1.5, int, MoveY, uint, 0, int, 0)
        }
    }
}
 
Pause:: pause
return:
goto, init