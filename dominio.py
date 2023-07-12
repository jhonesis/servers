import subprocess
import os

# Command 1: sudo apt update
subprocess.run(['sudo', 'apt', 'update'])
print("*****************UPDATE*********************")
# Command 2: sudo apt-get -y install realmd sssd sssd-tools samba-common krb5-user packagekit samba-common-bin samba-libs adcli ntp
subprocess.run(['sudo', 'apt-get', '-y', 'install', 'realmd', 'sssd', 'sssd-tools', 'samba-common', 'krb5-user', 'packagekit', 'samba-common-bin', 'samba-libs', 'adcli', 'ntp'])
print("*****************INSTALL REALMD SSSD SAMBA*********************")
# Command 3: sudo realm join dominio -U 'Administrador' -v
subprocess.run(['sudo', 'realm', 'join', 'ip-domain', '-U', 'Administrador', '-v'])
print("*****************JOIN DOMAIN*********************")
# Abrir el archivo con sudo nano

texto = "[users]\ndefault-home = /home/%D/%U\ndefault-shell = /bin/bash\n[active-directory]\ndefault-client = sssd\nos-name = Ubuntu Server Linux\nos-version = 22.04\n[service]\nautomatic-install = no\n[DOMINIO]\nfully-qualified-names = no\nautomatic-id-mapping = yes\nuser-principal = yes\nmanage-system = no"
os.system("echo '{}' | sudo tee /etc/realmd.conf > /dev/null".format(texto))
print("*****************EDIT REALMD.CONF*********************")

# Abrir el archivo con sudo nano

texto2 = "session required pam_unix.so\nsession optional pam_winbind.so\nsession optional pam_sss.so\nsession optional pam_systemd.so\nsession required pam_mkhomedir.so skel=/etc/skel/ umask=0077\nsession [default=1] pam_permit.so\nsession requisite pam_deny.so"
os.system("echo '{}' | sudo tee /etc/pam.d/common-session > /dev/null".format(texto2))
print("*****************EDIT PAM.D*********************")
print("ahora... sudo nano /etc/hosts ... y adiciona: ip-server nom-server nom-server.dominio ejm: 127.0.0.15 server25 server25.domain.com " )
print("ahora... sudo nano /etc/sssd/sssd.conf ... en [domain] adiciona: ad_gpo_access_control = permissive")
print("ahora reboot y ok")
