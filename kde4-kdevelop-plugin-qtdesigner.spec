%define		orgname		qtdesigner
%define		svnrev		1123908

Summary:	Qt4 Designer plugin for kdevplatform
Summary(pl.UTF-8):	Wtyczka wysyłania dla kdevplatform
Name:		kde4-kdevelop-plugin-qtdesigner
Version:	0.0.1
Release:	0.%{svnrev}.1
License:	GPL
Group:		X11/Development/Tools
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/playground/devtools/kdevelop4-extra-plugins/qtdesigner
Source0:	http://team.pld-linux.org/~vip/%{orgname}-svn-%{svnrev}.tar.bz2
# Source0-md5:	1d791e9684c45738a011bed518f48ca2
URL:		http://www.kdevelop.org/
BuildRequires:	kde4-kdevplatform-devel >= 0.9.97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qti4 Designer kdevelop plugin.

%description -l pl.UTF-8
Wtyczka Qt Designer dla kdevelop.

%prep
%setup -q -n %{orgname}-svn-%{svnrev}

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	../
%{__make}
cd ../

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kdevqtdesigner.so
%{_datadir}/apps/kdevqtdesigner/kdevqtdesigner.rc
%{_datadir}/kde4/services/kdevqtdesigner.desktop
