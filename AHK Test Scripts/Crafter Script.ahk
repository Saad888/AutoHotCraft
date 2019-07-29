^s:: ; Command to start bot. In this case it is CTRL+S
WinGet, programid, List, FINAL FANTASY XIV
Loop 1 ; This line dictates how many times the following code will be repeated.
    {
    Loop 50  ; This line dictates how many times it will craft something before your character consumes a food buff.
        {
        ControlSend,,{Numpad0}, ahk_id %programid1% 
        Sleep 2000
        ControlSend,,{Numpad0}, ahk_id %programid1% 
        Sleep 2000
        ControlSend,,{Numpad0}, ahk_id %programid1% 
        Sleep 2000
        ControlSend,,{Numpad0}, ahk_id %programid1% 
        Sleep 2000
        ControlSend,,{8}, ahk_id %programid1%  ; This is the first crafting macro that will be pressed.
        Sleep 2000     ; This the amount of time that will pass until the next button is pressed, to be safe multiply the number of lines in macro by three.
        ;ControlSend,,{-}, ahk_id %programid1%  ; This is the second crafting macro that will be pressed.
        ;Sleep 20000     ; This the amount of time that will pass until the next button is pressed, to be safe multiply the number of lines in macro by three.
        ControlSend,,{Numpad0}, ahk_id %programid1% 
        Sleep 4800
        }
    ControlSend,,{Escape}, ahk_id %programid1% 
    Sleep 4000
    ;ControlSend,,{9}, ahk_id %programid1%  ; This line is the button pressed to consume a food buff.
    ;Sleep 7000
    ;ControlSend,,{N}, ahk_id %programid1%
    ;Sleep 2000
    ;ControlSend,,{Numpad0}, ahk_id %programid1% 
    }
    INS::pause
Return