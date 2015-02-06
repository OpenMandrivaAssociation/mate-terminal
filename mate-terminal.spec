%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE terminal
Name:		mate-terminal
Version:	1.8.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(x11)

%description
This is the MATE terminal emulator application.

%prep
%setup -q
%apply_patches
NOCONFIGURE=yes ./autogen.sh

%build
%configure

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%post
if [ "$1" = "2" ]; then
	update-alternatives --remove xvt %{_bindir}/mate-terminal
fi

%files -f %{name}.lang
%doc AUTHORS README NEWS HACKING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%{_datadir}/mate-terminal
%{_mandir}/man1/mate-terminal.1*

