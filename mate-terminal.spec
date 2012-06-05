Summary:	MATE terminal
Name:		mate-terminal
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	rarian
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(x11)

%description
This is the MATE terminal emulator application.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-schemas-install \
	--disable-scrollkeeper

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%post
if [ "$1" = "2" ]; then
	update-alternatives --remove xvt %{_bindir}/mate-terminal
fi

%files -f %{name}.lang
%doc AUTHORS README NEWS HACKING
%{_sysconfdir}/mateconf/schemas/mate-terminal.schemas
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mate-terminal
# mate help files
%{_datadir}/mate/help

