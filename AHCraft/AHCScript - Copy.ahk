; Do NOT modify this script. If you did, restart AutoHotCraft.exe
#NoEnv
#ErrorStdOut
SendMode Input
WinGet, programid, List, FINAL FANTASY XIV
Sleep 2000
ControlSend,, {Shift down}{vk31}{Shift up}, ahk_id %programid1%
