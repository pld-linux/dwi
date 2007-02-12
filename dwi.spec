Summary:	Data With Interaction
Summary(pl.UTF-8):   Data With Interaction - biblioteka do pracy z danymi
Name:		dwi
Version:	0.6.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/dwi/%{name}-%{version}.tar.gz
# Source0-md5:	30fa12e13238b80151538513ff189bdc
Patch0:		%{name}-libpq.patch
Patch1:		%{name}-libxml2.patch
Patch2:		%{name}-qof.patch
Patch3:		%{name}-link.patch
URL:		http://dwi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libdbi-devel
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	unixODBC-devel
#BuildRequires: old qof-devel - forget for now
BuildConflicts:	libiodbc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DWI is a fairly simple environment for quickly creating data-driven
applications, that is, graphical applications that manipulate and show
info from a database.

%description -l pl.UTF-8
DWI to w miarę proste środowisko do szybkiego tworzenia aplikacji
pracujących z danymi, czyli graficznych aplikacji obrabiających i
wyświetlających informacje z bazy danych.

%package devel
Summary:	Header files for DWI library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki DWI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0
Requires:	libxml2-devel >= 2.0.0

%description devel
Header files for DWI library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki DWI.

%package static
Summary:	Static DWI library
Summary(pl.UTF-8):   Statyczna biblioteka DWI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static DWI library.

%description static -l pl.UTF-8
Statyczna biblioteka DWI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libdwi-db-*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/dwi-run
%attr(755,root,root) %{_libdir}/libdwi.so.*.*.*
%attr(755,root,root) %{_libdir}/libdwi-parse.so.*.*.*
#%attr(755,root,root) %{_libdir}/libdwi-qof.so.*.*.*
%attr(755,root,root) %{_libdir}/libdwi-dbdrivers.so.*.*.*
%attr(755,root,root) %{_libdir}/libdwi-gtk.so.*.*.*
# drivers
%attr(755,root,root) %{_libdir}/libdwi-db-libdbi.so
%attr(755,root,root) %{_libdir}/libdwi-db-libpg.so
%attr(755,root,root) %{_libdir}/libdwi-db-odbc.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdwi.so
%attr(755,root,root) %{_libdir}/libdwi-parse.so
#%attr(755,root,root) %{_libdir}/libdwi-qof.so
%attr(755,root,root) %{_libdir}/libdwi-dbdrivers.so
%attr(755,root,root) %{_libdir}/libdwi-gtk.so
%{_libdir}/libdwi.la
%{_libdir}/libdwi-parse.la
#%{_libdir}/libdwi-qof.la
%{_libdir}/libdwi-dbdrivers.la
%{_libdir}/libdwi-gtk.la
%{_includedir}/dwi
%{_pkgconfigdir}/dwi-0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdwi.a
%{_libdir}/libdwi-parse.a
#%{_libdir}/libdwi-qof.a
%{_libdir}/libdwi-dbdrivers.a
%{_libdir}/libdwi-gtk.a
