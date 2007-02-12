Summary:	USB Manager
Summary(pl.UTF-8):	Zarządca urządzeń USB
Name:		usbmgr
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.dotaster.com/~shuu/linux/usbmgr/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	070c75f83f2bc84750a87fa685a89031
URL:		http://www.dotaster.com/~shuu/linux/usbmgr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbin	/sbin

%description
The usbmgr is user-mode daemon which loads and unloads some kernel
modules according to the configuration and executes some scripts to
setup USB devices.

%description -l pl.UTF-8
usbmgr jest demonem ładującym i usuwającym moduły jądra w zależności
od konfiguracji oraz uruchamiający skrypty konfigurujące urządzenia
USB.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%lang(ja) %doc README.eucJP
%dir %{_sysconfdir}/usbmgr
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/usbmgr/usbmgr.conf
%attr(755,root,root) %{_sysconfdir}/usbmgr/network
%attr(755,root,root) %{_sbindir}/dump_usbdev
%attr(755,root,root) %{_sbindir}/update_usbdb
%attr(755,root,root) %{_sbindir}/usbmgr
