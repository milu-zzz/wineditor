import os, time, ctypes, sys, winreg

os.system("title wineditor  ^|  www.milu.cf")
os.system('mode con lines=17 cols=78')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # ---------- defender options ----------
    def defenderoptions():
        os.system("cls")
        print("      Windows Defender Options")
        print("=====================================")
        print("1. Enable Defender")
        print("2. Disable Defender")
        print("3. Go Back")
        print("=====================================")
        defenderchoice = input("Choice> ")
        if defenderchoice == '1':
            enabledefender()
        elif defenderchoice == '2':
            disabledefender()
        elif defenderchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            defenderoptions()

    # - enable defender -
    def enabledefender():
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows Defender\Features")
        os.system(r'reg add "HKLM\SOFTWARE\Microsoft\Windows Defender\Features" /v "TamperProtection" /t "REG_DWORD" /d "5" /f')
        os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t "REG_DWORD" /d "0" /f')
        os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t "REG_DWORD" /d "0" /f')
        rebootdefender()

    # - disable defender -
    def disabledefender():
        print("due to a windows update, doing this can no longer be done 100% automated\nyou have to manually go into windows security and turn off \"Tamper Protection\"")
        print("after you have turned it off, come back here and type \"continue\"")
        ans = input("> ")
        if ans == "continue":
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows Defender\Features")
            #os.system(r'reg add "HKLM\SOFTWARE\Microsoft\Windows Defender\Features" /v "TamperProtection" /t "REG_DWORD" /d "0" /f')
            os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t "REG_DWORD" /d "1" /f')
            os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t "REG_DWORD" /d "1" /f')
            rebootdefender()
        else:
            print("returning to main screen...")
            time.sleep(3)
            main()

    # - reboot defender -
    def rebootdefender():
        os.system("cls")
        restart = input("Windows Defender has been modified. Do you want to re-log your PC to apply\nthe new setting? (Y/N): ")
        if restart == 'N':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'n':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'Y':
            os.system("shutdown -l")
        elif restart == 'y':
            os.system("shutdown -l")
        else:
            print("invalid choice option")
            time.sleep(1)
            os.system("cls")
            rebootdefender()

    # ---------- cortana options ----------
    def cortanaoptions():
        os.system("cls")
        print("           Cortana Options")
        print("=====================================")
        print("1. Enable Cortana")
        print("2. Disable Cortana")
        print("3. Go Back")
        print("=====================================")
        cortanachoice = input("Choice> ")
        if cortanachoice == '1':
            enablecortana()
        elif cortanachoice == '2':
            disablecortana()
        elif cortanachoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            defenderoptions()

    # - enable cortana -
    def enablecortana():
        os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "AllowCortana" /t "REG_DWORD" /d "1" /f')
        rebootcortana()

    # - disable cortana -
    def disablecortana():
        os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "AllowCortana" /t "REG_DWORD" /d "0" /f')
        rebootcortana()

    # - reboot cortana -
    def rebootcortana():
        os.system("cls")
        restart = input("Cortana has been modified. Do you want to re-log your PC to apply the new\nsetting? (Y/N): ")
        if restart == 'N':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'n':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'Y':
            os.system("shutdown -l /t 1")
        elif restart == 'y':
            os.system("shutdown -l /t 1")
        else:
            print("invalid choice option")
            time.sleep(1)
            os.system("cls")
            rebootcortana()

    # ---------- windows feedback options ----------
    def feedbackoptions():
        os.system("cls")
        print("       Windows Feedback Options")
        print("=====================================")
        print("1. Enable Feedback Notifs")
        print("2. Disable Feedback Notifs")
        print("3. Go Back")
        print("=====================================")
        feedbackchoice = input("Choice> ")
        if feedbackchoice == '1':
            enablefeedback()
        elif feedbackchoice == '2':
            disablefeedback()
        elif feedbackchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            defenderoptions()

    # - enable feedback -
    def enablefeedback():
        os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "DoNotShowFeedbackNotifications" /t "REG_DWORD" /d "0" /f')
        rebootfeedback()

    # - disable feedback -
    def disablefeedback():
        os.system(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "DoNotShowFeedbackNotifications" /t "REG_DWORD" /d "1" /f')
        rebootfeedback()

    # - reboot feedback -
    def rebootfeedback():
        os.system("cls")
        restart = input("Windows Feedback has been modified. Do you want to re-log your PC to apply\nthe new setting? (Y/N): ")
        if restart == 'N':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'n':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'Y':
            os.system("shutdown -l /t 1")
        elif restart == 'y':
            os.system("shutdown -l /t 1")
        else:
            print("invalid choice option")
            time.sleep(1)
            os.system("cls")
            rebootfeedback()

    # ---------- optimize shutdown options ----------
    def shutdownoptions():
        os.system("cls")
        print("      Optimize Shutdown Options")
        print("=====================================")
        print("1. Optimize Shutdown")
        print("2. What Does This Do?")
        print("3. Go Back")
        print("=====================================")
        shutdownchoice = input("Choice> ")
        if shutdownchoice == '1':
            optimizeshutdown()
        elif shutdownchoice == '2':
            aboutshutdown()
        elif shutdownchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            shutdownoptions()

    # - optimize shutdown -
    def optimizeshutdown():
        os.system(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v "WaitToKillServiceTimeout" /t "REG_DWORD" /d "1000" /f')
        rebootshutdown()

    # - about shutdown -
    def aboutshutdown():
        print("Optimize Shutdown will speed up the time it takes for your PC to shut down.\nIt removes the \"waiting for all apps to close\" feature.")
        shutdownchoice = input("Choice> ")
        if shutdownchoice == '1':
            optimizeshutdown()
        elif shutdownchoice == '2':
            aboutshutdown()
        elif shutdownchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            shutdownoptions()

    # - reboot shutdown -
    def rebootshutdown():
        os.system("cls")
        restart = input("Shutdown speed has been optimized. Do you want to re-log your PC to apply\nthe new setting? (Y/N): ")
        if restart == 'N':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'n':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'Y':
            os.system("shutdown -l /t 1")
        elif restart == 'y':
            os.system("shutdown -l /t 1")
        else:
            print("invalid choice option")
            time.sleep(1)
            os.system("cls")
            rebootshutdown()

    # ---------- optimize start-up options ----------
    def startupoptions():
        os.system("cls")
        print("     Optimize Start-Up Options")
        print("=====================================")
        print("1. Optimize Start-Up")
        print("2. What Does This Do?")
        print("3. Go Back")
        print("=====================================")
        print("NOTE: This may not have a visible effect.")
        startupchoice = input("Choice> ")
        if startupchoice == '1':
            optimizestartup()
        elif startupchoice == '2':
            aboutstartup()
        elif startupchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            startupoptions()

    # - optimize startup -
    def optimizestartup():
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize")
        os.system(r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" /v "StartupDelayInMSec" /t "REG_DWORD" /d "0" /f')
        rebootstartup()

    # - about start-up -
    def aboutstartup():
        print("Optimize Start-Up will speed up the time it takes for your PC to start-up\nwhen you turn it on.\nIt removes the delay that windows defaults before your apps open at start-up.")
        startupchoice = input("Choice> ")
        if startupchoice == '1':
            optimizestartup()
        elif startupchoice == '2':
            aboutstartup()
        elif startupchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            startupoptions()

    # - reboot start-up -
    def rebootstartup():
        os.system("cls")
        restart = input("Start-Up speed has been optified. Do you want to re-log your PC to apply\nthe new setting? (Y/N): ")
        if restart == 'N':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'n':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'Y':
            os.system("shutdown -l /t 1")
        elif restart == 'y':
            os.system("shutdown -l /t 1")
        else:
            print("invalid choice option")
            time.sleep(1)
            os.system("cls")
            rebootstartup()

    # ---------- clear TEMP options ----------
    def cleartempoptions():
        os.system("cls")
        print("     Clear TEMP Folders Options")
        print("=====================================")
        print("1. Clear TEMP Folders")
        print("2. What Does This Do?")
        print("3. Go Back")
        print("=====================================")
        cleartempchoice = input("Choice> ")
        if cleartempchoice == '1':
            cleartemp()
        elif cleartempchoice == '2':
            aboutcleartemp()
        elif cleartempchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            cleartempoptions()

    # - clear TEMP -
    def cleartemp():
        os.system(r'del /F /S /Q "%TEMP%\*.*" >nul 2>nul')
        os.system(r'rd /S /Q "%TEMP%" >nul 2>nul')
        os.system(r'md "%TEMP%" >nul 2>nul')
        os.system(r'rd /S /Q "%SystemDrive%\temp" >nul 2>nul')
        print("successfully cleared TEMP folders, returning to main screen...")
        time.sleep(3)
        main()

    # - about clear TEMP -
    def aboutcleartemp():
        print("Clear TEMP Folders will delete most files in your %temp% folders.\nIt won't delete anything needed, they're temporary files that take up space.")
        cleartempchoice = input("Choice> ")
        if cleartempchoice == '1':
            cleartemp()
        elif cleartempchoice == '2':
            aboutcleartemp()
        elif cleartempchoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            cleartempoptions()
        
     # ---------- windows security options ----------
    def securityoptions():
        os.system("cls")
        print("      Windows Security Options")
        print("=====================================")
        print("1. Enable Security Notifs")
        print("2. Disable Security Notifs")
        print("3. Go Back")
        print("=====================================")
        print("NOTE: This may or may not work for you.")
        securitychoice = input("Choice> ")
        if securitychoice == '1':
            enablesecnotifs()
        elif securitychoice == '2':
            disablesecnotifs()
        elif securitychoice == '3':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            os.system("cls")
            securityoptions()

    # - enable security notifs -
    def enablesecnotifs():
        os.system(r'reg add "HKLM\SOFTWARE\Microsoft\Windows Defender Security Center\Notifications" /v "DisableAllNotifications" /t "REG_DWORD" /d "0" /f')
        rebootsecnotifs()

    # - disable security notifs -
    def disablesecnotifs():
        os.system(r'reg add "HKLM\SOFTWARE\Microsoft\Windows Defender Security Center\Notifications" /v "DisableAllNotifications" /t "REG_DWORD" /d "1" /f')
        rebootsecnotifs()

    # - reboot start-up -
    def rebootsecnotifs():
        os.system("cls")
        restart = input("Windows Security Notifs have been changed. Do you want to re-log your PC to\napply the new setting? (Y/N): ")
        if restart == 'N':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'n':
            print("returning to main screen...")
            time.sleep(3)
            main()
        elif restart == 'Y':
            os.system("shutdown -l /t 1")
        elif restart == 'y':
            os.system("shutdown -l /t 1")
        else:
            print("invalid choice option")
            time.sleep(1)
            os.system("cls")
            rebootsecnotifs()

    # ---------- info screen ----------
    def info():
        os.system("cls")
        print("                info")
        print("=====================================")
        print(" wineditor vers   |     1.1")
        print(" creator          |     www.milu.cf")
        print("=====================================")
        choice = input("Type 1 to go back> ")
        if choice == '1':
            main()
        else:
            print("invalid choice option")
            time.sleep(2)
            info()

    def defendercheck(): # unfinished
        try:
            path = winreg.HKEY_LOCAL_MACHINE
            key = winreg.OpenKeyEx(path, r"SOFTWARE\\Policies\\Microsoft\\Windows Defender")
            value = "DisableAntiSpyware"
            data = winreg.QueryValueEx(key,value)
            if key:
                winreg.CloseKey(key)
            print(data[1:2])
        except Exception as e:
            print(e)
        return None

    # ---------- main screen ----------
    def main():
        os.system("cls")
        print("  Welcome to wineditor v1.1 by milu")
        print("=====================================")
        print("1. Windows Defender Options")
        print("2. Cortana Options")
        print("3. Windows Feedback Options")
        print("4. Optimize Shutdown")
        print("5. Optimize Start-Up")
        print("6. Clear TEMP Folders")
        print("7. Windows Security Options")
        print("8. Info")
        print("=====================================")
        choice = input("Choice> ")
        if choice == '1':
            defenderoptions()
        elif choice == '2':
            cortanaoptions()
        elif choice == '3':
            feedbackoptions()
        elif choice == '4':
            shutdownoptions()
        elif choice == '5':
            startupoptions()
        elif choice == '6':
            cleartempoptions()
        elif choice == '7':
            securityoptions()
        elif choice == '8':
            info()
        else:
            print("invalid choice option")
            time.sleep(2)
            main()

    main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
