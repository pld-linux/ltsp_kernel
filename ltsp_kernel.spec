#
# TODO:
# desc, cleanups
#
Summary:	Linux Terminal Server Project - Kernel
Summary(pl):	Rdzeñ Linux Terminal Server Project
Name:		ltsp_kernel
Version:	3.0.5
Release:	0.1
License:	GPL
Group:		Applications/Network
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/ltsp/%{name}-%{version}-i386.tgz
URL:		http://www.ltsp.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_ltspdir	/home/services/ltsp
%define no_install_post_strip	1

%description
Kernel package

%description -l pl

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}/lib/

cp vmlinuz-2.4.19-ltsp-1 $RPM_BUILD_ROOT%{_ltspdir}

cd i386
cp -r lib/* $RPM_BUILD_ROOT%{_ltspdir}/lib/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(600,root,root,700)
%doc README
%{_ltspdir}/lib/
%{_ltspdir}/vmlinuz-2.4.19-ltsp-1
