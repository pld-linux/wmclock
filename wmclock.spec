Summary:	The AfterStep Clock for Window Maker
Summary(pl):	Zegarek przeniesiony z AfterStep do WindowMakera
Name:		wmclock
Version:	1.0.12.2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.ntrnet.net/~jmknoble/WindowMaker/wmclock/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-pl_xpm.patch
Icon:		wmclock.gif
URL:		http://www.pobox.com/~jmknoble/WindowMaker/wmclock/
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
%setup -q
%patch -p1

%build
#rm -f asclock.o asclock clk.xpm weekday.xpm month.xpm
./configure --lang english
#ln -sf xpm/color.xpm clk.xpm
#ln -sf lang.english/month.xpm month.xpm 
#ln -sf lang.english/weekday.xpm weekday.xpm

xmkmf -a
%{__make} CCOPTIONS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets \
	$RPM_BUILD_ROOT%{_pixmapsdir}/{br,cz,da,de,es,fr,hu,id,it,nl,no,pl,pt,ru,si,sv,uk}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__make} install.man DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install lang.breton/*		$RPM_BUILD_ROOT%{_pixmapsdir}/br
install lang.czech/*		$RPM_BUILD_ROOT%{_pixmapsdir}/cz
install lang.danish/*		$RPM_BUILD_ROOT%{_pixmapsdir}/da
install lang.german/*		$RPM_BUILD_ROOT%{_pixmapsdir}/de
install lang.spanish/*		$RPM_BUILD_ROOT%{_pixmapsdir}/es
install lang.french/*		$RPM_BUILD_ROOT%{_pixmapsdir}/fr
# install lang.french2/*	$RPM_BUILD_ROOT%{_pixmapsdir}/fr
install lang.hungarian/*	$RPM_BUILD_ROOT%{_pixmapsdir}/hu
install lang.indonesian/*	$RPM_BUILD_ROOT%{_pixmapsdir}/id
install lang.italian/*		$RPM_BUILD_ROOT%{_pixmapsdir}/it
install lang.dutch/*		$RPM_BUILD_ROOT%{_pixmapsdir}/nl
install lang.norwegian/*	$RPM_BUILD_ROOT%{_pixmapsdir}/no
install lang.polish/*		$RPM_BUILD_ROOT%{_pixmapsdir}/pl
install lang.portuguese/*	$RPM_BUILD_ROOT%{_pixmapsdir}/pt
install lang.russian/*		$RPM_BUILD_ROOT%{_pixmapsdir}/ru
install lang.slovene/*		$RPM_BUILD_ROOT%{_pixmapsdir}/si
install lang.swedish/*		$RPM_BUILD_ROOT%{_pixmapsdir}/sv
install lang.ukrainian/*	$RPM_BUILD_ROOT%{_pixmapsdir}/uk

gzip -9nf README COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/wmclock
%{_mandir}/man1/wmclock.1x*

%{_applnkdir}/DockApplets/wmclock.desktop
%lang(br) %{_pixmapsdir}/br
%lang(cz) %{_pixmapsdir}/cz
%lang(da) %{_pixmapsdir}/da
%lang(de) %{_pixmapsdir}/de
%lang(es) %{_pixmapsdir}/es
%lang(fr) %{_pixmapsdir}/fr
%lang(hu) %{_pixmapsdir}/hu
%lang(id) %{_pixmapsdir}/id
%lang(it) %{_pixmapsdir}/it
%lang(nl) %{_pixmapsdir}/nl
%lang(no) %{_pixmapsdir}/no
%lang(pl) %{_pixmapsdir}/pl
%lang(pt) %{_pixmapsdir}/pt
%lang(ru) %{_pixmapsdir}/ru
%lang(si) %{_pixmapsdir}/si
%lang(sv) %{_pixmapsdir}/sv
%lang(uk) %{_pixmapsdir}/uk
