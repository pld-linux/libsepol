Summary:	SELinux binary policy manipulation library
Summary(pl):	Biblioteka do obr�bki polityk SELinuksa w postaci binarnej
Name:		libsepol
Version:	1.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	54e2052452d5247b944252652ed94594
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

%description -l pl
Security-enhanced Linux jest prototypem j�dra Linuksa i wielu
aplikacji u�ytkowych o funkcjach podwy�szonego bezpiecze�stwa.
Zaprojektowany jest tak, aby w prosty spos�b ukaza� znaczenie
obowi�zkowej kontroli dost�pu dla spo�eczno�ci linuksowej. Ukazuje
r�wnie� jak tak� kontrol� mo�na doda� do istniej�cego systemu typu
Linux. J�dro SELinux zawiera nowe sk�adniki architektury pierwotnie
opracowane w celu ulepszenia bezpiecze�stwa systemu operacyjnego
Flask. Te elementy zapewniaj� og�lne wsparcie we wdra�aniu wielu typ�w
polityk obowi�zkowej kontroli dost�pu, w��czaj�c te wzorowane na: Type
Enforcement (TE), kontroli dost�pu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

libsepol dostarcza API do obr�bki polityk SELinuksa w postaci
binarnej. Jest u�ywane przez checkpolicy (kompilator polityk) i
podobne narz�dzia, a tak�e przez programy w rodzaju load_policy,
potrzebne do wykonywania okre�lonych przekszta�ce� na binarnych
politykach, takich jak dostosowywanie logicznych ustawie� polityki.

%package devel
Summary:	Header files used to build policy manipulation tools
Summary(pl):	Pliki nag��wkowe do budowania narz�dzi obrabiaj�cych polityk�
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed for developing
applications that manipulate binary policies.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe potrzebne do tworzenia aplikacji
obrabiaj�cych binarne polityki.

%package static
Summary:	Static version of libsepol library
Summary(pl):	Statyczna wersja biblioteki libsepol
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libsepol library.

%description static -l pl
Statyczna wersja biblioteki libsepol.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
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
