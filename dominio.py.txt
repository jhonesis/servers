import subprocess

# Command 1: sudo apt update
subprocess.run(['sudo', 'apt', 'update'])

# Command 2: sudo apt-get -y install realmd sssd sssd-tools samba-common krb5-user packagekit samba-common-bin samba-libs adcli ntp
subprocess.run(['sudo', 'apt-get', '-y', 'install', 'realmd', 'sssd', 'sssd-tools', 'samba-common', 'krb5-user', 'packagekit', 'samba-common-bin', 'samba-libs', 'adcli', 'ntp'])

# Command 3: sudo realm join solvetic.com -U 'Administrador' -v
subprocess.run(['sudo', 'realm', 'join', 'solvetic.com', '-U', 'Administrador', '-v'])

# Abrir el archivo con sudo nano
subprocess.run(["sudo", "nano", "/etc/realmd.conf"])
texto = "[users]
default-home = /home/%D/%U
default-shell = /bin/bash
[active-directory]
default-client = sssd
os-name = Ubuntu Desktop Linux
os-version = 20.04
[service]
automatic-install = no
[solvetic.com]
fully-qualified-names = no
automatic-id-mapping = yes
user-principal = yes
manage-system = no"
subprocess.run(["echo", f"'{texto}'", "|", "sudo", "tee", "-a", "/etc/realmd.conf"], shell=True)

# Abrir el archivo con sudo nano
subprocess.run(["sudo", "nano", "/etc/pam.d/common-session"])
texto2 = "session required pam_unix.so
session optional pam_winbind.so
session optional pam_sss.so
session optional pam_systemd.so
session required pam_mkhomedir.so skel=/etc/skel/ umask=0077"
subprocess.run(["echo", f"'{texto2}'", "|", "sudo", "tee", "-a", "/etc/pam.d/common-session"], shell=True)



