#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAB4655A126D292E4 (coreteam@netfilter.org)
#
Name     : libnetfilter_conntrack
Version  : 1.0.6
Release  : 16
URL      : https://www.netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-1.0.6.tar.bz2
Source0  : https://www.netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-1.0.6.tar.bz2
Source99 : https://www.netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-1.0.6.tar.bz2.sig
Summary  : netfilter userspace conntrack access library
Group    : Development/Tools
License  : GPL-2.0
Requires: libnetfilter_conntrack-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32libmnl)
BuildRequires : pkgconfig(32libnfnetlink)
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnfnetlink)

%description
libnetfilter_conntrack - userspace library for the connection tracking system
(C) 2005-2011 Pablo Neira Ayuso <pablo@netfilter.org>
=============================================================================

%package dev
Summary: dev components for the libnetfilter_conntrack package.
Group: Development
Requires: libnetfilter_conntrack-lib
Provides: libnetfilter_conntrack-devel

%description dev
dev components for the libnetfilter_conntrack package.


%package dev32
Summary: dev32 components for the libnetfilter_conntrack package.
Group: Default
Requires: libnetfilter_conntrack-lib32
Requires: libnetfilter_conntrack-dev

%description dev32
dev32 components for the libnetfilter_conntrack package.


%package lib
Summary: lib components for the libnetfilter_conntrack package.
Group: Libraries

%description lib
lib components for the libnetfilter_conntrack package.


%package lib32
Summary: lib32 components for the libnetfilter_conntrack package.
Group: Default

%description lib32
lib32 components for the libnetfilter_conntrack package.


%prep
%setup -q -n libnetfilter_conntrack-1.0.6
pushd ..
cp -a libnetfilter_conntrack-1.0.6 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492120044
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492120044
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_dccp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_icmp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_ipv4.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_ipv6.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_sctp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_tcp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_udp.h
/usr/include/libnetfilter_conntrack/linux_nfnetlink_conntrack.h
/usr/lib64/libnetfilter_conntrack.so
/usr/lib64/pkgconfig/libnetfilter_conntrack.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libnetfilter_conntrack.so
/usr/lib32/pkgconfig/32libnetfilter_conntrack.pc
/usr/lib32/pkgconfig/libnetfilter_conntrack.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnetfilter_conntrack.so.3
/usr/lib64/libnetfilter_conntrack.so.3.6.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnetfilter_conntrack.so.3
/usr/lib32/libnetfilter_conntrack.so.3.6.0
