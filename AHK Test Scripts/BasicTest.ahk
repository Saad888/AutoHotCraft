#NoEnv 
#ErrorStdOut
SendMode Input
WinGet, programid, List, Untitled - Notepad
if A_Args.Length() > 0 
{
    ControlSend,, {%1%}, ahk_id %programid1%
}
FileAppend, %programid1%, *