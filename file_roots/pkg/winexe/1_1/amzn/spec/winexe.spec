%if ( "0%{?dist}" == "0.amzn1" )
%global with_explicit_python27 1
%global pybasever 2.7
%global __python_ver 27
%else

%if ! (0%{?rhel} >= 6 || 0%{?fedora} > 12)
%global with_python26 1
%define pybasever 2.6
%define __python_ver 26
%endif

%endif


Name: winexe
Version: 1.1
Release: b787d2.1%{?dist}
Summary: Remote Windows command executor.


Group: Applications/System
License: GPLv3
URL: http://sourceforge.net/projects/winexe/
Source0: %{name}-%{version}.tar.gz
Patch0:  %{name}-%{version}-gcrypt.patch

AutoReqProv: no
BuildRequires: gcc
BuildRequires: perl
BuildRequires: mingw-binutils-generic
BuildRequires: mingw-filesystem-base
BuildRequires: mingw32-binutils
BuildRequires: mingw32-cpp
BuildRequires: mingw32-crt
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-headers
BuildRequires: mingw64-binutils
BuildRequires: mingw64-cpp
BuildRequires: mingw64-crt
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-headers
BuildRequires: libcom_err-devel
BuildRequires: popt-devel
BuildRequires: zlib-devel
BuildRequires: zlib-static
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git
BuildRequires: gnutls-devel
BuildRequires: libacl-devel
BuildRequires: openldap-devel
Requires: samba4-libs >= 4.0.0

BuildRequires: python%{?__python_ver}-devel
%if (0%{?rhel} >= 7 || "0%{?dist}" == "0.amzn1")
Requires: glibc >= 2.17 
%endif

%if (0%{?rhel} == 6)
Requires: glibc >= 2.12
%endif

%if (0%{?rhel} == 6 || "0%{?dist}" == "0.amzn1")
BuildRequires: rpm-build
BuildRequires: pkgconfig
BuildRequires: libtalloc-devel
BuildRequires: samba4-devel
%endif

%if ("0%{?dist}" == "0.amzn1")
BuildRequires: libgcrypt
BuildRequires: libgcrypt-devel
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
Winexe remotely executes commands on Windows
NT/2000/XP/2003/Vista/7/2008/8/2012 systems from GNU/Linux.


%prep
cd ../SOURCES
tar -xf winexe-1.1.tar.gz
chmod +x ./generatetarball
./generatetarball


%setup -q
%patch0 -p1


%build
cd source
./waf --samba-dir=../../samba configure build


%install
echo %{buildroot}
rm -rf %{buildroot}
%__install -d %{buildroot}/usr/bin
%__install source/build/winexe %{buildroot}/usr/bin


%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/winexe


%changelog
* Wed Oct 26 2016 SaltStack Packaging Team <packaging@saltstack.com> - 1.1-b787d2-1
- Update to support Redhat 6 and native Amazon Linux

* Sun Feb 14 2016 Randy Thompson <randy@heroictek.com> - 1.1-b787d2
- b787d2a2c4b1abc3653bad10aec943b8efcd7aab from git://git.code.sf.net/p/winexe/winexe-waf
- a6bda1f2bc85779feb9680bc74821da5ccd401c5 from git://git.samba.org/samba.git
