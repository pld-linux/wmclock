Summary:	The AfterStep Clock for Window Maker
Summary(pl):	Zegarek przeniesiony z AfterStep do WindowMakera
Name:		wmclock
Version:	1.0
Release:	2
Copyright:	Freeware
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.windowmaker.org/ftp/pub/contrib/srcs/apps/asclock.tgz
Source1:	%{name}.desktop
Icon:		wmclock.gif
URL:		http://afterstep.edoc.com/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
This is a Window Maker enhanced asclock (i.e. a patch to allow asclock
to be docked on Window Maker has been included). In this package,
asclock was renamed to wmclock to avoid clashes with an AfterStep
installation on the system.

%description -l pl
wmclock to asclock z dodan± mo¿liwo¶ci± u¿ywania go w WindowMakerze.

%prep
%setup -q -n asclock

%build
rm -f asclock.o asclock clk.xpm weekday.xpm month.xpm
ln -sf xpm/color.xpm clk.xpm
ln -sf english/month.xpm month.xpm 
ln -sf english/weekday.xpm weekday.xpm

xmkmf -a
%{__make} CFLAGS="%{rpmcflags} -I%{_includedir}" \
	CXXFLAGS="%{rpmcflags} -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install asclock $RPM_BUILD_ROOT%{_bindir}/wmclock
install asclock.man $RPM_BUILD_ROOT%{_mandir}/man1/wmclock.1x
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/wmclock
%{_mandir}/man1/wmclock.1x*

%{_applnkdir}/DockApplets/wmclock.desktop
