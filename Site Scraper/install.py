import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 755 sitescraper.py')
    run('mkdir /usr/share/sitescraper')
    run('cp sitescraper.py /usr/share/sitescraper/sitescraper.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/sitescraper/sitescraper.py "$@"')
    with open('/usr/bin/sitescraper','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/sitescraper & chmod +x /usr/share/sitescraper/sitescraper.py')
    print('''\n\ncongratulation sitescraper is installed successfully \nfrom now just type \x1b[6;30;42msitescraper\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/sitescraper ')
    run('rm /usr/bin/sitescraper ')
    print('[!] now sitescraper  has been removed successfully')
