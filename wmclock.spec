Summary:        The AfterStep Clock for Window Maker
Summary(pl):	Zegarek przeniesiony z AfterStep do WindowMakera
Name: 		wmclock
Version: 	1.0
Release: 	2
Copyright: 	Freeware
Group:          X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0: 	http://www.windowmaker.org/ftp/pub/contrib/srcs/apps/asclock.tgz
Source1:	wmclock.desktop
Icon:           wmclock.gif
URL:            http://afterstep.edoc.com/
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6
%define _mandir %{_prefix}/man

%description
This is a Window Maker enhanced asclock (i.e. a patch to allow asclock to be
docked on Window Maker has been included). In this package, asclock was
renamed to wmclock to avoid clashes with an AfterStep installation on the
system.

%description -l pl
wmclock to asclock z dodan± mo¿liwo¶ci± u¿ywania go w WindowMakerze.

%prep
%setup -q -n asclock

%build
rm -f asclock.o asclock clk.xpm weekday.xpm month.xpm
ln -s xpm/color.xpm clk.xpm
ln -s english/month.xpm month.xpm 
ln -s english/weekday.xpm weekday.xpm

xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include" \
	CXXFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

install -s asclock $RPM_BUILD_ROOT%{_bindir}/wmclock
install asclock.man $RPM_BUILD_ROOT%{_mandir}/man1/wmclock.1x
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/wmclock.1x \
	README

%files
%defattr(644,root,root,755)
%doc README.gz
%{_bindir}/wmclock
%{_mandir}/man1/wmclock.1x.gz

/etc/X11/applnk/DockApplets/wmclock.desktop

%changelog
* Sun Jul 11 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.0-2]
- spec rewritten for PLD use,
- based on spec file by Thomas Ribbrock <emgaron@gmx.net>.
