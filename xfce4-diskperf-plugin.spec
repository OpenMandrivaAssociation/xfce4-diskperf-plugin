%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Disk performance panel plugin for Xfce
Name:		xfce4-diskperf-plugin
Version:	2.8.0
Release:	1
License:	BSD
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-diskperf-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-diskperf-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Group:		Graphical desktop/Xfce
Requires:	xfce4-panel >= 4.9.0
BuildRequires:	meson
BuildRequires:	make
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
Obsoletes:	xfce-diskperf-plugin

%description
Disk performance panel plugin for the Xfce Desktop Environment.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name "*.la" -exec rm -rf {} \;

%find_lang %{name}

%files -f %{name}.lang
%doc README* AUTHORS
%{_libdir}/xfce4/panel/plugins/libdiskperf.so
%{_datadir}/xfce4/panel/plugins/diskperf.desktop
