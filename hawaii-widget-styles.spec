%define debug_package %{nil}

Summary:	Hawaii widget styles
Name:		hawaii-widget-styles
Version:	0.5.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://hawaii-desktop.github.io
Source0:	https://github.com/hawaii-desktop/%{name}/archive/v%{version}.tar.gz
Source1:	hawaii-widget-styles.rpmlintrc
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Quick) >= 5.5

%track
prog %{name} = {
	url = https://github.com/hawaii-desktop/%{name}/archive/
	regex = "v(__VER__)\.tar\.gz"
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
