%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Disk performance panel plugin for Xfce
Name:		xfce4-diskperf-plugin
Version:	2.5.4
Release:	2
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


%changelog
* Sat Jul 14 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5.4-1
+ Revision: 809263
- update to new version 2.5.4
- spec file clean

* Mon Apr 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5.1-1
+ Revision: 791375
- fix file list
- update to new version 2.5.1

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.4.0-1
+ Revision: 789816
- update to new version 2.4.0

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3.0-1
+ Revision: 632779
- update to new version 2.3.0
- update url for Source0

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.0-6mdv2010.1
+ Revision: 543423
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 2.2.0-5mdv2010.0
+ Revision: 446013
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.0-4mdv2009.1
+ Revision: 349451
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.0-3mdv2009.1
+ Revision: 294993
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-2mdv2009.0
+ Revision: 269785
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.0-1mdv2009.0
+ Revision: 195200
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.0-3mdv2008.1
+ Revision: 110117
- correct buildrequires
- do not package COPYING file
- spec file clean
- use upstream tarball name as a real name
- use upstream name

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.0-2mdv2008.0
+ Revision: 30477
- update url
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.0-1mdv2008.0
+ Revision: 30353
- own translation files
- new version

