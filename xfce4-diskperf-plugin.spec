%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Disk performance panel plugin for Xfce
Name:		xfce4-diskperf-plugin
Version:	2.5.4
Release:	1
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-diskperf-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-diskperf-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Group:		Graphical desktop/Xfce
Requires:	xfce4-panel >= 4.9.0
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4ui-devel >= 4.9.1
Obsoletes:	xfce-diskperf-plugin

%description
Disk performance panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

find %{buildroot} -name "*.la" -exec rm -rf {} \;

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libdiskperf.so
%{_datadir}/xfce4/panel/plugins/diskperf.desktop
