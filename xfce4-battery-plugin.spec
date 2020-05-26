#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-battery-plugin
Version  : 1.1.3
Release  : 1
URL      : http://archive.xfce.org/src/panel-plugins/xfce4-battery-plugin/1.1/xfce4-battery-plugin-1.1.3.tar.bz2
Source0  : http://archive.xfce.org/src/panel-plugins/xfce4-battery-plugin/1.1/xfce4-battery-plugin-1.1.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: xfce4-battery-plugin-data = %{version}-%{release}
Requires: xfce4-battery-plugin-lib = %{version}-%{release}
Requires: xfce4-battery-plugin-license = %{version}-%{release}
Requires: xfce4-battery-plugin-locales = %{version}-%{release}
BuildRequires : intltool
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4panel-2.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)

%description
Battery monitor panel plugin for XFce4.
Battery Icon borrowed from KDE :-)

%package data
Summary: data components for the xfce4-battery-plugin package.
Group: Data

%description data
data components for the xfce4-battery-plugin package.


%package lib
Summary: lib components for the xfce4-battery-plugin package.
Group: Libraries
Requires: xfce4-battery-plugin-data = %{version}-%{release}
Requires: xfce4-battery-plugin-license = %{version}-%{release}

%description lib
lib components for the xfce4-battery-plugin package.


%package license
Summary: license components for the xfce4-battery-plugin package.
Group: Default

%description license
license components for the xfce4-battery-plugin package.


%package locales
Summary: locales components for the xfce4-battery-plugin package.
Group: Default

%description locales
locales components for the xfce4-battery-plugin package.


%prep
%setup -q -n xfce4-battery-plugin-1.1.3
cd %{_builddir}/xfce4-battery-plugin-1.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590453318
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1590453318
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-battery-plugin
cp %{_builddir}/xfce4-battery-plugin-1.1.3/COPYING %{buildroot}/usr/share/package-licenses/xfce4-battery-plugin/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/xfce4-battery-plugin-1.1.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/xfce4-battery-plugin/83ba6546e00f890f3a26a9bedd264084f8527d5e
%make_install
%find_lang xfce4-battery-plugin

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-critical-charging.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-critical.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-full-charging.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-full.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-low-charging.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-low.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-missing.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-ok-charging.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-ok.png
/usr/share/icons/hicolor/16x16/apps/xfce4-battery-plugin.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-critical-charging.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-critical.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-full-charging.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-full.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-low-charging.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-low.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-missing.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-ok-charging.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-ok.png
/usr/share/icons/hicolor/22x22/apps/xfce4-battery-plugin.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-critical-charging.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-critical.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-full-charging.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-full.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-low-charging.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-low.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-missing.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-ok-charging.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-ok.png
/usr/share/icons/hicolor/24x24/apps/xfce4-battery-plugin.png
/usr/share/icons/hicolor/32x32/apps/xfce4-battery-plugin.png
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-critical-charging.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-critical.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-full-charging.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-full.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-low-charging.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-low.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-missing.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-ok-charging.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-ok.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-battery-plugin.svg
/usr/share/xfce4/panel/plugins/battery.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/panel/plugins/libbattery.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-battery-plugin/83ba6546e00f890f3a26a9bedd264084f8527d5e
/usr/share/package-licenses/xfce4-battery-plugin/dfac199a7539a404407098a2541b9482279f690d

%files locales -f xfce4-battery-plugin.lang
%defattr(-,root,root,-)

