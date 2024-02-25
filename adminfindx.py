# -*- coding: utf-8 -*-

import requests
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

def find_admin(url):
    admin_urls = [
      "/admin",
      "/administrator",
      "/login",
      "/admin/login",
      "/administrator/login",
      "/admin.php",
      "/administrator.php",
      "/admin/login.php",
      "/administrator/login.php",
      "/admin.html",
      "/administrator.html",
      "/login.html",
      "/admin/login.html",
      "/administrator/login.html",
      "/admin.jsp",
      "/administrator.jsp",
      "/login.jsp",
      "/admin/login.jsp",
      "/administrator/login.jsp",
      "/admin.asp",
      "/administrator.asp",
      "/login.asp",
      "/admin/login.asp",
      "/administrator/login.asp",
      "/admin.cgi",
      "/administrator.cgi",
      "/login.cgi",
      "/admin/login.cgi",
      "/administrator/login.cgi",
      "/admin/index",
      "/administrator/index",
      "/admin/home",
      "/administrator/home",
      "/admin/controlpanel",
      "/administrator/controlpanel",
      "/admin/administration",
      "/administrator/administration",
      "/admin/cp",
      "/administrator/cp",
      "/admin/admin",
      "/administrator/admin",
      "/admin/administrator",
      "/administrator/administrator",
      "/adminpanel",
      "/admin-panel",
      "/admincontrol",
      "/admin-control",
      "/adminsite",
      "/admin-site",
      "/adminconsole",
      "/admin-console",
      "/adminarea",
      "/admin-area",
      "/admincp",
      "/admin-cp",
      "/administratorcp",
      "/administrator-cp",
      "/administrators",
      "/administrators/login",
      "/administratorlogin",
      "/administrator-login",
      "/admin/administrators",
      "/admin/administratorlogin",
      "/admin/administrator-login",
      "/admin/administrators-login",
      "/admin/login/admin",
      "/admin/login/administrator",
      "/admin/login/administrators",
      "/admin/login/administrators-login",
      "/admin/administrators/login",
      "/admin/administrators/login.php",
      "/admin/administrators/login.html",
      "/admin/administrators/login.jsp",
      "/admin/administrators/login.asp",
      "/admin/administrators/login.cgi",
      "/administrator/administrators-login",
      "/administrator/administrators-login.php",
      "/administrator/administrators-login.html",
      "/administrator/administrators-login.jsp",
      "/administrator/administrators-login.asp",
      "/administrator/administrators-login.cgi",
      "/admin/siteadmin",
      "/admin/site-admin",
      "/admin/siteadministrator",
      "/admin/site-administrator",
      "/admin/adminsite",
      "/admin/admin-site",
      "/admin/adminsiteadmin",
      "/admin/admin-site-admin",
      "/admin/administration/login",
      "/admin/administration-login",
      "/admin/administrations",
      "/admin/administrations/login",
      "/admin/administrations-login",
      "/administration",
      "/administrations",
      "/administration/login",
      "/administration-login",
      "/login/administration",
      "/login-administration",
      "/login/administrations",
      "/login-administrations",
      "/administration/admin",
      "/administration/administrator",
      "/administration/administrators",
      "/administration/login/admin",
      "/administration/login/administrator",
      "/administration/login/administrators",
      "/administration/login/administrators-login",
      "/administration/administrators/login",
      "/administration/administrators/login.php",
      "/administration/administrators/login.html",
      "/administration/administrators/login.jsp",
      "/administration/administrators/login.asp",
      "/administration/administrators/login.cgi",
      "/administration/administrators-login",
      "/administration/administrators-login.php",
      "/administration/administrators-login.html",
      "/administration/administrators-login.jsp",
      "/administration/administrators-login.asp",
      "/administration/administrators-login.cgi",
      "/administration/siteadmin",
      "/administration/site-admin",
      "/administration/siteadministrator",
      "/administration/site-administrator",
      "/administration/adminsite",
      "/administration/admin-site",
      "/administration/adminsiteadmin",
      "/administration/admin-site-admin",
      "/administration/administration-login",
      "/administration/administrations",
      "/administration/administrations-login",
      "/administrations/login/admin",
      "/administrations/login/administrator",
      "/administrations/login/administrators",
      "/administrations/login/administrators-login",
      "/administrations/admin",
      "/administrations/administrator",
      "/administrations/administrators",
      "/administrations/login/admin",
      "/administrations/login/administrator",
      "/administrations/login/administrators",
      "/administrations/login/administrators-login",
      "/administrations/admin/admin",
      "/administrations/admin/administrator",
      "/administrations/admin/administrators",
      "/administrations/login/admin",
      "/administrations/login/administrator",
      "/administrations/login/administrators",
      "/administrations/login/administrators-login",
      "/administration/admin",
      "/administration/administrator",
      "/administration/administrators",
      "/administration/login/admin",
      "/administration/login/administrator",
      "/administration/login/administrators",
      "/administration/login/administrators-login",
      "/administration/admin/admin",
      "/administration/admin/administrator",
      "/administration/admin/administrators",
      "/administration/login/admin",
      "/administration/login/administrator",
      "/administration/login/administrators",
      "/administration/login/administrators-login",
      "/administrations/admin",
      "/administrations/administrator",
      "/administrations/administrators",
      "/administrations/login/admin",
      "/administrations/login/administrator",
      "/administrations/login/administrators",
      "/administrations/login/administrators-login",
      "/admin",
      "/administrator",
      "/administrators",
      "/login",
      "/panel",
      "/paneladmin",
      "/panel-admin",
      "/panel_admin",
      "/panel-administration",
      "/panel-administrator",
      "/panellogin",
      "/panel-login",
      "/panel/signin",
      "/panel/sign-in",
      "/panel/sign_in",
      "/panel/admin",
      "/panel/administrator",
      "/panel/administrators",
      "/panel/login/admin",
      "/panel/login/administrator",
      "/panel/login/administrators",
      "/panel/login/administrators-login",
      "/panel/admin/admin",
      "/panel/admin/administrator",
      "/panel/admin/administrators",
      "/panel/login/admin",
      "/panel/login/administrator",
      "/panel/login/administrators",
      "/panel/login/administrators-login",
      "/controlpanel",
      "/control-panel",
      "/control_panel",
      "/control-admin",
      "/control-administrator",
      "/control-administrators",
      "/control/login",
      "/control/login-admin",
      "/control/login-administrator",
      "/control/login-administrators",
      "/control/login-administrators-login",
      "/control/login/admin",
      "/control/login/administrator",
      "/control/login/administrators",
      "/control/login/administrators-login",
      "/control/admin",
      "/control/administrator",
      "/control/administrators",
      "/control/login/admin",
      "/control/login/administrator",
      "/control/login/administrators",
      "/control/login/administrators-login",
      "/cp",
      "/cp-admin",
      "/cp-administrator",
      "/cp-administrators",
      "/cp/login",
      "/cp/login-admin",
      "/cp/login-administrator",
      "/cp/login-administrators",
      "/cp/login-administrators-login",
      "/cp/login/admin",
      "/cp/login/administrator",
      "/cp/login/administrators",
      "/cp/login/administrators-login",
      "/cp/admin",
      "/cp/administrator",
      "/cp/administrators"


    ]

    found_admin_pages = []

    for admin_url in admin_urls:
        full_url = url + admin_url
        response = requests.get(full_url)
        if response.status_code == 200:
            found_admin_pages.append(full_url)
            print(Fore.GREEN + "[+] Admin page found:", full_url)
        elif response.status_code == 401:
            print(Fore.YELLOW + "[!] Authorization Required:", full_url)
        elif response.status_code == 403:
            print(Fore.RED + "[!] Forbidden Access:", full_url)
        else:
            print(Fore.WHITE + "[?] Unknown Status:", full_url)

    return found_admin_pages

def loading_animation():
    chars = "/\ "  # Animation characters
    for _ in range(20):
        for char in chars:
            time.sleep(0.1)
            print("\b" + char, end="", flush=True)

if __name__ == "__main__":
    print(Style.BRIGHT + Fore.CYAN + """
           _____  __  __ _____ _   _ ______ _____ _   _ _______   __
     /\   |  __ \|  \/  |_   _| \ | |  ____|_   _| \ | |  __ \ \ / /
    /  \  | |  | | \  / | | | |  \| | |__    | | |  \| | |  | \ V / 
   / /\ \ | |  | | |\/| | | | | . ` |  __|   | | | . ` | |  | |> <  
  / ____ \| |__| | |  | |_| |_| |\  | |     _| |_| |\  | |__| / . \ 
 /_/    \_\_____/|_|  |_|_____|_| \_|_|    |_____|_| \_|_____/_/ \_\
                                 
                                                    BY NEWTON                                                        

""" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.MAGENTA + "Welcome to ADMINFINDX!" + Style.RESET_ALL)
    print("Enter the target URL (e.g., http://example.com):")
    target_url = input("> ")
    print("\nSearching for admin pages", end="")

    # Start loading animation
    loading_animation()

    # Search for admin pages
    found_admin_pages = find_admin(target_url)

    # Highlight found admin pages with variety of colors
    if found_admin_pages:
        print("\n\n" + Style.BRIGHT + Fore.WHITE + "Found admin pages:")
        for i, page in enumerate(found_admin_pages):
            color = [Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.RED]
            print(color[i % len(color)] + "  - " + page)
    else:
        print(Fore.RED + "\n\nNo admin pages found!")
