#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mutter
Version  : 3.38.3
Release  : 81
URL      : https://download.gnome.org/sources/mutter/3.38/mutter-3.38.3.tar.xz
Source0  : https://download.gnome.org/sources/mutter/3.38/mutter-3.38.3.tar.xz
Summary  : Mutter window manager library
Group    : Development/Tools
License  : GPL-2.0
Requires: mutter-bin = %{version}-%{release}
Requires: mutter-config = %{version}-%{release}
Requires: mutter-data = %{version}-%{release}
Requires: mutter-lib = %{version}-%{release}
Requires: mutter-libexec = %{version}-%{release}
Requires: mutter-license = %{version}-%{release}
Requires: mutter-locales = %{version}-%{release}
Requires: mutter-man = %{version}-%{release}
Requires: gnome-session
Requires: gnome-settings-daemon
Requires: gsettings-desktop-schemas
Requires: hicolor-icon-theme
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gnome-session
BuildRequires : gnome-settings-daemon
BuildRequires : gnome-settings-daemon-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : hicolor-icon-theme
BuildRequires : libgudev-dev
BuildRequires : libwacom-dev
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(cogl-1.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(graphene-gobject-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libwacom)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb-randr)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xkeyboard-config)
BuildRequires : pkgconfig(xtst)
BuildRequires : startup-notification-dev
BuildRequires : sysprof-dev
BuildRequires : sysprof-staticdev
BuildRequires : wayland-dev
BuildRequires : xorg-server
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


%package lib
Summary: lib components for the mutter package.
Group: Libraries
Requires: mutter-data = %{version}-%{release}
Requires: mutter-libexec = %{version}-%{release}
Requires: mutter-license = %{version}-%{release}

%description lib
lib components for the mutter package.


%package libexec
Summary: libexec components for the mutter package.
Group: Default
Requires: mutter-config = %{version}-%{release}
Requires: mutter-license = %{version}-%{release}

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
%setup -q -n mutter-3.38.3
cd %{_builddir}/mutter-3.38.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611707506
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -falign-functions=32 -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -Os -falign-functions=32 -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -Os -falign-functions=32 -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -Os -falign-functions=32 -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mutter
cp %{_builddir}/mutter-3.38.3/COPYING %{buildroot}/usr/share/package-licenses/mutter/4cc77b90af91e615a64ae04893fdffa7939db84c
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang mutter
## Remove excluded files
rm -f %{buildroot}/usr/lib64/haswell/mutter/Cally-2.gir
rm -f %{buildroot}/usr/lib64/haswell/mutter/Cally-2.typelib
rm -f %{buildroot}/usr/lib64/haswell/mutter/Clutter-2.gir
rm -f %{buildroot}/usr/lib64/haswell/mutter/Clutter-2.typelib
rm -f %{buildroot}/usr/lib64/haswell/mutter/ClutterX11-2.gir
rm -f %{buildroot}/usr/lib64/haswell/mutter/ClutterX11-2.typelib
rm -f %{buildroot}/usr/lib64/haswell/mutter/Cogl-2.gir
rm -f %{buildroot}/usr/lib64/haswell/mutter/Cogl-2.typelib
rm -f %{buildroot}/usr/lib64/haswell/mutter/CoglPango-2.gir
rm -f %{buildroot}/usr/lib64/haswell/mutter/CoglPango-2.typelib
rm -f %{buildroot}/usr/lib64/haswell/mutter/Meta-2.gir
rm -f %{buildroot}/usr/lib64/haswell/mutter/Meta-2.typelib
rm -f %{buildroot}/usr/lib64/haswell/libmutter-2.so

%files
%defattr(-,root,root,-)
/usr/lib64/mutter-7/Cally-7.gir
/usr/lib64/mutter-7/Cally-7.typelib
/usr/lib64/mutter-7/Clutter-7.gir
/usr/lib64/mutter-7/Clutter-7.typelib
/usr/lib64/mutter-7/ClutterX11-7.gir
/usr/lib64/mutter-7/ClutterX11-7.typelib
/usr/lib64/mutter-7/Cogl-7.gir
/usr/lib64/mutter-7/Cogl-7.typelib
/usr/lib64/mutter-7/CoglPango-7.gir
/usr/lib64/mutter-7/CoglPango-7.typelib
/usr/lib64/mutter-7/Meta-7.gir
/usr/lib64/mutter-7/Meta-7.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/mutter

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
/usr/share/mutter-7/tests/stacking/basic-wayland.metatest
/usr/share/mutter-7/tests/stacking/basic-x11.metatest
/usr/share/mutter-7/tests/stacking/client-side-decorated.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-no-default-focus.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-no-input-no-take-focus-parent.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-no-input-no-take-focus-parents.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-no-input-parent-delayed-focus-default-cancelled.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-no-input-parent.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-no-input-parents-queued-default-focus-destroyed.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-no-input-parents.metatest
/usr/share/mutter-7/tests/stacking/closed-transient-only-take-focus-parents.metatest
/usr/share/mutter-7/tests/stacking/closed-transient.metatest
/usr/share/mutter-7/tests/stacking/default-size.metatest
/usr/share/mutter-7/tests/stacking/fullscreen-maximize.metatest
/usr/share/mutter-7/tests/stacking/minimized.metatest
/usr/share/mutter-7/tests/stacking/mixed-windows.metatest
/usr/share/mutter-7/tests/stacking/modals.metatest
/usr/share/mutter-7/tests/stacking/override-redirect.metatest
/usr/share/mutter-7/tests/stacking/restore-position.metatest
/usr/share/mutter-7/tests/stacking/restore-size.metatest
/usr/share/mutter-7/tests/stacking/set-override-redirect-parent.metatest
/usr/share/mutter-7/tests/stacking/set-parent-exported.metatest
/usr/share/mutter-7/tests/stacking/set-parent.metatest
/usr/share/mutter-7/tests/stacking/unmaximize-new-size.metatest

%files dev
%defattr(-,root,root,-)
/usr/include/mutter-7/clutter/cally/cally-actor.h
/usr/include/mutter-7/clutter/cally/cally-clone.h
/usr/include/mutter-7/clutter/cally/cally-factory.h
/usr/include/mutter-7/clutter/cally/cally-main.h
/usr/include/mutter-7/clutter/cally/cally-root.h
/usr/include/mutter-7/clutter/cally/cally-stage.h
/usr/include/mutter-7/clutter/cally/cally-text.h
/usr/include/mutter-7/clutter/cally/cally-util.h
/usr/include/mutter-7/clutter/cally/cally.h
/usr/include/mutter-7/clutter/clutter/clutter-action.h
/usr/include/mutter-7/clutter/clutter/clutter-actor-meta.h
/usr/include/mutter-7/clutter/clutter/clutter-actor.h
/usr/include/mutter-7/clutter/clutter/clutter-align-constraint.h
/usr/include/mutter-7/clutter/clutter/clutter-animatable.h
/usr/include/mutter-7/clutter/clutter/clutter-autocleanups.h
/usr/include/mutter-7/clutter/clutter/clutter-backend.h
/usr/include/mutter-7/clutter/clutter/clutter-bin-layout.h
/usr/include/mutter-7/clutter/clutter/clutter-bind-constraint.h
/usr/include/mutter-7/clutter/clutter/clutter-binding-pool.h
/usr/include/mutter-7/clutter/clutter/clutter-blur-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-box-layout.h
/usr/include/mutter-7/clutter/clutter/clutter-brightness-contrast-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-cairo.h
/usr/include/mutter-7/clutter/clutter/clutter-canvas.h
/usr/include/mutter-7/clutter/clutter/clutter-child-meta.h
/usr/include/mutter-7/clutter/clutter/clutter-click-action.h
/usr/include/mutter-7/clutter/clutter/clutter-clone.h
/usr/include/mutter-7/clutter/clutter/clutter-color-static.h
/usr/include/mutter-7/clutter/clutter/clutter-color.h
/usr/include/mutter-7/clutter/clutter/clutter-colorize-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-config.h
/usr/include/mutter-7/clutter/clutter/clutter-constraint.h
/usr/include/mutter-7/clutter/clutter/clutter-container.h
/usr/include/mutter-7/clutter/clutter/clutter-content.h
/usr/include/mutter-7/clutter/clutter/clutter-deform-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-deprecated.h
/usr/include/mutter-7/clutter/clutter/clutter-desaturate-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-enum-types.h
/usr/include/mutter-7/clutter/clutter/clutter-enums.h
/usr/include/mutter-7/clutter/clutter/clutter-event.h
/usr/include/mutter-7/clutter/clutter/clutter-feature.h
/usr/include/mutter-7/clutter/clutter/clutter-fixed-layout.h
/usr/include/mutter-7/clutter/clutter/clutter-flow-layout.h
/usr/include/mutter-7/clutter/clutter/clutter-frame-clock.h
/usr/include/mutter-7/clutter/clutter/clutter-gesture-action.h
/usr/include/mutter-7/clutter/clutter/clutter-grid-layout.h
/usr/include/mutter-7/clutter/clutter/clutter-image.h
/usr/include/mutter-7/clutter/clutter/clutter-input-device-tool.h
/usr/include/mutter-7/clutter/clutter/clutter-input-device.h
/usr/include/mutter-7/clutter/clutter/clutter-input-focus.h
/usr/include/mutter-7/clutter/clutter/clutter-input-method.h
/usr/include/mutter-7/clutter/clutter/clutter-interval.h
/usr/include/mutter-7/clutter/clutter/clutter-keyframe-transition.h
/usr/include/mutter-7/clutter/clutter/clutter-keymap.h
/usr/include/mutter-7/clutter/clutter/clutter-keysyms.h
/usr/include/mutter-7/clutter/clutter/clutter-layout-manager.h
/usr/include/mutter-7/clutter/clutter/clutter-layout-meta.h
/usr/include/mutter-7/clutter/clutter/clutter-macros.h
/usr/include/mutter-7/clutter/clutter/clutter-main.h
/usr/include/mutter-7/clutter/clutter/clutter-marshal.h
/usr/include/mutter-7/clutter/clutter/clutter-mutter.h
/usr/include/mutter-7/clutter/clutter/clutter-offscreen-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-page-turn-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-paint-context.h
/usr/include/mutter-7/clutter/clutter/clutter-paint-node.h
/usr/include/mutter-7/clutter/clutter/clutter-paint-nodes.h
/usr/include/mutter-7/clutter/clutter/clutter-pan-action.h
/usr/include/mutter-7/clutter/clutter/clutter-path-constraint.h
/usr/include/mutter-7/clutter/clutter/clutter-path.h
/usr/include/mutter-7/clutter/clutter/clutter-pick-context.h
/usr/include/mutter-7/clutter/clutter/clutter-property-transition.h
/usr/include/mutter-7/clutter/clutter/clutter-rotate-action.h
/usr/include/mutter-7/clutter/clutter/clutter-script.h
/usr/include/mutter-7/clutter/clutter/clutter-scriptable.h
/usr/include/mutter-7/clutter/clutter/clutter-scroll-actor.h
/usr/include/mutter-7/clutter/clutter/clutter-seat.h
/usr/include/mutter-7/clutter/clutter/clutter-settings.h
/usr/include/mutter-7/clutter/clutter/clutter-shader-effect.h
/usr/include/mutter-7/clutter/clutter/clutter-shader-types.h
/usr/include/mutter-7/clutter/clutter/clutter-snap-constraint.h
/usr/include/mutter-7/clutter/clutter/clutter-stage-manager.h
/usr/include/mutter-7/clutter/clutter/clutter-stage-view.h
/usr/include/mutter-7/clutter/clutter/clutter-stage.h
/usr/include/mutter-7/clutter/clutter/clutter-swipe-action.h
/usr/include/mutter-7/clutter/clutter/clutter-tap-action.h
/usr/include/mutter-7/clutter/clutter/clutter-text-buffer.h
/usr/include/mutter-7/clutter/clutter/clutter-text.h
/usr/include/mutter-7/clutter/clutter/clutter-timeline.h
/usr/include/mutter-7/clutter/clutter/clutter-transition-group.h
/usr/include/mutter-7/clutter/clutter/clutter-transition.h
/usr/include/mutter-7/clutter/clutter/clutter-types.h
/usr/include/mutter-7/clutter/clutter/clutter-units.h
/usr/include/mutter-7/clutter/clutter/clutter-virtual-input-device.h
/usr/include/mutter-7/clutter/clutter/clutter-zoom-action.h
/usr/include/mutter-7/clutter/clutter/clutter.h
/usr/include/mutter-7/clutter/clutter/deprecated/clutter-container.h
/usr/include/mutter-7/clutter/clutter/deprecated/clutter-timeline.h
/usr/include/mutter-7/clutter/clutter/x11/clutter-x11.h
/usr/include/mutter-7/cogl/cogl-pango/cogl-pango.h
/usr/include/mutter-7/cogl/cogl/cogl-atlas-texture.h
/usr/include/mutter-7/cogl/cogl/cogl-attribute-buffer.h
/usr/include/mutter-7/cogl/cogl/cogl-attribute.h
/usr/include/mutter-7/cogl/cogl/cogl-bitmap.h
/usr/include/mutter-7/cogl/cogl/cogl-buffer.h
/usr/include/mutter-7/cogl/cogl/cogl-color.h
/usr/include/mutter-7/cogl/cogl/cogl-context.h
/usr/include/mutter-7/cogl/cogl/cogl-defines.h
/usr/include/mutter-7/cogl/cogl/cogl-depth-state.h
/usr/include/mutter-7/cogl/cogl/cogl-display.h
/usr/include/mutter-7/cogl/cogl/cogl-dma-buf-handle.h
/usr/include/mutter-7/cogl/cogl/cogl-egl-defines.h
/usr/include/mutter-7/cogl/cogl/cogl-egl.h
/usr/include/mutter-7/cogl/cogl/cogl-fence.h
/usr/include/mutter-7/cogl/cogl/cogl-frame-info.h
/usr/include/mutter-7/cogl/cogl/cogl-framebuffer.h
/usr/include/mutter-7/cogl/cogl/cogl-glib-source.h
/usr/include/mutter-7/cogl/cogl/cogl-glx.h
/usr/include/mutter-7/cogl/cogl/cogl-gtype-private.h
/usr/include/mutter-7/cogl/cogl/cogl-index-buffer.h
/usr/include/mutter-7/cogl/cogl/cogl-indices.h
/usr/include/mutter-7/cogl/cogl/cogl-macros.h
/usr/include/mutter-7/cogl/cogl/cogl-matrix-stack.h
/usr/include/mutter-7/cogl/cogl/cogl-matrix.h
/usr/include/mutter-7/cogl/cogl/cogl-meta-texture.h
/usr/include/mutter-7/cogl/cogl/cogl-object.h
/usr/include/mutter-7/cogl/cogl/cogl-offscreen.h
/usr/include/mutter-7/cogl/cogl/cogl-onscreen-template.h
/usr/include/mutter-7/cogl/cogl/cogl-onscreen.h
/usr/include/mutter-7/cogl/cogl/cogl-output.h
/usr/include/mutter-7/cogl/cogl/cogl-pipeline-layer-state.h
/usr/include/mutter-7/cogl/cogl/cogl-pipeline-state.h
/usr/include/mutter-7/cogl/cogl/cogl-pipeline.h
/usr/include/mutter-7/cogl/cogl/cogl-pixel-buffer.h
/usr/include/mutter-7/cogl/cogl/cogl-pixel-format.h
/usr/include/mutter-7/cogl/cogl/cogl-poll.h
/usr/include/mutter-7/cogl/cogl/cogl-primitive-texture.h
/usr/include/mutter-7/cogl/cogl/cogl-primitive.h
/usr/include/mutter-7/cogl/cogl/cogl-renderer.h
/usr/include/mutter-7/cogl/cogl/cogl-scanout.h
/usr/include/mutter-7/cogl/cogl/cogl-snippet.h
/usr/include/mutter-7/cogl/cogl/cogl-sub-texture.h
/usr/include/mutter-7/cogl/cogl/cogl-swap-chain.h
/usr/include/mutter-7/cogl/cogl/cogl-texture-2d-sliced.h
/usr/include/mutter-7/cogl/cogl/cogl-texture-2d.h
/usr/include/mutter-7/cogl/cogl/cogl-texture-pixmap-x11.h
/usr/include/mutter-7/cogl/cogl/cogl-texture.h
/usr/include/mutter-7/cogl/cogl/cogl-trace.h
/usr/include/mutter-7/cogl/cogl/cogl-types.h
/usr/include/mutter-7/cogl/cogl/cogl-version.h
/usr/include/mutter-7/cogl/cogl/cogl-wayland-server.h
/usr/include/mutter-7/cogl/cogl/cogl-xlib-renderer.h
/usr/include/mutter-7/cogl/cogl/cogl-xlib.h
/usr/include/mutter-7/cogl/cogl/cogl.h
/usr/include/mutter-7/cogl/cogl/cogl1-context.h
/usr/include/mutter-7/cogl/cogl/deprecated/cogl-auto-texture.h
/usr/include/mutter-7/cogl/cogl/deprecated/cogl-clutter.h
/usr/include/mutter-7/cogl/cogl/deprecated/cogl-material-compat.h
/usr/include/mutter-7/cogl/cogl/deprecated/cogl-shader.h
/usr/include/mutter-7/cogl/cogl/deprecated/cogl-type-casts.h
/usr/include/mutter-7/cogl/cogl/gl-prototypes/cogl-core-functions.h
/usr/include/mutter-7/cogl/cogl/gl-prototypes/cogl-gles2-functions.h
/usr/include/mutter-7/cogl/cogl/gl-prototypes/cogl-glsl-functions.h
/usr/include/mutter-7/cogl/cogl/gl-prototypes/cogl-in-gles-core-functions.h
/usr/include/mutter-7/cogl/cogl/gl-prototypes/cogl-in-gles2-core-functions.h
/usr/include/mutter-7/meta/barrier.h
/usr/include/mutter-7/meta/boxes.h
/usr/include/mutter-7/meta/common.h
/usr/include/mutter-7/meta/compositor-mutter.h
/usr/include/mutter-7/meta/compositor.h
/usr/include/mutter-7/meta/display.h
/usr/include/mutter-7/meta/group.h
/usr/include/mutter-7/meta/keybindings.h
/usr/include/mutter-7/meta/main.h
/usr/include/mutter-7/meta/meta-backend.h
/usr/include/mutter-7/meta/meta-background-actor.h
/usr/include/mutter-7/meta/meta-background-content.h
/usr/include/mutter-7/meta/meta-background-group.h
/usr/include/mutter-7/meta/meta-background-image.h
/usr/include/mutter-7/meta/meta-background.h
/usr/include/mutter-7/meta/meta-close-dialog.h
/usr/include/mutter-7/meta/meta-cursor-tracker.h
/usr/include/mutter-7/meta/meta-dnd.h
/usr/include/mutter-7/meta/meta-enum-types.h
/usr/include/mutter-7/meta/meta-idle-monitor.h
/usr/include/mutter-7/meta/meta-inhibit-shortcuts-dialog.h
/usr/include/mutter-7/meta/meta-later.h
/usr/include/mutter-7/meta/meta-launch-context.h
/usr/include/mutter-7/meta/meta-monitor-manager.h
/usr/include/mutter-7/meta/meta-plugin.h
/usr/include/mutter-7/meta/meta-remote-access-controller.h
/usr/include/mutter-7/meta/meta-selection-source-memory.h
/usr/include/mutter-7/meta/meta-selection-source.h
/usr/include/mutter-7/meta/meta-selection.h
/usr/include/mutter-7/meta/meta-settings.h
/usr/include/mutter-7/meta/meta-shadow-factory.h
/usr/include/mutter-7/meta/meta-shaped-texture.h
/usr/include/mutter-7/meta/meta-sound-player.h
/usr/include/mutter-7/meta/meta-stage.h
/usr/include/mutter-7/meta/meta-startup-notification.h
/usr/include/mutter-7/meta/meta-version.h
/usr/include/mutter-7/meta/meta-wayland-client.h
/usr/include/mutter-7/meta/meta-window-actor.h
/usr/include/mutter-7/meta/meta-window-group.h
/usr/include/mutter-7/meta/meta-window-shape.h
/usr/include/mutter-7/meta/meta-workspace-manager.h
/usr/include/mutter-7/meta/meta-x11-display.h
/usr/include/mutter-7/meta/meta-x11-errors.h
/usr/include/mutter-7/meta/prefs.h
/usr/include/mutter-7/meta/theme.h
/usr/include/mutter-7/meta/types.h
/usr/include/mutter-7/meta/util.h
/usr/include/mutter-7/meta/window.h
/usr/include/mutter-7/meta/workspace.h
/usr/lib64/libmutter-7.so
/usr/lib64/pkgconfig/libmutter-7.pc
/usr/lib64/pkgconfig/mutter-clutter-7.pc
/usr/lib64/pkgconfig/mutter-clutter-x11-7.pc
/usr/lib64/pkgconfig/mutter-cogl-7.pc
/usr/lib64/pkgconfig/mutter-cogl-pango-7.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmutter-7.so.0
/usr/lib64/libmutter-7.so.0.0.0
/usr/lib64/mutter-7/libmutter-clutter-7.so
/usr/lib64/mutter-7/libmutter-clutter-7.so.0
/usr/lib64/mutter-7/libmutter-clutter-7.so.0.0.0
/usr/lib64/mutter-7/libmutter-cogl-7.so
/usr/lib64/mutter-7/libmutter-cogl-7.so.0
/usr/lib64/mutter-7/libmutter-cogl-7.so.0.0.0
/usr/lib64/mutter-7/libmutter-cogl-pango-7.so
/usr/lib64/mutter-7/libmutter-cogl-pango-7.so.0
/usr/lib64/mutter-7/libmutter-cogl-pango-7.so.0.0.0
/usr/lib64/mutter-7/plugins/libdefault.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mutter-restart-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mutter/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mutter.1

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/mutter-7/cogl/conform/config.env
/usr/libexec/installed-tests/mutter-7/cogl/conform/run-tests.sh
/usr/libexec/installed-tests/mutter-7/cogl/conform/test-conformance
/usr/libexec/installed-tests/mutter-7/cogl/conform/unit-tests
/usr/libexec/installed-tests/mutter-7/mutter-headless-start-test
/usr/libexec/installed-tests/mutter-7/mutter-stage-view-tests
/usr/libexec/installed-tests/mutter-7/mutter-test-client
/usr/libexec/installed-tests/mutter-7/mutter-test-runner
/usr/libexec/installed-tests/mutter-7/mutter-test-unit-tests
/usr/libexec/installed-tests/mutter-7/wayland-test-clients/meta-anonymous-file
/usr/libexec/installed-tests/mutter-7/wayland-test-clients/subsurface-remap-toplevel
/usr/share/installed-tests/mutter-7/mutter-all.test
/usr/share/installed-tests/mutter-7/mutter-cogl.test

%files locales -f mutter.lang
%defattr(-,root,root,-)

