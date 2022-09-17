# alyx-system-utilities
Quality of life improvements for linux and windows systems. In essence, just a cli wrapper for a multitude of applications

### Universal Package Manager (upm)
```
        Universal Package Manager/upm     
        [written/maintained by Alyxx]
        
    !! might/should work with winget? !!

Usage: [-I] [-R] [-U] [-P] [-d]
       [--manager] [--sandbox] [--autoremove] [--debug]
ex. [upm -I firefox] Would install the firefox from our repository
ex. [upm -I firefox --manager snap] Would install the snap version of firefox
Options:
-I, --install        Installs specified package
-R, --remove         Removes specified package
-U, --update         Updates packages in background then upgrades available packages
-P, --purge          Remove package as well as all dependencies/unused related packages
-d, --details        Gives information on the specified package as well as the dependencies
Long commands only:
--no-confirm         Don't require confirmation for further permissions
--manager            If a specific package manager needs to be used, use this flag
--autoremove         Autoremove unused/unneeded packages from system
Dev tools:
--sandbox            sandbox and test package without installing to system [WIP]
--debug
```
```
To-Do list:
        --add all package managers
        --finish adding all options and main functions
        --find a way to push and pull from repos from within script?
        --add manager.conf file
        --make downloader function
        --use google drive as repo location?
        --add winget
        --add pacstall
        --finish help/man page

```
