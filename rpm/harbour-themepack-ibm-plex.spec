Name:          harbour-themepack-ibm-plex
Version:       0.0.1
Release:       3
Summary:       IBM Plex font pack
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      harbour-themepacksupport >= 0.8.8-1
Packager:      fravaccaro <me@fravaccaro.com>
URL:           www.jollacommunity.it
License:       GPLv3
Source0:       %{name}-%{version}.tar.gz
BuildArch:     noarch

%description
IBM Plex package for Theme pack support for Sailfish OS.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/%{name}
cp -a theme/. %{buildroot}/usr/share/%{name}/

%files
%defattr(-,root,root,-)
/usr/share/%{name}

%post
mkdir -p /home/defaultuser/.themepack/%{name}
if [ -d "/usr/share/%{name}/font" ]; then
    mv /usr/share/%{name}/font /home/defaultuser/.themepack/%{name}/
    ln -s /home/defaultuser/.themepack/%{name}/font /usr/share/%{name}/
fi
if [ -d "/usr/share/%{name}/font-nonlatin" ]; then
    mv /usr/share/%{name}/font-nonlatin /home/defaultuser/.themepack/%{name}/
    ln -s /home/defaultuser/.themepack/%{name}/ /usr/share/%{name}/
fi

%postun
if [ $1 = 0 ]; then
    # Do stuff specific to uninstalls
    rm -rf /usr/share/%{name}
    rm -rf /home/defaultuser/.themepack/%{name}
elif [ $1 = 1 ]; then
    # Do stuff specific to upgrades
    echo "Upgrading"
fi

%changelog
* Mon Nov 20 2017 0.0.1
- First build.
