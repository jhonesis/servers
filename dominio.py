import subprocess

# Command 1: sudo apt update
subprocess.run(['sudo', 'apt', 'update'])

# Command 2: sudo apt-get -y install realmd sssd sssd-tools samba-common krb5-user packagekit samba-common-bin samba-libs adcli ntp
subprocess.run(['sudo', 'apt-get', '-y', 'install', 'realmd', 'sssd', 'sssd-tools', 'samba-common', 'krb5-user', 'packagekit', 'samba-common-bin', 'samba-libs', 'adcli', 'ntp'])

# Command 3: sudo realm join solvetic.com -U 'Administrador' -v
subprocess.run(['sudo', 'realm', 'join', 'dominio', '-U', 'Administrador', '-v'])

# Abrir el archivo con sudo nano

subprocess.Popen(["sudo", "nano", "/etc/realmd.conf"]).wait()
texto = "[users]\ndefault-home = /home/%D/%U\ndefault-shell = /bin/bash\n[active-directory]\ndefault-client = sssd\nos-name = Ubuntu Server Linux\nos-version = 22.04\n[service]\nautomatic-install = no\n[DOMINIO]\nfully-qualified-names = no\nautomatic-id-mapping = yes\nuser-principal = yes\nmanage-system = no"
with open("/etc/realmd.conf", "a") as f:
    f.write(texto)


# Abrir el archivo con sudo nano

subprocess.Popen(["sudo", "nano", "/etc/pam.d/common-session"]).wait()
texto2 = "session required pam_unix.so\nsession optional pam_winbind.so\nsession optional pam_sss.so\nsession optional pam_systemd.so\nsession required pam_mkhomedir.so skel=/etc/skel/ umask=0077"
with open("/etc/pam.d/common-session", "a") as f:
    f.write(texto)
