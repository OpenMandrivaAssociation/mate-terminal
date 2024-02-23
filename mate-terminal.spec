%define mate_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	MATE terminal
Name:		mate-terminal
Version:	1.28.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	libxml2-utils
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(libpcre2-posix)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(x11)
BuildRequires:	yelp-tools

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides the MATE terminal emulator application. The MATE
terminal emulator application is only the shell (menubar, prefs dialog); the
terminal emulation ("stuff in the middle") comes from the VTE widget.

%files -f %{name}.lang
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/mate-terminal
%{_bindir}/mate-terminal.wrapper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%doc %{_mandir}/man1/mate-terminal.1*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--disable-schemas-compile \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

