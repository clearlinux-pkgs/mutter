#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mutter
Version  : 3.24.2
Release  : 18
URL      : https://download.gnome.org/sources/mutter/3.24/mutter-3.24.2.tar.xz
Source0  : https://download.gnome.org/sources/mutter/3.24/mutter-3.24.2.tar.xz
Summary  : An object oriented GL/GLES Abstraction/Utility Layer
Group    : Development/Tools
License  : GPL-2.0
Requires: mutter-bin
Requires: mutter-lib
Requires: mutter-data
Requires: mutter-locales
Requires: mutter-doc
BuildRequires : gettext
BuildRequires : libXtst-dev
BuildRequires : libgudev-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(cogl-1.0)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glesv1_cm)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb-randr)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xkeyboard-config)
BuildRequires : pkgconfig(xrandr)
BuildRequires : sed
BuildRequires : startup-notification-dev
BuildRequires : zenity
Patch1: build.patch
Patch2: disable-netwm-ping-dialogs.patch
Patch3: headless.patch

%description
Outline of test categories:
The conform/ tests:
-------------------
These tests should be non-interactive unit-tests that verify a single
feature is behaving as documented. See conform/ADDING_NEW_TESTS for more
details.

%package bin
Summary: bin components for the mutter package.
Group: Binaries
Requires: mutter-data

%description bin
bin components for the mutter package.


%package data
Summary: data components for the mutter package.
Group: Data

%description data
data components for the mutter package.


%package dev
Summary: dev components for the mutter package.
Group: Development
Requires: mutter-lib
Requires: mutter-bin
Requires: mutter-data
Provides: mutter-devel

%description dev
dev components for the mutter package.


%package doc
Summary: doc components for the mutter package.
Group: Documentation

%description doc
doc components for the mutter package.


%package lib
Summary: lib components for the mutter package.
Group: Libraries
Requires: mutter-data

%description lib
lib components for the mutter package.


%package locales
Summary: locales components for the mutter package.
Group: Default

%description locales
locales components for the mutter package.


%prep
%setup -q -n mutter-3.24.2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496581409
export CFLAGS="$CFLAGS -Os -Wl,--gc-sections -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -Wl,--gc-sections -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -Wl,--gc-sections -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -Wl,--gc-sections -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static --enable-compile-warnings=minimum \
--disable-schemas-compile \
--enable-native-backend
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1496581409
rm -rf %{buildroot}
%make_install
%find_lang mutter

%files
%defattr(-,root,root,-)
/usr/lib64/mutter/Cally-0.gir
/usr/lib64/mutter/Cally-0.typelib
/usr/lib64/mutter/Clutter-0.gir
/usr/lib64/mutter/Clutter-0.typelib
/usr/lib64/mutter/ClutterX11-0.gir
/usr/lib64/mutter/ClutterX11-0.typelib
/usr/lib64/mutter/Cogl-0.gir
/usr/lib64/mutter/Cogl-0.typelib
/usr/lib64/mutter/CoglPango-0.gir
/usr/lib64/mutter/CoglPango-0.typelib
/usr/lib64/mutter/Meta-0.gir
/usr/lib64/mutter/Meta-0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/mutter
/usr/libexec/mutter-restart-helper

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/mutter-schemas.convert
/usr/share/applications/mutter.desktop
/usr/share/glib-2.0/schemas/org.gnome.mutter.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
/usr/share/gnome-control-center/keybindings/50-mutter-navigation.xml
/usr/share/gnome-control-center/keybindings/50-mutter-system.xml
/usr/share/gnome-control-center/keybindings/50-mutter-windows.xml

%files dev
%defattr(-,root,root,-)
/usr/include/mutter/clutter-0/cally/cally-actor.h
/usr/include/mutter/clutter-0/cally/cally-clone.h
/usr/include/mutter/clutter-0/cally/cally-factory.h
/usr/include/mutter/clutter-0/cally/cally-group.h
/usr/include/mutter/clutter-0/cally/cally-main.h
/usr/include/mutter/clutter-0/cally/cally-rectangle.h
/usr/include/mutter/clutter-0/cally/cally-root.h
/usr/include/mutter/clutter-0/cally/cally-stage.h
/usr/include/mutter/clutter-0/cally/cally-text.h
/usr/include/mutter/clutter-0/cally/cally-texture.h
/usr/include/mutter/clutter-0/cally/cally-util.h
/usr/include/mutter/clutter-0/cally/cally.h
/usr/include/mutter/clutter-0/clutter/clutter-action.h
/usr/include/mutter/clutter-0/clutter/clutter-actor-meta.h
/usr/include/mutter/clutter-0/clutter/clutter-actor.h
/usr/include/mutter/clutter-0/clutter/clutter-align-constraint.h
/usr/include/mutter/clutter-0/clutter/clutter-animatable.h
/usr/include/mutter/clutter-0/clutter/clutter-autocleanups.h
/usr/include/mutter/clutter-0/clutter/clutter-backend.h
/usr/include/mutter/clutter-0/clutter/clutter-bin-layout.h
/usr/include/mutter/clutter-0/clutter/clutter-bind-constraint.h
/usr/include/mutter/clutter-0/clutter/clutter-binding-pool.h
/usr/include/mutter/clutter-0/clutter/clutter-blur-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-box-layout.h
/usr/include/mutter/clutter-0/clutter/clutter-brightness-contrast-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-cairo.h
/usr/include/mutter/clutter-0/clutter/clutter-canvas.h
/usr/include/mutter/clutter-0/clutter/clutter-child-meta.h
/usr/include/mutter/clutter-0/clutter/clutter-click-action.h
/usr/include/mutter/clutter-0/clutter/clutter-clone.h
/usr/include/mutter/clutter-0/clutter/clutter-color-static.h
/usr/include/mutter/clutter-0/clutter/clutter-color.h
/usr/include/mutter/clutter-0/clutter/clutter-colorize-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-config.h
/usr/include/mutter/clutter-0/clutter/clutter-constraint.h
/usr/include/mutter/clutter-0/clutter/clutter-container.h
/usr/include/mutter/clutter-0/clutter/clutter-content.h
/usr/include/mutter/clutter-0/clutter/clutter-deform-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-deprecated.h
/usr/include/mutter/clutter-0/clutter/clutter-desaturate-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-device-manager.h
/usr/include/mutter/clutter-0/clutter/clutter-drag-action.h
/usr/include/mutter/clutter-0/clutter/clutter-drop-action.h
/usr/include/mutter/clutter-0/clutter/clutter-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-enum-types.h
/usr/include/mutter/clutter-0/clutter/clutter-enums.h
/usr/include/mutter/clutter-0/clutter/clutter-event.h
/usr/include/mutter/clutter-0/clutter/clutter-feature.h
/usr/include/mutter/clutter-0/clutter/clutter-fixed-layout.h
/usr/include/mutter/clutter-0/clutter/clutter-flow-layout.h
/usr/include/mutter/clutter-0/clutter/clutter-gesture-action.h
/usr/include/mutter/clutter-0/clutter/clutter-grid-layout.h
/usr/include/mutter/clutter-0/clutter/clutter-group.h
/usr/include/mutter/clutter-0/clutter/clutter-image.h
/usr/include/mutter/clutter-0/clutter/clutter-input-device-tool.h
/usr/include/mutter/clutter-0/clutter/clutter-input-device.h
/usr/include/mutter/clutter-0/clutter/clutter-interval.h
/usr/include/mutter/clutter-0/clutter/clutter-keyframe-transition.h
/usr/include/mutter/clutter-0/clutter/clutter-keysyms.h
/usr/include/mutter/clutter-0/clutter/clutter-layout-manager.h
/usr/include/mutter/clutter-0/clutter/clutter-layout-meta.h
/usr/include/mutter/clutter-0/clutter/clutter-macros.h
/usr/include/mutter/clutter-0/clutter/clutter-main.h
/usr/include/mutter/clutter-0/clutter/clutter-marshal.h
/usr/include/mutter/clutter-0/clutter/clutter-mutter.h
/usr/include/mutter/clutter-0/clutter/clutter-offscreen-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-page-turn-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-paint-node.h
/usr/include/mutter/clutter-0/clutter/clutter-paint-nodes.h
/usr/include/mutter/clutter-0/clutter/clutter-pan-action.h
/usr/include/mutter/clutter-0/clutter/clutter-path-constraint.h
/usr/include/mutter/clutter-0/clutter/clutter-path.h
/usr/include/mutter/clutter-0/clutter/clutter-property-transition.h
/usr/include/mutter/clutter-0/clutter/clutter-rotate-action.h
/usr/include/mutter/clutter-0/clutter/clutter-script.h
/usr/include/mutter/clutter-0/clutter/clutter-scriptable.h
/usr/include/mutter/clutter-0/clutter/clutter-scroll-actor.h
/usr/include/mutter/clutter-0/clutter/clutter-settings.h
/usr/include/mutter/clutter-0/clutter/clutter-shader-effect.h
/usr/include/mutter/clutter-0/clutter/clutter-shader-types.h
/usr/include/mutter/clutter-0/clutter/clutter-snap-constraint.h
/usr/include/mutter/clutter-0/clutter/clutter-stage-manager.h
/usr/include/mutter/clutter-0/clutter/clutter-stage.h
/usr/include/mutter/clutter-0/clutter/clutter-swipe-action.h
/usr/include/mutter/clutter-0/clutter/clutter-tap-action.h
/usr/include/mutter/clutter-0/clutter/clutter-test-utils.h
/usr/include/mutter/clutter-0/clutter/clutter-text-buffer.h
/usr/include/mutter/clutter-0/clutter/clutter-text.h
/usr/include/mutter/clutter-0/clutter/clutter-texture.h
/usr/include/mutter/clutter-0/clutter/clutter-timeline.h
/usr/include/mutter/clutter-0/clutter/clutter-transition-group.h
/usr/include/mutter/clutter-0/clutter/clutter-transition.h
/usr/include/mutter/clutter-0/clutter/clutter-types.h
/usr/include/mutter/clutter-0/clutter/clutter-units.h
/usr/include/mutter/clutter-0/clutter/clutter-version.h
/usr/include/mutter/clutter-0/clutter/clutter-virtual-input-device.h
/usr/include/mutter/clutter-0/clutter/clutter-zoom-action.h
/usr/include/mutter/clutter-0/clutter/clutter.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-actor.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-alpha.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-animatable.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-animation.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-animator.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-backend.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-behaviour-depth.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-behaviour-ellipse.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-behaviour-opacity.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-behaviour-path.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-behaviour-rotate.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-behaviour-scale.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-behaviour.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-bin-layout.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-box.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-cairo-texture.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-container.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-frame-source.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-group.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-input-device.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-keysyms.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-list-model.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-main.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-media.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-model.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-rectangle.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-score.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-shader.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-stage-manager.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-stage.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-state.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-table-layout.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-texture.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-timeline.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-timeout-pool.h
/usr/include/mutter/clutter-0/clutter/deprecated/clutter-util.h
/usr/include/mutter/clutter-0/clutter/egl/clutter-egl-headers.h
/usr/include/mutter/clutter-0/clutter/egl/clutter-egl.h
/usr/include/mutter/clutter-0/clutter/evdev/clutter-evdev.h
/usr/include/mutter/clutter-0/clutter/wayland/clutter-wayland-compositor.h
/usr/include/mutter/clutter-0/clutter/wayland/clutter-wayland-surface.h
/usr/include/mutter/clutter-0/clutter/x11/clutter-x11-texture-pixmap.h
/usr/include/mutter/clutter-0/clutter/x11/clutter-x11.h
/usr/include/mutter/cogl/cogl-pango/cogl-pango.h
/usr/include/mutter/cogl/cogl-path/cogl-path-enum-types.h
/usr/include/mutter/cogl/cogl-path/cogl-path-functions.h
/usr/include/mutter/cogl/cogl-path/cogl-path-types.h
/usr/include/mutter/cogl/cogl-path/cogl-path.h
/usr/include/mutter/cogl/cogl/cogl-atlas-texture.h
/usr/include/mutter/cogl/cogl/cogl-attribute-buffer.h
/usr/include/mutter/cogl/cogl/cogl-attribute.h
/usr/include/mutter/cogl/cogl/cogl-auto-texture.h
/usr/include/mutter/cogl/cogl/cogl-bitmap.h
/usr/include/mutter/cogl/cogl/cogl-buffer.h
/usr/include/mutter/cogl/cogl/cogl-clutter.h
/usr/include/mutter/cogl/cogl/cogl-color.h
/usr/include/mutter/cogl/cogl/cogl-context.h
/usr/include/mutter/cogl/cogl/cogl-defines.h
/usr/include/mutter/cogl/cogl/cogl-deprecated.h
/usr/include/mutter/cogl/cogl/cogl-depth-state.h
/usr/include/mutter/cogl/cogl/cogl-display.h
/usr/include/mutter/cogl/cogl/cogl-egl-defines.h
/usr/include/mutter/cogl/cogl/cogl-egl.h
/usr/include/mutter/cogl/cogl/cogl-error.h
/usr/include/mutter/cogl/cogl/cogl-euler.h
/usr/include/mutter/cogl/cogl/cogl-fence.h
/usr/include/mutter/cogl/cogl/cogl-frame-info.h
/usr/include/mutter/cogl/cogl/cogl-framebuffer.h
/usr/include/mutter/cogl/cogl/cogl-gles2-types.h
/usr/include/mutter/cogl/cogl/cogl-gles2.h
/usr/include/mutter/cogl/cogl/cogl-glib-source.h
/usr/include/mutter/cogl/cogl/cogl-glx.h
/usr/include/mutter/cogl/cogl/cogl-gtype-private.h
/usr/include/mutter/cogl/cogl/cogl-index-buffer.h
/usr/include/mutter/cogl/cogl/cogl-indices.h
/usr/include/mutter/cogl/cogl/cogl-macros.h
/usr/include/mutter/cogl/cogl/cogl-material-compat.h
/usr/include/mutter/cogl/cogl/cogl-matrix-stack.h
/usr/include/mutter/cogl/cogl/cogl-matrix.h
/usr/include/mutter/cogl/cogl/cogl-meta-texture.h
/usr/include/mutter/cogl/cogl/cogl-mutter.h
/usr/include/mutter/cogl/cogl/cogl-object.h
/usr/include/mutter/cogl/cogl/cogl-offscreen.h
/usr/include/mutter/cogl/cogl/cogl-onscreen-template.h
/usr/include/mutter/cogl/cogl/cogl-onscreen.h
/usr/include/mutter/cogl/cogl/cogl-output.h
/usr/include/mutter/cogl/cogl/cogl-pango.h
/usr/include/mutter/cogl/cogl/cogl-pipeline-layer-state.h
/usr/include/mutter/cogl/cogl/cogl-pipeline-state.h
/usr/include/mutter/cogl/cogl/cogl-pipeline.h
/usr/include/mutter/cogl/cogl/cogl-pixel-buffer.h
/usr/include/mutter/cogl/cogl/cogl-poll.h
/usr/include/mutter/cogl/cogl/cogl-primitive-texture.h
/usr/include/mutter/cogl/cogl/cogl-primitive.h
/usr/include/mutter/cogl/cogl/cogl-primitives.h
/usr/include/mutter/cogl/cogl/cogl-quaternion.h
/usr/include/mutter/cogl/cogl/cogl-renderer.h
/usr/include/mutter/cogl/cogl/cogl-shader.h
/usr/include/mutter/cogl/cogl/cogl-snippet.h
/usr/include/mutter/cogl/cogl/cogl-sub-texture.h
/usr/include/mutter/cogl/cogl/cogl-swap-chain.h
/usr/include/mutter/cogl/cogl/cogl-texture-2d-gl.h
/usr/include/mutter/cogl/cogl/cogl-texture-2d-sliced.h
/usr/include/mutter/cogl/cogl/cogl-texture-2d.h
/usr/include/mutter/cogl/cogl/cogl-texture-3d.h
/usr/include/mutter/cogl/cogl/cogl-texture-pixmap-x11.h
/usr/include/mutter/cogl/cogl/cogl-texture-rectangle.h
/usr/include/mutter/cogl/cogl/cogl-texture.h
/usr/include/mutter/cogl/cogl/cogl-type-casts.h
/usr/include/mutter/cogl/cogl/cogl-types.h
/usr/include/mutter/cogl/cogl/cogl-vector.h
/usr/include/mutter/cogl/cogl/cogl-version.h
/usr/include/mutter/cogl/cogl/cogl-vertex-buffer.h
/usr/include/mutter/cogl/cogl/cogl-wayland-server.h
/usr/include/mutter/cogl/cogl/cogl-xlib-renderer.h
/usr/include/mutter/cogl/cogl/cogl-xlib.h
/usr/include/mutter/cogl/cogl/cogl.h
/usr/include/mutter/cogl/cogl/cogl1-context.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-auto-texture.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-clutter-xlib.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-clutter.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-framebuffer-deprecated.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-material-compat.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-shader.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-type-casts.h
/usr/include/mutter/cogl/cogl/deprecated/cogl-vertex-buffer.h
/usr/include/mutter/cogl/cogl/gl-prototypes/cogl-core-functions.h
/usr/include/mutter/cogl/cogl/gl-prototypes/cogl-gles2-functions.h
/usr/include/mutter/cogl/cogl/gl-prototypes/cogl-glsl-functions.h
/usr/include/mutter/cogl/cogl/gl-prototypes/cogl-in-gles-core-functions.h
/usr/include/mutter/cogl/cogl/gl-prototypes/cogl-in-gles2-core-functions.h
/usr/include/mutter/meta/barrier.h
/usr/include/mutter/meta/boxes.h
/usr/include/mutter/meta/common.h
/usr/include/mutter/meta/compositor-mutter.h
/usr/include/mutter/meta/compositor.h
/usr/include/mutter/meta/display.h
/usr/include/mutter/meta/errors.h
/usr/include/mutter/meta/group.h
/usr/include/mutter/meta/keybindings.h
/usr/include/mutter/meta/main.h
/usr/include/mutter/meta/meta-backend.h
/usr/include/mutter/meta/meta-background-actor.h
/usr/include/mutter/meta/meta-background-group.h
/usr/include/mutter/meta/meta-background-image.h
/usr/include/mutter/meta/meta-background.h
/usr/include/mutter/meta/meta-cursor-tracker.h
/usr/include/mutter/meta/meta-dnd.h
/usr/include/mutter/meta/meta-enum-types.h
/usr/include/mutter/meta/meta-idle-monitor.h
/usr/include/mutter/meta/meta-monitor-manager.h
/usr/include/mutter/meta/meta-plugin.h
/usr/include/mutter/meta/meta-shadow-factory.h
/usr/include/mutter/meta/meta-shaped-texture.h
/usr/include/mutter/meta/meta-version.h
/usr/include/mutter/meta/meta-window-actor.h
/usr/include/mutter/meta/meta-window-shape.h
/usr/include/mutter/meta/prefs.h
/usr/include/mutter/meta/screen.h
/usr/include/mutter/meta/theme.h
/usr/include/mutter/meta/types.h
/usr/include/mutter/meta/util.h
/usr/include/mutter/meta/window.h
/usr/include/mutter/meta/workspace.h
/usr/lib64/libmutter-0.so
/usr/lib64/pkgconfig/libmutter-0.pc
/usr/lib64/pkgconfig/mutter-clutter-0.pc
/usr/lib64/pkgconfig/mutter-clutter-x11-0.pc
/usr/lib64/pkgconfig/mutter-cogl-0.pc
/usr/lib64/pkgconfig/mutter-cogl-pango-0.pc
/usr/lib64/pkgconfig/mutter-cogl-path-0.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmutter-0.so.0
/usr/lib64/libmutter-0.so.0.0.0
/usr/lib64/mutter/libmutter-clutter-0.so
/usr/lib64/mutter/libmutter-cogl-0.so
/usr/lib64/mutter/libmutter-cogl-pango-0.so
/usr/lib64/mutter/libmutter-cogl-path-0.so
/usr/lib64/mutter/plugins/default.so

%files locales -f mutter.lang
%defattr(-,root,root,-)

