%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE terminal
Name:		mate-terminal
Version:	1.18.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(x11)

%description
This is the MATE terminal emulator application.

%prep
%setup -q
%apply_patches

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%post
#FIXME: error: %post(mate-terminal-1.18.1-1.x86_64) scriptlet failed, exit status 2
if [ "$1" = "2" ]; then
	update-alternatives --remove xvt %{_bindir}/mate-terminal
fi

%files -f %{name}.lang
%doc AUTHORS README NEWS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%{_datadir}/mate-terminal
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/mate-terminal.1*

