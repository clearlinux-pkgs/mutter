#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mutter
Version  : 43.3
Release  : 139
URL      : https://download.gnome.org/sources/mutter/43/mutter-43.3.tar.xz
Source0  : https://download.gnome.org/sources/mutter/43/mutter-43.3.tar.xz
Summary  : Mutter window manager library
Group    : Development/Tools
License  : GPL-2.0
Requires: mutter-bin = %{version}-%{release}
Requires: mutter-config = %{version}-%{release}
Requires: mutter-data = %{version}-%{release}
Requires: mutter-filemap = %{version}-%{release}
Requires: mutter-lib = %{version}-%{release}
Requires: mutter-libexec = %{version}-%{release}
Requires: mutter-license = %{version}-%{release}
Requires: mutter-locales = %{version}-%{release}
Requires: mutter-man = %{version}-%{release}
Requires: gnome-session
Requires: gnome-settings-daemon
Requires: gsettings-desktop-schemas
Requires: hicolor-icon-theme
Requires: xwayland
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord-dev
BuildRequires : gnome-settings-daemon-dev
BuildRequires : gobject-introspection-dev
BuildRequires : lcms2-dev
BuildRequires : libgudev-dev
BuildRequires : libwacom-dev
BuildRequires : libxcvt
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(cogl-1.0)
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(graphene-gobject-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libwacom)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb-randr)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xkeyboard-config)
BuildRequires : pkgconfig(xtst)
BuildRequires : pkgconfig(xwayland)
BuildRequires : startup-notification-dev
BuildRequires : sysprof-dev
BuildRequires : sysprof-staticdev
BuildRequires : wayland-dev
BuildRequires : xorg-server
BuildRequires : xvfb-run
BuildRequires : xwayland
BuildRequires : zenity
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Intro
=====
In general, the compositor splits the window from the contents of
the window from the shape of the window. In other words, a window
has contents, and the contents of the window have a shape. This is
represented by the actor hierarchy:

%package bin
Summary: bin components for the mutter package.
Group: Binaries
Requires: mutter-data = %{version}-%{release}
Requires: mutter-libexec = %{version}-%{release}
Requires: mutter-config = %{version}-%{release}
Requires: mutter-license = %{version}-%{release}
Requires: mutter-filemap = %{version}-%{release}

%description bin
bin components for the mutter package.


%package config
Summary: config components for the mutter package.
Group: Default

%description config
config components for the mutter package.


%package data
Summary: data components for the mutter package.
Group: Data

%description data
data components for the mutter package.


%package dev
Summary: dev components for the mutter package.
Group: Development
Requires: mutter-lib = %{version}-%{release}
Requires: mutter-bin = %{version}-%{release}
Requires: mutter-data = %{version}-%{release}
Provides: mutter-devel = %{version}-%{release}
Requires: mutter = %{version}-%{release}

%description dev
dev components for the mutter package.


%package filemap
Summary: filemap components for the mutter package.
Group: Default

%description filemap
filemap components for the mutter package.


%package lib
Summary: lib components for the mutter package.
Group: Libraries
Requires: mutter-data = %{version}-%{release}
Requires: mutter-libexec = %{version}-%{release}
Requires: mutter-license = %{version}-%{release}
Requires: mutter-filemap = %{version}-%{release}

%description lib
lib components for the mutter package.


%package libexec
Summary: libexec components for the mutter package.
Group: Default
Requires: mutter-config = %{version}-%{release}
Requires: mutter-license = %{version}-%{release}
Requires: mutter-filemap = %{version}-%{release}

%description libexec
libexec components for the mutter package.


%package license
Summary: license components for the mutter package.
Group: Default

%description license
license components for the mutter package.


%package locales
Summary: locales components for the mutter package.
Group: Default

%description locales
locales components for the mutter package.


%package man
Summary: man components for the mutter package.
Group: Default

%description man
man components for the mutter package.


%package tests
Summary: tests components for the mutter package.
Group: Default
Requires: mutter = %{version}-%{release}

%description tests
tests components for the mutter package.


%prep
%setup -q -n mutter-43.3
cd %{_builddir}/mutter-43.3
pushd ..
cp -a mutter-43.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676473559
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mutter
cp %{_builddir}/mutter-%{version}/COPYING %{buildroot}/usr/share/package-licenses/mutter/4cc77b90af91e615a64ae04893fdffa7939db84c || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang mutter
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/mutter-11/Cally-11.gir
/usr/lib64/mutter-11/Cally-11.typelib
/usr/lib64/mutter-11/Clutter-11.gir
/usr/lib64/mutter-11/Clutter-11.typelib
/usr/lib64/mutter-11/Cogl-11.gir
/usr/lib64/mutter-11/Cogl-11.typelib
/usr/lib64/mutter-11/CoglPango-11.gir
/usr/lib64/mutter-11/CoglPango-11.typelib
/usr/lib64/mutter-11/Meta-11.gir
/usr/lib64/mutter-11/Meta-11.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/mutter
/usr/share/clear/optimized-elf/bin*

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/61-mutter.rules

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/mutter-schemas.convert
/usr/share/applications/mutter.desktop
/usr/share/glib-2.0/schemas/org.gnome.mutter.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
/usr/share/gnome-control-center/keybindings/50-mutter-navigation.xml
/usr/share/gnome-control-center/keybindings/50-mutter-system.xml
/usr/share/gnome-control-center/keybindings/50-mutter-wayland.xml
/usr/share/gnome-control-center/keybindings/50-mutter-windows.xml
/usr/share/mutter-11/tests/dbusmock-templates/colord.py
/usr/share/mutter-11/tests/dbusmock-templates/gsd-color.py
/usr/share/mutter-11/tests/dbusmock-templates/iio-sensors-proxy.py
/usr/share/mutter-11/tests/dbusmock-templates/localed.py
/usr/share/mutter-11/tests/dbusmock-templates/meta-mocks-manager.py
/usr/share/mutter-11/tests/mutter_dbusrunner.py
/usr/share/mutter-11/tests/stacking/always-on-top.metatest
/usr/share/mutter-11/tests/stacking/basic-wayland.metatest
/usr/share/mutter-11/tests/stacking/basic-x11.metatest
/usr/share/mutter-11/tests/stacking/client-resize-respect-constraints.metatest
/usr/share/mutter-11/tests/stacking/client-side-decorated.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-no-default-focus.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-no-input-no-take-focus-parent.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-no-input-no-take-focus-parents.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-no-input-parent-delayed-focus-default-cancelled.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-no-input-parent.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-no-input-parents-queued-default-focus-destroyed.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-no-input-parents.metatest
/usr/share/mutter-11/tests/stacking/closed-transient-only-take-focus-parents.metatest
/usr/share/mutter-11/tests/stacking/closed-transient.metatest
/usr/share/mutter-11/tests/stacking/default-size.metatest
/usr/share/mutter-11/tests/stacking/focus-default-window-globally-active-input.metatest
/usr/share/mutter-11/tests/stacking/fullscreen-maximize.metatest
/usr/share/mutter-11/tests/stacking/map-fixed-size.metatest
/usr/share/mutter-11/tests/stacking/map-on-hotplug.metatest
/usr/share/mutter-11/tests/stacking/minimized.metatest
/usr/share/mutter-11/tests/stacking/mixed-windows.metatest
/usr/share/mutter-11/tests/stacking/modals.metatest
/usr/share/mutter-11/tests/stacking/override-redirect.metatest
/usr/share/mutter-11/tests/stacking/restore-position.metatest
/usr/share/mutter-11/tests/stacking/restore-size.metatest
/usr/share/mutter-11/tests/stacking/set-override-redirect-parent.metatest
/usr/share/mutter-11/tests/stacking/set-parent-exported.metatest
/usr/share/mutter-11/tests/stacking/set-parent.metatest
/usr/share/mutter-11/tests/stacking/unfullscreen-strut-change.metatest
/usr/share/mutter-11/tests/stacking/unmaximize-new-size.metatest
/usr/share/mutter-11/tests/stacking/workspace-basic.metatest
/usr/share/mutter-11/tests/stacking/workspace-test.metatest

%files dev
%defattr(-,root,root,-)
/usr/include/mutter-11/clutter/cally/cally-actor.h
/usr/include/mutter-11/clutter/cally/cally-clone.h
/usr/include/mutter-11/clutter/cally/cally-factory.h
/usr/include/mutter-11/clutter/cally/cally-main.h
/usr/include/mutter-11/clutter/cally/cally-root.h
/usr/include/mutter-11/clutter/cally/cally-stage.h
/usr/include/mutter-11/clutter/cally/cally-text.h
/usr/include/mutter-11/clutter/cally/cally-util.h
/usr/include/mutter-11/clutter/cally/cally.h
/usr/include/mutter-11/clutter/clutter/clutter-action.h
/usr/include/mutter-11/clutter/clutter/clutter-actor-meta.h
/usr/include/mutter-11/clutter/clutter/clutter-actor.h
/usr/include/mutter-11/clutter/clutter/clutter-align-constraint.h
/usr/include/mutter-11/clutter/clutter/clutter-animatable.h
/usr/include/mutter-11/clutter/clutter/clutter-autocleanups.h
/usr/include/mutter-11/clutter/clutter/clutter-backend.h
/usr/include/mutter-11/clutter/clutter/clutter-bin-layout.h
/usr/include/mutter-11/clutter/clutter/clutter-bind-constraint.h
/usr/include/mutter-11/clutter/clutter/clutter-binding-pool.h
/usr/include/mutter-11/clutter/clutter/clutter-blur-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-box-layout.h
/usr/include/mutter-11/clutter/clutter/clutter-brightness-contrast-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-cairo.h
/usr/include/mutter-11/clutter/clutter/clutter-canvas.h
/usr/include/mutter-11/clutter/clutter/clutter-child-meta.h
/usr/include/mutter-11/clutter/clutter/clutter-click-action.h
/usr/include/mutter-11/clutter/clutter/clutter-clone.h
/usr/include/mutter-11/clutter/clutter/clutter-color-state.h
/usr/include/mutter-11/clutter/clutter/clutter-color-static.h
/usr/include/mutter-11/clutter/clutter/clutter-color.h
/usr/include/mutter-11/clutter/clutter/clutter-colorize-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-constraint.h
/usr/include/mutter-11/clutter/clutter/clutter-container.h
/usr/include/mutter-11/clutter/clutter/clutter-content.h
/usr/include/mutter-11/clutter/clutter/clutter-deform-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-deprecated.h
/usr/include/mutter-11/clutter/clutter/clutter-desaturate-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-enum-types.h
/usr/include/mutter-11/clutter/clutter/clutter-enums.h
/usr/include/mutter-11/clutter/clutter/clutter-event.h
/usr/include/mutter-11/clutter/clutter/clutter-fixed-layout.h
/usr/include/mutter-11/clutter/clutter/clutter-flow-layout.h
/usr/include/mutter-11/clutter/clutter/clutter-frame-clock.h
/usr/include/mutter-11/clutter/clutter/clutter-frame.h
/usr/include/mutter-11/clutter/clutter/clutter-gesture-action.h
/usr/include/mutter-11/clutter/clutter/clutter-grab.h
/usr/include/mutter-11/clutter/clutter/clutter-grid-layout.h
/usr/include/mutter-11/clutter/clutter/clutter-image.h
/usr/include/mutter-11/clutter/clutter/clutter-input-device-tool.h
/usr/include/mutter-11/clutter/clutter/clutter-input-device.h
/usr/include/mutter-11/clutter/clutter/clutter-input-focus.h
/usr/include/mutter-11/clutter/clutter/clutter-input-method.h
/usr/include/mutter-11/clutter/clutter/clutter-interval.h
/usr/include/mutter-11/clutter/clutter/clutter-keyframe-transition.h
/usr/include/mutter-11/clutter/clutter/clutter-keymap.h
/usr/include/mutter-11/clutter/clutter/clutter-keysyms.h
/usr/include/mutter-11/clutter/clutter/clutter-layout-manager.h
/usr/include/mutter-11/clutter/clutter/clutter-layout-meta.h
/usr/include/mutter-11/clutter/clutter/clutter-macros.h
/usr/include/mutter-11/clutter/clutter/clutter-main.h
/usr/include/mutter-11/clutter/clutter/clutter-marshal.h
/usr/include/mutter-11/clutter/clutter/clutter-mutter.h
/usr/include/mutter-11/clutter/clutter/clutter-offscreen-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-page-turn-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-paint-context.h
/usr/include/mutter-11/clutter/clutter/clutter-paint-node.h
/usr/include/mutter-11/clutter/clutter/clutter-paint-nodes.h
/usr/include/mutter-11/clutter/clutter/clutter-pan-action.h
/usr/include/mutter-11/clutter/clutter/clutter-path-constraint.h
/usr/include/mutter-11/clutter/clutter/clutter-path.h
/usr/include/mutter-11/clutter/clutter/clutter-pick-context.h
/usr/include/mutter-11/clutter/clutter/clutter-property-transition.h
/usr/include/mutter-11/clutter/clutter/clutter-rotate-action.h
/usr/include/mutter-11/clutter/clutter/clutter-script.h
/usr/include/mutter-11/clutter/clutter/clutter-scriptable.h
/usr/include/mutter-11/clutter/clutter/clutter-scroll-actor.h
/usr/include/mutter-11/clutter/clutter/clutter-seat.h
/usr/include/mutter-11/clutter/clutter/clutter-settings.h
/usr/include/mutter-11/clutter/clutter/clutter-shader-effect.h
/usr/include/mutter-11/clutter/clutter/clutter-shader-types.h
/usr/include/mutter-11/clutter/clutter/clutter-snap-constraint.h
/usr/include/mutter-11/clutter/clutter/clutter-stage-manager.h
/usr/include/mutter-11/clutter/clutter/clutter-stage-view.h
/usr/include/mutter-11/clutter/clutter/clutter-stage.h
/usr/include/mutter-11/clutter/clutter/clutter-swipe-action.h
/usr/include/mutter-11/clutter/clutter/clutter-tap-action.h
/usr/include/mutter-11/clutter/clutter/clutter-text-buffer.h
/usr/include/mutter-11/clutter/clutter/clutter-text.h
/usr/include/mutter-11/clutter/clutter/clutter-texture-content.h
/usr/include/mutter-11/clutter/clutter/clutter-timeline.h
/usr/include/mutter-11/clutter/clutter/clutter-transition-group.h
/usr/include/mutter-11/clutter/clutter/clutter-transition.h
/usr/include/mutter-11/clutter/clutter/clutter-types.h
/usr/include/mutter-11/clutter/clutter/clutter-units.h
/usr/include/mutter-11/clutter/clutter/clutter-virtual-input-device.h
/usr/include/mutter-11/clutter/clutter/clutter-zoom-action.h
/usr/include/mutter-11/clutter/clutter/clutter.h
/usr/include/mutter-11/clutter/clutter/deprecated/clutter-box-layout.h
/usr/include/mutter-11/clutter/clutter/deprecated/clutter-container.h
/usr/include/mutter-11/clutter/clutter/deprecated/clutter-timeline.h
/usr/include/mutter-11/cogl/cogl-pango/cogl-pango.h
/usr/include/mutter-11/cogl/cogl/cogl-atlas-texture.h
/usr/include/mutter-11/cogl/cogl/cogl-attribute-buffer.h
/usr/include/mutter-11/cogl/cogl/cogl-attribute.h
/usr/include/mutter-11/cogl/cogl/cogl-bitmap.h
/usr/include/mutter-11/cogl/cogl/cogl-buffer.h
/usr/include/mutter-11/cogl/cogl/cogl-color.h
/usr/include/mutter-11/cogl/cogl/cogl-context.h
/usr/include/mutter-11/cogl/cogl/cogl-defines.h
/usr/include/mutter-11/cogl/cogl/cogl-depth-state.h
/usr/include/mutter-11/cogl/cogl/cogl-display.h
/usr/include/mutter-11/cogl/cogl/cogl-dma-buf-handle.h
/usr/include/mutter-11/cogl/cogl/cogl-egl-defines.h
/usr/include/mutter-11/cogl/cogl/cogl-egl.h
/usr/include/mutter-11/cogl/cogl/cogl-fence.h
/usr/include/mutter-11/cogl/cogl/cogl-frame-info.h
/usr/include/mutter-11/cogl/cogl/cogl-framebuffer.h
/usr/include/mutter-11/cogl/cogl/cogl-glib-source.h
/usr/include/mutter-11/cogl/cogl/cogl-glx.h
/usr/include/mutter-11/cogl/cogl/cogl-graphene.h
/usr/include/mutter-11/cogl/cogl/cogl-gtype-private.h
/usr/include/mutter-11/cogl/cogl/cogl-index-buffer.h
/usr/include/mutter-11/cogl/cogl/cogl-indices.h
/usr/include/mutter-11/cogl/cogl/cogl-macros.h
/usr/include/mutter-11/cogl/cogl/cogl-matrix-stack.h
/usr/include/mutter-11/cogl/cogl/cogl-meta-texture.h
/usr/include/mutter-11/cogl/cogl/cogl-object.h
/usr/include/mutter-11/cogl/cogl/cogl-offscreen.h
/usr/include/mutter-11/cogl/cogl/cogl-onscreen-template.h
/usr/include/mutter-11/cogl/cogl/cogl-onscreen.h
/usr/include/mutter-11/cogl/cogl/cogl-output.h
/usr/include/mutter-11/cogl/cogl/cogl-pipeline-layer-state.h
/usr/include/mutter-11/cogl/cogl/cogl-pipeline-state.h
/usr/include/mutter-11/cogl/cogl/cogl-pipeline.h
/usr/include/mutter-11/cogl/cogl/cogl-pixel-buffer.h
/usr/include/mutter-11/cogl/cogl/cogl-pixel-format.h
/usr/include/mutter-11/cogl/cogl/cogl-poll.h
/usr/include/mutter-11/cogl/cogl/cogl-primitive-texture.h
/usr/include/mutter-11/cogl/cogl/cogl-primitive.h
/usr/include/mutter-11/cogl/cogl/cogl-renderer.h
/usr/include/mutter-11/cogl/cogl/cogl-scanout.h
/usr/include/mutter-11/cogl/cogl/cogl-snippet.h
/usr/include/mutter-11/cogl/cogl/cogl-sub-texture.h
/usr/include/mutter-11/cogl/cogl/cogl-swap-chain.h
/usr/include/mutter-11/cogl/cogl/cogl-texture-2d-sliced.h
/usr/include/mutter-11/cogl/cogl/cogl-texture-2d.h
/usr/include/mutter-11/cogl/cogl/cogl-texture-pixmap-x11.h
/usr/include/mutter-11/cogl/cogl/cogl-texture.h
/usr/include/mutter-11/cogl/cogl/cogl-trace.h
/usr/include/mutter-11/cogl/cogl/cogl-types.h
/usr/include/mutter-11/cogl/cogl/cogl-xlib-renderer.h
/usr/include/mutter-11/cogl/cogl/cogl-xlib.h
/usr/include/mutter-11/cogl/cogl/cogl.h
/usr/include/mutter-11/cogl/cogl/cogl1-context.h
/usr/include/mutter-11/cogl/cogl/deprecated/cogl-clutter.h
/usr/include/mutter-11/cogl/cogl/deprecated/cogl-shader.h
/usr/include/mutter-11/cogl/cogl/deprecated/cogl-type-casts.h
/usr/include/mutter-11/cogl/cogl/gl-prototypes/cogl-core-functions.h
/usr/include/mutter-11/cogl/cogl/gl-prototypes/cogl-gles2-functions.h
/usr/include/mutter-11/cogl/cogl/gl-prototypes/cogl-glsl-functions.h
/usr/include/mutter-11/cogl/cogl/gl-prototypes/cogl-in-gles-core-functions.h
/usr/include/mutter-11/cogl/cogl/gl-prototypes/cogl-in-gles2-core-functions.h
/usr/include/mutter-11/meta-test/meta-context-test.h
/usr/include/mutter-11/meta/barrier.h
/usr/include/mutter-11/meta/boxes.h
/usr/include/mutter-11/meta/common.h
/usr/include/mutter-11/meta/compositor-mutter.h
/usr/include/mutter-11/meta/compositor.h
/usr/include/mutter-11/meta/display.h
/usr/include/mutter-11/meta/group.h
/usr/include/mutter-11/meta/keybindings.h
/usr/include/mutter-11/meta/main.h
/usr/include/mutter-11/meta/meta-backend.h
/usr/include/mutter-11/meta/meta-background-actor.h
/usr/include/mutter-11/meta/meta-background-content.h
/usr/include/mutter-11/meta/meta-background-group.h
/usr/include/mutter-11/meta/meta-background-image.h
/usr/include/mutter-11/meta/meta-background.h
/usr/include/mutter-11/meta/meta-close-dialog.h
/usr/include/mutter-11/meta/meta-context.h
/usr/include/mutter-11/meta/meta-cursor-tracker.h
/usr/include/mutter-11/meta/meta-dnd.h
/usr/include/mutter-11/meta/meta-enum-types.h
/usr/include/mutter-11/meta/meta-enums.h
/usr/include/mutter-11/meta/meta-idle-monitor.h
/usr/include/mutter-11/meta/meta-inhibit-shortcuts-dialog.h
/usr/include/mutter-11/meta/meta-later.h
/usr/include/mutter-11/meta/meta-launch-context.h
/usr/include/mutter-11/meta/meta-monitor-manager.h
/usr/include/mutter-11/meta/meta-plugin.h
/usr/include/mutter-11/meta/meta-remote-access-controller.h
/usr/include/mutter-11/meta/meta-selection-source-memory.h
/usr/include/mutter-11/meta/meta-selection-source.h
/usr/include/mutter-11/meta/meta-selection.h
/usr/include/mutter-11/meta/meta-settings.h
/usr/include/mutter-11/meta/meta-shadow-factory.h
/usr/include/mutter-11/meta/meta-shaped-texture.h
/usr/include/mutter-11/meta/meta-sound-player.h
/usr/include/mutter-11/meta/meta-stage.h
/usr/include/mutter-11/meta/meta-startup-notification.h
/usr/include/mutter-11/meta/meta-wayland-client.h
/usr/include/mutter-11/meta/meta-window-actor.h
/usr/include/mutter-11/meta/meta-window-group.h
/usr/include/mutter-11/meta/meta-window-shape.h
/usr/include/mutter-11/meta/meta-workspace-manager.h
/usr/include/mutter-11/meta/meta-x11-display.h
/usr/include/mutter-11/meta/meta-x11-errors.h
/usr/include/mutter-11/meta/prefs.h
/usr/include/mutter-11/meta/theme.h
/usr/include/mutter-11/meta/types.h
/usr/include/mutter-11/meta/util.h
/usr/include/mutter-11/meta/window.h
/usr/include/mutter-11/meta/workspace.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libmutter-11.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libmutter-test-11.so
/usr/lib64/libmutter-11.so
/usr/lib64/libmutter-test-11.so
/usr/lib64/pkgconfig/libmutter-11.pc
/usr/lib64/pkgconfig/libmutter-test-11.pc
/usr/lib64/pkgconfig/mutter-clutter-11.pc
/usr/lib64/pkgconfig/mutter-cogl-11.pc
/usr/lib64/pkgconfig/mutter-cogl-pango-11.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-mutter

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libmutter-11.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libmutter-11.so.0.0.0
/usr/lib64/libmutter-11.so.0
/usr/lib64/libmutter-11.so.0.0.0
/usr/lib64/mutter-11/libmutter-clutter-11.so
/usr/lib64/mutter-11/libmutter-clutter-11.so.0
/usr/lib64/mutter-11/libmutter-clutter-11.so.0.0.0
/usr/lib64/mutter-11/libmutter-cogl-11.so
/usr/lib64/mutter-11/libmutter-cogl-11.so.0
/usr/lib64/mutter-11/libmutter-cogl-11.so.0.0.0
/usr/lib64/mutter-11/libmutter-cogl-pango-11.so
/usr/lib64/mutter-11/libmutter-cogl-pango-11.so.0
/usr/lib64/mutter-11/libmutter-cogl-pango-11.so.0.0.0
/usr/lib64/mutter-11/plugins/libdefault.so
/usr/share/clear/optimized-elf/other*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mutter-restart-helper
/usr/share/clear/optimized-elf/exec*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mutter/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mutter.1

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/mutter-11/mutter-anonymous-file
/usr/libexec/installed-tests/mutter-11/mutter-color-management
/usr/libexec/installed-tests/mutter-11/mutter-color-management-profile-conflict
/usr/libexec/installed-tests/mutter-11/mutter-edid
/usr/libexec/installed-tests/mutter-11/mutter-headless-start
/usr/libexec/installed-tests/mutter-11/mutter-installed-dbus-session.py
/usr/libexec/installed-tests/mutter-11/mutter-kms-utils
/usr/libexec/installed-tests/mutter-11/mutter-monitor-unit
/usr/libexec/installed-tests/mutter-11/mutter-monitor-utils
/usr/libexec/installed-tests/mutter-11/mutter-native-unit
/usr/libexec/installed-tests/mutter-11/mutter-persistent-virtual-monitor
/usr/libexec/installed-tests/mutter-11/mutter-pointer-constraints
/usr/libexec/installed-tests/mutter-11/mutter-ref-test-sanity
/usr/libexec/installed-tests/mutter-11/mutter-screen-cast-client
/usr/libexec/installed-tests/mutter-11/mutter-stage-views
/usr/libexec/installed-tests/mutter-11/mutter-test-client
/usr/libexec/installed-tests/mutter-11/mutter-test-runner
/usr/libexec/installed-tests/mutter-11/mutter-unit
/usr/libexec/installed-tests/mutter-11/mutter-wayland-fullscreen
/usr/libexec/installed-tests/mutter-11/mutter-wayland-unit
/usr/libexec/installed-tests/mutter-11/mutter-xwayland
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/buffer-transform
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/dma-buf-scanout
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/fullscreen
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/invalid-subsurfaces
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/invalid-xdg-shell-actions
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/single-pixel-buffer
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/subsurface-parent-unmapped
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/subsurface-remap-toplevel
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/subsurface-reparenting
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/xdg-activation
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/xdg-apply-limits
/usr/libexec/installed-tests/mutter-11/wayland-test-clients/xdg-toplevel-bounds
/usr/share/clear/optimized-elf/test*
/usr/share/installed-tests/mutter-11/mutter-all.test

%files locales -f mutter.lang
%defattr(-,root,root,-)

