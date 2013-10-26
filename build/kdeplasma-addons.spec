#This needs to be placed in macros
%define _kde4_services %_kde4_datadir/kde4/services
%define _kde4_servicetypes %_kde4_datadir/kde4/servicetypes

#Majors
%define plasmacomicprovidercore_major 1
%define plasmaweather_major 4
%define rtm_major 4
%define plasmapotdprovidercore_major 1
%define lancelot_datamodels_major 1
%define plasma_containments_grouping_major 4
%define lancelot_major 2

Name:           kdeplasma-addons
Summary:        Additional plasmoids for KDE
Version:        4.11.2
Release:        1%{dist}

License:        GPLv2+
Group:          User Interface/Desktops
URL:            http://www.kde.org/
Source0:        ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

## upstreamable patches

## upstream patches

BuildRequires:  boost-devel
BuildRequires:  gettext
BuildRequires:  kdepimlibs-devel >= %{version}
# for libplasmaclock
BuildRequires:  kde-workspace-devel >= %{version}
BuildRequires:  pkgconfig(eigen2)
BuildRequires:  marble-devel >= %{version}
BuildRequires:  pkgconfig(dbusmenu-qt)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libattica)
BuildRequires:  pkgconfig(libkexiv2) >= 0.4.0
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(qca2)
BuildRequires:  pkgconfig(qimageblitz)
# lancelot eye-candy
BuildRequires:  pkgconfig(xcomposite) pkgconfig(xdamage) pkgconfig(xrender)
BuildRequires:  qwt-devel

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

Requires: plasma-desktoptheme-default
Requires: plasma-applet-showdesktop
Requires: plasma-applet-comic
Requires: plasma-applet-konqprofiles
Requires: plasma-applet-rssnow
Requires: plasma-applet-previewer
Requires: plasma-applet-bball
Requires: plasma-applet-incomingmsg
Requires: plasma-applet-leavenote
Requires: plasma-applet-life
Requires: plasma-applet-konsoleprofiles
Requires: plasma-applet-luna
Requires: plasma-applet-lancelot
Requires: plasma-applet-microblog
Requires: plasma-applet-nowplaying
Requires: plasma-applet-binaryclock
Requires: plasma-applet-dict
Requires: plasma-applet-fuzzy-clock
Requires: plasma-applet-frame
Requires: plasma-applet-showdashboard
Requires: plasma-applet-calculator
Requires: plasma-applet-fifteenpuzzle
Requires: plasma-applet-kolourpicker
Requires: plasma-applet-unitconverter
Requires: plasma-applet-systemloadviewer
Requires: plasma-applet-weather
Requires: plasma-applet-bubblemon
Requires: plasma-applet-weatherstation
Requires: plasma-applet-news
Requires: plasma-applet-charselect
Requires: plasma-applet-eyes
Requires: plasma-applet-paste
Requires: plasma-applet-timer
Requires: plasma-applet-opendesktop
Requires: plasma-applet-magnifique
Requires: plasma-applet-mediaplayer
Requires: plasma-applet-rtm
Requires: plasma-applet-knowledgebase
Requires: plasma-applet-blackboard
Requires: plasma-applet-plasmaboard
Requires: plasma-applet-qalculate
Requires: plasma-applet-webslice
Requires: plasma-applet-spellcheck
Requires: plasma-applet-bookmarks
Requires: plasma-applet-kimpanel
Requires: plasma-applet-icontasks

Requires: plasma-runner-converter
Requires: plasma-runner-contacts
Requires: plasma-runner-konquerorsessions
Requires: plasma-runner-katesessions
Requires: plasma-runner-konsolesessions
Requires: plasma-runner-browserhistory
Requires: plasma-runner-spellchecker
Requires: plasma-runner-audioplayercontrol
Requires: plasma-runner-mediawiki
Requires: plasma-runner-kopete
Requires: plasma-runner-charrunner
Requires: plasma-runner-datetime
Requires: plasma-runner-events

Requires: plasma-wallpaper-pattern
Requires: plasma-wallpaper-weather
Requires: plasma-wallpaper-virus
Requires: plasma-wallpaper-mandelbrot
Requires: plasma-wallpaper-marble
Requires: plasma-wallpaper-potd

%description
This is a meta package for kdeplasma that is a compilation of plasma items ( runners, applets, plasmoids ) for kde4.

%files
%doc COPYING

#-----------------------------------------------------------------------------

%package -n plasma-applet-icontasks
Summary: Plasma icontasks applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-icontasks
Plasma icontasks applet.

%files -n plasma-applet-icontasks
%_kde4_libdir/kde4/plasma_applet_icontasks.so
%_kde4_services/plasma-applet-icontasks.desktop
%_kde4_appsdir/kdeplasma-addons/mediabuttonsrc
%_kde4_appsdir/desktoptheme/default/icontasks

#-----------------------------------------------------------------------------


%package -n plasma-applet-filewatcher
Summary: Monitor applet for files
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-filewatcher
Monitor applet for files.

%files -n plasma-applet-filewatcher

%_kde4_libdir/kde4/plasma_applet_fileWatcher.so
%_kde4_services/plasma-fileWatcher-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-bookmarks
Summary: Bookmark applet for KDE
Group: User Interface/Desktops
Requires: kdebase-runtime
Provides: plasma-applet

%description -n plasma-applet-bookmarks
This applet provides access to KDE's bookmark

%files -n plasma-applet-bookmarks

%_kde4_services/plasma-applet-bookmarks.desktop
%_kde4_libdir/kde4/plasma_applet_bookmarks.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-notes
Summary: Plasma notes applets
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-notes
Plasma notes applets.

%files -n plasma-applet-notes

%_kde4_libdir/kde4/plasma_applet_notes.so
%_kde4_services/plasma-notes-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-showdesktop
Summary: Show desktop contents
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-showdesktop
Show desktop contents.

%files -n plasma-applet-showdesktop

%_kde4_libdir/kde4/plasma_applet_showdesktop.so
%_kde4_services/plasma-applet-showdesktop.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-comic
Summary: Make your day happy with daily desktop comics applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine-comic = %{version}-%{release}
Requires: plasma-dataengine-comic = %version

%description -n plasma-applet-comic
Make your day happy with daily desktop comics applet

%files -n plasma-applet-comic
%_kde4_libdir/kde4/plasma_applet_comic.so
%_kde4_configdir/comic.knsrc
%_kde4_services/plasma-comic-default.desktop
%_kde4_appsdir/plasma/packages/org.kde.comic

#-----------------------------------------------------------------------------

%package -n plasma-applet-konqprofiles
Summary: Live konqueror profile viewer
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-konqprofiles
Live konqueror profile viewer.

%files -n plasma-applet-konqprofiles

%_kde4_libdir/kde4/plasma_engine_konqprofiles.so
%_kde4_services/plasma-applet-konqprofiles.desktop
%_kde4_services/plasma-dataengine-konqprofiles.desktop
%_kde4_appsdir/plasma/plasmoids/konqprofiles/contents/ui/konqprofiles.qml
%_kde4_appsdir/plasma/plasmoids/konqprofiles/metadata.desktop
%_kde4_appsdir/plasma/services/org.kde.plasma.dataengine.konqprofiles.operations

#-----------------------------------------------------------------------------

%package -n plasma-applet-rssnow
Summary: Plasma RSS Applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-rssnow
Plasma RSS Applet

%files -n plasma-applet-rssnow

%_kde4_libdir/kde4/plasma_applet_rssnow.so
%_kde4_appsdir/desktoptheme/default/rssnow
%_kde4_services/plasma-applet-rssnow.desktop
%_kde4_appsdir/rssnow

#-----------------------------------------------------------------------------

%package -n plasma-applet-previewer
Summary: Previewer Plasma Applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-previewer
Previewer Plasma Applet

%files -n plasma-applet-previewer

%_kde4_libdir/kde4/plasma_applet_previewer.so
%_kde4_iconsdir/hicolor/*/apps/previewer.png
%_kde4_services/ServiceMenus/preview.desktop
%_kde4_services/plasma-applet-previewer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-bball
Summary: bball Plasma Applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-bball
bball Plasma Applet

%files -n plasma-applet-bball

%_kde4_iconsdir/*/*/*/bball*
%_kde4_services/plasma-applet-bball.desktop
%_kde4_appsdir/bball
%_kde4_libdir/kde4/plasma_applet_bball.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-incomingmsg
Summary: incomingmsg Plasma Applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-incomingmsg
incomingmsg Plasma Applet

%files -n plasma-applet-incomingmsg

%_kde4_services/plasma-applet-incomingmsg.desktop
%_kde4_libdir/kde4/plasma_applet_incomingmsg.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-leavenote
Summary: Leave A Note
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-leavenote
Leave notes for users while they are away

%files -n plasma-applet-leavenote

%_kde4_libdir/kde4/plasma_applet_leavenote.so
%_kde4_services/plasma-applet-leavenote.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-life
Summary: life Plasma Applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-life
life Plasma Applet

%files -n plasma-applet-life

%_kde4_libdir/kde4/plasma_applet_life.so
%_kde4_services/plasma-applet-life.desktop
%_kde4_iconsdir/hicolor/*/apps/lifegame.*

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-kdeobservatory
Summary:  Engine of the kdeobservatory plasma applet
Group:    User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine

%description -n plasma-dataengine-kdeobservatory
Engine of the kdeobservatory plasma applet

%files -n plasma-dataengine-kdeobservatory

%_kde4_libdir/kde4/plasma_engine_kdeobservatory.so
%_kde4_appsdir/plasma/services/kdeobservatory.operations
%_kde4_services/plasma-engine-kdeobservatory.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-pastebin
Summary: Pastebin plasma Applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-pastebin
Paste text/images to a remote server

%files -n plasma-applet-pastebin

%_kde4_services/plasma-applet-pastebin.desktop
%_kde4_libdir/kde4/plasma_applet_pastebin.so
%_kde4_appsdir/plasma_pastebin
%_kde4_datadir/config/pastebin.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-applet-knowledgebase
Summary: Widget that can query the knowledgebase of opendesktop.org
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine-ocs
Requires: plasma-dataengine-ocs

%description -n plasma-applet-knowledgebase
Widget that can query the knowledgebase of opendesktop.org

%files -n plasma-applet-knowledgebase

%_kde4_libdir/kde4/plasma_applet_knowledgebase.so
%_kde4_services/plasma-applet-knowledgebase.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-blackboard
Summary: A blackboard plasma applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-blackboard
A blackboard plasma applet

%files -n plasma-applet-blackboard

%_kde4_libdir/kde4/plasma_applet_blackboard.so
%_kde4_services/plasma-applet-blackboard.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-plasmaboard
Summary: A plasmaboard plasma applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-plasmaboard
A virtual, on-screen keyboard

%files -n plasma-applet-plasmaboard

%_kde4_libdir/kde4/plasma_applet_plasmaboard.so
%_kde4_services/plasma_applet_plasmaboard.desktop
%_kde4_appsdir/plasmaboard

#-----------------------------------------------------------------------------

%package -n plasma-applet-konsoleprofiles
Summary: Live konsole profile viewer
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-konsoleprofiles
Live konsole profile viewer.

%files -n plasma-applet-konsoleprofiles

%_kde4_libdir/kde4/plasma_engine_konsoleprofiles.so
%_kde4_services/plasma-applet-konsoleprofiles.desktop
%_kde4_services/plasma-dataengine-konsoleprofiles.desktop
%_kde4_appsdir/plasma/plasmoids/konsoleprofiles/contents/ui/konsoleprofiles.qml
%_kde4_appsdir/plasma/plasmoids/konsoleprofiles/metadata.desktop
%_kde4_appsdir/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations

#-----------------------------------------------------------------------------

%package -n plasma-applet-luna
Summary: Lunar calendar
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-luna
Lunar calendar applet.

%files -n plasma-applet-luna

%_kde4_libdir/kde4/plasma_applet_luna.so
%_kde4_services/plasma-applet-luna.desktop
%_kde4_iconsdir/hicolor/*/apps/luna.png

#-----------------------------------------------------------------------------

%package -n plasma-applet-lancelot
Summary: Plasma lancelot applets
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-lancelot
Plasma lancelot applets.

%files -n plasma-applet-lancelot

%_kde4_bindir/lancelot
%_kde4_libdir/kde4/plasma_applet_lancelot_part.so
%_kde4_libdir/kde4/plasma_applet_lancelot_launcher.so
%_kde4_services/plasma-applet-lancelot-launcher.desktop
%_kde4_iconsdir/hicolor/*/apps/lancelot*.png
%_kde4_iconsdir/hicolor/*/apps/plasmaapplet-shelf.png
%_kde4_services/plasma-applet-lancelot-part.desktop
%_kde4_services/lancelot.desktop
%_kde4_datadir/mime/packages/lancelotpart-mime.xml
%_kde4_appsdir/desktoptheme/*/lancelot
%_kde4_appsdir/lancelot

#-----------------------------------------------------------------------------

%package -n lancelot-libs
Summary: %name library
Group: System/Libraries

%description -n lancelot-libs
%name library.

%post -n lancelot-libs -p /sbin/ldconfig
%postun -n lancelot-libs -p /sbin/ldconfig

%files -n lancelot-libs
%defattr(-,root,root,-)
%_kde4_libdir/liblancelot.so.*

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-default                                       
Summary: Plasma default desktopthemes                                         
Group: User Interface/Desktops                                                  
Requires: kde-workspace                                                  
                                                                              
%description -n plasma-desktoptheme-default                                   
Plasma default desktopthemes.                                                 
                                                                              
%files -n plasma-desktoptheme-default                                         
                                                         
%_kde4_appsdir/desktoptheme/default/widgets                                    
                                                                              
#-----------------------------------------------------------------------------

%package -n plasma-applet-microblog
Summary: Microblog applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine-microblog
Requires: plasma-dataengine-microblog = %version
Provides: plasma-applet-twitter = %version-%release

%description -n plasma-applet-microblog
Update and view your microblog status

%files -n plasma-applet-microblog

%_kde4_libdir/kde4/plasma_applet_microblog.so
%_kde4_services/plasma-applet-microblog.desktop
#%_kde4_appsdir/plasma/services/tweet.operations

#-----------------------------------------------------------------------------

%package -n plasma-applet-nowplaying
Summary: SWoong notifier applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-nowplaying
Song notifier applet

%files -n plasma-applet-nowplaying
%_kde4_appsdir/plasma/plasmoids/nowplaying
%_kde4_services/plasma-applet-nowplaying.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-binaryclock
Summary: Simplified way to see the hours
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-binaryclock
Simplified way to see the hours.

%files -n plasma-applet-binaryclock

%_kde4_libdir/kde4/plasma_applet_binaryclock.so
%_kde4_services/plasma-applet-binaryclock.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-dict
Summary: Dict applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-dict
A dict applets.

%files -n plasma-applet-dict

%_kde4_libdir/kde4/plasma_applet_dict.so
%_kde4_services/plasma-dict-default.desktop
%_kde4_iconsdir/hicolor/scalable/apps/accessories-dict*

#-----------------------------------------------------------------------------

%package -n plasma-applet-fuzzy-clock
Summary: A lazy way to see the hours
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-fuzzy-clock
A lazy way to see the hours.

%files -n plasma-applet-fuzzy-clock

%_kde4_libdir/kde4/plasma_applet_fuzzy_clock.so
%_kde4_services/plasma-clock-fuzzy.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-frame
Summary: A basic pictures frame to desktop
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-frame
A basic pictures frame to desktop.

%files -n plasma-applet-frame

%_kde4_libdir/kde4/plasma_applet_frame.so
%_kde4_services/plasma-frame-default.desktop
%_kde4_appsdir/plasma-applet-frame

#-----------------------------------------------------------------------------

%package -n plasma-applet-showdashboard
Summary: Plasma showdashboard applets
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-showdashboard
Plasma showdashboard applets.

%files -n plasma-applet-showdashboard

%_kde4_libdir/kde4/plasma_applet_showdashboard.so
%_kde4_services/plasma-applet-showdashboard.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-calculator
Summary: Plasma calculator applets
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-calculator
Plasma calculator applets.

%files -n plasma-applet-calculator
%_kde4_appsdir/plasma/plasmoids/calculator
%_kde4_services/plasma-applet-calculator.desktop


#-----------------------------------------------------------------------------

%package -n plasma-applet-fifteenpuzzle
Summary: Plasma fifteenpuzzle applets
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-fifteenpuzzle
Plasma fifteenpuzzle applets.

%files -n plasma-applet-fifteenpuzzle

%_kde4_libdir/kde4/plasma_applet_fifteenPuzzle.so
%_kde4_services/plasma-applet-fifteenPuzzle.desktop
%_kde4_appsdir/desktoptheme/default/fifteenPuzzle
%_kde4_iconsdir/*/*/*/fifteenpuzzle.*

#-----------------------------------------------------------------------------

%package -n plasma-applet-kolourpicker
Summary: Basic color picker
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-kolourpicker
Basic color picker.

%files -n plasma-applet-kolourpicker

%_kde4_libdir/kde4/plasma_applet_kolourpicker.so
%_kde4_services/plasma-kolourpicker-default.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-unitconverter
Summary: Unit Converter
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-unitconverter
Unit Converter.

%files -n plasma-applet-unitconverter

%_kde4_libdir/kde4/plasma_applet_unitconverter.so
%_kde4_services/plasma-applet-unitconverter.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-systemloadviewer
Summary: System Load Viewer
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-systemloadviewer
System Load Viewer.

%files -n plasma-applet-systemloadviewer

%_kde4_libdir/kde4/plasma-applet_systemloadviewer.so
%_kde4_services/plasma-applet-systemloadviewer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-weather
Summary: Weather Forecast
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-weather
Weather Forecast.

%files -n plasma-applet-weather
%_kde4_libdir/kde4/plasma_applet_weather.so
%_kde4_services/plasma-applet-weather.desktop
%_kde4_appsdir/desktoptheme/default/weather/wind-arrows.svgz
%_kde4_appsdir/plasma/packages/org.kde.weather/

#-----------------------------------------------------------------------------

%package -n plasma-applet-bubblemon
Summary: Monitor your system
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-bubblemon
A pretty bubble that monitors your system.

%files -n plasma-applet-bubblemon

%_kde4_libdir/kde4/plasma_applet_bubblemon.so
%_kde4_services/plasma-applet-bubblemon.desktop
%_kde4_appsdir/desktoptheme/default/bubblemon/bubble.svg

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-comic
Summary: Plasma comic dataengines
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine

%description -n plasma-dataengine-comic
Plasma comic dataengines.

%files -n plasma-dataengine-comic
%_kde4_libdir/kde4/plasma_comic_krossprovider.so
%_kde4_libdir/kde4/plasma_engine_comic.so
%_kde4_libdir/kde4/plasma_packagestructure_comic.so
%_kde4_services/plasma-dataengine-comic.desktop
%_kde4_services/plasma-packagestructure-comic.desktop
%_kde4_servicetypes/plasma_comicprovider.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-rtm
Summary: An engine to work with Remember the Milk
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine
Provides: plasma-dataengine-rememberthemilk = %{version}-%{release}
Requires: plasma-dataengine-rtm = %version-%release

%description -n plasma-dataengine-rtm
An engine to work with Remember the Milk.

%files -n plasma-dataengine-rtm

%{_kde4_libdir}/kde4/plasma_engine_rtm.so
%{_kde4_services}/plasma-engine-rtm.desktop
%{_kde4_appsdir}/plasma/services/rtmauth.operations
%{_kde4_appsdir}/plasma/services/rtmtask.operations
%{_kde4_appsdir}/plasma/services/rtmtasks.operations

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-ocs
Summary: Open Collaboration Services
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine
Requires: plasma-dataengine-ocs = %version-%release

%description -n plasma-dataengine-ocs
Open Collaboration Services.

%files -n plasma-dataengine-ocs

%{_kde4_libdir}/kde4/plasma_engine_ocs.so
%{_kde4_services}/plasma-dataengine-ocs.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-potd
Summary: Picture of the Day
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine
Provides: plasma-dataengine-potd
Requires: plasma-dataengine-potd = %version-%release

%description -n plasma-dataengine-potd
Data Engine for getting various online Pictures of The Day.


%files -n plasma-dataengine-potd
%_kde4_libdir/kde4/plasma_potd_apodprovider.so
%_kde4_libdir/kde4/plasma_potd_epodprovider.so
%_kde4_libdir/kde4/plasma_potd_flickrprovider.so
%_kde4_libdir/kde4/plasma_potd_oseiprovider.so
%_kde4_libdir/kde4/plasma_potd_wcpotdprovider.so
%_kde4_libdir/kde4/plasma_engine_potd.so
%_kde4_libdir/kde4/plasma_potd_natgeoprovider.so
%_kde4_services/natgeoprovider.desktop
%_kde4_services/plasma-dataengine-potd.desktop
%_kde4_services/apodprovider.desktop
%_kde4_services/epodprovider.desktop
%_kde4_services/flickrprovider.desktop
%_kde4_services/oseiprovider.desktop
%_kde4_services/wcpotdprovider.desktop
%_kde4_servicetypes/plasma_potdprovider.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-converter
Summary: Plasma converter runners
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-converter
Plasma converter runners.

%files -n plasma-runner-converter

%_kde4_services/plasma-runner-converter.desktop
%_kde4_libdir/kde4/krunner_converter.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-charrunner
Summary: Plasma charrunner runners
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-charrunner
Plasma charrunner runners.

%files -n plasma-runner-charrunner

%_kde4_libdir/kde4/kcm_krunner_charrunner.so
%_kde4_libdir/kde4/krunner_charrunner.so
%_kde4_services/CharRunner_config.desktop
%_kde4_services/CharacterRunner.desktop


#-----------------------------------------------------------------------------

%package -n plasma-runner-datetime
Summary: Plasma charrunner runners
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-datetime
Plasma datetime runners.

%files -n plasma-runner-datetime

%_kde4_libdir/kde4/plasma_runner_datetime.so
%_kde4_services/plasma-runner-datetime.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-dictionary
Summary: Plasma charrunner runners
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-runner

%description -n plasma-runner-dictionary
Plasma datetime runners.

%files -n plasma-runner-dictionary
%_kde4_libdir/kde4/kcm_krunner_dictionary.so
%_kde4_libdir/kde4/krunner_dictionary.so
%_kde4_services/plasma-runner-dictionary.desktop
%_kde4_services/plasma-runner-dictionary_config.desktop

#------------------------------------------------------------------------------

%package -n plasma-runner-contacts
Summary: Plasma contacts runners
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-contacts
Plasma contacts runners.

%files -n plasma-runner-contacts

%_kde4_libdir/kde4/krunner_contacts.so
%_kde4_services/plasma-runner-contacts.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-events
Summary: Plasma events runners
Group: User Interface/Desktops
Requires: kde-workspace
Provides:  plasma-runner-events
Provides: plasma-runner

%description -n plasma-runner-events
Plasma events runners.

%files -n plasma-runner-events

%_kde4_libdir/kde4/plasma_runner_events.so
%_kde4_libdir/kde4/kcm_plasma_runner_events.so
%_kde4_services/plasma-runner-events_config.desktop
%_kde4_services/plasma-runner-events.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-weatherstation
Summary: Plasma applet weatherstation
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-weatherstation
Plasma applet weatherstation

%files -n plasma-applet-weatherstation
%_kde4_libdir/kde4/plasma_applet_weatherstation.so
%_kde4_appsdir/desktoptheme/default/weatherstation
%_kde4_appsdir/plasma/packages/org.kde.lcdweather/
%_kde4_services/plasma-applet-weatherstation.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-news
Summary: Plasma applet news
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-news
Plasma applet news

%files -n plasma-applet-news

%_kde4_services/plasma-applet-news.desktop
%_kde4_libdir/kde4/plasma_applet_news.so
%_kde4_appsdir/desktoptheme/default/stylesheets/news.css

#-----------------------------------------------------------------------------

%package -n plasma-applet-charselect
Summary: Plasma applet charselect
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-charselect
Plasma applet charselect

%files -n plasma-applet-charselect

%_kde4_services/plasma-applet-charselect.desktop
%_kde4_libdir/kde4/plasma_applet_charselect.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-eyes
Summary: Plasma applet paste
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-eyes
Plasma applet eyes

%files -n plasma-applet-eyes

%_kde4_libdir/kde4/plasma_applet_eyes.so                                                                                       
%_kde4_services/plasma-applet-eyes.desktop
%_kde4_iconsdir/hicolor/*/apps/eyes.*

#-----------------------------------------------------------------------------

%package -n plasma-applet-paste
Summary: Plasma applet paste
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-paste
Plasma applet paste

%files -n plasma-applet-paste

%_kde4_libdir/kde4/plasma_applet_paste.so                                                                                      
%_kde4_services/plasma-applet-paste.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-timer
Summary: Plasma applet timer
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-timer
Plasma applet timer

%files -n plasma-applet-timer

%_kde4_libdir/kde4/plasma_applet_timer.so
%_kde4_services/plasma-applet-timer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-opendesktop
Summary: Communicate using the Social Desktop
Group: User Interface/Desktops
Requires: kde-workspace
Requires: plasma-dataengine-ocs
Provides: plasma-applet

%description -n plasma-applet-opendesktop
Communicate using the Social Desktop.

%files -n plasma-applet-opendesktop

%_kde4_libdir/kde4/plasma_applet_opendesktop.so
%_kde4_services/plasma-applet-opendesktop.desktop
%_kde4_libdir/kde4/plasma_applet_opendesktop_activities.so
%_kde4_appsdir/plasma-applet-opendesktop-activities/plasma-applet-opendesktop-activities.notifyrc
%_kde4_appsdir/plasma/services/ocsPerson.operations
%_kde4_datadir/kde4/services/plasma-applet-opendesktop-activities.desktop
%_kde4_appsdir/plasma-applet-opendesktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-magnifique
Summary: A magnification glass for Plasma canvas
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-magnifique
A magnification glass for Plasma canvas.

%files -n plasma-applet-magnifique

%_kde4_libdir/kde4/plasma_applet_magnifique.so
%_kde4_services/plasma-applet-magnifique.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-qalculate
Summary: A Qalculate plasma applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-qalculate
A Qalculate plasma applet

%files -n plasma-applet-qalculate

%_kde4_libdir/kde4/plasma_applet_qalculate.so
%_kde4_datadir/kde4/services/plasma-applet-qalculate.desktop
%_kde4_iconsdir/hicolor/*/apps/qalculate-applet.png

#-----------------------------------------------------------------------------

%package -n plasma-applet-mediaplayer
Summary: Widget that can play video and sound
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-mediaplayer
Widget that can play video and sound.

%files -n plasma-applet-mediaplayer

%_kde4_libdir/kde4/plasma_applet_mediaplayer.so
%_kde4_services/plasma-applet-mediaplayer.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-spellcheck
Summary:  Fast spell checking applet
Group:    User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-spellcheck
Fast spell checking applet

%files -n plasma-applet-spellcheck

%_kde4_libdir/kde4/plasma_applet_spellcheck.so
%_kde4_services/plasma-applet-spellcheck.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-webslice
Summary:  Applet that show a part of a webpage
Group:    User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet

%description -n plasma-applet-webslice
Applet that show a part of a webpage

%files -n plasma-applet-webslice

%_kde4_services/plasma-applet-webslice.desktop
%_kde4_libdir/kde4/plasma_applet_webslice.so

#-----------------------------------------------------------------------------

%package -n plasma-applet-rtm
Summary: Remember The Milk Todo list applet
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet
Provides: plasma-applet-rememberthemilk = %{version}-%{release}
Requires: plasma-dataengine-rtm = %{version}

%description -n plasma-applet-rtm
Remember The Milk Todo list applet.

%files -n plasma-applet-rtm

%_kde4_libdir/kde4/plasma_applet_rtm.so
%_kde4_services/plasma-applet-rememberthemilk.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-konquerorsessions
Summary: Plasma applet places
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-konquerorsessions
Plasma runner konquerorsessions

%files -n plasma-runner-konquerorsessions

%_kde4_services/konquerorsessions.desktop
%_kde4_libdir/kde4/krunner_konquerorsessions.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-katesessions
Summary: Plasma katesessions runner
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-katesessions
Plasma runner katesessions

%files -n plasma-runner-katesessions

%_kde4_services/katesessions.desktop
%_kde4_libdir/kde4/krunner_katesessions.so


#-----------------------------------------------------------------------------

%package -n plasma-runner-konsolesessions
Summary: Plasma runner konsolesessions
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-konsolesessions
Plasma runner konsolesessions

%files -n plasma-runner-konsolesessions

%_kde4_services/konsolesessions.desktop
%_kde4_libdir/kde4/krunner_konsolesessions.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-browserhistory
Summary: Plasma runner browserhistory
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-browserhistory
Plasma runner konsolesessions

%files -n plasma-runner-browserhistory

%_kde4_libdir/kde4/krunner_browserhistory.so
%_kde4_services/browserhistory.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-spellchecker
Summary: Plasma runner spellchecker
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-spellchecker
Plasma runner konsolesessions

%files -n plasma-runner-spellchecker

%_kde4_services/plasma-runner-spellchecker.desktop
%_kde4_services/plasma-runner-spellchecker_config.desktop
%_kde4_libdir/kde4/krunner_spellcheckrunner.so
%_kde4_libdir/kde4/kcm_krunner_spellcheck.so

#-----------------------------------------------------------------------------

%package -n plasma-runner-audioplayercontrol
Summary: Plasma runner audioplayercontrol
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-audioplayercontrol
Plasma runner audioplayercontrol

%files -n plasma-runner-audioplayercontrol

%_kde4_libdir/kde4/kcm_krunner_audioplayercontrol.so
%_kde4_libdir/kde4/krunner_audioplayercontrol.so
%_kde4_datadir/kde4/services/plasma-runner-audioplayercontrol.desktop
%_kde4_datadir/kde4/services/plasma-runner-audioplayercontrol_config.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-kopete
Summary: Plasma runner kopete
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-kopete
Plasma runner kopete

%files -n plasma-runner-kopete

%_kde4_libdir/kde4/krunner_kopete.so
%_kde4_datadir/kde4/services/plasma-runner-kopete.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-mediawiki
Summary: Plasma runner mediawiki
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-runner

%description -n plasma-runner-mediawiki
Plasma runner mediawiki

%files -n plasma-runner-mediawiki

%_kde4_libdir/kde4/krunner_mediawiki.so
%_kde4_datadir/kde4/services/plasma-runner-techbase.desktop
%_kde4_datadir/kde4/services/plasma-runner-wikipedia.desktop
%_kde4_datadir/kde4/services/plasma-runner-wikitravel.desktop

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-pattern
Summary: Pattern wallpaper
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-pattern
Pattern wallpaper.

%files -n plasma-wallpaper-pattern

%_kde4_libdir/kde4/plasma_wallpaper_pattern.so
%_kde4_services/plasma-wallpaper-pattern.desktop
%_kde4_appsdir/plasma_wallpaper_pattern

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-weather
Summary: Weather wallpaper
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-weather
Weather wallpaper.

%files -n plasma-wallpaper-weather

%_kde4_libdir/kde4/plasma_wallpaper_weather.so
%_kde4_services/plasma-wallpaper-weather.desktop
%_kde4_datadir/config/plasmaweather.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-virus
Summary: Virus wallpaper
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-virus
Virus wallpaper.

%files -n plasma-wallpaper-virus

%_kde4_libdir/kde4/plasma_wallpaper_virus.so
%_kde4_services/plasma-wallpaper-virus.desktop
%_kde4_configdir/virus_wallpaper.knsrc

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-marble
Summary: Marble wallpaper
Group: User Interface/Desktops
Requires: kde-workspace
Requires: marble-libs
Provides: plasma-wallpaper

%description -n plasma-wallpaper-marble
+Marble wallpaper.

%files -n plasma-wallpaper-marble

%_kde4_libdir/kde4/plasma_wallpaper_marble.so
%_kde4_services/plasma-wallpaper-marble.desktop

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-mandelbrot
Summary: Mandelbrot wallpaper
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-mandelbrot
Mandelbrot wallpaper.

%files -n plasma-wallpaper-mandelbrot

%_kde4_libdir/kde4/plasma_wallpaper_mandelbrot.so
%_kde4_services/plasma-wallpaper-mandelbrot.desktop

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-qml
Summary: Animated Wallpaper
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-qml
Animated Wallpaper

%files -n plasma-wallpaper-qml
%_kde4_libdir/kde4/plasma_wallpaper_qml.so
%_kde4_appsdir/plasma/wallpapers/org.kde.animals/
%_kde4_appsdir/plasma/wallpapers/org.kde.haenau/
%_kde4_appsdir/plasma/wallpapers/org.kde.hunyango/
%_kde4_services/plasma-wallpaper-qml.desktop

#------------------------------------------------------------------------------

%package -n plasma-dataengine-comic-libs
Summary: %name library
Group: System/Libraries

%description -n plasma-dataengine-comic-libs
%name library.

%files -n plasma-dataengine-comic-libs
%defattr(-,root,root,-)
%_kde4_libdir/libplasmacomicprovidercore.so.%{plasmacomicprovidercore_major}*

#-----------------------------------------------------------------------------

%package -n plasma-weather-libs
Summary: %name library
Group: System/Libraries

%description -n plasma-weather-libs
%name library.

%files -n plasma-weather-libs
%defattr(-,root,root,-)
%_kde4_libdir/libplasmaweather.so.%{plasmaweather_major}*

#-----------------------------------------------------------------------------

%package -n plasma-rtm-libs
Summary: %name library
Group: System/Libraries

%description -n plasma-rtm-libs
%name library.

%files -n plasma-rtm-libs
%defattr(-,root,root,-)
%_kde4_libdir/librtm.so.%{rtm_major}*

#-----------------------------------------------------------------------------

%package -n plasma-potd-providercore-libs
Summary: %name library
Group: System/Libraries

%description -n plasma-potd-providercore-libs
%name library.

%files -n plasma-potd-providercore-libs
%_kde4_libdir/libplasmapotdprovidercore.so.%{plasmapotdprovidercore_major}*

#-----------------------------------------------------------------------------

%package -n lancelot-datamodels-libs
Summary: %name library
Group: System/Libraries

%description -n lancelot-datamodels-libs
%name library.

%files -n lancelot-datamodels-libs
%defattr(-,root,root,-)
%_kde4_libdir/liblancelot-datamodels.so.%{lancelot_datamodels_major}
%_kde4_libdir/liblancelot-datamodels.so.%{lancelot_datamodels_major}.*

#-----------------------------------------------------------------------------

%package -n plasma-containments-grouping-libs
Summary: %name library
Group: System/Libraries

%description -n plasma-containments-grouping-libs
%name library.

%files -n plasma-containments-grouping-libs
%defattr(-,root,root,-)
%_kde4_libdir/libplasma_groupingcontainment.so.%{plasma_containments_grouping_major}*

#------------------------------------------------------------------------------

%package -n plasma-applet-kimpanel
Summary: KDE Input method panel (applet) 
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-applet
Requires: plasma-dataengine-kimpanel

%description -n plasma-applet-kimpanel
KDE Input method panel (applet)

%files -n plasma-applet-kimpanel
%_kde4_libdir/kde4/plasma_applet_kimpanel.so
%_kde4_datadir/config.kcfg/kimpanelconfig.kcfg
%_kde4_services/plasma-applet-kimpanel.desktop

#-----------------------------------------------------------------------------

%package -n plasma-dataengine-kimpanel
Summary:  Engine of the kimpanel plasma applet
Group:    User Interface/Desktops
Requires: kde-workspace
Provides: plasma-dataengine

%description -n plasma-dataengine-kimpanel
Engine of the kimpanel plasma applet

%files -n plasma-dataengine-kimpanel
%_kde4_libdir/kde4/plasma_engine_kimpanel.so
%_kde4_appsdir/plasma/services/kimpanel.operations
%_kde4_services/plasma-dataengine-kimpanel.desktop
/usr/libexec/kde4/kimpanel-ibus-panel

#-----------------------------------------------------------------------------

%package -n plasma-wallpaper-potd   
Summary: Potd wallpaper
Group: User Interface/Desktops
Requires: kde-workspace
Provides: plasma-wallpaper

%description -n plasma-wallpaper-potd     
Potd wallpaper.   

%files -n plasma-wallpaper-potd
%_kde4_libdir/kde4/plasma_wallpaper_potd.so
%_kde4_services/plasma-wallpaper-potd.desktop

#-----------------------------------------------------------------------------

%package -n plasma-containments-grouping
Summary: Containments that do widget grouping and gridding
Group: User Interface/Desktops

%description -n plasma-containments-grouping
This little project will provide the user the ability to layout his
applets in a more advanced way: He will be able to group them inside
special QGraphicsWidgets called Groups, in a way that depends on the
specific group.


%files -n plasma-containments-grouping
%defattr(-,root,root,-)
%_kde4_libdir/kde4/plasma_containment_groupingdesktop.so
%_kde4_libdir/kde4/plasma_containment_groupingpanel.so
%_kde4_libdir/kde4/plasma_containment_griddesktop.so
%_kde4_services/plasma-containment-griddesktop.desktop
%_kde4_services/plasma-containment-groupingdesktop.desktop
%_kde4_services/plasma-containment-groupingpanel.desktop

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: plasma-dataengine-comic-libs = %version
Requires: plasma-weather-libs = %version
Requires: plasma-rtm-libs = %version
Requires: plasma-potd-providercore-libs = %version
Requires: lancelot-libs = %version
Requires: plasma-applet-kimpanel = %version
Requires: kdelibs-devel
Obsoletes: extragear-plasma-devel

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel

%{_kde4_libdir}/*.so
%_kde4_includedir/lancelot
%_kde4_includedir/KDE/Lancelot
%_kde4_includedir/lancelot-datamodels
%_kde4_appsdir/cmake/modules/FindLancelot-Datamodels.cmake
%_kde4_appsdir/cmake/modules/FindLancelot.cmake

#-----------------------------------------------------------------------------

%prep
%setup -qn %name-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

## unpackaged files
rm -f %{buildroot}%{_kde4_libdir}/lib{plasma*,rtm}.so


%clean
rm -rf %{buildroot}

%changelog
* Thu Oct 17 2013 JMiahMan <JMiahMan at gmail dot com> - 4.11.2-1
- Import into my test korora repo
- Update to 4.11.2
- Added missing packages and remove obsolete packages from 4.9.1+

* Thu Sep 06 2012  BuildBot < BUILDBOT@synergy-linux.com> 4.9.1-1
- Update to version 4.9.1

* Sun Jun 17 2012 JMiahMan <JMiahMan at gmail dot com> - 4.8.4-1
- Update to 4.8.4

* Thu Apr 26 2012 JMiahMan <JMiahMan at gmail dot com> - 4.8.2-1
- Update 4.8.2

* Fri Dec 09 2011 JMiahMan <JMiahMan at gmail dot com> - 4.7.90-2
- Import into Synergy Linux

