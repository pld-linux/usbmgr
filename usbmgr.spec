Summary:	USB Manager
Summary(pl):	Menad¿er urz±dzeñ USB
Name:		usbmgr
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	%{name}-%{version}.tar.gz
#Patch0:	
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbin	/sbin

%description
Applications/Communications

%description -l pl

%prep
%setup -q

#%patch

%build
#./configure --prefix=%{_prefix}
CC="%{__cc}" make OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/usb,%{_sbin}}
%{__make} CONF_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/usb BIN_DIR=$RPM_BUILD_ROOT%{_sbin} install

gzip -9nf CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(640,root,root) %{_sysconfdir}/usb/*
%attr(755,root,root) %{_sbin}/usbmgr
%attr(755,root,root) %{_sbin}/dump_usbdev
