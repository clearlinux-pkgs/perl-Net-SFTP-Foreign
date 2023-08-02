#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-SFTP-Foreign
Version  : 1.93
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-SFTP-Foreign-1.93.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-SFTP-Foreign-1.93.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-sftp-foreign-perl/libnet-sftp-foreign-perl_1.89+dfsg-1.debian.tar.xz
Summary  : 'Secure File Transfer Protocol client'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Net-SFTP-Foreign-license = %{version}-%{release}
Requires: perl-Net-SFTP-Foreign-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Net::SFTP::Foreign
===================
Net::SFTP::Foreign implements an SFTP client in Perl using the native
SSH client application to establish the connection to the remote host.

%package dev
Summary: dev components for the perl-Net-SFTP-Foreign package.
Group: Development
Provides: perl-Net-SFTP-Foreign-devel = %{version}-%{release}
Requires: perl-Net-SFTP-Foreign = %{version}-%{release}

%description dev
dev components for the perl-Net-SFTP-Foreign package.


%package license
Summary: license components for the perl-Net-SFTP-Foreign package.
Group: Default

%description license
license components for the perl-Net-SFTP-Foreign package.


%package perl
Summary: perl components for the perl-Net-SFTP-Foreign package.
Group: Default
Requires: perl-Net-SFTP-Foreign = %{version}-%{release}

%description perl
perl components for the perl-Net-SFTP-Foreign package.


%prep
%setup -q -n Net-SFTP-Foreign-1.93
cd %{_builddir}
tar xf %{_sourcedir}/libnet-sftp-foreign-perl_1.89+dfsg-1.debian.tar.xz
cd %{_builddir}/Net-SFTP-Foreign-1.93
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-SFTP-Foreign-1.93/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-SFTP-Foreign
cp %{_builddir}/Net-SFTP-Foreign-1.93/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-SFTP-Foreign/2e3c27fee4f8b7c606df7f86eb519196f444acca
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::SFTP::Foreign.3
/usr/share/man/man3/Net::SFTP::Foreign::Attributes.3
/usr/share/man/man3/Net::SFTP::Foreign::Attributes::Compat.3
/usr/share/man/man3/Net::SFTP::Foreign::Buffer.3
/usr/share/man/man3/Net::SFTP::Foreign::Compat.3
/usr/share/man/man3/Net::SFTP::Foreign::Constants.3
/usr/share/man/man3/Net::SFTP::Foreign::Local.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-SFTP-Foreign/2e3c27fee4f8b7c606df7f86eb519196f444acca

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
