%define name pessulus
%define version 2.28.0

Summary: Desktop lockdown editor for GNOME
Name: %{name}
Version: %{version}
Release: %mkrel 1
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


