%define debug_package %{nil}

Summary:	Hawaii widget styles
Name:		hawaii-widget-styles
Version:	0.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	hawaii-widget-styles.rpmlintrc
BuildRequires:	cmake
BuildRequires:	qt5-devel

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Hawaii widget styles.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Aluminium
