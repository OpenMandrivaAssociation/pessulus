%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Desktop lockdown editor for GNOME
Name:		pessulus
Version:	2.30.4
Release:	7
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/~vuntz/pessulus/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pessulus/%{url_ver}/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-python-desktop
BuildRequires:	intltool
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(gnome-python-2.0)
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	pygtk2.0-libglade
#gw for bugbuddy
Requires:	gnome-python-desktop

%description 
pessulus is a lockdown editor for GNOME, written in python.  pessulus
enables administrators to set mandatory settings in GConf. The users
can not change these settings.

Use of pessulus can be useful on computers that are open to use by
everyone, e.g. in an internet cafe.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%make

%install
%makeinstall_std
%find_lang %{name}
desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-System-Configuration-GNOME-Advanced" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*


%files -f %{name}.lang
%doc AUTHORS ChangeLog HACKING NEWS MAINTAINERS README TODO
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{py_puresitedir}/Pessulus/

