%define debug_package %{nil}

Summary:	Hawaii widget styles
Name:		hawaii-widget-styles
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.hawaiios.org
Source0:	https://github.com/hawaii-desktop/hawaii-widget-styles/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	hawaii-widget-styles.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Quick) >= 5.5

%track
prog %{name} = {
	url = https://github.com/hawaii-desktop/hawaii-widget-styles/releases/download/v%{version}/
	regex = "v(__VER__)\.tar\.xz"
	version = %{version}
}

%description
Hawaii widget styles.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_libdir}/qml/QtQuick/Controls/Styles/Aluminium
%{_datadir}/color-schemes/Hawaii*.colors
