import os
import time

os.system('clear')

Version = '1.0.0'
BuildNumber = 'Lin12MPB5'

SetupSays = 'Downloading Files'

def LinuxCustom7Shell():
    while True:
        UserPowershell7Input = input('root@linux:~$ ')

        if UserPowershell7Input == 'GetPnp - Clear':
            os.system('clear')

        if UserPowershell7Input == 'GetPnp - Version':
            print(),print(f"System Version: {Version}"),print(f'System Number: {BuildNumber}'),print()

        elif UserPowershell7Input == 'GetPnp - Help?':
            print(),print('>> Linux Custom?Shell Commands. <<'),print(),print("GetPnp - Clear > Wipes the Screen"),print("GetPnp - Version > Show's System Info!"),print()

for SetupShell in range(50):
    if SetupShell >= 45:
        SetupSays = 'Configuring Info'

    print(f'{SetupSays} > Powershell Plus: ', end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: .', end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: ..',end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: ...',end='\r'), time.sleep(0.2)

    os.system('clear')
os.system('clear'), time.sleep(0.75), LinuxCustom7Shell()