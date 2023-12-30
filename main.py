# ███████╗██╗  ██╗ █████╗ ███╗   ███╗███████╗ #
# ██╔════╝██║  ██║██╔══██╗████╗ ████║██╔════╝ #
# ███████╗███████║███████║██╔████╔██║█████╗   #
# ╚════██║██╔══██║██╔══██║██║╚██╔╝██║██╔══╝   #
# ███████║██║  ██║██║  ██║██║ ╚═╝ ██║███████╗ #
# ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ #

# made by stillwish
# honestly i dont care what you do with this but dont skid!! 
# (code is shit u can learn how to do all this in an hour)

# imports lol
import subprocess, tkinter, ctypes, time, sys, os, re; from tkinter import filedialog;
os.system('cls'); ctypes.windll.kernel32.SetConsoleTitleW("shame 1.0.1 | pls dont skid!!");

# paths of adb & ldconsole (needed for literally everything)
adb = "C:/LDPlayer/LDPlayer9/adb.exe"

# ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗ #
# ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝ #
# █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗ #
# ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║ #
# ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║ #
# ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ #

# lists all online ldplayer instances
def listADB():
    r = subprocess.run(f"{adb} devices", capture_output=True, text=True)
    return [line.split('\t')[0] for line in r.stdout.strip().split('\n')[1:]];

# roots the adb instances so that way u can actually do stuff in them
def rootADB():
    instances = listADB()
    for instance in instances:
        subprocess.run(f"{adb} -s {instance} root");

# launch instances woohooo!!
def launchInstances():
    os.system('cls')
    print("[1] launch all instances\n[2] launch all instances (Private Server)\n[3] back\n")
    option = int(input("> "))
    
    # normal placeid option
    if option == 1:
        id = int(input("place id > "))
        instances = listADB()
        for instance in instances:
            subprocess.run(f"{adb} -s {instance} shell am start -a android.intent.action.VIEW -d roblox://placeId={id}")
            print(f"launched into game using {instance}");
        
        print("\nlaunched all instances"); time.sleep(1.5); os.system('cls'); main();
    
    # private server link option
    if option == 2:
        os.system('cls')
        link = input("ps link > ")
        instances = listADB()
        
        # this is just to get the placeId & link code from a ps link
        m = re.match(r'https://www\.roblox\.com/games/(\d+)/(?:[^?]+)?\?privateServerLinkCode=([a-zA-Z0-9_\-]+)', link)
        if not m:
            return print("\ninvalid ps link");

        id = m.group(1); code = m.group(2)
        for instance in instances:
            subprocess.run(["adb", "-s", instance, "shell", f'am start -a android.intent.action.VIEW -d "roblox://placeId={id}&linkcode={code}"'])
            print(f"launched into ps using {instance}");
        
        print("\nlaunched all instances into ps"); time.sleep(1.5); os.system('cls'); main();
    
    if option == 3:
        main();

# install any apk you wanna install!!!
def installApk():
    os.system('cls')
    file = filedialog.askopenfilename(filetypes=[("APK files", "*.apk")])
    filePath = os.path.abspath(file)
    instances = listADB()
    
    for instance in instances:
        subprocess.run([adb, "-s", instance, "install", filePath], shell=True)
        print(f"{filePath} installed on {instance}")
    
    print(f"\n{filePath} installed on all instances")
    time.sleep(1.5)
    os.system('cls')
    main()

# clones Storage/autoexec folder to autoexec for fluxus
def cloneAutoexec():
    os.system('cls')
    if getattr(sys, 'frozen', False):
        basePath = os.path.dirname(sys.executable)
    else:
        basePath = os.path.abspath(os.path.dirname(__file__))

    instances = listADB()
    for instance in instances:
        subprocess.run(f'{adb} -s {instance} push "{os.path.abspath(os.path.join(basePath, "Storage/Autoexec"))}" "/data/media/0/Android/data/com.roblox1.client/files/Fluxus/"', shell=True);

    print("\ncloned autoexec to all instances"); time.sleep(1.5); os.system('cls'); main();

# clones Storage/workspace folder to workspace for fluxus
def cloneWorkspace():
    os.system('cls')
    if getattr(sys, 'frozen', False):
        basePath = os.path.dirname(sys.executable)
    else:
        basePath = os.path.abspath(os.path.dirname(__file__));

    instances = listADB()
    for instance in instances:
        subprocess.run(f'{adb} -s {instance} push "{os.path.abspath(os.path.join(basePath, "Storage/Workspace"))}" "/data/media/0/Android/data/com.roblox1.client/files/Fluxus/"', shell=True);

    print("\ncloned workspace to all instances"); time.sleep(1.5); os.system('cls'); main();

# ███████╗██╗  ██╗ █████╗ ███╗   ███╗███████╗ #
# ██╔════╝██║  ██║██╔══██╗████╗ ████║██╔════╝ #
# ███████╗███████║███████║██╔████╔██║█████╗   #
# ╚════██║██╔══██║██╔══██║██║╚██╔╝██║██╔══╝   #
# ███████║██║  ██║██║  ██║██║ ╚═╝ ██║███████╗ #
# ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ #

# main shit lolol
def main():
    rootADB()
    os.system('cls')
    print("shame open source | made by @stillwish\n")
    print("[1] Launch Instances\n[2] Cloning Menu\n[3] Install APK")
    option = int(input("\n > "))

    if option == 1:
        launchInstances()
    
    if option == 2:
        print("[1] Workspace\n[2] Autoexec\n")
        option = int(input("\n > "))
        if option == 1:
            cloneWorkspace()
        if option == 2:
            cloneAutoexec()

    if option == 3:
        installApk()
    
    if option != [1,2,3]:
        main()

main()
