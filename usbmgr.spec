Summary:	USB Manager
Summary(pl):	Menad¿er urz±dzeñ USB
Name:		usbmgr
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.wondernetworkresources.com/staff/shuu/linux/usbmgr/%{name}-%{version}.tar.gz
#development:	http://www.wondernetworkresources.com/staff/shuu/linux/usbmgr/0.4.8/usbmgr-0.4.8.tar.gz
URL:		http://www.wondernetworkresources.com/staff/shuu/linux/usbmgr/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbin	/sbin

%description
The usbmgr is user-mode daemon which loads and unloads some kernel
modules according to the configuration and executes some scripts to
setup USB devices.
	     
%description -l pl
usbmgr jest demonem ³aduj±cym i usuwaj±cym modu³y kernela w zale¿no¶ci
od konfiguracji oraz uruchamiaj±cy skrypty konfiguruj±ce urz±dzenia
USB.

%prep
%setup -q

#%patch

%build
#./configure --prefix=%{_prefix}
CC="%{__cc}" %{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/usb,%{_sbindir}}
%{__make} CONF_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/usb BIN_DIR=$RPM_BUILD_ROOT%{_sbindir} install

gzip -9nf CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(640,root,root) %{_sysconfdir}/usb/*
%attr(755,root,root) %{_sbindir}/usbmgr
%attr(755,root,root) %{_sbindir}/dump_usbdev
