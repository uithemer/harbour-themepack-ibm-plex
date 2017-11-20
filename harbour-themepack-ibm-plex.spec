Name:          harbour-themepack-ibm-plex
Version:       0.0.1
Release:       1
Summary:       IBM Plex font pack
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires: harbour-themepacksupport >= 0.0.8-1
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
IBM Plex package for Theme pack support for Sailfish OS.

%files
%defattr(-,root,root,-)
/usr/share/*

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/harbour-themepack-{name}
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
fi
fi

%changelog
* Mon Nov 20 2017 0.0.1
- First build.
