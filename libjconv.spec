Summary:	Japanese Code Conversion Library
Name:		libjconv
Version:	2.8.1
Release:	%mkrel 4
License:	GPL
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.bz2
Requires:	glibc >= 2.1.0

%description
This package provide Japanese Code Conversion capability based on iconv.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS -Wall -O3 -fPIC -DHAVE_CODESET"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 libjconv.so -D $RPM_BUILD_ROOT%{_libdir}/libjconv.so
install -m644 libjconv.a -D $RPM_BUILD_ROOT%{_libdir}/libjconv.a
install -m755 jconv -D $RPM_BUILD_ROOT%{_bindir}/jconv
install -m644 jconv.h -D $RPM_BUILD_ROOT%{_includedir}/jconv.h
install -m644 default.conf -D $RPM_BUILD_ROOT%{_sysconfdir}/libjconv/default.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%{_libdir}/libjconv.so*
%{_libdir}/libjconv.a
%{_bindir}/jconv
%{_includedir}/jconv.h
%dir %{_sysconfdir}/libjconv
%config(noreplace) %{_sysconfdir}/libjconv/*
