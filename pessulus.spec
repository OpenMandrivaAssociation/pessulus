%define name pessulus
%define version 2.30.4

Summary: Desktop lockdown editor for GNOME
Name: %{name}
Version: %{version}
Release: 4
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/~vuntz/pessulus/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: pygtk2.0-devel >= 2.6.0
BuildRequires: gnome-python >= 2.6.0
BuildRequires: gnome-python-devel >= 2.6.0
BuildRequires: gnome-python-desktop
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires: gnome-python gnome-python-gconf pygtk2.0-libglade
#gw for bugbuddy
Requires: gnome-python-desktop

%description 
pessulus is a lockdown editor for GNOME, written in python.  pessulus
enables administrators to set mandatory settings in GConf. The users
can not change these settings.

Use of pessulus can be useful on computers that are open to use by
everyone, e.g. in an internet cafe.


%prep
%setup -q

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME-Advanced" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%if %mdkversion < 200900
%post
%update_menus
%endif
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS MAINTAINERS README TODO
%_bindir/%name
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/
%_datadir/applications/%name.desktop
%py_puresitedir/Pessulus/




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.4-2mdv2011.0
+ Revision: 667473
- mass rebuild

* Wed Nov 17 2010 Götz Waschk <waschk@mandriva.org> 2.30.4-1mdv2011.0
+ Revision: 598367
- update to new version 2.30.4

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 2.30.3-2mdv2011.0
+ Revision: 592033
- Rebuild

* Tue Sep 14 2010 Götz Waschk <waschk@mandriva.org> 2.30.3-1mdv2011.0
+ Revision: 578285
- update to new version 2.30.3

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 550678
- update to new version 2.30.2

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528958
- update to new version 2.30.0

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509640
- update to new version 2.29.91

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 497247
- update to new version 2.29.6

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446793
- update to new version 2.28.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437226
- update to new version 2.27.92

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 421046
- update to new version 2.27.91

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 402525
- update to new version 2.27.5

* Tue Jun 30 2009 Götz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 390821
- update to new version 2.26.2

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366932
- update to new version 2.26.1

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356261
- update to new version 2.26.0

* Tue Mar 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 348024
- update to new version 2.25.92

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 2.24.0-2mdv2009.1
+ Revision: 319381
- rebuild for new python

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286519
- fix build on x86_64
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.1-1mdv2009.0
+ Revision: 230962
- update deps
- new version
- update license
- update buildrequires
- update file list

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.16.4-1mdv2009.0
+ Revision: 218428
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.16.4-1mdv2008.1
+ Revision: 183841
- new version

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.16.3-2mdv2008.1
+ Revision: 180111
- fix build deps
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.16.3-1mdv2008.0
+ Revision: 89334
- new version
- fix build


* Tue Dec 19 2006 Götz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.0
+ Revision: 99161
- fix build on x86_64
- new version

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Rebuild against new python

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-2mdv2007.1
+ Revision: 63738
- rebuild
- Import pessulus

* Fri Oct 06 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- New version 2.16.1

* Tue Sep 05 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1
- New release 2.15.90

* Wed Jul 12 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2007.0
- xdg menu
- New release 0.10.4

* Wed Apr 26 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- New release 0.10.1

* Tue Apr 11 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdk
- New release 0.9.1

* Mon Mar 13 2006 Götz Waschk <waschk@mandriva.org> 0.9-1mdk
- New release 0.9

* Tue Feb 28 2006 Götz Waschk <waschk@mandriva.org> 0.8-1mdk
- New release 0.8

* Mon Feb 20 2006 Götz Waschk <waschk@mandriva.org> 0.7-4mdk
- fix deps

* Mon Feb 20 2006 Götz Waschk <waschk@mandriva.org> 0.7-3mdk
- fix buildrequires

* Fri Feb 17 2006 Götz Waschk <waschk@mandriva.org> 0.7-2mdk
- fix deps

* Fri Feb 17 2006 Götz Waschk <waschk@mandriva.org> 0.7-1mdk
- initial package

