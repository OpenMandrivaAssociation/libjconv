Summary:	Japanese Code Conversion Library
Name:		libjconv
Version:	2.8.1
Release:	9
License:	GPL
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.bz2
Requires:	glibc >= 2.1.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.1-8mdv2011.0
+ Revision: 620145
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.8.1-7mdv2010.0
+ Revision: 429780
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2.8.1-6mdv2009.0
+ Revision: 240977
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 10 2007 Funda Wang <fwang@mandriva.org> 2.8.1-4mdv2008.0
+ Revision: 50843
- Rebuild for new era
- Import libjconv



* Thu Jan 13 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.8.1-3mdk
- fix unpackaged files
- compile with $RPM_OPT_FLAGS
- wipe out buildroot at the beginning of %%install
- drop useless prefix tag
- cosmetics

* Thu Jun 12 2003 Marcel Pol <mpol@gmx.net> 2.8.1-2mdk
- rebuild for rpm 4.2

* Sat Nov 17 2001 DU Xiaoming <dxiaoming@mandrakesoft.com> 2.8.1-1mdk
- First version for Mandrake Linux
