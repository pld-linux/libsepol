Summary:	SELinux binary policy manipulation library
Summary(pl.UTF-8):	Biblioteka do obróbki polityk SELinuksa w postaci binarnej
Name:		libsepol
Version:	1.16.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	f40612cf2199c4d7157718ce3c2d1688
URL:		http://www.nsa.gov/selinux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing policy
boolean settings.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

libsepol dostarcza API do obróbki polityk SELinuksa w postaci
binarnej. Jest używane przez checkpolicy (kompilator polityk) i
podobne narzędzia, a także przez programy w rodzaju load_policy,
potrzebne do wykonywania określonych przekształceń na binarnych
politykach, takich jak dostosowywanie logicznych ustawień polityki.

%package devel
Summary:	Header files used to build policy manipulation tools
Summary(pl.UTF-8):	Pliki nagłówkowe do budowania narzędzi obrabiających politykę
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed for developing
applications that manipulate binary policies.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia aplikacji
obrabiających binarne polityki.

%package static
Summary:	Static version of libsepol library
Summary(pl.UTF-8):	Statyczna wersja biblioteki libsepol
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libsepol library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libsepol.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	SHLIBDIR=$RPM_BUILD_ROOT/%{_lib}

# make symlink across / absolute
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib} ; echo libsepol.so.*) \
	$RPM_BUILD_ROOT%{_libdir}/libsepol.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) /%{_lib}/libsepol.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libsepol.so
%{_includedir}/sepol
%{_mandir}/man3/*.3*
%{_mandir}/man8/*.8*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsepol.a
