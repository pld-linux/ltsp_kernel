%define		_arch	i386
%define		_pver	4.1

Summary:	Linux Terminal Server Project - Kernel for terminals
Summary(pl.UTF-8):	Jądro dla terminali z Linux Terminal Server Project
Name:		ltsp_kernel
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-modules-2.6.9-1.5-0-%{_arch}.tgz
# Source1-md5:	1d28770269edff570e93492716bf5221
Source2:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-kernel-2.6.9-1.5-0-%{_arch}.tgz
# Source2-md5:	6267bcf4c48bec32a8923531884f9118
URL:		http://www.ltsp.org/
Requires:	ltsp_core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp

%description
This package contains Linux kernel for LTSP terminals.

%description -l pl.UTF-8
Ten pakiet zawiera jądro Linuksa dla terminali LTSP.

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}{/lib,/2.6.9-ltsp-3}
tar zxf %{SOURCE1}
tar zxf %{SOURCE2}
install vmlinuz-2.6.9-ltsp-3 $RPM_BUILD_ROOT%{_ltspdir}
cp -r i386/lib/* $RPM_BUILD_ROOT%{_ltspdir}/lib
cp -r 2.6.9-ltsp-3/* $RPM_BUILD_ROOT%{_ltspdir}/2.6.9-ltsp-3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%{_ltspdir}/vmlinuz-2.6.9-ltsp-3
%{_ltspdir}/2.6.9-ltsp-3
%{_ltspdir}/lib/modules
