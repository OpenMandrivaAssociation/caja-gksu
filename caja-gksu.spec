%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname    mate-file-manager-gksu
Summary: Run command as root in a specified folder
Name:    caja-gksu
Version: 1.6.0
Release: 1
Group:   File tools
License: GPLv2+
URL:     http://mate-desktop.org
Source0: http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz
Patch0:  mate-file-manager-gksu-1.6.0-mga-fix-configure_ac-script.patch

BuildRequires: intltool
BuildRequires: mate-common >= 1.6.0
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libcaja-extension) >= 1.6.0
BuildRequires: pkgconfig(libgksu2)

Provides:      caja-open-gksu = %{version}-%{release}
Provides:      %{oname}-gksu = %{version}-%{release}

%description
This is a proof-of-concept Caja extension which allows you to run
a command as root in arbitrary local folders.

%prep
%setup -q -n %{oname}-%{version}
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
   --disable-static

%make

%install
%makeinstall_std

#we don't want these
rm -f %{buildroot}%{_libdir}/caja/extensions-2.0/*.la

%find_lang %{oname} --with-gnome --all-name

%files -f %{oname}.lang
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so

