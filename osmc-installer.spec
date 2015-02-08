%define osmc_name qt_host_installer
Summary:	OSMC Installer for Linux
Name:		osmc-installer
Version:	1
Release:	42.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	src.tar.gz
# Source0-md5:	b475aa2540255265f682a14cf16dbc72
Patch0:		desktop.patch
URL:		https://github.com/samnazarko/osmc
BuildRequires:	QtCore-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
Requires:	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSMC Installer allows you to install OSMC on a variety of devices.

%prep
%setup -qc
%patch0 -p1

%build
cd src
qmake-qt4
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install -p src/qt_host_installer $RPM_BUILD_ROOT%{_bindir}/qt_host_installer
install -p src/osmcinstaller $RPM_BUILD_ROOT%{_bindir}/osmcinstaller

desktop-file-install --dir=$RPM_BUILD_ROOT%{_desktopdir} src/osmcinstaller.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/osmcinstaller.desktop

# icon image
cp -p src/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/osmcinstaller.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/osmcinstaller
%attr(755,root,root) %{_bindir}/qt_host_installer
%{_desktopdir}/osmcinstaller.desktop
%{_pixmapsdir}/osmcinstaller.png
