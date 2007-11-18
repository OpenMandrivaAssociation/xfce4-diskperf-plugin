Summary:	Disk performance panel plugin for Xfce
Name:		xfce-diskperf-plugin
Version:	2.1.0
Release:	%mkrel 2
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-diskperf-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-diskperf-plugin/xfce4-diskperf-plugin-%{version}.tar.bz2
Group:		Graphical desktop/Xfce
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Disk performance panel plugin for the Xfce Desktop Environment.

%prep
%setup -qn xfce4-diskperf-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang xfce4-diskperf-plugin

%clean
rm -rf %{buildroot}

%files -f xfce4-diskperf-plugin.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
