set WshShell = WScript.CreateObject("WScript.Shell")
   while (1)
   WScript.Sleep 180000
   WshShell.SendKeys "e"
   WshShell.SendKeys "{BACKSPACE}"
   Wend