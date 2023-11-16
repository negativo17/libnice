Name:           libnice
Version:        0.1.21
Release:        2%{?dist}
Summary:        GLib ICE implementation
License:        LGPLv2 and MPLv1.1
URL:            https://nice.freedesktop.org/wiki/

Source0:        https://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
#Patch0:         libnice-gupnp-1.2.patch

BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= 2.5.4
BuildRequires:  pkgconfig(gnutls) >= 2.12.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.12.0
BuildRequires:  pkgconfig(gupnp-igd-1.0)

%description
%{name} is an implementation of the IETF draft Interactive Connectivity
Establishment standard (ICE). ICE is useful for applications that want to
establish peer-to-peer UDP data streams. It automates the process of traversing
NATs and provides security against some attacks. Existing standards that use
ICE include the Session Initiation Protocol (SIP) and Jingle, XMPP extension
for audio/video calls.

%package        gstreamer1
Summary:        GStreamer plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gstreamer1
The %{name}-gstreamer1 package contains a gstreamer 1.0 plugin for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -D gtk_doc=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc NEWS README
%license COPYING COPYING.LGPL COPYING.MPL
%{_bindir}/stunbdc
%{_bindir}/stund
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Nice-0.1.typelib

%files gstreamer1
%{_libdir}/gstreamer-1.0/libgstnice.so

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/nice.pc
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Nice-0.1.gir

%changelog
* Thu Nov 16 2023 Simone Caronni <negativo17@gmail.com> - 0.1.21-2
- First build of 0.1.21 for EL9.

* Sun Jan 08 2023 Stefan Becker <chemobejk@gmail.com> - 0.1.21-1
- Update to 0.1.21 (#2158912)
