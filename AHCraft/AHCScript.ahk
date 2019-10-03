; Do NOT modify this script. If you did, restart AutoHotCraft.exe
#NoEnv
#ErrorStdOut
SendMode Input
WinGet, programid, List, FINAL FANTASY XIV
if A_Args.Length() > 0
{
ControlSend,, %1%, ahk_id %programid1%
}
FileAppend, %programid1%, *
