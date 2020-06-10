set WshShell = WScript.CreateObject("WScript.Shell")
   while (1)
   WScript.Sleep 10000
   WshShell.SendKeys "e"
   WshShell.SendKeys "{BACKSPACE}"
   Wend