Summary:	Linux Terminal Server Project - Kernel for terminals
Summary(pl):	J±dro dla terminali z Linux Terminal Server Project
Name:		ltsp_kernel
Version:	3.0.15
Release:	1
License:	GPL
Group:		Applications/Network
Source0:	http://dl.sourceforge.net/ltsp/%{name}-%{version}-i386.tgz
# Source0-md5:	adbf0a966b0e97d9698616c65df7fc9a
URL:		http://www.ltsp.org/
Requires:	ltsp_core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp
%define		no_install_post_strip	1

%description
This package contains Linux kernel for LTSP terminals.

%description -l pl
Ten pakiet zawiera j±dro Linuksa dla terminali LTSP.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}/lib

cp vmlinuz-2.4.24-ltsp-4 $RPM_BUILD_ROOT%{_ltspdir}

cd i386
cp -r lib/* $RPM_BUILD_ROOT%{_ltspdir}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_ltspdir}/vmlinuz-2.4.24-ltsp-4
%{_ltspdir}/lib/modules
