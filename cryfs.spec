Name: cryfs
Version: 0.10.2
Release: 1%{?dist}
Summary: Cryptographic filesystem for the cloud
License: LGPLv3
Group: Security
Source:  %{name}-%{version}.tar.gz
# Source: https://github.com/cryfs/cryfs
URL: https://www.cryfs.org/


%if 0%{?rhel} == 7
BuildRequires: cmake3
BuildRequires: devtoolset-7-gcc-c++
%else
%if 0%{?fedora} >= 28 || 0%{?rhel} == 8
BuildRequires: gcc-c++
BuildRequires: cmake
%endif # fedora
%endif # rhel
BuildRequires: make
BuildRequires: libcurl-devel
%if 0%{?rhel} == 7
BuildRequires: boost166-devel
BuildRequires: boost166-static
BuildRequires: cryptopp-devel
%else
%if 0%{?fedora} >= 28 || 0%{?rhel} == 8
BuildRequires: boost-devel
BuildRequires: boost-static
%endif # fedora
%endif # rhel
BuildRequires: cryptopp-devel
BuildRequires: openssl-devel
BuildRequires: fuse-devel
BuildRequires: python


%description
CryFS encrypts your files, so you can safely store them anywhere.
It works well together with cloud services like Dropbox, iCloud, OneDrive
and others.

%define debug_package %{nil}

%prep
%setup -qn %{name}-%{version}

%build
mkdir cmake && cd cmake
%if 0%{?rhel} == 7
scl enable devtoolset-7 -- cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=off -DCRYFS_UPDATE_CHECKS=off -DBOOST_ROOT=/usr/include/boost
%else
%if 0%{?fedora} >=28 || 0%{?rhel} > 7
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=off -DCRYFS_UPDATE_CHECKS=off
%endif # fedora
%endif # rhel
%{__make}


%install
%make_install -C cmake

%files
%{_bindir}/cryfs*
%{_mandir}/man1/cryfs.1.gz

%changelog
* Tue Jul 30 2019 Nick Cross <fedora@goots.org>
- 0.10.2

* Sun Jun  9 2019 Alex <redhat@att.org.ru>
- 0.10.2

* Thu Apr  4 2019 Alex <redhat@att.org.ru>
- 0.10.1

* Sat Feb  9 2019 Alex <redhat@att.org.ru>
- 0.10.0

* Tue Jan 29 2019 Alex <redhat@att.org.ru>
- 0.10-rc3

* Tue Jan 22 2019 Alex <redhat@att.org.ru>
- 0.10-rc2

* Tue Apr 03 2018 Jan Pazdziora <jpazdziora@redhat.com> 0.9.9-1
- Packaging 0.9.9.
