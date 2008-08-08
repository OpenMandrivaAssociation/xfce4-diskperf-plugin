Summary:	Disk performance panel plugin for Xfce
Name:		xfce4-diskperf-plugin
Version:	2.2.0
Release:	%mkrel 2
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-diskperf-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-diskperf-plugin/%{name}-%{version}.tar.bz2
Group:		Graphical desktop/Xfce
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-diskperf-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Disk performance panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
