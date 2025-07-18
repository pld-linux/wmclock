Summary:	The AfterStep Clock for Window Maker
Summary(es.UTF-8):	Reloj para el "dock" de Winow Maker
Summary(pl.UTF-8):	Zegarek przeniesiony z AfterStep do WindowMakera
Summary(pt_BR.UTF-8):	Relógio para o "dock" do Window Maker
Name:		wmclock
Version:	1.0.12.2
Release:	9
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.jmknoble.net/WindowMaker/wmclock/%{name}-%{version}.tar.gz
# Source0-md5:	97f6e82f55f216ba724859d4652586b4
Source1:	%{name}.desktop
Patch0:		%{name}-pl_xpm.patch
URL:		http://www.jmknoble.net/WindowMaker/wmclock/
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmclock is an applet which displays the date and time in a dockable
tile in the same style as the clock from the NEXTSTEP(tm) operating
system. Wmclock is specially designed for the Window Maker window
manager, by Alfredo Kojima, and features multiple language support,
twenty-four-hour and twelve-hour (am/pm) time display, and,
optionally, can run a user-specified program on a mouse click. Wmclock
is derived from asclock, a similar clock for the AfterStep window
manager.

%description -l pl.UTF-8
Wmclock jest apletem, który wyświetla czas i datę w dock'u w ten sam
sposób jak zegar z NEXTSTEP(tm). Wmclock jest specjalnie
zaprojektowany dla Window Maker'a przez Alfredo Kojima; wspiera wiele
języków, 24- i 12-godzinne (am/pm) wyświetlanie czasu oraz opcjonalnie
może pozwalać na uruchamianie określonego przez użytkownika programu
po kliknięciu myszką. Wmclock został przejęty z asclock'a - podobnego
zegara z AfterStep'a poprzez odpowiednie patche.

%description -l pt_BR.UTF-8
O wmclock é um aplicativo que mostra a data e a hora no "dock" do
Window Maker no mesmo estilo do relógio no sistema operacional
NEXTSTEP(r). Foi projetado especialmente para o gerenciador de janelas
Window Maker, do Alfredo Kojima, e tem várias características: suporte
a várias línguas, mostra a hora em formato 24 horas e 12 horas (am/pm)
e, opcionalmente, pode executar um programa especificado pelo usuário
quando for clicado. É derivado do asclock, um relógio similar para o
gerente de janelas AfterStep.

%description -l es.UTF-8
Reloj para el "dock" de Winow Maker

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--lang english

xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CCOPTIONS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/{br,cs,da,de,es,fr,hu,id,it,nl,no,pl,pt,ru,sl,sv,uk}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1x

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

install lang.breton/*		$RPM_BUILD_ROOT%{_pixmapsdir}/br
install lang.czech/*		$RPM_BUILD_ROOT%{_pixmapsdir}/cs
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
install lang.slovene/*		$RPM_BUILD_ROOT%{_pixmapsdir}/sl
install lang.swedish/*		$RPM_BUILD_ROOT%{_pixmapsdir}/sv
install lang.ukrainian/*	$RPM_BUILD_ROOT%{_pixmapsdir}/uk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/wmclock
%{_mandir}/man1/wmclock.1x*

%{_desktopdir}/docklets/wmclock.desktop
%lang(br) %{_pixmapsdir}/br
%lang(cs) %{_pixmapsdir}/cs
%lang(da) %{_pixmapsdir}/da
%lang(de) %{_pixmapsdir}/de
%lang(es) %{_pixmapsdir}/es
%lang(fr) %{_pixmapsdir}/fr
%lang(hu) %{_pixmapsdir}/hu
%lang(id) %{_pixmapsdir}/id
%lang(it) %{_pixmapsdir}/it
%lang(nl) %{_pixmapsdir}/nl
%lang(nb) %{_pixmapsdir}/no
%lang(pl) %{_pixmapsdir}/pl
%lang(pt) %{_pixmapsdir}/pt
%lang(ru) %{_pixmapsdir}/ru
%lang(sl) %{_pixmapsdir}/sl
%lang(sv) %{_pixmapsdir}/sv
%lang(uk) %{_pixmapsdir}/uk
