Name: wmclock
Version: 1.0
Release: 1
Copyright: Freeware
URL: http://afterstep.edoc.com/
Source0: http://www.windowmaker.org/ftp/pub/contrib/srcs/apps/asclock.tgz
Group: X11/Utilities
Icon: AStep.gif
Summary: The AfterStep Clock for Window Maker
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is a Window Maker enhanced asclock (i.e. a patch to allow asclock to be
docked on Window Maker has been included). In this package, asclock was
renamed to wmclock to avoid clashes with an AfterStep installation on the
system.
Asclock is a clock written to emulate the date/time application on the
NeXTStep OS. It supports multiple languages, military and AM/PM time,
program execution, shape extension, and multiple color depths.
This version is compiled with English language support and 2bit display
(four colours).

%changelog
* Mon Feb 1 1999 Thomas Ribbrock <emgaron@gmx.net> wmclock 1.0-1
- renamed to wmclock to avoid clashes with AfterStep
- using the Window Maker as source for the tar ball now, as their tar ball
  already includes the necessary patch.

* Sat Feb 7 1998 Cesar Cardoso <ccardoso@cesarcardoso.dyn.ml.org> 1.0-2
- A patch for asclock be dockable on WindowMaker

* Sun Jun 8 1997 Xi <ximenes@null.net> 1.0-1
- Initial RPM

%prep
%setup -n asclock
rm -f weekday.xpm asclock month.xpm asclock.o
ln -s english/month.xpm month.xpm
ln -s english/weekday.xpm weekday.xpm
rm -f clk.xpm
ln -s xpm/clk2.xpm clk.xpm
xmkmf

%build
make
strip asclock

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/X11R6/bin/asclock $RPM_BUILD_ROOT/usr/X11R6/bin/wmclock
mv $RPM_BUILD_ROOT/usr/X11R6/man/man1/asclock.1x $RPM_BUILD_ROOT/usr/X11R6/man/man1/wmclock.1x

%files
%doc README INSTALL
/usr/X11R6/bin/wmclock
/usr/X11R6/man/man1/wmclock.1x
